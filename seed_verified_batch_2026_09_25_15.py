#!/usr/bin/env python3
"""Verified foreign employers with active career routes, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path
OUT=Path(__file__).resolve().parent/"verified_batches"/"batch_2026_09_25_15.csv"

def r(key:str, **v:str)->dict[str,str]:
    d={"organization_key":key,"checked_date":"2026-09-25","verified_email":"Aucun email public vérifié","email_status":"Candidature via le portail officiel uniquement","recommended_cv":"CV_ATS_EN.pdf","language":"Anglais","foreign_employee_status":"Non vérifiable","foreign_employee_evidence":"Aucun engagement public de sponsoring de visa trouvé pour le poste ciblé.","verification_status":"Vérifié — recherche manuelle effectuée"}; d.update(v); return d

RECORDS=[
r("airbus",
 sector="Aerospace, software engineering, Data, AI/GenAI, cloud and digital transformation",target_roles="Junior Data Analyst & AI Specialist; Entry-level AI Software Developer; Junior Software/AI Engineer",match_score_10="9.1",potential_score_100="78",
 match_reason="Two current entry-level roles match Python, Java, C++, AI agents, APIs, cloud and CI/CD. The security-clearance condition may restrict eligibility.",junior_status="Oui — offres entry-level actives",junior_evidence="The official Workday postings label Junior Data Analyst and AI Specialist and AI Software Developer as Entry Level.",
 foreign_employee_status="Non vérifiable — habilitation de sécurité à contrôler",foreign_employee_evidence="The France roles do not state visa sponsorship and require eligibility for security clearance. A separate UK graduate role explicitly refuses Skilled Worker sponsorship, but that restriction cannot automatically be generalized to France.",
 active_jobs="Junior Data Analyst and AI Specialist — Toulouse — Entry Level — https://ag.wd3.myworkdayjobs.com/en-US/Airbus/job/Toulouse-Area/Junior-Data-Analyst-and-AI-Specialist--h-f-_JR10405135-1 ; AI Software Developer — Toulouse — Entry Level — https://ag.wd3.myworkdayjobs.com/en-US/Airbus/job/AI-Software-Developer--M-F-_JR10432748-1",
 linkedin_contact_name="Carmélina Panico",linkedin_contact_role="Talent Acquisition Partner — Airbus",linkedin_profile="https://fr.linkedin.com/in/carm%C3%A9lina-panico-b5a500a9",contact_verification="Current Airbus Talent Acquisition profile in Toulouse.",application_channel="https://ag.wd3.myworkdayjobs.com/Airbus",
 sources="https://ag.wd3.myworkdayjobs.com/en-US/Airbus/job/Toulouse-Area/Junior-Data-Analyst-and-AI-Specialist--h-f-_JR10405135-1 | https://ag.wd3.myworkdayjobs.com/en-US/Airbus/job/AI-Software-Developer--M-F-_JR10432748-1 | https://fr.linkedin.com/in/carm%C3%A9lina-panico-b5a500a9",
 verification_status="Vérifié — deux offres IA entry-level actives, admissibilité internationale à confirmer",notes="Très haute priorité. Apply through Workday immediately; do not email welcome.earlycareers@airbus.com because it is not the application route for these roles.",
 email_subject="Application – Junior Data Analyst and AI Specialist",
 email_body="""Dear Airbus Recruitment Team,

I am applying for the Junior Data Analyst and AI Specialist position in Toulouse. I recently graduated as a Computer Engineer from ENSI, with a specialization in Financial Engineering, and my final-year project at Linedata focused on modernizing a financial product through AI agents.

This experience allowed me to connect business needs with Python-based AI, data processing, APIs and integration into an existing product. I also have experience with Java, C++, full-stack development, SQL, Git and CI/CD. The position's combination of data management, analytical solutions, AI agents and operational digital excellence strongly matches the direction in which I want to build my career.

I am based in Tunisia and fully open to relocating to Toulouse. I understand that work authorization and security-clearance eligibility must be assessed, and I am ready to provide any required information.

Thank you for considering my application.

Kind regards,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Bonjour Mme Panico, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur des agents IA intégrés à un produit financier. Les offres Airbus Junior Data Analyst & AI Specialist et AI Software Developer correspondent fortement à mon profil. Ravi d’échanger.",linkedin_followup="Bonjour Mme Panico, merci pour la connexion. Je souhaite candidater à l’offre Junior Data Analyst and AI Specialist à Toulouse. Étant basé en Tunisie, pourriez-vous m’indiquer si l’autorisation de travail et l’habilitation peuvent être étudiées pour ce poste entry-level ?"),
r("murex",
 sector="Capital-markets FinTech software, trading, risk, post-trade, Java/C++, DevOps and AI research",target_roles="Graduate Software Engineer; Java Developer; FinTech Consultant; QA/Testing Engineer; AI/Data junior",match_score_10="9.7",potential_score_100="82",
 match_reason="Near-perfect match between computer engineering, financial engineering, Java/C++, software development and the Linedata financial-product PFE.",junior_status="Oui — official graduate careers",junior_evidence="Murex explicitly recruits fresh graduates, assigns mentors and offers early-career tracks in software, QA, support and consulting.",
 foreign_employee_status="Non vérifiable",foreign_employee_evidence="Murex has 65+ nationalities and global graduate careers, but the Paris portal does not promise French visa sponsorship. Its VIE route is limited to EEA citizens and therefore does not apply to a Tunisian candidate.",
 active_jobs="Software Engineer Java — Paris — posted 13 days ago — https://murex.wd3.myworkdayjobs.com/en-US/MurexCareerPage1/job/Software-Engineer-Java_JR103089 ; Students & Graduates route — https://www.murex.com/en/careers/students-graduates",
 linkedin_contact_name="Amal Bacha",linkedin_contact_role="Current Murex professional connected to Recruitment & Mobility Europe activity",linkedin_profile="https://fr.linkedin.com/in/amal-bacha",contact_verification="Current Murex profile; reposted a current Recruitment & Mobility Europe hiring message. Apply through portal rather than sending a CV unsolicited.",application_channel="https://murex.wd3.myworkdayjobs.com/MurexCareerPage1",
 recommended_cv="CV_ATS_Fintech_EN.pdf",sources="https://murex.wd3.myworkdayjobs.com/en-US/MurexCareerPage1/job/Software-Engineer-Java_JR103089 | https://www.murex.com/en/careers/students-graduates | https://www.murex.com/en/careers/our-teams | https://fr.linkedin.com/in/amal-bacha",
 verification_status="Vérifié — excellente cible FinTech et poste Java actif, sponsoring France non documenté",notes="Très haute priorité. Apply through Workday. mxhr@murex.com in the CSV was not confirmed on the current careers site.",
 email_subject="Application – Graduate Java Software Engineer",
 email_body="""Dear Murex Recruitment Team,

I am applying for the Software Engineer Java opportunity in Paris. I recently graduated as a Computer Engineer from ENSI with a specialization in Financial Engineering, a combination that directly reflects Murex's position at the intersection of technology and capital markets.

My final-year project at Linedata focused on modernizing a financial product with AI agents. Beyond AI, I developed practical experience in Java, Python, C++, APIs, databases, full-stack development, testing and Git-based workflows. Working on an established financial product taught me to understand business constraints while building maintainable software.

Murex particularly attracts me because graduates can develop both strong engineering foundations and genuine capital-markets expertise. I am based in Tunisia and open to relocating to Paris, subject to work-authorization feasibility.

Thank you for considering my application.

Kind regards,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Bonjour Mme Bacha, diplômé ingénieur ENSI spécialisé en ingénierie financière, j’ai réalisé mon PFE chez Linedata sur la modernisation d’un produit financier avec des agents IA. Le poste Software Engineer Java chez Murex correspond très fortement à mon profil. Ravi d’échanger.",linkedin_followup="Bonjour Mme Bacha, merci pour la connexion. Je vais candidater au poste Software Engineer Java à Paris. Mon profil combine Java/C++/Python, développement produit et ingénierie financière. Savez-vous si un jeune diplômé basé en Tunisie peut être considéré pour cette offre ?"),
r("societe generale",
 sector="Banking, investment banking, Data/AI, GenAI, LLM/RAG, APIs, Azure and CI/CD",target_roles="AI Engineer junior; Data/ML Engineer junior; Software Engineer; IT/FinTech analyst",match_score_10="9.4",potential_score_100="84",
 match_reason="The live AI Engineer role explicitly targets a Bac+5 young graduate with internship experience, Python, software development, APIs, GenAI/RAG and CI/CD — a direct match.",junior_status="Oui — offre jeune diplômé active",junior_evidence="The official AI Engineer posting published 24 September 2026 explicitly says 'jeune diplômé' with internship/apprenticeship experience.",
 active_jobs="AI Engineer — CDI — La Défense — published 24/09/2026 — https://careers.societegenerale.com/offres-d-emploi/ai-engineer-26000FBD-fr",
 linkedin_contact_name="Rosaëlle Ferendo",linkedin_contact_role="Current HR professional — Société Générale",linkedin_profile="https://fr.linkedin.com/in/rosa%C3%ABlle-ferendo",contact_verification="Profile announced joining Société Générale one week before verification; exact assignment to the AI role is not established.",application_channel="https://careers.societegenerale.com/offres-d-emploi/ai-engineer-26000FBD-fr",
 recommended_cv="CV_ATS_Fintech.pdf",language="Français",sources="https://careers.societegenerale.com/offres-d-emploi/ai-engineer-26000FBD-fr | https://fr.linkedin.com/in/rosa%C3%ABlle-ferendo",
 verification_status="Vérifié — offre AI Engineer jeune diplômé publiée hier, mobilité internationale non précisée",notes="Priorité maximale. Apply through the portal immediately. Do not use adm.stages@socgen.com; it is not the channel for this CDI.",
 email_subject="Candidature – AI Engineer – Réf. 26000FBD",
 email_body="""Bonjour,

Je vous présente ma candidature au poste d’AI Engineer, référence 26000FBD. Récemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, j’ai réalisé mon PFE chez Linedata sur la modernisation d’un produit financier à l’aide d’agents IA.

Cette expérience m’a permis de travailler avec Python, les LLM, les APIs et les données tout en intégrant la solution dans un produit métier existant. Je maîtrise également Java, C++, SQL, le développement full-stack, Git et les principes de CI/CD. Je souhaite désormais approfondir l’industrialisation de solutions de machine learning et d’IA générative dans un environnement bancaire exigeant.

La collaboration annoncée entre Data Scientists, équipes IT et métiers correspond précisément à mon double parcours informatique-finance. Basé en Tunisie, je suis disponible pour une mobilité en France, sous réserve des démarches d’autorisation de travail.

Je vous remercie pour l’attention portée à ma candidature.

Bien cordialement,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Bonjour Mme Ferendo, jeune diplômé ingénieur ENSI spécialisé en ingénierie financière, mon PFE Linedata concernait l’intégration d’agents IA dans un produit financier. Je candidate au poste AI Engineer 26000FBD publié par Société Générale. Ravi d’échanger.",linkedin_followup="Bonjour Mme Ferendo, merci pour la connexion. J’ai ciblé le poste AI Engineer 26000FBD, explicitement ouvert aux jeunes diplômés. Mon profil réunit Python, IA générative, APIs, CI/CD et ingénierie financière. Pourriez-vous m’indiquer si une candidature depuis la Tunisie est recevable ?"),
r("dassault systemes",
 sector="Industrial software, 3DEXPERIENCE, virtual twins, AI, simulation and cloud",target_roles="Graduate Software Engineer; Junior AI/ML Engineer; Python/C++ Developer; Data Engineer",match_score_10="8.2",potential_score_100="65",
 match_reason="Strong software/AI/C++ fit and formal graduate programs. No exact current France vacancy was isolated in the search result.",junior_status="Oui — official graduate and entry-level programs",junior_evidence="Dassault Systèmes officially offers graduate programs for recent graduates and lists 672 opportunities globally.",
 foreign_employee_status="Non vérifiable",foreign_employee_evidence="The VIE program requires EEA citizenship and is not available to the candidate. Regular French roles may still be possible, but sponsorship is not documented.",active_jobs="Graduate/entry-level search portal — https://www.3ds.com/fr/careers/jobs ; 672 global results at verification time; no exact suitable France role confirmed.",
 linkedin_contact_name="Diane Bartmann",linkedin_contact_role="Talent Acquisition Partner — Dassault Systèmes",linkedin_profile="https://fr.linkedin.com/in/dianebartmann",contact_verification="Current profile and recent Dassault Systèmes recruiting/academic-relations activity.",application_channel="https://www.3ds.com/fr/careers/jobs",
 sources="https://www.3ds.com/fr/careers/students-graduates | https://www.3ds.com/fr/careers/jobs | https://fr.linkedin.com/in/dianebartmann",
 verification_status="Vérifié — programmes graduate officiels, aucune offre française exacte retenue aujourd’hui",notes="Monitor and apply through the portal. The CSV email fr.people.admin@3ds.com is administrative, not a verified application address.",
 email_subject="Application – Graduate Software / AI Engineer",
 email_body="""Dear Dassault Systèmes Recruitment Team,

I am a recent Computer Engineering graduate from ENSI seeking an entry-level software or AI engineering opportunity. My final-year project at Linedata involved modernizing a financial product with AI agents, from understanding the business need to integrating the solution into an existing application.

My background includes Python, Java, C++, machine learning, APIs, databases, full-stack development, Git and CI/CD. I am particularly interested in Dassault Systèmes because virtual twins and AI connect rigorous software engineering with real industrial impact.

I am based in Tunisia and open to relocation to France. I would be grateful to be considered for a suitable graduate or junior role through your official career portal.

Kind regards,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Bonjour Mme Bartmann, jeune diplômé ingénieur ENSI, mon PFE chez Linedata portait sur l’intégration d’agents IA dans un produit existant. Je recherche un poste graduate en logiciel/IA et l’environnement 3DEXPERIENCE m’intéresse beaucoup. Ravi d’échanger.",linkedin_followup="Bonjour Mme Bartmann, merci pour la connexion. Mon profil combine Python, Java, C++, IA et développement produit. Pourriez-vous me conseiller sur les opportunités graduate/junior françaises adaptées à un candidat tunisien ouvert à la mobilité ?"),
r("orange gardens",
 sector="Telecommunications, AI/Data, cybersecurity, cloud, software development and digital services",target_roles="Graduate AI/Data Engineer; Junior Software Engineer; Cloud/Cybersecurity junior",match_score_10="8.1",potential_score_100="61",
 match_reason="Orange's AI/data, development, cloud and cybersecurity tracks match the profile; the Graduate Program targets recent Master graduates.",junior_status="Oui — Orange Graduate Program",junior_evidence="The official France page lists the Orange Graduate Program for candidates graduating in 2026 or holding a Master obtained in the last three years.",
 foreign_employee_status="Non vérifiable",foreign_employee_evidence="The program includes international rotations but the public eligibility page does not confirm French visa sponsorship for non-EU candidates.",active_jobs="Orange Graduate Program — recent graduates — https://orange.jobs/fr/fr/etudiant/orange-graduate-program ; general France tech vacancies — https://orange.jobs/fr/fr/europe/france",
 linkedin_contact_name="Orange Talent Acquisition France",linkedin_contact_role="Official recruitment channel",linkedin_profile="https://www.linkedin.com/company/orange/jobs/",contact_verification="No current individual recruiter for the candidate's exact domain was identified unambiguously.",application_channel="https://orange.jobs/fr/fr/europe/france",
 language="Français",recommended_cv="CV_ATS.pdf",sources="https://orange.jobs/fr/fr/europe/france | https://orange.jobs/fr/fr/etudiant/orange-graduate-program",
 verification_status="Vérifié — Graduate Program et filières IA/Data/Cloud officiels, sponsoring non documenté",notes="Apply only to a specific portal vacancy. Do not use poleoperations.orangefrance@orange.com, which is not a recruitment address.",
 email_subject="Candidature – Orange Graduate Program / Ingénieur IA-Data junior",
 email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, je souhaite rejoindre Orange dans le cadre d’une opportunité graduate ou junior en IA, Data, développement logiciel ou cloud.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. J’ai travaillé avec Python, les LLM, les APIs, les bases de données et une application existante. Je maîtrise également Java, C++, le développement full-stack, Git et les principes de CI/CD.

La diversité des activités technologiques d’Orange et la possibilité de contribuer à des projets ayant un impact à grande échelle correspondent à mon projet professionnel. Basé en Tunisie, je suis ouvert à une mobilité en France et à un parcours international adapté.

Je vous remercie pour l’attention portée à ma candidature.

Bien cordialement,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Bonjour, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur des agents IA intégrés à un produit financier. Je recherche une première opportunité en IA, Data, logiciel ou cloud et le Graduate Program Orange m’intéresse particulièrement. Ravi de rejoindre votre réseau.",linkedin_followup="Bonjour, merci pour la connexion. Mon profil combine Python, Java/C++, IA, APIs et développement full-stack. Pourriez-vous m’orienter vers les postes graduate/junior Orange accessibles à un candidat tunisien ouvert à la mobilité en France ?"),
r("arhs group",
 sector="IT consulting, software development, Data Science, ML, cloud, cybersecurity and public-sector systems; part of Accenture",target_roles="Junior Java/Full-stack Engineer; Data/AI Engineer; Cloud/DevOps junior",match_score_10="7.7",potential_score_100="47",
 match_reason="Java, SQL, REST, full-stack, Data/AI and CI/CD fit the company's stack. Current Luxembourg vacancies found are mid-level/senior and often onsite in regulated EU institutions.",junior_status="Junior hiring historically possible; no suitable junior vacancy confirmed",junior_evidence="The live portal contains many technical roles, but the reviewed Luxembourg Java roles require solid experience, 3 years or 7 years.",
 foreign_employee_status="Non vérifiable",foreign_employee_evidence="No visa sponsorship found. Onsite work for European institutional clients and background checks may create additional eligibility constraints.",active_jobs="Mid-level Fullstack Java Developer — Luxembourg — minimum 3 years — https://jobs.smartrecruiters.com/ARHS/744000127172599 ; other current Java roles are experienced.",
 linkedin_contact_name="ARHS Group / Accenture Careers",linkedin_contact_role="Official careers channel",linkedin_profile="https://www.linkedin.com/company/arhs-group/",contact_verification="Company is currently part of Accenture; no individual recruiter for a junior role was identified safely.",application_channel="https://jobs.smartrecruiters.com/ARHS",
 sources="https://jobs.smartrecruiters.com/ARHS/744000127172599 | https://jobs.smartrecruiters.com/ARHS/744000017668871-java-jee-developer",
 verification_status="Vérifié — bonne adéquation technique, mais offres luxembourgeoises actuelles expérimentées",notes="Low current priority. Do not use the old personal ARHS emails in the CSV; apply only through SmartRecruiters.",
 email_subject="Future Junior Software / Data Engineering Opportunities",
 email_body="""Dear ARHS Recruitment Team,

I am a recent Computer Engineering graduate from ENSI with skills in Java, Python, C++, REST APIs, SQL, full-stack development, Data/AI, Git and CI/CD. My final-year project at Linedata focused on modernizing a financial product through AI agents.

ARHS's work across enterprise software, data, cloud and secure public-sector systems is relevant to my profile. I noticed that the current Luxembourg Java vacancies require several years of experience, so I am not presenting myself for those roles. I would instead be interested in a future graduate or junior engineering opportunity.

I am based in Tunisia and open to relocation if work-authorization support is possible.

Kind regards,
Mohamed Oussema Bahloul""",
 linkedin_invitation="Hello, I’m a recent ENSI Computer Engineering graduate with Java, Python, REST, SQL, full-stack and AI experience. ARHS/Accenture’s software, Data and cloud projects interest me. I’d be glad to follow future junior opportunities in Luxembourg.",linkedin_followup="Thank you for connecting. I saw that current Luxembourg Java roles are mid-level or senior. Could you advise whether ARHS expects any graduate/junior software, Data or cloud openings that could consider a Tunisian candidate requiring mobility support?"),
]
fields=[]
for row in RECORDS:
    for k in row:
        if k not in fields: fields.append(k)
with OUT.open("w",encoding="utf-8-sig",newline="") as h:
    w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
