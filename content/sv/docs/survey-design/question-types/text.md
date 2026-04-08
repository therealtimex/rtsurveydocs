---
title: "Text"
description: "Fritextsvar frågtyp i rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Frågtypen `text` samlar in ett fritextsvar — valfri teckensträng. Det är den mest flexibla inmatningstypen och används för namn, adresser, beskrivningar, koder och allt som inte passar en mer specifik typ.

rtSurvey utökar också `text` med **tidsinmatningswidgets** som möjliggör exakt tidsinmatning med en klockväljare.

## Grundläggande XLSForm-specifikation

| type | name | label |
|------|------|-------|
| text | respondent_name | Respondentens fullständiga namn |
| text | address | Hemadress |

För mer detaljer om standardfrågtypen text i XLSForm, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Användningsområden

Textfrågor används för:

1. Namn, adresser, fria beskrivningar
2. Öppna kommentarer eller återkoppling
3. Koder, ID:n eller referensnummer som inte passar integer/decimal
4. Samla in tidsvärden med rtSurves tidsinmatningstillägg
5. Autokompletteringstextfält (via `search-autocomplete-noedit-v2()`)

## Standardutseendealternativ

| Utseende | Beskrivning |
|----------|-------------|
| *(inget)* | Enrads textinmatning |
| `multiline` | Flerrads textområde — bäst för längre fritext på webben |
| `richtext` | Ersätter det vanliga textfältet med en riktexteditor (fetstil, kursiv, listor, länkar). Lagrar HTML |
| `typingtest` | Skrivtestwidget — etikettexten är passagen; widgetten registrerar det skrivna svaret och tidtagningen |

## rtSurvey-tidsinmatningstillägg

rtSurvey utökar `text` med en **klockväljare-widget** för att samla in tidsvärden. Dessa utseendealternativ visar en klockikon som räknaren kan trycka på för att välja timmar, minuter, sekunder eller millisekunder.

### Utseendevarianter

| Utseende | Beskrivning |
|----------|-------------|
| `inline` | Klockikon visas bredvid fältet |
| `inline colors("RRGGBB")` | Klockikon med anpassad hexfärg |
| `inline-1line` | Klocka visad i ett kompakt enkelradsformat |
| `inline-1line-RRGGBB` | Enkelrad med anpassad ikonfärg (hex, utan `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Enkelrad med två färger |
| `inline-onlyresult` | Klockikon försvinner efter val; bara värdet visas |
| `inline-onlyresult colors("RRGGBB")` | Detsamma, med anpassad ikonfärg |

### Tidsformattoken

Lägg till en formatsträng inom hakparentes för att styra vilka tidskomponenter som visas:

| Formatsträng | Visar |
|--------------|-------|
| `inline-[%H:%M]` | Timmar och minuter (24-timmars) |
| `inline-[%h:%M]` | Timmar och minuter (12-timmars) |
| `inline-[%H:%M:%S]` | Timmar, minuter, sekunder (24-timmars) |
| `inline-[%h:%M:%S]` | Timmar, minuter, sekunder (12-timmars) |
| `inline-[%H:%M:%3]` | Timmar, minuter, millisekunder |
| `inline-[%M:%S]` | Minuter och sekunder endast |
| `inline-[%M:%3]` | Minuter och millisekunder endast |
| `inline-[%S]` | Sekunder endast |
| `inline-[%3]` | Millisekunder endast |
| `inline-[%H]` | Timmar endast (24-timmars) |
| `inline-[%h]` | Timmar endast (12-timmars) |

### Exempel: Registrera en uppgiftslängd i minuter och sekunder

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Tid det tog att slutföra uppgiften | `inline-[%M:%S]` |

### Exempel: Registrera en händelsetid i 24-timmarsformat med anpassad färg

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Tid för händelsen | `inline-1line colors("0099FF")` |

## Dataformat

Textdata lagras och exporteras som en vanlig sträng. För tidsbaserade inmatningar med inline-klockwidgeten lagras värdet i det format som matchar den valda formatsträngen (t.ex. `14:32` för `%H:%M`).

## Begränsningar och validering

Tillämpa begränsningar för att kontrollera format, längd eller mönster:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Fullständigt namn | `string-length(.) >= 2` | Namn måste vara minst 2 tecken |
| text | code | Referenskod | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Ange 2 versaler följt av 4 siffror |
| text | phone | Telefonnummer | `regex(., '^[0-9]{9,15}$')` | Ange ett giltigt telefonnummer |

## Bästa praxis

1. Använd mer specifika typer (`integer`, `decimal`, `date`) när data har en känd struktur — detta förhindrar ogiltiga poster och förenklar analysen.
2. Lägg till `constraint` med `string-length()` eller `regex()` för att validera koder eller ID:n.
3. Använd `multiline`-utseende för öppna frågor där respondenter kan skriva flera meningar.
4. För tidsinsamling, välj de tidsformattoken som matchar den precision din analys kräver.

## Plattformsstöd

Frågtypen text och alla tidsinmatningsutseenden stöds på iOS, Android och webbplattformar.

## Begränsningar

- Textsvar är i friformat — det finns ingen inbyggd stavningskontroll eller ordförrådsbegränsning utöver regex-mönster.
- Inline-tidswidgeten är ett rtSurvey-tillägg och är inte en del av standardspecifikationen för XLSForm.
