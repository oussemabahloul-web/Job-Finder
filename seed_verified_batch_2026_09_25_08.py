#!/usr/bin/env python3
"""Verified research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_08.csv"

RECORDS = [
    {
        "organization_key": "gina cody school of engineering and computer science",
        "sector": "Université, recherche et enseignement en informatique, génie logiciel, cybersécurité et IA",
        "target_roles": "Research Assistant en IA/logiciel; Research Associate; développeur de recherche; candidat Master/PhD financé en informatique ou cybersécurité",
        "match_score_10": "5.8",
        "match_reason": "Les domaines scientifiques correspondent à l'informatique, l'IA et la cybersécurité, mais l'organisme recrute surtout des enseignants-chercheurs, postdoctorants et étudiants déjà inscrits. Le candidat recherche un premier emploi d'ingénieur et ne possède pas encore le doctorat ou le statut étudiant Concordia requis pour la majorité des rôles.",
        "junior_status": "Oui, principalement pour ses propres étudiants",
        "junior_evidence": "Les assistantships et rôles TA sont réservés aux étudiants inscrits; la page CSSE indique qu'aucun Research Assistantship n'est ouvert. Les postes académiques exigent généralement un profil de recherche avancé.",
        "active_jobs": "Aucun Research Assistantship CSSE ouvert le 2026-09-25 — https://www.concordia.ca/ginacody/computer-science-software-eng/about/jobs.html. La page générale liste des opportunités de recherche dans d'autres disciplines et des admissions PhD/MASc en sécurité, mais pas un emploi junior logiciel/IA adapté — https://www.concordia.ca/ginacody/about/jobs.html.",
        "linkedin_contact_name": "Aucun contact RH LinkedIn actuel suffisamment fiable identifié",
        "linkedin_contact_role": "Utiliser l'équipe Talent de Concordia et le portail officiel",
        "linkedin_profile": "https://www.linkedin.com/school/concordia-university/",
        "contact_verification": "Aucun profil personnel actuel n'a été retenu faute de preuve suffisante d'un rôle de recrutement pour Gina Cody School.",
        "verified_email": "hr-employment@concordia.ca",
        "email_status": "Adresse de l'équipe Talent publiée sur la page officielle destinée aux candidats externes. reception@ece.concordia.ca du CSV est un accueil départemental et non un canal de recrutement.",
        "application_channel": "https://www.concordia.ca/hr/jobs/openings/external-candidates.html",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "24",
        "foreign_employee_status": "Oui, sous conditions strictes",
        "foreign_employee_evidence": "Concordia détaille une procédure de permis de travail pour certains recrutements internationaux, mais donne priorité aux citoyens/résidents permanents pour les postes académiques. Les postes à temps partiel exigent déjà la citoyenneté, la résidence permanente ou un permis ouvert; les assistantships exigent l'inscription comme étudiant.",
        "sources": "https://www.concordia.ca/ginacody/about/jobs.html | https://www.concordia.ca/ginacody/computer-science-software-eng/about/jobs.html | https://www.concordia.ca/hr/jobs/openings/external-candidates.html | https://www.concordia.ca/provost/resources/new-hires/work-permits.html",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — aucune ouverture junior professionnelle adaptée; restrictions académiques et permis documentées",
        "notes": "Faible priorité pour un emploi immédiat. Ne pas envoyer une candidature générique au département. Créer une alerte sur le portail externe ou viser une admission Master/PhD financée seulement si le candidat souhaite poursuivre des études/recherche.",
        "email_subject": "Inquiry – Early-Career AI/Software Research Opportunities",
        "email_body": "Dear Concordia Talent Team,\n\nI am a recent Computer Engineering graduate from ENSI in Tunisia with a specialisation in Financial Engineering. My final-year project at Linedata focused on modernising a financial software product with AI agents, and my background includes Python, Java, C++, full-stack development, databases, machine learning and generative AI.\n\nI reviewed the current Gina Cody School opportunities and understand that research assistantships are not presently open and that many teaching roles require current Concordia student status or an existing Canadian work permit. I am therefore not submitting an application for a role for which I am ineligible.\n\nCould you please advise whether externally recruited early-career research software, AI or cybersecurity positions are sometimes published through the Concordia Careers portal, and whether such positions may consider an international applicant requiring a work permit? I will continue monitoring the official portal and apply only to a matching opening.\n\nThank you for your guidance.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello, I am a recent ENSI Computer Engineering graduate interested in future AI/software research opportunities at Concordia's Gina Cody School. I understand current assistantships are mainly student roles and will follow the official portal for eligible openings. I would be glad to follow your network.",
        "linkedin_followup": "Hello, thank you for connecting. My background combines software engineering, AI agents and financial engineering. I am monitoring Concordia's official careers portal for an early-career research software/AI role open to external international candidates. If you know the appropriate team or alert to follow, I would appreciate your guidance.",
    },
    {
        "organization_key": "it grow",
        "sector": "Agence digitale, développement web/mobile, produit, UX/UI, marketing et solutions intégrant l'IA",
        "target_roles": "Junior Full-stack Developer; Software Engineer junior; AI-enabled Product Developer; développeur web/mobile; Product/Business Analyst junior",
        "match_score_10": "7.8",
        "match_reason": "Le développement web/mobile, les produits numériques et certains cas d'usage IA correspondent au full-stack et au profil logiciel. L'activité reste toutefois très orientée agence, marque et marketing, avec moins de profondeur Data/IA que les cibles prioritaires du candidat.",
        "junior_status": "Oui",
        "junior_evidence": "IT Grow a publié plusieurs stages, une campagne PFE 2025 fondée sur de vrais produits livrés et des opportunités de stage immédiat. L'entreprise est récemment devenue House of Growth avec la même équipe tunisienne.",
        "active_jobs": "Aucune opportunité technique actuelle sur la page carrière officielle le 2026-09-25, qui affiche explicitement « no career opportunities available ». Une annonce de stage Community Manager/Content Creator est visible mais ne correspond pas au profil ingénieur. Candidature spontanée uniquement — https://it-grow.tn/career.",
        "linkedin_contact_name": "Sami Arif",
        "linkedin_contact_role": "Fondateur/dirigeant — IT Grow, désormais House of Growth",
        "linkedin_profile": "https://tn.linkedin.com/in/sami-arif-029a95186",
        "contact_verification": "Profil actuel, activité récente et publication de stages IT Grow; il confirme le changement de marque vers House of Growth sans changement d'équipe tunisienne.",
        "verified_email": "hello@it-grow.tn",
        "email_status": "Adresse publiée sur la page carrière officielle. L'adresse mohamed.hmida@it-grow.tn est liée à un ancien stage marketing et n'est pas retenue pour une candidature technique.",
        "application_channel": "mailto:hello@it-grow.tn | https://it-grow.tn/career",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "55",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Équipe et bureau à Ennasr 2, Ariana.",
        "sources": "https://it-grow.tn/career | https://www.linkedin.com/company/wemakeitgrow | https://tn.linkedin.com/in/sami-arif-029a95186",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — entreprise junior-friendly, aucune ouverture technique actuelle",
        "notes": "Priorité moyenne. Mentionner House of Growth dans le message pour montrer que la recherche est à jour. Ne pas candidater au stage Community Manager. Envoyer une candidature spontanée centrée produit/full-stack/IA appliquée.",
        "email_subject": "Candidature spontanée – Ingénieur logiciel junior | Full-stack et IA",
        "email_body": "Bonjour Monsieur Arif,\n\nJe souhaite vous proposer ma candidature spontanée pour une première opportunité en développement logiciel, produit numérique ou IA appliquée au sein de House of Growth, anciennement IT Grow.\n\nRécemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, j'ai réalisé mon PFE chez Linedata sur la modernisation d'un produit financier à l'aide d'agents IA. Cette expérience m'a appris à comprendre un besoin métier, construire une solution intégrée et penser au produit dans son ensemble. Je maîtrise notamment Python, Java, C++, le développement full-stack web/mobile/desktop, les APIs, les bases de données, le machine learning et les LLM.\n\nVotre manière d'unifier produit, marque et distribution m'intéresse particulièrement : je souhaite rejoindre une équipe où l'ingénieur ne se limite pas à exécuter une fonctionnalité, mais comprend l'usage et la valeur qu'elle doit créer.\n\nVotre page carrière n'affichant actuellement aucun poste technique, je vous transmets mon CV pour tout besoin junior actuel ou futur en software, full-stack ou produit enrichi par l'IA. Je reste disponible pour un échange.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Arif, jeune diplômé ingénieur ENSI, je suis le passage d'IT Grow à House of Growth avec intérêt. Mon profil associe full-stack, logiciel et IA agentique, avec un PFE produit chez Linedata. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Arif, merci pour la connexion. J'ai envoyé une candidature spontanée à hello@it-grow.tn pour un futur besoin junior software/full-stack/IA. Votre approche qui relie produit, marque et distribution correspond à ma volonté de construire des solutions utiles au-delà du code. Je reste disponible pour vous transmettre mon CV ici.",
    },
    {
        "organization_key": "it serv",
        "sector": "ESN, développement logiciel, Java/.NET, intégration, Business Intelligence, télécoms, santé et transformation digitale",
        "target_roles": "Junior Software Engineer; développeur Java/.NET junior; Full-stack Developer junior; ingénieur intégration/API; BI/Data junior; QA/Test Engineer",
        "match_score_10": "8.2",
        "match_reason": "Java, développement full-stack, SQL, APIs et intégration correspondent aux centres de compétences IT SERV. L'IA agentique est moins centrale que le développement d'applications et l'intégration, mais le profil d'ingénieur logiciel reste cohérent.",
        "junior_status": "Oui",
        "junior_evidence": "Le PFE Book 2026 présente des stages pré-embauche, un encadrement par des experts et plusieurs sujets logiciels. Une ancienne offre .NET acceptait un Bac+5 avec PFE ou première expérience, preuve d'accès aux jeunes diplômés.",
        "active_jobs": "Aucune offre junior adaptée confirmée ouverte le 2026-09-25. L'offre Développeur Java Confirmé publiée en 2026 exige au moins trois ans et affiche « ne prend plus de candidatures »; elle est exclue des offres actives — https://tn.linkedin.com/jobs/view/d%C3%A9veloppeur-java-confirm%C3%A9-at-it-serv-4375507409. Candidature spontanée via l'adresse recrutement.",
        "linkedin_contact_name": "Moez Boukhris",
        "linkedin_contact_role": "Founder & CTO — IT SERV",
        "linkedin_profile": "https://tn.linkedin.com/in/moez-boukhris-68a0674",
        "contact_verification": "Fondateur et CTO actuel, auteur de l'annonce Java 2026 et de contenus sur l'ouverture aux jeunes talents.",
        "verified_email": "recrutement@itserv.tn",
        "email_status": "Adresse publiée dans plusieurs annonces officielles IT SERV, dont l'offre Java 2026. L'adresse générale itserv@itserv.tn reste valide sur le site, mais recrutement@ est le meilleur canal.",
        "application_channel": "mailto:recrutement@itserv.tn | https://itserv.tn/carrieres-it-en-tunisie/",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "68",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Candidature au bureau d'El Menzah, Tunis.",
        "sources": "https://itserv.tn/en/it-careers/ | https://itserv.tn/carrieres-it-en-tunisie/ | https://itserv.tn/wp-content/uploads/2025/12/IT-SERV-PFE-Book-2026.pdf | https://tn.linkedin.com/jobs/view/d%C3%A9veloppeur-java-confirm%C3%A9-at-it-serv-4375507409 | https://tn.linkedin.com/in/moez-boukhris-68a0674",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — stages pré-embauche et email recrutement, aucune offre junior ouverte confirmée",
        "notes": "Priorité moyenne-haute en candidature spontanée. Ne pas postuler à l'offre Java Confirmé. Mettre en avant Java, SQL, REST/API, Git, full-stack et capacité d'intégration, puis l'IA comme compétence additionnelle.",
        "email_subject": "Candidature spontanée – Ingénieur logiciel junior | Java, Full-stack et intégration",
        "email_body": "Bonjour Monsieur Boukhris,\n\nRécemment diplômé ingénieur en informatique de l'ENSI, je souhaite proposer ma candidature spontanée à IT SERV pour une première opportunité en développement logiciel, intégration ou Data/BI.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. J'y ai renforcé ma capacité à comprendre un produit existant, développer des composants fiables et intégrer des services autour d'un besoin métier. Je maîtrise Java, Python, C++, le développement full-stack, SQL, les bases de données, les APIs REST, Git ainsi que les fondamentaux du machine learning et de l'IA générative.\n\nLes activités d'IT SERV en développement, intégration et transformation digitale correspondent à la base d'ingénierie logicielle que je souhaite consolider. Je sais que votre offre Java récente demandait trois ans d'expérience et qu'elle n'est plus ouverte; ma démarche concerne donc un besoin véritablement junior actuel ou futur, et non ce poste confirmé.\n\nJe joins mon CV et serais ravi d'échanger sur toute équipe où mon profil polyvalent pourrait apporter de la valeur tout en continuant à progresser.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Monsieur Boukhris, jeune diplômé ingénieur ENSI, je m'intéresse à IT SERV pour une première opportunité software/intégration. Je maîtrise Java, Python, C++, full-stack, SQL et APIs; mon PFE Linedata portait sur des agents IA. Je serais ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Monsieur Boukhris, merci pour la connexion. J'ai envoyé à recrutement@itserv.tn une candidature spontanée pour un futur besoin junior, distinct de l'offre Java Confirmé. Mon profil associe Java/full-stack/intégration et IA appliquée. Je serais reconnaissant si mon CV pouvait être conservé pour une équipe adaptée.",
    },
    {
        "organization_key": "kauz gmbh",
        "sector": "Plateforme GenAI, CompanyGPT, chatbots, agents IA, RAG, workflows et NLP",
        "target_roles": "Junior AI/LLM Engineer; Python/NLP Developer junior; RAG/Agent Engineer junior; Software Engineer junior; AI Product Engineer",
        "match_score_10": "8.8",
        "match_reason": "Les agents, assistants d'entreprise, workflows et LLM de Kauz correspondent très fortement au PFE agentique et aux compétences Python/LLM/logiciel. Les obstacles sont l'absence d'offre technique junior actuelle, l'allemand généralement requis et l'absence d'engagement public sur le visa/relocation.",
        "junior_status": "Oui, mais ouverture actuelle hors profil",
        "junior_evidence": "Kauz publie actuellement un poste Junior Content Marketing Manager explicitement conçu pour l'entrée dans la vie professionnelle et accepte aussi des étudiants salariés; cela démontre l'ouverture junior, sans prouver un besoin technique junior.",
        "active_jobs": "Junior Content Marketing Manager — Düsseldorf/remote partiel — actif le 2026-09-25, allemand et anglais excellents, portfolio de contenu requis — https://de.linkedin.com/jobs/view/junior-content-marketing-manager-m-w-d-at-kauz-ai-4437182935. Poste non recommandé car marketing et allemand. Aucune offre AI/software junior ouverte confirmée.",
        "linkedin_contact_name": "Cheryl Hodgkinson",
        "linkedin_contact_role": "Head of Product / interlocutrice indiquée dans l'offre junior actuelle — Kauz.ai",
        "linkedin_profile": "https://de.linkedin.com/in/cheryl-hodgkinson-0b185b247",
        "contact_verification": "Profil Kauz.ai actuel et actif en 2026; l'offre Junior Content Marketing la désigne directement comme interlocutrice.",
        "verified_email": "jobs@kauz.ai",
        "email_status": "Adresse publiée dans l'offre junior actuelle et dans une annonce étudiante 2026. info@kauz.ai du CSV est une adresse générale; jobs@ est le canal recrutement approprié.",
        "application_channel": "mailto:jobs@kauz.ai | https://www.linkedin.com/company/kauz-gmbh/jobs/",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "34",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "L'offre actuelle autorise une grande flexibilité de lieu mais prévoit des rencontres régulières à Düsseldorf et exige un excellent allemand. Elle ne mentionne ni visa, ni relocation, ni recrutement hors UE; ne pas interpréter « remote » comme international.",
        "sources": "https://www.linkedin.com/company/kauz-gmbh/ | https://de.linkedin.com/jobs/view/junior-content-marketing-manager-m-w-d-at-kauz-ai-4437182935 | https://www.w-hs.de/fileadmin/user_upload/form_5a06f14dd2db14b8814a02066ba9682640d208af/2026_Kauz_Werkstudent_CSM.pdf | https://de.linkedin.com/in/cheryl-hodgkinson-0b185b247 | https://de.linkedin.com/in/thomas-ruedel-92980985",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — forte adéquation technique, mais aucune offre technique junior et mobilité non documentée",
        "notes": "Candidature étrangère de faible priorité malgré l'excellente adéquation technique. Ne pas postuler au poste marketing sans allemand/portfolio. Envoyer seulement une demande ciblée pour un futur rôle AI/software et demander explicitement si anglais seul et visa sont envisageables.",
        "email_subject": "Spontaneous Application – Junior AI/LLM Software Engineer",
        "email_body": "Dear Ms Hodgkinson,\n\nI am a recent Computer Engineering graduate from ENSI in Tunisia, and I am writing to express interest in a future junior AI or software engineering opportunity at Kauz.ai.\n\nMy final-year project at Linedata focused on modernising a financial product with AI agents. I worked on translating business needs into agent workflows and integrating them into an existing software product. My background includes Python, LLMs, RAG concepts, APIs, databases, Java, C++ and full-stack development. Kauz.ai's work on enterprise assistants, grounded knowledge, workflows and production-ready agentic AI is therefore especially relevant to the direction I want to pursue.\n\nI reviewed your current Junior Content Marketing Manager opening and understand that it is a marketing role requiring excellent German, so I am not applying to an unsuitable position. Instead, I would be grateful to know whether Kauz.ai may consider a future English-speaking junior AI/software profile based outside the EU and requiring work authorisation or relocation support.\n\nI attach my CV for context and would welcome an opportunity to discuss a genuinely matching opening.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello Ms Hodgkinson, I am a recent ENSI Computer Engineering graduate specialising in AI agents and software. Kauz.ai's enterprise assistants and agentic workflows strongly match my Linedata final project. I know the current junior role is marketing-focused, but I would be glad to connect for future AI roles.",
        "linkedin_followup": "Hello Ms Hodgkinson, thank you for connecting. I sent a targeted inquiry to jobs@kauz.ai for a future junior AI/software opening, rather than applying to the current marketing role. As I am based in Tunisia, I also asked whether an English-speaking candidate requiring work authorisation could ever be considered. I would value your guidance.",
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
