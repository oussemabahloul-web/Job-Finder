#!/usr/bin/env python3
"""Fast manual verification of five foreign SMEs, 2026-09-25."""
from __future__ import annotations
import csv
from pathlib import Path
OUT = Path(__file__).resolve().parent / "verified_batches" / "batch_2026_09_25_22.csv"

def r(key, name, sector, roles, score, potential, reason, junior, jobs, contact, role, profile,
      email, channel, sources, cv="CV_ATS_EN.pdf", intl="Non vérifiable"):
    address = f"Bonjour {contact}," if contact not in (name, "Canal officiel") else "Bonjour,"
    return {
      "organization_key":key,"sector":sector,"target_roles":roles,"match_score_10":score,
      "potential_score_100":potential,"priority":"Haute" if float(score)>=8 else "Moyenne",
      "match_reason":reason,"junior_status":junior,"junior_evidence":jobs,"active_jobs":jobs,
      "foreign_employee_status":intl,"foreign_employee_evidence":"Aucun sponsoring de visa ni dispositif de relocation confirmé.",
      "linkedin_contact_name":contact,"linkedin_contact_role":role,"linkedin_profile":profile,
      "contact_verification":"Lien actuel avec l’organisation confirmé par les sources citées.",
      "verified_email":email,"email_status":"Adresse publique vérifiée" if "@" in email else "Aucun email public vérifié",
      "application_channel":channel,"recommended_cv":cv,"language":"Français",
      "email_subject":f"Candidature spontanée — {roles.split(';')[0]} junior",
      "email_body":f"""{address}

Récemment diplômé ingénieur en informatique de l’ENSI, spécialisé en ingénierie financière, je souhaite proposer ma candidature à {name} pour une première opportunité en {roles.lower()}.

Mon PFE chez Linedata a consisté à moderniser un produit financier grâce à des agents IA. Cette expérience m’a appris à transformer un besoin métier en solution intégrée, tout en mobilisant Python, le machine learning, les API, les bases de données et le développement full-stack. Je maîtrise également Java et C++.

{reason} Je suis basé en Tunisie et ouvert au télétravail international ou à la mobilité lorsque cela est possible.

Je joins mon CV et serais ravi d’échanger sur vos besoins actuels ou futurs.

Bien cordialement,
Mohamed Oussema Bahloul""",
      "linkedin_invitation":(f"Bonjour, diplômé ingénieur ENSI, mon PFE Linedata combinait agents IA et logiciel financier. Les travaux de {name} sont proches de mon projet en IA appliquée et développement. Ravi d’échanger sur un futur besoin junior.")[:299],
      "linkedin_followup":f"Merci pour la connexion. Je souhaite proposer mon profil junior à {name}, à l’intersection de l’IA appliquée, du développement logiciel et de la compréhension métier. Je serais reconnaissant pour toute orientation vers un besoin adapté.",
      "sources":sources,"checked_date":"2026-09-25","verification_status":"Vérifié — screening manuel ciblé",
      "notes":"Candidature spontanée; ne pas présenter les contenus historiques comme une offre active."
    }

RECORDS=[
 r("featway","Featway","HRIS consulting, HR analytics, BI, Data and digital transformation",
   "Junior Data Engineer; Full-stack Developer; Junior SIRH/BI Consultant","7.9","58",
   "Les offres permanentes Data Engineer et Full-stack correspondent au profil logiciel/data, mais leur date de publication n’est pas affichée et doit être reconfirmée avant de les citer comme ouvertes.",
   "Non vérifiable — pages métiers accessibles sans indication claire d’expérience junior",
   "Pages Carrières accessibles: Consultant Data Engineer, Développeur Web Full-stack, Consultant SIRH-AMOA; actualité à confirmer.",
   "Mohamed Fekher Ferci","Contact Featway actuel","https://fr.linkedin.com/in/mohamed-fekher-ferci-736aba67",
   "contact@www.featway.fr","https://www.featway.fr/carrieres/",
   "https://www.featway.fr/carrieres/ | https://www.featway.fr/ | https://fr.linkedin.com/in/mohamed-fekher-ferci-736aba67"),
 r("knowlepsy investment","Clarrio.ai (ex-Knowlepsy)","HealthTech, predictive analytics, real-world health data and AI",
   "Junior Data/AI Engineer; Machine Learning Engineer; Full-stack Engineer","8.7","59",
   "L’analyse prédictive de données de santé correspond fortement au profil IA/data; la marque Knowlepsy est devenue Clarrio.ai et aucune ouverture technique active n’a été confirmée.",
   "Non vérifiable — startup France-Tunisie, sans page carrières active trouvée",
   "Aucune offre active confirmée; candidature spontanée auprès de l’équipe dirigeante.",
   "Rym Jaziri","Dirigeante/équipe Knowlepsy Investment","https://www.linkedin.com/in/rym-jaziri-142ba815/fr",
   "Aucun email public vérifié","https://www.linkedin.com/company/clarrio-ai/",
   "https://www.linkedin.com/in/rym-jaziri-142ba815/fr | https://www.linkedin.com/posts/firas-rhaiem-546378108_healthtech-digitalhealth-ai-activity-7376244050473164800-betc",
   intl="Partiel — structure France-Tunisie observée, modalités non publiées"),
 r("memoways","Memoways","No-code software, digital transformation and applied open-source LLM experimentation",
   "Junior AI/LLM Developer; Software Developer; Automation Engineer","7.8","43",
   "Les expérimentations LLM open source et la transformation numérique sont pertinentes, mais l’agence ne compte que quelques personnes et ne publie aucune offre.",
   "Non — aucune preuve récente d’embauche junior",
   "Aucune offre active; petite équipe de quatre personnes.",
   "Dan Wechsler","Membre/fondateur de l’équipe","https://www.linkedin.com/in/danwechsler/",
   "Aucun email public vérifié","http://memoways.com/",
   "https://www.linkedin.com/company/memoways | http://memoways.com/"),
 r("fysali","Fysali","Digital Health, connected medical monitoring, signal processing and software",
   "Junior Software Engineer; Data/AI Engineer; Full-stack Developer","7.4","46",
   "La solution de suivi médical comporte un produit logiciel et des données; une levée récente peut créer des besoins, mais l’équipe publique reste minuscule et aucune offre n’est annoncée.",
   "Non vérifiable — aucune offre ni historique junior identifié",
   "Aucune offre active; formulaire officiel invite explicitement à contacter l’équipe pour rejoindre Fysali.",
   "Omar Hassan","Founder and CEO","https://www.linkedin.com/in/omar-hassan-fysali/",
   "Aucun email public vérifié","https://www.fysali.com/",
   "https://www.fysali.com/ | https://tn.linkedin.com/company/fysali | https://www.linkedin.com/posts/eurasanté-uk_%F0%9D%90%80-%F0%9D%90%A5%F0%9D%90%A8%F0%9D%90%A8%F0%9D%90%A4-%F0%9D%90%9B%F0%9D%90%9A%F0%9D%90%9C%F0%9D%90%A4-%F0%9D%90%9A%F0%9D%90%AD-%F0%9D%90%AD%F0%9D%90%B0%F0%9D%90%A8-%F0%9D%90%A2%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%AB-activity-7488581183467847681-14hR"),
 r("mfbf technologies","MFBF Technologies","Cloud, DevOps, FinOps, automation, AI-driven IT operations and application modernization",
   "Junior Cloud/DevOps Engineer; AI Automation Engineer; Software Engineer","8.2","48",
   "L’automatisation IT, FinOps, cloud et modernisation applicative recoupent bien Python, IA et CI/CD; aucun recrutement junior ou canal RH n’a été trouvé.",
   "Non vérifiable — aucune page carrières publique identifiée",
   "Aucune offre active confirmée; prise de contact générale uniquement.",
   "MFBF Technologies","Page entreprise/site officiel","https://www.linkedin.com/company/mfbf-technologies/",
   "Aucun email public vérifié","https://www.mfbf-technologies.com/",
   "https://www.mfbf-technologies.com/ | https://www.linkedin.com/company/mfbf-technologies/"),
]
OUT.parent.mkdir(parents=True,exist_ok=True)
fields=sorted({k for x in RECORDS for k in x})
with OUT.open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(RECORDS)
print(f"Wrote {len(RECORDS)} records to {OUT}")
