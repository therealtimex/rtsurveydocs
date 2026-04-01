---
title: "Geoshape"
description: "Geoshape-spørsmål lar respondenter tegne former på et kart, og registrere komplekse geografiske data som en del av spørreundersøkelsen."
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

Geoshape-spørsmålstypen i XLSForm og rtSurvey lar respondenter tegne former (polygoner) på et kart, og registrere komplekse geografiske data. Denne funksjonen er særlig nyttig for kartlegging av områder, definering av grenser eller markering av interesseregioner i romlige undersøkelser.

## Grunnleggende XLSForm-spesifikasjon

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Tegn grensen til åkeren        |

## Brukstilfeller

Geoshape-spørsmål brukes vanligvis for:

1. Kartlegge åkergrenser i landbruksundersøkelser
2. Definere områder med miljøpåvirkning
3. Markere soner i byplanleggingsstudier
4. Avgrense regioner for geologiske undersøkelser
5. Registrere komplekse geografiske trekk for romlig analyse

## Beste praksis

1. Sørg for at enheten har plasseringstjenester aktivert og tillatelser gitt.
2. Gi klare instruksjoner om hvordan du tegner formen og hvilket område som bør inkluderes.
3. Vurder å bruke satellittbilder eller basekart for å hjelpe respondenter med å tegne nøyaktige former.
4. Vær oppmerksom på den potensielle kompleksiteten til former og deres innvirkning på datastørrelse og behandling.

## Eksempelbruk

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Tegn grensen til skogsflaten               | Bruk minst 3 punkter for å lage en lukket form |

## Dataformat

Geoshape-data lagres vanligvis som en streng med mellomrom-separerte koordinatpar:

```
(breddegrad1 lengdegrad1; breddegrad2 lengdegrad2; ... breddegradN lengdegradN)
```

## Begrensninger

- Å tegne nøyaktige former på små mobilskjermer kan være utfordrende.
- Komplekse former kan kreve betydelig lagrings- og behandlingskapasitet.
- Geoshape-spørsmål er kanskje ikke egnet for alle typer undersøkelser eller respondenter.
- Det kan være personvernbekymringer knyttet til innsamling av detaljerte romlige data.
