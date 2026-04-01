---
title: "Område"
description: "Områdespørsmål lar respondenter velge et tall ved å dra en glidebryter mellom en definert minimum- og maksimumsverdi."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

`range`-spørsmålstypen viser en **glidebryter** (eller tilsvarende inndata) som lar respondenter velge et tall innenfor et definert minimum og maksimum. Det er ideelt for å samle inn vurderinger, tilfredsstillelsespoeng eller et numerisk verdi der du ønsker å begrense området visuelt snarere enn å stole på en tekstinndata med begrensninger.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Hvor fornøyd er du med tjenesten? | start=1 end=5 step=1 |

`parameters`-kolonnen definerer glidebryteres grenser og trinnstørrelse:

| Parameter | Beskrivelse | Standard |
|-----------|-------------|---------|
| `start` | Minimumsverdi (inkludert) | 0 |
| `end` | Maksimumsverdi (inkludert) | 10 |
| `step` | Inkrement mellom gyldige verdier | 1 |

## Brukstilfeller

Områdespørsmål brukes vanligvis for:

1. Tilfredsstillelses- eller vurderingsskalaer (f.eks. 1–5 eller 0–10)
2. Likert-stil numeriske skalaer
3. Innsamling av målinger der bare diskrete verdier er gyldige
4. Aldersbraketter eller poengsumområder der en glidebryter forbedrer brukervennligheten over et tekstfelt

## Eksempelbruk

### Grunnleggende vurderingsskala

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Totalvurdering (0–10) | start=0 end=10 step=1 |

### Desimaltrinn

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Vekt (kg) | start=0 end=200 step=0.5 |

### Bruke verdien i en beregning

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Testpoengsum (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Karakteren din er: ${grade} | | |

## Beste praksis

1. Angi alltid meningsfulle `start`-, `end`- og `step`-verdier — ikke stol på standardverdiene.
2. Merk endene av skalaen i `hint`-kolonnen (f.eks. `hint: 0 = Svært misfornøyd, 10 = Svært fornøyd`) for å gi respondentene kontekst.
3. For 5-punkts Likert-skalaer, bruk `start=1 end=5 step=1` snarere enn 0–4, siden respondentene forventer at "1" betyr det laveste.
4. Bruk `range` i stedet for `integer` + begrensning når den avgrensede naturen til inndataene er del av spørsmålsdesignet.

## Begrensninger

- Glidebryter-widgeten er kanskje ikke ideell for svært brede områder (f.eks. 0–10000) — en tekst `integer` med begrensninger er mer brukervennlig i slike tilfeller.
- På mobile enheter kan fine trinnverdier (f.eks. `step=0.1`) være vanskelige å kontrollere presist med en berøringsglidebryter.
