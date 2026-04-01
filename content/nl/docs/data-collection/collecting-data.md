---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Gegevens verzamelen"
icon: "rocket_launch"
toc: true
description: "Een snelstartgids voor het uitvoeren van een enquête met rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Zodra een formulier is uitgerold en enumeratoren zijn toegewezen, kan de gegevensverzameling beginnen. **rtSurvey** ondersteunt naadloze gegevensverzameling via zowel webbrowsers als speciale mobiele applicaties, waardoor flexibiliteit gewaarborgd is of uw team nu verbonden is met het internet of in afgelegen, offline omgevingen werkt.

## De juiste verzamelmethode kiezen

Afhankelijk van de geografie en connectiviteit van uw project kunt u de optimale methode voor uw enumeratoren kiezen:

- **Webbrowser (online):** Beste keuze voor callcenters, kantoorgebaseerde gegevensinvoer of respondenten die zelfbeheerde publieke enquêtes invullen.
- **rtWork / rtSurvey mobiele app (online en offline):** Beste keuze voor veldoperaties, afgelegen gebieden met instabiel internet en enquêtes waarbij mediabijlagen vereist zijn (foto's, GPS-coördinaten, offline kaarten).

---

## Methode 1: Gegevens verzamelen via webbrowser

Via de Webformulier-interface kunnen enumeratoren direct beginnen met gegevensverzameling zonder software te installeren.

### 1. Open de webformulier-URL
Ga vanuit het **Formulieren beheren**-dashboard in het Configuratiescherm naar uw doelformulier en klik op de knop **Webformulier-URL** om een beveiligde link te genereren.

### 2. Formulier invullen
- Open de opgegeven URL in een moderne webbrowser.
- Als het formulier authenticatie vereist, moet de enumerator inloggen met zijn of haar inloggegevens. Als het is ingesteld op "Publieke zichtbaarheid", kan de enumerator direct verder gaan.
- Vul de enquêtevragen in. De interface past automatisch logica, overslaapatronen en validatieregels toe.
- **Mediaopname:** Als het formulier afbeeldings-, audio- of videovragen bevat, vraagt de webbrowser u een bestand te uploaden vanaf uw computer of gebruik te maken van de webcam/microfoon van uw apparaat indien beschikbaar.

### 3. Indienen
Klik op de laatste pagina op **Indienen**. De browser vereist een actieve internetverbinding om de indiening te voltooien. Na een succesvolle indiening verschijnen de gegevens direct in de interface **Inzendingen beheren**.

---

## Methode 2: Gegevens verzamelen via mobiele app (offline)

Voor robuuste veldgegevensverzameling bieden de mobiele applicaties volledige offlinemogelijkheden.

### 1. Installeren en authenticeren
- Download de **rtWork**- (of **rtSurvey**-)applicatie uit de Google Play Store of Apple App Store.
- Open de app en log in met de toegewezen enumeratorgegevens.

### 2. Formulieren downloaden (internetverbinding vereist)
- Navigeer naar het gedeelte **Formulieren** of **Taken** in de app.
- Tik op het pictogram **Synchroniseren** of **Downloaden** om de nieuwste vragenlijstontwerpen van de server op te halen. Na het downloaden worden de formulieren lokaal op het apparaat opgeslagen.

### 3. Gegevens verzamelen (offline)
- Open het gedownloade formulier en begin het interview.
- U kunt gegevens volledig offline verzamelen.
- **Mediaopname:** De mobiele app integreert van nature met de hardware van uw apparaat. U kunt foto's maken, audio opnemen, video opnemen en nauwkeurige GPS-coördinaten vastleggen rechtstreeks in de app, zelfs zonder internetverbinding.
- Wanneer u een interview afrondt, sluit u het record af. Afgesloten records worden veilig in de outbox van de app in de wachtrij geplaatst.

### 4. Inzendingen synchroniseren (internetverbinding vereist)
- Zodra de enumerator terugkeert naar een gebied met internettoegang (wifi of mobiele data), moet hij of zij naar de interface **Outbox** of **Synchroniseren** navigeren.
- Instrueer de app om de afgesloten formulieren te verzenden. De app verzendt de gequeude records en alle bijgevoegde mediabestanden veilig naar de server, waarna ze verschijnen in het gegevensraster voor controle.
