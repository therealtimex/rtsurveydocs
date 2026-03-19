---
title: "Select_multiple"
description: "Select_multiple-frågor låter respondenter välja ett eller flera alternativ från en fördefinierad lista."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Frågtypen `select_multiple` visar en lista där respondenten kan välja **ett eller flera alternativ**. Som standard renderas alternativ som kryssrutor. Det lagrade värdet är en **mellanslagsseparerad lista** med alla valda alternativvärden.

## Grundläggande XLSForm-specifikation

**survey-kalkylblad:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Vilka grödor odlar hushållet? |

**choices-kalkylblad:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Majs |
| crops | beans | Bönor |
| crops | rice | Ris |
| crops | vegetables | Grönsaker |
| crops | other | Övrigt |

För mer detaljer se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Lagrat dataformat

Den exporterade kolumnen innehåller en mellanslagsseparerad lista med valda värden:

```
maize beans vegetables
```

Använd funktionen `selected()` — inte `=` — när du testar select_multiple-värden i uttryck (se nedan).

## Användningsområden

Select_multiple-frågor används för:

1. Samla in flera tillämpliga svar (t.ex. inkomstkällor, odlade grödor, symptom)
2. Kryssruteliknande samtyckeobjekt (t.ex. "Välj alla som gäller")
3. Språk- eller kompetensförteckningar
4. Alla frågor där flera svar är simultant giltiga

## Utseendealternativ

{{< table >}}
| Utseende | Beskrivning |
|----------|-------------|
| *(inget)* | Standard kryssrutor, en per rad |
| `minimal` | Rullgardinsmeny med flerval |
| `compact` | Kompakt rutnät, kolumner anpassas till skärmbredden |
| `compact-N` | Kompakt rutnät tvingat till N kolumner |
| `horizontal` | Alternativ arrangerade horisontellt i en rad (webb) |
| `horizontal-compact` | Horisontellt, kompakt avstånd (webb) |
| `label` | Visar bara etiketter, inga kryssrutor (använd med `list-nolabel`) |
| `list-nolabel` | Visar bara kryssrutor, inga etiketter (använd med `label`) |
| `columns(N)` | Visa i N kolumner (rtSurvey-tillägg) |
{{< /table >}}

### Exempel: 3-kolumns kompakt layout

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Välj alla observerade symptom | compact-3 |

## Använda `selected()` i uttryck

Eftersom det lagrade värdet är en mellanslagsseparerad sträng **måste** du använda `selected()` för att testa om ett specifikt alternativ valdes. Att använda `=` fungerar inte korrekt.

### I `relevant`

Visa en uppföljningsfråga bara om "other" valdes:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Vilka grödor odlas? | |
| text | crops_other | Vänligen ange andra grödor | `selected(${crops_grown}, 'other')` |

### I `constraint`

Kräv minst 2 val:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Välj minst 2 problem |

Begränsa till maximalt 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Välj högst 3 prioriteringar |

## "Inget av ovanstående" / exklusivt alternativ

Ett vanligt mönster är att göra ett alternativ ömsesidigt uteslutande med alla andra. Använd ett `constraint` för att tillämpa det:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Välj alla problem som finns | `not(selected(., 'none') and count-selected(.) > 1)` | "Inga" kan inte väljas tillsammans med andra alternativ |

## Räkna och sammanfatta val

| Funktion | Exempel | Resultat |
|----------|---------|---------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Antal valda alternativ |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Första valda värdet |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Etikett för ett värde |

## Bästa praxis

1. Använd alltid `selected()` i `relevant`, `constraint` och `calculate` — aldrig `=` eller `!=`.
2. Lägg till ett constraint för att begränsa det maximala antalet val om frågans design kräver det.
3. Inkludera alternativet "Inget" eller "Ej tillämpligt" när noll val är ett giltigt svar.
4. För långa listor (15+ alternativ), använd `minimal` (rullgardinsmeny med flerval) för att undvika alltför mycket scrollning.
5. Exportera data och använd strängdelning i ditt analysverktyg — det mellanslagsseparerade formatet kräver delning innan pivotering.

## Begränsningar

- Select_multiple-värden kan inte jämföras direkt med `=`. Använd alltid `selected()`.
- Det kompakta utseendet kanske inte renderas bra för mycket långa alternativetiketter.
- Vid filtrering av alternativ med `choice_filter` gäller filtreringen alla visade alternativ, precis som för `select_one`.
