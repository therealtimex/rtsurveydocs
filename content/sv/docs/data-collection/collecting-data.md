---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Samla in data"
icon: "rocket_launch"
toc: true
description: "En snabbstartsguide för att köra en undersökning med rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Nybörjare"]
---

När ett formulär har driftsatts och räknare är tilldelade kan datainsamlingen börja. **rtSurvey** stöder sömlös datainsamling i både webbläsare och dedikerade mobilapplikationer, vilket säkerställer flexibilitet oavsett om ditt team är uppkopplat mot internet eller arbetar i avlägsna, offlinemiljöer.

## Välja rätt insamlingsmetod

Beroende på ditt projekts geografi och anslutning kan du välja den optimala metoden för dina räknare:

- **Webbläsare (Online):** Bäst för callcenter, kontorsbaserad datainmatning eller respondenter som fyller i självadministrerade offentliga undersökningar.
- **rtWork / rtSurvey-mobilapp (Online och Offline):** Bäst för fältoperationer, avlägsna områden med instabilt internet och undersökningar som kräver mediabilagor (foton, GPS-koordinater, offlinekartor).

---

## Metod 1: Samla in data via webbläsare

Att använda webbformulärsgränssnittet gör det möjligt för räknare att omedelbart börja samla in data utan att installera någon programvara.

### 1. Åtkomst till webbformulär-URL:en
Från instrumentpanelen **Hantera formulär** i kontrollpanelen, hitta ditt målformulär och klicka på knappen **Webbformulär-URL** för att generera en säker länk.

### 2. Formulärinmatning
- Öppna den angivna URL:en i valfri modern webbläsare.
- Om formuläret kräver autentisering måste räknaren logga in med sina inloggningsuppgifter. Om det är inställt på "Offentlig synlighet" kan de fortsätta direkt.
- Fyll i undersökningsfrågorna. Gränssnittet tillämpar automatiskt logik, hoppmönster och valideringsregler.
- **Mediainsamling:** Om formuläret inkluderar bild-, ljud- eller videofrågor uppmanar webbläsaren dig att ladda upp en fil från din dator eller använda din enhets webbkamera/mikrofon om tillgänglig.

### 3. Inlämning
Vid den sista sidan, klicka på **Skicka in**. Webbläsaren kräver en aktiv internetanslutning för att slutföra inlämningen. När inlämningen lyckats reflekteras data omedelbart i gränssnittet **Hantera inlämningar**.

---

## Metod 2: Samla in data via mobilapp (Offline)

För robust fältdatainsamling erbjuder mobilapplikationerna fullständiga offlinekapabiliteter.

### 1. Installera och autentisera
- Ladda ner applikationen **rtWork** (eller **rtSurvey**) från Google Play Store eller Apple App Store.
- Öppna appen och logga in med de tilldelade räknarinloggningsuppgifterna.

### 2. Ladda ner formulär (Kräver Internet)
- Navigera till avsnittet **Formulär** eller **Uppgifter** i appen.
- Tryck på ikonen **Synkronisera** eller **Ladda ner** för att hämta de senaste frågeformulärsdesignerna från servern. När de laddats ner lagras formulären lokalt på enheten.

### 3. Samla in data (Offline)
- Öppna det nedladdade formuläret och börja intervjun.
- Du kan säkert samla in data helt offline.
- **Mediainsamling:** Mobilappen integreras nativt med din enhets hårdvara. Du kan ta foton, spela in ljud, spela in video och logga exakta GPS-koordinater direkt i appen, även utan internetanslutning.
- När du avslutar en intervju, slutför posten. Slutförda poster köas säkert i appens utkorg.

### 4. Synkronisera inlämningar (Kräver Internet)
- När räknaren återvänder till ett område med internetåtkomst (Wi-Fi eller mobildata) måste de navigera till gränssnittet **Utkorg** eller **Synkronisera**.
- Instruera appen att skicka de slutförda formulären. Appen överför de köade posterna och alla bifogade mediafiler säkert till servern, varefter de visas i datanätet för granskning.
