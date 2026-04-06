---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Systeemgebruiker"
icon: "people"
toc: true
description: "Beheer rollen, machtigingen en onboarding voor alle platformdeelnemers."
tags: ["Gebruikers", "Toegangsbeheer", "Onboarding", "Rollen"]
---

# Systeemgebruikersbeheer

De module **Systeemgebruiker** (`/cpms/cpmsSystemUser/admin`) is een uitgebreide beheerinterface voor het controleren wie toegang heeft tot uw Real-Time Survey-platform (RT-CPMS) en welke acties ze kunnen uitvoeren.

![Systeemgebruikersinterface](/images/system_user.png)

## Uniforme beheerbenadering

In RT-CPMS is een **Enquêteur** gewoon een specifieke Rol die is toegewezen aan een Systeemgebruiker. Er is geen aparte "Enquêteur"-database. Of een gebruiker nu een beheerder op hoog niveau is die het webportaal monitort of een veldenquêteur die gegevens verzamelt via de mobiele app, ze worden allemaal beheerd binnen dit enkelvoudige, geïntegreerde kader.

## Belangrijkste functies

### 1. Gebruikersdirectory & rasterweergave
De hoofdinterface toont een gepagineerde lijst van alle gebruikers die zijn verbonden met de werkruimte. Belangrijke attributen zijn:
* **Organisatie-ID & Naam**: Logische groepering van gebruikers onder specifieke organisatie-entiteiten (bijv. `rta`, `partner_org`).
* **Rol**: Specificeert het machtigingsniveau van de gebruiker (bijv. `Beheerder`, `Teamleider`, `Enquêteur`).
* **Groep**: Ruimtelijke of logische groepstoewijzingen (bijv. specifieke districten of operationele teams).
* **Is gesynchroniseerd**: Geeft aan of het account succesvol is geïntegreerd met het centrale Single Sign-On (SSO)-systeem.
* **Status**: Visuele indicatoren die bevestigen of een account `Actief`, `Inactief`, `Verwijderd` of `Geblokkeerd` is.

**Globale acties:**
* **Systeemgebruiker toevoegen**: Handmatig een individueel profiel aanmaken.
* **Systeemgebruiker importeren**: Accounts in bulk uploaden via een Excel-sjabloon. U kunt conflicten oplossen met `Overslaan` of `Vervangen`-modi en direct synchroniseren met de SSO.
* **Bulk verwijderen**: Ondersteuning voor meervoudige selectie voor het verwijderen van accounts in bulk.

### 2. Toegangsbeheer & beveiliging
Bij het aanmaken of bewerken van een gebruikersprofiel zijn verschillende kritische beveiligings- en workflowvelden beschikbaar:
* **Gebruikerscode**: Een unieke identificator die het lokale CPMS-account koppelt aan de centrale SSO-opslagplaats.
* **Apparaatwisselcode**: Een robuust beveiligingstoken dat vereist is wanneer een enquêteur het mobiele apparaat moet wisselen dat hij gebruikt voor gegevensverzameling.
* **Bevoegdheidsniveau**: Een gedetailleerde prioriteits-/toegangsschaal variërend van 0 (laagste) tot 20 (hoogste).
* **Toezichttoggle**: Een selectievakje dat een standaardgebruiker onmiddellijk verheft tot beheerdersstatus.
* **Workflowautomatisering**: Een optie om "Bewerkingsverzoek automatisch goed te keuren," wat het gegevensopschoonings- en verificatieproces stroomlijnt voor vertrouwde gebruikers.

### 3. Codebeheer (Geautomatiseerde onboarding)
Gevonden onder het "Code"-subtabblad, beheert deze functie op hash gebaseerde registratie- en uitnodigingslinks, waardoor het onboardingproces voor grote teams wordt gestroomlijnd.

* **Registratie vs. Uitnodiging**: Kies of gebruikers zichzelf kunnen registreren via een gedistribueerde link of dat ze een directe beheerdersuitnodiging nodig hebben.
* **Vervaldatums**: Beperk onboarding tot specifieke tijdvensters.
* **Gebruikslimieten**: Beperk het aantal gebruikers dat kan deelnemen met één gegenereerde code.
* **Vooraf toegewezen rollen**: Gebruikers die via deze codes deelnemen, erven automatisch de vooraf gedefinieerde rol en het bevoegdheidsniveau, zodat ze onmiddellijk kunnen werken zonder handmatige beheerdersinterventie.
