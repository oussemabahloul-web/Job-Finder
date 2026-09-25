#!/usr/bin/env python3
"""Verified high-fit Luxembourg/Turkey employers, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_17.csv"

def r(key: str, **values: str) -> dict[str, str]:
    row = {
        "organization_key": key,
        "checked_date": "2026-09-25",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Candidature via le portail officiel uniquement",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Aucun engagement public de sponsoring de visa trouvé.",
        "verification_status": "Vérifié — recherche manuelle effectuée",
    }
    row.update(values)
    return row

RECORDS = [
    r(
        "neofacto",
        sector="IT consulting, software engineering, Data/AI, cloud, DevOps and finance",
        target_roles="Junior .NET/Full-stack Developer; AI/ML Engineer; Python Backend Developer; IT Business Analyst Finance",
        match_score_10="8.2",
        potential_score_100="70",
        priority="Haute",
        match_reason="Plusieurs rôles actuels couvrent full-stack, Python, Data/AI et finance. L'offre .NET est classée premier emploi mais demande 2–5 ans et C#, ce qui constitue un écart réel.",
        junior_status="Oui — junior, stages et intégration de stagiaires en CDI",
        junior_evidence="Offre Développeur .NET Junior active, trois stages techniques publiés récemment et témoignage officiel d'un stagiaire recruté ensuite comme Software Engineer.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="L'entreprise travaille au Luxembourg et exige une présence locale/hybride; aucune promesse de visa ou relocation n'est publiée.",
        active_jobs="Développeur .NET Junior — Luxembourg — 2 à 5 ans — https://lu.linkedin.com/jobs/view/d%C3%A9veloppeur-net-junior-at-neofacto-4455716802 ; AI/ML Engineer Internship — Luxembourg — https://lu.linkedin.com/jobs/neofacto-emplois ; Back-end Python Developer — https://www.neofacto.com/careers/",
        linkedin_contact_name="Florian Sey",
        linkedin_contact_role="CTO — NEOFACTO",
        linkedin_profile="https://lu.linkedin.com/in/floriansey/en",
        contact_verification="CTO actuel, actif dans les recrutements et les initiatives destinées aux développeurs juniors.",
        application_channel="https://www.neofacto.com/careers/",
        sources="https://www.neofacto.com/careers/ | https://lu.linkedin.com/jobs/view/d%C3%A9veloppeur-net-junior-at-neofacto-4455716802 | https://lu.linkedin.com/jobs/neofacto-emplois | https://lu.linkedin.com/in/floriansey/en",
        verification_status="Vérifié — plusieurs offres actuelles et culture junior, mais visa non documenté",
        notes="Cibler d'abord les postes Python/AI/ML/full-stack. Ne pas prétendre maîtriser .NET/C# si ce n'est pas dans le CV.",
        email_subject="Application – Junior Software / AI Engineer",
        email_body="""Dear NEOFACTO Recruitment Team,

I am a recent Computer Engineering graduate from ENSI seeking a junior software or AI engineering opportunity in Luxembourg. My final-year project at Linedata focused on modernizing a financial software product through AI agents.

I bring hands-on skills in Python, Java, C++, REST APIs, SQL, full-stack development, machine learning, Git and CI/CD. My specialization in Financial Engineering also enables me to understand projects in banking, insurance and digital transformation.

NEOFACTO particularly interests me because of its mix of product development, Data/AI and financial-sector assignments, as well as its visible support for emerging technical talent. I am based in Tunisia and ready to relocate if work-authorization support is feasible.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour M. Sey, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur des agents IA intégrés à un produit financier. Mon profil Python/Java/C++/full-stack et ingénierie financière correspond aux activités de NEOFACTO. Ravi d'échanger.",
        linkedin_followup="Bonjour M. Sey, merci pour la connexion. Je cible vos opportunités junior en logiciel, Python et IA/ML. Pourriez-vous m'indiquer si NEOFACTO peut étudier un jeune diplômé tunisien nécessitant une mobilité vers le Luxembourg ?",
    ),
    r(
        "scorechain",
        sector="FinTech/RegTech, blockchain analytics, AML compliance, Data and SaaS",
        target_roles="Frontend React Developer; Junior Full-stack Engineer; Data & Blockchain Analyst; FinTech Software Engineer",
        match_score_10="8.8",
        potential_score_100="72",
        priority="Haute",
        match_reason="Très forte adéquation FinTech, blockchain, React/full-stack, Python/Data et IA. L'offre frontend est active mais demande 2–5 ans; le niveau LinkedIn est néanmoins 'Premier emploi'.",
        junior_status="Oui/partiel — poste classé premier emploi mais 2–5 ans demandés",
        junior_evidence="L'offre Frontend Developer actuelle est classée Premier emploi. Scorechain a aussi publié stages et rôles Data accessibles avec des bases Python, mais les anciennes offres fermées ne sont pas présentées comme actives.",
        foreign_employee_status="Non vérifiable — relocalisation acceptée sans sponsoring explicite",
        foreign_employee_evidence="L'annonce accepte les personnes basées au Luxembourg ou disposées à s'y installer, mais ne promet pas de visa ni de prise en charge de la relocation.",
        active_jobs="Frontend React Developer — Belval, Luxembourg — React/TypeScript, 2–5 ans — https://lu.linkedin.com/jobs/view/frontend-developer-at-scorechain-4464996193",
        linkedin_contact_name="Lobna Sellami",
        linkedin_contact_role="Scorechain professional active on Data & Blockchain hiring",
        linkedin_profile="https://lu.linkedin.com/in/sellami-lobna-996a961a7",
        contact_verification="Profil Scorechain actuel ayant relayé et décrit le recrutement Data & Blockchain; rôle RH non établi.",
        verified_email="jobs@scorechain.com",
        email_status="Adresse de recrutement publiée dans plusieurs annonces Scorechain; postuler d'abord via l'annonce active",
        application_channel="https://lu.linkedin.com/jobs/view/frontend-developer-at-scorechain-4464996193",
        recommended_cv="CV_ATS_Fintech_EN.pdf",
        sources="https://lu.linkedin.com/jobs/view/frontend-developer-at-scorechain-4464996193 | https://lu.linkedin.com/in/sellami-lobna-996a961a7 | https://lu.linkedin.com/jobs/view/data-research-analyst-at-scorechain-4335989173",
        verification_status="Vérifié — offre React active et très forte adéquation FinTech/blockchain",
        notes="Candidature pertinente si le CV démontre React et des projets concrets. Être transparent sur l'absence d'expérience professionnelle longue.",
        email_subject="Application – Frontend React Developer – Scorechain",
        email_body="""Dear Scorechain Hiring Team,

I am applying for the Frontend React Developer position in Belval. I recently graduated as a Computer Engineer from ENSI, specialized in Financial Engineering, and my final-year project at Linedata focused on integrating AI agents into a financial software product.

My background includes React and full-stack development, REST APIs, databases, Python, Java, C++, testing, Git and CI/CD. I have also worked with blockchain concepts and I am particularly motivated by the opportunity to build a real compliance product at the intersection of software, digital assets and financial risk.

Although I am at the beginning of my professional career, I can demonstrate complete engineering projects and I am ready to grow quickly in React and TypeScript. I am based in Tunisia and willing to relocate to Luxembourg, subject to work-authorization feasibility.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour Mme Sellami, jeune diplômé ENSI spécialisé en ingénierie financière, mon PFE Linedata combinait produit financier et agents IA. Mon profil React/full-stack, Python et blockchain correspond fortement à Scorechain. Ravi d'échanger.",
        linkedin_followup="Bonjour Mme Sellami, merci pour la connexion. Je candidate au poste Frontend React Developer. Mon profil combine logiciel, IA, blockchain et finance. Savez-vous si Scorechain peut étudier un junior tunisien disposé à s'installer au Luxembourg ?",
    ),
    r(
        "insider",
        sector="AI-native B2B SaaS, customer data platform, marketing technology and large-scale software",
        target_roles="AI-Native Software Engineer; Graduate Software Developer; Junior QA/Support Engineer; AI platform engineer",
        match_score_10="8.5",
        potential_score_100="62",
        priority="Haute",
        match_reason="Le poste actif correspond très bien à l'usage quotidien d'agents pour planifier, coder, tester et documenter. Il est toutefois de niveau mid et limité à la Turquie malgré le libellé remote.",
        junior_status="Oui — programmes fresh graduate, mais poste ciblé mid-level",
        junior_evidence="Insider One possède le programme F.I.R.E. pour étudiants/fresh grads et publie des rôles fresh grad/junior. L'offre AI-Native active est cependant décrite comme mid-level par les agrégateurs.",
        foreign_employee_status="Non vérifiable — remote limité à la Turquie",
        foreign_employee_evidence="L'offre est remote mais localisée Turkey; elle ne constitue pas une autorisation de télétravail depuis la Tunisie et ne mentionne pas de sponsoring.",
        active_jobs="Software Engineer – AI Native — Turkey, remote within Turkey — https://jobs.lever.co/insiderone/ee932b8c-0e12-45c1-8c1a-1ec95c4e623c ; Career Revolution: Hi-Tech — Istanbul — https://jobs.lever.co/insiderone",
        linkedin_contact_name="Ece Cosgun",
        linkedin_contact_role="Recruitment Booster — Insider One",
        linkedin_profile="https://tr.linkedin.com/in/ece-cosgun",
        contact_verification="Profil Insider One actuel, actif sur le programme fresh-graduate F.I.R.E. et le recrutement.",
        application_channel="https://jobs.lever.co/insiderone/ee932b8c-0e12-45c1-8c1a-1ec95c4e623c",
        sources="https://jobs.lever.co/insiderone/ee932b8c-0e12-45c1-8c1a-1ec95c4e623c | https://jobs.lever.co/insiderone | https://tr.linkedin.com/in/ece-cosgun",
        verification_status="Vérifié — très bon fit Agentic AI, mais rôle actif mid-level et localisé Turquie",
        notes="Postuler comme candidature ambitieuse, sans masquer le niveau junior. Demander explicitement si la Tunisie ou une relocation vers Istanbul est possible.",
        email_subject="Application – AI-Native Software Engineer",
        email_body="""Dear Insider One Recruitment Team,

I am applying for the AI-Native Software Engineer position. I recently graduated as a Computer Engineer from ENSI, and my final-year project at Linedata focused on using AI agents to modernize an existing financial product.

This experience taught me to use agents across analysis, tool calling, implementation and validation while remaining responsible for the quality of the final software. I also bring strong foundations in Python, Java, C++, APIs, databases, full-stack development, testing, Git and CI/CD.

I recognize that the role expects more production experience than a typical graduate position. I am nevertheless applying because its AI-native engineering philosophy closely matches the way I have built my most significant project. I am based in Tunisia and open to relocation to Istanbul or another workable arrangement.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Ms Cosgun, I am a recent ENSI Computer Engineering graduate whose Linedata PFE used AI agents across a real product workflow. Insider One's AI-native engineering approach and graduate culture strongly resonate with me. Glad to connect.",
        linkedin_followup="Thank you for connecting. I am interested in the AI-Native Software Engineer role, while recognizing it may be above graduate level. Could you advise whether Insider One has a junior route and can consider a Tunisian candidate for Turkey or relocation?",
    ),
]

fields = []
for row in RECORDS:
    for key in row:
        if key not in fields:
            fields.append(key)
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
