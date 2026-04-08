---
title: "Select_one"
description: "Select_one-spørsmål lar respondenter velge nøyaktig ett alternativ fra en forhåndsdefinert liste over valg."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

`select_one`-spørsmålstypen ber respondenten om å velge **nøyaktig ett alternativ** fra en forhåndsdefinert liste. Som standard gjengis valg som radioknapper, men et bredt utvalg av utseendealternativer er tilgjengelig for å endre oppsettet og adferden.

## Grunnleggende XLSForm-spesifikasjon

**survey-regneark:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Ga respondenten samtykke? |

**choices-regneark:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Ja |
| yesno | no | Nei |

`listname` i `select_one listname` må samsvare med `list_name`-kolonnen i choices-regnearket.

## Brukstilfeller

Select_one-spørsmål brukes for:

1. Ja/Nei-spørsmål
2. Enkeltsvars flervalg (f.eks. utdanningsnivå, kjønn, sivilstatus)
3. Kategoriske vurderinger (f.eks. dårlig / middels / god / utmerket)
4. Kaskaderende (koblede) select-er der valgene filtreres basert på et tidligere svar
5. Land, region, distrikt eller andre administrative enhetsvalg

## Utseendealternativer

{{< table >}}
| Utseende | Beskrivelse |
|----------|-------------|
| *(ingen)* | Standard radioknapper, én per linje |
| `minimal` | Enkelt nedtrekksmeny/spinner i stedet for radioknapper |
| `quick` | Går automatisk videre til neste spørsmål umiddelbart etter valg (kun mobil) |
| `compact` | Kompakt grid av valg — antall kolonner justeres til skjermbredde |
| `compact-N` | Kompakt grid tvunget til N kolonner (f.eks. `compact-3`) |
| `quickcompact` | Kombinerer `quick` og `compact` |
| `quickcompact-N` | Kombinerer `quick` og `compact` med N tvungne kolonner |
| `horizontal` | Valg arrangert i en horisontal rad (web) |
| `horizontal-compact` | Horisontal, kompakt avstand (web) |
| `likert` | Likert-skalarad — etiketter over, radioknapper under |
| `label` | Viser bare valgetiketter uten inndata (bruk kombinert med `list-nolabel`) |
| `list-nolabel` | Viser bare inndataene uten etiketter (bruk kombinert med `label`) |
| `columns(N)` | Vis i N kolonner (rtSurvey-utvidelse, f.eks. `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emosjonell ikonwidget |
| `search-api(...)` | Dynamisk søk — laster valg fra et API ved kjøretid |
| `tagging` | Viser valg som klikkbare tag-chips i stedet for radioknapper |
| `boxtag` | Viser valg som stiliserte rektangulære bokser som brukeren trykker for å velge |
| `boxtag -search` | Boxtag-oppsett med et søke-/filtreringsfelt over boksene |
| `duolingo-style1` | Duolingo-inspirert kortoppsett — store trykkbare kort med ikoner |
| `rating_box` | Gridbaserte vurderingsbokser — best for numeriske eller skalavalg |
| `star_rating` | Stjernevurderingswidget — valg gjengis som 1–N stjerner |
| `choices-noshow` | Viser bare de første 10 valgene innledningsvis; avslører resten på forespørsel |
| `noshow` | Skjuler valglisten fullstendig; verdi settes programmatisk |
| `checkall` | Legger til et "Velg alle"-alternativ øverst i listen |
| `max-items(N)` | Begrenser antall synlige valg til N (f.eks. max-items(5)) |
{{< /table >}}

### Eksempel: Likert-skala

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Hvor fornøyd er du med tjenesten? | likert |

### Eksempel: Kompakt 3 kolonner

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Velg region | compact-3 |

## Kaskaderende select-er

En kaskaderende (koblet) select filtrerer valg basert på verdien valgt i et foregående spørsmål. Bruk `choice_filter`-kolonnen med navnet på en kolonne fra choices-regnearket.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Velg fylke | |
| select_one district | district | Velg distrikt | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Når respondenten velger `nairobi`, vises bare `Westlands` og `Kasarani` i distriktlisten.

{{% alert icon=" " context="warning" %}}
Kolonnenavnet brukt i `choice_filter` (f.eks. `province_name`) må eksistere i choices-regnearket. `${province}` refererer til survey-feltet kalt `province`.
{{% /alert %}}

## Bruke den valgte verdien i uttrykk

Referer til den valgte **verdien** (ikke etiketten) med `${feltnavn}`:

```
relevant: ${consent} = 'yes'
```

For å få valgetiketten i stedet for verdien, bruk `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## "Annet"-alternativ med fritekst

Et vanlig mønster er å inkludere et "annet"-alternativ som avdekker et tekstfelt:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Hva er yrket ditt? | |
| text | job_other | Vennligst spesifiser | `${job} = 'other'` |

## Beste praksis

1. Hold lister korte og gjensidig utelukkende — hvis respondenter kan ønske mer enn ett, bruk `select_multiple` i stedet.
2. Sett det vanligste svaret først, eller organiser alfabetisk for lange lister.
3. Inkluder alltid et "Vet ikke" eller "Vil ikke svare"-alternativ der det er relevant.
4. Bruk `minimal` (nedtrekksmeny) for lister med mer enn 7–8 valg på mobil for å spare skjermhøyde.
5. For kaskaderende select-er, legg til alle filterkolonner i choices-regnearket før du bygger skjemaet.

## Begrensninger

- En respondent kan bare velge ett alternativ — bruk `select_multiple` for spørsmål med flere svar.
- `likert`-utseendet fungerer best med 5–7 valg som passer på én linje.
- `quick` automatisk-fremgang er kun for mobil; det har ingen effekt på webskjemaer.
