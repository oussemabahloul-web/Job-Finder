#!/usr/bin/env python3
"""Verified mixed Tunisia/foreign research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path


OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_03.csv"


RECORDS = [
    {
        "organization_key": "bnp paribas",
        "sector": "Banque internationale, assurance, IT, Data et intelligence artificielle",
        "target_roles": "Applied AI Engineer; Data/AI Analyst junior; Software Engineer; Business Analyst bancaire; IT risk et transformation",
        "match_score_10": "9.1",
        "match_reason": "L'offre Applied AI Engineer RAG & Agentic AI correspond directement au PFE Linedata, à Python, aux LLM, au RAG et à l'IA agentique, tout en valorisant la compréhension des métiers financiers. Elle demande toutefois une première expérience professionnelle significative, ce qui rend la candidature ambitieuse.",
        "junior_status": "Oui",
        "junior_evidence": "BNP Paribas propose des parcours premier emploi et Graduate Programmes. L'offre Applied AI Engineer est classée « Je recherche mon premier emploi », malgré l'exigence d'une première expérience significative en IA.",
        "active_jobs": "Applied AI Engineer RAG & Agentic AI H/F — CDI — Nanterre, France — mise à jour 2026-09-23 — https://group.bnpparibas/emploi-carriere/offre-emploi/applied-ai-engineer-rag-agentic-ai-h-f | Stage AI Project Officer Junior — Paris — https://group.bnpparibas/emploi-carriere/toutes-offres-emploi/transformation-numerique-data/france",
        "linkedin_contact_name": "Elodie Crouin",
        "linkedin_contact_role": "Staffing Business Partner / Early Careers — BNP Paribas",
        "linkedin_profile": "https://fr.linkedin.com/in/elodie-crouin-64a223b6",
        "contact_verification": "Profil public actuel BNP Paribas avec activité récente et explicite sur le recrutement Early Careers.",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Les deux adresses BNP du CSV sont invalides/incomplètes et sont exclues. missionhandicap@bnpparibas.com est réservé aux candidatures liées au handicap et ne doit pas être utilisé comme email général.",
        "application_channel": "https://group.bnpparibas/emploi-carriere/offre-emploi/applied-ai-engineer-rag-agentic-ai-h-f",
        "recommended_cv": "CV_ATS_Fintech.pdf",
        "language": "Français",
        "potential_score_100": "69",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "L'offre française ne précise ni parrainage de visa ni relocation. Un candidat tunisien doit donc vérifier son éligibilité au travail en France dans le formulaire ; ne pas supposer une prise en charge du titre de séjour.",
        "sources": "https://group.bnpparibas/emploi-carriere/offre-emploi/applied-ai-engineer-rag-agentic-ai-h-f | https://group.bnpparibas/emploi-carriere/metiers/it-tech-et-data | https://group.bnpparibas/emploi-carriere/candidat-jeune-professionnel/graduate-programmes/tech-transformation | https://fr.linkedin.com/in/elodie-crouin-64a223b6",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — offre IA active, mobilité internationale non précisée",
        "notes": "Candidature ambitieuse mais cohérente. Le Tech Graduate Programme Développeur repéré est déjà pourvu et n'est pas listé comme actif. Postuler uniquement par le portail officiel.",
        "email_subject": "Candidature – Applied AI Engineer RAG & Agentic AI H/F",
        "email_body": "Bonjour Madame, Monsieur,\n\nJe souhaite vous présenter ma candidature au poste d'Applied AI Engineer RAG & Agentic AI. Récemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, j'ai précisément construit mon parcours à l'intersection de l'IA, du logiciel et des services financiers.\n\nLors de mon PFE chez Linedata, j'ai contribué à moderniser un produit financier à l'aide d'agents IA. J'ai ainsi travaillé sur la compréhension d'un besoin métier, la conception de workflows agentiques, l'exploitation de modèles de langage et l'intégration de la solution dans un produit existant. Cette expérience m'a surtout appris à rechercher une IA utile, fiable et compréhensible pour ses utilisateurs.\n\nJe maîtrise Python, le développement logiciel, les bases de données, les APIs et les concepts de RAG, de LLM et d'agents. La dimension transverse du poste chez BNP Paribas Cardif—de l'identification des cas d'usage à l'industrialisation et à l'accompagnement des métiers—correspond particulièrement à mon projet professionnel.\n\nMême en début de carrière, je peux apporter une expérience récente et directement alignée, une forte capacité d'apprentissage et une double lecture technique et financière. Je suis mobile pour la France, sous réserve des formalités d'autorisation de travail, et reste disponible pour un entretien.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Madame Crouin, jeune ingénieur ENSI spécialisé en ingénierie financière, je candidate au poste Applied AI Engineer RAG & Agentic AI. Mon PFE Linedata portait précisément sur des agents IA appliqués à un produit financier. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Madame Crouin, merci pour la connexion. J'ai candidaté via le portail au poste Applied AI Engineer. Mon PFE chez Linedata concernait l'IA agentique appliquée à la modernisation d'un produit financier. Étant candidat tunisien mobile pour la France, pourriez-vous m'indiquer si ce poste peut étudier un dossier nécessitant une autorisation de travail ?",
    },
    {
        "organization_key": "colombus capital",
        "sector": "FinTech, marchés de change, trésorerie et analyse financière",
        "target_roles": "Trading & Sales junior; analyste marchés/FX junior; Data/finance analyst; automatisation et développement FinTech",
        "match_score_10": "8.4",
        "match_reason": "La spécialisation en ingénierie financière est directement pertinente pour l'offre Trading & Sales destinée aux jeunes diplômés. Les compétences Data/IA et logiciel constituent un complément utile dans une FinTech fondée sur l'analyse et la technologie, même si le poste est davantage marché et relation client que développement.",
        "junior_status": "Oui",
        "junior_evidence": "Une publication de l'entreprise datant d'environ deux mois invite explicitement les recent graduates à candidater au rôle Trading & Sales ; une publication antérieure visait aussi les étudiants PFE et jeunes diplômés.",
        "active_jobs": "Trading & Sales Talent — Tunis — publication entreprise accessible, environ 2 mois — candidature à confirmer par email — https://www.linkedin.com/company/colombus-capital-the-infinite-trust",
        "linkedin_contact_name": "Faten Sidhom",
        "linkedin_contact_role": "Software Engineer — Colombus Capital",
        "linkedin_profile": "https://tn.linkedin.com/in/faten-sidhom",
        "contact_verification": "Profil actuellement rattaché à Colombus Capital. Contact technique pertinent pour comprendre la composante produit/tech ; pas recruteuse RH.",
        "verified_email": "contact@colombus-capital.com | Yosr.BenAmar@colombus-capital.com",
        "email_status": "Les deux adresses ont été publiées par la page officielle Colombus Capital dans sa campagne récente Trading & Sales.",
        "application_channel": "mailto:contact@colombus-capital.com | https://www.linkedin.com/company/colombus-capital-the-infinite-trust",
        "recommended_cv": "CV_ATS_Fintech_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "87",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Poste local à Tunis.",
        "sources": "https://www.linkedin.com/company/colombus-capital-the-infinite-trust | https://tn.linkedin.com/in/faten-sidhom",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — campagne junior récente et emails publiés",
        "notes": "Envoyer à contact@colombus-capital.com avec Yosr.BenAmar@colombus-capital.com en copie. Mettre en avant finance de marché, analyse et capacité client ; ne pas présenter le profil comme uniquement technique.",
        "email_subject": "Application – Junior Trading & Sales / FinTech Analyst",
        "email_body": "Dear Colombus Capital Team,\n\nI am applying for the recent Trading & Sales opportunity at Colombus Capital. I recently graduated as a Computer Engineer from ENSI with a specialization in Financial Engineering, and I am looking for a first role where financial markets, analytical thinking and technology reinforce one another.\n\nMy final-year project at Linedata focused on modernizing a financial product with AI agents. Beyond the technical work, it trained me to understand financial workflows, turn complex information into clear decisions and communicate effectively with both business and technical stakeholders. I also bring strong foundations in Python, SQL, data analysis and software development.\n\nWhat attracts me to Colombus Capital is the opportunity to work directly with FX markets and clients in a FinTech environment driven by data and performance. I am motivated to learn trade execution and treasury solutions quickly, prepare disciplined market insights and contribute to client relationships with clarity and reliability.\n\nPlease find my CV attached. I would welcome the opportunity to discuss how my combined finance and technology background could contribute to your team.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello Ms Sidhom, I am a recent ENSI Computer Engineering graduate specialized in Financial Engineering. I am applying to Colombus Capital's junior Trading & Sales opportunity and am particularly interested in its FinTech and data-driven environment. Glad to connect.",
        "linkedin_followup": "Hello Ms Sidhom, thank you for connecting. I have sent my application to Colombus Capital for the recent junior Trading & Sales opportunity. My background combines financial engineering, software, Data/AI and a final-year project at Linedata. If appropriate, could you share how technology profiles contribute to the team or point me to the right colleague?",
    },
    {
        "organization_key": "agence nationale de la cyber securite",
        "sector": "Cybersécurité nationale, audit des SI, réponse aux incidents et sécurité des réseaux",
        "target_roles": "Ingénieur cybersécurité junior; analyste SOC/CSIRT junior; audit SI; sécurité applicative; automatisation et IA pour la cybersécurité",
        "match_score_10": "7.8",
        "match_reason": "Le diplôme informatique, Python, le développement et les bases en cybersécurité sont pertinents, notamment pour l'automatisation et l'IA appliquées à la détection. Le CV ne démontre toutefois pas encore une spécialisation cyber aussi forte que les profils SOC, réseau ou audit dédiés.",
        "junior_status": "Oui — stages et formation observés, recrutement actuel non vérifié",
        "junior_evidence": "Des profils étudiants et jeunes diplômés documentent des stages récents à l'ANCS, et l'agence co-construit un mastère en cybersécurité opérationnelle. Aucun concours ou recrutement junior ouvert n'a été trouvé le 2026-09-25.",
        "active_jobs": "Aucun concours ou poste junior ANCS officiellement ouvert et adapté n'a été confirmé le 2026-09-25. L'appel à détachement d'ingénieurs trouvé date de trois ans et n'est pas actif.",
        "linkedin_contact_name": "Dr. Eng. Yacine Djemaiel",
        "linkedin_contact_role": "Directeur général / Head of ANCS Tunisie",
        "linkedin_profile": "https://tn.linkedin.com/in/dr-eng-yacine-djemaiel-63582153",
        "contact_verification": "Profil public actuellement rattaché à ANCS-tunCERT et identifié dans des événements 2025-2026 comme Head of Tunisia's National Cybersecurity Agency.",
        "verified_email": "ancs@ancs.tn",
        "email_status": "Adresse générale publiée sur la page de contact officielle ; aucune adresse RH dédiée n'est publique.",
        "application_channel": "https://www.ancs.tn/fr/contactez-nous | https://www.linkedin.com/company/ancs-tuncert",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "55",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Organisme public tunisien situé à Tunis.",
        "sources": "https://www.ancs.tn/fr/contactez-nous | https://www.linkedin.com/company/ancs-tuncert | https://tn.linkedin.com/in/dr-eng-yacine-djemaiel-63582153 | https://fr.linkedin.com/posts/ancs-tuncert-80bb4b172_lagence-nationale-de-la-s%C3%A9curit%C3%A9-informatique-activity-7062835424934678528-fhqk",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — candidature spontanée, aucune ouverture actuelle",
        "notes": "Canal public général uniquement. La candidature doit rester une demande d'orientation et ne remplace pas un éventuel concours ou appel officiel.",
        "email_subject": "Candidature spontanée – Ingénieur informatique junior | Cybersécurité, automatisation et IA",
        "email_body": "Bonjour Madame, Monsieur,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, je souhaite manifester mon intérêt pour toute future opportunité junior à l'Agence Nationale de la Cybersécurité dans l'analyse, l'audit des systèmes d'information, la sécurité applicative ou l'automatisation des activités cyber.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents d'intelligence artificielle. Cette expérience m'a permis de renforcer mes compétences en Python, développement logiciel, APIs, bases de données et IA, tout en accordant une attention particulière à la fiabilité, au contrôle et à l'intégration dans un environnement métier sensible.\n\nJe maîtrise également Java, C++, le développement full-stack et les principes fondamentaux de cybersécurité. Je souhaite approfondir ce domaine dans un environnement exigeant où mes compétences en logiciel et en IA pourraient contribuer à l'automatisation, à l'analyse des menaces et à la résilience des systèmes.\n\nJe comprends que les recrutements de l'ANCS peuvent suivre des procédures spécifiques. Je vous serais reconnaissant de m'indiquer le canal approprié pour les futurs besoins ou concours correspondant à mon profil. Mon CV est joint.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Djemaiel, jeune ingénieur ENSI en informatique, je m'intéresse à l'IA et à l'automatisation appliquées à la cybersécurité. Le rôle national de l'ANCS et ses travaux sur la cyber à l'ère de l'IA motivent ma démarche. Je serais honoré de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Djemaiel, merci pour la connexion. Mon PFE chez Linedata portait sur des agents IA intégrés à un produit financier. Je souhaite orienter mes compétences Python, logiciel et IA vers la cybersécurité. Pourriez-vous, si possible, m'indiquer les futurs concours, stages professionnels ou équipes ANCS à suivre pour un jeune ingénieur ?",
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
