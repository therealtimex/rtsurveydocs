---
title: "Rang"
description: "Rang-vragen laten respondenten een reeks keuzes ordenen op voorkeur of prioriteit."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

Het vraagtype `rank` presenteert een lijst met keuzes die de respondent **in volgorde moet slepen** (of anderszins rangschikken van eerste naar laatste). Het slaat het resultaat op als een door spaties gescheiden lijst van keuzewaarden in de geselecteerde volgorde, met de hoogst geprioriteerde keuze als eerste.

## Basis XLSForm-specificatie

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Rangschik deze gemeenschapsbehoeften van meest naar minst belangrijk |

De keuzes worden gedefinieerd in het **choices-werkblad** net als bij `select_one`:

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Schoon water |
| priorities | health | Gezondheidszorg |
| priorities | education | Onderwijs |
| priorities | roads | Wegen |
| priorities | electricity | Elektriciteit |

## Opgeslagen waardeformaat

De opgeslagen waarde is een **door spaties gescheiden lijst** van keuzewaarden in gerangschikte volgorde (eerste = hoogste prioriteit):

```
water education health roads electricity
```

## Gerangschikte posities extraheren

Gebruik `selected-at()` om de keuze op een specifieke rang te krijgen:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Rang gemeenschapsbehoeften | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` geeft de waarde terug die op de **eerste** plaats is gezet (index 0 = hoogste rang).

## Toepassingen

Rang-vragen worden veelgebruikt voor:

1. **Prioriteitsrangschikking** — gemeenschappen vragen ontwikkelingsbehoeften te rangschikken
2. **Voorkeurordening** — productfuncties, serviceattributen of beleidsopties rangschikken
3. **Processtapordening** — stappen in een proces rangschikken
4. **Top-N selectie** — gecombineerd met `selected-at()` om alleen de top 1, 2 of 3 keuzes te extraheren

## Aanbevolen werkwijzen

1. Houd de lijst kort (3–7 items) — rangschikken wordt cognitief belastend boven 7–8 keuzes.
2. Gebruik duidelijke, wederzijds uitsluitende keuzelabels om verwarring over wat "eerste" betekent te vermijden.
3. Voeg hinttekst toe die de rangschikkingsrichting uitlegt (bijv. "Sleep om te ordenen: eerste = meest belangrijk").
4. Valideer met `count-selected(.) = x` als u moet zorgen dat alle keuzes zijn gerangschikt.

## Beperkingen

- De slepen-om-te-rangschikken-widget vereist een aanraakscherm of muis — het werkt mogelijk niet goed in alleen-toetsenbord-omgevingen.
- Op sommige oudere mobiele clients kan de rangwidget terugvallen op een genummerde invoerinterface.
- U kunt niet gedeeltelijk rangschikken (d.w.z. slechts enkele keuzes rangschikken) — alle keuzes moeten worden geordend.
