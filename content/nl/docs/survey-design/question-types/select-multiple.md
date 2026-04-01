---
title: "Select_multiple"
description: "Select_multiple-vragen laten respondenten één of meer opties kiezen uit een vooraf gedefinieerde lijst."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Het vraagtype `select_multiple` toont een lijst waarbij de respondent **één of meer opties** kan selecteren. Standaard worden keuzes weergegeven als selectievakjes. De opgeslagen waarde is een **door spaties gescheiden lijst** van alle geselecteerde keuzewaarden.

## Basis XLSForm-specificatie

**survey-werkblad:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Welke gewassen verbouwt het huishouden? |

**choices-werkblad:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maïs |
| crops | beans | Bonen |
| crops | rice | Rijst |
| crops | vegetables | Groenten |
| crops | other | Anders |

## Opgeslagen gegevensformaat

De geëxporteerde kolom bevat een door spaties gescheiden lijst van geselecteerde waarden:

```
maize beans vegetables
```

Gebruik de functie `selected()` — niet `=` — bij het testen van select_multiple-waarden in expressies (zie hieronder).

## Toepassingen

Select_multiple-vragen worden gebruikt voor:

1. Het verzamelen van meerdere toepasselijke antwoorden (bijv. inkomstenbronnen, verbouwde gewassen, symptomen)
2. Selectievakjes voor overeenkomstitems (bijv. "Selecteer alles wat van toepassing is")
3. Taal- of vaardigheidsinventarissen
4. Elke vraag waarbij meerdere antwoorden tegelijkertijd geldig zijn

## Weergaveopties

{{< table >}}
| Weergave | Beschrijving |
|----------|-------------|
| *(geen)* | Standaard selectievakjes, één per regel |
| `minimal` | Dropdown meervoudige selectiewidget |
| `compact` | Compact raster, kolommen passen zich aan aan schermbreedte |
| `compact-N` | Compact raster geforceerd naar N kolommen |
| `horizontal` | Keuzes horizontaal in een rij gerangschikt (web) |
| `horizontal-compact` | Horizontaal, compacte afstand (web) |
| `label` | Toont alleen labels, geen selectievakjes (gebruik met `list-nolabel`) |
| `list-nolabel` | Toont alleen selectievakjes, geen labels (gebruik met `label`) |
| `columns(N)` | Weergave in N kolommen (rtSurvey-uitbreiding) |
{{< /table >}}

## `selected()` gebruiken in expressies

Omdat de opgeslagen waarde een door spaties gescheiden tekenreeks is, **moet** u `selected()` gebruiken om te testen of een specifieke keuze is geselecteerd. Het gebruik van `=` werkt niet correct.

### In `relevant`

Toon een vervolgvraag alleen als "other" is geselecteerd:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Welke gewassen worden verbouwd? | |
| text | crops_other | Specificeer andere gewassen | `selected(${crops_grown}, 'other')` |

### In `constraint`

Vereist minimaal 2 keuzes:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Selecteer minimaal 2 problemen |

Beperken tot maximaal 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Selecteer niet meer dan 3 prioriteiten |

## "Geen van de bovenstaande" / exclusieve optie

Een veelgebruikt patroon is om één optie wederzijds exclusief te maken met alle anderen. Gebruik een `constraint` om dit te handhaven:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Selecteer alle aanwezige problemen | `not(selected(., 'none') and count-selected(.) > 1)` | "Geen" kan niet worden geselecteerd met andere opties |

## Selecties tellen en samenvatten

| Functie | Voorbeeld | Resultaat |
|---------|---------|----------|
| `count-selected(veld)` | `count-selected(${crops_grown})` | Aantal geselecteerde keuzes |
| `selected(veld, waarde)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(veld, index)` | `selected-at(${crops_grown}, 0)` | Eerste geselecteerde waarde |
| `choice-label(veld, waarde)` | `choice-label(${crops_grown}, 'maize')` | Label voor een waarde |

## Aanbevolen werkwijzen

1. Gebruik altijd `selected()` in `relevant`, `constraint` en `calculate` — nooit `=` of `!=`.
2. Voeg een beperking toe om het maximale aantal selecties te beperken als het vraagontwerp dit vereist.
3. Neem een optie "Geen" of "Niet van toepassing" op wanneer nul selecties een geldig antwoord is.
4. Gebruik voor lange lijsten (15+ keuzes) `minimal` (meervoudige selectie dropdown) om overmatig scrollen te vermijden.

## Beperkingen

- Select_multiple-waarden kunnen niet direct worden vergeleken met `=`. Gebruik altijd `selected()`.
- De compacte weergave wordt mogelijk niet goed weergegeven voor zeer lange keuzelabels.
- Bij het filteren van keuzes met `choice_filter` is het filteren van toepassing op alle weergegeven keuzes, net als bij `select_one`.
