---
title: "Select_one"
description: "Select_one-frågor låter respondenter välja exakt ett alternativ från en fördefinierad lista med alternativ."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Frågtypen `select_one` uppmanar respondenten att välja **exakt ett alternativ** från en fördefinierad lista. Som standard renderas alternativ som radioknappar, men ett brett urval av utseendealternativ är tillgängliga för att ändra layout och beteende.

## Grundläggande XLSForm-specifikation

**survey-kalkylblad:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Gav respondenten sitt samtycke? |

**choices-kalkylblad:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Ja |
| yesno | no | Nej |

`listname` i `select_one listname` måste matcha kolumnen `list_name` i choices-kalkylbladet.

För mer detaljer se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Användningsområden

Select_one-frågor används för:

1. Ja/Nej-frågor
2. Flervalsfrågor med ett svar (t.ex. utbildningsnivå, kön, civilstånd)
3. Kategoriska betyg (t.ex. dålig / godtagbar / bra / utmärkt)
4. Kaskaderande (länkade) val där alternativ filtreras baserat på ett tidigare svar
5. Land, region, distrikt eller andra administrativa enhetsval

## Utseendealternativ

Ange ett värde i kolumnen `appearance` för att ändra hur alternativ visas:

{{< table >}}
| Utseende | Beskrivning |
|----------|-------------|
| *(inget)* | Standard radioknappar, en per rad |
| `minimal` | Enskild rullgardinsmeny/spinner istället för radioknappar |
| `quick` | Avancerar automatiskt till nästa fråga omedelbart efter val (bara mobil) |
| `compact` | Kompakt rutnät med alternativ — antal kolumner anpassas till skärmbredden |
| `compact-N` | Kompakt rutnät tvingat till N kolumner (t.ex. `compact-3`) |
| `quickcompact` | Kombinerar `quick` och `compact` |
| `quickcompact-N` | Kombinerar `quick` och `compact` med N tvingade kolumner |
| `horizontal` | Alternativ arrangerade i en horisontell rad (webb) |
| `horizontal-compact` | Horisontellt, kompakt avstånd (webb) |
| `likert` | Likert-skalrad — etiketter ovanpå, radioknappar nedanför |
| `label` | Visar bara alternativetiketter utan inmatningar (använd ihop med `list-nolabel`) |
| `list-nolabel` | Visar bara inmatningarna utan etiketter (använd ihop med `label`) |
| `columns(N)` | Visa i N kolumner (rtSurvey-tillägg, t.ex. `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emotionell ikonwidget |
| `search-api(...)` | Dynamisk sökning — laddar alternativ från ett API vid körning |
{{< /table >}}

### Exempel: Likert-skala

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Hur nöjd är du med tjänsten? | likert |

### Exempel: Kompakt 3 kolumner

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Välj region | compact-3 |

## Kaskaderande val

Ett kaskaderande (länkat) val filtrerar alternativ baserat på värdet som valts i en tidigare fråga. Använd kolumnen `choice_filter` med namnet på en kolumn från ditt choices-kalkylblad.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Välj provins | |
| select_one district | district | Välj distrikt | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

När respondenten väljer `nairobi` visas bara `Westlands` och `Kasarani` i distriktslistan.

{{% alert icon=" " context="warning" %}}
Kolumnnamnet som används i `choice_filter` (t.ex. `province_name`) måste finnas i choices-kalkylbladet. `${province}` refererar till undersökningsfältet med namnet `province`.
{{% /alert %}}

## Använda det valda värdet i uttryck

Referera till det valda **värdet** (inte etiketten) med `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

För att hämta alternativetiketten istället för värdet, använd `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## "Övrigt"-alternativ med fritext

Ett vanligt mönster är att inkludera ett "övrigt"-alternativ som visar ett textfält:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Vad är ditt yrke? | |
| text | job_other | Vänligen specificera | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Jordbrukare |
| occupation | trader | Handlare |
| occupation | student | Student |
| occupation | other | Övrigt (vänligen specificera) |

## Bästa praxis

1. Håll listorna korta och ömsesidigt uteslutande — om respondenter kan vilja välja mer än ett, använd `select_multiple` istället.
2. Lägg det vanligaste svaret först, eller ordna alfabetiskt för långa listor.
3. Inkludera alltid alternativet "Vet inte" eller "Föredrar att inte svara" där det är relevant.
4. Använd `minimal` (rullgardinsmeny) för listor med mer än 7–8 alternativ på mobil för att spara skärmutrymme.
5. För kaskaderande val, lägg till alla filterkolumner i choices-kalkylbladet innan du bygger formuläret.

## Begränsningar

- En respondent kan bara välja ett alternativ — använd `select_multiple` för flervalsfrågor.
- `likert`-utseendet fungerar bäst med 5–7 alternativ som ryms på en rad.
- `quick` automatisk avancering är bara för mobil; det har ingen effekt i webbformulär.
