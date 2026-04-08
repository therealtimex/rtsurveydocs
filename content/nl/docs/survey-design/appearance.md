---
title: "Weergave"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

De `appearance`-kolom in rtSurvey stelt u in staat de visuele presentatie en het gedrag van vragen in uw enquêtes aan te passen. Deze functie verbetert de gebruikerservaring en kan de efficiëntie van gegevensverzameling aanzienlijk verbeteren. rtSurvey ondersteunt standaard XLSForm-weergaveattributen en breidt ze uit met aanvullende opties.

## Standaard XLSForm-weergaveattributen

rtSurvey ondersteunt de volgende standaard XLSForm-weergaveattributen:

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| multiline | text | Maakt een tekstgebied met meerdere regels aan (het beste voor webclients) |
| minimal | select_one, select_multiple | Toont keuzes in een vervolgkeuzemenu |
| quick | select_one | Gaat automatisch naar de volgende vraag na selectie (alleen mobiel) |
| no-calendar | date | Onderdrukt de kalenderweergave (alleen mobiel) |
| month-year | date | Maakt selectie van alleen maand en jaar mogelijk |
| year | date | Maakt selectie van alleen jaar mogelijk |
| horizontal-compact | select_one, select_multiple | Toont keuzes horizontaal (alleen web) |
| horizontal | select_one, select_multiple | Toont keuzes horizontaal in kolommen (alleen web) |
| likert | select_one | Presenteert keuzes als een Likert-schaal |
| compact | select_one, select_multiple | Toont keuzes naast elkaar met minimale opvulling |
| quickcompact | select_one | Combineert compacte weergave met automatisch doorgaan (alleen mobiel) |
| field-list | groups | Toont de gehele groep op één scherm (alleen mobiel) |
| label | select_one, select_multiple | Toont keuzelabels zonder invoervelden |
| list-nolabel | select_one, select_multiple | Toont invoervelden zonder labels (gebruik met `label`) |
| table-list | groups | Toont vragen in een tabelindeling |
| signature | image | Schakelt handtekeningregistratie in (alleen mobiel) |
| draw | image | Maakt vrij tekenen mogelijk (alleen mobiel) |
| map, quick map | select_one, select_one_from_file | Maakt selectie van kaartfuncties mogelijk |

## Aanbevolen werkwijzen voor het gebruik van Weergave

1. **Consistentie**: Gebruik weergaveattributen consistent door uw enquête voor een uniforme uitstraling.
2. **Mobiel vs. Web**: Overweeg hoe weergaven worden weergegeven op verschillende apparaten en platforms.
3. **Prestaties**: Wees voorzichtig met weergaveattributen die het laden van formulieren kunnen vertragen (bijv. `table-list` voor grote groepen).
4. **Gebruikerservaring**: Kies weergaven die gegevensinvoer gemakkelijker en intuïtiever maken voor respondenten.
5. **Testen**: Test uw formulier altijd op doelappara ten om te controleren of weergaven werken zoals verwacht.

## Geavanceerde technieken

### Weergaven combineren

Sommige weergaveattributen kunnen worden gecombineerd voor complexere indelingen:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Selecteer één: | minimal compact |
```

### Dynamische weergaven

rtSurvey maakt dynamische weergavewijzigingen mogelijk op basis van formulierlogica:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Voer tijd in: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Overwegingen voor de mobiele app

- Sommige weergaven (bijv. `quick`, `signature`) zijn specifiek voor mobiele apparaten.
- Test grondig op zowel Android als iOS om consistent gedrag te waarborgen.

## Uitgebreide rtSurvey-weergaveattributen

Naast standaard XLSForm-weergaven ondersteunt rtSurvey de volgende platformspecifieke opties:

### Gegevens- en weergavecontrole

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `invisible` | elk | Verbergt het veld voor de weergave terwijl de waarde nog steeds wordt verzameld of berekend. Anders dan het `hidden`-type — het veld neemt nog steeds deel aan logica. |
| `displaytitle` | elk | Dwingt de weergave van het label/de titel van het veld, zelfs wanneer het anders zou worden onderdrukt. |
| `autopull` | select_one, select_multiple | Haalt automatisch externe gegevens op om keuzes te vullen wanneer het formulier laadt of een triggerveld verandert. |
| `floating_hint` | text, integer, decimal | Toont de hinttekst als een zwevend label boven het invoerveld in plaats van eronder. |
| `calculate-button` | calculate | Voegt een zichtbare knop toe die herberekening van het veld op aanvraag triggert, in plaats van automatisch te berekenen. |

### Indeling

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `1screen` | group | Dwingt de gehele groep om op één scherm te worden weergegeven, ongeacht de groepsgrootte. |
| `columns(n)` | select_one, select_multiple | Toont keuzes in `n` kolommen. Voorbeeld: `columns(3)` toont drie kolommen keuzerondjes. |
| `gridformat<row=R col=C colspan=S align=center>` | elk | Plaatst het veld in een CSS-rasterindeling op rij `R`, kolom `C`, met `S` kolommen spanning. Gebruikt met `advanced-extension/grid-layout`. |
| `ignore-simplify` | elk | Instrueert de formulierweergave om automatische vereenvoudiging of condensering van de indeling van dit veld over te slaan. |
| `required-but-simplify` | elk | Veld is verplicht maar de indeling wordt toch vereenvoudigd |
| `embed` | elk | Geeft het veld weer in ingesloten/inline weergavemodus |
| `popup` | select_one, select_multiple | Geeft de keuzenlijst weer in een popup/modaal overlay |
| `auto-hide-empty` | boxtag, select | Verbergt de widget wanneer de keuzenlijst leeg is |
| `text-nolabel` | select_one, select_multiple | Verbergt het tekstlabel voor elke keuze |

### Widgets

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `likert` | select_one | Presenteert keuzes als een Likert-schaalrij (al in de standaardtabel; bevestigd ondersteund). |
| `distress` | select_one | Geeft keuzes weer als de Kessler Psychological Distress Scale (K10) visuele widget met emotionele iconen. |

### Visuele selectiewidgets

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Toont keuzes als klikbare tag-chips in plaats van keuzerondjes of selectievakjes |
| `boxtag` | select_one, select_multiple | Toont keuzes als gestileerde rechthoekige vakken die de gebruiker aanraakt om te selecteren |
| `boxtag -search` | select_one, select_multiple | Boxtag-indeling met een zoek-/filterveld boven de vakken |
| `duolingo-style1` | select_one, select_multiple | Duolingo-geïnspireerde kaartindeling — grote aantikbare kaarten met pictogrammen |
| `rating_box` | select_one | Op grid gebaseerde beoordelingsvakken — best voor numerieke of schaalgebaseerde keuzes |
| `star_rating` | select_one | Sterbeoordelingswidget — keuzes worden weergegeven als 1–N sterren |
| `choices-noshow` | select_one, select_multiple | Toont aanvankelijk alleen de eerste 10 keuzes; onthult de rest op aanvraag |
| `noshow` | select_one | Verbergt de keuzenlijst volledig; de waarde wordt programmatisch ingesteld |
| `checkall` | select_multiple | Voegt een optie "Alles selecteren" toe bovenaan de lijst |
| `max-items(N)` | select_one, select_multiple | Beperkt het aantal zichtbare keuzes tot N (bijv. max-items(5)) |

### Visuele tekstwidgets

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `richtext` | text | RTF-editor — werkbalk met vet, cursief, lijsten en koppelingen |
| `typingtest` | text | Typtestinterface — toont een passage en meet typsnelheid en nauwkeurigheid |

### Media-uitbreidingen

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `watermark("expr")` | image | Plaatst een tekstwatermerk over de gemaakte foto; het argument is een XPath-expressie die bij vastleggen wordt geëvalueerd |
| `editable` | image | Stelt de respondent in staat om de gemaakte foto te annoteren of op te tekenen |

### Inline weergaveconfiguratie

Gebruik `display{}` om te bepalen hoe de waarde van een veld inline in een label of notitie wordt weergegeven. Gebruik `results{}` om het resultatensamenvattingsscherm na indiening te bepalen.

| Syntaxis | Vraagtypen | Beschrijving |
|----------|----------------|-------------|
| `display{format="..."}` | elk | Formatteert de veldwaarde wanneer deze inline in een label via `${fieldname}` wordt ingevoegd |
| `results{show="true"}` | elk | Toont de veldwaarde in de resultatensamenvattingsweergave na indiening |

### API-integratie

| Weergaveattribuut | Vraagtypen | Beschrijving |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Schakelt API-aanroepintegratie in voor dit veld. De berekeningskolom moet een `callapi()`-expressie bevatten. Zie [API aanroepen](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Triggert een API-verificatieaanroep met statische parameters. Het formulier blokkeert voortgang totdat de API de waarde bevestigt. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Hetzelfde als `callapi-verify` maar met parameters die worden afgeleid van andere veldwaarden tijdens runtime. |

### Inline datum/tijdnotatie

Voor `date`-, `time`- en `datetime`-velden kunt u een aangepaste weergavenotatie opgeven met een notatiereeks toegevoegd aan de weergave:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Notatietokens zijn hetzelfde als `format-date()` en `format-date-time()`. Zie [Functies — Datum- en tijdfuncties](operators-and-functions/functions#date-and-time-functions).

Voorbeeld:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Datum en tijd van het evenement | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Geboortedatum | inline-[%d/%m/%Y] |

## Bekende beperkingen

- Complexe weergaven worden mogelijk niet identiek weergegeven op alle platforms.
- Sommige geavanceerde rtSurvey-weergaven worden mogelijk niet ondersteund in de offlinemodus.

## Weergaveproblemen oplossen

1. **Weergave niet toegepast**: Controleer op typfouten in de weergavekolom.
2. **Inconsistente weergave**: Verifieer compatibiliteit met het vraagtype en het platform.
3. **Prestatieproblemen**: Overweeg het vereenvoudigen van complexe weergaven, met name voor grote enquêtes.
