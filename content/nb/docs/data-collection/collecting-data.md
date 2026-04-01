---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Samle inn data"
icon: "rocket_launch"
toc: true
description: "En hurtigstartveiledning for å gjennomføre en undersøkelse med rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Nybegynnere"]
---

Når et skjema er distribuert og feltarbeidere er tildelt, kan datainnsamling begynne. **rtSurvey** støtter sømløs datainnhenting på tvers av både nettlesere og dedikerte mobilapplikasjoner, og sikrer fleksibilitet enten teamet er koblet til internett eller arbeider i avsidesliggende, frakoblede miljøer.

## Velge riktig innsamlingsmetode

Avhengig av prosjektets geografi og tilkobling kan du velge den optimale metoden for feltarbeiderne:

- **Nettleser (Online):** Best for telefonsentre, kontorbasert dataregistrering eller respondenter som fyller ut selvadministrerte offentlige undersøkelser.
- **rtWork / rtSurvey-mobilapp (Online og offline):** Best for feltoperasjoner, avsidesliggende områder med ustabilt internett og undersøkelser som krever medievedlegg (bilder, GPS-koordinater, offline-kart).

---

## Metode 1: Samle inn data via nettleser

Ved å bruke nettskjemagrensesnittet kan feltarbeidere begynne å samle inn data umiddelbart uten å installere programvare.

### 1. Åpne nettskjema-URL-en
Fra **Administrer skjemaer**-dashbordet i kontrollpanelet, finn målskjemaet ditt og klikk **Nettskjemaets URL**-knappen for å generere en sikker lenke.

### 2. Skjemautfylling
- Åpne den oppgitte URL-en i en hvilken som helst moderne nettleser.
- Hvis skjemaet krever autentisering, må feltarbeideren logge inn med sine legitimasjonsopplysninger. Hvis det er satt til "Offentlig synlighet," kan de gå direkte.
- Fyll ut undersøkelsesspørsmålene. Grensesnittet vil automatisk håndheve logikk, hoppemønstre og valideringsregler.
- **Mediefangst:** Hvis skjemaet inkluderer bilde-, lyd- eller videospørsmål, vil nettleseren be deg om å laste opp en fil fra datamaskinen eller bruke enhetens webkamera/mikrofon hvis tilgjengelig.

### 3. Innsending
Når du er på den siste siden, klikk **Send**. Nettleseren krever en aktiv internettforbindelse for å ferdigstille innsendingen. Når vellykket, vil dataene umiddelbart vises i **Administrer innsendinger**-grensesnittet.

---

## Metode 2: Samle inn data via mobilapp (offline)

For robust feltdatainnsamling gir mobilapplikasjonene fullstendig offline-kapasitet.

### 1. Installer og autentiser
- Last ned **rtWork** (eller **rtSurvey**)-applikasjonen fra Google Play Store eller Apple App Store.
- Åpne appen og logg inn med tildelte feltarbeiderlegitimasjonsopplysninger.

### 2. Last ned skjemaer (krever internett)
- Naviger til **Skjemaer** eller **Oppgaver**-seksjonen i appen.
- Trykk på **Synkroniser** eller **Last ned**-ikonet for å hente de nyeste spørreskjemadesignene fra serveren. Når de er lastet ned, lagres skjemaene lokalt på enheten.

### 3. Samle inn data (offline)
- Åpne det nedlastede skjemaet og begynn intervjuet.
- Du kan samle inn data fullstendig offline.
- **Mediefangst:** Mobilappen integreres nativt med enhetens maskinvare. Du kan ta bilder, spille inn lyd, spille inn video og logge presise GPS-koordinater direkte i appen, selv uten internettforbindelse.
- Når du er ferdig med et intervju, ferdigstill posten. Ferdigstilte poster settes i kø trygt i appens utboks.

### 4. Synkroniser innsendinger (krever internett)
- Når feltarbeideren returnerer til et område med internettilgang (Wi-Fi eller mobildata), må de navigere til **Utboks** eller **Synkroniser**-grensesnittet.
- Instruer appen til å sende de ferdigstilte skjemaene. Appen vil overføre postene i kø og alle vedlagte mediefiler sikkert til serveren, og de vil deretter vises i datarutenettet for gjennomgang.
