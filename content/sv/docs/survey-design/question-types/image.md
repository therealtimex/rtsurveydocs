---
title: "Bild"
description: "Bildfrågor gör det möjligt för respondenter att ta och skicka in foton som en del av undersökningen."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Frågtypen image i XLSForms och rtSurvey gör det möjligt för respondenter att ta och skicka in foton som en del av sina undersökningssvar. Den här funktionen är särskilt användbar för att samla in visuella data, dokumentera observationer eller ge bevis i fältundersökningar.

## Grundläggande XLSForm-specifikation

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Ta ett foto av platsen         |

För mer detaljer om grundläggande frågtypen image, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Användningsområden

Bildfrågor används vanligtvis för:

1. Dokumentera fältförhållanden eller observationer
2. Fånga visuella bevis i forskningsstudier
3. Samla in före-och-efter-foton i konsekvensutredningar
4. Verifiera slutförandet av uppgifter eller närvaro på platser
5. Samla in visuella data för fjärranalys

## Bästa praxis

1. Ge tydliga instruktioner om vad som ska fotograferas.
2. Tänk på integritetsfrågor och informera respondenter om hur deras foton kommer att användas.
3. Var uppmärksam på filstorlekar och lagringsbegränsningar, särskilt för undersökningar i områden med begränsad internetanslutning.
4. Se till att enheten har tillräckligt med lagringsutrymme och att kamerabehörigheter är beviljade.

## Exempelanvändning

Här är ett exempel på hur du kan använda en bildfråga i en undersökning:

| type  | name           | label                                      | hint                                              |
|-------|----------------|--------------------------------------------|----------------------------------------------------|
| image | storefront     | Ta ett foto av butikens entré              | Se till att butiksnamnet är tydligt synligt        |

## Datahantering

Bilder som samlas in via denna frågtyp:

1. Sparas i ett vanligt bildformat (t.ex. JPG, PNG)
2. Lagras tillsammans med andra undersökningsdata, ofta i en separat mediamapp
3. Är tillgängliga för visning och analys via undersökningshanteringsplattformen

## Begränsningar

- Bildfiler kan vara stora, vilket kan påverka dataöverföring och lagring.
- Inte alla enheter kan ha högkvalitetskameror eller tillräckligt lagringsutrymme.
- Analys av stora mängder bilder kan vara tidskrävande.
- Det kan finnas integritetsfrågor vid tagning av bilder, särskilt på offentliga platser.
