#!/usr/bin/env python3
"""Build the consolidated job-research dataset and Markdown report.

The script deliberately separates source-derived facts from externally verified
facts.  Research gathered later is stored in ``verified_research.csv`` and is
merged when this generator is rerun.  Missing information is rendered as
``Non trouvé/non vérifiable`` rather than guessed.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_CANDIDATES = (
    ROOT / "latest with errors 1" / "Export.csv",
    ROOT / "Export.csv",
)
OUTPUT_CSV = ROOT / "job_research" / "company_research.csv"
OUTPUT_MD = ROOT / "job_research" / "README.md"
FOREIGN_DIR = ROOT / "job_research" / "foreign_companies"
FOREIGN_OUTPUT_CSV = FOREIGN_DIR / "company_research.csv"
FOREIGN_OUTPUT_MD = FOREIGN_DIR / "README.md"
OVERRIDES_CSV = ROOT / "job_research" / "verified_research.csv"
OVERRIDE_BATCH_DIR = ROOT / "job_research" / "verified_batches"
LOCATION_OVERRIDES_CSV = ROOT / "job_research" / "location_research.csv"
TODAY = date.today().isoformat()

MISSING = "Non trouvé/non vérifiable"
NO_EMAIL = "Aucun email public vérifié"


def ascii_norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.encode("ascii", "ignore").decode("ascii").casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def organization_key(value: str) -> str:
    """Normalize spelling without collapsing legally distinct local entities."""
    key = ascii_norm(value)
    key = re.sub(r"\b(sarl|sa|sas|sasu|ltd|limited|inc|corp|corporation)\b", " ", key)
    key = re.sub(r"\s+", " ", key).strip()
    # High-confidence aliases observed in Export.csv.  They consolidate spelling,
    # language and regional-office variants, not merely similar-looking names.
    alias_rules = [
        (r"^sofrecom(?: tunisie| tunisia| sfax)?$", "sofrecom tunisie"),
        (r"^(?:tunisie|tunisise|tunsie) telecom(?:\b.*)?$", "tunisie telecom"),
        (r"^talan(?: tunisie(?: consulting)?)?$", "talan tunisie"),
        (r"^talan (?:consulting tunisie|tunisie international)$", "talan tunisie"),
        (r"^laboratoire de recherche riadi talan innovation factory$", "talan tunisie"),
        (r"^linedata(?:\b.*)?$", "linedata"),
        (r"^(?:m c|mnc)(?: it consulting| aero)?$", "mnc aero"),
        (r"^vermeg(?: factory)?$", "vermeg"),
        (r"^pwc(?: tunisie| services maghreb| risk services maghreb| technology acceleration center)?$", "pwc tunisie"),
        (r"^(?:centre d audit et formation |conseil audit formation internationale membre du reseau )pwc$", "pwc tunisie"),
        (r"^telnet(?: holding| incorporated)?$", "telnet"),
        (r"^altran telnet(?: corporation)?(?: atc)?(?: capgemini(?: engineering)?)?$", "altran telnet capgemini engineering"),
        (r"^(?:athena technology services(?: ats)?|athena thechnology services(?: ats)?|ats digital dev)$", "athena technology services ats"),
        (r"^business (?:and|&) decision(?: tunisie)?$", "business and decision tunisie"),
        (r"^orange tunisie(?: siege social)?$", "orange tunisie"),
        (r"^sagemcom(?: software (?:and|technologies|and technologies).*)?$", "sagemcom"),
        (r"^st ?microelectronics(?: tunis| tunisia)?$", "stmicroelectronics"),
        (r"^axe ?finance$", "axe finance"),
        (r"^bh bank(?: le siege social)?$", "bh bank"),
        (r"^arab ?soft$", "arabsoft"),
        (r"^(?:siege de la )?societe tunisienne de bank$", "stb"),
        (r"^focus(?: corporation)?(?: tunisie)?$", "focus"),
        (r"^focus technology solutions$", "focus"),
        (r"^mbh data works$", "tanitlab"),
        (r"^cognira(?: tunisia)?$", "cognira"),
        (r"^keyrus(?: group)?$", "keyrus"),
        (r"^equinoxes$", "keyrus"),
        (r"^oddo bhf(?: tunis)?$", "oddo bhf"),
        (r"^(?:la )?banque centrale de tunisie(?: bct)?$", "banque centrale de tunisie"),
        (r"^societe tunisienne des? banques?$", "stb"),
        (r"^(?:biat tunisie|banque internationale arabe de tunisie)$", "biat"),
        (r"^inetum(?: tunisie)?$", "inetum"),
        (r"^rhis (?:software|solutions)$", "rhis solutions"),
        (r"^yonnov ia(?: sas)?$", "yonnov ia"),
        (r"^binit(?: nearshore service|ns)$", "binit nearshore service"),
        (r"^centre national (?:de l |d )informatique$", "centre national informatique"),
        (r"^orange(?: tunisie)?$", "orange tunisie"),
        (r"^(?:3s )?standard sharing software(?: 3s)?$", "standard sharing software"),
        (r"^deepshift (?:ai|ia)$", "deepshift ai"),
        (r"^(?:mp soft|manager partner software|mp soft manager partner software)$", "manager partner software"),
        (r"^(?:top|t o p)(?: team opportunity prediction)?$", "team opportunity prediction"),
        (r"^(?:faurecia|forvia) informatique tunisie$", "forvia informatique tunisie"),
        (r"^laboratoire d informatique signal et image de la cote d opp?ale universite littorale de la cote d opp?ale$", "lisic ulco"),
        (r"^laboratoire (?:de recherche laria|lara de l ensi)$", "laboratoire laria ensi"),
        (r"^(?:societe )?leoni$", "leoni tunisie"),
        (r"^s ?w ?consulting$", "sw consulting"),
        (r"^actia (?:engineering services(?: siege social)?|es)$", "actia engineering services"),
        (r"^(?:siemens(?: di software| industry software| eda(?: tunisia)?| mentor graphics(?: tunisia)?)|mentor graphics siemens business)$", "siemens"),
        (r"^coding ?factory$", "coding factory"),
        (r"^eura ?nova$", "euranova"),
        (r"^we ?settle$", "wesettle"),
        (r"^yonnov ia(?: sas)?$", "yonnov ia"),
        (r"^national smart for green solutions? and applications?$", "national smart for green solutions and applications"),
        (r"^value digital services?$", "value digital services"),
        (r"^integration objects?$", "integration objects"),
        (r"^whitecape technolo(?:gies|ies)$", "whitecape technologies"),
        (r"^coding betounsi$", "coding betounsi"),
        (r"^(?:bna )?banque nationale agricole$", "banque nationale agricole"),
        (r"^(?:atb )?arab tunisian bank(?: atb)?$", "arab tunisian bank"),
        (r"^societe tunisienne de l electricite et du gaz(?: steg)?$", "steg"),
        (r"^groupe chimique tunisien(?: gct| sfax)?$", "groupe chimique tunisien"),
        (r"^centre informatique du ministere de la sante(?: cims)?$", "centre informatique du ministere de la sante"),
    ]
    for pattern, canonical in alias_rules:
        if re.fullmatch(pattern, key):
            return canonical
    return key


FOREIGN_TERMS = {
    "France": ["france", "paris", "lyon", "marseille", "toulouse", "nantes", "lille", "metz", "reims", "limoges", "blagnac", "gif sur yvette", "boulogne billancourt", "bezons", "auzeville", "rouen", "grenoble", "bordeaux", "montpellier", "strasbourg", "nice", "sophia antipolis"],
    "Canada": ["canada", "quebec", "montreal", "ontario", "toronto", "hamilton on", "nova scotia", "wolfville", "ottawa", "vancouver", "rouyn noranda"],
    "États-Unis": ["usa", "united states", "etats unis", "california", "new york", "massachusetts", "washington", "florida", "fort lauderdale", "sioux falls", " san francisco", "boston", "chicago", "texas"],
    "Allemagne": ["germany", "allemagne", "munich", "berlin", "hamburg", "frankfurt", "geesthacht"],
    "Belgique": ["belgium", "belgique", "brussels", "bruxelles"],
    "Royaume-Uni": ["united kingdom", "royaume uni", " uk", "london", "edinburgh", "england", "scotland"],
    "Suisse": ["switzerland", "suisse", "geneva", "geneve", "lausanne", "zurich"],
    "Pays-Bas": ["netherlands", "pays bas", " holland", "amsterdam", "rotterdam", "winterswijk", " nl"],
    "Luxembourg": ["luxembourg", "esch sur alzette"],
    "Maroc": ["morocco", "maroc", "casablanca", "rabat"],
    "Algérie": ["algeria", "algerie", "algiers", "alger"],
    "Égypte": ["egypt", "egypte", "cairo", "le caire"],
    "Émirats arabes unis": ["uae", "emirates", "dubai", "abu dhabi"],
    "Arabie saoudite": ["saudi arabia", "arabie saoudite", "riyadh", "jeddah"],
    "Espagne": ["spain", "espagne", "madrid", "barcelona"],
    "Italie": ["italy", "italie", "milan", "rome"],
    "Portugal": ["portugal", "lisbon", "lisbonne"],
    "Pologne": ["poland", "pologne", "warsaw", "varsovie"],
    "Roumanie": ["romania", "roumanie", "bucharest", "bucarest"],
    "Hongrie": ["hungary", "hongrie", "budapest"],
    "Lettonie": ["latvia", "lettonie", "riga"],
    "Qatar": ["qatar", "doha"],
    "Turquie": ["turkey", "turquie", "istanbul"],
    "Sénégal": ["senegal", "dakar"],
    "Côte d’Ivoire": ["cote d ivoire", "abidjan"],
    "Maurice": ["mauritius", "ile maurice"],
    "Mauritanie": ["mauritania", "mauritanie", "nouakchott"],
    "Burkina Faso": ["burkina faso", "ouagadougou"],
    "Australie": ["australia", "australie", "sydney", "melbourne", "nsw"],
    "Autriche": ["austria", "autriche", "vienna", "vienne"],
    "Irlande": ["ireland", "irlande", "dublin"],
    "Suède": ["sweden", "suede", "stockholm"],
    "Norvège": ["norway", "norvege", "oslo"],
    "Danemark": ["denmark", "danemark", "copenhagen"],
    "Finlande": ["finland", "finlande", "helsinki"],
    "Tchéquie": ["czech", "tcheque", "prague"],
    "Slovaquie": ["slovakia", "slovaquie", "bratislava"],
    "Brésil": ["brazil", "bresil", "sao paulo"],
    "Mexique": ["mexico", "mexique"],
    "Inde": ["india", "inde", "bangalore", "bengaluru", "hyderabad"],
    "Chine": ["china", "chine", "beijing", "shanghai"],
    "Japon": ["japan", "japon", "tokyo"],
}

FOREIGN_COUNTRY_TERMS = {
    "France": ["france"], "Canada": ["canada"],
    "États-Unis": ["usa", "united states", "etats unis"],
    "Allemagne": ["germany", "allemagne"], "Belgique": ["belgium", "belgique"],
    "Royaume-Uni": ["united kingdom", "royaume uni"], "Suisse": ["switzerland", "suisse"],
    "Pays-Bas": ["netherlands", "pays bas"], "Luxembourg": ["luxembourg"],
    "Maroc": ["morocco", "maroc"], "Algérie": ["algeria", "algerie"],
    "Égypte": ["egypt", "egypte"], "Émirats arabes unis": ["uae", "emirates"],
    "Arabie saoudite": ["saudi arabia", "arabie saoudite"],
    "Espagne": ["spain", "espagne"], "Italie": ["italy", "italie"],
    "Portugal": ["portugal"], "Pologne": ["poland", "pologne"],
    "Roumanie": ["romania", "roumanie"], "Hongrie": ["hungary", "hongrie"],
    "Lettonie": ["latvia", "lettonie"], "Qatar": ["qatar"],
    "Turquie": ["turkey", "turquie"], "Sénégal": ["senegal"],
    "Côte d’Ivoire": ["cote d ivoire"], "Maurice": ["mauritius", "ile maurice"],
    "Mauritanie": ["mauritania", "mauritanie"], "Burkina Faso": ["burkina faso"],
    "Australie": ["australia", "australie"], "Autriche": ["austria", "autriche"],
    "Irlande": ["ireland", "irlande"], "Suède": ["sweden", "suede"],
    "Norvège": ["norway", "norvege"], "Danemark": ["denmark", "danemark"],
    "Finlande": ["finland", "finlande"], "Tchéquie": ["czech", "tcheque"],
    "Slovaquie": ["slovakia", "slovaquie"], "Brésil": ["brazil", "bresil"],
    "Mexique": ["mexico", "mexique"], "Inde": ["india", "inde"],
    "Chine": ["china", "chine"], "Japon": ["japan", "japon"],
}

TUNIS_TERMS = [
    "tunis", "lac 1", "lac1", "lac 2", "lac2", "berges du lac", "charguia",
    "charquia", "centre urbain", "montplaisir", "monplaisir", "belvedere",
    "le bardo", "bardo", "la marsa", "marsa", "carthage", "sidi bou said",
    "le kram", "la goulette", "mutuelleville", "el menzah", "menzah", "manar",
    "cite el khadra", "jeanne d arc", "bab bhar", "bab souika", "el omrane",
]

ARIANA_TERMS = [
    "ariana", "ennasr", "en nasr", "el ghazala", "elghazala", "ghazela",
    "ghazala", "raoued", "soukra", "la soukra", "mnihla", "borj louzir",
    "chotrana", "technopole el ghazala", "technopole elghazala",
]

OTHER_TUNISIA_TERMS = [
    "sfax", "sousse", "monastir", "nabeul", "bizerte", "ben arous", "manouba",
    "kairouan", "gabes", "gafsa", "medenine", "mahdia", "beja", "jendouba",
    "kef", "siliana", "zaghouan", "tozeur", "kasserine", "tataouine", "djerba",
    "hammamet", "mornag", "megrine", "rades", "ezzahra", "mourouj", "korba",
    "ben gardane", "zriba", "enfidha", "teboulba", "soliman", "grombalia",
    "dar chaabane", "kelibia", "msaken", "kebili", "zarzis", "moknine",
    "ghannouch", "agba", "borj cedria", "jedaida", "nouvelle medina",
]


def contains_term(text: str, term: str) -> bool:
    return bool(re.search(r"(?:^|\s)" + re.escape(term) + r"(?:$|\s)", text))


def classify_address(address: str) -> tuple[str, str, bool, str]:
    text = " " + ascii_norm(address) + " "
    # An explicit Tunis/Ariana locality takes precedence over country names
    # embedded in Tunisian street names (Rue de l'Égypte, Avenue de France,
    # Avenue de Madrid, etc.).
    if any(contains_term(text, term) for term in TUNIS_TERMS):
        return "Tunis", "Tunisie", True, "Adresse CSV dans le gouvernorat de Tunis"
    if any(contains_term(text, term) for term in ARIANA_TERMS):
        return "Ariana", "Tunisie", True, "Adresse CSV dans le gouvernorat de l’Ariana"
    for country, terms in FOREIGN_COUNTRY_TERMS.items():
        if any(contains_term(text, term.strip()) for term in terms):
            return "Étranger", country, True, "Adresse CSV située à l’étranger"
    if any(contains_term(text, term) for term in OTHER_TUNISIA_TERMS):
        return "Exclue — autre ville tunisienne", "Tunisie", False, "Adresse CSV hors Tunis et Ariana"

    # Foreign city and postal patterns are considered only after Tunisian
    # locations, preventing false positives caused by local street names.
    for country, terms in FOREIGN_TERMS.items():
        if any(contains_term(text, term.strip()) for term in terms):
            return "Étranger", country, True, "Adresse CSV située à l’étranger"
    if re.search(r"\b(?:75|69|13|31|44|59|33|67|06|92|93|94|95|91|57|87|65|26)\d{3}\b", text):
        return "Étranger", "France", True, "Code postal français dans l’adresse CSV"
    if re.search(r"\b[a-z]\d[a-z]\s?\d[a-z]\d\b", text):
        return "Étranger", "Canada", True, "Code postal canadien dans l’adresse CSV"
    if re.search(r"\b(?:fl|sd|ca|ny|ma|tx|wa|il)\s+\d{5}\b", text):
        return "Étranger", "États-Unis", True, "État et code postal américains dans l’adresse CSV"
    return "Localisation non vérifiable", MISSING, False, "Adresse CSV insuffisante ou ambiguë"


SECTOR_RULES = [
    ("Finance / Banque / FinTech", ["bank", "banque", "finance", "financial", "fintech", "capital", "leasing", "assurance", "insurance", "payment", "paiement", "bourse", "microfinance", "bnp", "biat", "ubci", "uib", "attijari", "zitouna", "wifak", "vermeg", "linedata", "axe finance", "vneuron", "fis"]),
    ("IA / Data / Logiciel", ["artificial intelligence", "intelligence artificielle", " ai ", "data", "analytics", "software", "logiciel", "digital", "informatique", "information technology", " it ", "cloud", "cyber", "robot", "computer", "telnet", "talan", "sofrecom", "keyrus", "wevioo", "focus corporation", "cognira", "elyadata"]),
    ("Télécom / Électronique / Industrie", ["telecom", "telecommunication", "electron", "engineering", "industrie", "industrial", "automotive", "aeronaut", "energy", "energie", "sagemcom", "actia", "siemens"]),
    ("Recherche / Enseignement", ["universite", "university", "laboratoire", "laboratory", "research", "recherche", "ecole", "institut", "faculty", "faculte", "ensi", "enit"]),
    ("Santé", ["hospital", "hopital", "clinic", "clinique", "medical", "medic", "pharma", "sante"]),
    ("Secteur public / Institution", ["ministere", "ministry", "office national", "municipalite", "centrale", "steg", "etap", "cnss", "caisse nationale"]),
]


def infer_sector(name: str, emails: list[str], addresses: list[str]) -> str:
    # Addresses describe geography, not activity: street names such as
    # "Avenue de la Bourse" must not classify an IT company as financial.
    haystack = " " + ascii_norm(" ".join([name, *emails])) + " "
    for sector, terms in SECTOR_RULES:
        # Match complete tokens/phrases. Substring matching incorrectly turned
        # "Avenue Habib Bourguiba" into UIB and "Ibn Al Nafis" into FIS.
        if any(contains_term(haystack, ascii_norm(term).strip()) for term in terms):
            return sector
    return "Autre / à vérifier"


def initial_match(sector: str) -> tuple[float, str, str]:
    mapping = {
        "Finance / Banque / FinTech": (9.0, "IA, Data, développement logiciel, Business Analysis, audit IT ou transformation digitale", "Très forte correspondance avec l’ingénierie informatique et financière"),
        "IA / Data / Logiciel": (8.5, "AI Engineer, Data/ML Engineer, développeur logiciel, full-stack ou Business Analyst technique", "Forte correspondance avec Python, Java, C++, IA, RAG et développement full-stack"),
        "Télécom / Électronique / Industrie": (7.0, "développement logiciel, IA/Data, automatisation, systèmes ou transformation digitale", "Correspondance technique réelle, à confirmer selon les besoins logiciels"),
        "Recherche / Enseignement": (7.5, "ingénieur IA/Data, ingénieur de recherche, développeur ou assistant de recherche", "Bon alignement avec les projets IA et le parcours ENSI"),
        "Santé": (5.5, "IA/Data appliquée, développement de solutions numériques ou systèmes d’information", "Correspondance indirecte via la transformation numérique"),
        "Secteur public / Institution": (5.5, "ingénieur informatique, Data/IA, audit IT ou systèmes d’information", "Correspondance possible selon les concours et projets numériques"),
        "Autre / à vérifier": (4.0, "informatique, automatisation, Data/IA ou transformation digitale", "Activité insuffisamment précise dans le fichier source"),
    }
    return mapping[sector]


def valid_email(value: str) -> bool:
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", (value or "").strip()))


def cv_for(sector: str, location: str, country: str) -> tuple[str, str]:
    fintech = sector == "Finance / Banque / FinTech"
    francophone = location != "Étranger" or country in {
        "France", "Belgique", "Luxembourg", "Suisse", "Canada", "Maroc",
        "Algérie", "Sénégal", "Côte d’Ivoire", "Mauritanie",
    }
    if fintech:
        return ("CV_ATS_Fintech.pdf" if francophone else "CV_ATS_Fintech_EN.pdf", "fr" if francophone else "en")
    return ("CV_ATS.pdf" if francophone else "CV_ATS_EN.pdf", "fr" if francophone else "en")


def priority(score: int) -> str:
    if score >= 75:
        return "A — Très prioritaire"
    if score >= 55:
        return "B — Prioritaire"
    if score >= 35:
        return "C — À tenter"
    return "D — Faible priorité"


def templates(name: str, sector: str, roles: str, language: str, foreign: bool) -> dict[str, str]:
    fintech = sector == "Finance / Banque / FinTech"
    if language == "fr":
        subject = f"Candidature junior – IA, Data et développement logiciel – Mohamed Oussema Bahloul"
        if fintech:
            opening = f"Je souhaite proposer ma candidature à {name} pour une première opportunité en IA, Data, développement logiciel, Business Analysis ou transformation digitale appliquée aux services financiers."
            experience = "Lors de mon PFE chez Linedata, j’ai contribué à moderniser un produit financier en concevant une solution fondée sur trois agents IA, une architecture RAG et 24 outils d’intégration."
        else:
            opening = f"Je souhaite proposer ma candidature à {name} pour une première opportunité correspondant à mon profil d’ingénieur informatique, notamment autour de {roles}."
            experience = "Lors de mon PFE chez Linedata, j’ai conçu une solution d’IA agentique destinée à moderniser un produit logiciel complexe, en reliant analyse métier, développement et automatisation."
        body = (
            "Bonjour,\n\n"
            f"{opening}\n\n"
            "Récemment diplômé ingénieur en informatique de l’ENSI, avec une spécialisation en ingénierie financière, je maîtrise Python, Java, C++, le développement full-stack, les bases de données, le machine learning et l’IA générative. "
            f"{experience}\n\n"
            "Je recherche une première expérience dans laquelle je pourrai apprendre rapidement, prendre des responsabilités et transformer des besoins concrets en solutions utiles. Je reste ouvert aux différents métiers cohérents avec mon diplôme et serais heureux d’échanger sur vos besoins actuels ou futurs.\n\n"
            "Vous trouverez mon CV en pièce jointe. Je vous remercie pour votre attention.\n\n"
            "Bien cordialement,\n"
            "Mohamed Oussema Bahloul\n"
            "mohamedoussema.bahloul@ensi-uma.tn | +216 50 606 692\n"
            "linkedin.com/in/mohamedoussemabahloul"
        )
        invitation = f"Bonjour, jeune ingénieur ENSI en informatique et IA, je m’intéresse aux opportunités chez {name}. Je serais ravi de rejoindre votre réseau et d’échanger sur les profils juniors recherchés."
        followup = (
            f"Bonjour, merci d’avoir accepté mon invitation. Je recherche une première opportunité chez {name} autour de {roles}. "
            "Mon PFE chez Linedata portait sur la modernisation d’un produit financier avec des agents IA. Pourrais-je vous transmettre mon CV ou connaître le bon interlocuteur ?"
        )
    else:
        subject = "Junior AI, Data & Software Engineering Application – Mohamed Oussema Bahloul"
        if fintech:
            opening = f"I would like to apply to {name} for an entry-level opportunity in AI, data, software engineering, business analysis, or technology-driven financial services."
            experience = "During my final-year project at Linedata, I helped modernize a financial software product by building an agentic AI solution involving three specialized agents, a RAG architecture, and 24 integration tools."
        else:
            opening = f"I would like to apply to {name} for an entry-level opportunity aligned with my computer engineering background, particularly in {roles}."
            experience = "During my final-year project at Linedata, I built an agentic AI solution to modernize a complex software product, combining business analysis, development, and automation."
        body = (
            "Dear Hiring Team,\n\n"
            f"{opening}\n\n"
            "I recently graduated as a Computer Engineer from ENSI, specializing in Financial Engineering. My background includes Python, Java, C++, full-stack development, databases, machine learning, and generative AI. "
            f"{experience}\n\n"
            "I am looking for a first full-time opportunity where I can learn quickly, take ownership, and turn real business needs into useful solutions. I am open to roles consistent with my degree and would welcome a conversation about your current or upcoming needs."
            + (" I am based in Tunisia and open to relocation or an international remote arrangement where available." if foreign else "")
            + "\n\nMy CV is attached for your consideration. Thank you for your time.\n\n"
            "Kind regards,\n"
            "Mohamed Oussema Bahloul\n"
            "mohamedoussema.bahloul@ensi-uma.tn | +216 50 606 692\n"
            "linkedin.com/in/mohamedoussemabahloul"
        )
        invitation = f"Hello, I am an ENSI Computer Engineering graduate interested in junior opportunities at {name}. I would be glad to connect and learn which profiles your team is currently seeking."
        followup = (
            f"Hello, thank you for accepting my invitation. I am seeking an entry-level opportunity at {name} in {roles}. "
            "My final-year project at Linedata focused on modernizing a financial product with AI agents. May I share my CV or ask who the right contact would be?"
        )
    return {
        "email_subject": subject,
        "email_body": body,
        "linkedin_invitation": invitation[:295],
        "linkedin_followup": followup,
    }


def load_source() -> list[dict[str, str]]:
    source = next((path for path in SOURCE_CANDIDATES if path.exists()), None)
    if not source:
        raise FileNotFoundError("Export.csv was not found")
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def load_overrides() -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    paths = ([OVERRIDES_CSV] if OVERRIDES_CSV.exists() else [])
    if OVERRIDE_BATCH_DIR.exists():
        paths.extend(sorted(OVERRIDE_BATCH_DIR.glob("*.csv")))
    for path in paths:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                overrides[row["organization_key"]] = row
    return overrides


def load_location_overrides() -> dict[str, dict[str, str]]:
    """Load externally checked locations without mixing them with HR research."""
    if not LOCATION_OVERRIDES_CSV.exists():
        return {}
    with LOCATION_OVERRIDES_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["organization_key"]: row for row in csv.DictReader(handle)}


def choose_location(rows: list[dict[str, str]]) -> tuple[str, str, bool, str]:
    classifications = [classify_address(row.get("Adresse", "")) for row in rows]
    for wanted in ("Tunis", "Ariana", "Étranger"):
        for result in classifications:
            if result[0] == wanted:
                return result
    if any(item[0] == "Localisation non vérifiable" for item in classifications):
        return "Localisation non vérifiable", MISSING, False, "Adresse CSV insuffisante ou ambiguë"
    return "Exclue — autre ville tunisienne", "Tunisie", False, "Toutes les adresses CSV sont hors Tunis et Ariana"


def build_records(source_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        grouped[organization_key(row.get("Nom de l'entreprise", ""))].append(row)

    overrides = load_overrides()
    location_overrides = load_location_overrides()
    records: list[dict[str, str]] = []
    for key, rows in grouped.items():
        names = [row.get("Nom de l'entreprise", "").strip() for row in rows if row.get("Nom de l'entreprise", "").strip()]
        name = Counter(names).most_common(1)[0][0] if names else key
        addresses = sorted({row.get("Adresse", "").strip() for row in rows if row.get("Adresse", "").strip()})
        raw_emails = sorted({row.get("Email entreprise", "").strip() for row in rows if row.get("Email entreprise", "").strip()})
        source_ids = sorted({row.get("ID", "").strip() for row in rows if row.get("ID", "").strip()}, key=lambda x: int(x) if x.isdigit() else x)
        location, country, eligible, location_reason = choose_location(rows)
        location_override = location_overrides.get(key, {})
        if location_override:
            location = location_override["location_status"].strip()
            country = location_override["country"].strip()
            eligible = location_override["eligible"].strip() == "Oui"
            location_reason = location_override["location_reason"].strip()
        sector = infer_sector(name, raw_emails, addresses)
        match, roles, match_reason = initial_match(sector)
        cv, language = cv_for(sector, location, country)
        valid_source_emails = [email for email in raw_emails if valid_email(email)]

        # Conservative baseline.  External research may replace every field below.
        junior_status = MISSING
        foreign_status = "Non applicable" if location != "Étranger" else "Non vérifiable"
        potential = 0
        if eligible:
            potential = 20 + round(match * 2)
            potential += 5 if valid_source_emails else 0
        verification_status = "À rechercher" if eligible else "Exclu par localisation"
        email_status = "Présent dans le CSV — à vérifier" if valid_source_emails else NO_EMAIL

        record = {
            "organization_key": key,
            "organization_name": name,
            "source_ids": " | ".join(source_ids),
            "source_row_count": str(len(rows)),
            "source_addresses": " | ".join(addresses),
            "source_emails": " | ".join(raw_emails),
            "location_status": location,
            "country": country,
            "eligible": "Oui" if eligible else "Non",
            "location_reason": location_reason,
            "sector": sector,
            "target_roles": roles if eligible else "Non applicable",
            "match_score_10": f"{match:.1f}" if eligible else "0.0",
            "match_reason": match_reason if eligible else "Exclu par la condition géographique",
            "junior_status": junior_status if eligible else "Non applicable",
            "junior_evidence": MISSING if eligible else "Non applicable",
            "foreign_employee_status": foreign_status,
            "foreign_employee_evidence": MISSING if location == "Étranger" else "Non applicable",
            "active_jobs": MISSING if eligible else "Non applicable",
            "linkedin_contact_name": MISSING if eligible else "Non applicable",
            "linkedin_contact_role": MISSING if eligible else "Non applicable",
            "linkedin_profile": MISSING if eligible else "Non applicable",
            "contact_verification": "À vérifier" if eligible else "Non applicable",
            "verified_email": NO_EMAIL if eligible else "Non applicable",
            "email_status": email_status if eligible else "Non applicable",
            "application_channel": MISSING if eligible else "Non applicable",
            "recommended_cv": cv if eligible else "Non applicable",
            "language": language if eligible else "Non applicable",
            "potential_score_100": str(potential),
            "priority": priority(potential) if eligible else "Exclu",
            "sources": MISSING if eligible else "CSV source",
            "checked_date": TODAY,
            "verification_status": verification_status,
            "notes": "Faible adéquation initiale : candidature à faible priorité." if eligible and match < 5 else "",
        }
        if eligible:
            record.update(templates(name, sector, roles, language, location == "Étranger"))
        else:
            record.update({"email_subject": "", "email_body": "", "linkedin_invitation": "", "linkedin_followup": ""})

        if location_override:
            record["sources"] = location_override["location_sources"].strip()
            record["checked_date"] = location_override["location_checked_date"].strip()
            confidence = location_override["location_confidence"].strip()
            record["notes"] = (record["notes"] + " " if record["notes"] else "") + f"Confiance localisation : {confidence}."
            if location == "Localisation non vérifiable":
                record["verification_status"] = "Localisation non vérifiable après recherche Google"
            elif eligible:
                record["verification_status"] = "Localisation vérifiée — recrutement à rechercher"
            else:
                record["verification_status"] = "Exclu après vérification externe de localisation"

        override = overrides.get(key, {})
        for field, value in override.items():
            if field != "organization_key" and value.strip():
                record[field] = value.strip()
        if record["eligible"] == "Oui":
            try:
                record["priority"] = priority(int(float(record["potential_score_100"])))
            except ValueError:
                pass
        records.append(record)
    return sorted(records, key=lambda item: (item["eligible"] != "Oui", -float(item["match_score_10"]), item["organization_name"].casefold()))


FIELDNAMES = [
    "organization_key", "organization_name", "source_ids", "source_row_count",
    "source_addresses", "source_emails", "location_status", "country", "eligible",
    "location_reason", "sector", "target_roles", "match_score_10", "match_reason",
    "junior_status", "junior_evidence", "foreign_employee_status",
    "foreign_employee_evidence", "active_jobs", "linkedin_contact_name",
    "linkedin_contact_role", "linkedin_profile", "contact_verification",
    "verified_email", "email_status", "application_channel", "recommended_cv",
    "language", "potential_score_100", "priority", "email_subject", "email_body",
    "linkedin_invitation", "linkedin_followup", "sources", "checked_date",
    "verification_status", "notes",
]


def write_csv(records: list[dict[str, str]]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def write_csv_to(path: Path, records: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def md_escape(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ")


def write_markdown(records: list[dict[str, str]], source_count: int) -> None:
    eligible = [row for row in records if row["eligible"] == "Oui"]
    excluded = [row for row in records if row["eligible"] != "Oui"]
    counts = Counter(row["location_status"] for row in records)
    verified_count = sum(
        row["verification_status"].startswith("Vérifié manuellement")
        for row in eligible
    )
    pending_count = len(eligible) - verified_count
    location_review_eligible = sum(
        row["verification_status"] == "Localisation vérifiée — recrutement à rechercher"
        for row in records
    )
    location_review_excluded = sum(
        row["verification_status"] == "Exclu après vérification externe de localisation"
        for row in records
    )
    location_review_unresolved = sum(
        row["verification_status"] == "Localisation non vérifiable après recherche Google"
        for row in records
    )
    lines = [
        "# Recherche d’entreprises et candidatures personnalisées",
        "",
        f"> Généré le **{TODAY}** à partir de **{source_count} lignes**. Les scores de potentiel sont des indicateurs de priorisation, pas des probabilités d’embauche.",
        "",
        "## État de la recherche",
        "",
        f"- Organismes consolidés : **{len(records)}**",
        f"- Organismes admissibles : **{len(eligible)}**",
        f"- Organismes exclus ou non localisables : **{len(excluded)}**",
        f"- Tunis : **{counts.get('Tunis', 0)}** ; Ariana : **{counts.get('Ariana', 0)}** ; étranger : **{counts.get('Étranger', 0)}**",
        f"- Recherche des anciennes localisations ambiguës : **{location_review_eligible} admissibles**, **{location_review_excluded} hors périmètre tunisien** et **{location_review_unresolved} encore non vérifiables**.",
        f"- Fiches enrichies et contrôlées manuellement sur sources externes : **{verified_count}** ; fiches de base restant à vérifier : **{pending_count}**.",
        "- `À rechercher` signifie que la fiche repose encore sur le CSV et doit être enrichie par des sources externes. `Localisation vérifiée — recrutement à rechercher` confirme uniquement la ville ou le pays.",
        "- **Ne pas envoyer une fiche dont le recrutement reste à rechercher sans vérifier au préalable son offre, son contact et son canal de candidature.**",
        "- Aucune adresse email marquée comme vérifiée n’est déduite d’un modèle de nommage.",
        "",
        "## Méthodologie",
        "",
        "- Les 1 563 lignes sont normalisées puis regroupées par organisme ; tous les identifiants et toutes les adresses d’origine sont conservés.",
        "- L’admissibilité géographique repose d’abord sur les adresses du CSV. Les entrées auparavant ambiguës ont ensuite été recherchées individuellement par nom sur Google et classées à partir de sources externes citées ; Tunis et Ariana ou l’étranger sont admissibles, les autres villes tunisiennes sont exclues.",
        "- Les informations de recrutement vérifiées proviennent en priorité des sites officiels, puis de LinkedIn et de plateformes d’emploi fiables. Une offre ancienne ou fermée est signalée comme telle et n’est jamais comptée comme active.",
        "- **Score de correspondance /10** : domaine et métiers (3), compétences techniques (3), expérience demandée (2), pertinence des projets et expériences (2).",
        "- **Score de potentiel /100** : ouverture aux juniors (25), offre active adaptée (25), localisation/admissibilité (20), adéquation globale (20), accessibilité d’un recruteur ou canal fiable (10). Il sert uniquement à prioriser.",
        "- Pour l’étranger, `Oui`, `Non` ou `Non vérifiable` n’est renseigné qu’avec une preuve ou une explication. L’absence d’information sur le visa ou la mobilité reste `Non vérifiable`.",
        "- Les emails du fichier source restent séparés du champ `Email vérifié`. Aucune adresse nominative n’est construite ou supposée.",
        "- Date de référence de la recherche : **" + TODAY + "**.",
        "",
        "## Légende",
        "",
        "- **A** : très prioritaire ; **B** : prioritaire ; **C** : à tenter ; **D** : faible priorité.",
        "- **CV FinTech** : banque, finance, assurance, paiement, risque et produits financiers.",
        "- **CV général** : IA, Data, logiciel, cloud, cybersécurité, recherche et IT.",
        "",
        "## Tableau de priorité",
        "",
        "| Organisme | Zone | Domaine | Match /10 | Potentiel /100 | Priorité | Junior | Vérification |",
        "|---|---|---|---:|---:|---|---|---|",
    ]
    for row in sorted(
        eligible,
        key=lambda item: (
            -int(float(item["potential_score_100"])),
            item["organization_name"].casefold(),
        ),
    ):
        lines.append(
            f"| {md_escape(row['organization_name'])} | {md_escape(row['location_status'])} | {md_escape(row['sector'])} | "
            f"{row['match_score_10']} | {row['potential_score_100']} | {md_escape(row['priority'])} | "
            f"{md_escape(row['junior_status'])} | {md_escape(row['verification_status'])} |"
        )

    lines.extend(["", "## Fiches de candidature", ""])
    for row in sorted(eligible, key=lambda item: (-int(float(item["potential_score_100"])), item["organization_name"].casefold())):
        lines.extend([
            f"### {row['organization_name']}",
            "",
            f"- **IDs source :** {row['source_ids']}",
            f"- **Adresse(s) CSV :** {row['source_addresses']}",
            f"- **Zone :** {row['location_status']} — {row['country']}",
            f"- **Domaine :** {row['sector']}",
            f"- **Correspondance :** {row['match_score_10']}/10 — {row['match_reason']}",
            f"- **Potentiel :** {row['potential_score_100']}/100 — {row['priority']}",
            f"- **Métiers ciblés :** {row['target_roles']}",
            f"- **Juniors :** {row['junior_status']} — {row['junior_evidence']}",
            f"- **Candidats étrangers :** {row['foreign_employee_status']} — {row['foreign_employee_evidence']}",
            f"- **Offres actives :** {row['active_jobs']}",
            f"- **Contact :** {row['linkedin_contact_name']} — {row['linkedin_contact_role']}",
            f"- **LinkedIn :** {row['linkedin_profile']}",
            f"- **Email :** {row['verified_email']} ({row['email_status']})",
            f"- **Canal officiel :** {row['application_channel']}",
            f"- **CV conseillé :** `{row['recommended_cv']}`",
            f"- **Sources :** {row['sources']}",
            f"- **Vérifié le :** {row['checked_date']} — {row['verification_status']}",
            "",
            f"**Objet :** {row['email_subject']}",
            "",
            "**Email prêt à envoyer**",
            "",
            row["email_body"],
            "",
            "**Invitation LinkedIn**",
            "",
            row["linkedin_invitation"],
            "",
            "**Message après acceptation**",
            "",
            row["linkedin_followup"],
            "",
            "---",
            "",
        ])

    lines.extend([
        "## Organismes exclus ou non localisables",
        "",
        "| Organisme | IDs source | Adresse(s) | Statut | Motif | Source / vérification |",
        "|---|---|---|---|---|---|",
    ])
    for row in sorted(excluded, key=lambda item: item["organization_name"].casefold()):
        lines.append(
            f"| {md_escape(row['organization_name'])} | {md_escape(row['source_ids'])} | {md_escape(row['source_addresses'])} | "
            f"{md_escape(row['location_status'])} | {md_escape(row['location_reason'])} | "
            f"{md_escape(row['sources'])} — {md_escape(row['checked_date'])} |"
        )
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_foreign_markdown(records: list[dict[str, str]]) -> None:
    """Write a standalone report containing no Tunisian organizations."""
    foreign = sorted(
        (row for row in records if row["location_status"] == "Étranger"),
        key=lambda item: (
            -int(float(item["potential_score_100"])),
            item["organization_name"].casefold(),
        ),
    )
    countries = Counter(row["country"] for row in foreign)
    lines = [
        "# Entreprises situées hors de Tunisie",
        "",
        f"> Généré le **{TODAY}**. Ce document contient uniquement les **{len(foreign)} organismes étrangers** identifiés dans la base consolidée.",
        "",
        "## Règles de lecture",
        "",
        "- Aucune entreprise située en Tunisie n’est incluse dans ce fichier.",
        "- Le statut concernant les candidats étrangers, le visa, la relocation ou le travail international n’est affirmé que lorsqu’une preuve est disponible.",
        "- `Non vérifiable` signifie qu’aucune politique publique suffisamment fiable n’a été trouvée.",
        "- Une offre ancienne ou fermée n’est jamais présentée comme active.",
        "- Les scores de potentiel servent à prioriser les démarches ; ils ne représentent pas une probabilité d’embauche.",
        "",
        "## Répartition par pays",
        "",
        "| Pays | Organismes |",
        "|---|---:|",
    ]
    for country, count in sorted(countries.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {md_escape(country)} | {count} |")

    lines.extend([
        "",
        "## Tableau de priorité",
        "",
        "| Organisme | Pays | Domaine | Match /10 | Potentiel /100 | Priorité | Juniors | Candidats étrangers | Vérification |",
        "|---|---|---|---:|---:|---|---|---|---|",
    ])
    for row in foreign:
        lines.append(
            f"| {md_escape(row['organization_name'])} | {md_escape(row['country'])} | {md_escape(row['sector'])} | "
            f"{row['match_score_10']} | {row['potential_score_100']} | {md_escape(row['priority'])} | "
            f"{md_escape(row['junior_status'])} | {md_escape(row['foreign_employee_status'])} | "
            f"{md_escape(row['verification_status'])} |"
        )

    lines.extend(["", "## Fiches de candidature", ""])
    for row in foreign:
        lines.extend([
            f"### {row['organization_name']}",
            "",
            f"- **Pays :** {row['country']}",
            f"- **Adresse(s) source :** {row['source_addresses']}",
            f"- **Domaine :** {row['sector']}",
            f"- **Correspondance :** {row['match_score_10']}/10 — {row['match_reason']}",
            f"- **Potentiel :** {row['potential_score_100']}/100 — {row['priority']}",
            f"- **Métiers ciblés :** {row['target_roles']}",
            f"- **Ouverture aux juniors :** {row['junior_status']} — {row['junior_evidence']}",
            f"- **Candidats étrangers/visa/relocation :** {row['foreign_employee_status']} — {row['foreign_employee_evidence']}",
            f"- **Offres actives :** {row['active_jobs']}",
            f"- **Contact :** {row['linkedin_contact_name']} — {row['linkedin_contact_role']}",
            f"- **LinkedIn :** {row['linkedin_profile']}",
            f"- **Email :** {row['verified_email']} ({row['email_status']})",
            f"- **Canal officiel :** {row['application_channel']}",
            f"- **CV conseillé :** `{row['recommended_cv']}`",
            f"- **Sources :** {row['sources']}",
            f"- **Vérifié le :** {row['checked_date']} — {row['verification_status']}",
            "",
            f"**Objet :** {row['email_subject']}",
            "",
            "**Email prêt à envoyer**",
            "",
            row["email_body"],
            "",
            "**Invitation LinkedIn**",
            "",
            row["linkedin_invitation"],
            "",
            "**Message après acceptation**",
            "",
            row["linkedin_followup"],
            "",
            "---",
            "",
        ])
    FOREIGN_OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    FOREIGN_OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    source_rows = load_source()
    records = build_records(source_rows)
    write_csv(records)
    write_markdown(records, len(source_rows))
    foreign_records = [row for row in records if row["location_status"] == "Étranger"]
    write_csv_to(FOREIGN_OUTPUT_CSV, foreign_records)
    write_foreign_markdown(records)
    eligible = sum(row["eligible"] == "Oui" for row in records)
    print(f"Source rows: {len(source_rows)}")
    print(f"Consolidated organizations: {len(records)}")
    print(f"Eligible organizations: {eligible}")
    print(f"CSV: {OUTPUT_CSV}")
    print(f"README: {OUTPUT_MD}")
    print(f"Foreign organizations: {len(foreign_records)}")
    print(f"Foreign CSV: {FOREIGN_OUTPUT_CSV}")
    print(f"Foreign README: {FOREIGN_OUTPUT_MD}")


if __name__ == "__main__":
    main()
