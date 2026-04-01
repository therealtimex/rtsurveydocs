---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Systemanvändare"
icon: "people"
toc: true
description: "Hantera roller, behörigheter och introduktion för alla plattformsdeltagare."
tags: ["Användare", "Åtkomstkontroll", "Introduktion", "Roller"]
---

# Hantering av systemanvändare

Modulen **Systemanvändare** (`/cpms/cpmsSystemUser/admin`) är ett omfattande hanteringsgränssnitt för att kontrollera vem som har åtkomst till din Real-Time Survey-plattform (RT-CPMS) och vilka åtgärder de kan utföra.

![Gränssnitt för systemanvändare](/images/system_user.png)

## Enhetlig hanteringsmetod

I RT-CPMS är en **intervjuare** helt enkelt en specifik roll tilldelad en systemanvändare. Det finns ingen separat "intervjuare"-databas. Oavsett om en användare är en högnivåadministratör som övervakar webbportalen eller en fältintervjuare som samlar in data via mobilappen, hanteras de alla inom detta enda, enhetliga ramverk.

## Nyckelfunktioner

### 1. Användarkatalog och rutnätsvy
Huvudgränssnittet visar en sidindelad lista över alla användare anslutna till arbetsytan. Viktiga attribut inkluderar:
* **Organisations-ID och namn**: Logisk gruppering av användare under specifika organisatoriska enheter (t.ex. `rta`, `partner_org`).
* **Roll**: Anger användarens behörighetsnivå (t.ex. `Administratör`, `Teamledare`, `Intervjuare`).
* **Grupp**: Rumsliga eller logiska grupperingstilldelningar (t.ex. specifika distrikt eller operativa team).
* **Är synkroniserad**: Anger om kontot är framgångsrikt integrerat med det centrala Single Sign-On-systemet (SSO).
* **Status**: Visuella indikatorer som bekräftar om ett konto är `Aktivt`, `Inaktivt`, `Raderat` eller `Blockerat`.

**Globala åtgärder:**
* **Lägg till systemanvändare**: Skapa manuellt en individuell profil.
* **Importera systemanvändare**: Massuppladdning av konton med en Excel-mall. Du kan lösa konflikter med lägena `Hoppa över` eller `Ersätt` och synkronisera direkt med SSO.
* **Massradering**: Stöd för flerval för massborttagning av konton.

### 2. Åtkomstkontroll och säkerhet
När du skapar eller redigerar en användarprofil finns flera kritiska säkerhets- och arbetsflödesfält tillgängliga:
* **Användarkod**: En unik identifierare som kopplar det lokala CPMS-kontot till det centrala SSO-förrådet.
* **Byt-enhets-kod**: En robust säkerhetstoken som krävs när en intervjuare behöver byta den mobila enhet de använder för datainsamling.
* **Effektnivå**: En granulär prioritets-/åtkomstskala från 0 (lägst) till 20 (högst).
* **Tillsynsväxling**: En kryssruta som omedelbart höjer en standardanvändare till hanteringsstatus.
* **Arbetsflödesautomatisering**: Ett alternativ för att "Automatiskt godkänna begäran om redigering", vilket effektiviserar processen för datarensning och verifiering för betrodda användare.

### 3. Kodhantering (automatiserad introduktion)
Under underfliken "Kod" hanterar denna funktion hashbaserade registrerings- och inbjudningslänkar, vilket effektiviserar introduktionsprocessen för stora team.

* **Registrering kontra inbjudan**: Välj om användare kan självregistrera sig med en distribuerad länk eller om de kräver en direkt adminbjudan.
* **Utgångsdatum**: Begränsa introduktionen till specifika tidsfönster.
* **Användningsgränser**: Begränsa antalet användare som kan ansluta sig med en enda genererad kod.
* **Förtilldelade roller**: Användare som ansluter via dessa koder ärver automatiskt den fördefinierade rollen och effektnivån, vilket säkerställer att de är redo att arbeta omedelbart utan manuell adminintervention.
