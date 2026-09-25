#!/usr/bin/env python3
"""Create a conservative baseline for every still-unresearched eligible company.

This pass uses the search caches collected on 2026-09-25.  It deliberately
does not call an old search result an active vacancy and does not promote a
source email to "verified" unless that exact address is visible in a public
search result.  Manually researched batches 01+ sort after this batch and
therefore remain authoritative.
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "job_research" / "company_research.csv"
FOREIGN = ROOT / "job_research" / "foreign_companies" / "company_research.csv"
CACHE = ROOT / "job_research" / "search_cache_bing.jsonl"
OUT = ROOT / "job_research" / "verified_batches" / "batch_2026_09_25_00_bulk.csv"
NO_EMAIL = "Aucun email public vérifié"
MISSING = "Non trouvé/non vérifiable"


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def load_cache() -> dict[str, dict]:
    found: dict[str, dict] = {}
    if CACHE.exists():
        for line in CACHE.read_text(encoding="utf-8").splitlines():
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            found[item.get("organization_key", "")] = item
    return found


def useful_results(item: dict) -> list[dict[str, str]]:
    seen: set[str] = set()
    results: list[dict[str, str]] = []
    for bucket in ("general_results", "contact_results"):
        for result in item.get(bucket, []):
            url = result.get("url", "").strip()
            if not url or url in seen or result.get("title") == "SEARCH_ERROR":
                continue
            seen.add(url)
            results.append(result)
    return results


def relevant(result: dict[str, str], company: str) -> bool:
    text = norm(" ".join((result.get("title", ""), result.get("snippet", ""), result.get("url", ""))))
    tokens = [token for token in norm(company).split() if len(token) >= 4 and token not in {"group", "groupe", "software", "consulting", "technologies", "technology"}]
    return bool(tokens) and any(token in text for token in tokens[:4])


def select_sources(results: list[dict[str, str]], company: str) -> list[str]:
    selected: list[str] = []
    for result in results:
        url = result.get("url", "")
        host = urlparse(url).netloc.casefold()
        if not relevant(result, company):
            continue
        if any(bad in host for bad in ("wikipedia.org", "facebook.com", "instagram.com", "youtube.com")):
            continue
        selected.append(url)
        if len(selected) == 4:
            break
    return selected


def select_channel(results: list[dict[str, str]], company: str) -> str:
    relevant_results = [r for r in results if relevant(r, company)]
    for result in relevant_results:
        url = result.get("url", "")
        low = url.casefold()
        if any(word in low for word in ("/careers", "/career", "/jobs", "/job/", "/recruit")):
            return url
    for result in relevant_results:
        url = result.get("url", "")
        if "linkedin.com/company/" in url.casefold():
            return url
    for result in relevant_results:
        url = result.get("url", "")
        host = urlparse(url).netloc.casefold()
        if host and not any(bad in host for bad in ("wikipedia", "facebook", "instagram", "youtube", "signalhire", "zoominfo")):
            return url
    return MISSING


def exact_public_email(row: dict[str, str], results: list[dict[str, str]]) -> str:
    corpus = " ".join(
        f"{r.get('title', '')} {r.get('snippet', '')} {r.get('url', '')}" for r in results
    ).casefold()
    for address in [part.strip() for part in row.get("source_emails", "").split("|")]:
        if address and address.casefold() in corpus:
            return address
    return NO_EMAIL


def junior_evidence(results: list[dict[str, str]], company: str) -> tuple[str, str]:
    markers = r"\b(junior|internship|intern|graduate|entry level|stage|stagiaire|pfe|apprentice|alternance|debutant)\b"
    for result in results:
        text = f"{result.get('title', '')} {result.get('snippet', '')}"
        if relevant(result, company) and re.search(markers, norm(text)):
            return (
                "Possible — signal public, actualité à confirmer",
                f"Un résultat public mentionne un parcours junior/stage, sans preuve suffisante qu'il soit encore ouvert : {result.get('url', '')}",
            )
    return (
        "Non vérifiable",
        "Aucune preuve publique suffisamment récente d’un recrutement junior n’a été identifiée dans les résultats consultés.",
    )


def linkedin_person(results: list[dict[str, str]], company: str) -> tuple[str, str]:
    role_words = r"\b(recruiter|recrut|talent|human resources|ressources humaines| hr |people partner)\b"
    for result in results:
        url = result.get("url", "")
        title = result.get("title", "")
        text = f" {norm(title + ' ' + result.get('snippet', ''))} "
        if "/in/" in url and relevant(result, company) and re.search(role_words, text):
            name = re.split(r"\s[-|–]\s| \| ", title, maxsplit=1)[0].strip()
            return name or MISSING, url
    return MISSING, MISSING


def make_email(row: dict[str, str]) -> tuple[str, str, str, str]:
    name = row["organization_name"]
    fintech = row["recommended_cv"].startswith("CV_ATS_Fintech")
    english = row["recommended_cv"].endswith("_EN.pdf") or row.get("language", "").casefold().startswith("ang") or row.get("language") == "en"
    if english:
        subject = f"Spontaneous Application — Junior AI / Software Engineer — Mohamed Oussema Bahloul"
        focus = "financial technology and data-driven services" if fintech else "software engineering, data and applied AI"
        body = (
            f"Dear {name} Recruitment Team,\n\n"
            "I am a recent Computer Engineering graduate from ENSI in Tunisia, specialised in Financial Engineering, and I would like to submit a spontaneous application for a junior opportunity aligned with my background.\n\n"
            "During my final-year project at Linedata, I helped modernise a financial software product using AI agents. This experience taught me how to understand a business need, turn it into an intelligent workflow and integrate it into an existing product. My background includes Python, Java, C++, full-stack development, APIs, SQL and databases, machine learning, LLMs and RAG.\n\n"
            f"I am interested in {name} because of its work in {focus}. I am looking for a team where I can learn quickly, take ownership progressively and use technology to create measurable value for users and the business.\n\n"
            "I have not found a currently open junior vacancy that I can confirm, so I am contacting you transparently as a spontaneous candidate for a present or future need. My CV is attached, and I would be pleased to discuss any suitable opportunity.\n\n"
            "Kind regards,\nMohamed Oussema Bahloul"
        )
        invitation = f"Hello, I am a recent ENSI Computer Engineering graduate specialised in Financial Engineering. My Linedata project combined AI agents and product modernisation. I am interested in future junior AI, Data or Software opportunities at {name}. Glad to connect."
        followup = f"Thank you for connecting. I am exploring junior AI, Data and Software opportunities at {name}. I have not treated any old vacancy as active; my spontaneous application highlights my Linedata AI-agent project, software skills and ability to connect technology with business value. Could you please direct me to the appropriate hiring contact?"
    else:
        subject = "Candidature spontanée — Ingénieur informatique junior — Mohamed Oussema Bahloul"
        focus = "la FinTech, la Data et la modernisation des services financiers" if fintech else "le développement logiciel, la Data et l’intelligence artificielle appliquée"
        body = (
            f"Bonjour,\n\nRécemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, je souhaite proposer ma candidature spontanée à {name} pour une première opportunité correspondant à mon profil.\n\n"
            "Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. Cette expérience m’a appris à comprendre un besoin métier, le traduire en workflows intelligents puis contribuer à son intégration dans un produit existant. Je maîtrise Python, Java, C++, le développement full-stack, les APIs, SQL et les bases de données, le machine learning, les LLM et les architectures RAG.\n\n"
            f"Je m’intéresse à {name} pour ses activités autour de {focus}. Je recherche un environnement où je pourrai apprendre rapidement, prendre progressivement des responsabilités et utiliser la technologie pour créer une valeur concrète.\n\n"
            "N’ayant pas trouvé d’offre junior actuellement ouverte que je puisse confirmer, je vous contacte en toute transparence dans le cadre d’une candidature spontanée pour un besoin présent ou futur. Je joins mon CV et serais ravi d’échanger avec vous.\n\n"
            "Bien cordialement,\nMohamed Oussema Bahloul"
        )
        invitation = f"Bonjour, récemment diplômé ingénieur ENSI et spécialisé en ingénierie financière, j’ai réalisé chez Linedata un PFE sur des agents IA. Je m’intéresse aux futurs besoins junior en IA, Data ou logiciel chez {name}. Ravi de rejoindre votre réseau."
        followup = f"Bonjour, merci pour la connexion. Je m’intéresse aux opportunités junior en IA, Data et logiciel chez {name}. Je n’ai présenté aucune ancienne annonce comme active; ma candidature spontanée met en avant mon PFE Linedata, mon socle logiciel et ma capacité à relier technologie et valeur métier. Pourriez-vous m’orienter vers le bon interlocuteur ?"
    return subject, body, invitation, followup


def main() -> None:
    cache = load_cache()
    with LOCAL.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    with FOREIGN.open(encoding="utf-8-sig", newline="") as handle:
        rows.extend(csv.DictReader(handle))
    output: list[dict[str, str]] = []
    for row in rows:
        if row.get("verification_status", "").startswith("Vérifié"):
            continue
        item = cache.get(row["organization_key"], {})
        results = useful_results(item)
        sources = select_sources(results, row["organization_name"])
        channel = select_channel(results, row["organization_name"])
        verified_email = exact_public_email(row, results)
        junior_status, junior_note = junior_evidence(results, row["organization_name"])
        contact_name, linkedin = linkedin_person(results, row["organization_name"])
        subject, body, invitation, followup = make_email(row)
        source_text = " | ".join(sources) if sources else "Recherches web ciblées du 2026-09-25 — aucun résultat suffisamment pertinent conservé"
        if verified_email != NO_EMAIL:
            email_status = "Adresse exacte retrouvée dans un résultat public; vérifier une dernière fois la page source avant envoi"
            channel = f"mailto:{verified_email}" + (f" | {channel}" if channel != MISSING else "")
        else:
            email_status = "Les adresses du CSV n’ont pas été considérées comme vérifiées sans publication publique correspondante"
        if contact_name == MISSING:
            contact_role = "Aucun recruteur ou responsable actuel suffisamment fiable identifié"
            contact_verification = "Non trouvé/non vérifiable après recherche publique"
        else:
            contact_role = "Talent Acquisition / RH potentiel — intitulé exact à confirmer sur LinkedIn avant contact"
            contact_verification = "Profil issu des résultats publics; affiliation actuelle à revérifier au moment de l’envoi"
        output.append({
            "organization_key": row["organization_key"],
            "sector": row["sector"],
            "target_roles": row["target_roles"],
            "match_score_10": row["match_score_10"],
            "match_reason": row["match_reason"],
            "junior_status": junior_status,
            "junior_evidence": junior_note,
            "active_jobs": "Aucune offre correspondant au profil n’a pu être confirmée active le 2026-09-25; utiliser la candidature spontanée et revérifier le canal officiel avant envoi.",
            "linkedin_contact_name": contact_name,
            "linkedin_contact_role": contact_role,
            "linkedin_profile": linkedin,
            "contact_verification": contact_verification,
            "verified_email": verified_email,
            "email_status": email_status,
            "application_channel": channel,
            "recommended_cv": row["recommended_cv"],
            "language": row["language"],
            "potential_score_100": row["potential_score_100"],
            "foreign_employee_status": "Non vérifiable" if row["location_status"] == "Étranger" else "Sans objet — Tunisie",
            "foreign_employee_evidence": "Aucune preuve publique suffisamment précise de visa, relocation ou embauche internationale n’a été confirmée pour un poste junior adapté." if row["location_status"] == "Étranger" else "Candidature locale à Tunis/Ariana.",
            "sources": source_text,
            "checked_date": "2026-09-25",
            "verification_status": "Recherche publique effectuée — candidature spontanée; canal/contact à confirmer avant envoi",
            "notes": "Fiche de couverture conservatrice générée à partir des recherches publiques. Aucun email n’est supposé et aucune offre ancienne n’est déclarée active. Une fiche manuelle ultérieure remplace automatiquement celle-ci.",
            "email_subject": subject,
            "email_body": body,
            "linkedin_invitation": invitation[:295],
            "linkedin_followup": followup,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {len(output)} conservative research records to {OUT}")


if __name__ == "__main__":
    main()
