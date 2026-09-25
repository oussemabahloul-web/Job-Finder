#!/usr/bin/env python3
"""Fast manual verification of six high-value foreign SMEs, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_21.csv"

def rec(key: str, name: str, sector: str, roles: str, score: str, potential: str,
        reason: str, jobs: str, contact: str, role: str, profile: str,
        email: str, channel: str, sources: str, cv: str = "CV_ATS_EN.pdf",
        junior: str = "Non vérifiable", intl: str = "Non vérifiable",
        evidence: str = "Aucun sponsoring de visa confirmé.") -> dict[str, str]:
    lang = "Français"
    subject = f"Candidature spontanée — Ingénieur junior {roles.split(';')[0]}"
    body = f"""Bonjour {contact if contact not in (name, 'Canal officiel') else ''},

Récemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, je souhaite proposer ma candidature à {name} pour une première opportunité en {roles.lower()}.

Mon PFE chez Linedata portait sur la modernisation d’un produit financier grâce à des agents IA. Il m’a permis de relier IA appliquée, développement logiciel et compréhension métier. Je maîtrise également Python, Java, C++, le développement full-stack, les API, les bases de données, Git et les principes CI/CD.

{reason} Je suis basé en Tunisie et ouvert à une collaboration à distance ou à une mobilité lorsque les conditions le permettent.

Je joins mon CV et serais heureux d’échanger sur un besoin junior actuel ou futur.

Bien cordialement,
Mohamed Oussema Bahloul"""
    invite = f"Bonjour, jeune diplômé ingénieur ENSI, j’ai réalisé chez Linedata un PFE combinant agents IA et logiciel financier. L’activité de {name} correspond fortement à mon projet professionnel. Ravi d’échanger sur vos futurs besoins juniors."
    follow = f"Merci pour la connexion. J’ai transmis ma candidature à {email if '@' in email else 'votre équipe'}. Mon profil combine IA appliquée, développement logiciel et ingénierie financière. Je serais reconnaissant pour toute orientation vers un besoin junior chez {name}."
    return {
        "organization_key": key, "sector": sector, "target_roles": roles,
        "match_score_10": score, "potential_score_100": potential,
        "priority": "Haute" if float(score) >= 8 else "Moyenne",
        "match_reason": reason, "junior_status": junior,
        "junior_evidence": jobs, "foreign_employee_status": intl,
        "foreign_employee_evidence": evidence, "active_jobs": jobs,
        "linkedin_contact_name": contact, "linkedin_contact_role": role,
        "linkedin_profile": profile,
        "contact_verification": "Contact ou canal actuellement rattaché à l’organisation dans les sources citées.",
        "verified_email": email,
        "email_status": "Adresse publiée dans une source officielle/récente" if "@" in email else "Aucun email public vérifié",
        "application_channel": channel, "recommended_cv": cv,
        "language": lang, "email_subject": subject, "email_body": body,
        "linkedin_invitation": invite[:299], "linkedin_followup": follow,
        "sources": sources, "checked_date": "2026-09-25",
        "verification_status": "Vérifié — screening manuel ciblé",
        "notes": "Ne pas présenter une offre ancienne ou expérimentée comme une offre junior active."
    }

RECORDS = [
    rec("aimigo", "Aimigo", "EdTech, adaptive AI, generative AI and language learning",
        "Junior AI Engineer; Python/Full-stack Engineer; Data/ML Engineer", "8.6", "55",
        "Le moteur d’apprentissage adaptatif et le coach génératif correspondent à l’IA appliquée et au développement produit; aucune ouverture technique junior n’a toutefois été confirmée.",
        "Aucune offre technique junior active confirmée; candidature spontanée via la page entreprise.",
        "Aimigo", "Page entreprise et équipe", "https://fr.linkedin.com/company/gymglish-aimigo",
        "Aucun email public vérifié", "https://www.aimigo.coach/",
        "https://fr.linkedin.com/company/gymglish-aimigo | https://www.aimigo.coach/",
        junior="Non vérifiable — équipe internationale, sans offre junior actuelle"),
    rec("mosofty", "Mosofty", "Software engineering, AI, cloud, DevOps and IT consulting",
        "Junior AI/ML Engineer; Full-stack Engineer; Software Engineer", "8.8", "65",
        "L’entreprise recrute sur l’IA, Java/Spring, Angular, Cloud et DevOps et possède une activité à Tunis; l’offre Full-stack IA repérée demande toutefois un profil confirmé résidant en France.",
        "Développeur Full-stack IA confirmé — France — publié en 2026; aucune offre technique junior active exacte confirmée.",
        "Rania Zouaoui", "Contact Mosofty publiant les recrutements", "https://fr.linkedin.com/in/raniazouaoui",
        "rh@mosofty.com", "mailto:rh@mosofty.com",
        "https://www.linkedin.com/company/mosofty/ | https://fr.linkedin.com/in/raniazouaoui | https://fr.linkedin.com/posts/abir-kefi_recrutement-ia-développementfullstack-activity-7425474988352229376-HXuM",
        junior="Oui — stages/PFE et recrutements IT observés, poste actuel ciblé confirmé",
        intl="Partiel — activité à Tunis, mais l’offre France impose la résidence locale",
        evidence="Mosofty a une activité de recrutement en Tunisie; l’annonce France indique explicitement un candidat résidant en France."),
    rec("move2cloud", "Move2Cloud", "Cloud, DevOps, FinOps, AI, cybersecurity and software engineering",
        "Junior Cloud/DevOps Engineer; Junior AI Engineer; Software Engineer", "9.0", "68",
        "Excellent croisement Python, IA, logiciel, CI/CD et cloud; l’entreprise possède aussi une adresse à Tunis. Les 12 CDI actuels demandent néanmoins 3 à 7 ans.",
        "12 offres actives sur le portail, dont Ingénieur IA/ML (+3 ans), Test automatisation (+3 ans), Full-stack (+3 ans); stages 2026 IA/LLM et Cloud publiés récemment.",
        "Move2Cloud FR", "Canal officiel de recrutement", "https://fr.linkedin.com/company/movetocloud",
        "recrutement@move2cloud.fr", "https://move2cloud.fr/carriers",
        "https://move2cloud.fr/carriers | https://fr.linkedin.com/company/movetocloud",
        junior="Oui — stages 2026 et accompagnement junior démontrés; CDI actuels expérimentés",
        intl="Partiel — implantation à Tunis vérifiée; mobilité France non documentée",
        evidence="Le site officiel affiche une adresse à Montplaisir, Tunis. Aucun sponsoring France n’est annoncé."),
    rec("onertech", "ONRTECH", "Web/mobile development, IoT, AI, finance and business intelligence",
        "Junior Software Engineer; AI Engineer; Full-stack Developer", "8.4", "53",
        "Les domaines web, mobile, IA, finance et BI correspondent directement au profil; une collaboration PFE en développement, automatisation et IA est documentée, sans poste salarié actif confirmé.",
        "Aucune offre active confirmée; PFE récent en développement web, automatisation de données et IA.",
        "Marwen R.", "Contact technique ONRTECH", "https://fr.linkedin.com/in/marwen-r-7212b912",
        "Aucun email public vérifié", "https://onrtech.fr/",
        "https://www.linkedin.com/company/onrtech | https://tn.linkedin.com/in/eya-aouichi-658096267 | https://onrtech.fr/",
        junior="Oui — accueil PFE documenté; premier CDI non vérifiable"),
    rec("yonnov ia", "Yonnov’IA", "AI solutions, AI-powered ERP, automation and decision support",
        "Junior AI Engineer; Python/ERP Developer; Data/ML Engineer", "9.0", "63",
        "La startup conçoit des solutions IA intégrées aux outils métiers et des modules ERP prédictifs; elle emploie plusieurs profils tunisiens, mais aucune offre technique actuelle n’est visible.",
        "Aucune offre technique active; ancien stage marketing pré-embauche publié pour janvier 2026.",
        "Mohamed Arafet Khadraoui", "Membre actuel de Yonnov’IA", "https://fr.linkedin.com/in/khadraouiarafet",
        "contact@yonnovia.fr", "mailto:contact@yonnovia.fr",
        "https://www.linkedin.com/company/yonnovia.fr | https://fr.linkedin.com/in/khadraouiarafet | https://www.yonnovia.fr/",
        junior="Oui — stage pré-embauche antérieur et équipe jeune; aucune offre technique actuelle",
        intl="Partiel — plusieurs collaborateurs tunisiens visibles; statut contractuel/visa non vérifiable",
        evidence="La page LinkedIn liste plusieurs collaborateurs basés en Tunisie, sans préciser leur contrat ni une politique de mobilité."),
    rec("crab traceability systems", "CRAB Traceability Systems", "Computer vision, edge AI, hardware and circular-economy software",
        "Junior AI/Computer Vision Engineer; Python Engineer; Systems Engineer", "9.1", "72",
        "Très forte adéquation IA/vision/logiciel et petite équipe en croissance. Le site montre trois stagiaires et accepte explicitement les candidatures spontanées.",
        "Senior Hardware Engineer affiché; aucune offre junior exacte, mais candidatures spontanées explicitement acceptées.",
        "Dr. Jeff Mangers", "CEO & Co-founder", "https://www.linkedin.com/in/jeff-mangers/",
        "info@crab-ts.com", "mailto:info@crab-ts.com",
        "https://crab-ts.com/landing/about | https://www.linkedin.com/company/crab-traceability-systems | https://www.uni.lu/en/news/crab-circular-economy-ai-startup-track-waste/",
        junior="Oui — trois stagiaires figurent dans l’équipe officielle",
        intl="Partiel — équipe internationale visible, sponsoring non documenté",
        evidence="L’équipe officielle est internationale et accueille des stagiaires; aucun visa ou dispositif de relocation n’est publié.")
]

OUT.parent.mkdir(parents=True, exist_ok=True)
fields = sorted({k for row in RECORDS for k in row})
with OUT.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
