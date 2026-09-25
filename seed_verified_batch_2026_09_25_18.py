#!/usr/bin/env python3
"""Verified foreign AI/data SMEs, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_18.csv"

def record(key: str, company: str, hook: str, **v: str) -> dict[str, str]:
    d = {
        "organization_key": key,
        "checked_date": "2026-09-25",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Portail ou LinkedIn officiel privilégié",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Aucun engagement public de sponsoring de visa trouvé.",
        "verification_status": "Vérifié — screening manuel effectué",
        "email_subject": f"Spontaneous Application – Junior AI / Software Engineer – {company}",
        "email_body": f"""Dear {company} Team,

I am a recent Computer Engineering graduate from ENSI seeking a junior AI or software engineering opportunity. My final-year project at Linedata focused on modernizing a financial software product through AI agents, from business analysis to integration into an existing application.

I bring skills in Python, Java, C++, machine learning, APIs, databases, full-stack development, Git and CI/CD. {hook}

I am based in Tunisia and open to relocation, subject to work-authorization feasibility. I would be grateful to be considered for a suitable graduate or junior opportunity.

Kind regards,
Mohamed Oussema Bahloul""",
    }
    d.update(v)
    return d

RECORDS = [
    record(
        "planblue gmbh", "PlanBlue",
        "PlanBlue's combination of AI-driven imaging, data science and environmental impact is exactly the kind of multidisciplinary product environment in which I want to grow.",
        sector="Marine technology, AI-driven imaging, computer vision, data science and embedded systems",
        target_roles="Junior AI/Computer Vision Engineer; Software Engineer; Data Scientist; Python Engineer",
        match_score_10="7.8", potential_score_100="48", priority="Moyenne",
        match_reason="Bonne adéquation IA, imagerie, Python et logiciel, mais l'unique poste actuel confirmé est Engineering Manager senior.",
        junior_status="Historique d'étudiants/stages; aucune offre junior active confirmée",
        junior_evidence="L'entreprise a déjà recruté des étudiants/assistants AWS et présente une équipe internationale, mais le portail actuel ne confirme qu'un rôle de management expérimenté.",
        foreign_employee_status="Oui/partiel — équipe internationale et relocation pour le poste senior",
        foreign_employee_evidence="L'annonce Engineering Manager demande une présence à Brême et accepte explicitement une relocation; aucune aide de visa n'est promise.",
        active_jobs="Engineering Manager — Brême — senior — https://jobs.planblue.com/engineering-manager/en ; aucune offre junior active confirmée",
        linkedin_contact_name="Jannet A.", linkedin_contact_role="People Operations — PlanBlue",
        linkedin_profile="https://de.linkedin.com/in/jannetallani",
        contact_verification="Profil People Operations actuel chez PlanBlue à Brême.",
        application_channel="https://jobs.planblue.com/",
        sources="https://jobs.planblue.com/engineering-manager/en | https://www.planblue.com/articles/story | https://de.linkedin.com/in/jannetallani",
        verification_status="Vérifié — société très pertinente, mais aucun poste junior actuel",
        linkedin_invitation="Hello Jannet, I am a recent ENSI Computer Engineering graduate with an AI-agent PFE at Linedata and skills in Python, ML and software. PlanBlue's AI-driven ocean-imaging mission strongly interests me. Glad to connect.",
        linkedin_followup="Thank you for connecting. I saw that the current role is for an Engineering Manager. Would PlanBlue consider a spontaneous application for a future junior AI, computer-vision or software position from a Tunisian graduate open to Bremen?",
    ),
    record(
        "synapse dx", "SynapseDX",
        "Your origin in banking software and your work on reliable LLM-based document automation make SynapseDX an unusually strong match for my combined software, AI and financial-engineering background.",
        sector="AI document processing, LLMs, inference engines, APIs and banking back-office automation",
        target_roles="Junior AI/LLM Engineer; Python Backend Engineer; Full-stack Developer; AI Product Engineer",
        match_score_10="9.1", potential_score_100="59", priority="Haute",
        match_reason="Excellente convergence LLM, intégration produit, APIs et finance; petite équipe sans poste public actuel.",
        junior_status="Non vérifiable",
        junior_evidence="Startup de 2–10 personnes fondée en 2024; aucune page carrière ni offre junior active n'a été trouvée.",
        active_jobs="Aucune offre active confirmée — candidature spontanée via le contact officiel ou LinkedIn",
        linkedin_contact_name="Emna Miled", linkedin_contact_role="CPO — SynapseDX",
        linkedin_profile="https://pt.linkedin.com/company/synapsedx",
        contact_verification="Emna Miled est listée dans l'équipe officielle comme CPO; profil personnel public non isolé avec certitude.",
        application_channel="https://synapsedx.com/about.html",
        sources="https://synapsedx.com/about.html | https://pt.linkedin.com/company/synapsedx",
        verification_status="Vérifié — fit excellent, mais aucune ouverture publique actuelle",
        linkedin_invitation="Bonjour Mme Miled, jeune diplômé ENSI spécialisé en ingénierie financière, mon PFE Linedata portait sur des agents IA intégrés à un produit financier. L'ADN banking+LLM de SynapseDX correspond remarquablement à mon profil. Ravi d'échanger.",
        linkedin_followup="Bonjour Mme Miled, merci pour la connexion. Je souhaiterais proposer ma candidature spontanée pour un futur poste junior IA/logiciel. Mon profil combine LLM/agents, APIs, full-stack et compréhension des produits financiers. Puis-je vous transmettre mon CV ?",
    ),
    record(
        "wsk medical", "WSK Medical",
        "I am particularly interested in applying reliable AI and software engineering to a regulated healthcare product such as Zeno AI.",
        sector="Medical AI, computer vision, deep learning, video analysis and digital pathology",
        target_roles="Junior AI/ML Engineer; Computer Vision Engineer; Python Software Engineer",
        match_score_10="7.8", potential_score_100="45", priority="Moyenne",
        match_reason="Bonne adéquation IA/ML et développement; expérience santé, vision et réglementation non démontrée, aucune offre active trouvée.",
        junior_status="Oui historiquement; aucune offre actuelle confirmée",
        junior_evidence="WSK Medical a publiquement intégré une diplômée dans son équipe AI après un travail à temps partiel, mais aucun recrutement junior actuel n'est visible.",
        active_jobs="Aucune offre active confirmée — surveiller https://www.wskmedical.ai/ et la page LinkedIn",
        linkedin_contact_name="WSK Medical", linkedin_contact_role="Canal officiel de l'entreprise",
        linkedin_profile="https://www.linkedin.com/company/wsk-medical",
        contact_verification="Aucun recruteur individuel actuel n'a été identifié de manière fiable.",
        application_channel="https://www.wskmedical.ai/",
        sources="https://www.linkedin.com/company/wsk-medical | https://www.wskmedical.ai/",
        verification_status="Vérifié — société HealthTech IA pertinente, aucune offre actuelle",
        linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with an AI-agent PFE at Linedata and skills in Python and ML. WSK Medical's work on production medical AI is highly relevant to my goals. I would be glad to follow future junior opportunities.",
        linkedin_followup="Thank you for connecting. Could you advise whether WSK Medical accepts spontaneous applications for junior AI/ML or Python engineering roles from international graduates willing to relocate?",
    ),
    record(
        "omnidata", "Omnidata / Omnishore",
        "Your banking and telecom transformation projects are relevant to both my software-engineering skills and my specialization in Financial Engineering.",
        sector="IT services, banking and telecom software, digital transformation, QA and enterprise systems",
        target_roles="Junior Java/Python Developer; Software Engineer; QA Automation Engineer; Junior Business Analyst",
        match_score_10="7.4", potential_score_100="52", priority="Moyenne",
        match_reason="Secteurs et développement pertinents, mais les offres actuelles trouvées demandent 3 à 8 ans et des stacks spécifiques .NET/BSCS.",
        junior_status="Non confirmé dans les offres actuelles",
        junior_evidence="L'offre .NET du 1er septembre 2026 exige au moins 3 ans; les recrutements publiés par la chargée de recrutement sont expérimentés.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Aucune indication de prise en charge d'un candidat tunisien pour un poste au Maroc.",
        active_jobs="Développeur .NET — Casablanca — 3 ans minimum — valable jusqu'au 31/10/2026 — https://betterjob.online/offre/developpeur-net-casablanca-2026-09 ; autres missions actuelles expérimentées",
        linkedin_contact_name="Imane Nayssa", linkedin_contact_role="Recruitment / opportunities — Omnishore Groupe Medtech",
        linkedin_profile="https://ma.linkedin.com/in/imane-nayssa-78174a155",
        contact_verification="Profil actuel publiant plusieurs besoins Omnishore/Omnidata en septembre 2026.",
        application_channel="https://ma.linkedin.com/company/omnishore/",
        language="Français", recommended_cv="CV_ATS_Fintech.pdf",
        sources="https://betterjob.online/offre/developpeur-net-casablanca-2026-09 | https://ma.linkedin.com/in/imane-nayssa-78174a155",
        verification_status="Vérifié — bonne cible générale, mais postes actuels trop expérimentés",
        email_subject="Candidature spontanée — Ingénieur logiciel / Data junior",
        email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l'ENSI, avec une spécialisation en ingénierie financière, je vous propose ma candidature pour une future opportunité junior en développement logiciel, Data, QA/automatisation ou transformation digitale.

Mon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. Je maîtrise Python, Java, C++, les APIs, SQL, le développement full-stack, le machine learning, Git et les principes de CI/CD. Les projets banque et télécom d'Omnidata/Omnishore correspondent ainsi à mon double profil technique et métier.

Je suis basé en Tunisie et ouvert à une mobilité au Maroc si cela est envisageable.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour Mme Nayssa, jeune diplômé ingénieur ENSI spécialisé en ingénierie financière, mon PFE Linedata combinait produit financier et agents IA. Je recherche un poste junior logiciel/Data/QA et les projets Omnishore m'intéressent. Ravi d'échanger.",
        linkedin_followup="Bonjour Mme Nayssa, merci pour la connexion. Les offres actuelles semblent demander plusieurs années d'expérience; pourriez-vous garder mon CV pour un futur besoin junior en logiciel, Data, QA ou transformation digitale ?",
    ),
    record(
        "findata", "FinData",
        "FinData's work on data infrastructure and decision modernization for financial institutions directly matches my Data/AI and financial-engineering profile.",
        sector="Data infrastructure, analytics, BI, AI/ML and financial-sector modernization",
        target_roles="Junior Data Scientist; Data Engineer; BI/Power BI Analyst; Python Engineer",
        match_score_10="8.7", potential_score_100="58", priority="Haute",
        match_reason="Très bon fit Python, SQL, ML, BI et finance; l'unique offre trouvée est Lead Data Scientist et n'accepte plus les candidatures.",
        junior_status="Oui — juniors mentionnés, mais aucune offre junior active",
        junior_evidence="L'annonce Lead Data Scientist indique un encadrement de junior data scientists et un environnement jeune; aucun poste junior actif n'est publié.",
        active_jobs="Aucune offre junior active confirmée; l'offre Lead Data Scientist est fermée",
        linkedin_contact_name="FinData", linkedin_contact_role="Page officielle de l'entreprise",
        linkedin_profile="https://www.linkedin.com/company/findatarim",
        contact_verification="Petite équipe officielle; aucun profil RH distinct identifié.",
        verified_email="careers@findata.work", email_status="Adresse de recrutement publiée dans l'annonce officielle FinData",
        application_channel="mailto:careers@findata.work",
        recommended_cv="CV_ATS_Fintech_EN.pdf",
        sources="https://www.linkedin.com/company/findatarim | https://mr.linkedin.com/jobs/view/lead-data-scientist-at-findata-4347351645",
        verification_status="Vérifié — excellente cible Data/finance, candidature junior spontanée",
        email_subject="Spontaneous Application – Junior Data / AI Engineer",
        linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate specialized in Financial Engineering, with a Linedata PFE on AI agents for financial software. FinData's Data/BI work for financial institutions strongly matches my profile.",
        linkedin_followup="Thank you for connecting. I saw that the Lead Data Scientist role is closed, but it mentions junior data scientists. May I submit a spontaneous application for a junior Data, BI or AI role in Nouakchott?",
    ),
    record(
        "ixias", "Ixias",
        "Ixias' focus on Java and elegant, well-tested software is relevant to my Java/C++/Python and full-stack foundation.",
        sector="Micro IT consultancy focused on Java software, design and testing",
        target_roles="Junior Java Developer; Full-stack Developer; Software Engineer",
        match_score_10="6.8", potential_score_100="35", priority="Faible",
        match_reason="Stack Java pertinente, mais micro-structure d'environ 1 ETP sans offre ni fonction RH identifiée.",
        junior_status="Non vérifiable",
        junior_evidence="Aucune offre ou programme junior public trouvé.",
        active_jobs="Aucune offre active confirmée",
        linkedin_contact_name="Akrem Ayadi", linkedin_contact_role="Seul collaborateur public listé — Ixias",
        linkedin_profile="https://www.linkedin.com/company/ixias-srl",
        contact_verification="La page officielle ne liste qu'un collaborateur; rôle et disponibilité de recrutement non vérifiés.",
        application_channel="http://ixias.be",
        sources="https://www.linkedin.com/company/ixias-srl | https://www.companyweb.be/en/0767498939/ixias",
        verification_status="Vérifié — micro-entreprise active, potentiel de recrutement faible",
        linkedin_invitation="Bonjour M. Ayadi, jeune diplômé ingénieur ENSI, je maîtrise Java, C++, Python et le full-stack. L'accent mis par Ixias sur le code propre, le design et les tests m'intéresse. Ravi d'échanger autour d'éventuels besoins juniors.",
        linkedin_followup="Bonjour M. Ayadi, merci pour la connexion. Ixias étant une petite structure, je souhaitais simplement savoir si vous envisagez à moyen terme un renfort junior Java/full-stack. Je peux vous transmettre mon CV si utile.",
    ),
    record(
        "sowiso bv", "SOWISO",
        "SOWISO's adaptive STEM-learning product would allow me to combine software, AI and a direct impact on how students learn technical subjects.",
        sector="EdTech SaaS, adaptive STEM learning, assessment and educational software",
        target_roles="Junior Full-stack Developer; Software Engineer; AI/EdTech Engineer",
        match_score_10="7.0", potential_score_100="42", priority="Moyenne",
        match_reason="Développement logiciel et IA applicative pertinents, mais aucune offre technique actuelle confirmée; SOWISO est désormais intégré au groupe Paragin.",
        junior_status="Non vérifiable",
        junior_evidence="L'entreprise a recruté des développeurs auparavant, mais les publications actuelles trouvées concernent surtout Customer Support et des rôles groupe.",
        active_jobs="Aucune offre technique active confirmée — surveiller https://www.sowiso.com/ et les postes Paragin Group",
        linkedin_contact_name="Andrea Sovilj", linkedin_contact_role="Current SOWISO professional",
        linkedin_profile="https://nl.linkedin.com/in/andrea-sovilj-3a8b0710a",
        contact_verification="Profil actuel chez SOWISO; fonction de recrutement non établie.",
        application_channel="https://www.sowiso.com/",
        sources="https://www.sowiso.com/ | https://nl.linkedin.com/in/andrea-sovilj-3a8b0710a",
        verification_status="Vérifié — cible EdTech pertinente, aucune offre technique actuelle",
        linkedin_invitation="Hello Andrea, I am a recent ENSI Computer Engineering graduate with software, AI and full-stack experience. SOWISO's adaptive STEM-learning platform interests me greatly. I would be glad to follow future junior engineering opportunities.",
        linkedin_followup="Thank you for connecting. Could you advise whether SOWISO or Paragin Group expects any junior software or AI-oriented openings in Amsterdam that could consider an international graduate?",
    ),
]

fields = []
for row in RECORDS:
    for key in row:
        if key not in fields:
            fields.append(key)
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader(); writer.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
