---
title: "Geotrace"
description: "Geotrace-spørgsmål giver respondenter mulighed for at fange en serie af forbundne punkter på et kort og oprette linjer eller stier som en del af undersøgelsen."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Spørgsmålstypen geotrace i XLSForms og rtSurvey giver respondenter mulighed for at fange en serie af forbundne punkter på et kort og oprette linjer eller stier. Denne funktion er særligt nyttig til kortlægning af ruter, grænser eller lineære træk i rumlige undersøgelser.

## Grundlæggende XLSForm-specifikation

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Spor flodens sti     |

For flere detaljer om den grundlæggende geotrace-spørgsmålstype, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Anvendelser

Geotrace-spørgsmål bruges typisk til:

1. Kortlægning af ruter eller stier taget under feltundersøgelser
2. Sporing af lineære træk som veje, floder eller grænser
3. Fangst af omfanget af lineær infrastruktur (f.eks. rørledninger, elledninger)
4. Registrering af rejsestier i transportstudier
5. Definition af transekter i økologiske undersøgelser

## Bedste praksis

1. Sørg for, at enheden har placeringstjenester aktiveret og tilladelser givet.
2. Giv klare instruktioner om, hvordan stien spores, og hvilke træk der skal inkluderes.
3. Overvej at bruge satellitbilleder eller basiskort for at hjælpe respondenter med at spore stier nøjagtigt.
4. Vær opmærksom på potentiel kompleksitet af spor og dens indvirkning på datastørrelse og behandling.

## Eksempel på brug

Her er et eksempel på, hvordan du kan bruge et geotrace-spørgsmål i en undersøgelse:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Spor vandrestiens sti         | Start ved trailhead og slut ved toppen |

## rtSurvey-udvidelser

Mens den grundlæggende XLSForm-specifikation for geotrace-spørgsmål er enkel, kan rtSurvey tilbyde yderligere funktioner eller tilpasninger:

1. Integration med offline-kort til fjerne områder
2. Muligheder for at angive minimum og maksimum antal punkter for sporet
3. Mulighed for at redigere eller forfine spor efter indledende tegning
4. Understøttelse af automatisk sporing med angivne intervaller under bevægelse

## Dataformat

Geotrace-data gemmes typisk som en streng med mellemrumsadskilte koordinatpar, svarende til geoshape, men uden det lukkende punkt:

```
breddegrad1 længdegrad1; breddegrad2 længdegrad2; breddegrad3 længdegrad3; ... breddegrad_N længdegrad_N
```

## Overvejelser for analyse

Når du bruger geotrace-spørgsmål, bør du overveje:

1. Hvordan de geografiske data vil blive visualiseret og analyseret (f.eks. GIS-software)
2. Det potentielle behov for datarensning eller forenkling af komplekse spor
3. Privatlivs- og databeskyttelsesforanstaltninger til håndtering af detaljerede rumlige data
4. Integration med andre rumlige datakilder til omfattende analyse

## Begrænsninger

- At spore præcise stier på små mobilskærme kan være udfordrende.
- Komplekse spor kan kræve betydelig lager- og behandlingskapacitet.
- Kontinuerlig GPS-brug til automatisk sporing kan hurtigt aflæse enhedens batteri.
- Der kan være privatlivsbekymringer forbundet med indsamling af detaljerede stidata.
