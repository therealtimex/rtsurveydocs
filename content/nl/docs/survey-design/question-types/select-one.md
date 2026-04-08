---
title: "Select_one"
description: "Select_one-vragen laten respondenten precies één optie kiezen uit een vooraf gedefinieerde lijst met keuzes."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Het vraagtype `select_one` vraagt de respondent om **precies één optie** te kiezen uit een vooraf gedefinieerde lijst. Standaard worden keuzes weergegeven als keuzerondjes, maar er zijn veel weergaveopties beschikbaar om de indeling en het gedrag te wijzigen.

## Basis XLSForm-specificatie

**survey-werkblad:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Heeft de respondent toestemming gegeven? |

**choices-werkblad:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Ja |
| yesno | no | Nee |

De `lijstnaam` in `select_one lijstnaam` moet overeenkomen met de kolom `list_name` in het choices-werkblad.

## Toepassingen

Select_one-vragen worden gebruikt voor:

1. Ja/Nee-vragen
2. Meerkeuzevragen met één antwoord (bijv. opleidingsniveau, geslacht, burgerlijke staat)
3. Categorische beoordelingen (bijv. slecht / redelijk / goed / uitstekend)
4. Cascaderende (gekoppelde) selecties waarbij keuzes worden gefilterd op basis van een eerder antwoord
5. Land, regio, district of andere administratieve eenheidsselectie

## Weergaveopties

Specificeer een waarde in de kolom `appearance` om te wijzigen hoe keuzes worden weergegeven:

{{< table >}}
| Weergave | Beschrijving |
|----------|-------------|
| *(geen)* | Standaard keuzerondjes, één per regel |
| `minimal` | Enkel dropdown/spinner in plaats van keuzerondjes |
| `quick` | Gaat automatisch naar de volgende vraag na selectie (alleen mobiel) |
| `compact` | Compact raster van keuzes — aantal kolommen past zich aan aan schermbreedte |
| `compact-N` | Compact raster geforceerd naar N kolommen (bijv. `compact-3`) |
| `quickcompact` | Combineert `quick` en `compact` |
| `quickcompact-N` | Combineert `quick` en `compact` met N geforceerde kolommen |
| `horizontal` | Keuzes horizontaal gerangschikt in een rij (web) |
| `horizontal-compact` | Horizontaal, compacte afstand (web) |
| `likert` | Likert-schaalrij — labels erboven, keuzerondjes eronder |
| `label` | Toont alleen keuzelabels zonder invoervelden (gebruik gepaard met `list-nolabel`) |
| `list-nolabel` | Toont alleen invoervelden zonder labels (gebruik gepaard met `label`) |
| `columns(N)` | Weergave in N kolommen (rtSurvey-uitbreiding, bijv. `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emotionele pictogramwidget |
| `search-api(...)` | Dynamisch zoeken — laadt keuzes uit een API bij uitvoering |
| `tagging` | Toont keuzes als klikbare tag-chips in plaats van keuzerondjes |
| `boxtag` | Toont keuzes als gestileerde rechthoekige vakken die de gebruiker aanraakt om te selecteren |
| `boxtag -search` | Boxtag-indeling met een zoek-/filterveld boven de vakken |
| `duolingo-style1` | Duolingo-geïnspireerde kaartindeling — grote aantikbare kaarten met pictogrammen |
| `rating_box` | Op grid gebaseerde beoordelingsvakken — best voor numerieke of schaalgebaseerde keuzes |
| `star_rating` | Sterbeoordelingswidget — keuzes worden weergegeven als 1–N sterren |
| `choices-noshow` | Toont aanvankelijk alleen de eerste 10 keuzes; onthult de rest op aanvraag |
| `noshow` | Verbergt de keuzenlijst volledig; de waarde wordt programmatisch ingesteld |
| `checkall` | Voegt een optie "Alles selecteren" toe bovenaan de lijst |
| `max-items(N)` | Beperkt het aantal zichtbare keuzes tot N (bijv. max-items(5)) |
{{< /table >}}

### Voorbeeld: Likert-schaal

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Hoe tevreden bent u met de dienst? | likert |

### Voorbeeld: Compact 3 kolommen

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Selecteer regio | compact-3 |

## Cascaderende selecties

Een cascaderende (gekoppelde) selectie filtert keuzes op basis van de geselecteerde waarde in een vorige vraag. Gebruik de kolom `choice_filter` met de naam van een kolom uit uw choices-werkblad.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Selecteer provincie | |
| select_one district | district | Selecteer district | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Wanneer de respondent `nairobi` selecteert, verschijnen alleen `Westlands` en `Kasarani` in de districtlijst.

{{% alert icon=" " context="warning" %}}
De kolomnaam die wordt gebruikt in `choice_filter` (bijv. `province_name`) moet bestaan in het choices-werkblad. De `${province}` verwijst naar het surveyveld genaamd `province`.
{{% /alert %}}

## De geselecteerde waarde gebruiken in expressies

Verwijs naar de geselecteerde **waarde** (niet het label) met `${veldnaam}`:

```
relevant: ${consent} = 'yes'
```

Om het keuzelabel te krijgen in plaats van de waarde, gebruikt u `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## "Anders"-optie met vrije tekst

Een veelgebruikt patroon is het opnemen van een "anders"-optie die een tekstveld onthult:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Wat is uw beroep? | |
| text | job_other | Specificeer alstublieft | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Landbouwer |
| occupation | trader | Handelaar |
| occupation | student | Student |
| occupation | other | Anders (specificeer alstublieft) |

## Aanbevolen werkwijzen

1. Houd lijsten kort en wederzijds uitsluitend — als respondenten mogelijk meer dan één willen, gebruik dan `select_multiple`.
2. Zet het meest voorkomende antwoord eerst, of orden alfabetisch voor lange lijsten.
3. Neem altijd een optie "Weet niet" of "Wil liever niet antwoorden" op waar van toepassing.
4. Gebruik `minimal` (dropdown) voor lijsten met meer dan 7–8 keuzes op mobiel om schermruimte te besparen.
5. Voeg voor cascaderende selecties alle filterkolommen toe aan het choices-werkblad voor het bouwen van het formulier.

## Beperkingen

- Een respondent kan slechts één keuze selecteren — gebruik `select_multiple` voor vragen met meerdere antwoorden.
- De weergave `likert` werkt het beste met 5–7 keuzes die op één regel passen.
- `quick` automatisch doorgaan is alleen voor mobiel; het heeft geen effect op webformulieren.
