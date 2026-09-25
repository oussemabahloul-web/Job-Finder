#!/usr/bin/env python3
"""Collect mobility/visa evidence for every foreign organization."""

from __future__ import annotations

import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

from collect_search_results import search

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "job_research" / "foreign_companies" / "company_research.csv"
CACHE = ROOT / "job_research" / "foreign_mobility_cache.jsonl"


def completed() -> set[str]:
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


with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))

done = completed()
pending = [row for row in rows if row["organization_key"] not in done]
with CACHE.open("a", encoding="utf-8") as output:
    for index, row in enumerate(pending, start=1):
        query = f'"{row["organization_name"]}" {row["country"]} visa sponsorship relocation work permit careers'
        results = search(query)
        output.write(json.dumps({
            "organization_key": row["organization_key"],
            "organization_name": row["organization_name"],
            "searched_on": date.today().isoformat(),
            "query": query,
            "results": results,
        }, ensure_ascii=False) + "\n")
        output.flush()
        print(f"[{index}/{len(pending)}] {row['organization_name']}: results={len(results)}", flush=True)
        time.sleep(0.1)

print(f"Cached foreign organizations: {len(completed())}")
