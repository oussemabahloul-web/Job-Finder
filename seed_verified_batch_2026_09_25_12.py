#!/usr/bin/env python3
"""Verified company research batch checked on 2026-09-25."""
from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_12.csv"


def record(key: str, **values: str) -> dict[str, str]:
    base = {
        "organization_key": key,
        "sector": "Non trouvé/non vérifiable",
        "target_roles": "Non trouvé/non vérifiable",
        "match_score_10": "0.0",
        "match_reason": "Non trouvé/non vérifiable",
        "junior_status": "Non vérifiable",
        "junior_evidence": "Non trouvé/non vérifiable",
        "active_jobs": "Aucune offre active confirmée le 2026-09-25.",
        "linkedin_contact_name": "Non trouvé/non vérifiable",
        "linkedin_contact_role": "Non trouvé/non vérifiable",
        "linkedin_profile": "Non trouvé/non vérifiable",
        "contact_verification": "Non trouvé/non vérifiable",
        "verified_email": "Aucun email public vérifié",
        "email_status": "Aucun email public vérifié",
        "application_channel": "Non trouvé/non vérifiable",
        "recommended_cv": "CV_ATS.pdf",
        "language": "Français",
        "potential_score_100": "0",
        "foreign_employee_status": "Sans objet — Tunisie",
        "foreign_employee_evidence": "Candidature locale en Tunisie.",
        "sources": "Non trouvé/non vérifiable",
        "checked_date": "2026-09-25",
        "verification_status": "Vérifié — recherche manuelle effectuée",
        "notes": "",
        "email_subject": "Candidature spontanée — Ingénieur informatique junior",
        "email_body": "",
        "linkedin_invitation": "",
        "linkedin_followup": "",
    }
    base.update(values)
    return base


RECORDS = [
    record(
        "rhis solutions",
        sector="Édition de logiciels SIRH, planification, prédiction, machine learning, Java/Angular, AWS et DevOps",
        target_roles="Ingénieur logiciel junior; Java/Angular junior; DevOps/Cloud junior; Data/ML junior; support applicatif junior",
        match_score_10="8.8",
        match_reason="Java, Python, APIs, SQL, full-stack, IA et cloud correspondent aux produits et équipes R&D de RHIS. Le PFE Linedata prouve aussi la capacité à moderniser un produit métier existant.",
        junior_status="Oui — preuve directe, mais aucune offre junior ouverte aujourd’hui",
        junior_evidence="RHIS a publié un poste Ingénieur DevOps Junior, Bac+5 et débutant accepté, et accueille des stagiaires. Cette annonce date d’environ un an et n’est pas active.",
        active_jobs="Aucune offre adaptée encore ouverte. Support Applicatif L2 — https://tn.linkedin.com/jobs/view/support-applicatif-l2-at-rhis-software-4468650725 — n’accepte plus les candidatures et demande 2–3 ans. Les anciennes offres Full-Stack et DevOps junior sont closes.",
        linkedin_contact_name="Inés CHARGUI",
        linkedin_contact_role="HR Manager / IT Talent Acquisition — RHIS Software",
        linkedin_profile="https://www.linkedin.com/pub/dir/%2B/Chargui/tn-0-Tunisia",
        contact_verification="L’annuaire LinkedIn et la page RHIS identifient actuellement Inés CHARGUI. Ouvrir son profil depuis les employés RHIS afin d’éviter l’homonyme allemand.",
        verified_email="recrutement.tunis@rhis-solutions.com",
        email_status="Adresse publiée par RHIS Software dans une annonce junior; l’annonce est ancienne, mais le canal RH est vérifiable.",
        application_channel="https://sge.rhis-solutions.com/ | https://www.linkedin.com/company/rhis-software",
        potential_score_100="76",
        sources="https://www.linkedin.com/company/rhis-software | https://fr.linkedin.com/posts/rhis-software_hello-linkedin-rhis-software-recrute-activity-7251973354167877635-3jq7 | https://tn.linkedin.com/jobs/view/support-applicatif-l2-at-rhis-software-4468650725 | https://sge.rhis-solutions.com/",
        verification_status="Vérifié — junior-friendly démontré; aucune offre adaptée active",
        notes="Haute priorité en candidature spontanée. Ne pas écrire que le poste DevOps Junior est encore ouvert.",
        email_subject="Candidature spontanée — Ingénieur logiciel / IA junior ENSI",
        email_body="""Bonjour Madame Chargui,

Récemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, je souhaite proposer ma candidature spontanée pour une première opportunité en développement logiciel, Data/IA ou DevOps chez RHIS Software.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. J’ai travaillé de la compréhension du besoin jusqu’à l’intégration dans une application existante. Je maîtrise Java, Python, C++, le full-stack, les APIs, SQL, les bases de données, le machine learning et les bases du cloud/CI-CD.

L’environnement produit de RHIS, à la croisée du logiciel métier, de la Data et du cloud, correspond à mon profil. Les offres visibles étant closes ou expérimentées, ma démarche concerne un besoin junior présent ou futur.

Je joins mon CV et reste disponible pour un échange.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour Mme Chargui, jeune diplômé ingénieur ENSI, mon PFE Linedata portait sur la modernisation d’un produit avec des agents IA. Le logiciel métier, la Data et le cloud chez RHIS correspondent à mon profil. Ravi de suivre vos futurs besoins juniors.",
        linkedin_followup="Bonjour Madame Chargui, merci pour la connexion. Je vous ai transmis une candidature spontanée à recrutement.tunis@rhis-solutions.com. Les offres visibles étant closes ou expérimentées, je souhaite seulement être considéré pour un futur besoin junior en logiciel, Data/IA ou DevOps.",
    ),
    record(
        "shamash information technology",
        sector="FinTech et logiciels d’affacturage pour banques; ERP/Odoo, outsourcing IT et transformation digitale",
        target_roles="Ingénieur logiciel FinTech junior; Business Analyst technique; Data/IA junior; full-stack; QA/Data Processing junior",
        match_score_10="9.4",
        match_reason="La spécialisation en ingénierie financière, le PFE Linedata, les agents IA et le développement correspondent directement à Xpert-Factor et aux solutions bancaires de Shamash.",
        junior_status="Oui — stages/PFE et rôles 1 à 3 ans observés",
        junior_evidence="Le PFE Book 2025 et d’anciens postes QA/Data Processing à 1–3 ans prouvent l’accueil de profils précoces. La page Carrières indique néanmoins qu’aucune offre n’est disponible actuellement.",
        active_jobs="Aucune offre disponible actuellement selon la page Carrières officielle. Les anciennes fiches Quality Assurance Analyst et Data Processing encore rendues dans la page ne sont pas actives.",
        linkedin_contact_name="Aymen Lagha",
        linkedin_contact_role="Collaborateur/chef de projet actuel chez Shamash-IT — contact métier technique",
        linkedin_profile="https://fr.linkedin.com/in/aymen-lagha-43a8408a",
        contact_verification="Profil actuel rattaché à Shamash-IT. Aucun recruteur personnel actuel plus fiable n’a été identifié; lui demander une orientation.",
        verified_email="recrutement@shamash-it.com",
        email_status="Adresse explicitement publiée sur la page Carrières officielle pour les candidatures spontanées.",
        application_channel="https://www.shamash-it.com/carrieres/ | recrutement@shamash-it.com",
        recommended_cv="CV_ATS_Fintech.pdf",
        potential_score_100="82",
        sources="https://www.shamash-it.com/ | https://www.shamash-it.com/carrieres/ | https://www.linkedin.com/company/shamash-it | https://fr.linkedin.com/in/aymen-lagha-43a8408a | https://files.thetunisianengineers.com/pfe_books_2025/PFE%20Book%20-%202025%20-%20Shamash%20Information%20Technology.pdf",
        verification_status="Vérifié — excellente cible FinTech; candidature spontanée officiellement acceptée",
        notes="Très haute priorité. Insister sur la modernisation de produits financiers et la valeur métier de l’IA.",
        email_subject="Candidature spontanée — Ingénieur informatique junior FinTech / IA",
        email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, spécialisé en ingénierie financière, je souhaite proposer ma candidature spontanée à Shamash IT pour une première opportunité liée aux solutions FinTech, au développement logiciel, à la Data ou à l’IA.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier grâce à des agents IA. J’y ai appris à comprendre les processus métier, identifier les usages où l’IA apporte une valeur concrète et intégrer la solution dans un produit existant.

Votre expertise dans l’affacturage, les solutions bancaires et la transformation digitale correspond précisément à mon projet. Votre page Carrières indiquant que les candidatures spontanées sont acceptées, je vous transmets mon CV pour un besoin junior présent ou prochain.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour M. Lagha, jeune diplômé ENSI spécialisé en ingénierie financière, mon PFE Linedata portait sur un produit financier modernisé avec des agents IA. Shamash réunit logiciel, banques et factoring. Pourriez-vous m’orienter vers le bon interlocuteur junior ?",
        linkedin_followup="Bonjour M. Lagha, merci pour la connexion. J’ai envoyé une candidature spontanée à recrutement@shamash-it.com conformément à votre page Carrières. Mon profil combine développement, IA et ingénierie financière. Pourriez-vous m’indiquer l’équipe la plus pertinente ?",
    ),
    record(
        "smart it partner",
        sector="Développement Web/mobile, IA, LLM, computer vision, cloud, DevOps et formation IT",
        target_roles="Junior AI Engineer; full-stack junior; Java/Python Developer; Cloud/DevOps junior; ingénieur R&D produit",
        match_score_10="9.1",
        match_reason="Le site 2026 cite explicitement ML, LLM, computer vision, Web/mobile, cloud et CI/CD, ce qui couvre presque tout le socle du candidat avec une expérience agentique différenciante.",
        junior_status="Oui — preuves récentes de stages et PFE",
        junior_evidence="Des profils publics documentent des PFE et stages 2025–2026 chez Smart IT Partner, encadrés par Mohamed Amine Mezghich et Seif Eddine Amara. Aucun emploi junior actuel n’est confirmé.",
        active_jobs="Aucune offre d’emploi ouverte confirmée le 2026-09-25. Candidature spontanée recommandée pour IA/LLM, full-stack ou cloud.",
        linkedin_contact_name="Mohamed Amine Mezghich",
        linkedin_contact_role="Fondateur de Smart IT Partner et encadrant technique",
        linkedin_profile="https://www.linkedin.com/company/smart-it-partner",
        contact_verification="La page officielle confirme qu’il a fondé l’entreprise; son email est publié sur le site. Rechercher son nom exact depuis la page entreprise pour son profil personnel.",
        verified_email="ma.mezghich@smart-it-partner.com",
        email_status="Adresse professionnelle affichée sur le site officiel 2026.",
        application_channel="https://www.smart-it-partner.com/ | formulaire officiel et ma.mezghich@smart-it-partner.com",
        potential_score_100="79",
        sources="https://www.smart-it-partner.com/ | https://tn.linkedin.com/company/smart-it-partner | https://fr.linkedin.com/posts/douaa-atallah_ing%C3%A9nieure-enetcom-smartitpartner-activity-7346555111713759234-KLVH | https://www.linkedin.com/posts/ouerghemmi-emna-10a468217_springboot-angular-java-activity-7369411479529250822-lKAK",
        verification_status="Vérifié — excellente adéquation et accueil junior démontré; pas d’offre active",
        notes="Très bonne candidature spontanée. Mettre en avant agentic AI + full-stack.",
        email_subject="Candidature spontanée — Ingénieur IA / Full-Stack junior ENSI",
        email_body="""Bonjour Monsieur Mezghich,

Récemment diplômé ingénieur en informatique de l’ENSI, je souhaite proposer ma candidature spontanée pour une première opportunité en IA, développement full-stack ou cloud chez Smart IT Partner.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. Je maîtrise Python, Java, C++, le développement Web, mobile et desktop, les APIs, SQL, le machine learning et les LLM/RAG.

Votre positionnement autour du Web/mobile, de l’IA, des LLM, de la computer vision et du cloud correspond particulièrement à mon profil polyvalent. Je serais motivé à contribuer rapidement à des produits concrets et à progresser au contact de votre équipe.

Je joins mon CV et reste disponible pour échanger.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour M. Mezghich, jeune diplômé ENSI, mon PFE Linedata portait sur des agents IA intégrés à un produit. Les activités de Smart IT Partner en LLM/ML, Web, cloud et DevOps correspondent fortement à mon profil. Ravi d’échanger sur un futur besoin junior.",
        linkedin_followup="Bonjour Monsieur Mezghich, merci pour la connexion. Je vous ai envoyé ma candidature à l’adresse publiée sur votre site. Mon profil associe agents IA, Python/Java/C++, APIs et full-stack. Je serais ravi de contribuer à un projet produit ou client.",
    ),
    record(
        "standard sharing software",
        sector="Infrastructure IT, cloud, cybersécurité, réseaux, data centers et applications/IA",
        target_roles="Applied AI Engineer junior; Cloud/DevOps junior; Software Engineer; Data Engineer; cybersécurité junior",
        match_score_10="8.6",
        match_reason="L’ancien poste Applied AI Engineer correspond presque mot pour mot au PFE: Python, LLM, RAG, agents, APIs, CI/CD et 0–3 ans. Le candidat peut aussi viser logiciel ou cloud.",
        junior_status="Oui — explicitement étudiants, fresh graduates et 0–3 ans",
        junior_evidence="Le portail décrit ses stages pour étudiants et jeunes diplômés. Applied AI Engineer acceptait 0–3 ans et un projet LLM/RAG/agent, mais l’offre est close depuis le 17/09/2026.",
        active_jobs="Aucune: https://careers.3s.com.tn/jobs affiche 0 position et https://careers.3s.com.tn/internships 0 programme. Applied AI Engineer — https://careers.3s.com.tn/jobs/a92f9bb6-1ebd-49da-8340-cf03b407c51f — a fermé le 17/09/2026.",
        linkedin_contact_name="Sirine Nasri",
        linkedin_contact_role="Ingénieure Cloud & Software et ancienne encadrante PFE chez 3S",
        linkedin_profile="https://tn.linkedin.com/in/sirine-nasri",
        contact_verification="Profil actuel chez 3S; elle a encadré plusieurs PFE. Lui demander seulement une orientation.",
        email_status="recrutement@3s.com.tn apparaît dans une publication officielle vieille de trois ans; le portail 2026 centralise les candidatures et n’affiche aucune ouverture. Ne pas automatiser l’ancien email.",
        application_channel="https://careers.3s.com.tn/jobs | https://careers.3s.com.tn/internships",
        potential_score_100="73",
        sources="https://careers.3s.com.tn/ | https://careers.3s.com.tn/jobs | https://careers.3s.com.tn/internships | https://careers.3s.com.tn/jobs/a92f9bb6-1ebd-49da-8340-cf03b407c51f | https://www.linkedin.com/company/3s-tn | https://tn.linkedin.com/in/sirine-nasri",
        verification_status="Vérifié — fit IA junior exceptionnel démontré, portail actuellement vide",
        notes="Haute priorité de veille. Ne pas candidater à l’ancienne offre fermée.",
        email_subject="Candidature spontanée — Ingénieur Applied AI / Software junior",
        email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, je souhaite manifester mon intérêt pour une future opportunité junior en Applied AI, développement logiciel ou cloud chez 3S.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. Mon profil réunit Python, Java, C++, LLM/RAG, agents, APIs, bases de données, full-stack et notions de CI/CD.

L’offre Applied AI Engineer de 3S correspondait étroitement à mon parcours par son ouverture aux profils 0–3 ans. J’ai bien vérifié qu’elle est close depuis le 17 septembre et je ne candidate pas à cette annonce. Je souhaite seulement être considéré pour sa prochaine réouverture ou un besoin junior similaire.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour Sirine, jeune diplômé ENSI, mon PFE Linedata portait sur LLM/RAG et agents IA intégrés à un produit. L’offre Applied AI 0–3 ans de 3S correspondait à mon profil, mais je sais qu’elle est close. Pourriez-vous m’orienter vers un futur besoin similaire ?",
        linkedin_followup="Bonjour Sirine, merci pour la connexion. Je ne candidate pas à l’offre Applied AI close. Comme vous avez encadré des PFE chez 3S, pourriez-vous m’indiquer si une prochaine campagne junior/IA est prévue ou quel canal surveiller ?",
    ),
    record(
        "talys consulting",
        sector="Conseil et solutions FinTech pour banque, assurance, microfinance, GRC, Data, BI, RPA et transformation digitale",
        target_roles="Consultant FinTech junior; Business Analyst junior; Data/BI junior; développeur; AI/automation junior; consultant transformation digitale",
        match_score_10="9.5",
        match_reason="Talys combine exactement services financiers, transformation digitale, Data, logiciel et automatisation. La spécialisation financière et le PFE Linedata permettent de dialoguer avec les équipes métier et techniques.",
        junior_status="Oui historiquement — PFE et profils débutants; besoin actuel expérimenté",
        junior_evidence="Talys publie des PFE Books et a recruté de jeunes profils. Au 2026-09-25, le besoin tunisien visible concerne un Consultant Talend expérimenté.",
        active_jobs="Consultant Talend expérimenté — Tunisie, secteur bancaire — publié par Emna BEN ALI il y a environ une semaine: https://fr.linkedin.com/in/emna-ben-ali-9152901b4. Non adapté sans expérience Talend. Aucune offre junior actuelle confirmée.",
        linkedin_contact_name="Emna BEN ALI",
        linkedin_contact_role="Talent Acquisition Specialist — TALYS",
        linkedin_profile="https://fr.linkedin.com/in/emna-ben-ali-9152901b4",
        contact_verification="Profil actuel très actif, publiant les besoins TALYS Tunisie et France avec une adresse professionnelle directe.",
        verified_email="ebenali@talys.digital",
        email_status="Adresse publiée à plusieurs reprises par la recruteuse actuelle, y compris pour TALYS Tunisie en septembre 2026.",
        application_channel="ebenali@talys.digital | recrutement@talys.digital | https://www.linkedin.com/company/talys",
        recommended_cv="CV_ATS_Fintech.pdf",
        potential_score_100="81",
        sources="https://www.linkedin.com/company/talys | https://fr.linkedin.com/in/emna-ben-ali-9152901b4 | https://www.talys.digital/ | https://www.talys.digital/wp-content/uploads/2022/12/PFE-BOOK-TALYS-2023-VF.pdf",
        verification_status="Vérifié — cible FinTech prioritaire; offre actuelle expérimentée seulement",
        notes="Très haute priorité en candidature spontanée. Préciser que vous ne postulez pas au poste Talend expérimenté.",
        email_subject="Candidature junior — FinTech, Data/IA et transformation digitale",
        email_body="""Bonjour Madame Ben Ali,

Récemment diplômé ingénieur en informatique de l’ENSI, spécialisé en ingénierie financière, je souhaite vous proposer mon profil pour une première opportunité chez TALYS en FinTech, Data/IA, logiciel ou transformation digitale.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier grâce à des agents IA. Cette expérience m’a appris à comprendre les processus métier, identifier des usages d’automatisation à forte valeur et intégrer une solution dans un produit existant.

TALYS réunit banque, assurance, microfinance, Data et solutions digitales. J’ai bien vu votre besoin actuel de Consultant Talend expérimenté et je ne prétends pas correspondre à ce niveau. Ma démarche concerne un besoin junior présent ou futur où mon profil hybride pourrait être utile.

Je joins mon CV et serais ravi d’échanger avec vous.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Bonjour Mme Ben Ali, ingénieur ENSI récemment diplômé et spécialisé en ingénierie financière, mon PFE Linedata portait sur des agents IA pour un produit financier. TALYS réunit banque, Data et transformation digitale. Ravi de suivre vos futurs besoins juniors.",
        linkedin_followup="Bonjour Madame Ben Ali, merci pour la connexion. Je vous ai envoyé mon CV à ebenali@talys.digital. J’ai compris que le besoin Talend actuel exige de l’expérience; ma démarche concerne un futur poste junior en FinTech, Data/IA, logiciel ou transformation digitale.",
    ),
    record(
        "radix engineering and software",
        location_status="Étranger",
        country="États-Unis",
        eligible="Oui",
        location_reason="Les deux adresses CSV sont à Houston; « Tunis à distance » est une modalité et non une implantation tunisienne.",
        sector="Ingénierie numérique industrielle, logiciels, automatisation, Data/IA, asset performance et supply chain",
        target_roles="Junior Software Engineer; Data Engineer; AI/ML Engineer; Digital Solutions Analyst; Python/C++ Developer",
        match_score_10="8.2",
        match_reason="Python/C++, Data/IA, logiciel et analyse métier sont pertinents pour Radix. L’absence d’expérience industrielle et les postes visibles plutôt expérimentés réduisent le potentiel immédiat.",
        junior_status="Oui globalement — fresh graduates explicitement bienvenus",
        junior_evidence="La page Careers indique que les candidats sortant de l’université sont bienvenus et met en avant formation et développement. Les postes techniques visibles ne sont pas adaptés.",
        active_jobs="Des offres sont actives, mais aucune adaptée et internationalement accessible: Solutions Expert Supply Chain demande 5–8 ans; Program Manager exige expérience industrie/vente. Portail: https://radix.inhire.app/.",
        linkedin_contact_name="Ana Mastrangelo",
        linkedin_contact_role="People & Management Coordinator — Radix North America",
        linkedin_profile="https://www.linkedin.com/in/ana-mastrangelo-574298100",
        contact_verification="Le site Radix et LinkedIn la rattachent actuellement à Radix North America à Houston.",
        verified_email="contact@radixeng.com",
        email_status="Adresse générale publiée sur la page Careers pour les questions; ce n’est pas une adresse de candidature. Utiliser le portail.",
        application_channel="https://radix.inhire.app/ | https://www.radixeng.com/careers",
        recommended_cv="CV_ATS_EN.pdf",
        language="Anglais",
        potential_score_100="46",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Diversité internationale et modèle online/hybrid sont mentionnés, mais aucune offre adaptée ne confirme visa, relocation ou recrutement depuis la Tunisie. Les rôles US sont localisés aux États-Unis.",
        sources="https://www.radixeng.com/careers | https://radix.inhire.app/ | https://www.linkedin.com/company/radixeng/jobs | https://www.linkedin.com/in/ana-mastrangelo-574298100 | https://www.linkedin.com/jobs/view/solutions-expert-supply-chain-at-radix-4398495079",
        verification_status="Vérifié — entreprise étrangère junior-friendly, aucune voie internationale adaptée confirmée",
        notes="Priorité moyenne-faible. Surveiller Europe/remote/junior. Ne pas envoyer le CV à l’email général sans demande préalable.",
        email_subject="Future Junior Software / AI Opportunities — International Candidate",
        email_body="""Dear Radix People & Management Team,

I am a recent Computer Engineering graduate from ENSI in Tunisia, specialised in Financial Engineering, and I am interested in future junior software, data or AI opportunities at Radix.

My final-year project at Linedata modernised a financial product with AI agents, connecting business needs with software integration. My background includes Python, C++, Java, APIs, databases, full-stack development, machine learning and LLM/RAG applications.

Radix appeals to me because it turns engineering, operational data and digital technology into measurable industrial value. I have not found a junior opening confirming international eligibility, so I am not applying to an unsuitable role. Could you advise whether Radix may consider a Tunisia-based candidate in the future and which location I should monitor?

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Hello Ana, I’m a recent ENSI Computer Engineering graduate from Tunisia. My Linedata project used AI agents to modernise a business product. Radix’s blend of engineering, software and industrial data is compelling. May I follow future junior roles open internationally?",
        linkedin_followup="Thank you for connecting, Ana. I found no suitable junior role with confirmed international eligibility, so I have not applied to an unrelated opening. Could you advise whether a future software/data/AI role might consider a Tunisia-based graduate, or which Radix location I should monitor?",
    ),
    record(
        "responsible cyber",
        sector="Cybersécurité, gouvernance des risques tiers, conformité et plateforme IA IMMUNE X-TPRM",
        target_roles="Junior Cybersecurity/AI Engineer; Risk Data Analyst; Software Engineer; GRC Technology Analyst",
        match_score_10="7.6",
        match_reason="Développement, IA et ingénierie financière sont utiles à une plateforme combinant risques financiers, ESG et cyber. Le candidat n’a pas encore de spécialisation cyber/GRC profonde.",
        junior_status="Oui historiquement, situation actuelle non vérifiable",
        junior_evidence="D’anciens recrutements montrent des juniors et reconversions accompagnées, mais aucune campagne récente n’a été trouvée. Ces preuves ne valent pas offre actuelle.",
        linkedin_contact_name="Dr Magda Chelly",
        linkedin_contact_role="Fondatrice de Responsible Cyber; experte cyber et risque",
        linkedin_profile="https://www.linkedin.com/in/magda-chelly",
        contact_verification="Des sources 2026 la présentent toujours comme fondatrice; son profil demande de suivre plutôt que se connecter car la limite de relations est atteinte.",
        email_status="info@responsible-cyber.com figure dans le CSV, mais le domaine officiel est inaccessible et l’adresse n’a pas été retrouvée sur une page carrière actuelle; ne pas automatiser.",
        application_channel="https://riskimmune.com/ | https://www.linkedin.com/in/magda-chelly — suivre et surveiller",
        recommended_cv="CV_ATS_Fintech_EN.pdf",
        language="Anglais",
        potential_score_100="37",
        foreign_employee_status="Non vérifiable",
        foreign_employee_evidence="Entreprise historiquement à Singapour et équipe internationale, mais aucune offre actuelle ne précise visa, relocation, remote international ou B2B depuis la Tunisie.",
        sources="https://riskimmune.com/ | https://www.linkedin.com/in/magda-chelly | https://www.linkedin.com/posts/cybersecurityworldasia_responsiblecyber-riskmanagement-operationalresilience-activity-7090587743155597312-JQJV",
        verification_status="Vérifié — bonne piste cyber/risque, recrutement et mobilité non vérifiables",
        notes="Faible priorité immédiate. Suivre Dr Chelly; ne pas utiliser l’adresse CSV sans nouvelle validation.",
        email_subject="Future Junior AI / Cyber Risk Opportunities — ENSI Graduate",
        email_body="""Dear Responsible Cyber team,

I am a recent Computer Engineering graduate from ENSI in Tunisia, specialised in Financial Engineering, and I am interested in a future junior opportunity connecting AI, software and cyber-risk management.

My Linedata final-year project modernised a financial product with AI agents. It strengthened my ability to understand regulated processes, work with data and integrate intelligent workflows into a product. My background includes Python, software development, APIs, databases, ML and LLM/RAG systems.

IMMUNE X-TPRM is meaningful to me because it connects technology with financial, compliance and cybersecurity risk. I have found no current opening or verified international policy, so this is only an expression of interest for a future junior or internationally remote role.

Kind regards,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Dr Chelly’s profile has reached its connection limit; follow the profile rather than sending an invitation.",
        linkedin_followup="Hello Dr Chelly, I’m a recent ENSI graduate from Tunisia specialised in Financial Engineering. My Linedata project applied AI agents to a regulated product. I’m following your work on cyber and third-party risk and would value guidance on future junior roles at Responsible Cyber/RiskImmune.",
    ),
    record(
        "smart world it swit",
        sector="Commerce de gros d’équipements informatiques/électroniques — activité logicielle avancée non démontrée",
        target_roles="Support IT junior; intégration systèmes; technico-commercial IT; automatisation interne",
        match_score_10="3.8",
        match_reason="Le registre public disponible classe Smart World IT dans le commerce de gros d’équipements informatiques et électroniques. Aucun projet logiciel, Data ou IA tunisien n’est confirmé.",
        junior_evidence="Aucune annonce junior, page carrière ou équipe technique actuelle trouvée.",
        linkedin_contact_role="Aucun recruteur ou responsable actuel univoque identifié",
        contact_verification="Les recherches renvoient surtout des homonymes étrangers; aucun profil fourni pour éviter la mauvaise société.",
        email_status="contact@swit.com.tn figure dans le CSV, mais le domaine est inaccessible et l’adresse n’apparaît dans aucune source publique actuelle; ne pas envoyer automatiquement.",
        potential_score_100="18",
        sources="https://www.dnb.com/business-directory/company-information.household_appliances_and_electrical_and_electronic_goods_merchant_wholesalers.tn.html?page=3 | recherches exactes du domaine et du nom le 2026-09-25",
        verification_status="Vérifié — faible adéquation; présence et recrutement numériques insuffisants",
        notes="Très faible priorité. Ne pas envoyer tant qu’un canal officiel actuel n’est pas identifié.",
        email_body="""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, je souhaite manifester mon intérêt pour un éventuel besoin junior en support, intégration, développement ou automatisation chez Smart World IT.

Mon PFE chez Linedata a porté sur la modernisation d’un produit financier à l’aide d’agents IA. Je maîtrise Python, Java, C++, les APIs, SQL, les bases de données et le développement full-stack.

Je n’ai trouvé ni offre ni canal de recrutement public vérifiable; ce message ne doit être utilisé qu’après confirmation de l’identité de l’entreprise et de la bonne adresse.

Bien cordialement,
Mohamed Oussema Bahloul""",
        linkedin_invitation="Aucun profil personnel fiable identifié — ne pas envoyer d’invitation à un homonyme.",
        linkedin_followup="À utiliser après identification certaine : Bonjour, merci pour la connexion. Je recherche une première opportunité en IT, intégration ou logiciel. Pourriez-vous m’indiquer le canal officiel de candidature de Smart World IT ?",
    ),
]

fieldnames = list(RECORDS[0])
for item in RECORDS[1:]:
    for field in item:
        if field not in fieldnames:
            fieldnames.append(field)

with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(RECORDS)

print(f"Wrote {len(RECORDS)} records to {OUT}")
