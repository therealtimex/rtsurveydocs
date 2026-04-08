---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolonnen `appearance` i rtSurvey giver dig mulighed for at tilpasse den visuelle præsentation og adfærden for spørgsmål i dine undersøgelser. Denne funktion forbedrer brugeroplevelsen og kan markant forbedre effektiviteten af dataindsamlingen. rtSurvey understøtter standard XLSForm-appearance-attributter og udvider dem med yderligere muligheder.

## Standard XLSForm-appearance-attributter

rtSurvey understøtter følgende standard XLSForm-appearance-attributter:

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| multiline | text | Opretter en flerlinjet tekstboks (bedst til webklienter) |
| minimal | select_one, select_multiple | Viser valgmuligheder i en rullemenu |
| quick | select_one | Avancerer automatisk til næste spørgsmål efter valg (kun mobil) |
| no-calendar | date | Undertrykker kalendervisningen (kun mobil) |
| month-year | date | Giver mulighed for valg af kun måned og år |
| year | date | Giver mulighed for valg af kun år |
| horizontal-compact | select_one, select_multiple | Viser valgmuligheder horisontalt (kun web) |
| horizontal | select_one, select_multiple | Viser valgmuligheder horisontalt i kolonner (kun web) |
| likert | select_one | Præsenterer valgmuligheder som en Likert-skala |
| compact | select_one, select_multiple | Viser valgmuligheder side om side med minimal fyld |
| quickcompact | select_one | Kombinerer kompakt visning med automatisk fremrykning (kun mobil) |
| field-list | groups | Viser hele gruppen på én skærm (kun mobil) |
| label | select_one, select_multiple | Viser valglabels uden input |
| list-nolabel | select_one, select_multiple | Viser input uden labels (brug med `label`) |
| table-list | groups | Viser spørgsmål i tabelformat |
| signature | image | Aktiverer signaturoptagelse (kun mobil) |
| draw | image | Giver mulighed for frihåndstegning (kun mobil) |
| map, quick map | select_one, select_one_from_file | Aktiverer valg fra kortfunktioner |

## Bedste praksis ved brug af appearance

1. **Konsistens**: Brug appearance-attributter konsekvent i din undersøgelse for et ensartet udseende.
2. **Mobil vs. web**: Overvej, hvordan appearances gengives på forskellige enheder og platforme.
3. **Ydeevne**: Vær forsigtig med appearance-attributter, der kan sænke formularindlæsningen (f.eks. `table-list` til store grupper).
4. **Brugeroplevelse**: Vælg appearances, der gør dataindtastning nemmere og mere intuitiv for respondenter.
5. **Test**: Test altid din formular på målenheder for at sikre, at appearances fungerer som forventet.

## Avancerede teknikker

### Kombination af appearances

Nogle appearance-attributter kan kombineres til mere komplekse layouts:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Vælg én: | minimal compact |
```

### Dynamiske appearances

rtSurvey giver mulighed for dynamiske appearance-ændringer baseret på formularlogik:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Indtast tid: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobilapp-overvejelser

- Visse appearances (f.eks. `quick`, `signature`) er specifikke for mobilenheder.
- Test grundigt på både Android og iOS for at sikre ensartet adfærd.

## rtSurvey udvidede appearance-attributter

Ud over standard XLSForm-appearances understøtter rtSurvey følgende platformspecifikke muligheder:

### Data- og visningskontrol

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `invisible` | enhver | Skjuler feltet fra visning, mens dets værdi stadig indsamles eller beregnes. |
| `displaytitle` | enhver | Tvinger visning af feltets label/titel, selv når den ellers ville undertrykkes. |
| `autopull` | select_one, select_multiple | Henter automatisk eksterne data til udfyldning af valgmuligheder ved formularindlæsning. |
| `floating_hint` | text, integer, decimal | Viser hintteksten som en flydende label over inputfeltet frem for under det. |
| `calculate-button` | calculate | Tilføjer en synlig knap, der udløser genberegning af feltet efter behov. |

### Layout

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `1screen` | group | Tvinger hele gruppen til at vises på én skærm uanset gruppestørrelse. |
| `columns(n)` | select_one, select_multiple | Viser valgmuligheder i `n` kolonner. Eksempel: `columns(3)` viser tre kolonner med radioknapper. |
| `gridformat<row=R col=C colspan=S align=center>` | enhver | Placerer feltet i et CSS-grid-layout på række `R`, kolonne `C`, og spænder `S` kolonner. |
| `ignore-simplify` | enhver | Instruerer formulargengiveren om at springe automatisk forenkling af dette felts layout over. |
| `required-but-simplify` | enhver | Feltet er påkrævet, men dets layout forenkles stadig af gengiveren (tilsidesætter standardadfærden, hvor påkrævede felter udelukkes fra forenkling). |
| `embed` | enhver | Gengiver feltet i indlejret/inline-visningstilstand, undertrykker den ydre indpakning og labelcontainer — bruges, når et spørgsmål er indlejret i tilpasset HTML. |
| `popup` | select_one, select_multiple | Gengiver valglisten i et popup/modal-overlag i stedet for inline. |
| `auto-hide-empty` | boxtag, select | Skjuler hele spørgsmålswidgetten, når valglisten er tom (f.eks. ingen API-resultater returneret). |
| `text-nolabel` | select_one, select_multiple | Skjuler tekstlabelen for hvert valg og viser kun inputkontrollen. Ligner `list-nolabel`, men anvendes pr. valg frem for som kolonnesplit. |

### Widgets

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `likert` | select_one | Præsenterer valgmuligheder som en Likert-skala-række. |
| `distress` | select_one | Gengiver valgmuligheder som den visuelle Kessler Psychological Distress Scale (K10) widget. |

### Visuelle select-widgets

Disse appearances ændrer hele gengivelsen af select-valglister.

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Valgmuligheder gengives som pilleformede klikbare tag-chips. |
| `boxtag` | select_one, select_multiple | Valgmuligheder gengives som rektangulære stilede bokse, som brugeren trykker på. |
| `boxtag -search` | select_one, select_multiple | Boxtag-layout med et live søge-/filterinput over boksene. |
| `duolingo-style1` | select_one, select_multiple | Stort kortlayout inspireret af Duolingo — velegnet til korte lister med ikoner. |
| `rating_box` | select_one, select_multiple | Grid af klikbare nummererede bokse — velegnet til skala- eller NPS-spørgsmål. |
| `star_rating` | select_one | Valgmuligheder gengives som stjerner; stjerneantallet svarer til antallet af valgmuligheder. |
| `choices-noshow` | select_one, select_multiple | Viser i første omgang kun de første 10 valgmuligheder med en "Vis mere"-kontrol. |
| `noshow` | select_one, select_multiple | Skjuler valglisten helt; værdien angives programmatisk via `calculate` eller API. |
| `checkall` | select_multiple | Tilføjer en "Vælg alle"-genvej øverst på valglisten. |
| `max-items(N)` | select_one, select_multiple | Begrænser den synlige valgliste til N elementer. Eksempel: `max-items(5)`. |

### Visuelle tekst-widgets

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `richtext` | text | Erstatter det almindelige tekstfelt med en teksteditor med formatering (fed, kursiv, lister, links). Gemmer HTML. |
| `typingtest` | text | Skrivetestewidget — labelteksten er passagen; widgetten registrerer det skrevne svar og tidspunktet. |

### Medieudvidelser

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `watermark("udtryk")` | image | Overlejrer et tekstvandmærke på optagne fotos. Argumentet er et XPath-udtryk, der evalueres ved optagelsestidspunktet. Eksempel: `watermark("${id} ${today()}")`. |
| `editable` | image | Muliggør annotering/tegning oven på det optagne foto inden gemning. |

### Inline visningskonfiguration

`display{}`- og `results{}`-modifikatorerne kan tilføjes til `inline`-appearances for at styre ikonjustering og resultatvisning. Disse bruges sammen med `inline`-tidsinputudvidelsen på `text`-felter og med medieoptagewidgets.

#### `display{}`-parametre

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parameter | Værdier | Beskrivelse |
|-----------|---------|-------------|
| Justering | `left`, `right`, `top`, `bottom`, `center` | Position af ikonet i forhold til inputfeltet |
| Størrelse | `small`, `medium`, `large` | Ikonstørrelse (svarer til henholdsvis 2,5 rem, 5 rem, 8 rem) |
| Tilstand | `inline-icon` | Gengiver udløseren som ikon alene (ingen knapkant) |
| Tilstand | `inline-button` | Gengiver udløseren som en fuld knap |

#### `results{}`-parametre

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parameter | Værdier | Beskrivelse |
|-----------|---------|-------------|
| Justering | `left`, `right`, `top`, `bottom`, `center` | Position af resultatværdivisningen |
| `hide(felt)` | ethvert underfeltsnavn | Skjuler en specifik komponent af resultatet (f.eks. `hide(seconds)`) |

### API-integration

| Appearance-attribut | Spørgsmålstyper | Beskrivelse |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Aktiverer API-kaldsintegration for dette felt. |
| `callapi-verify(params)` | text, integer, decimal | Udløser et API-verifikationskald med statiske parametre. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Samme som `callapi-verify`, men med parametre hentet fra andre feltværdier ved kørsel. |

### Inline dato/tid-format

For `date`-, `time`- og `datetime`-felter kan du angive et brugerdefineret visningsformat:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Eksempel:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Begivenhedsdato og -tid | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Fødselsdato | inline-[%d/%m/%Y] |

## Kendte begrænsninger

- Komplekse appearances gengives muligvis ikke identisk på alle platforme.
- Visse avancerede rtSurvey-appearances understøttes muligvis ikke i offline-tilstand.

## Fejlfinding af appearance-problemer

1. **Appearance ikke anvendt**: Kontrollér for stavefejl i appearance-kolonnen.
2. **Inkonsistent gengivelse**: Bekræft kompatibilitet med spørgsmålstypen og platformen.
3. **Ydelsesproblemer**: Overvej at forenkle komplekse appearances, især til store undersøgelser.
