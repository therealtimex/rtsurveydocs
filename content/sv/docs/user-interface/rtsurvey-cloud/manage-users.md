---
title: "Hantera användare"
description: "Skapa, organisera och hantera systemanvändare och fältpersonal."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 314
---

Modulen **Hantera användare** (ofta märkt **Hantera personal** i menyn Konfigurera) är den centraliserade katalogen för hantering av alla konton inom din CPMS-miljö. Den ger projektadministratörer de verktyg som behövs för att introducera personal, tilldela roller och bestämma geografiska åtkomstnivåer.

![Gränssnitt för hantera användare](/images/manage_users.png)

## Användarrutnätsöversikt

Huvudgränssnittet innehåller ett heltäckande rutnät som visar alla registrerade personalmedlemmar. Den här vyn låter administratörer snabbt söka, filtrera och granska kontostatus.

### Viktiga datakolumner

Rutnätet inkluderar följande viktig information för varje användare:

- **Användarnamn och fullständigt namn:** Primära identifierare för personalmedlemmen.
- **E-post:** Kontaktens e-postadress kopplad till kontot.
- **Användarroll:** Anger systembehörigheterna beviljade till användaren (t.ex. Administratör, Personal, Monitor, Gäst).
- **Grupp:** Visar den specifika användargruppen eller teamet som personalmedlemmen tillhör.
- **Status:** Anger om kontot för närvarande är **Aktivt** eller **Inaktivt**.
- **Skapat datum:** Tidsstämpeln för när kontot registrerades.

## Personalhanteringsåtgärder

Administratörer har tillgång till en uppsättning verktyg för introduktion och underhåll av användarkonton, tillgängliga från den övre kontrollpanelen:

- **Lägg till personal:** Öppnar ett detaljerat skapelseformulär för att manuellt mata in en ny användares profil, inklusive deras roll, tilldelade regioner och kontaktinformation.
- **Importera personal:** Möjliggör masskontokapande genom att ladda upp ett Excel-kalkylblad. Detta är särskilt användbart för att snabbt etablera stora fältteam.
- **Ladda ned importmall:** Tillhandahåller den standardiserade `.xlsx`-mallen som krävs för massimportprocessen.
- **Exportera till Excel:** Genererar en nedladdningsbar rapport som innehåller den aktuella rutnätets filtrerade lista över användare och deras detaljer.
- **Radera:** Tar permanent bort valda användarkonton från systemet.

## Användarprofiler och tilldelningar

När du skapar eller redigerar en specifik användare (via knappen **Lägg till personal** eller genom att klicka på ett användarnamn) kan administratörer konfigurera detaljerade profiler:

- **Personlig information:** Fält för födelsedatum, kön, identifikationsnummer och avatar.
- **Kontaktuppgifter:** Mobilnummer och detaljerad platsinformation (provins, distrikt, stadsdel, adress).
- **Systemtilldelningar:** Avgörande för datasäkerhet, administratörer kan koppla användare till specifika **regioner** och tilldela exakta **användarroller**.
- **Handledarkonfiguration:** I avancerade konfigurationer kan användare tilldelas specifika handledarkoder eller mappas till specifika surfplattor (enheter).
