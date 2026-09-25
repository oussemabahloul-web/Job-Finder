#!/usr/bin/env python3
"""Collect public search evidence for eligible organizations.

This is an intentionally conservative discovery pass.  It records search-result
URLs, titles and snippets; a later enrichment pass decides whether the evidence
is strong enough to mark a recruiter, junior policy or application channel as
verified.  Results are cached incrementally so interrupted batches can resume.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "job_research" / "company_research.csv"
CACHE = ROOT / "job_research" / "search_cache_bing.jsonl"
SEARCH_URL = "https://www.bing.com/search?format=rss&setlang=en-US&q="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def clean_markup(value: str) -> str:
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def parse_results(document: str) -> list[dict[str, str]]:
    root = ET.fromstring(document)
    results: list[dict[str, str]] = []
    for item in root.findall(".//item")[:10]:
        results.append(
            {
                "url": (item.findtext("link") or "").strip(),
                "title": clean_markup(item.findtext("title") or ""),
                "snippet": clean_markup(item.findtext("description") or ""),
            }
        )
    return results


def search(query: str, retries: int = 3) -> list[dict[str, str]]:
    url = SEARCH_URL + urllib.parse.quote(query)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "fr,en;q=0.8"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                body = response.read().decode("utf-8", errors="replace")
            return parse_results(body)
        except (urllib.error.URLError, TimeoutError, ET.ParseError) as exc:
            if attempt + 1 == retries:
                return [{"url": "", "title": "SEARCH_ERROR", "snippet": str(exc)}]
            time.sleep(2 ** attempt)
    return []


def existing_keys() -> set[str]:
    if not CACHE.exists():
        return set()
    keys: set[str] = set()
    with CACHE.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                keys.add(json.loads(line)["organization_key"])
            except (json.JSONDecodeError, KeyError):
                continue
    return keys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--delay", type=float, default=0.8)
    args = parser.parse_args()

    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["eligible"] == "Oui"]
    done = existing_keys()
    pending = [row for row in rows if row["organization_key"] not in done]
    selected = pending[args.start : args.start + args.limit]
    CACHE.parent.mkdir(parents=True, exist_ok=True)

    with CACHE.open("a", encoding="utf-8") as output:
        for index, row in enumerate(selected, start=1):
            name = row["organization_name"]
            location = row["country"] if row["location_status"] == "Étranger" else "Tunisie"
            general_query = f'"{name}" {location} careers jobs junior'
            contact_query = f'"{name}" {location} recruiter LinkedIn email'
            general = search(general_query)
            time.sleep(args.delay)
            contacts = search(contact_query)
            payload = {
                "organization_key": row["organization_key"],
                "organization_name": name,
                "searched_on": date.today().isoformat(),
                "general_query": general_query,
                "general_results": general,
                "contact_query": contact_query,
                "contact_results": contacts,
            }
            output.write(json.dumps(payload, ensure_ascii=False) + "\n")
            output.flush()
            print(f"[{index}/{len(selected)}] {name}: general={len(general)} contacts={len(contacts)}", flush=True)
            time.sleep(args.delay)

    print(f"Cached organizations: {len(existing_keys())}")
    print(f"Remaining organizations: {max(0, len(rows) - len(existing_keys()))}")


if __name__ == "__main__":
    main()
