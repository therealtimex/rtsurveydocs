---
title: "Datetime, date, time"
description: "Datetime-spørsmål lar respondenter angi både dato og klokkeslett i ett enkelt felt."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Datetime-spørsmålstypen i XLSForm og rtSurvey lar respondenter angi både dato og klokkeslett i ett enkelt felt. Denne spørsmålstypen er nyttig når du trenger å registrere et spesifikt tidspunkt, inkludert både datoen og det nøyaktige klokkeslettet.

## Grunnleggende XLSForm-spesifikasjon

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Når skjedde hendelsen?          |

## Brukstilfeller

Datetime-spørsmål brukes vanligvis for:

1. Registrere tidsstempler for hendelser eller observasjoner
2. Planlegge avtaler eller møter
3. Logge start- og sluttider for aktiviteter
4. Registrere presise tidspunkter for tidssensitiv datainnsamling

## rtSurvey-utvidelser

rtSurvey utvider funksjonaliteten til datetime-spørsmål med ulike utseender og tilpasningsalternativer:

### Utseendealternativer

- `(standard)`: Vis kalenderen og klokken for valg av dato og klokkeslett
- `inline`: Vis kalenderen og klokken som ikoner
- `inline-1line`: Vis kalenderen og klokken i enkeltradformat
- `inline-onlyresult`: Vis ikonene på slutten av linjen; ikoner forsvinner etter valg

### Fargetilpasning

Du kan tilpasse fargen på kalender- og klokkeikonene ved hjelp av `colors()`-funksjonen:

- `inline colors("0099FF")`: Vis ikoner med tilpasset farge
- `inline-1line-0000FF`: Vis i enkeltradformat med tilpasset farge
- `inline-1line colors("0000FF","FFFF00")`: Vis i enkeltradformat med flere tilpassede farger
- `inline-onlyresult colors("0099FF")`: Vis ikoner som forsvinner etter valg, med tilpasset farge

### Tilpassede dato- og klokkeslettformater

rtSurvey tillater tilpassede dato- og klokkeslettformater ved hjelp av spesiell syntaks:

- `inline-[%Y-%m-%d %H:%M:%S]`: Eksempel på tilpasset format (År-Måned-Dag Time:Minutt:Sekund)
- `inline-[%d/%m/%Y %I:%M %p]`: Eksempel på tilpasset format (Dag/Måned/År Time:Minutt AM/PM)

## Eksempelbruk

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Når skjedde hendelsen?                     | inline-[%d/%m/%Y %I:%M %p]  |

## Beste praksis

1. Gi klare instruksjoner om forventet dato- og klokkeslettformat.
2. Vurder å bruke `inline`-utseendet for en mer kompakt visning.
3. Bruk tilpassede formater når du trenger spesifikke dato- og klokkeslettkomponenter eller formatering.
4. Vær oppmerksom på tidssoner ved innsamling av datetime-data på tvers av ulike regioner.

## Begrensninger

- Noen utseender eller tilpassede formater støttes kanskje ikke på alle enheter eller plattformer.
- Brukere kan trenge veiledning om å angi dato og klokkeslett korrekt, spesielt med tilpassede formater.
- Tidssoneforskjeller kan komplisere dataanalyse hvis de ikke håndteres korrekt.
