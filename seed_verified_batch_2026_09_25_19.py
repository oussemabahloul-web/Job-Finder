#!/usr/bin/env python3
"""Verified foreign product companies, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_19.csv"

def r(key: str, **v: str) -> dict[str, str]:
    d = {"organization_key": key, "checked_date": "2026-09-25", "verified_email": "Aucun email public vérifié", "email_status": "Portail officiel ou LinkedIn privilégié", "recommended_cv": "CV_ATS_EN.pdf", "language": "Anglais", "foreign_employee_status": "Non vérifiable", "foreign_employee_evidence": "Aucun engagement public de sponsoring de visa trouvé.", "verification_status": "Vérifié — screening manuel effectué"}
    d.update(v); return d

RECORDS = [
    r("deep learn strategies",
      sector="Applied AI, deep learning, computer vision, time series, Agentic AI and financial analytics", target_roles="Junior AI/ML Engineer; Agentic AI Engineer; Data Scientist; FinTech AI Engineer", match_score_10="9.5", potential_score_100="70", priority="Haute",
      match_reason="Correspondance exceptionnelle : la société encadre des PFE en systèmes multi-agents, analyse financière et optimisation de portefeuille, très proches du PFE Linedata et de la spécialisation financière.",
      junior_status="Oui — stages/PFE récents avec jeunes ingénieurs marocains", junior_evidence="Deux profils diplômés en 2025 décrivent un PFE DLS sur un système multi-agent d'analyse financière, CrewAI, prévision et optimisation, ensuite publié à IEEE WINCOM 2025.",
      foreign_employee_status="Oui/partiel — collaboration à distance avec le Maroc observée", foreign_employee_evidence="Des étudiants marocains ont réalisé leur PFE avec DLS; cela prouve une collaboration internationale, mais pas un sponsoring de visa ni un CDI au Royaume-Uni.",
      active_jobs="Aucune offre salariée active confirmée — candidature spontanée auprès de la petite équipe",
      linkedin_contact_name="Imtiaz Adam", linkedin_contact_role="Founder — Deep Learn Strategies; AI/FinTech leader", linkedin_profile="https://uk.linkedin.com/in/imtiaz-adam-7467528", contact_verification="Fondateur identifié par Companies House, la page DLS et les PFE/communications récentes; son titre LinkedIn principal actuel est Alpha Agentic Intelligence.",
      verified_email="info@dls.ltd", email_status="Adresse générale sur le domaine officiel; aucune adresse RH distincte", application_channel="mailto:info@dls.ltd", recommended_cv="CV_ATS_Fintech_EN.pdf",
      sources="https://uk.linkedin.com/company/deep-learn-strategies | https://find-and-update.company-information.service.gov.uk/company/10379706 | https://ma.linkedin.com/in/youssra-farissi-a7840321b | https://uk.linkedin.com/in/imtiaz-adam-7467528",
      verification_status="Vérifié — adéquation AI/FinTech remarquable, petite structure sans poste public",
      notes="Très bonne candidature spontanée. Mentionner la proximité avec leurs PFE multi-agents financiers sans prétendre qu'un poste est ouvert.",
      email_subject="Spontaneous Application – Junior Agentic AI / FinTech Engineer",
      email_body="""Dear Mr Adam,

I am a recent Computer Engineering graduate from ENSI, specialized in Financial Engineering, and I would like to submit a spontaneous application to Deep Learn Strategies.

My final-year project at Linedata focused on modernizing a financial software product through AI agents. I worked on agent workflows, LLM integration, APIs and the integration of the solution into an existing business product. I also bring skills in Python, machine learning, Java, C++, databases and full-stack development.

DLS's recent work with graduates on multi-agent financial analysis, time-series forecasting and portfolio optimization is remarkably close to my own academic and professional direction. I am based in Tunisia and open to remote collaboration or relocation where feasible.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello Mr Adam, I am a recent ENSI Computer Engineering graduate specialized in Financial Engineering. My Linedata PFE used AI agents in a financial product. DLS's multi-agent finance and portfolio work is remarkably close to my profile. Glad to connect.",
      linkedin_followup="Thank you for connecting. I sent a spontaneous application to info@dls.ltd. My profile combines Agentic AI, software engineering and finance. I would be grateful to discuss any junior project or role, remotely or with relocation."),
    r("medicusclinic",
      sector="HealthTech, LLM-powered medical consultation, AI automation and web platform", target_roles="Junior AI/LLM Engineer; Automation AI Platform Engineer; Python/Full-stack Engineer; QA Automation", match_score_10="8.5", potential_score_100="62", priority="Haute",
      match_reason="L'offre Automation AI Platform Engineer et la plateforme LLM correspondent aux agents, APIs, automatisation et logiciel; le niveau d'expérience exact n'est pas visible dans l'extrait.",
      junior_status="Oui — stage QA junior récent; rôle AI non confirmé junior", junior_evidence="Doctorina a publié un stage Junior QA à Varsovie et recrute activement. L'offre AI Platform Engineer a été publiée il y a quatre mois.",
      foreign_employee_status="Non vérifiable — présence à Varsovie", foreign_employee_evidence="Les publications récentes indiquent des postes en présentiel à Varsovie; aucune option Tunisie/remote internationale ni visa n'est annoncée.",
      active_jobs="Automation AI Platform Engineer — publication encore accessible, actualité à confirmer — https://www.linkedin.com/posts/kseniyapavlova_job-automation-ai-activity-7437175238167093248-a1PM ; autres recrutements récents à Varsovie",
      linkedin_contact_name="Ksu Paulava", linkedin_contact_role="Recruiting/People contact — Doctorina", linkedin_profile="https://pl.linkedin.com/in/kseniyapavlova", contact_verification="Profil Doctorina actuel publiant les offres et l'adresse work@doctorina.com.",
      verified_email="work@doctorina.com", email_status="Adresse de candidature publiée dans plusieurs offres Doctorina récentes", application_channel="mailto:work@doctorina.com",
      sources="https://pl.linkedin.com/in/kseniyapavlova | https://www.linkedin.com/posts/kseniyapavlova_job-automation-ai-activity-7437175238167093248-a1PM",
      verification_status="Vérifié — très bon fit HealthTech/LLM, localisation et niveau à confirmer",
      email_subject="Application – Junior AI / Automation Platform Engineer",
      email_body="""Dear Ms Paulava,

I am a recent Computer Engineering graduate from ENSI interested in Doctorina's AI and automation engineering work. My final-year project at Linedata focused on integrating AI agents into an existing financial product, including tool use, APIs and application integration.

I bring skills in Python, LLM applications, Java, C++, databases, full-stack development, testing, Git and CI/CD. Doctorina's mission to turn LLM capabilities into a reliable healthcare product is exactly the type of practical, high-impact AI work I want to pursue.

I am based in Tunisia and open to relocating to Warsaw if work-authorization support is possible. I would also welcome consideration for a junior engineering or QA-automation route.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello Ms Paulava, I am a recent ENSI Computer Engineering graduate with an AI-agent PFE at Linedata and skills in Python, LLMs, APIs and full-stack development. Doctorina's LLM-powered healthcare mission strongly interests me. Glad to connect.",
      linkedin_followup="Thank you for connecting. I am interested in Doctorina's AI automation work and sent my CV to work@doctorina.com. Could a junior Tunisian engineer willing to relocate to Warsaw be considered for a suitable technical role?"),
    r("fourity",
      sector="Web/mobile product development, React, TypeScript, Node.js, AWS and serverless", target_roles="Junior Full-stack Developer; React/Node.js Engineer; Software Engineer", match_score_10="7.6", potential_score_100="44", priority="Moyenne",
      match_reason="Stack MERN/React/Node/AWS fortement pertinente, mais l'unique poste actuel demande au moins six ans.", junior_status="Non — aucune offre junior active confirmée", junior_evidence="Le portail actuel ne présente qu'un Senior Software Engineer avec six ans minimum; l'entreprise continue néanmoins d'élargir son équipe.",
      active_jobs="Senior Software Engineer — Novi Sad — 6+ ans — https://www.fourity.com/careers/",
      linkedin_contact_name="Fourity", linkedin_contact_role="Canal officiel", linkedin_profile="https://www.linkedin.com/company/fourity", contact_verification="Aucun recruteur individuel actuel identifié avec certitude.",
      verified_email="office@fourity.com", email_status="Adresse de candidature publiée sur la page Careers officielle", application_channel="mailto:office@fourity.com", sources="https://www.fourity.com/careers/ | https://www.linkedin.com/company/fourity",
      verification_status="Vérifié — excellente stack, mais offre actuelle senior",
      email_subject="Spontaneous Application – Junior Full-stack Software Engineer",
      email_body="""Dear Fourity Team,

I am a recent Computer Engineering graduate from ENSI seeking a junior full-stack software engineering opportunity. I have experience with React, Node.js, APIs, databases, JavaScript/TypeScript, Python, Java, C++, Git and CI/CD. My final-year project at Linedata also involved integrating AI agents into an existing financial product.

Your current opening is clearly senior, so I am not presenting myself for that position. I would instead be grateful to be considered for a future junior role where I can contribute to React/Node.js products and grow within your collaborative engineering culture.

I am based in Tunisia and open to relocation to Novi Sad if feasible.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with React, Node.js, APIs and AI-agent project experience. Fourity's product-development stack strongly matches mine. I would be glad to follow future junior opportunities in Novi Sad.",
      linkedin_followup="Thank you for connecting. I saw that the current Software Engineer role requires 6+ years. Could Fourity keep my profile for a future junior React/Node.js or full-stack opportunity open to relocation?"),
    r("jawaker",
      sector="Mobile gaming, backend services, product engineering and data", target_roles="Junior Software Engineer; Backend Developer; QA Engineer; Data/AI Engineer", match_score_10="6.9", potential_score_100="39", priority="Faible",
      match_reason="Développement produit pertinent, mais les dernières offres techniques identifiées sont anciennes et senior; aucune offre junior actuelle confirmée.", junior_status="Non vérifiable", junior_evidence="Jawaker possède un portail carrière, mais les offres Senior/Principal retrouvées datent de 2024–2025.",
      active_jobs="Aucune offre junior active confirmée; vérifier le portail officiel https://careers.jawaker.com/",
      linkedin_contact_name="Jawaker", linkedin_contact_role="Canal officiel carrières", linkedin_profile="https://www.linkedin.com/company/jawaker", contact_verification="Aucun recruteur individuel actuel identifié de manière fiable.",
      application_channel="https://careers.jawaker.com/", sources="https://careers.jawaker.com/ | https://www.linkedin.com/company/jawaker",
      verification_status="Vérifié — entreprise produit pertinente, aucune ouverture junior confirmée",
      email_subject="Spontaneous Application – Junior Software Engineer",
      email_body="""Dear Jawaker Team,

I am a recent Computer Engineering graduate from ENSI seeking a junior software engineering opportunity. My background includes Java, Python, C++, full-stack development, APIs, databases, testing, Git and CI/CD. At Linedata, my final-year project focused on integrating AI agents into an existing financial software product.

I am attracted by Jawaker's large-scale consumer product and the engineering challenges behind reliable mobile-game services. I noticed that the technical openings available in public search results are senior, so I would like to be considered for a future graduate or junior software, QA or data role.

I am based in Tunisia and willing to relocate to the UAE or Jordan if feasible.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with Java/Python/C++, full-stack and AI-agent experience. Jawaker's large-scale gaming product interests me, and I would be glad to follow future junior software, QA or data opportunities.",
      linkedin_followup="Thank you for connecting. I found only older senior engineering openings. Could you advise whether Jawaker expects any junior software, QA or data roles that could consider a Tunisian graduate open to relocation?"),
    r("novinopath",
      sector="Digital pathology, cloud LIS/IMS, medical imaging AI and healthcare software", target_roles="Junior AI/ML Engineer; Healthcare Software Engineer; Python/Cloud Developer", match_score_10="7.7", potential_score_100="47", priority="Moyenne",
      match_reason="Bonne adéquation IA, cloud et produit logiciel, mais l'équipe recherche une expérience healthcare/FDA et aucune offre technique active n'a été confirmée.", junior_status="Non vérifiable", junior_evidence="Le site mentionne une culture ouverte aux interns et la progression interne, mais ne publie pas actuellement de rôle junior correspondant.",
      foreign_employee_status="Oui/partiel — entreprise remote-first", foreign_employee_evidence="Le site indique une équipe distribuée et 'hires for talent, not zip code'; les pays autorisés, le contrat international et le sponsoring restent non précisés.",
      active_jobs="Aucune offre technique active confirmée — consulter les open roles depuis https://www.novopath.com/about-us/",
      linkedin_contact_name="NovinoAI / NovoPath", linkedin_contact_role="Canal officiel", linkedin_profile="https://www.linkedin.com/company/novopath", contact_verification="Aucun recruteur individuel vérifié pour une ouverture technique actuelle.",
      application_channel="https://www.novopath.com/about-us/", sources="https://www.novinoai.com/ | https://www.novinoai.com/about.html | https://www.novopath.com/about-us/",
      verification_status="Vérifié — HealthTech IA pertinente et remote-first, aucune offre actuelle",
      email_subject="Spontaneous Application – Junior AI / Healthcare Software Engineer",
      email_body="""Dear NovinoAI / NovoPath Team,

I am a recent Computer Engineering graduate from ENSI seeking a junior AI or software engineering opportunity. My final-year project at Linedata focused on integrating AI agents into an existing financial product, giving me practical experience with Python, LLM applications, APIs, databases and product integration.

I also bring Java, C++, full-stack development, machine learning, testing, Git and CI/CD. I am particularly interested in your work because it turns AI and cloud software into a dependable clinical workflow rather than a standalone demonstration.

I am based in Tunisia and would welcome a remote international arrangement or relocation where feasible.

Kind regards,
Mohamed Oussema Bahloul""",
      linkedin_invitation="Hello, I am a recent ENSI Computer Engineering graduate with AI-agent, Python and full-stack experience. NovinoAI's cloud-native digital pathology platform is the kind of high-impact product I want to help build. Glad to connect.",
      linkedin_followup="Thank you for connecting. Does your remote-first team accept spontaneous applications from international junior AI/software engineers? I would be glad to share my CV and project portfolio."),
]

fields=[]
for row in RECORDS:
    for key in row:
        if key not in fields: fields.append(key)
with OUT.open("w",encoding="utf-8-sig",newline="") as h:
    w=csv.DictWriter(h,fieldnames=fields); w.writeheader(); w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
