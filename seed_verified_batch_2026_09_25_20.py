#!/usr/bin/env python3
"""Verified large foreign employers without an exact junior opening, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path
OUT=Path(__file__).resolve().parent/"verified_batches"/"batch_2026_09_25_20.csv"

def r(key:str, **v:str)->dict[str,str]:
    d={"organization_key":key,"checked_date":"2026-09-25","verified_email":"Aucun email public vérifié","email_status":"Candidature via le portail officiel uniquement","recommended_cv":"CV_ATS_EN.pdf","language":"Anglais","foreign_employee_status":"Non vérifiable","foreign_employee_evidence":"Aucun sponsoring de visa confirmé pour une offre junior correspondante.","verification_status":"Vérifié — screening manuel effectué"};d.update(v);return d

RECORDS=[
r("sncf reseau",sector="Rail infrastructure, software, Data/AI, cybersecurity, IoT and digital transformation",target_roles="Junior Software Engineer; Data/AI Engineer; QA Automation Engineer; Cybersecurity Engineer",match_score_10="7.5",potential_score_100="45",priority="Moyenne",
 match_reason="Les métiers SI/Data correspondent bien, mais les offres débutantes actuelles identifiées sont stages/alternances réservés aux étudiants; le CDI IA actuel demande 6–10 ans.",junior_status="Oui — nombreuses offres débutant, surtout stages/alternances",junior_evidence="Le portail SNCF affiche des offres SI/Data débutant et un stage ingénieur test publié le 24/09/2026, mais le candidat est déjà diplômé.",
 active_jobs="Tech Lead IA — Saint-Denis — 6 à 10 ans — https://emploi.sncf.com/nos-offres/834267 ; Stage Ingénieur Test — publié 24/09/2026 — réservé étudiant — https://emploi.sncf.com/nos-offres/798355 ; aucune offre CDI junior exacte retenue",
 linkedin_contact_name="SNCF Recrutement",linkedin_contact_role="Canal officiel carrières",linkedin_profile="https://www.linkedin.com/company/sncf/jobs/",contact_verification="Aucun recruteur individuel pour un CDI junior exact identifié sans ambiguïté.",application_channel="https://emploi.sncf.com/nos-metiers/si-data",language="Français",
 sources="https://emploi.sncf.com/nos-metiers/si-data | https://emploi.sncf.com/nos-offres/834267 | https://emploi.sncf.com/nos-offres/798355",
 verification_status="Vérifié — grand employeur junior-friendly, mais aucune offre CDI junior exacte aujourd'hui",notes="Surveiller les CDI 'Débutant - 1ère expérience'. Ne pas utiliser l'adresse personnelle du CSV.",
 email_subject="Candidature spontanée — Ingénieur SI / Data / IA junior",email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l'ENSI, je souhaite rejoindre SNCF Réseau dans une fonction junior en développement logiciel, Data/IA, automatisation des tests ou cybersécurité.

Mon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. Je maîtrise Python, Java, C++, les APIs, SQL, le développement full-stack, Git et les principes de CI/CD. Je souhaite mettre ces compétences au service de systèmes numériques à grande échelle et d'une mobilité plus fiable.

Basé en Tunisie, je suis ouvert à une mobilité en France si les démarches d'autorisation de travail sont envisageables.

Bien cordialement,
Mohamed Oussema Bahloul""",linkedin_invitation="Bonjour, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur des agents IA intégrés à un produit existant. Je recherche un CDI junior en logiciel, Data/IA ou QA et souhaite suivre les opportunités SI & Data de SNCF Réseau.",linkedin_followup="Bonjour, merci pour la connexion. Les offres débutantes repérées sont surtout des stages/alternances. Pourriez-vous m'orienter vers les futurs CDI junior SI/Data accessibles à un diplômé tunisien ouvert à la mobilité ?"),
r("suez france",sector="Environmental services, water/waste operations, Data/AI and digital solutions",target_roles="Junior Data/AI Engineer; Software Engineer; Digital Transformation Analyst; Data Analyst",match_score_10="6.8",potential_score_100="39",priority="Faible",
 match_reason="SUEZ possède des activités Data/IA et Digital Solutions, mais aucune offre junior IT exacte n'a été confirmée dans le screening actuel.",junior_status="Oui — relations écoles et jeunes diplômés; aucune offre cible confirmée",junior_evidence="SUEZ participe à des Career Days de futurs diplômés et met en avant des profils Data/IA; les résultats actuels ne donnent pas de rôle junior logiciel/IA précis.",active_jobs="Aucune offre junior IT correspondant au profil confirmée — portail groupe à surveiller",
 linkedin_contact_name="Alrick Barreau",linkedin_contact_role="Talent Acquisition — SUEZ",linkedin_profile="https://fr.linkedin.com/in/alrick-barreau-098b6293",contact_verification="Talent Acquisition actuel chez SUEZ; ses besoins publiés sont surtout ingénierie environnementale, pas nécessairement IT.",application_channel="https://www.suez.com/fr/carrieres",language="Français",sources="https://fr.linkedin.com/in/alrick-barreau-098b6293 | https://fr.linkedin.com/in/laure-meunier | https://www.suez.com/fr/carrieres",
 verification_status="Vérifié — Data/IA présente, aucune offre junior IT exacte confirmée",notes="Candidature à faible priorité. Ne pas utiliser l'adresse externe/personnelle du CSV.",email_subject="Candidature spontanée — Ingénieur Data / IA junior",email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l'ENSI, je souhaite proposer ma candidature pour une future opportunité junior en Data, intelligence artificielle, développement logiciel ou transformation digitale chez SUEZ.

Mon PFE chez Linedata a porté sur l'intégration d'agents IA dans un produit financier existant. Mon profil couvre Python, Java, C++, les APIs, SQL, le développement full-stack, le machine learning, Git et CI/CD. Je suis particulièrement motivé par l'utilisation de la donnée et de l'IA pour améliorer des opérations ayant un impact environnemental concret.

Basé en Tunisie, je suis ouvert à la mobilité en France.

Bien cordialement,
Mohamed Oussema Bahloul""",linkedin_invitation="Bonjour M. Barreau, jeune diplômé ingénieur ENSI, mon PFE Linedata concernait des agents IA intégrés à un produit existant. Je recherche un poste junior Data/IA ou logiciel et les activités Digital Solutions de SUEZ m'intéressent. Ravi d'échanger.",linkedin_followup="Bonjour M. Barreau, merci pour la connexion. Je ne vois pas actuellement d'offre junior IT exacte. Pourriez-vous m'indiquer si SUEZ prévoit des besoins débutants en Data, IA, logiciel ou transformation digitale ?"),
r("vilmorin mikado limagrain group",sector="AgriTech, seed research, industrial operations, Data, cybersecurity and digital transformation",target_roles="Junior Data Analyst; IT Project Engineer; Software/Data Engineer; Cybersecurity junior",match_score_10="5.9",potential_score_100="34",priority="Faible",
 match_reason="Des activités IT/Data existent, mais le cœur métier est agricole et aucune offre junior informatique exacte n'a été isolée.",junior_status="Oui — stages et alternances réguliers",junior_evidence="Limagrain met publiquement en avant ses alternants/stagiaires et un nouveau portail regroupe ces contrats; aucune ouverture CDI junior cible confirmée.",active_jobs="Aucune offre CDI junior informatique exacte confirmée — portail officiel https://jobs.limagrain.com/?locale=fr_FR",
 linkedin_contact_name="LIMAGRAIN Careers",linkedin_contact_role="Canal officiel",linkedin_profile="https://www.linkedin.com/company/limagrain/jobs/",contact_verification="Aucun recruteur IT individuel actuel identifié avec certitude.",application_channel="https://jobs.limagrain.com/?locale=fr_FR",language="Français",sources="https://jobs.limagrain.com/?locale=fr_FR | https://talent.limagrain.com/ | https://fr.linkedin.com/in/fabienne-lauret-blachon-gestiondeprojet",
 verification_status="Vérifié — junior-friendly, aucune cible IT exacte aujourd'hui",notes="Faible priorité; surveiller les familles IT/Data/cybersécurité. Ne pas contacter l'email nominatif du CSV.",email_subject="Candidature spontanée — Ingénieur informatique / Data junior",email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l'ENSI, je souhaite proposer ma candidature pour une future opportunité junior en Data, développement logiciel, cybersécurité ou transformation digitale au sein du Groupe Limagrain.

Mon PFE chez Linedata a porté sur la modernisation d'un produit financier avec des agents IA. Je maîtrise Python, Java, C++, les APIs, SQL, le développement full-stack, Git et les principes de CI/CD. Je serais motivé par l'application de ces compétences à la digitalisation de processus industriels et agricoles.

Basé en Tunisie, je suis ouvert à une mobilité en France si elle est envisageable.

Bien cordialement,
Mohamed Oussema Bahloul""",linkedin_invitation="Bonjour, jeune diplômé ingénieur ENSI, mon profil couvre Python, Java/C++, Data/IA et full-stack. Je souhaite suivre les futures opportunités junior IT/Data/cybersécurité du Groupe Limagrain. Ravi de rejoindre votre réseau.",linkedin_followup="Bonjour, merci pour la connexion. Pourriez-vous m'orienter vers les futures opportunités CDI junior en IT, Data ou digitalisation, accessibles à un candidat tunisien ouvert à la mobilité ?"),
r("meta",sector="Large-scale software, AI/ML, infrastructure, AR/VR and product engineering",target_roles="University Graduate Software Engineer; Junior ML Engineer; Production Engineer",match_score_10="7.2",potential_score_100="37",priority="Faible",
 match_reason="Compétences générales pertinentes, mais concurrence extrême et aucune offre London University Graduate officiellement confirmée accessible aujourd'hui.",junior_status="Oui historiquement; aucune offre graduate London confirmée",junior_evidence="Meta recrute régulièrement des university graduates, mais les résultats officiels actuels accessibles ne permettent pas de confirmer une ouverture londonienne adaptée.",foreign_employee_status="Non vérifiable",foreign_employee_evidence="Meta peut sponsoriser certains profils spécialisés, mais aucune preuve de sponsoring n'est attachée à une offre junior actuellement confirmée.",active_jobs="Aucune offre London University Graduate confirmée active — vérifier https://www.metacareers.com/jobs/",
 linkedin_contact_name="Meta Careers",linkedin_contact_role="Canal officiel",linkedin_profile="https://www.linkedin.com/company/meta/jobs/",contact_verification="Aucun recruteur individuel lié à une offre junior exacte identifié.",application_channel="https://www.metacareers.com/jobs/",sources="https://www.metacareers.com/jobs/ | https://www.linkedin.com/company/meta/jobs/",
 verification_status="Vérifié — employeur possible mais aucune offre graduate London confirmée",notes="Ne pas envoyer à l'adresse personnelle @fb.com du CSV. Postuler uniquement à une offre officielle précise.",email_subject="Future University Graduate Software Engineering Opportunities",email_body="""Dear Meta Recruitment Team,

I am a recent Computer Engineering graduate from ENSI with experience in Python, Java, C++, full-stack development, APIs, databases, machine learning, testing and CI/CD. My final-year project at Linedata focused on integrating AI agents into an existing financial software product.

I am interested in future university-graduate software or AI engineering opportunities in London. I am based in Tunisia and would require confirmation of Skilled Worker sponsorship before applying to a location-restricted role.

Kind regards,
Mohamed Oussema Bahloul""",linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with Python/Java/C++, full-stack and AI-agent product experience. I would be glad to follow future Meta university-graduate software or AI opportunities in London.",linkedin_followup="Thank you for connecting. I have not found a currently confirmed London graduate role. Could you advise when suitable university-graduate software openings may reopen and whether sponsorship is assessed per vacancy?"),
]
fields=[]
for row in RECORDS:
    for k in row:
        if k not in fields: fields.append(k)
with OUT.open("w",encoding="utf-8-sig",newline="") as h:
    w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
