#!/usr/bin/env python3
"""Verified Tunisian banking research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path


OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_02.csv"


RECORDS = [
    {
        "organization_key": "attijari bank siege social",
        "sector": "Banque, Data, transformation digitale et cybersécurité",
        "target_roles": "Ingénieur Data; Data/AI Analyst junior; ingénieur SI; cybersécurité; Business Analyst bancaire; audit IT",
        "match_score_10": "9.2",
        "match_reason": "L'offre Ingénieur Data accessible sur le portail officiel, les projets IA/Data/cybersécurité du PFE Book 2026 et la double compétence informatique-finance créent une correspondance particulièrement forte.",
        "junior_status": "Oui",
        "junior_evidence": "Le portail officiel s'adresse aux candidats emploi et stage, le PFE Book 2026 contient de nombreux sujets IT/IA/Data et Attijari a encore signé en juin 2026 un partenariat visant les stages, le recrutement et l'employabilité des jeunes.",
        "active_jobs": "Ingénieur Data — Ariana — page accessible sur le portail officiel le 2026-09-25 — https://recrutement.attijaribank.com.tn/offre/emploi/47",
        "linkedin_contact_name": "Sinda Krifa",
        "linkedin_contact_role": "Talent Acquisition | IT Training & Development | Employer Branding — Attijari bank Tunisie",
        "linkedin_profile": "https://tn.linkedin.com/in/sinda-krifa",
        "contact_verification": "Profil public encore rattaché à Attijari bank, avec activité récente en recrutement et développement des talents.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse RH officielle trouvée ; candidature à déposer sur le portail officiel et prise de contact LinkedIn avec Sinda Krifa.",
        "application_channel": "https://recrutement.attijaribank.com.tn/offre/emploi/47 | https://recrutement.attijaribank.com.tn/",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "93",
        "sources": "https://recrutement.attijaribank.com.tn/offre/emploi/47 | https://recrutement.attijaribank.com.tn/ | https://www.attijaribank.com.tn/sites/default/files/2025-11/PFE-book-26.pdf | https://tn.linkedin.com/in/sinda-krifa | https://www.linkedin.com/company/attijari-bank-tunisie",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — offre Ingénieur Data accessible et contact actuel",
        "notes": "Postuler d'abord via le portail. Le portail ne montre pas de date limite dans le texte accessible : vérifier l'étape finale avant envoi. Ne pas confondre avec l'ancienne offre Consultant Junior en Stratégie, fermée.",
        "email_subject": "Candidature – Ingénieur Data | Informatique, IA et ingénierie financière",
        "email_body": "Bonjour Madame, Monsieur,\n\nJe vous adresse ma candidature au poste d'Ingénieur Data chez Attijari bank. Récemment diplômé ingénieur en informatique de l'ENSI et spécialisé en ingénierie financière, je souhaite mettre mes compétences en données et en développement au service de la transformation d'une banque innovante.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. J'y ai appris à comprendre des besoins métiers financiers, structurer les données nécessaires et concevoir une solution logicielle utile et fiable. Je maîtrise notamment Python, SQL, les bases de données, Java, C++, le développement full-stack ainsi que les approches de machine learning et d'IA générative.\n\nLes travaux d'Attijari bank autour de la Data, de l'automatisation et de la digitalisation correspondent exactement à la direction que je souhaite donner à ma carrière. Curieux, rigoureux et rapidement opérationnel, je suis prêt à apprendre votre environnement et à contribuer aux pipelines, à la qualité et à la valorisation des données.\n\nJe vous remercie pour l'étude de ma candidature et reste disponible pour un entretien.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Krifa, ingénieur ENSI récemment diplômé en informatique et ingénierie financière, je candidate à l'offre Ingénieur Data d'Attijari bank. Mon PFE Linedata portait sur l'IA appliquée à un produit financier. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Krifa, merci pour la connexion. J'ai déposé ma candidature au poste d'Ingénieur Data sur le portail Attijari bank. Mon profil associe Python/SQL, développement logiciel, IA et ingénierie financière, avec un PFE chez Linedata. Je serais reconnaissant si vous pouviez m'indiquer si mon dossier est bien orienté vers l'équipe concernée.",
    },
    {
        "organization_key": "biat",
        "sector": "Banque, finance, Data et transformation digitale",
        "target_roles": "Data/AI Analyst junior; Business Analyst bancaire; systèmes d'information; audit IT; risque et transformation digitale",
        "match_score_10": "8.8",
        "match_reason": "Le double cursus informatique-finance et le PFE Linedata correspondent aux besoins de transformation, de Data, d'analyse métier, d'audit IT et de modernisation bancaire. La filiale BIAT Innovation & Technology fait déjà l'objet d'une fiche distincte.",
        "junior_status": "Oui — preuves de vivier jeunes talents",
        "junior_evidence": "La BIAT participe à des forums emploi IT et présente les stagiaires comme un vivier de recrutement. BIAT Innovation & Technology a encore recruté récemment des Junior Business Analysts et QA Engineers, mais ces offres relèvent de la fiche distincte BIAT IT.",
        "active_jobs": "Aucune offre directe BIAT banque, junior et adaptée, n'a été confirmée comme ouverte le 2026-09-25. Les recrutements BIAT IT sont documentés dans sa fiche séparée.",
        "linkedin_contact_name": "Mariem Habibi",
        "linkedin_contact_role": "Gestionnaire de carrières / Ressources humaines — BIAT",
        "linkedin_profile": "https://tn.linkedin.com/in/mariem-habibi",
        "contact_verification": "Profil public actuellement rattaché à BIAT et activité explicite de gestion des carrières et de représentation RH dans des forums emploi IT.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse RH publique adaptée n'a été trouvée. Les emails d'agences ne sont pas des canaux de recrutement.",
        "application_channel": "https://www.biat.com.tn/vous-etes | https://www.biat.com.tn/nous-contacter",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "70",
        "sources": "https://www.biat.com.tn/vous-etes | https://www.biat.com.tn/nous-contacter | https://tn.linkedin.com/in/mariem-habibi | https://www.linkedin.com/company/biat",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — contact carrière actuel, candidature spontanée",
        "notes": "Utiliser la rubrique Candidat du site BIAT et le formulaire corporate. Ne pas envoyer à une adresse d'agence bancaire. Consulter aussi la fiche BIAT Innovation & Technology, encore plus prioritaire pour l'IT.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | Data/IA, analyse métier et audit IT",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite proposer ma candidature pour une opportunité junior à la BIAT dans la Data et l'IA, l'analyse métier, les systèmes d'information, l'audit informatique ou la transformation digitale.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Cette expérience m'a permis de travailler au croisement des enjeux métiers financiers et des solutions numériques, avec l'objectif d'améliorer l'efficacité, la qualité de l'information et l'expérience des utilisateurs.\n\nJe maîtrise Python, Java, C++, SQL, les bases de données et le développement full-stack, ainsi que les approches de machine learning et d'IA générative. Je souhaite aujourd'hui mettre cette polyvalence au service des projets de modernisation d'une banque de référence.\n\nJe serais reconnaissant que mon profil soit étudié pour toute opportunité junior actuelle ou future correspondant à mon diplôme. Mon CV est joint à ma candidature.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Habibi, ingénieur ENSI récemment diplômé en informatique et ingénierie financière, je recherche une opportunité junior en Data/IA, analyse métier, SI ou audit IT à la BIAT. Votre rôle en gestion des carrières m'incite à vous contacter. Ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Habibi, merci pour la connexion. J'ai transmis une candidature spontanée à la BIAT. Mon PFE chez Linedata concernait la modernisation d'un produit financier avec des agents IA. Pourriez-vous, si possible, m'orienter vers les équipes Data/IA, transformation, SI ou audit IT susceptibles d'étudier un profil junior ?",
    },
    {
        "organization_key": "banque nationale agricole",
        "sector": "Banque publique, Data, cybersécurité et transformation digitale",
        "target_roles": "Data Science junior; sécurité informatique; ingénieur informatique; auditeur informatique; finance/risk analyst; transformation digitale",
        "match_score_10": "9.0",
        "match_reason": "Le concours 2026 comportait des spécialités Data Science, sécurité informatique, informatique, finance et risk management, soit une correspondance directe avec le profil. La date limite est cependant passée.",
        "junior_status": "Oui — concours externe 2026 clos",
        "junior_evidence": "Le concours externe BNA 2026 proposait des postes centraux en Data Science, sécurité informatique, informatique, finance et risk management. La date limite était le 17 septembre 2026.",
        "active_jobs": "Concours externe BNA 2026 — profils Data Science/Sécurité informatique/Finance notamment — clôturé le 2026-09-17 ; ne plus candidater à ce concours.",
        "linkedin_contact_name": "Charfeddine Imed",
        "linkedin_contact_role": "Directeur / expert informatique bancaire — BNA Bank, ancien ENSI",
        "linkedin_profile": "https://tn.linkedin.com/in/charfeddine-imed-68680a5",
        "contact_verification": "Profil actuel BNA, plus de 28 ans d'expérience informatique bancaire et formation ENSI. Contact technique pertinent, pas recruteur RH.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse de recrutement publique fiable identifiée. Les candidatures aux concours passent par le canal indiqué dans l'avis officiel.",
        "application_channel": "http://www.bna.tn/ | https://www.linkedin.com/company/bnabank",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "63",
        "sources": "https://www.linkedin.com/company/bnabank | https://fr.linkedin.com/posts/kedmatn_concours-bna-bank-2026-avis-de-concours-externe-activity-7502132715148734464-uh07 | http://www.bna.tn/ | https://tn.linkedin.com/in/charfeddine-imed-68680a5",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — concours très adapté mais clôturé",
        "notes": "Surveiller un éventuel nouvel avis officiel. Le concours clos démontre une demande réelle pour les compétences du candidat, mais ne doit pas être présenté comme actif.",
        "email_subject": "Candidature spontanée – Ingénieur informatique ENSI | Data, cybersécurité et finance",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite manifester mon intérêt pour toute future opportunité à la BNA dans la Data Science, la sécurité informatique, les systèmes d'information, l'audit IT, la finance ou la gestion des risques.\n\nLe concours 2026 étant désormais clôturé, je vous adresse cette démarche uniquement afin que mon profil puisse être considéré lors d'un prochain besoin correspondant. Mon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle, ce qui m'a permis d'allier compréhension métier, traitement des données et développement logiciel.\n\nJe maîtrise notamment Python, Java, C++, SQL, les bases de données, le développement full-stack, le machine learning et l'IA générative. Je serais motivé à mettre ces compétences au service de la transformation digitale et de la maîtrise des risques d'une banque publique majeure.\n\nJe reste disponible pour tout échange et vous joins mon CV.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Charfeddine, jeune diplômé ENSI en informatique et ingénierie financière, j'ai suivi avec intérêt le concours BNA 2026, désormais clos. Votre parcours ENSI et informatique bancaire m'inspire ; je serais ravi de rejoindre votre réseau et de bénéficier de votre orientation.",
        "linkedin_followup": "Bonjour Monsieur Charfeddine, merci pour la connexion. Le concours BNA 2026 est malheureusement déjà clôturé, mais ses profils Data Science et sécurité informatique correspondent fortement à mon parcours. Mon PFE Linedata portait sur l'IA appliquée à un produit financier. Pourriez-vous me conseiller sur les futurs canaux ou équipes à suivre à la BNA ?",
    },
    {
        "organization_key": "banque centrale de tunisie",
        "sector": "Banque centrale, régulation, FinTech, supervision et systèmes d'information",
        "target_roles": "Ingénieur informatique; Data/AI Analyst; cybersécurité; supervision bancaire; FinTech et innovation réglementaire; audit IT",
        "match_score_10": "8.7",
        "match_reason": "La combinaison ingénierie informatique, finance et IA est très pertinente pour les systèmes, la cybersécurité, la supervision et les initiatives FinTech de la BCT. Les recrutements suivent toutefois des concours formels.",
        "junior_status": "Oui — par concours, aucun concours 2026 confirmé",
        "junior_evidence": "Le concours externe BCT 2024 recrutait 64 cadres et comportait plusieurs codes d'ingénieur informatique et de sécurité informatique. Aucun nouvel avis 2026 officiel n'a été trouvé.",
        "active_jobs": "Aucun concours BCT 2026 adapté et officiellement ouvert n'a été confirmé le 2026-09-25. Le concours externe 2024 est ancien et fermé.",
        "linkedin_contact_name": "Kaouther Bouzamitta",
        "linkedin_contact_role": "Professionnelle BCT spécialisée en FinTech et innovation réglementaire",
        "linkedin_profile": "https://tn.linkedin.com/in/kaouther-bouzamitta-1a51b182",
        "contact_verification": "Profil public actuellement rattaché à la Banque Centrale de Tunisie, avec spécialisation FinTech et regulatory innovation. Contact métier pertinent, pas contact RH.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse de recrutement publique adaptée trouvée ; les candidatures doivent respecter les modalités du concours officiel lorsqu'il est ouvert.",
        "application_channel": "https://www.bct.gov.tn/ | https://www.linkedin.com/company/banque-centrale-de-tunisie",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "56",
        "sources": "https://www.bct.gov.tn/ | https://www.emploi.nat.tn/ckeditor/ckfinder/userfiles/files/Avis_Concours%20bct%202024.pdf | https://tn.linkedin.com/in/kaouther-bouzamitta-1a51b182 | https://fintech.bct.gov.tn/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — aucun concours actuel confirmé",
        "notes": "Ne pas envoyer une candidature hors procédure comme si elle remplaçait un concours. Le message LinkedIn sert à demander une orientation et à surveiller les prochaines ouvertures.",
        "email_subject": "Manifestation d'intérêt – Ingénieur informatique | FinTech, Data/IA et cybersécurité",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite manifester mon intérêt pour de futurs concours ou recrutements de la Banque Centrale de Tunisie en informatique, Data/IA, cybersécurité, supervision ou innovation FinTech.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Cette expérience m'a permis de rapprocher développement logiciel, exploitation des données et compréhension des processus financiers, avec une attention particulière à la fiabilité et à la gouvernance des solutions.\n\nJe maîtrise notamment Python, Java, C++, SQL, les bases de données, le développement full-stack, le machine learning et l'IA générative. Je serais particulièrement motivé par des missions où la technologie soutient la stabilité, la supervision, la sécurité et la modernisation de l'écosystème financier tunisien.\n\nJe comprends que les recrutements de la BCT suivent des procédures officielles et resterai attentif aux prochains avis. Je vous serais reconnaissant de m'indiquer, si possible, le canal à suivre pour les profils correspondant au mien.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Bouzamitta, ingénieur ENSI récemment diplômé en informatique et ingénierie financière, je m'intéresse aux projets FinTech, Data/IA et supervision de la BCT. Votre parcours en innovation réglementaire m'intéresse particulièrement. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Bouzamitta, merci pour la connexion. Mon PFE chez Linedata portait sur la modernisation d'un produit financier avec des agents IA. Je souhaite suivre les futurs concours BCT en informatique, Data, cybersécurité ou FinTech. Pourriez-vous, si possible, me conseiller sur les équipes et canaux officiels à surveiller ?",
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
