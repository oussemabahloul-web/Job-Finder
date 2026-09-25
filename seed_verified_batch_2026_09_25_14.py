#!/usr/bin/env python3
"""Fast verified foreign-company batch, checked on 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_14.csv"

def r(key: str, **v: str) -> dict[str, str]:
    d = {
        "organization_key": key, "checked_date": "2026-09-25",
        "verification_status": "Vérifié — recherche manuelle effectuée",
        "verified_email": "Aucun email public vérifié", "email_status": "Aucun email public de recrutement vérifié",
        "recommended_cv": "CV_ATS_EN.pdf", "language": "Anglais",
        "foreign_employee_status": "Non vérifiable", "foreign_employee_evidence": "Aucune politique publique de visa/relocation trouvée.",
        "active_jobs": "Aucune offre adaptée confirmée le 2026-09-25.",
    }
    d.update(v)
    return d

RECORDS = [
    r("amalytics",
      sector="HealthTech; AI automation for clinical-trial data entry and eCRF workflows",
      target_roles="Junior AI Engineer; ML Engineer; Python/Full-stack Engineer; Data/Automation Engineer",
      match_score_10="8.5", potential_score_100="49",
      match_reason="Strong AI-automation and product fit. Mohamed's Linedata AI-agent work shows relevant product integration, but he has no clinical-research domain experience.",
      junior_status="Non vérifiable", junior_evidence="The current public footprint shows a 2–10 person startup and no careers page or current vacancy.",
      active_jobs="No current job opening found. The company page has been inactive for about eleven months.",
      linkedin_contact_name="Tahira Ghafoor", linkedin_contact_role="Only publicly listed Amalytics team member / startup contact",
      linkedin_profile="https://www.linkedin.com/company/amalytics", contact_verification="The current company page lists Tahira Ghafoor; no unambiguous personal profile URL was found.",
      application_channel="https://www.linkedin.com/company/amalytics",
      sources="https://www.linkedin.com/company/amalytics | https://amalytics.net/",
      verification_status="Vérifié — forte adéquation IA, mais aucune offre ni voie internationale confirmée",
      notes="Do not use sbenhadj@amalytics.care: it appears only in the CSV and the current official domain is amalytics.net. Contact through LinkedIn only.",
      email_subject="Future Junior AI Engineering Opportunities at Amalytics",
      email_body="""Dear Amalytics Team,

I am a recent Computer Engineering graduate from ENSI with a specialization in Financial Engineering. During my final-year project at Linedata, I helped modernize a business product through AI agents, from understanding the operational need to integrating the solution into an existing application.

Amalytics' use of AI to reduce repetitive work in clinical trials strongly appeals to me because it connects intelligent automation with measurable human impact. My background includes Python, machine learning, APIs, databases and full-stack development.

I found no current vacancy, but I would be glad to be considered for a future junior AI, data or software-engineering need. I am based in Tunisia and open to relocation or an eligible international arrangement.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello, I’m a recent ENSI Computer Engineering graduate whose Linedata PFE used AI agents to modernize a business product. Amalytics’ practical AI automation for clinical trials strongly interests me. I’d be glad to connect and follow future engineering needs.",
      linkedin_followup="Thank you for connecting. I found no current vacancy, but Amalytics’ AI automation mission closely matches my software and AI background. May I share my CV for a future junior engineering opportunity? I am based in Tunisia and open to relocation."),
    r("cede labs",
      sector="FinTech/Web3; CEX connectivity, trading infrastructure, APIs and digital-asset data",
      target_roles="Junior Full-stack Engineer; Backend/API Engineer; Data Scientist; FinTech Software Engineer",
      match_score_10="8.8", potential_score_100="66",
      match_reason="Excellent FinTech and software fit: APIs, full-stack, data and financial-engineering background. Direct crypto/Web3 production experience is the main gap.",
      junior_status="Possible — open general application, but experience level is not specified", junior_evidence="The official application form is live and accepts applications by role and contract type. Recent leadership posts show active hiring, but no explicit junior label.",
      foreign_employee_status="Oui — remote openness observed; visa sponsorship non vérifiable",
      foreign_employee_evidence="A founder's public post states that the team is based at Station F and remote work is not a problem. This supports remote openness, not visa sponsorship or employment from every country.",
      active_jobs="Open application form — https://join.cedelabs.io/ ; a recent careers post lists Fullstack Software Engineer, but the linked detailed vacancy must be rechecked at application time.",
      linkedin_contact_name="Nikita Terekhov", linkedin_contact_role="Co-founder / technical leader — Cede Hub (formerly Cede Labs)",
      linkedin_profile="https://fr.linkedin.com/in/nikita-terekhov", contact_verification="Current profile shows Cede Hub activity and recent hiring posts.",
      verified_email="hello@cedelabs.io", email_status="Published on the official CEDE Labs website and GitHub; general company address, while the application form is preferred.",
      application_channel="https://join.cedelabs.io/",
      recommended_cv="CV_ATS_Fintech_EN.pdf",
      sources="https://join.cedelabs.io/ | https://cede-labs-landing.webflow.io/ | https://github.com/cedelabs | https://fr.linkedin.com/in/nikita-terekhov | https://www.linkedin.com/posts/pierre-ni_cede-labs-cedelabs-twitter-activity-6980130290694266881-9M-b",
      verification_status="Vérifié — excellente cible FinTech, candidature ouverte et remote observé",
      notes="High priority. Prefer the official form; email only if the form fails. Confirm whether the Fullstack role remains open before naming it.",
      email_subject="Application – Junior Full-Stack / FinTech Software Engineer",
      email_body="""Dear Cede Team,

I am a recent Computer Engineering graduate from ENSI, specialized in Financial Engineering, and I would like to apply for a junior full-stack, backend or data-oriented engineering opportunity.

My final-year project at Linedata focused on modernizing a financial product with AI agents. It gave me experience connecting financial workflows with software implementation, APIs, data processing and an existing product environment. I also work with Python, Java, C++, JavaScript, databases and full-stack technologies.

Cede's combination of financial infrastructure, exchange connectivity and product engineering is especially relevant to my dual background. While I am still at the beginning of my career, I bring strong learning ability, ownership and genuine interest in building reliable financial technology.

I am based in Tunisia and open to remote collaboration or relocation. My CV is attached for your consideration.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello Mr Terekhov, I’m an ENSI Computer Engineering graduate specialized in Financial Engineering. My Linedata PFE combined AI agents, APIs and a financial product. Cede’s exchange infrastructure strongly fits my profile; I’d be glad to connect.",
      linkedin_followup="Hello Mr Terekhov, thank you for connecting. I have submitted/plan to submit my profile through Cede’s form for a junior full-stack, backend or data role. My combination of software engineering, AI and financial engineering could fit your product. May I share my CV here?"),
    r("codoc",
      sector="HealthTech; health-data warehouse, DataOps, NLP/LLM, secure data platforms and SaaS",
      target_roles="Junior Data Engineer; Junior AI/ML Engineer; Python Backend Engineer; QA/Support Engineer",
      match_score_10="8.0", potential_score_100="61",
      match_reason="Python, ML, data, APIs and product-integration skills fit codoc's health-data platform. The candidate lacks healthcare-data experience, but the current DataOps and QA roles are relevant.",
      junior_status="Yes — internships, apprenticeships and permanent roles are recruited throughout the year",
      junior_evidence="codoc's recruiting post explicitly mentions internship, permanent and apprenticeship hiring; the live careers page also accepts spontaneous applications.",
      foreign_employee_status="Non vérifiable",
      foreign_employee_evidence="Current roles are Paris-based with frequent remote work, but no visa sponsorship or relocation statement was found.",
      active_jobs="Data Engineer – Run DataOps (CDI, Paris, frequent remote); QA / Support Engineer (CDI, Paris, frequent remote); spontaneous application — https://www.welcometothejungle.com/fr/companies/codoc/jobs",
      linkedin_contact_name="Arthur Delapalme", linkedin_contact_role="Co-founder — codoc",
      linkedin_profile="https://fr.linkedin.com/in/arthur-delapalme-codoc-healthtech", contact_verification="Current codoc co-founder profile and company site are active.",
      application_channel="https://www.welcometothejungle.com/fr/companies/codoc/jobs",
      language="Français", recommended_cv="CV_ATS.pdf",
      sources="https://www.welcometothejungle.com/fr/companies/codoc/jobs | https://www.linkedin.com/company/codoc-healthdata/ | https://fr.linkedin.com/in/arthur-delapalme-codoc-healthtech",
      verification_status="Vérifié — offres DataOps et QA actives, culture junior démontrée, mobilité non documentée",
      notes="High priority if the candidate is willing to relocate to Paris. Apply through Welcome to the Jungle; arthur@codoc.co is not treated as a recruitment address.",
      email_subject="Candidature – Data Engineer / Ingénieur IA junior",
      email_body="""Bonjour Monsieur Delapalme,

Récemment diplômé ingénieur en informatique de l’ENSI, je souhaite proposer ma candidature pour une opportunité junior en Data Engineering, IA ou développement Python chez codoc.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. J’ai ainsi travaillé sur l’intégration d’une solution intelligente dans un produit existant, avec Python, les APIs, les bases de données et le développement logiciel. Cette expérience m’a également sensibilisé aux exigences de fiabilité et de gouvernance propres aux données métier sensibles.

La mission de codoc, qui consiste à rendre les données de santé réellement exploitables pour améliorer la recherche et les soins, donne une finalité concrète à la Data et à l’IA. Je serais particulièrement intéressé par vos besoins en DataOps, backend Python ou IA.

Je suis actuellement basé en Tunisie et disponible pour une mobilité en France si les conditions administratives le permettent. Je joins mon CV et reste disponible pour échanger.

Bien cordialement,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Bonjour M. Delapalme, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur l’intégration d’agents IA dans un produit financier. Les projets Data/IA de codoc au service de la santé m’intéressent particulièrement. Ravi d’échanger avec vous.",
      linkedin_followup="Bonjour M. Delapalme, merci pour la connexion. Les postes Data Engineer/QA actuellement publiés chez codoc ont retenu mon attention. Mon profil combine Python, Data, IA, APIs et intégration produit. Accepteriez-vous que je vous transmette mon CV avant de postuler via le portail ?"),
    r("kshuttle",
      sector="RegTech/FinTech SaaS; financial and ESG regulatory reporting, Data governance, APIs and AI",
      target_roles="Junior Software Engineer; Data/BI Engineer; AI Engineer; Technical Consultant; Business Analyst junior",
      match_score_10="9.0", potential_score_100="58",
      match_reason="Exceptional fit between software/data/AI, financial engineering and regulated reporting. No live technical vacancy or public international-mobility policy was found.",
      junior_status="Yes — young-talent hiring demonstrated", junior_evidence="The company's current CSR report says it recruited 49 people including seven apprentices in 2024 and trains junior project managers; it sets a 2026 objective around young-talent recruitment and retention.",
      active_jobs="No current public vacancy page or suitable live role found on the official site on 2026-09-25.",
      linkedin_contact_name="kShuttle Talent/HR team", linkedin_contact_role="Company recruiting team — no current individual recruiter identified unambiguously",
      linkedin_profile="https://www.linkedin.com/company/kshuttle", contact_verification="Current company page and official report verified; no safe personal HR profile was found.",
      verified_email="Aucun email public vérifié", email_status="rh@kshuttle.io figure dans le CSV, mais aucune publication officielle actuelle retrouvée; ne pas envoyer automatiquement.",
      application_channel="https://www.linkedin.com/company/kshuttle",
      recommended_cv="CV_ATS_Fintech_EN.pdf", language="Français",
      sources="https://kshuttle.io/entreprise/ | https://kshuttle.io/wp-content/uploads/2026/02/Rapport-RSE_31102025.pdf | https://www.linkedin.com/company/kshuttle",
      verification_status="Vérifié — adéquation FinTech/Data exceptionnelle et culture jeunes talents, aucun poste actif confirmé",
      notes="High-priority spontaneous application. Contact through LinkedIn until an official recruitment address or portal is confirmed.",
      email_subject="Candidature spontanée – Ingénieur Data / IA / logiciel junior",
      email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, je souhaite proposer ma candidature pour une première opportunité en Data, IA, développement logiciel ou conseil technique chez kShuttle.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. J’y ai relié compréhension du métier, traitement de données et intégration logicielle dans un produit existant. Je maîtrise notamment Python, Java, C++, les APIs, SQL, les bases de données et le développement full-stack.

kShuttle correspond particulièrement à mon double profil : vos solutions associent données réglementaires, finance, technologie et nouveaux usages de l’IA. Je serais motivé par une mission junior me permettant de contribuer à cette évolution tout en développant ma compréhension des enjeux de reporting et de conformité.

Je suis basé en Tunisie et ouvert à une mobilité en France ou à un dispositif international adapté. Je joins mon CV et reste disponible pour un échange.

Bien cordialement,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Bonjour, jeune diplômé ingénieur ENSI spécialisé en ingénierie financière, j’ai réalisé chez Linedata un PFE mêlant produit financier et agents IA. L’approche Data, réglementation et IA de kShuttle correspond fortement à mon profil. Ravi de rejoindre votre réseau.",
      linkedin_followup="Bonjour, merci pour la connexion. Je recherche une première opportunité en Data, IA, logiciel ou conseil technique. Mon double parcours informatique/finance et mon PFE Linedata correspondent particulièrement aux activités de kShuttle. Puis-je vous transmettre mon CV ?"),
]

fields=[]
for row in RECORDS:
    for k in row:
        if k not in fields: fields.append(k)
with OUT.open("w", encoding="utf-8-sig", newline="") as h:
    w=csv.DictWriter(h, fieldnames=fields); w.writeheader(); w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
