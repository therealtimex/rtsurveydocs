---
title: "Note"
description: "Note-spørsmål viser skrivebeskyttet tekst eller medier for å gi informasjon eller instruksjoner i spørreundersøkelsen."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

Note-spørsmålstypen i XLSForm og rtSurvey brukes til å vise skrivebeskyttet tekst eller medier for respondenten. Det er ikke et spørsmål som krever et svar, men snarere en måte å gi informasjon, instruksjoner eller kontekst innenfor spørreundersøkelsen.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label |
|------|------|-------|
| note | info_text | Denne spørreundersøkelsen handler om lesevanene dine. |

## Brukstilfeller

Note-spørsmål brukes vanligvis for:

1. Gi instruksjoner eller kontekst for kommende spørsmål
2. Vise beregnede resultater eller sammendrag
3. Vise bilder eller andre medier
4. Skille seksjoner i en spørreundersøkelse
5. Gi tilbakemelding basert på tidligere svar

## Beste praksis

1. Hold note-teksten kortfattet og klar for å opprettholde respondentengasjementet.
2. Bruk formatering (fet, kursiv) for å fremheve viktig informasjon.
3. Vurder å bruke medier (bilder, lyd) for å forbedre forståelsen der det er hensiktsmessig.
4. Bruk noter sparsomt for å unngå å rote til spørreundersøkelsen.

## Eksempelbruk

| type | name | label |
|------|------|-------|
| note | intro | Velkommen til vår undersøkelse om lesevaner. Vi vil spørre om preferansene og lesefrekvensen din. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | Du leser omtrent ${books_per_month} bøker per måned. |

## Avansert bruk

### Betinget visning

Du kan bruke relevansuttrykk for å vise noter betinget:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | Du er en ivrig leser! | ${books_per_month} > 5 |

### Inkludere beregninger

Noter kan inkludere beregninger for å gi dynamisk tilbakemelding:

| type | name | label |
|------|------|-------|
| note | reading_time | Basert på svarene dine bruker du omtrent ${books_per_month * 5} timer på lesing hver måned. |

## Begrensninger

- Noter samler ikke inn data, så de bør ikke brukes når du trenger å innhente informasjon fra respondenter.
- Overbruk av noter kan gjøre en spørreundersøkelse rotete eller unødvendig lang.
- Noen avanserte formaterings- eller mediealternativer støttes kanskje ikke på alle enheter eller plattformer.
