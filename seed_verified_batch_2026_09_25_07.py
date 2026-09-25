#!/usr/bin/env python3
"""Verified research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_07.csv"

RECORDS = [
    {
        "organization_key": "farness",
        "sector": "DeepTech, intelligence artificielle, drones autonomes, robotique, Computer Vision et logiciels",
        "target_roles": "AI/ML Engineer junior; Computer Vision Engineer junior; Robotics Software Engineer junior; Python Engineer; Data/AI Engineer; Software Engineer junior",
        "match_score_10": "9.2",
        "match_reason": "Le moteur IA, les systèmes autonomes et la coordination multi-agent de Farness correspondent directement à Python, au machine learning, au logiciel et au PFE sur les agents IA. La robotique et la vision 3D restent des domaines à approfondir, mais l'offre précise qu'une expérience préalable en robotique n'est pas nécessaire.",
        "junior_status": "Oui",
        "junior_evidence": "Farness recrute actuellement un AI Engineer Intern de deux mois à Tunis et a déjà accueilli des PFE ensuite convertis en emploi. Une ancienne offre AI Engineer acceptait 1 à 3 ans d'expérience académique ou professionnelle.",
        "active_jobs": "AI Engineer Intern — Self-Learning Prediction Engine — Tunis, hybride, 2 mois — Python, PyTorch/scikit-learn, Git; publication officielle visible le 2026-09-25 — https://www.linkedin.com/company/farness. L'ancienne offre AI Engineer à temps plein date d'un an et est fermée; elle n'est pas présentée comme active.",
        "linkedin_contact_name": "Mohamed Wassim Mnaouar",
        "linkedin_contact_role": "Founder — Farness",
        "linkedin_profile": "https://fr.linkedin.com/in/mohamed-wassim-mnaouar-815394ab",
        "contact_verification": "Fondateur actuel, profil actif et auteur d'anciennes publications de recrutement Farness utilisant l'adresse officielle de candidature.",
        "verified_email": "contact@farness-ai.com",
        "email_status": "Adresse publiée par le fondateur dans une campagne de recrutement Farness et rattachée au domaine officiel. L'adresse personnelle du fondateur affichée sur le site n'est pas nécessaire.",
        "application_channel": "mailto:contact@farness-ai.com | https://www.linkedin.com/company/farness",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Anglais",
        "potential_score_100": "84",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Stage hybride localisé à Tunis et entreprise disposant d'une équipe locale.",
        "sources": "https://www.linkedin.com/company/farness | https://fr.linkedin.com/in/mohamed-wassim-mnaouar-815394ab | https://farness-ai.com/ | https://tn.linkedin.com/jobs/view/ai-engineer-at-farness-a-b2g-company-4117664248 | https://tn.linkedin.com/in/haroun-tahri",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — opportunité IA junior actuelle et adresse de candidature confirmée",
        "notes": "Très haute priorité. Le format de deux mois est un stage court; demander clairement si un jeune diplômé peut être retenu et si une continuité en emploi junior est envisageable. Ne pas présenter l'ancienne offre AI Engineer comme encore ouverte.",
        "email_subject": "Application – AI Engineer Intern | Self-Learning Prediction Engine",
        "email_body": "Dear Mr Mnaouar,\n\nI am applying for Farness's AI Engineer Intern opportunity focused on a self-learning prediction engine. I recently graduated as a Computer Engineer from ENSI and am looking for an opportunity where AI is connected to a real autonomous system rather than remaining only a prototype.\n\nDuring my final-year project at Linedata, I worked on modernising a financial product through AI agents. I translated business needs into intelligent workflows and contributed to their integration into an existing software product. My background includes Python, machine learning, deep learning fundamentals, LLMs, APIs, databases, C++ and full-stack development.\n\nWhat attracts me to Farness is the challenge of making an AI system evaluate and improve its own decisions in changing real-world conditions. My experience is not yet specialised in robotics or 3D registration, but I bring strong ML/software foundations, an agentic-systems mindset and the ability to learn quickly through experimentation and rigorous evaluation.\n\nAs I am already a graduate, I would also be grateful to know whether the two-month internship can be open to my situation and potentially lead to a junior opportunity. My CV is attached, and I would be pleased to discuss how I could contribute.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Mnaouar, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur les agents IA. L'offre Farness sur un moteur auto-apprenant et votre travail en drones autonomes correspondent fortement à mon profil Python/ML/software. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Mnaouar, merci pour la connexion. J'ai envoyé ma candidature à contact@farness-ai.com pour l'opportunité AI Engineer Intern. Étant déjà diplômé, je souhaiterais savoir si ce stage court peut accueillir mon profil et éventuellement ouvrir vers un rôle junior. Je joins volontiers mon CV ici également.",
    },
    {
        "organization_key": "forvia informatique tunisie",
        "sector": "Automobile, centre IT, Data, intelligence artificielle, automatisation, logiciel et transformation digitale",
        "target_roles": "Product Owner junior Data/AI; RPA Developer junior/apprenti; Data/Integration Engineer junior; AI/Data Engineer junior; Software Engineer junior; Business Analyst IT",
        "match_score_10": "8.9",
        "match_reason": "Le centre IT tunisien mène des projets Data, IA et automatisation à l'échelle du groupe. Le poste actuel Product Owner junior sur des projets IA/Data valorise un diplôme d'ingénieur récent, la compréhension métier et la coordination avec data scientists et développeurs, ce qui correspond particulièrement au parcours ENSI, au PFE Linedata et à l'ingénierie financière. La formation demandée cite toutefois l'ingénierie industrielle ou équivalente.",
        "junior_status": "Oui",
        "junior_evidence": "FORVIA dispose d'un parcours officiel étudiants/jeunes diplômés. À Tunis, le Product Owner junior cible explicitement un diplômé récent; plusieurs alternances récentes Data, RPA, testing et support confirment l'accès aux profils early-career.",
        "active_jobs": "Product Owner junior — Tunis — projets IA et Data, diplômé récent ingénieur/Master, anglais courant — actif le 2026-09-25 — https://www.linkedin.com/jobs/faurecia-jobs-worldwide | RPA Developer Apprentice — Tunis — C/C++/Java, SQL, Git/RPA — actif le 2026-09-25 — https://tn.linkedin.com/jobs/view/rpa-developer-apprentice-at-faurecia-4459681781. Les offres Data Scientist, Data Integration, Software Tester et L2 Support Apprentice consultées affichent « ne prend plus de candidatures » et sont exclues des offres actives.",
        "linkedin_contact_name": "Malek Majoul",
        "linkedin_contact_role": "Collaborateur FORVIA Informatique Tunisie relayant les recrutements et l'adresse RH locale",
        "linkedin_profile": "https://tn.linkedin.com/in/malek-majoul-98119a251",
        "contact_verification": "Profil FORVIA actuel, actif récemment, ayant relayé les campagnes d'alternance FIT et l'adresse RH officielle. Yasmine Ghariani est également une interlocutrice RH actuelle vérifiable.",
        "verified_email": "hr_fit@forvia.com",
        "email_status": "Adresse de recrutement FIT publiée à plusieurs reprises par des collaborateurs actuels FORVIA dans des annonces locales. Utiliser aussi le bouton officiel de l'offre quand il est disponible.",
        "application_channel": "https://www.linkedin.com/jobs/faurecia-jobs-worldwide | mailto:hr_fit@forvia.com",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Anglais",
        "potential_score_100": "90",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Postes situés au centre informatique FORVIA de Tunis.",
        "sources": "https://www.linkedin.com/jobs/faurecia-jobs-worldwide | https://tn.linkedin.com/jobs/view/rpa-developer-apprentice-at-faurecia-4459681781 | https://tn.linkedin.com/jobs/view/data-integration-interface-coordinator-apprentice-at-faurecia-4429902423 | https://tn.linkedin.com/jobs/view/software-tester-apprentice-alternance-at-faurecia-4437768232 | https://tn.linkedin.com/in/malek-majoul-98119a251 | https://tn.linkedin.com/in/yasmine-ghariani-544a04207 | https://www.forvia.com/fr/carrieres/etudiants-et-jeunes-diplomes",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — postes actuels Product Owner junior et RPA Apprentice, canal RH local confirmé",
        "notes": "Très haute priorité pour Product Owner junior. Postuler d'abord via l'annonce, puis envoyer un email ciblé et contacter Malek Majoul. Pour RPA Apprentice, vérifier l'éligibilité à l'alternance après diplomation; ne pas candidater uniquement à ce format si un contrat étudiant est exigé.",
        "email_subject": "Application – Junior Product Owner, AI & Data Projects – FORVIA IT Tunis",
        "email_body": "Dear FORVIA Informatique Tunisie Recruitment Team,\n\nI am applying for the Junior Product Owner position within the Global Data Transformation department in Tunis. I recently graduated as a Computer Engineer from ENSI, with a specialisation in Financial Engineering, and I am seeking a first role at the intersection of technology, business needs and product delivery.\n\nMy final-year project at Linedata focused on modernising a financial product with AI agents. Beyond the technical work, I had to understand business objectives, structure requirements, coordinate the evolution of an existing product and communicate results clearly. This experience, together with my background in Python, Java, C++, full-stack development, databases, APIs, machine learning and generative AI, enables me to work effectively with both business stakeholders and technical teams.\n\nFORVIA's Tunis IT hub particularly interests me because the role connects AI and Data initiatives to real industrial productivity challenges at international scale. Although my specialisation is computer and financial engineering rather than industrial engineering, I bring the recent engineering degree, analytical mindset, software understanding, adaptability and ownership sought for this entry-level role.\n\nI have applied through the official job posting and attach my CV for consideration. I would welcome the opportunity to discuss my motivation and potential contribution.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Majoul, jeune diplômé ingénieur ENSI, je candidate au poste Product Owner junior de FORVIA IT Tunis. Mon PFE chez Linedata associait produit financier et agents IA, avec un profil logiciel, Data et compréhension métier. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Majoul, merci pour la connexion. J'ai candidaté au poste Product Owner junior et envoyé mon CV à hr_fit@forvia.com. Mon expérience Linedata m'a placé à l'interface entre besoin métier, IA et intégration logicielle. Si possible, pourriez-vous m'indiquer si mon dossier peut être orienté vers l'équipe Global Data Transformation ?",
    },
    {
        "organization_key": "gaia code ai",
        "sector": "IA industrielle, automatisation, planification de production, conseil IT et portage/freelance",
        "target_roles": "Junior AI/ML Engineer; Data Scientist junior; Software Developer junior; Python/Automation Engineer; consultant IT junior",
        "match_score_10": "8.5",
        "match_reason": "GAIA développe de l'IA et de l'automatisation pour résoudre des problèmes opérationnels concrets, ce qui correspond au profil IA/logiciel et à l'orientation valeur métier du candidat. L'entreprise est toutefois très petite et le seul canal talent public vise surtout une communauté de freelances expérimentés plutôt qu'un emploi salarié junior.",
        "junior_status": "Non vérifiable",
        "junior_evidence": "La page officielle recherche des Software Developers, AI/ML Engineers et Data Scientists, mais emploie les termes skilled, proactive et seasoned sans programme junior identifié.",
        "active_jobs": "Aucune offre salariée junior nominative vérifiée le 2026-09-25. La page officielle « Join our community of Freelancers » accepte actuellement des candidatures en Software, DevOps, AI/ML, Data et conseil, avec projets à distance — https://gaiacodeai.com/join-it-freelancing/",
        "linkedin_contact_name": "Marouene Mhadhbi",
        "linkedin_contact_role": "Co-founder — GAIA Code AI",
        "linkedin_profile": "https://de.linkedin.com/in/marouene-mhadhbi-11118645",
        "contact_verification": "Fondateur actuel, lancement de GAIA Code AI annoncé en 2025 et activité publique récente sur l'IA appliquée à la planification industrielle.",
        "verified_email": "contact@gaiacodeai.com",
        "email_status": "Adresse affichée sur le site officiel, avec bureau au Centre Urbain Nord. L'adresse mariem@valuecometrics.com du CSV n'est pas liée à GAIA et est exclue.",
        "application_channel": "https://gaiacodeai.com/join-it-freelancing/ | mailto:contact@gaiacodeai.com",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "57",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Adresse du CSV et siège opérationnel au Centre Urbain Nord, Tunis. Le réseau freelance annonce des projets mondiaux réalisables à distance.",
        "sources": "https://gaiacodeai.com/join-it-freelancing/ | https://gaiacodeai.com/our-it-services/ | https://www.linkedin.com/company/gaia-code-ai | https://de.linkedin.com/in/marouene-mhadhbi-11118645 | https://www.linkedin.com/posts/marouene-mhadhbi-11118645_productionplanning-aiautomation-entrepreneurship-activity-7442111803620376576-r28e",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — canal freelance officiel ouvert, aucun emploi salarié junior confirmé",
        "notes": "Priorité moyenne. Écrire directement au fondateur en distinguant une recherche de première mission/emploi d'une expérience freelance déjà établie. Ne pas laisser entendre qu'un contrat salarié est ouvert; demander s'il existe un projet compatible avec un jeune diplômé.",
        "email_subject": "Spontaneous Application – Junior AI / Software Engineer",
        "email_body": "Dear Mr Mhadhbi,\n\nI am a recent Computer Engineering graduate from ENSI and would like to introduce my profile for a junior AI, data or software opportunity with GAIA Code AI.\n\nMy final-year project at Linedata focused on modernising a financial product through AI agents. It taught me to connect an intelligent solution to a concrete business objective, work within an existing software environment and communicate value beyond the model itself. My background includes Python, machine learning, LLMs, APIs, databases, Java, C++ and full-stack development.\n\nGAIA's focus on practical AI for production planning particularly appeals to me. I am motivated by systems that reduce operational friction and support people in making better decisions, not by AI used only as a demonstration. I would bring strong engineering foundations, curiosity, ownership and the perspective of someone trained in both software and business-oriented financial engineering.\n\nI understand that your public talent channel currently focuses on freelancers. As an early-career engineer based in Tunis, I would be grateful to know whether you may consider a junior employee, trainee-to-hire profile or an appropriately mentored first project. My CV is attached.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello Mr Mhadhbi, I am a recent ENSI Computer Engineering graduate whose Linedata project used AI agents to modernise a financial product. GAIA's practical approach to AI for production planning strongly resonates with me. I would be glad to connect and follow your work.",
        "linkedin_followup": "Hello Mr Mhadhbi, thank you for connecting. I sent my CV to contact@gaiacodeai.com for a junior AI/software opportunity. I know GAIA's public channel focuses on freelancers, so I asked whether an early-career role or mentored first project could fit. I would value any guidance on where my profile could contribute.",
    },
]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(RECORDS[0]))
        writer.writeheader()
        writer.writerows(RECORDS)
    print(f"Wrote {len(RECORDS)} records to {OUT}")


if __name__ == "__main__":
    main()
