#!/usr/bin/env python3
"""Fast verified foreign-company batch, checked on 2026-09-25."""
from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_13.csv"


def record(key: str, **values: str) -> dict[str, str]:
    base = {
        "organization_key": key,
        "sector": "Non trouvé/non vérifiable",
        "target_roles": "Non trouvé/non vérifiable",
        "match_score_10": "0.0",
        "match_reason": "Non trouvé/non vérifiable",
        "junior_status": "Non vérifiable",
        "junior_evidence": "Non trouvé/non vérifiable",
        "foreign_employee_status": "Non vérifiable",
        "foreign_employee_evidence": "Aucune politique publique de visa ou relocation trouvée.",
        "active_jobs": "Aucune offre adaptée confirmée le 2026-09-25.",
        "linkedin_contact_name": "Non trouvé/non vérifiable",
        "linkedin_contact_role": "Non trouvé/non vérifiable",
        "linkedin_profile": "Non trouvé/non vérifiable",
        "contact_verification": "Non trouvé/non vérifiable",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucun email public vérifié",
        "application_channel": "Non trouvé/non vérifiable",
        "recommended_cv": "CV_ATS_EN.pdf",
        "language": "Anglais",
        "potential_score_100": "0",
        "sources": "Non trouvé/non vérifiable",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — recherche manuelle effectuée",
        "notes": "",
        "email_subject": "Spontaneous Application – Junior Software / AI Engineer",
        "email_body": "",
        "linkedin_invitation": "",
        "linkedin_followup": "",
    }
    base.update(values)
    return base


RECORDS = [
    record(
        "aicentive gmbh",
        sector="AI-based industrial energy optimization, Data Science and energy management software (the current brand is encentive)",
        target_roles="Junior AI/ML Engineer; Data Scientist; Python Software Engineer; Data/Optimization Engineer",
        match_score_10="8.3",
        match_reason="The company combines AI, industrial data and optimization. Mohamed's Python, ML and software-engineering background is relevant, although he lacks direct energy-sector experience and German proficiency is not documented.",
        junior_status="Yes — internships and working-student roles are active, but no matching junior engineering vacancy",
        junior_evidence="The official career page states that responsibility is given from interns to founders. The live portal lists three internship/working-student roles and an unsolicited permanent application.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="The team advertises nine languages, but the public pages do not promise visa sponsorship or relocation. Current roles are in Berlin/Hamburg and student roles normally require German enrolment.",
        active_jobs="Unsolicited Application — Berlin/Hamburg/Hybrid/Remote — https://encentive.jobs.personio.de/job/2134556 ; current student roles are business-facing rather than AI engineering.",
        linkedin_contact_name="Daniel Ehnes",
        linkedin_contact_role="Co-founder / Managing Director — encentive",
        linkedin_profile="https://de.linkedin.com/in/ehnes",
        contact_verification="Current encentive leader; official career page names Daniel Ehnes in the management team and LinkedIn shows current activity.",
        application_channel="https://encentive.jobs.personio.de/",
        potential_score_100="54",
        sources="https://www.encentive.de/karriere | https://encentive.jobs.personio.de/ | https://de.linkedin.com/in/ehnes",
        verification_status="Vérifié — excellente adéquation IA/Data, candidature spontanée active, mobilité internationale non documentée",
        notes="Le nom Aicentive du CSV semble être une ancienne graphie ou une erreur; l'entreprise actuelle est encentive. Utiliser le portail, pas l'adresse générale contact@encentive.de.",
        email_subject="Spontaneous Application – Junior AI / Data Engineer",
        email_body="""Dear encentive Team,

I am a recent Computer Engineering graduate from ENSI, specialized in Financial Engineering, and I would like to express my interest in a junior AI, data, or software-engineering opportunity at encentive.

During my final-year project at Linedata, I contributed to modernizing a financial product through AI agents, connecting business needs with the implementation of a usable software solution. My background includes Python, machine learning, data processing, APIs, databases, and full-stack development.

encentive particularly interests me because it applies AI and optimization to a concrete industrial challenge with measurable economic and environmental value. I would be motivated to grow within this product-focused environment and contribute wherever my software and analytical profile can be useful.

I am currently based in Tunisia and open to relocation. I understand that work-authorisation support is not stated publicly, and I would be grateful to know whether an international junior application could be considered.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Mr Ehnes, I’m an ENSI Computer Engineering graduate with a Financial Engineering background and an AI-agent PFE at Linedata. encentive’s use of AI for measurable industrial impact strongly interests me. I’d be glad to connect.",
        linkedin_followup="Hello Mr Ehnes, thank you for connecting. I am seeking a first role in AI, data or software engineering and am open to relocating from Tunisia. Would encentive consider an international junior profile through its unsolicited-application route? I would be happy to share my CV.",
    ),
    record(
        "cloudsquid",
        sector="Agentic AI for enterprise finance, procurement, operations and compliance workflows",
        target_roles="Junior AI Engineer; Agentic AI Engineer; Python/Full-stack Engineer; Data Engineer",
        match_score_10="9.3",
        match_reason="This is one of the closest matches: AI agents applied to document-heavy finance workflows closely mirrors Mohamed's Linedata PFE and Financial Engineering specialization.",
        junior_status="No active role",
        junior_evidence="The official JOIN career page states that there are no available jobs as of 2026-09-25.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="The company is Berlin-based. No public visa-sponsorship, relocation or international-remote policy was found.",
        active_jobs="No available jobs — https://join.com/companies/cloudsquid",
        linkedin_contact_name="Sangwoo Bae",
        linkedin_contact_role="Founder & CTO — cloudsquid",
        linkedin_profile="https://de.linkedin.com/in/sangwoo-bae",
        contact_verification="Current founder and CTO according to his current LinkedIn profile and cloudsquid's official company page.",
        application_channel="https://join.com/companies/cloudsquid",
        potential_score_100="57",
        sources="https://www.cloudsquid.io/de-de/ | https://join.com/companies/cloudsquid | https://www.linkedin.com/company/cloudsquid/ | https://de.linkedin.com/in/sangwoo-bae",
        verification_status="Vérifié — correspondance exceptionnelle, mais aucun poste ouvert et mobilité non documentée",
        notes="Ne pas envoyer automatiquement d'email : filip@cloudsquid.io figure dans le CSV mais n'est pas publié comme adresse de recrutement actuelle. Privilégier LinkedIn et surveiller le portail.",
        email_subject="Future Junior AI Engineering Opportunities at cloudsquid",
        email_body="""Dear cloudsquid Team,

I am a recent Computer Engineering graduate from ENSI with a specialization in Financial Engineering. My final-year project at Linedata focused on modernizing a financial product with AI agents, which makes cloudsquid's work on agentic automation for finance and operations particularly relevant to my background.

I have practical experience with Python, AI and machine learning, APIs, databases, full-stack development, and the integration of AI capabilities into an existing business product. I am looking for a first full-time role where I can keep developing these skills while contributing to a real product.

I noticed that your official career page currently has no open positions, so I am writing only to express interest in a future junior AI or software-engineering opportunity. I am based in Tunisia and open to relocation.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Mr Bae, my ENSI engineering PFE at Linedata involved AI agents for a financial product. cloudsquid’s agentic automation for Finance & Ops is an unusually close match to my background. I’d be glad to connect and follow future engineering opportunities.",
        linkedin_followup="Hello Mr Bae, thank you for connecting. I saw that cloudsquid currently has no vacancies, but its combination of AI agents and finance workflows closely matches my Linedata PFE and Financial Engineering specialization. May I share my CV for a future junior engineering need?",
    ),
    record(
        "meddevo",
        sector="MedTech regulatory-documentation software, APIs and digital workflows",
        target_roles="Junior Backend Developer; Python/TypeScript Developer; API/Software Engineer; Data/Automation Engineer",
        match_score_10="6.9",
        match_reason="Mohamed's API, database, full-stack and software-engineering skills are relevant. The visible backend role requires several years, TypeScript/NestJS, German B2 and work from Germany.",
        junior_status="Spontaneous applications accepted; no matching junior vacancy confirmed",
        junior_evidence="The current official career page explicitly accepts general applications and emphasizes growth opportunities, but the available backend description asks for several years of experience.",
        foreign_employee_status="Non",
        foreign_employee_evidence="The official careers page states 100% remote from anywhere in Germany, not international remote. The backend description asks for German and English at B2 or above; no sponsorship promise was found.",
        active_jobs="General Application — https://meddevo.com/de/jobs/bewerben ; the published Backend Developer page asks for several years of experience and German B2.",
        linkedin_contact_name="Markus Falk",
        linkedin_contact_role="Current meddevo team member and named contact on the backend vacancy",
        linkedin_profile="https://de.linkedin.com/in/markus-falk-69b195109",
        contact_verification="The official job page names Markus Falk and his current LinkedIn profile lists meddevo.com.",
        application_channel="https://meddevo.com/de/jobs/bewerben",
        potential_score_100="38",
        sources="https://meddevo.com/de/jobs | https://www.meddevo.com/jobs/back-end-entwickler-m-w-d | https://de.linkedin.com/in/markus-falk-69b195109",
        verification_status="Vérifié — candidature spontanée ouverte, mais travail limité à l’Allemagne et exigence linguistique défavorable",
        notes="Faible priorité sans allemand B2 et sans autorisation de travail allemande. Utiliser le formulaire, pas contact@meddevo.com.",
        email_subject="Spontaneous Application – Junior Software Engineer",
        email_body="""Dear meddevo Team,

I am a recent Computer Engineering graduate from ENSI, with experience in software development, APIs, databases, AI and full-stack applications. My final-year project at Linedata involved integrating AI agents into an existing financial product and taught me how to connect technical implementation with a regulated business context.

I am interested in meddevo's mission of improving regulatory documentation through practical software. I would be glad to be considered for a future junior backend, API, automation or data-oriented position.

I am currently based in Tunisia and open to relocation. I also understand that your current remote policy is limited to Germany and that some roles require German; I would therefore appreciate confirmation before any formal application.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Mr Falk, I’m a recent ENSI Computer Engineering graduate with software, API and AI experience gained notably through my Linedata PFE. meddevo’s product work in a regulated field interests me, and I’d be glad to connect.",
        linkedin_followup="Hello Mr Falk, thank you for connecting. I am exploring junior software/API opportunities and am open to relocation from Tunisia. I saw that meddevo accepts general applications but works remotely within Germany. Could an international junior profile be considered in the future?",
    ),
    record(
        "neusta inspire gmbh",
        sector="Atlassian consulting, DevOps, cloud migration, application operations and software development",
        target_roles="Junior Software Developer; Full-stack Developer; DevOps/Cloud Junior; Application Operations Engineer",
        match_score_10="7.2",
        match_reason="The software, APIs, full-stack, Git and CI/CD background fits software and DevOps work. The main gaps are German-market experience and likely German-language requirements.",
        junior_status="Yes — official page explicitly welcomes IT newcomers",
        junior_evidence="The current official career page says it seeks both experienced colleagues and newcomers to IT and explicitly invites spontaneous applications.",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Jobs and offices are Germany-based. Home office is offered, but no visa sponsorship, relocation or international remote arrangement is documented.",
        active_jobs="Softwareentwickler:in Full Stack — Berlin — https://www.team-neusta.de/karriere/offene-stellen?company=neustainspire&field=all&level=all&location=all&type=all ; spontaneous applications are explicitly welcomed.",
        linkedin_contact_name="Martin S. Fredrich",
        linkedin_contact_role="Founder/shareholder and official contact for personnel questions — neusta inspire",
        linkedin_profile="https://de.linkedin.com/in/martin-fredrich-b69380173",
        contact_verification="The official career page names Martin S. Fredrich as the personnel contact; LinkedIn confirms his current leadership role.",
        application_channel="https://www.team-neusta.de/karriere/offene-stellen?company=neustainspire&field=all&level=all&location=all&type=all",
        potential_score_100="52",
        sources="https://www.neusta-inspire.de/karriere/ | https://www.team-neusta.de/karriere/offene-stellen?company=neustainspire&field=all&level=all&location=all&type=all | https://de.linkedin.com/in/martin-fredrich-b69380173",
        verification_status="Vérifié — nouveaux entrants acceptés et candidature spontanée ouverte, mobilité non documentée",
        notes="Cible intéressante mais non prioritaire sans allemand. L'email affiché par le site est protégé/incomplet; utiliser le portail ou LinkedIn.",
        email_subject="Spontaneous Application – Junior Software / DevOps Engineer",
        email_body="""Dear Mr Fredrich,

I am a recent Computer Engineering graduate from ENSI and would like to express my interest in a junior software-development, application-operations or DevOps opportunity at neusta inspire.

My final-year project at Linedata focused on modernizing a financial product with AI agents. I also developed skills in Python, Java, C++, full-stack development, APIs, databases, Git, testing and CI/CD. I am particularly attracted by environments where junior engineers can learn through real product and customer challenges.

Your explicit openness to IT newcomers encouraged me to contact you. I am currently based in Tunisia and open to relocation; as international mobility support is not described publicly, I would be grateful to know whether my profile could be considered.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Mr Fredrich, your career page’s openness to IT newcomers caught my attention. I’m a recent ENSI Computer Engineering graduate with software, API, AI and CI/CD experience, notably through my Linedata PFE. I’d be glad to connect.",
        linkedin_followup="Hello Mr Fredrich, thank you for connecting. I am looking for a first software/DevOps opportunity and am open to relocating from Tunisia. Would neusta inspire consider an international junior profile through its spontaneous-application route? I would be glad to send my CV.",
    ),
]

fieldnames = list(RECORDS[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(RECORDS)

print(f"Wrote {len(RECORDS)} records to {OUT}")
