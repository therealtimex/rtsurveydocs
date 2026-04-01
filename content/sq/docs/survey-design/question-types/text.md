---
title: "Text"
description: "Lloji i pyetjes me përgjigje të lirë me tekst në rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Lloji i pyetjes `text` mbledh një përgjigje me tekst të lirë — çdo varg karakteresh. Është lloji më fleksibël i hyrjes dhe përdoret për emra, adresa, përshkrime, kode dhe çdo gjë që nuk i përshtatet një lloji më specifik.

rtSurvey gjithashtu zgjet `text` me **widget-e hyrjeje kohe** që lejojnë hyrje të saktë kohe me zgjedhësin e orës.

## Specifikimi bazë XLSForm

| type | name | label |
|------|------|-------|
| text | respondent_name | Emri i plotë i të anketuarit |
| text | address | Adresa e shtëpisë |

Për më shumë detaje mbi llojin standard XLSForm text, shikoni [specifikimin XLSForm](https://xlsform.org/en/#question-types).

## Përdorimet

Pyetjet me tekst përdoren për:

1. Emra, adresa, përshkrime të lira
2. Komente ose reagime me fund të hapur
3. Kode, ID, ose numra reference që nuk i përshtaten integer/decimal
4. Mbledhjen e vlerave të kohës me zgjerime hyrjeje kohe të rtSurvey
5. Fushat e tekstit me plotësim automatik (nëpërmjet `search-autocomplete-noedit-v2()`)

## Opsionet standarde të pamjes

| Pamja | Përshkrimi |
|-------|------------|
| *(asnjë)* | Hyrje teksti me një rresht |
| `multiline` | Zonë teksti me shumë rreshta — më e mirë për tekst të gjatë të lirë në web |

## Zgjerime hyrjeje kohe të rtSurvey

rtSurvey zgjet `text` me **widget zgjedhësi ore** për mbledhjen e vlerave të kohës. Këto opsione pamjeje shfaqin një ikonë ore që numëruesi mund ta prekë për të zgjedhur orë, minuta, sekonda, ose milisekonda.

### Variantet e pamjes

| Pamja | Përshkrimi |
|-------|------------|
| `inline` | Ikona e orës shfaqur pranë fushës |
| `inline colors("RRGGBB")` | Ikona e orës me ngjyrë hex të personalizuar |
| `inline-1line` | Ora shfaqur në format kompakt me një rresht |
| `inline-1line-RRGGBB` | Rresht i vetëm me ngjyrë ikone të personalizuar (hex, pa `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Rresht i vetëm me dy ngjyra |
| `inline-onlyresult` | Ikona e orës zhduket pas zgjedhjes; shfaqet vetëm vlera |
| `inline-onlyresult colors("RRGGBB")` | E njëjtë, me ngjyrë ikone të personalizuar |

### Argumentet e formatit të kohës

Shtoni një varg formati në kllapa për të kontrolluar se cilat komponente kohe shfaqen:

| Vargu i formatit | Shfaq |
|-----------------|-------|
| `inline-[%H:%M]` | Orët dhe minutat (24-orësh) |
| `inline-[%h:%M]` | Orët dhe minutat (12-orësh) |
| `inline-[%H:%M:%S]` | Orët, minutat, sekondat (24-orësh) |
| `inline-[%h:%M:%S]` | Orët, minutat, sekondat (12-orësh) |
| `inline-[%H:%M:%3]` | Orët, minutat, milisekondat |
| `inline-[%M:%S]` | Minutat dhe sekondat vetëm |
| `inline-[%M:%3]` | Minutat dhe milisekondat vetëm |
| `inline-[%S]` | Sekondat vetëm |
| `inline-[%3]` | Milisekondat vetëm |
| `inline-[%H]` | Orët vetëm (24-orësh) |
| `inline-[%h]` | Orët vetëm (12-orësh) |

### Shembull: Regjistroni kohëzgjatjen e detyrës në minuta dhe sekonda

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Koha e nevojshme për të përfunduar detyrën | `inline-[%M:%S]` |

### Shembull: Regjistroni orën e ngjarjes në format 24-orësh me ngjyrë të personalizuar

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Ora e ngjarjes | `inline-1line colors("0099FF")` |

## Formati i të dhënave

Të dhënat e tekstit ruhen dhe eksportohen si varg i thjeshtë. Për hyrjet bazuar në kohë duke përdorur widget-in e orës inline, vlera ruhet në formatin që përputhet me vargun e formatit të zgjedhur (p.sh., `14:32` për `%H:%M`).

## Kufizimet dhe validimi

Aplikoni kufizime për të zbatuar formatin, gjatësinë, ose modelin:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Emri i plotë | `string-length(.) >= 2` | Emri duhet të ketë të paktën 2 karaktere |
| text | code | Kodi i referencës | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Shkruani 2 shkronja të mëdha të ndjekura nga 4 shifra |
| text | phone | Numri i telefonit | `regex(., '^[0-9]{9,15}$')` | Shkruani një numër telefoni të vlefshëm |

## Praktikat më të mira

1. Përdorni lloje më specifike (`integer`, `decimal`, `date`) sa herë që të dhënat kanë një strukturë të njohur — kjo parandalon hyrjet e pavlefshme dhe thjeshton analizën.
2. Shtoni `constraint` me `string-length()` ose `regex()` për të validuar kodet ose ID-të.
3. Përdorni pamjen `multiline` për pyetjet me fund të hapur ku të anketuarit mund të shkruajnë disa fjali.
4. Për mbledhjen e kohës, zgjidhni argumentet e formatit të kohës që përputhen me saktësinë e kërkuar nga analiza juaj — mbledhja e milisekondave kur ju nevojiten vetëm minutat shpërdoron përpjekjet e numëruesit.

## Mbështetja e platformës

Lloji i pyetjes text dhe të gjitha pamjet e hyrjes kohe mbështeten në platformat iOS, Android dhe web.

## Kufizimet

- Përgjigjet me tekst janë me formë të lirë — nuk ka kontroll drejtshkrimi të integruar ose kufizim të fjalorit përtej modeleve regex.
- Widget-i i orës inline është një zgjerim i rtSurvey dhe nuk është pjesë e specifikimit standard XLSForm.
