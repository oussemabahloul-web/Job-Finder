#!/usr/bin/env python3
"""Verified research batch checked on 2026-09-25."""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_09.csv"

RECORDS = [
    {
        "organization_key": "laboratoire cnrs irit institut de recherche en informatique toulouse",
        "sector": "Recherche publique en informatique, IA, Data, NLP, systèmes, réseaux et interaction humain-machine",
        "target_roles": "Ingénieur de recherche junior en IA/Data; Research Software Engineer; ingénieur NLP/LLM; doctorant contractuel; stage de recherche Master 2",
        "match_score_10": "8.4",
        "match_reason": "L'IA agentique, Python, le logiciel et les LLM correspondent à plusieurs équipes IRIT. Une offre 2026 en IA éducative recherchait même un ingénieur 0–3 ans avec Python, web, clustering et chatbot. Le principal écart est l'orientation recherche académique et l'absence d'ouverture encore active.",
        "junior_status": "Oui, selon les projets",
        "junior_evidence": "L'offre CYSRev 2026 acceptait explicitement un ingénieur de recherche ayant 0 à 3 ans d'expérience avec un Master 2; l'IRIT publie également des stages Master 2 et contrats doctoraux.",
        "active_jobs": "Aucune offre d'ingénieur junior IRIT encore ouverte confirmée le 2026-09-25. L'offre CYSRev — ingénieur de recherche IA éducative/Data, 0–3 ans — avait une fenêtre du 1er juin au 1er septembre 2026 et est donc traitée comme clôturée — https://lairdil.utoulouse.fr/offre-de-recrutement-ingenieur-e-de-recherche-postdoctorant-e. Un stage 2026/2027 IRIT existe, mais exige le statut Master 2 — https://midoc.univ-toulouse.fr/offres-demploi/.",
        "linkedin_contact_name": "Azzeddine Benabbou",
        "linkedin_contact_role": "Responsable scientifique IRIT, équipe TALENT — contact de l'offre CYSRev",
        "linkedin_profile": "Aucun profil LinkedIn personnel suffisamment fiable trouvé; utiliser la page IRIT https://www.linkedin.com/company/irit/",
        "contact_verification": "Nom, affiliation IRIT et email confirmés dans l'offre officielle 2026. Aucun profil personnel univoque n'a été retenu.",
        "verified_email": "azzeddine.benabbou@irit.fr",
        "email_status": "Adresse publiée dans l'offre officielle CYSRev. À utiliser pour une demande ciblée concernant l'équipe TALENT, pas comme boîte RH générale. val@irit.fr du CSV n'est pas retenue faute de contexte de recrutement actuel.",
        "application_channel": "https://www.irit.fr/emplois-stages/ | mailto:azzeddine.benabbou@irit.fr",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Français",
        "potential_score_100": "45",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Les offres consultées ne promettent ni visa ni relocation. Un recrutement contractuel en France peut nécessiter une autorisation de travail; aucun engagement propre à l'IRIT n'est publié. Les stages exigent généralement une convention et un statut étudiant.",
        "sources": "https://lairdil.utoulouse.fr/offre-de-recrutement-ingenieur-e-de-recherche-postdoctorant-e | https://midoc.univ-toulouse.fr/offres-demploi/ | https://aniti.univ-toulouse.fr/fr_fr/internship-positions/ | https://www.linkedin.com/company/irit/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — forte proximité scientifique, mais offre junior 2026 clôturée et mobilité non documentée",
        "notes": "Priorité moyenne-faible pour l'étranger. Ne pas envoyer comme candidature à l'offre CYSRev fermée. Écrire uniquement pour demander si un prochain contrat d'ingénieur de recherche 0–3 ans est prévu et s'il peut accueillir un diplômé tunisien hors statut étudiant.",
        "email_subject": "Intérêt pour un futur poste d'ingénieur de recherche junior en IA",
        "email_body": "Bonjour Monsieur Benabbou,\n\nRécemment diplômé ingénieur en informatique de l'ENSI en Tunisie, je me permets de vous contacter au sujet de futurs besoins d'ingénieur de recherche junior au sein de l'équipe TALENT de l'IRIT.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. J'ai travaillé sur la compréhension du besoin, la conception de workflows intelligents et leur intégration logicielle. Mon profil réunit Python, machine learning, LLM/RAG, développement web, APIs, bases de données, Java et C++.\n\nJ'ai pris connaissance de l'offre CYSRev sur l'IA éducative, l'analyse de données et le chatbot. Je comprends que sa période de candidature est terminée et je ne souhaite pas présenter une ancienne offre comme encore ouverte. Son contenu correspond néanmoins fortement à mon profil et à mon souhait de contribuer à une recherche appliquée produisant un système réellement utilisable.\n\nPourriez-vous m'indiquer si votre équipe prévoit prochainement un contrat similaire ouvert aux ingénieurs 0–3 ans et si un diplômé tunisien nécessitant une autorisation de travail peut être étudié ? Je joins mon CV à titre de présentation.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour, jeune diplômé ingénieur ENSI, mon PFE portait sur des agents IA intégrés à un produit. Les travaux de l'IRIT en IA/Data/NLP et l'ancien projet CYSRev correspondent fortement à mon profil Python/LLM/web. Je serais ravi de suivre vos futures opportunités de recherche junior.",
        "linkedin_followup": "Bonjour, merci pour la connexion. L'offre CYSRev étant clôturée, je ne candidate pas à tort. J'ai écrit à M. Benabbou pour demander si un futur contrat d'ingénieur de recherche IA 0–3 ans pourrait accueillir un diplômé tunisien. Mon CV associe Python, LLM/RAG, logiciel et capacité à relier recherche et produit.",
    },
    {
        "organization_key": "lgipm laboratoire de genie informatique de production et de maintenance universite de lorraine france",
        "sector": "Recherche en génie industriel, IA, optimisation, Data Science, systèmes de production et maintenance",
        "target_roles": "Ingénieur de recherche en IA/Data; Research Software Engineer; doctorant en IA/optimisation; stage Master 2 en LLM ou machine learning",
        "match_score_10": "7.6",
        "match_reason": "Le laboratoire travaille sur l'IA, les sciences des données, l'optimisation et les systèmes de production; un stage récent y a utilisé LLM, LangChain, FastAPI et Streamlit. Le candidat possède une base pertinente, mais la plupart des voies sont académiques, étudiantes ou doctorales et aucune ouverture junior professionnelle actuelle n'est confirmée.",
        "junior_status": "Oui, principalement stages et doctorats",
        "junior_evidence": "Des étudiants tunisiens effectuent actuellement des stages IA/LLM au LGIPM. Les recrutements permanents/enseignants visibles exigent généralement un doctorat ou un statut académique avancé.",
        "active_jobs": "Aucune offre d'ingénieur IA/logiciel junior au LGIPM confirmée ouverte le 2026-09-25. Les campagnes universitaires trouvées concernent des postes enseignants-chercheurs/doctoraux et ne correspondent pas à un jeune ingénieur recherchant un emploi logiciel immédiat — https://www.univ-lorraine.fr/travailler-a-l-ul/en/job-offers/.",
        "linkedin_contact_name": "Ons Rekik",
        "linkedin_contact_role": "Stagiaire/chercheuse actuelle au LGIPM sur un projet IA/LLM — contact de terrain, pas recruteuse",
        "linkedin_profile": "https://fr.linkedin.com/in/ons-rekik",
        "contact_verification": "Profil public actuel au LGIPM et projet visible avec LLM, LangChain, FastAPI et Streamlit. Aucun recruteur propre au laboratoire n'a été identifié.",
        "verified_email": "Aucun email public de recrutement junior vérifié",
        "email_status": "josette.linder@univ-lorraine.fr figure dans le CSV mais son rôle actuel de recrutement n'a pas été confirmé. Utiliser le portail Université de Lorraine ou le formulaire officiel du laboratoire; ne pas envoyer automatiquement à cette adresse.",
        "application_channel": "https://www.univ-lorraine.fr/travailler-a-l-ul/en/job-offers/ | https://lgipm.univ-lorraine.fr/contact/localisation",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Français",
        "potential_score_100": "31",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "La présence d'étudiants internationaux démontre l'accès académique, pas le sponsoring d'un emploi. Aucune offre correspondante ne précise visa ou relocation.",
        "sources": "https://lgipm.univ-lorraine.fr/contact/localisation | https://www.univ-lorraine.fr/travailler-a-l-ul/en/job-offers/ | https://doctorat.univ-lorraine.fr/fr/les-ecoles-doctorales/iaem/recrutement | https://fr.linkedin.com/in/ons-rekik",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — accueil de profils internationaux en stage, aucune ouverture d'ingénieur junior confirmée",
        "notes": "Faible priorité pour un emploi immédiat. Le contact LinkedIn sert à demander un retour d'expérience et le bon encadrant, pas une recommandation RH. Candidater seulement à une offre officielle future; envisager le laboratoire si le candidat souhaite une thèse ou un contrat de recherche.",
        "email_subject": "Candidature d'intérêt – futur contrat junior IA / logiciel de recherche",
        "email_body": "Bonjour,\n\nJe suis récemment diplômé ingénieur en informatique de l'ENSI en Tunisie et souhaite manifester mon intérêt pour un futur contrat d'ingénieur de recherche junior au LGIPM autour de l'IA, des LLM, de la Data Science ou du développement logiciel scientifique.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. J'ai acquis une expérience pratique de la traduction d'un besoin en workflows intelligents puis de leur intégration dans un produit existant. Je maîtrise Python, Java, C++, les APIs, les bases de données, le full-stack, le machine learning et les concepts LLM/RAG.\n\nLes projets du LGIPM associant intelligence artificielle, optimisation et systèmes réels correspondent à mon souhait de travailler sur des problèmes appliqués et mesurables. Je n'ai toutefois trouvé aucune offre junior actuellement ouverte et ne souhaite pas envoyer une candidature pour un poste inexistant.\n\nJe serais reconnaissant de savoir quel portail ou quelle équipe suivre pour un futur contrat accessible à un jeune ingénieur international, distinct d'un stage nécessitant encore le statut étudiant. Mon CV peut être transmis sur demande.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour Ons, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur des agents IA. Votre expérience au LGIPM avec LLM, LangChain et FastAPI m'intéresse beaucoup. Je souhaiterais comprendre les voies d'accès du laboratoire pour un diplômé tunisien. Ravi de rejoindre votre réseau.",
        "linkedin_followup": "Bonjour Ons, merci pour la connexion. Je recherche un premier rôle IA/software et le LGIPM m'intéresse, mais je n'ai trouvé que des voies académiques. Pourriez-vous me dire si le laboratoire accueille parfois des ingénieurs de recherche juniors déjà diplômés, et quel encadrant ou portail suivre ? Je ne souhaite pas vous demander une recommandation RH inappropriée.",
    },
    {
        "organization_key": "listic laboratoire d informatique systemes traitement de l information et de la connaissance",
        "sector": "Recherche en machine learning, fusion d'information, IA distribuée, systèmes, réseaux et traitement des connaissances",
        "target_roles": "Ingénieur de recherche IA/Data; Research Software Engineer; doctorant; stage Master 2 en LLM, confidentialité ou IA distribuée",
        "match_score_10": "8.0",
        "match_reason": "Les sujets LLM, confidentialité, IA distribuée et traitement de connaissances correspondent à l'IA/logiciel et au contexte finance sensible du PFE. Les offres disponibles sont toutefois des stages étudiants ou des postdoctorats exigeant un doctorat, pas un premier emploi d'ingénieur généraliste.",
        "junior_status": "Oui, par stages et doctorats",
        "junior_evidence": "Le LISTIC a publié plusieurs stages 2025/2026 de niveau Master 2/5e année, dont un sujet LLM sur la protection des informations sensibles. Un postdoctorat 2026 exige, par définition, un doctorat.",
        "active_jobs": "Aucun emploi d'ingénieur junior adapté confirmé ouvert le 2026-09-25. Le stage LLM/confidentialité était prévu entre février et juillet 2026 et est expiré — https://projects.listic.univ-smb.fr/emploi/stage/offre_stage_2026_faiza.pdf. Le postdoctorat « Energy-Aware Distributed AI » exige un doctorat et ne correspond pas au candidat — https://projects.listic.univ-smb.fr/emploi/post-doc/2026_PostDoc_LISTIC.pdf.",
        "linkedin_contact_name": "LISTIC",
        "linkedin_contact_role": "Page officielle actuelle du laboratoire",
        "linkedin_profile": "https://fr.linkedin.com/company/listic-lab",
        "contact_verification": "Page officielle active en septembre 2026; aucun profil RH personnel propre au laboratoire n'a été identifié.",
        "verified_email": "Aucun email de recrutement junior actuellement vérifié",
        "email_status": "directeur-listic@univ-smb.fr du CSV est une adresse institutionnelle, mais aucun appel junior actuel ne la désigne comme canal. L'ancienne adresse Recrutement.Listic@univ-smb.fr provenait d'une offre 2023 et ne doit pas être utilisée comme campagne actuelle.",
        "application_channel": "https://projects.listic.univ-smb.fr/emploi/ | https://www.univ-smb.fr/listic/",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Français",
        "potential_score_100": "32",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "L'école doctorale USMB accueille une proportion importante d'étrangers, mais cela concerne des doctorants et ne prouve pas le sponsoring d'un emploi junior. Les offres consultées ne mentionnent pas la relocation.",
        "sources": "https://fr.linkedin.com/company/listic-lab | https://projects.listic.univ-smb.fr/emploi/stage/offre_stage_2026_faiza.pdf | https://projects.listic.univ-smb.fr/emploi/post-doc/2026_PostDoc_LISTIC.pdf | https://www.univ-smb.fr/listic/en/informations/actualites/",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — sujets IA pertinents, mais stages expirés et postdoctorat hors niveau",
        "notes": "Faible priorité pour un emploi immédiat. Ne pas écrire au directeur sans offre précise. Suivre la page emploi et utiliser le message LinkedIn pour demander si un futur poste d'ingénieur contractuel non réservé aux étudiants est prévu.",
        "email_subject": "Intérêt pour de futurs contrats d'ingénieur de recherche junior en IA",
        "email_body": "Bonjour,\n\nRécemment diplômé ingénieur en informatique de l'ENSI en Tunisie, je m'intéresse aux travaux du LISTIC en apprentissage automatique, traitement des connaissances et IA distribuée.\n\nMon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. J'ai travaillé sur la conception de workflows intelligents, les LLM/RAG et leur intégration dans un environnement logiciel, avec une attention particulière à la fiabilité d'un produit manipulant des informations financières. Je maîtrise également Python, Java, C++, les APIs, les bases de données et le développement full-stack.\n\nLe sujet 2026 sur les LLM et la préservation des informations sensibles est particulièrement proche de mes intérêts. Je comprends néanmoins qu'il s'agissait d'un stage étudiant désormais terminé, tandis que le poste en IA distribuée est de niveau postdoctoral.\n\nJe souhaiterais simplement savoir si le LISTIC prévoit à l'avenir des contrats d'ingénieur de recherche junior accessibles à un jeune diplômé international déjà sorti de l'école. Je suivrai le portail officiel et ne candidaterai qu'à une ouverture adaptée.\n\nBien cordialement,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Bonjour, jeune diplômé ingénieur ENSI, mon PFE portait sur les agents IA dans un produit financier. Les travaux du LISTIC sur les LLM, la confidentialité et l'IA distribuée correspondent fortement à mes intérêts. Je serais ravi de suivre vos futures opportunités junior.",
        "linkedin_followup": "Bonjour, merci pour la connexion. Les stages 2026 du LISTIC étant terminés et le poste actuel étant postdoctoral, je ne candidate pas à tort. Je cherche plutôt un futur contrat d'ingénieur de recherche junior en IA/logiciel ouvert aux diplômés internationaux. Pourriez-vous m'indiquer la page ou l'équipe à suivre ?",
    },
    {
        "organization_key": "mass analytics",
        "sector": "Marketing Mix Modeling, Data Science, économétrie, machine learning, logiciels analytiques, Data Engineering et IA agentique",
        "target_roles": "Junior Data Scientist; Junior Machine Learning Engineer; Junior Marketing Scientist; Junior Software Engineer; Junior Java Developer; Data Engineer; Business/Data Analyst",
        "match_score_10": "9.5",
        "match_reason": "MASS associe finance/ROI, analyse métier, Python, machine learning, Data, logiciel et désormais une couche agentique appelée Maia. Le double parcours informatique–ingénierie financière et le PFE sur les agents IA sont très différenciants. Le candidat devra renforcer l'économétrie MMM et la communication analytique client.",
        "junior_status": "Oui — confirmé",
        "junior_evidence": "Le portail Talent officiel permet de s'inscrire spécifiquement pour Junior Data Scientist, Junior ML Engineer, Junior Software Engineer, Junior Java Developer, Junior Marketing Scientist et stages. Des diplômés récents sont actuellement intégrés dans l'équipe de Tunis.",
        "active_jobs": "Aucune offre nominative actuellement ouverte n'a été affichée par le portail public le 2026-09-25. L'offre Junior Marketing Scientist publiée en 2026 est désormais marquée « ne prend plus de candidatures » et n'est pas présentée comme active — https://tn.linkedin.com/jobs/view/junior-marketing-scientist-at-mass-analytics-4426015682. Le canal officiel Connect reste ouvert pour les catégories juniors — https://careers.mass-analytics.com/connect.",
        "linkedin_contact_name": "Firas Jabloun",
        "linkedin_contact_role": "Co-founder & CEO — MASS Analytics",
        "linkedin_profile": "https://uk.linkedin.com/in/firas-jabloun-b8127b8",
        "contact_verification": "Fondateur et CEO actuel, actif publiquement en 2026 sur l'évolution du logiciel et la valeur du raisonnement métier en ingénierie. Aucun recruteur/People Partner actuel suffisamment certain n'a été trouvé.",
        "verified_email": "Aucun email public de recrutement vérifié",
        "email_status": "info@mass-analytics.com du CSV est une adresse générale, pas un canal de recrutement confirmé. Utiliser le portail Talent Connect officiel plutôt que d'envoyer un CV à l'adresse info.",
        "application_channel": "https://careers.mass-analytics.com/connect",
        "recommended_cv": "CV_ATS_Fintech_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "82",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Le candidat vise le bureau de Tunis, affiché comme localisation officielle du portail carrière.",
        "sources": "https://careers.mass-analytics.com/connect | https://careers.mass-analytics.com/locations | https://tn.linkedin.com/jobs/view/junior-marketing-scientist-at-mass-analytics-4426015682 | https://www.linkedin.com/company/mass_analytics | https://uk.linkedin.com/in/firas-jabloun-b8127b8",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — excellente adéquation et filières junior officielles, aucune offre nominative ouverte",
        "notes": "Très haute priorité en veille. Créer immédiatement un profil Talent Connect pour Junior Data Scientist, Junior ML Engineer, Junior Software Engineer et Junior Marketing Scientist. Ne pas utiliser info@. Le message LinkedIn au CEO doit rester bref et demander l'orientation vers l'équipe People, sans exiger une réponse.",
        "email_subject": "Junior Data/AI & Software Profile – MASS Analytics Tunis",
        "email_body": "Dear MASS Analytics Talent Team,\n\nI am a recent Computer Engineering graduate from ENSI, specialised in Financial Engineering, and I would like to join your talent network for a junior Data Science, Machine Learning, Marketing Science or Software Engineering opportunity in Tunis.\n\nMy final-year project at Linedata focused on modernising a financial product with AI agents. I translated business objectives into intelligent workflows and contributed to their integration into an existing product. My background includes Python, machine learning, data analysis, LLMs, APIs, databases, Java, C++ and full-stack development.\n\nMASS Analytics is especially compelling to me because your work connects modelling to decisions: measuring business drivers, explaining results clearly and improving how budgets are allocated. The development of Maia as an agentic layer makes the fit even stronger. My combination of software engineering, AI and financial reasoning would allow me to approach both the analytical model and the business outcome it serves.\n\nI understand that the recent Junior Marketing Scientist posting is no longer accepting applications. I have therefore connected through the official talent portal for future junior openings rather than treating that role as active. I would be pleased to discuss any matching opportunity.\n\nKind regards,\nMohamed Oussema Bahloul",
        "linkedin_invitation": "Hello Mr Jabloun, I am a recent ENSI Computer Engineering graduate specialised in Financial Engineering. My Linedata project used AI agents to modernise a financial product. MASS Analytics' mix of modelling, software, ROI and the Maia agentic layer strongly matches my profile. Glad to connect.",
        "linkedin_followup": "Hello Mr Jabloun, thank you for connecting. I joined MASS Analytics' official talent network for future junior Data/ML/Software roles, since the recent Junior Marketing Scientist posting is closed. My profile combines AI agents, software engineering and financial/business reasoning. If appropriate, I would appreciate being directed to the People team for Tunis.",
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
