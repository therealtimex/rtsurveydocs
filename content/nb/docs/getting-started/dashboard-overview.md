---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Dashbordoversikt"
icon: "home"
toc: true
description: "Forstå RT-CPMS-systemdashbordet og verktøyene for prosjektovervåking."
tags: ["Dashbord", "Oversikt", "Overvåking"]
---

# Systemdashbordet

Dashbordet (`/cpms/cpmsDashBoard/indexNew`) fungerer som det administrative kommandosenteret og den primære landingssiden for Real-Time Survey-plattformen (RT-CPMS).

![Forhåndsvisning av systemdashbordet](/images/dashboard_overview.png)

Det er utformet for å gi undersøkelsesledere en umiddelbar oversikt over aktive prosjekter, snarveier til viktige verktøy og et sentralisert knutepunkt for navigasjon på tvers av alle større plattformmoduler.

## Hovedfunksjoner

### 1. Prosjekt- og skjemavalg
Venstre panel inneholder navigatoren **Skjemaer og rapporter**. Dette området viser alle aktive undersøkelser i arbeidsområdet ditt.
* Ved å velge en bestemt undersøkelse (f.eks. *RTA - SURVEY 02*) retter du dashbordets overvåking og metrikk utelukkende mot det prosjektet.

### 2. Visualiserings- og metrikfiltre
Over prosjektlisten kan du veksle mellom flere kritiske dataperspektiver for å overvåke fremdriften i feltarbeidet i sanntid:
* **Antall etter starttid / sluttid**: Spor når feltarbeidere begynner og fullfører undersøkelsesøktene sine.
* **Antall etter innsendingsdato**: Overvåk det totale daglige volumet av data som når serveren.
* **Antall etter brukernavn**: Evaluer individuell feltarbeiderproduktivitet og ytelse.
* **Kart over intervjuer**: Se en geografisk (GIS) fordeling av hvor undersøkelsessvar samles inn, for å sikre at krav til romlig dekning oppfylles.

### 3. Applikasjonsportaler
Midten av dashbordet gir umiddelbar tilgang til datainnsamlingsgrensesnittene. Avhengig av feltarbeidernes maskinvare kan du starte eller lede dem til:
* **Nettapp**: For nettleserbasert datainnsamling.
* **Android-app**: Lenke til Google Play Store eller APK.
* **iOS-app**: Lenke til Apple App Store.

### 4. Direktesnarveier til moduler
Tre fremtredende handlingsknapper gir rask overgang til de oftest brukte driftsmodulene:
* **Skjema og dataregistrering**: Gå direkte til manuell administrasjon av innsamlede data.
* **Analyse og rapporter**: Åpne Business Intelligence (BI)-suiten for å krysstabell og illustrere undersøkelsessvar.
* **Tillatelseskonfigurasjon**: Juster hvem som har tilgang til den aktive undersøkelsen og hvilke roller de har.

### 5. Global navigasjonslinje
Den sammenleggbare venstre sidefeltet gir tilgang til hele RT-CPMS-bakstystemets moduløkosystem. Herfra kan du gå inn i:
* **Oppsett**: Administrere ansatte og aktive enheter.
* **Feltarbeidsadministrasjon**: Spore feltarbeidernes daglige aktivitet.
* **Kvalitetssikring**: Implementere og gjennomgå QA-regler og flagg.
* **Endelige leveranser**: Eksportere de rensede datasettene til CSV, PDF eller Stata.
