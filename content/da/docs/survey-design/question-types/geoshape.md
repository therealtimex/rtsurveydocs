---
title: "Geoshape"
description: "Geoshape-spørgsmål giver respondenter mulighed for at tegne former på et kort og fange komplekse geografiske data som en del af undersøgelsen."
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

Spørgsmålstypen geoshape i XLSForms og rtSurvey giver respondenter mulighed for at tegne former (polygoner) på et kort og fange komplekse geografiske data. Denne funktion er særligt nyttig til kortlægning af arealer, definition af grænser eller markering af interesseregioner i rumlige undersøgelser.

## Grundlæggende XLSForm-specifikation

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Tegn grænsen for feltet  |

For flere detaljer om den grundlæggende geoshape-spørgsmålstype, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Anvendelser

Geoshape-spørgsmål bruges typisk til:

1. Kortlægning af feltgrænser i landbrugsundersøgelser
2. Definition af miljøpåvirkningsområder
3. Markering af zoner i byplanlægningsstudier
4. Afgrænsning af regioner i geologiske undersøgelser
5. Fangst af komplekse geografiske træk til rumlig analyse

## Bedste praksis

1. Sørg for, at enheden har placeringstjenester aktiveret og tilladelser givet.
2. Giv klare instruktioner om, hvordan formen tegnes, og hvilket område der skal inkluderes.
3. Overvej at bruge satellitbilleder eller basiskort for at hjælpe respondenter med at tegne nøjagtige former.
4. Vær opmærksom på potentiel kompleksitet af former og dens indvirkning på datastørrelse og behandling.

## Eksempel på brug

Her er et eksempel på, hvordan du kan bruge et geoshape-spørgsmål i en undersøgelse:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Oprid grænsen for skovstykket   | Brug mindst 3 punkter til at oprette en lukket form |

## rtSurvey-udvidelser

Mens den grundlæggende XLSForm-specifikation for geoshape-spørgsmål er enkel, kan rtSurvey tilbyde yderligere funktioner eller tilpasninger:

1. Integration med offline-kort til fjerne områder
2. Muligheder for at angive minimum og maksimum antal punkter for formen
3. Mulighed for at redigere eller forfine former efter indledende tegning
4. Understøttelse af forskellige formtyper (f.eks. rektangler, cirkler) ud over frihåndspolygoner

## Dataformat

Geoshape-data gemmes typisk som en streng med mellemrumsadskilte koordinatpar, omsluttet af parenteser:

```
(breddegrad1 længdegrad1; breddegrad2 længdegrad2; breddegrad3 længdegrad3; ... breddegrad_N længdegrad_N)
```

## Overvejelser for analyse

Når du bruger geoshape-spørgsmål, bør du overveje:

1. Hvordan de geografiske data vil blive visualiseret og analyseret (f.eks. GIS-software)
2. Det potentielle behov for datarensning eller forenkling af komplekse former
3. Privatlivs- og databeskyttelsesforanstaltninger til håndtering af detaljerede rumlige data
4. Integration med andre rumlige datakilder til omfattende analyse

## Begrænsninger

- At tegne præcise former på små mobilskærme kan være udfordrende.
- Komplekse former kan kræve betydelig lager- og behandlingskapacitet.
- Geoshape-spørgsmål er muligvis ikke egnede til alle typer undersøgelser eller respondenter.
- Der kan være privatlivsbekymringer forbundet med indsamling af detaljerede rumlige data.
