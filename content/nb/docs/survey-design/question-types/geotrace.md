---
title: "Geotrace"
description: "Geotrace-spørsmål lar respondenter registrere en serie med tilkoblede punkter på et kart, og lage linjer eller stier som en del av spørreundersøkelsen."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Geotrace-spørsmålstypen i XLSForm og rtSurvey lar respondenter registrere en serie med tilkoblede punkter på et kart, og lage linjer eller stier. Denne funksjonen er særlig nyttig for kartlegging av ruter, grenser eller lineære trekk i romlige undersøkelser.

## Grunnleggende XLSForm-spesifikasjon

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Tegn stien til elven            |

## Brukstilfeller

Geotrace-spørsmål brukes vanligvis for:

1. Kartlegge ruter eller stier tatt under feltundersøkelser
2. Tegne lineære trekk som veier, elver eller grenser
3. Registrere omfanget av lineær infrastruktur (f.eks. rørledninger, kraftlinjer)
4. Registrere reisestier i transportstudier
5. Definere transekter i økologiske undersøkelser

## Beste praksis

1. Sørg for at enheten har plasseringstjenester aktivert og tillatelser gitt.
2. Gi klare instruksjoner om hvordan du tegner stien og hvilke trekk som bør inkluderes.
3. Vurder å bruke satellittbilder eller basekart for å hjelpe respondenter med å tegne nøyaktige stier.
4. Vær oppmerksom på den potensielle kompleksiteten til spor og deres innvirkning på datastørrelse og behandling.

## Eksempelbruk

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Tegn stien til turløypen                   | Start ved startpunktet og avslutt ved toppen |

## Dataformat

Geotrace-data lagres vanligvis som en streng med mellomrom-separerte koordinatpar, lignende geoshape men uten avsluttende punkt:

```
breddegrad1 lengdegrad1; breddegrad2 lengdegrad2; ... breddegradN lengdegradN
```

## Begrensninger

- Å tegne nøyaktige stier på små mobilskjermer kan være utfordrende.
- Komplekse spor kan kreve betydelig lagrings- og behandlingskapasitet.
- Kontinuerlig GPS-bruk for automatisk sporing kan raskt tømme enhetsbatterier.
- Det kan være personvernbekymringer knyttet til innsamling av detaljerte stidata.
