#!/usr/bin/env python3
"""Verification of four foreign software SMEs, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path
OUT=Path(__file__).resolve().parent/"verified_batches"/"batch_2026_09_25_23.csv"

def r(key,name,sector,roles,score,potential,reason,junior,jobs,contact,role,profile,email,channel,sources,intl="Non vérifiable"):
    body=f"""Bonjour,

Récemment diplômé ingénieur en informatique de l’ENSI, spécialisé en ingénierie financière, je souhaite proposer ma candidature à {name} pour une première opportunité en {roles.lower()}.

Mon PFE chez Linedata portait sur la modernisation d’un produit financier à l’aide d’agents IA. Je maîtrise Python, Java, C++, le développement full-stack, les API, les bases de données, le machine learning, Git et les principes CI/CD.

{reason} Basé en Tunisie, je suis ouvert au télétravail ou à une mobilité réalisable.

Je serais ravi d’échanger et joins mon CV à cette candidature.

Bien cordialement,
Mohamed Oussema Bahloul"""
    return {"organization_key":key,"sector":sector,"target_roles":roles,"match_score_10":score,"potential_score_100":potential,"priority":"Haute" if float(score)>=8 else "Moyenne","match_reason":reason,"junior_status":junior,"junior_evidence":jobs,"active_jobs":jobs,"foreign_employee_status":intl,"foreign_employee_evidence":"Aucun visa sponsorisé confirmé; la présence ou collaboration tunisienne est indiquée lorsqu’elle est sourcée.","linkedin_contact_name":contact,"linkedin_contact_role":role,"linkedin_profile":profile,"contact_verification":"Rattachement actuel ou publication récente vérifié dans les sources.","verified_email":email,"email_status":"Adresse de recrutement/contact publiée" if "@" in email else "Aucun email public vérifié","application_channel":channel,"recommended_cv":"CV_ATS_EN.pdf","language":"Français","email_subject":f"Candidature — {roles.split(';')[0]} junior","email_body":body,"linkedin_invitation":(f"Bonjour, diplômé ingénieur ENSI, mon PFE Linedata combinait agents IA et logiciel financier. {name} correspond à mes compétences en Python, Data/IA et développement. Ravi d’échanger sur vos besoins juniors.")[:299],"linkedin_followup":f"Merci pour la connexion. Je viens de proposer mon profil junior à {name}. Pourriez-vous m’orienter vers la personne qui suit les besoins Data, IA ou développement logiciel ?","sources":sources,"checked_date":"2026-09-25","verification_status":"Vérifié — screening manuel ciblé","notes":"Vérifier de nouveau la disponibilité de la mission au moment de l’envoi."}

RECORDS=[
 r("agiir network","AGIIR Network","IT services, managed infrastructure, software maintenance, Big Data and cloud","Junior Data Engineer; Python Engineer; Software Engineer","8.1","67","La mission Data actuelle utilise Python, Pandas, PySpark, SQL, Kafka, cloud et CI/CD. Elle demande toutefois une forte autonomie et vise un freelance en France.","Oui — un diplômé ENSI récent travaille dans l’entreprise et une développeuse récemment diplômée y est présente","Consultant freelance Data Engineer Big Data — publication récente — hybride France — niveau solide/autonome requis","Yassine Boujebha","Software Engineer AGIIR et ancien ENSI","https://fr.linkedin.com/in/yassine-boujebha-44a742205","g.felix@agiir.com","mailto:g.felix@agiir.com","https://www.linkedin.com/company/agiir-network | https://agiir-network.com/ | https://fr.linkedin.com/in/yassine-boujebha-44a742205",intl="Partiel — recrutement de profils tunisiens observé; mission actuelle localisée en France"),
 r("azertyui","AzertyUI","Software development, web/mobile, cloud, AI agents, automation and cybersecurity","Junior AI/Automation Engineer; Full-stack Developer; Mobile Developer","8.7","66","Les agents IA, workflows n8n, web/mobile et cloud recoupent précisément le profil; l’entreprise collabore publiquement avec un ingénieur mobile basé en Tunisie.","Oui/partiel — collaboration avec un ingénieur tunisien vérifiée; anciennes offres techniques visibles","Aucune offre technique active récente confirmée; ancienne offre Web Architect et offre commerciale, candidature spontanée conseillée.","Ghaith Mefteh","Mobile Engineer chez AzertyUI, basé en Tunisie","https://tn.linkedin.com/in/ghaith-mefteh-995a18157","sales@azertyui.fr","mailto:sales@azertyui.fr","https://fr.linkedin.com/company/azertyui-software | https://azertyui.fr/ | https://pe.linkedin.com/posts/azertyui-software_delighted-to-have-met-ghaith-mefteh-at-the-activity-7285203822774222848-UotI",intl="Oui/partiel — collaboration France-Tunisie documentée, sans politique de visa publiée"),
 r("autris","AUTRIS","Automation, intelligent systems, robotics and AI","Junior AI/Automation Engineer; Robotics Software Engineer; Python/C++ Developer","8.0","45","L’automatisation, les systèmes intelligents et la robotique correspondent à Python/C++ et l’IA, mais aucune offre, page carrières ou procédure internationale n’est publiée.","Non vérifiable","Aucune offre active confirmée; candidature spontanée LinkedIn uniquement.","Celine Gilbert","Membre actuelle AUTRIS — Automation & Intelligent Systems","https://fr.linkedin.com/in/celine-gilbert-412838310","Aucun email public vérifié","https://fr.linkedin.com/in/celine-gilbert-412838310","https://fr.linkedin.com/in/celine-gilbert-412838310"),
 r("azertysoft","AzertySoft","IT services and software consulting","Junior Software Engineer; Full-stack Developer","6.5","34","Le secteur logiciel est pertinent, mais la page ne présente ni activités détaillées, ni emplois, ni canal de recrutement fiable.","Non vérifiable","Aucune offre active confirmée; présence publique limitée à une petite page LinkedIn.","Walid Aloui","Membre affiché de l’équipe","https://www.linkedin.com/in/walid-aloui/","Aucun email public vérifié","https://www.linkedin.com/company/azertysoft","https://www.linkedin.com/company/azertysoft")
]
OUT.parent.mkdir(parents=True,exist_ok=True)
fields=sorted({k for x in RECORDS for k in x})
with OUT.open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
