#!/usr/bin/env python3
"""Verified recruitment research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "verified_batches" / "batch_2026_09_25_01.csv"


RECORDS = [
    {
        "organization_key": "mnc aero",
        "sector": "TravelTech, FinTech, paiements et logiciels pour le transport aérien",
        "target_roles": "Junior Implementation Engineer; Business Analyst FinTech; Software Engineer junior; Data/AI Engineer junior; automatisation et intégration",
        "match_score_10": "9.0",
        "match_reason": "Très forte convergence entre l'ingénierie informatique, la spécialisation financière, le PFE Linedata et les activités de MNC Aero en paiements, rapprochement, revenue accounting et automatisation. Le profil possède aussi les bases logiciel, données et IA utiles aux métiers d'implémentation.",
        "junior_status": "Oui",
        "junior_evidence": "Une campagne récente pour des Entry-Level/Junior Implementation Engineers demandait notamment SQL, Linux/Unix, Git/GitOps et des compétences de coordination. L'annonce LinkedIn d'Implementation Engineer consultée est toutefois désormais fermée.",
        "active_jobs": "Aucune offre junior adaptée encore ouverte et vérifiée le 2026-09-25. Une offre Software Engineering Manager apparaît récente mais exige un niveau senior et n'est pas recommandée.",
        "linkedin_contact_name": "Aymen Mechria",
        "linkedin_contact_role": "Collaborateur MNC Aero ayant relayé la campagne Implementation Engineer",
        "linkedin_profile": "https://fr.linkedin.com/in/aymen-mechria-0889391b3",
        "contact_verification": "Profil LinkedIn public encore rattaché à MNC Aero et ayant relayé récemment l'offre Implementation Engineer. Contact métier pertinent, pas recruteur RH confirmé.",
        "verified_email": "contact@mnc.aero | info@mnc.aero | khadija.moones@mnc.aero",
        "email_status": "contact@mnc.aero et info@mnc.aero sont publiés sur le site officiel. khadija.moones@mnc.aero a été publiée dans une campagne junior récente, mais l'affiliation actuelle de la personne n'est plus confirmée : privilégier contact@mnc.aero.",
        "application_channel": "https://mnc.aero/ | https://www.linkedin.com/company/mnc-aero/jobs/",
        "recommended_cv": "CV_ATS_Fintech_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "70",
        "sources": "https://mnc.aero/ | https://www.linkedin.com/company/mnc-aero | https://tn.linkedin.com/jobs/view/implementation-engineer-at-mnc-aero-4430958559 | https://fr.linkedin.com/in/aymen-mechria-0889391b3 | https://tn.linkedin.com/in/mohamed-rayen-ben-dhia-4835ab266",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — aucune offre junior adaptée actuellement confirmée",
        "notes": "L'adresse jamel.Fourti@mnc.aero fournie par l'utilisateur n'est pas retenue comme canal vérifié : Jamel Fourti ne paraît plus actuellement rattaché à MNC Aero. Candidature spontanée recommandée via l'adresse générale officielle.",
        "email_subject": "Spontaneous Application – Junior Implementation / Software & AI Engineer",
        "email_body": "Dear MNC Aero Team,\n\nI am a recently graduated Computer Engineer from ENSI, specialized in Financial Engineering, and I would like to submit a spontaneous application for a junior opportunity in implementation, software engineering, data or AI.\n\nMy final-year project at Linedata focused on modernizing a financial product through AI agents. This experience strengthened my ability to understand business processes, translate them into reliable software solutions and work at the intersection of technology and finance. MNC Aero particularly interests me because its work combines travel payments, revenue accounting, reconciliation and automation—an environment where my dual profile can create value.\n\nI am comfortable with Python, Java, C++, SQL, databases and full-stack development, and I am especially motivated by client-facing implementation work that requires analysis, communication and continuous learning. I would be grateful if you could consider my profile for a current or upcoming junior opportunity.\n\nMy CV is attached, and I remain available for an interview.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello Mr Mechria, I recently graduated from ENSI in Computer Engineering and Financial Engineering. MNC Aero's Travel FinTech and implementation work closely matches my background. I would be glad to connect and learn about upcoming junior opportunities.",
        "linkedin_followup": "Hello Mr Mechria, thank you for connecting. I have already sent MNC Aero a spontaneous application for a junior role in implementation, software or AI. My PFE at Linedata focused on modernizing a financial product with AI agents. If appropriate, could you please guide me toward the right team or future opening? I would be happy to share my CV here as well.",
    },
    {
        "organization_key": "amen bank",
        "sector": "Banque, services financiers et transformation digitale",
        "target_roles": "Ingénieur systèmes d'information junior; Data/AI Analyst junior; Auditeur informatique junior; IT Risk; automatisation et transformation digitale",
        "match_score_10": "8.5",
        "match_reason": "Le double profil informatique et ingénierie financière correspond aux fonctions SI, audit, risque et transformation d'une banque. Le PFE Linedata permet de relier l'IA à la modernisation de processus financiers sans limiter la candidature à un rôle purement technique.",
        "junior_status": "Oui",
        "junior_evidence": "La page carrière officielle d'Amen Bank indique explicitement que la banque recrute des profils seniors et juniors. Elle cite notamment les Systèmes d'Information, l'Audit, les Risques et les Marchés parmi ses fonctions support.",
        "active_jobs": "Aucune offre junior IT/Data/IA adaptée et encore ouverte n'a été confirmée le 2026-09-25. Candidature spontanée recommandée.",
        "linkedin_contact_name": "Page officielle Amen Bank",
        "linkedin_contact_role": "Canal entreprise — aucun recruteur individuel actuel vérifié",
        "linkedin_profile": "https://www.linkedin.com/company/amen-bank",
        "contact_verification": "La page LinkedIn officielle et le portail carrière officiel sont vérifiés. Aucun profil Talent Acquisition actuel suffisamment fiable n'a été identifié.",
        "verified_email": "recrutement@amenbank.com.tn",
        "email_status": "Adresse de recrutement publiée par Amen Bank sur sa page LinkedIn officielle.",
        "application_channel": "https://www.amenbank.com.tn/fr/candidature.html",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "70",
        "sources": "https://www.amenbank.com.tn/fr/carriere-metiers.html | https://www.amenbank.com.tn/fr/candidature.html | https://www.linkedin.com/company/amen-bank | https://fr.linkedin.com/posts/amen-bank_amenbank-amenfirstbank-joinus-activity-6913498196279181313-cVak",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — candidature spontanée",
        "notes": "Déposer aussi la candidature sur le portail officiel pour assurer son enregistrement dans la base RH.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | SI, Data/IA et audit IT",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite vous proposer ma candidature pour une première opportunité au sein d'Amen Bank, notamment dans les systèmes d'information, la Data et l'IA, l'audit informatique, le risque IT ou la transformation digitale.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Il m'a appris à partir d'un besoin métier financier pour concevoir une solution utile, fiable et adaptée aux utilisateurs. Cette double compréhension de l'informatique et de la finance correspond particulièrement aux enjeux de modernisation d'une banque.\n\nJe maîtrise notamment Python, Java, C++, SQL, les bases de données, le développement logiciel et les approches de machine learning et d'IA générative. Je suis surtout motivé par la possibilité de mettre ces compétences au service de processus bancaires plus efficaces, d'une meilleure exploitation des données et d'une maîtrise renforcée des risques.\n\nJe serais reconnaissant que mon profil puisse être étudié pour toute opportunité junior actuelle ou à venir en rapport avec ma formation. Vous trouverez mon CV en pièce jointe.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour, diplômé ingénieur ENSI en informatique et ingénierie financière, je m'intéresse aux opportunités junior SI, Data/IA, audit IT et transformation digitale chez Amen Bank. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour, merci pour l'ajout. J'ai déposé une candidature spontanée auprès d'Amen Bank. Mon PFE chez Linedata portait sur la modernisation d'un produit financier avec des agents IA. Pourriez-vous, si possible, m'indiquer l'équipe ou le contact adapté aux opportunités junior en SI, Data/IA ou audit informatique ?",
    },
    {
        "organization_key": "arab financial consultants",
        "sector": "Intermédiation en bourse, conseil financier et services d'investissement",
        "target_roles": "Analyste Data/finance junior; automatisation des processus financiers; Business Analyst junior; développement d'outils internes",
        "match_score_10": "6.8",
        "match_reason": "L'ingénierie financière et les compétences en données et automatisation sont pertinentes, mais AFC est une petite structure de courtage et aucune fonction IT/IA junior structurée ni offre correspondante n'a été trouvée.",
        "junior_status": "Non vérifiable",
        "junior_evidence": "Aucune politique junior, campagne jeunes diplômés ou offre junior récente n'a été trouvée dans les sources accessibles.",
        "active_jobs": "Aucune offre IT, Data ou IA active et adaptée n'a été trouvée le 2026-09-25.",
        "linkedin_contact_name": "Page officielle Arab Financial Consultants",
        "linkedin_contact_role": "Canal entreprise — aucun responsable RH actuel vérifié",
        "linkedin_profile": "https://www.linkedin.com/company/arab-financial-consultants",
        "contact_verification": "Page d'entreprise publique correspondant à AFC Tunis. Aucun contact RH individuel actuel n'a été vérifié.",
        "verified_email": "afc@afc.fin.tn",
        "email_status": "Adresse générale publiée sur la page officielle de l'entreprise ; ce n'est pas une adresse RH dédiée.",
        "application_channel": "http://www.afc.com.tn/",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "42",
        "sources": "https://www.linkedin.com/company/arab-financial-consultants | https://tn.linkedin.com/company/afc-arab-financial-consultants | http://www.afc.com.tn/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié partiellement — candidature spontanée de faible priorité",
        "notes": "Petite structure ; cibler la valeur métier, l'analyse et l'automatisation plutôt qu'un poste d'AI Engineer dédié.",
        "email_subject": "Candidature spontanée – Ingénieur informatique et ingénierie financière",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite vous adresser ma candidature spontanée pour une opportunité junior chez Arab Financial Consultants.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Ce parcours m'a permis de développer une double compréhension des besoins financiers et des solutions numériques, notamment en analyse de données, automatisation et développement d'outils logiciels.\n\nJe serais particulièrement intéressé par une mission dans laquelle je pourrais contribuer à fiabiliser l'information, automatiser des traitements ou soutenir l'analyse et les services d'investissement par des solutions digitales pragmatiques.\n\nJe vous joins mon CV et reste disponible pour échanger sur toute opportunité correspondant à mon profil, actuellement ou à l'avenir.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour, ingénieur ENSI récemment diplômé en informatique, spécialisé en ingénierie financière, je m'intéresse aux usages de la Data et de l'automatisation dans les services d'investissement. Je serais ravi de suivre AFC et d'échanger sur d'éventuels besoins juniors.",
        "linkedin_followup": "Bonjour, merci pour la connexion. J'ai adressé une candidature spontanée à AFC. Mon profil associe développement logiciel, Data/IA et ingénierie financière, avec un PFE réalisé chez Linedata. Si un besoin junior en analyse, automatisation ou outils financiers existe, je serais ravi de vous transmettre mon CV.",
    },
    {
        "organization_key": "arab tunisian bank",
        "sector": "Banque, systèmes d'information et transformation digitale",
        "target_roles": "Ingénieur IT junior; Data/AI Analyst junior; Auditeur informatique; Business Analyst bancaire; automatisation et transformation digitale",
        "match_score_10": "8.7",
        "match_reason": "Le profil informatique-finance et le PFE Linedata sont directement pertinents pour les SI bancaires, la Data/IA, l'audit IT et la transformation. Le rapport annuel 2023 indique que l'ATB avait recruté douze ingénieurs informatiques pour soutenir sa transformation digitale.",
        "junior_status": "Oui — recrutement récent à reconfirmer",
        "junior_evidence": "Le rapport annuel officiel 2023 mentionne le recrutement de douze ingénieurs informatiques. Une annonce secondaire de concours/recrutement ATB a circulé en 2026, mais les postes et l'état d'ouverture n'ont pas pu être confirmés sur une page officielle accessible.",
        "active_jobs": "Aucune offre junior IT/Data/IA officiellement confirmée comme encore ouverte le 2026-09-25. Ne pas présenter le concours relayé sur LinkedIn comme actif sans validation officielle.",
        "linkedin_contact_name": "Rihab Ghanmi Ep Kacem",
        "linkedin_contact_role": "Direction des Ressources Humaines — Arab Tunisian Bank",
        "linkedin_profile": "https://tn.linkedin.com/in/rihab-ghanmi-ep-kacem-a6984a331",
        "contact_verification": "Profil LinkedIn public actuellement rattaché à la Direction des Ressources Humaines de l'ATB ; fonction Talent Acquisition précise non confirmée.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse de recrutement officielle fiable trouvée. Ne pas déduire une adresse à partir du nom du contact.",
        "application_channel": "https://atb.tn/ | https://www.linkedin.com/company/arabtunisianbank/jobs/",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "64",
        "sources": "https://www.linkedin.com/company/arabtunisianbank | https://atb.tn/doc/rapports_annules/ATB_Rapport_Annuel_2023.pdf | https://tn.linkedin.com/in/rihab-ghanmi-ep-kacem-a6984a331 | https://ae.linkedin.com/posts/tunisie-travail-emploi_2026-%D8%A7%D9%84%D8%A8%D9%86%D9%83-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A-%D9%84%D8%AA%D9%88%D9%86%D8%B3-atb-%D9%8A%D9%81%D8%AA%D8%AD-%D9%85%D9%86%D8%A7%D8%B8%D8%B1%D8%A9-%D9%87%D8%A7%D9%85%D8%A9-activity-7471509286750429184-2CrE",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — canal LinkedIn, pas d'email RH public",
        "notes": "Contacter Rihab sur LinkedIn et surveiller le site/page officielle. L'annonce secondaire 2026 nécessite une confirmation avant toute candidature ciblée.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | SI bancaire, Data/IA et audit IT",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite soumettre ma candidature pour une opportunité junior au sein de l'Arab Tunisian Bank dans les systèmes d'information, la Data et l'IA, l'audit informatique, l'analyse métier ou la transformation digitale.\n\nMon PFE chez Linedata a consisté à moderniser un produit financier à l'aide d'agents d'intelligence artificielle. Cette expérience m'a permis de relier des enjeux métier financiers à la conception de solutions logicielles utiles et fiables. Je maîtrise notamment Python, Java, C++, SQL, les bases de données et le développement full-stack.\n\nLa place accordée par l'ATB aux compétences informatiques dans sa transformation digitale renforce mon intérêt. Je serais heureux de contribuer à des projets qui améliorent l'efficacité des processus, l'exploitation des données et la qualité des services bancaires.\n\nJe reste disponible pour toute opportunité junior actuelle ou future correspondant à mon diplôme et vous joins mon CV.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Ghanmi, ingénieur ENSI récemment diplômé en informatique et ingénierie financière, je m'intéresse aux opportunités junior en SI, Data/IA, audit IT et transformation digitale à l'ATB. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Ghanmi, merci pour la connexion. Mon PFE chez Linedata portait sur la modernisation d'un produit financier avec des agents IA. Je recherche une première opportunité en SI bancaire, Data/IA, audit IT ou analyse métier. Pourriez-vous, si possible, m'indiquer le canal approprié pour transmettre mon CV à l'ATB ?",
    },
    {
        "organization_key": "assurances biat",
        "sector": "Assurance, services financiers et transformation digitale",
        "target_roles": "Data/AI Analyst junior; ingénieur systèmes d'information; Business Analyst assurance; automatisation; audit et risque IT",
        "match_score_10": "8.0",
        "match_reason": "L'ingénierie financière, l'IA et le développement logiciel sont pertinents pour la donnée, l'automatisation, les SI, le risque et la transformation de l'assurance. Aucune offre junior ciblée n'est toutefois visible.",
        "junior_status": "Non vérifiable",
        "junior_evidence": "Aucune campagne junior IT/Data récente et officielle n'a été trouvée. L'adresse candidature.agents concerne le recrutement d'agents généraux et ne doit pas être utilisée pour une candidature informatique.",
        "active_jobs": "Aucune offre junior IT, Data ou IA adaptée et encore ouverte n'a été confirmée le 2026-09-25.",
        "linkedin_contact_name": "Rafaa Jemli",
        "linkedin_contact_role": "Responsable RH / membre de la direction Assurances BIAT",
        "linkedin_profile": "https://tn.linkedin.com/in/rafaa-jemli-8a507910",
        "contact_verification": "Profil public actuellement rattaché à Assurances BIAT ; des sources récentes le présentent dans un rôle de direction couvrant les RH. Le titre exact affiché sur le profil public n'est pas entièrement exposé.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucune adresse RH générale adaptée n'a été trouvée. candidature.agents@assurancesbiat.com.tn est réservée à la campagne d'agents généraux et est volontairement exclue.",
        "application_channel": "https://www.linkedin.com/company/assurancesbiat | https://www.assurancesbiat.com.tn/",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "52",
        "sources": "https://www.linkedin.com/company/assurancesbiat | https://tn.linkedin.com/in/rafaa-jemli-8a507910 | https://fr.linkedin.com/posts/assurancesbiat_et-si-vous-deveniez-votre-propre-patron-activity-7292919320261586944-AiN6 | https://fr.linkedin.com/posts/med-rh_medrh2025-leadership-culture-activity-7393956202646257664-aBRa",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — contact LinkedIn, aucun email RH adapté",
        "notes": "Approche LinkedIn recommandée. Ne pas utiliser l'adresse de recrutement des agents généraux pour un profil ingénieur IT/IA.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | Data/IA et transformation de l'assurance",
        "email_body": "Bonjour Monsieur Jemli,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je souhaite vous soumettre ma candidature pour une première opportunité chez Assurances BIAT dans les systèmes d'information, la Data et l'IA, l'automatisation, l'analyse métier ou le risque IT.\n\nLors de mon PFE chez Linedata, j'ai contribué à la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Cette expérience m'a appris à relier un besoin métier à une solution numérique concrète, avec une attention particulière portée à la fiabilité et à la valeur pour les utilisateurs.\n\nMon profil associe développement logiciel, bases de données, machine learning, IA générative et compréhension des services financiers. Je serais particulièrement motivé par des projets permettant d'améliorer les processus, l'exploitation des données et l'expérience client dans l'assurance.\n\nJe serais heureux de vous transmettre mon CV et d'échanger sur toute opportunité junior actuelle ou future correspondant à mon parcours.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Jemli, ingénieur ENSI récemment diplômé en informatique et ingénierie financière, je m'intéresse aux opportunités junior en SI, Data/IA et transformation digitale chez Assurances BIAT. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Jemli, merci pour la connexion. Mon PFE chez Linedata portait sur la modernisation d'un produit financier avec des agents IA. Je recherche une première opportunité en SI, Data/IA, automatisation ou analyse métier. Pourrais-je vous transmettre mon CV afin d'être orienté vers l'équipe appropriée ?",
    },
]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(RECORDS[0])
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(RECORDS)
    print(f"Wrote {len(RECORDS)} records to {OUT}")


if __name__ == "__main__":
    main()
