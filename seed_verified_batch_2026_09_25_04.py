#!/usr/bin/env python3
"""Verified mixed Tunisia/foreign research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path


OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_04.csv"


RECORDS = [
    {
        "organization_key": "altran telnet capgemini engineering",
        "sector": "Ingénierie numérique, logiciel embarqué, automobile, aéronautique, Data, cloud et transformation digitale",
        "target_roles": "Software Engineer junior; ingénieur Python/C++ junior; Data/AI Engineer junior; Business Intelligence junior; DevOps junior; ingénieur validation et automatisation",
        "match_score_10": "8.3",
        "match_reason": "Le diplôme ENSI et les compétences Python, C++, Java, développement logiciel, Data/IA, Git et CI/CD correspondent à plusieurs familles de métiers de Capgemini Engineering Tunisia. Le profil est moins spécialisé en logiciel embarqué et automobile que certains besoins du site, mais sa polyvalence reste pertinente.",
        "junior_status": "Oui",
        "junior_evidence": "Capgemini Engineering dispose d'un parcours officiel Students and Graduates. À Tunis, Sana Ennouri a documenté l'intégration de 90 stagiaires en 2026 et de 50 stagiaires PFE l'année précédente, ce qui confirme une filière jeunes talents locale.",
        "active_jobs": "Aucune offre junior correspondant précisément au profil n'a été confirmée ouverte le 2026-09-25. Des recrutements tunisiens récents existent en BI, développement web, DevOps, DBA et toolchain, mais les publications repérées demandent généralement 2 à 5 ans ou plus d'expérience.",
        "linkedin_contact_name": "Sana Ennouri",
        "linkedin_contact_role": "Responsable/actrice de l'intégration des jeunes talents — Capgemini Engineering Tunisia",
        "linkedin_profile": "https://tn.linkedin.com/in/sana-ennouri-26552a30",
        "contact_verification": "Profil public actuellement rattaché à Capgemini Engineering, avec publications récentes sur les recrutements tunisiens et l'intégration de stagiaires.",
        "verified_email": "Aucun email public de recrutement vérifié",
        "email_status": "Les adresses nominatives du CSV n'ont pas été confirmées dans une source officielle publique et ne sont donc pas utilisées. L'adresse DPO publique de Capgemini est réservée à la protection des données, pas aux candidatures.",
        "application_channel": "https://www.capgemini.com/careers/join-capgemini/job-search/ | https://www.capgemini.com/careers/career-paths/careers-at-capgemini-engineering/students-and-graduates/",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "64",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Implantation admissible au Centre Urbain Nord, Tunis.",
        "sources": "https://www.capgemini.com/careers/career-paths/careers-at-capgemini-engineering/students-and-graduates/ | https://tn.linkedin.com/in/sana-ennouri-26552a30 | https://www.linkedin.com/posts/sana-ennouri-26552a30_capgeminiengineeringtunisia-talented-capgeminiengineeringtunisia-activity-7292291805239271424-AKM2 | https://www.capgemini.com/careers/join-capgemini/job-search/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — entreprise junior-friendly, aucune offre junior locale appropriée confirmée",
        "notes": "Surveiller le portail officiel et les publications de l'équipe tunisienne. Candidature spontanée via LinkedIn en attendant une ouverture junior ; ne pas envoyer aux emails nominatifs non vérifiés du CSV.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | Software, Data et IA",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, je souhaite rejoindre Capgemini Engineering Tunisia pour contribuer à des projets où le logiciel, la Data et l'intelligence artificielle répondent à des enjeux industriels concrets.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. Cette expérience m'a appris à comprendre un besoin métier, concevoir une solution, l'intégrer à un produit existant et collaborer dans un environnement exigeant. Je maîtrise Python, Java, C++, le développement full-stack, les bases de données, Git ainsi que les concepts de machine learning et d'IA générative.\n\nLa diversité des secteurs de Capgemini Engineering et l'accompagnement accordé aux jeunes ingénieurs correspondent particulièrement à ce que je recherche pour débuter ma carrière. Je suis ouvert aux postes juniors en développement logiciel, Data/IA, automatisation, Business Intelligence ou ingénierie numérique, ainsi qu'à tout métier proche de ma formation.\n\nJe serais heureux d'échanger sur les besoins actuels ou futurs de vos équipes. Mon CV est joint à cette candidature.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Ennouri, jeune diplômé ingénieur ENSI, je recherche une première opportunité en software, Data ou IA. Votre travail autour de l'intégration des jeunes ingénieurs chez Capgemini Engineering Tunisia m'intéresse beaucoup. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Ennouri, merci pour la connexion. Mon PFE chez Linedata portait sur des agents IA appliqués à un produit financier et mon profil couvre Python, Java, C++, full-stack et Data/IA. Je n'ai pas trouvé d'offre junior tunisienne actuellement adaptée. Pourriez-vous m'indiquer le bon canal ou les équipes à suivre ?",
    },
    {
        "organization_key": "ampere software technology tunisia",
        "sector": "Logiciel automobile, Software-Defined Vehicle, systèmes embarqués, Data et intelligence artificielle",
        "target_roles": "Software Engineer junior; Python/C++ Engineer junior; Data/AI Engineer junior; ingénieur logiciel automobile; automatisation et validation",
        "match_score_10": "8.5",
        "match_reason": "Le socle ENSI, Python/C++/Java, développement logiciel, Data et IA est très pertinent pour une entité consacrée au logiciel automobile. Les projets IA et full-stack renforcent le profil, même si l'expérience directe en embarqué, AUTOSAR ou temps réel n'est pas encore démontrée.",
        "junior_status": "Oui — stages observés, embauche junior permanente non confirmée",
        "junior_evidence": "Ampere Software Technology Tunisia a publié une opportunité de stage d'été en 2026 et des profils étudiants documentent des stages récents combinant IA et Data Engineering. Cela confirme l'accueil de jeunes profils, sans prouver un CDI junior ouvert au moment du contrôle.",
        "active_jobs": "Aucune offre permanente junior située en Tunisie et correspondant au profil n'a été confirmée ouverte le 2026-09-25. Les offres d'apprentissage IA trouvées concernent la France et ne sont pas présentées comme tunisiennes.",
        "linkedin_contact_name": "Ghada Rejibi",
        "linkedin_contact_role": "Engineering leader — Ampere Software Technology Tunisia; diplômée ENSI",
        "linkedin_profile": "https://tn.linkedin.com/in/ghada-rejibi-a9b62ba",
        "contact_verification": "Profil actuellement rattaché à Ampere Software Technology en Tunisie, diplômée de l'ENSI et ayant relayé une opportunité de stage locale en 2026.",
        "verified_email": "Aucun email public de recrutement vérifié",
        "email_status": "Les deux emails nominatifs présents dans le CSV n'ont pas été retrouvés dans une source officielle publique ; ils ne sont pas utilisés.",
        "application_channel": "https://www.renaultgroup.com/en/talent/careers/job-opportunities/ | https://tn.linkedin.com/in/ghada-rejibi-a9b62ba",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "62",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Entité située en Tunisie et présente dans le fichier avec une adresse admissible à Ariana.",
        "sources": "https://tn.linkedin.com/in/ghada-rejibi-a9b62ba | https://www.linkedin.com/posts/ghada-rejibi-a9b62ba_sdv-newbeginnings-teamwork-activity-7259229514197598209-gq5P | https://www.renaultgroup.com/en/talent/careers/job-opportunities/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — activité locale et accueil de stagiaires; aucune offre junior permanente confirmée",
        "notes": "Candidature spontanée et veille. Le lien ENSI avec Ghada Rejibi rend la prise de contact pertinente, mais elle n'est pas présentée comme recruteuse RH.",
        "email_subject": "Candidature spontanée – Ingénieur logiciel junior | Python, C++, Data et IA",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, je souhaite proposer ma candidature pour une première opportunité chez Ampere Software Technology Tunisia dans le développement logiciel, la Data, l'intelligence artificielle ou l'automatisation.\n\nAu cours de mon PFE chez Linedata, j'ai participé à la modernisation d'un produit financier grâce à des agents IA. J'y ai développé une approche complète allant de la compréhension du besoin à l'intégration d'une solution dans un produit existant, avec une attention portée à la qualité, à la fiabilité et à la valeur apportée aux utilisateurs.\n\nJe maîtrise Python, C++, Java, le développement full-stack, les bases de données et les principes de machine learning et d'IA générative. Je suis particulièrement motivé par l'opportunité d'appliquer ce socle au logiciel automobile et au Software-Defined Vehicle, tout en approfondissant les contraintes propres aux systèmes embarqués et industriels.\n\nCurieux, adaptable et prêt à apprendre rapidement, je serais heureux d'étudier tout poste junior correspondant à ma formation. Je joins mon CV et reste disponible pour un échange.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Rejibi, diplômé récent de l'ENSI, je m'intéresse aux opportunités junior chez Ampere Tunisia en logiciel, Python/C++, Data et IA. Votre parcours ENSI et votre rôle dans l'écosystème Software-Defined Vehicle m'encouragent à vous contacter. Ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Rejibi, merci pour la connexion. Mon PFE chez Linedata portait sur l'intégration d'agents IA dans un produit financier. Je maîtrise aussi Python, C++, Java et le développement full-stack. Je souhaite désormais mettre ce socle au service du logiciel automobile. Pourriez-vous m'orienter vers les futurs besoins juniors d'Ampere Tunisia ?",
    },
    {
        "organization_key": "apate ai",
        "sector": "FinTech, lutte contre la fraude, agents conversationnels et intelligence artificielle agentique",
        "target_roles": "Junior AI/LLM Engineer; AI Product Engineer junior; Python/TypeScript Software Engineer junior; Data/AI Analyst en lutte antifraude",
        "match_score_10": "8.8",
        "match_reason": "La combinaison agents IA, LLM, développement logiciel et ingénierie financière correspond exceptionnellement bien au produit d'Apate.ai, qui déploie des agents autonomes contre les fraudeurs pour des banques et télécoms. Le frein principal est le niveau : les postes techniques récents demandent six ans d'expérience ou un profil senior.",
        "junior_status": "Partiel — junior observé hors technique",
        "junior_evidence": "Apate.ai a recruté récemment un Junior Marketing Coordinator, ce qui montre une ouverture à certains débutants. En revanche, les recherches techniques publiques récentes ciblent des Senior AI/Product Engineers et ne constituent pas une voie junior démontrée.",
        "active_jobs": "Aucune offre technique junior adaptée n'a été confirmée ouverte le 2026-09-25. Senior AI Engineer — Sydney — fermé et exige 6+ ans — https://au.linkedin.com/jobs/view/senior-ai-engineer-at-apate-ai-4439984727. Operations Manager et Junior Marketing Coordinator sont ouverts/récents mais hors profil technique.",
        "linkedin_contact_name": "Brad Joffe",
        "linkedin_contact_role": "Chief Commercial Officer / dirigeant — Apate.ai",
        "linkedin_profile": "https://au.linkedin.com/in/brad-joffe-3a404155",
        "contact_verification": "Profil actuel Apate.ai avec activité très récente sur la croissance et les recrutements. Il ne s'agit pas d'un recruteur technique, mais d'un dirigeant accessible dans cette petite scale-up.",
        "verified_email": "careers@apate.ai",
        "email_status": "Adresse publiée dans une annonce d'ingénierie Apate.ai par le cofondateur Dali Kaafar. L'adresse contact@apate.ai du fichier n'a pas été retenue faute de confirmation équivalente.",
        "application_channel": "mailto:careers@apate.ai | https://www.linkedin.com/company/apate-ai/",
        "recommended_cv": "CV_ATS_Fintech_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "38",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Les annonces trouvées sont hybrides à Sydney et ne mentionnent ni visa sponsorship, ni relocation, ni travail international. La candidature doit demander explicitement si un profil tunisien peut être étudié.",
        "sources": "https://www.linkedin.com/company/apate-ai/ | https://au.linkedin.com/jobs/view/senior-ai-engineer-at-apate-ai-4439984727 | https://www.linkedin.com/feed/update/urn:li:activity:7400032572296318976/ | https://au.linkedin.com/in/brad-joffe-3a404155",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — excellente adéquation métier, aucune ouverture technique junior et mobilité non documentée",
        "notes": "Faible priorité immédiate malgré une excellente adéquation thématique. Envoyer une candidature spontanée courte sans prétendre répondre au poste Senior fermé. Demander la possibilité d'un futur rôle junior et la politique de mobilité internationale.",
        "email_subject": "Expression of Interest – Junior AI Engineer | Agentic AI and Financial Technology",
        "email_body": "Dear Apate.ai Team,\n\nI am writing to express my interest in a future junior AI or software engineering opportunity at Apate.ai. I recently graduated as a Computer Engineer from ENSI, specializing in Financial Engineering, and your mission sits precisely at the intersection I want to pursue: agentic AI, financial services and technology with measurable human impact.\n\nDuring my final-year project at Linedata, I helped modernize a financial product using AI agents. This experience taught me how to translate a business workflow into an integrated AI solution while considering reliability, user value and the realities of a regulated financial environment. My background also includes Python, TypeScript/JavaScript, full-stack development, databases, APIs, machine learning and generative AI.\n\nI understand that your recent engineering searches have targeted senior profiles, and I am not presenting myself as one. I am instead offering a highly aligned junior profile with strong learning capacity, genuine product curiosity and a distinctive combination of software, AI and finance. I would welcome the opportunity to contribute through a junior role or a suitable graduate pathway as the team grows.\n\nI am currently based in Tunisia and willing to relocate. Could you please let me know whether Apate.ai can consider an international junior candidate for future openings? My CV is attached.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hi Brad, I am a recent ENSI Computer Engineering graduate specialised in Financial Engineering. My Linedata project used AI agents to modernise a financial product, so Apate.ai's mission against fraud strongly resonates with me. I would be glad to connect and follow your team's growth.",
        "linkedin_followup": "Hi Brad, thank you for connecting. I have sent a brief expression of interest to careers@apate.ai. I know the recent engineering roles are senior; I am approaching you as a junior whose background combines agentic AI, software and financial engineering. If the team later opens a graduate role and can consider relocation, I would value being considered.",
    },
    {
        "organization_key": "assist you group bv",
        "sector": "IA conversationnelle, voice agents, LLM, cloud et intégration de solutions pour entreprises",
        "target_roles": "Software Developer; Junior AI/LLM Engineer; conversational AI engineer; Python/TypeScript developer; AI integration engineer",
        "match_score_10": "8.6",
        "match_reason": "L'offre couvre directement les LLM, les assistants numériques, les APIs, Python/TypeScript, le cloud et l'intégration client. Le PFE en agents IA et le full-stack sont très pertinents. Cependant, l'exigence de néerlandais natif constitue un obstacle déterminant et le candidat n'a pas encore les 1–2 années d'expérience professionnelle demandées.",
        "junior_status": "Oui — début de carrière avec 1–2 ans demandés",
        "junior_evidence": "L'offre officielle Software Developer est présentée comme une occasion de développer ses compétences et d'apprendre l'implémentation de LLM et d'AI Voice Agents, mais demande au moins 1–2 ans d'expérience.",
        "active_jobs": "Software Developer — Rotterdam, Pays-Bas — page officielle accessible le 2026-09-25 — https://www.assistyou.ai/jobs-software-developer | Open application — Rotterdam — https://www.assistyou.ai/nl/jobs/",
        "linkedin_contact_name": "Bram van Zanten",
        "linkedin_contact_role": "Founder & CEO — AssistYou Group",
        "linkedin_profile": "https://nl.linkedin.com/in/bramvanzanten",
        "contact_verification": "La page équipe officielle identifie Bram van Zanten comme fondateur et CEO ; son profil public est actuellement rattaché à AssistYou et publie sur les agents vocaux et multi-agents.",
        "verified_email": "jobs@assistyou.ai | bram@assistyou.ai",
        "email_status": "jobs@assistyou.ai est publié sur la page officielle des emplois. bram@assistyou.ai est publié sur la page officielle About/Team ; utiliser jobs@ en destinataire et Bram uniquement en copie ou pour un suivi ciblé.",
        "application_channel": "https://www.assistyou.ai/jobs-software-developer | mailto:jobs@assistyou.ai",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "43",
        "foreign_employee_status": "Non — pour l'offre actuelle selon les critères linguistiques; visa non vérifiable",
        "foreign_employee_evidence": "L'offre exige explicitement un locuteur natif néerlandais et un anglais courant. Elle ne mentionne aucun sponsoring de visa ou relocation. Même si la nationalité n'est pas interdite, le candidat ne satisfait pas le filtre linguistique annoncé.",
        "sources": "https://www.assistyou.ai/jobs-software-developer | https://www.assistyou.ai/nl/jobs/ | https://www.assistyou.ai/nl/about-us | https://nl.linkedin.com/in/bramvanzanten | https://nl.linkedin.com/in/pepijn-de-rijk-32390a7",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — offre officielle accessible, inadéquation linguistique majeure et mobilité non documentée",
        "notes": "Ne pas candidater comme si tous les critères étaient remplis. Si candidature envoyée, reconnaître clairement l'absence de néerlandais et demander si l'équipe accepterait exceptionnellement un profil anglophone ou pour une future fonction internationale.",
        "email_subject": "International Junior AI/Software Profile – Voice Agents and LLMs",
        "email_body": "Dear AssistYou Team,\n\nI discovered your Software Developer opening and was immediately drawn to the opportunity to build AI voice agents that combine LLMs, real-time processing, cloud services and customer integration. I recently graduated as a Computer Engineer from ENSI, and my final-year project at Linedata focused on modernising a financial product with AI agents.\n\nMy experience includes Python, TypeScript/JavaScript, full-stack development, databases, APIs, machine learning and generative AI. More importantly, I enjoy connecting technical work to a concrete user problem—exactly the product-oriented and customer-facing approach described in your role.\n\nI want to be transparent about two gaps: I am at the beginning of my career rather than having two full years of employment, and I am fluent in English and French but not a native Dutch speaker. I therefore understand that I may not meet the current role's strict language requirement. Still, the technical and product fit is unusually strong, so I would be grateful to know whether you might consider an English-speaking international junior for this or a future role.\n\nI am based in Tunisia and willing to relocate to Rotterdam, subject to work-authorisation support. My CV is attached for your consideration.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hi Bram, I am a recent ENSI Computer Engineering graduate whose Linedata project focused on AI agents. AssistYou's work on voice agents, LLMs and real-time customer experiences strongly matches my interests. I am exploring junior international opportunities and would be glad to connect.",
        "linkedin_followup": "Hi Bram, thank you for connecting. I found your Software Developer role and sent a transparent enquiry to jobs@assistyou.ai. My profile aligns with LLM agents, Python/TypeScript and product integration, but I am not a native Dutch speaker. If you may consider an English-speaking junior now or later, I would greatly value your guidance.",
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
