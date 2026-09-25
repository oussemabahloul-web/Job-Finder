#!/usr/bin/env python3
"""Fast verified foreign-company batch, 2026-09-25."""
from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_16.csv"


def r(key: str, **values: str) -> dict[str, str]:
    row = {
        "organization_key": key,
        "checked_date": "2026-09-25",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Candidature via le portail officiel uniquement",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Aucun engagement public de sponsoring de visa trouvé pour le poste ciblé.",
        "verification_status": "Vérifié — recherche manuelle effectuée",
    }
    row.update(values)
    return row


RECORDS = [
    r(
        "nxp",
        sector="Semiconductors, embedded software, edge AI and Agentic AI",
        target_roles="Junior Agentic AI Software Engineer; Graduate AI/ML Engineer; Junior Python/C++ Software Engineer",
        match_score_10="9.6",
        potential_score_100="86",
        priority="Priorité maximale",
        match_reason="L'offre active vise explicitement un New Graduate et reprend presque exactement le PFE : agents IA, raisonnement, planification, outils, mémoire, Python et pratiques de génie logiciel.",
        junior_status="Oui — offre New Graduate active",
        junior_evidence="L'annonce officielle NXP indique 'Junior Agentic AI Software Engineer' et 'New Graduate'. L'équipe France recrute aussi étudiants, diplômés et expérimentés.",
        foreign_employee_status="Non vérifiable — candidature internationale à tenter",
        foreign_employee_evidence="NXP recrute dans un environnement international, mais l'annonce française ne promet pas de sponsoring. L'autorisation de travail doit être confirmée par le recrutement.",
        active_jobs="Junior Agentic AI Software Engineer — Sophia Antipolis/Valbonne — New Graduate — https://nxp.wd3.myworkdayjobs.com/careers/job/Sophia-Antipolis-Valbonne/Junior-Agentic-AI-Software-Engineer_R-10063084",
        linkedin_contact_name="Fabien Escribe",
        linkedin_contact_role="Senior Talent Acquisition Business Partner — NXP Semiconductors France",
        linkedin_profile="https://fr.linkedin.com/in/fabienescrive/fr",
        contact_verification="Profil NXP actuel, Talent Acquisition pour la France et activité récente sur les recrutements NXP.",
        application_channel="https://nxp.wd3.myworkdayjobs.com/careers/job/Sophia-Antipolis-Valbonne/Junior-Agentic-AI-Software-Engineer_R-10063084",
        sources="https://nxp.wd3.myworkdayjobs.com/careers/job/Sophia-Antipolis-Valbonne/Junior-Agentic-AI-Software-Engineer_R-10063084 | https://fr.linkedin.com/in/fabienescrive/fr | https://fr.linkedin.com/jobs/view/apprenti-e-charg%C3%A9-e-de-recrutement-et-relations-ecoles-at-nxp-semiconductors-4431125819",
        verification_status="Vérifié — offre Agentic AI New Graduate active et fortement ciblée",
        notes="Candidater immédiatement via Workday. L'adresse personnelle présente dans le CSV n'est pas utilisée comme canal de candidature.",
        email_subject="Application – Junior Agentic AI Software Engineer – R-10063084",
        email_body="""Dear NXP Recruitment Team,

I am applying for the Junior Agentic AI Software Engineer position in Sophia Antipolis. I recently graduated as a Computer Engineer from ENSI, and my final-year project at Linedata focused on modernizing a financial software product through AI agents.

This project gave me hands-on experience with agent reasoning, tool use, LLM integration, APIs and the integration of AI capabilities into an existing product. I also bring strong foundations in Python, Java, C++, databases, full-stack development, testing, Git and CI/CD.

What attracts me most to this role is the opportunity to develop agent-based systems under the guidance of experienced engineers while contributing to robust, scalable software. I am based in Tunisia and fully prepared to relocate to France, subject to work-authorization feasibility.

Thank you for considering my application.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour M. Escribe, jeune diplômé ENSI, mon PFE chez Linedata portait sur des agents IA intégrés à un produit financier. L'offre NXP Junior Agentic AI Software Engineer à Valbonne correspond précisément à mon profil. Ravi d'échanger.",
        linkedin_followup="Bonjour M. Escribe, merci pour la connexion. Je candidate à l'offre R-10063084. Mon expérience couvre agents IA, Python, APIs et intégration produit. Pourriez-vous me confirmer si un jeune diplômé tunisien ouvert à la mobilité peut être étudié ?",
    ),
    r(
        "bmw group",
        sector="Automotive software, AI/ML, embedded systems, cybersecurity, cloud and full-stack development",
        target_roles="Trainee IT & Artificial Intelligence; Graduate AI/Software Engineer; Agentic AI Engineer",
        match_score_10="8.5",
        potential_score_100="68",
        priority="Haute",
        match_reason="Le programme couvre AI/ML, cloud, full-stack et C/C++/Python/Java. Le candidat possède le diplôme et l'expérience pratique, mais l'allemand courant et quatre mois d'expérience internationale réduisent l'adéquation.",
        junior_status="Oui — programme international Trainee actif",
        junior_evidence="L'offre AcceleratiON est un programme de début de carrière de 18 mois débouchant sur un CDI et publié le 13 septembre 2026.",
        foreign_employee_status="Non vérifiable — allemand courant demandé",
        foreign_employee_evidence="Le programme est international, mais l'annonce exige anglais et allemand courants et ne précise pas le sponsoring. BMW indique ailleurs que les non-UE doivent disposer d'un titre de séjour/travail valide.",
        active_jobs="Trainee IT & Artificial Intelligence — Munich — CDI, début 01/04/2027 — https://www.bmwgroup.jobs/en/jobfinder/job-description-copy.194966.html",
        linkedin_contact_name="Tamara Vuckovic",
        linkedin_contact_role="BMW Group professional sharing the AcceleratiON trainee programme",
        linkedin_profile="https://de.linkedin.com/in/tamara-vuckovic-0329a4219",
        contact_verification="Profil BMW Group actuel ayant relayé le programme AcceleratiON en septembre 2026; rôle exact dans la sélection non confirmé.",
        application_channel="https://www.bmwgroup.jobs/en/jobfinder/job-description-copy.194966.html",
        sources="https://www.bmwgroup.jobs/en/jobfinder/job-description-copy.194966.html | https://de.linkedin.com/in/tamara-vuckovic-0329a4219",
        verification_status="Vérifié — programme Trainee IT & AI actif, barrière linguistique importante",
        notes="Postuler seulement si le niveau d'allemand est réellement courant. Les stages BMW actifs exigent généralement d'être encore étudiant et ne sont donc pas retenus.",
        email_subject="Application – Trainee IT & Artificial Intelligence – Job ID 194966",
        email_body="""Dear BMW Group Recruitment Team,

I am applying for the AcceleratiON Trainee position in IT and Artificial Intelligence. I recently graduated as a Computer Engineer from ENSI, with a specialization in Financial Engineering, and completed my final-year project at Linedata on AI agents for the modernization of a financial software product.

My background combines Python, Java, C++, AI/ML, APIs, databases, full-stack development and Git-based delivery. I am particularly attracted by the programme's rotations across AI, software, cloud and cybersecurity, as well as its international and long-term development path.

I am based in Tunisia and open to relocating to Munich. I understand that fluent German and work authorization are important selection criteria and I would be pleased to clarify my eligibility during the process.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Ms Vuckovic, I am a recent ENSI Computer Engineering graduate with an AI-agent PFE at Linedata and skills in Python, Java/C++ and full-stack development. The BMW AcceleratiON IT & AI programme strongly interests me. Glad to connect.",
        linkedin_followup="Thank you for connecting. I am considering the Trainee IT & AI role 194966. Could you please confirm whether a Tunisian graduate requiring German work authorization may apply, and how strictly fluent German is assessed?",
    ),
    r(
        "progresssoft",
        sector="FinTech, payment systems, digital banking and enterprise software",
        target_roles="Associate Support Engineer; Junior Java Developer; Software Engineer; AI Engineer; FinTech implementation engineer",
        match_score_10="9.0",
        potential_score_100="73",
        priority="Haute",
        match_reason="Très forte convergence entre ingénierie informatique, spécialisation financière, Java/Python et PFE sur un produit financier. Un poste Associate Support Engineers – Induction vient d'être publié.",
        junior_status="Oui — poste Associate et programmes de stage",
        junior_evidence="Le portail officiel accueille les profils programmation/recherche et propose des stages; une offre Associate Support Engineers – Induction est apparue le 24 septembre 2026.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="ProgressSoft possède plusieurs implantations régionales, mais aucune preuve de sponsoring ou de relocation pour un candidat tunisien n'a été trouvée.",
        active_jobs="Associate Support Engineers – Induction — Amman — publié le 24/09/2026 — https://www.linkedin.com/company/progresssoftcorp/jobs/ ; Recruitment System — https://apply.workable.com/progresssoft/",
        linkedin_contact_name="ProgressSoft Corporation Talent Team",
        linkedin_contact_role="Canal officiel de l'entreprise et de ses recrutements",
        linkedin_profile="https://www.linkedin.com/company/progresssoftcorp",
        contact_verification="La page officielle publie les offres actuelles; aucun recruteur individuel actuel n'a été identifié avec assez de certitude.",
        application_channel="https://apply.workable.com/progresssoft/",
        recommended_cv="CV_ATS_Fintech_EN.pdf",
        sources="https://www.progressoft.com/careers | https://apply.workable.com/progresssoft/ | https://www.linkedin.com/company/progresssoftcorp",
        verification_status="Vérifié — forte cible FinTech et offre Associate récente; mobilité non documentée",
        notes="Utiliser le portail Workable. L'adresse marketing du CSV n'est pas une adresse de recrutement.",
        email_subject="Application – Associate Software / Support Engineering Opportunity",
        email_body="""Dear ProgressSoft Recruitment Team,

I am a recent Computer Engineering graduate from ENSI, specialized in Financial Engineering, and I am interested in the Associate Support Engineers induction opportunity and other entry-level software roles at ProgressSoft.

My final-year project at Linedata focused on modernizing a financial product with AI agents. It strengthened my ability to understand financial workflows and translate them into reliable software solutions. I also bring skills in Java, Python, C++, APIs, SQL, full-stack development, testing and Git.

ProgressSoft's focus on payment infrastructure and digital banking is an especially strong match for my combined technology and finance profile. I am based in Tunisia and willing to relocate to Amman if international recruitment is possible.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate specialized in Financial Engineering. My Linedata PFE combined financial software and AI agents. ProgressSoft's payments technology and current associate opportunities strongly match my profile.",
        linkedin_followup="Thank you for connecting. I am interested in the Associate Support Engineers induction role and junior software opportunities. Could you advise whether ProgressSoft considers Tunisian graduates who are willing to relocate to Amman?",
    ),
    r(
        "syslearn",
        sector="IT engineering and consulting: C++, Java, full-stack, AI, Data, cybersecurity and DevOps",
        target_roles="Junior C++ Engineer; Full-stack Developer; AI/Data Engineer; IT Consultant",
        match_score_10="8.2",
        potential_score_100="64",
        priority="Haute",
        match_reason="Les postes C++ et full-stack et les pôles IA/Data correspondent directement au profil. Les fiches publiques ne précisent toutefois pas le niveau d'expérience ni le sponsoring.",
        junior_status="Non vérifiable — dépôt de CV ouvert",
        junior_evidence="Le site officiel invite les candidats à déposer leur CV et affiche actuellement Consultant informatique, Ingénieur écosystème C++ et Développeur full-stack.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Aucune mention publique de visa, relocation ou recrutement hors UE sur la page consultée.",
        active_jobs="Ingénieur écosystème C++ — France — https://www.syslearn-group.com/carrieres/recrutement ; Développeur full-stack — moteur de matching IA — même portail ; Consultant informatique — même portail",
        linkedin_contact_name="Syslearn Group",
        linkedin_contact_role="Canal officiel de recrutement",
        linkedin_profile="https://www.linkedin.com/company/syslearn/",
        contact_verification="Aucun recruteur individuel actuel n'a été identifié de manière suffisamment fiable; utilisation du canal officiel.",
        application_channel="https://www.syslearn-group.com/carrieres/recrutement",
        language="Français",
        sources="https://www.syslearn-group.com/carrieres/recrutement | https://syslearn.fr/recrutement/",
        verification_status="Vérifié — trois postes affichés et dépôt de CV officiel, critères détaillés non publiés",
        notes="Déposer le CV via le formulaire. L'adresse personnelle présente dans le CSV n'est pas utilisée faute de confirmation publique actuelle.",
        email_subject="Candidature — Ingénieur C++ / Full-stack junior",
        email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l'ENSI, je souhaite vous proposer ma candidature pour vos opportunités en développement C++, full-stack, Data ou intelligence artificielle.

Mon PFE chez Linedata a porté sur la modernisation d'un produit financier à l'aide d'agents IA. Cette expérience m'a permis de combiner compréhension métier, développement logiciel et intégration de solutions d'IA. Je maîtrise notamment C++, Java, Python, les APIs, SQL, le développement full-stack, Git et les principes de CI/CD.

La diversité des pôles de Syslearn et votre volonté de faire progresser les consultants vers une expertise réelle correspondent à ce que je recherche pour ma première expérience. Basé en Tunisie, je suis ouvert à une mobilité en France si les démarches d'autorisation de travail sont envisageables.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour, jeune diplômé ingénieur ENSI, mon PFE Linedata combinait produit financier et agents IA. Je maîtrise C++, Java, Python et le full-stack. Vos postes C++ et full-stack ainsi que vos pôles IA/Data correspondent à mon profil. Ravi d'échanger.",
        linkedin_followup="Bonjour, merci pour la connexion. Je vais déposer ma candidature via votre portail pour les opportunités C++/full-stack. Savez-vous si Syslearn peut considérer un jeune diplômé tunisien nécessitant une mobilité vers la France ?",
    ),
    r(
        "estarta solutions",
        sector="IT services, networking, customer support, software engineering, cloud and AI integration",
        target_roles="Graduate Software Engineer; Technical Support Engineer; Full-stack/Backend Engineer; Python automation engineer",
        match_score_10="7.0",
        potential_score_100="49",
        priority="Moyenne",
        match_reason="Bonne base logiciel, APIs, full-stack et Python. Les postes Estarta sont souvent orientés réseau/Cisco, et l'offre AI full-stack retrouvée n'accepte plus de candidatures.",
        junior_status="Oui — graduate jobs et formations observés",
        junior_evidence="Le portail officiel est actif; des témoignages et annonces récentes mentionnent des parcours graduate/support, mais aucune offre logicielle junior active n'a été confirmée aujourd'hui.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Présence internationale, mais aucun engagement public de relocation pour les postes d'Amman.",
        active_jobs="Aucune offre software junior active confirmée; portail officiel — https://estarta-solutions.talentlyft.com/",
        linkedin_contact_name="Estarta Solutions",
        linkedin_contact_role="Canal officiel carrières",
        linkedin_profile="https://www.linkedin.com/company/estarta-solutions/",
        contact_verification="Aucun recruteur individuel actuel lié aux besoins junior n'a été vérifié; le portail officiel reste le canal sûr.",
        application_channel="https://estarta-solutions.talentlyft.com/",
        sources="https://estarta-solutions.talentlyft.com/ | https://www.estarta.com/contact/ | https://jo.linkedin.com/jobs/view/software-engineer-full-stack-or-backend-at-estarta-solutions-4405542427",
        verification_status="Vérifié — entreprise pertinente, mais aucune offre software junior active confirmée",
        notes="Candidature spontanée via le portail seulement. info@estarta.com est un contact commercial général, et l'adresse personnelle du CSV n'est pas utilisée.",
        email_subject="Open Application – Graduate Software / AI Engineer",
        email_body="""Dear Estarta Recruitment Team,

I am a recent Computer Engineering graduate from ENSI seeking an entry-level software, AI integration or technical engineering opportunity. My final-year project at Linedata focused on integrating AI agents into an existing financial software product.

I bring experience with Python, Java, C++, REST APIs, SQL, full-stack development, machine learning, Git and CI/CD. I am particularly interested in roles where software engineering, automation and customer-facing problem solving come together.

I am based in Tunisia and open to relocating to Amman or another Estarta location if a suitable graduate opportunity and work-authorization route are available.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with Python, Java/C++, APIs, full-stack and AI-agent experience from my Linedata PFE. I would be glad to follow Estarta's future graduate software and technical opportunities.",
        linkedin_followup="Thank you for connecting. I found that the recent AI full-stack role is closed. Could you advise whether Estarta expects graduate software, AI integration or technical-support openings that may consider a Tunisian candidate?",
    ),
    r(
        "smartovate",
        sector="AI agents, cloud, DevOps, cybersecurity, Data and EdTech",
        target_roles="Junior AI/Agent Engineer; Junior Cloud/DevOps Engineer; Full-stack Developer",
        match_score_10="8.3",
        potential_score_100="51",
        priority="Moyenne",
        match_reason="Très bonne adéquation agents IA, cloud et full-stack, et l'entreprise cible clairement les Tunisiens. Les recrutements actuels vérifiés concernent cependant des stages PFE, pas un emploi diplômé.",
        junior_status="Oui — très ouverte aux stagiaires et jeunes diplômés",
        junior_evidence="Publications récentes destinées aux étudiants et jeunes diplômés tunisiens; campagne PFE active en AI Agents, DevOps, cybersécurité et Data/IA.",
        foreign_employee_status="Oui — télétravail/stages internationaux observés",
        foreign_employee_evidence="L'entreprise recrute explicitement des Tunisiens et propose des expériences remote. Cela ne constitue pas une preuve d'emploi salarié au Royaume-Uni ni de visa.",
        active_jobs="Stage PFE 4–6 mois — AI Agent, DevOps, cybersécurité, Data & IA — publication active — candidature à careers@smartovate.com; aucune offre CDI junior confirmée",
        linkedin_contact_name="Abdelkhalek Bakkari",
        linkedin_contact_role="Founder — Smartovate",
        linkedin_profile="https://uk.linkedin.com/in/abdelkhalekbakkari",
        contact_verification="Fondateur actuel; relaie les campagnes de recrutement et de stage Smartovate en 2026.",
        verified_email="careers@smartovate.com",
        email_status="Adresse de candidature publiée dans une campagne officielle récente",
        application_channel="mailto:careers@smartovate.com",
        sources="https://uk.linkedin.com/in/abdelkhalekbakkari | https://www.linkedin.com/company/smartovate/ | https://www.smartovateai.com/company-info/",
        verification_status="Vérifié — junior-friendly et Tunisie-friendly, mais offre actuelle limitée au PFE",
        notes="Ne pas présenter le stage 2025 ou le Junior DevOps 2025 comme actifs. Pour un emploi, envoyer une candidature spontanée claire à careers@smartovate.com.",
        email_subject="Spontaneous Application – Junior AI / Agentic AI Engineer",
        email_body="""Dear Mr Bakkari,

I am a recent Computer Engineering graduate from ENSI and would like to submit a spontaneous application for a junior AI, Agentic AI or software engineering opportunity at Smartovate.

My final-year project at Linedata focused on modernizing a financial software product through AI agents. I worked on translating a real business need into an integrated solution involving LLMs, tools, APIs and application components. I also bring skills in Python, Java, C++, full-stack development, databases, machine learning, Git and CI/CD.

Smartovate's focus on AI agents, cloud and practical projects for young Tunisian talent strongly resonates with my background. As I have already completed my PFE, I am seeking a graduate employment opportunity rather than another internship.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour M. Bakkari, jeune diplômé ENSI, mon PFE chez Linedata portait sur des agents IA intégrés à un produit financier. Je recherche désormais un premier emploi en IA agentique/logiciel, et non un PFE. L'écosystème Smartovate m'intéresse beaucoup.",
        linkedin_followup="Bonjour M. Bakkari, merci pour la connexion. J'ai envoyé une candidature spontanée à careers@smartovate.com pour un poste junior en IA agentique/logiciel. Étant déjà diplômé, je recherche un emploi plutôt qu'un stage PFE. Je reste disponible pour échanger.",
    ),
]

FIELDS: list[str] = []
for record in RECORDS:
    for field in record:
        if field not in FIELDS:
            FIELDS.append(field)

with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(RECORDS)

print(f"Wrote {len(RECORDS)} records to {OUT}")
