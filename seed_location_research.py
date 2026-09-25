#!/usr/bin/env python3
"""Create the auditable location-review layer for the 98 ambiguous records."""

from __future__ import annotations

import csv
from pathlib import Path

from build_research import organization_key


OUT = Path(__file__).with_name("location_research.csv")
CHECKED = "2026-09-25"
FIELDS = [
    "organization_key", "location_status", "country", "eligible",
    "location_reason", "location_sources", "location_checked_date",
    "location_confidence",
]
records: dict[str, dict[str, str]] = {}


def add(keys: str | list[str], status: str, country: str, eligible: bool,
        reason: str, sources: str, confidence: str = "Élevée") -> None:
    if isinstance(keys, str):
        keys = [keys]
    row = {
        "location_status": status,
        "country": country,
        "eligible": "Oui" if eligible else "Non",
        "location_reason": reason,
        "location_sources": sources,
        "location_checked_date": CHECKED,
        "location_confidence": confidence,
    }
    for key in keys:
        records[organization_key(key)] = {"organization_key": organization_key(key), **row}


def tunis(key: str, reason: str, source: str, confidence: str = "Élevée") -> None:
    add(key, "Tunis", "Tunisie", True, reason, source, confidence)


def ariana(key: str, reason: str, source: str, confidence: str = "Élevée") -> None:
    add(key, "Ariana", "Tunisie", True, reason, source, confidence)


def foreign(key: str | list[str], country: str, reason: str, source: str,
            confidence: str = "Élevée") -> None:
    add(key, "Étranger", country, True, reason, source, confidence)


def excluded(key: str | list[str], reason: str, source: str,
             confidence: str = "Élevée") -> None:
    add(key, "Exclue — autre ville tunisienne", "Tunisie", False, reason, source, confidence)


def unresolved(key: str, reason: str) -> None:
    add(
        key, "Localisation non vérifiable", "Non trouvé/non vérifiable", False,
        reason, "Recherche Google par nom — aucun résultat fiable (25/09/2026)", "Faible",
    )


# Tunis et Ariana
tunis("advyteam global services", "L'adresse indique Les Berges du Lac, dans le gouvernorat de Tunis.", "https://lake.jort.tn/annonces-legales/fr/2011/156.pdf", "Moyenne")
ariana("alola", "L'adresse source Rue de l'UMA, La Soukra, situe l'organisme dans l'Ariana.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
tunis("amc ernest and young", "EY/AMC est implanté au Centre Urbain Nord à Tunis.", "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/legal-and-privacy/documents/ey-member-firms-and-affiliates-as-on-15-april.pdf")
tunis("azur systemes", "L'annuaire professionnel situe Azur Systèmes à Tunis.", "https://www.goafricaonline.com/tn/832946-azur-systemes")
tunis("coficab", "La page de contact officielle recense l'implantation tunisienne de COFICAB.", "https://www.coficab.com/contact/")
ariana("conseil solution formation", "La page LinkedIn de CSF indique Cité El Ghazala/Ennkhilet, Ariana.", "https://www.linkedin.com/company/csf-conseil-solution-formation")
ariana("contact center services", "La page de l'entreprise situe 2CS au Pôle technologique El Ghazala, Ariana.", "https://tn.linkedin.com/company/contact-center-services-2cs")
ariana("digimytch", "La page LinkedIn de l'entreprise indique Menzah 6, Ariana.", "https://www.linkedin.com/company/digimytch")
tunis("discovery intech", "Le site officiel situe Discovery Intech à Charguia II, Tunis.", "https://www.discovery.com.tn/fr/recherche")
ariana("eventizer platforms", "L'adresse publique et l'adresse CSV situent Eventizer à Menzah 8, Ariana.", "https://tn.linkedin.com/jobs/view/assistant-administratif-et-financier-chez-eventizer-platforms-at-eventizer-3953399959", "Moyenne")
tunis("get wireless", "Le site officiel indique une adresse au Lac 3/Khaireddine, Tunis.", "https://getwireless.com.tn/a-propos-get-wireless/")
tunis("hello dati", "L'annuaire d'entreprise situe Hello Dati à Cité El Khadhra, Tunis.", "https://www.africabizinfo.com/fr-TN/hello-dati", "Moyenne")
ariana("hope horizan", "L'adresse source indique Riadh El Andalous, Ariana.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
tunis("inoteqia health tech", "L'adresse source indique Aïn Zaghouan, gouvernorat de Tunis.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
ariana("international ems trainer", "Un document officiel du ministère mentionne l'adresse à Ennaser 2, Ariana.", "https://www.mtc.gov.tn/fileadmin/Investisseurs/Cahier_des_Charges/Liste__des_societes_integrateurs.pdf")
tunis("it network consulting", "L'adresse source indique Cité des Médecins, El Manar 2, Tunis.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
tunis("ke tunisia", "L'adresse source indique Rue du Lac Loch Ness, Les Berges du Lac, Tunis.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
tunis("level up by proxiad", "Golden Tower se trouve au Centre Urbain Nord, Tunis.", "https://mapcarta.com/fr/W522407305", "Moyenne")
tunis("military research center", "La publication scientifique rattache le Military Research Center à L'Aouina, Tunis.", "https://doi.org/10.1038/s41598-026-48925-1")
tunis("prologic tunisie", "L'annuaire situe le siège de Prologic Tunisie à Tunis.", "https://fr.cybo.com/TN-biz/prologic-tunisie-si%C3%A8ge-social_1i", "Moyenne")
tunis("quantylix", "L'annuaire professionnel situe Quantylix à La Goulette/Lac 3, Tunis.", "https://www.goafricaonline.com/tn/693204-quantylix-tunisie", "Moyenne")
tunis("seneca innovation center", "La page LinkedIn actuelle de l'entreprise indique Tunis comme siège.", "https://www.linkedin.com/company/seneca-innovation-center")
tunis("siryos", "La page de contact officielle situe Siryos au Centre Urbain Nord, Tunis.", "https://siryos.com/contact")
tunis("smart world it swit", "L'annonce légale et l'adresse source rattachent la société à Tunis.", "https://lake.jort.tn/annonces-legales/fr/2009/039.pdf", "Moyenne")
ariana("stmicroelectronics", "Une documentation certifiée situe STMicroelectronics au Technopôle El Ghazala, Ariana.", "https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/NSCIB-CC-0638980_st_vA01_0.pdf")
tunis("tunisie micro informatique tmi", "Le registre LEI situe TMI à El Kram, gouvernorat de Tunis.", "https://lei.bloomberg.com/leis/view/4117NMWXFO9M6JC1E362")

# Étranger
foreign("advensia gmbh", "Allemagne", "Le site officiel indique Stuttgart, Allemagne.", "https://advensia.de/career/working-at-advensia/")
foreign("agiir network", "France", "Le site officiel indique Riorges/Roanne, France.", "https://agiir-network.com/contact/")
foreign("ensta bretagne", "France", "L'annuaire officiel de l'administration française situe ENSTA Bretagne à Brest.", "https://lannuaire.service-public.gouv.fr/gouvernement/e789f321-05a2-4dc2-9367-c7d7228334a7")
foreign("esigelec", "France", "Le site officiel situe le campus à Saint-Étienne-du-Rouvray, France.", "https://esigelec.fr/fr/nous-contacter")
foreign("ess mondial gmbh", "Allemagne", "Le site officiel indique Reinbek, Allemagne.", "https://ess-mondial.de/de/unternehmen")
foreign("estarta solutions", "Jordanie", "Le site officiel indique Amman, Jordanie.", "https://www.estarta.com/privacy-policy/")
foreign("fourity", "Serbie", "Le site officiel indique Novi Sad, Serbie.", "https://www.fourity.com/contact-us/")
foreign("hochschule offenburg", "Allemagne", "Le site officiel indique Offenburg, Allemagne.", "https://www.hs-offenburg.de/impressum")
foreign("institute of reliable embedded systems and communication electronics ivesk", "Allemagne", "Le site de l'institut le rattache à Hochschule Offenburg, Allemagne.", "https://ivesk.hs-offenburg.de/en/page-3")
foreign("jawaker", "Émirats arabes unis", "La page de contact officielle indique le siège actuel à Abu Dhabi; l'adresse CSV d'Amman est également étrangère.", "https://www.jawaker.com/en/contact")
foreign(["laboratoire d informatique signal et image de la cote d opale universite littorale de la cote d opale", "laboratoire d informatique signal et image de la cote d oppale universite littorale de la cote d oppale"], "France", "Le site du LISIC indique Calais, France.", "https://lisic-prod.univ-littoral.fr/")
foreign("laboratoire dynafor", "France", "L'annuaire officiel INRAE situe DYNAFOR à Auzeville-Tolosane, France.", "https://annuaire.inrae.fr/structure/1201")
foreign("meddevo", "Allemagne", "Les mentions légales officielles indiquent Haunetal, Allemagne.", "https://www.meddevo.com/de/de/pharma/impressum")
foreign("neusta inspire gmbh", "Allemagne", "Les mentions légales officielles indiquent Brême, Allemagne.", "https://www.neusta-inspire.de/impressum/")
foreign("planblue gmbh", "Allemagne", "Un document institutionnel de l'entreprise indique Brême, Allemagne.", "https://sdgs.un.org/sites/default/files/2025-06/PlanBlue.pdf")
foreign("progresssoft", "Jordanie", "La page de contact officielle situe ProgressSoft à Amman, Jordanie.", "https://www.progressoft.com/cn/company/contactus")
foreign("responsible cyber", "Singapour", "Un document officiel CyberSG situe Responsible Cyber à Singapour.", "https://tig.cybersg.sg/wp-content/uploads/2024/05/Responsible-Cyber-Pte.-Ltd.pdf.pdf")
foreign("unite de catalyse et chimie du solide universite dartois faculte des sciences jean perrin", "France", "Le site universitaire situe l'UCCS Artois à Lens, France.", "https://uccs-old.univ-lille.fr/index.php/fr/vie-a-l-uccs/infos-pratiques/venir-a-l-uccs-lens")

# Autres villes tunisiennes, donc exclues par le périmètre convenu
excluded("abs computer", "Le site officiel et la page LinkedIn indiquent que le siège et l'équipe de développement sont à Sfax. La mention « Route de Tunis » est le nom de la route, pas une implantation dans le gouvernorat de Tunis.", "https://abscomputer.tn/ | https://www.linkedin.com/company/abscomputertn")
excluded("accent", "L'entreprise est située au Technopôle de Manouba.", "https://www.dnb.com/business-directory/company-profiles.ste_accent_alpha_connect_computing_for_entreprise.7803498b33d3a576a62a556f46d01e3a.html", "Moyenne")
excluded("agence via web", "L'adresse source indique Khézama, Sousse.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
excluded("ahwa solutions", "Le profil public du fondateur situe l'activité à Sidi Bouzid.", "https://tn.linkedin.com/in/hamed-bouallegui", "Moyenne")
excluded("aidodev", "Le registre d'entreprise situe AIDODEV à Mhamdia/Fouchana, Ben Arous.", "https://www.verif.com/en/company/AIDODEV-68d9e4571299230338fffd90/", "Moyenne")
excluded("anavid services tunisie", "Le site officiel situe l'entreprise à Sakiet Ezzit, Sfax.", "https://www.anavid.tn/")
excluded("caisse nationale d assurance maladie cnam bousalem", "L'agence CNAM est située à Bou Salem, Jendouba.", "https://www.zest-tourism.com/fr/direction/administrations/cnam-agence-bousalem-jendouba/", "Moyenne")
excluded("caveo automotive", "L'annuaire sectoriel situe CAVEO à Borj Cedria, Ben Arous.", "https://taa.tn/fr/node/247")
excluded("cgi studio", "Le profil public rattaché à CGI Studio indique Menzel Temime, Nabeul.", "https://tn.linkedin.com/in/amenallah-ben-achour-348a91130", "Moyenne")
excluded("compagnie des phosphates de gafsa", "L'annuaire gouvernemental situe la CPG à Gafsa.", "https://fr.tunisie.gov.tn/annuaireAdministration/527/11-compagnie-des-phosphates-de-gafsa-cpg.htm")
excluded("cresus solutions", "La page de contact officielle situe l'entreprise à Sfax.", "https://cresus-solutions.com/contact/")
excluded("delta web", "Une annonce publique situe Delta Web à Khézama, Sousse.", "https://www.tunisietravail.net/delta-web-it-recrute-developpeur-web-et-logiciels-92574/", "Moyenne")
excluded("docstream solutions", "La page LinkedIn de l'entreprise indique Monastir.", "https://www.linkedin.com/company/docstreamsolutions")
excluded("dot it", "L'adresse source indique la technopole de Sousse.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
excluded("dr oetker gias", "L'annuaire du gouvernorat situe Dr. Oetker GIAS à Grombalia, Nabeul.", "https://www.nabeul.gov.tn/fr/web-2-0-directory-2/dr-oetker-gias/")
excluded("designet web agency", "La page entreprise situe Designet à Menzel Temime, Nabeul.", "https://www.keejob.com/offres-emploi/companies/19911/designet-web-agency/")
excluded("influence consulting", "La page LinkedIn indique le Cyberparc Hammam Lif, Ben Arous.", "https://www.linkedin.com/company/influenceconsulting")
excluded("institut des regions arides ira", "Le site public de l'institut indique Médenine.", "https://grinta-sud.com/contact/", "Moyenne")
excluded("it youb consulting", "L'adresse source indique Ben Guerdane, Médenine; le mot « Tunis » désigne ici le pays et non la ville.", "https://www.xing.com/profile/Nacer_Selmi", "Moyenne")
excluded("la poste tunisienne bureau de poste 3070 kerkennah", "Le bureau est situé à Kerkennah, Sfax.", "https://ween.tn/fiche/bureau-de-poste-kerkennah", "Moyenne")
excluded("la societe tunisienne d electricite et de gaz", "L'enregistrement source concerne Médenine Nord.", "https://tunisie-electricite.com/medenine/beni-khedache", "Moyenne")
excluded(["laboratoire de recherche laria", "laboratoire lara de l ensi"], "L'ENSI et son laboratoire sont situés au campus de La Manouba.", "https://uma.rnu.tn/fr/research-structures?name=ecole-nationale-des-sciences-de-linformatique&universityEstablishment=2")
excluded("leader solution tactile", "Le profil public situe l'entreprise à Golaa, Kébili.", "https://tn.linkedin.com/in/arwa-benmansour-a57053262", "Moyenne")
excluded(["leoni", "societe leoni"], "Les implantations citées sont à Messadine et Sidi Bou Ali, gouvernorat de Sousse.", "https://taa.tn/fr/node/261")
excluded("maklada", "La documentation publique situe MAKLADA à El Jem, Mahdia.", "https://www.dm.gov.ae/wp-content/uploads/2019/02/CL12020162-1.pdf", "Moyenne")
excluded("medicacom", "Le site officiel situe Medicacom à Sfax.", "https://www.medicacom.tn/a-propos/")
excluded("megasoft", "La fiche publique de l'application indique Moknine, Monastir.", "https://play.google.com/store/apps/details?id=com.megasofterp.mobile", "Moyenne")
excluded("national smart for green solutions and applications", "Le registre d'entreprise indique Ras Jebel, Bizerte.", "https://b2bhint.com/en/company/tn/socobat--1333287N", "Moyenne")
excluded("novel ti", "L'annuaire professionnel situe Novel-TI à Sfax.", "https://annuairepro-afrique.com/en/novel-ti-sfax-tunisie", "Moyenne")
excluded("piva software", "Le registre d'entreprise situe PIVA Software à Sfax.", "https://www.dnb.com/business-directory/company-profiles.ste_piva_software.3e065201c2e6e3023b1d946eacf7937f.html", "Moyenne")
excluded("run it", "Le site officiel et la page LinkedIn indiquent Mahdia.", "https://www.run-it.tn/ | https://www.linkedin.com/company/runit-tunisie")
excluded("sancella", "Les annonces publiques de Sancella/SOTUPA indiquent Ksibet El Mediouni, Monastir.", "https://fr.linkedin.com/posts/groupe-sotupa-sancella-recrutement-97b5811a4_nous-recrutons-vous-%C3%AAtes-passionn%C3%A9-activity-7359510827424432128-xZnw", "Moyenne")
excluded("slama freres", "Le site officiel indique Oued Ellil, La Manouba.", "https://www.nejmahuiles.com/A-propos-de-nous?ln=eng")
excluded("smart engineering", "Le site de l'entreprise situe l'activité à Borj Cedria, Ben Arous.", "https://novahann.com/", "Moyenne")
excluded("smartegy tunisia", "La page de contact officielle indique Boumhel, Ben Arous.", "https://smartegy.tn/contact/")
excluded("societe regionale de transport medenine", "Le site officiel indique Médenine.", "https://srtm.tn/contact/")
excluded("sqlfm", "Le registre d'entreprise situe SQLFM à Zarzis, Médenine.", "https://entreprises.lefigaro.fr/sqlfm-00/entreprise-899294375", "Moyenne")
excluded("ste codiris technologique and consulting", "L'adresse source indique Monastir.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
excluded(["sw consulting", "s w consulting"], "Le registre d'entreprise situe SW Consulting à Bouhjar, Monastir.", "https://www.info-clipper.com/fr/entreprise/tunisie/sw-consulting.tnd62tl1c.html", "Moyenne")
excluded("taki academie", "L'adresse source et les résultats publics indiquent Sahloul, Sousse.", "Adresse complète du CSV recoupée par recherche Google, sans page officielle publique", "Moyenne")
excluded("zimys", "La page LinkedIn de l'entreprise indique Boumhel, Ben Arous.", "https://fr.linkedin.com/company/zimys")

# Les noms suivants restent trop vagues, factices ou sans identité concordante.
unresolved("conception", "Nom générique et adresse manifestement inexploitable; aucun organisme précis n'a pu être identifié.")
unresolved("ddddddd", "Nom et adresse factices; aucune entité concordante n'a été trouvée.")
unresolved("deeee", "Nom et adresse factices; aucune entité concordante n'a été trouvée.")
unresolved("eaezr", "Nom et adresse factices; aucune entité concordante n'a été trouvée.")
unresolved("national", "Nom trop générique et aucune adresse exploitable; identité impossible à déterminer.")
unresolved("qsffq", "Nom factice ou incomplet; aucune entité concordante n'a été trouvée.")
unresolved("sdfsdf", "Nom factice ou incomplet; aucune entité concordante n'a été trouvée.")
unresolved("the road solutions", "Les résultats trouvés concernent des homonymes étrangers sans preuve qu'ils correspondent à l'enregistrement tunisien.")
unresolved("training technology 2 0", "L'adresse « Zar » est insuffisante et aucun résultat fiable ne permet d'identifier l'entité.")
unresolved("vsx", "Sigle trop ambigu et aucune adresse exploitable; aucune entité concordante n'a été trouvée.")


with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(sorted(records.values(), key=lambda row: row["organization_key"]))

print(f"Location records: {len(records)}")
print(f"Output: {OUT}")
