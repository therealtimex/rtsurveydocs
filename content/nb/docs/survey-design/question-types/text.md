---
title: "Tekst"
description: "Fritekst svar-spørsmålstype i rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

`text`-spørsmålstypen samler inn et fritekstsvar — en hvilken som helst tegnstreng. Det er den mest fleksible inndatatypen og brukes for navn, adresser, beskrivelser, koder og alt som ikke passer i en mer spesifikk type.

rtSurvey utvider også `text` med **tidsinndatawidgets** som gir presis tidsregistrering med en klokkevelger.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label |
|------|------|-------|
| text | respondent_name | Respondentens fulle navn |
| text | address | Hjemmeadresse |

## Brukstilfeller

Tekstspørsmål brukes for:

1. Navn, adresser, frie beskrivelser
2. Åpne kommentarer eller tilbakemeldinger
3. Koder, ID-er eller referansenumre som ikke passer som heltall/desimal
4. Innsamling av tidsverdier med rtSurveys tidsinndatautvidelser
5. Autofullføringsfelt (via `search-autocomplete-noedit-v2()`)

## Standard utseendealternativer

| Utseende | Beskrivelse |
|----------|-------------|
| *(ingen)* | Enkelt-linje tekstinndata |
| `multiline` | Flerlinjet tekstområde — best for lengre fritekst på web |

## rtSurvey tidsinndatautvidelser

rtSurvey utvider `text` med en **klokkevelger-widget** for innsamling av tidsverdier. Disse utseendealternativene viser et klokkekikon som telleren kan trykke for å velge timer, minutter, sekunder eller millisekunder.

### Utseendevarianter

| Utseende | Beskrivelse |
|----------|-------------|
| `inline` | Klokkikon ved siden av feltet |
| `inline colors("RRGGBB")` | Klokkikon med tilpasset hex-farge |
| `inline-1line` | Klokke vist i kompakt enkeltradformat |
| `inline-1line-RRGGBB` | Enkeltrad med tilpasset ikonfarge (hex, uten `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Enkeltrad med to farger |
| `inline-onlyresult` | Klokkikon forsvinner etter valg; bare verdien vises |
| `inline-onlyresult colors("RRGGBB")` | Samme, med tilpasset ikonfarge |

### Tidsformattokener

Legg til en formatstreng i parentes for å kontrollere hvilke tidskomponenter som vises:

| Formatstreng | Viser |
|--------------|-------|
| `inline-[%H:%M]` | Timer og minutter (24-timers) |
| `inline-[%h:%M]` | Timer og minutter (12-timers) |
| `inline-[%H:%M:%S]` | Timer, minutter, sekunder (24-timers) |
| `inline-[%h:%M:%S]` | Timer, minutter, sekunder (12-timers) |
| `inline-[%H:%M:%3]` | Timer, minutter, millisekunder |
| `inline-[%M:%S]` | Minutter og sekunder kun |
| `inline-[%M:%3]` | Minutter og millisekunder kun |
| `inline-[%S]` | Sekunder kun |
| `inline-[%3]` | Millisekunder kun |
| `inline-[%H]` | Timer kun (24-timers) |
| `inline-[%h]` | Timer kun (12-timers) |

### Eksempel: Registrer en oppgavevarighet i minutter og sekunder

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Tid brukt på å fullføre oppgaven | `inline-[%M:%S]` |

### Eksempel: Registrer en hendelsestid i 24-timers format med tilpasset farge

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Tidspunkt for hendelsen | `inline-1line colors("0099FF")` |

## Dataformat

Tekstdata lagres og eksporteres som en vanlig streng. For tidsbaserte inndatatyper som bruker inline klokkevelger-widgeten, lagres verdien i formatet som samsvarer med den valgte formatstrengen (f.eks. `14:32` for `%H:%M`).

## Begrensninger og validering

Bruk begrensninger for å håndheve format, lengde eller mønster:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Fullt navn | `string-length(.) >= 2` | Navn må være minst 2 tegn |
| text | code | Referansekode | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Skriv inn 2 store bokstaver etterfulgt av 4 sifre |
| text | phone | Telefonnummer | `regex(., '^[0-9]{9,15}$')` | Skriv inn et gyldig telefonnummer |

## Beste praksis

1. Bruk mer spesifikke typer (`integer`, `decimal`, `date`) når dataene har en kjent struktur — dette forhindrer ugyldige oppføringer og forenkler analysen.
2. Legg til `constraint` med `string-length()` eller `regex()` for å validere koder eller ID-er.
3. Bruk `multiline`-utseende for åpne spørsmål der respondenter kan skrive flere setninger.
4. For tidsinnsamling, velg tidsformattokener som samsvarer med presisjonen analysen krever.

## Begrensninger

- Tekstsvar er friform — det er ingen innebygd stavekontroll eller vokabularbegrensning utover regex-mønstre.
- Inline tidswidgeten er en rtSurvey-utvidelse og er ikke del av standard XLSForm-spesifikasjonen.
