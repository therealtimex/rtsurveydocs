---
title: "Billede"
description: "Billedspørgsmål giver respondenter mulighed for at optage og indsende fotos som en del af undersøgelsen."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Spørgsmålstypen image i XLSForms og rtSurvey giver respondenter mulighed for at optage og indsende fotos som en del af deres undersøgelsessvar. Denne funktion er særligt nyttig til at indsamle visuelle data, dokumentere observationer eller levere beviser i feltundersøgelser.

## Grundlæggende XLSForm-specifikation

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Tag et foto af stedet    |

For flere detaljer om den grundlæggende billedspørgsmålstype, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Anvendelser

Billedspørgsmål bruges typisk til:

1. Dokumentering af feltforhold eller observationer
2. Fangst af visuelt bevis i forskningsstudier
3. Indsamling af før-og-efter-billeder i konsekvensvurderinger
4. Verificering af gennemførelse af opgaver eller tilstedeværelse på placeringer
5. Indsamling af visuelle data til fjernanalyse

## Bedste praksis

1. Giv klare instruktioner om, hvad der skal fotograferes.
2. Overvej privatlivsimplikationer og informér respondenter om, hvordan deres fotos vil blive brugt.
3. Vær opmærksom på filstørrelser og lagerbegrænsninger, især til undersøgelser i områder med begrænset internetforbindelseskvalitet.
4. Sørg for, at enheden har tilstrækkelig lagerplads og kameratilladelser er givet.

## Eksempel på brug

Her er et eksempel på, hvordan du kan bruge et billedspørgsmål i en undersøgelse:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Tag et foto af butikkens indgang       | Sørg for, at butiksnavnet er tydeligt synligt    |

## rtSurvey-udvidelser

Mens den grundlæggende XLSForm-specifikation for billedspørgsmål er enkel, kan rtSurvey tilbyde yderligere funktioner eller tilpasninger:

1. Billedkvalitetsindstillinger (f.eks. lav, mellem, høj opløsning)
2. Mulighed for at tilføje billedtekster eller tags til billeder
3. Flerfoldig billedoptagelse til ét spørgsmål
4. Integration med enhedens native kameraapp eller galleri

Se [Avancerede billeder](../advanced-extension/images) for vandmærkning og mediagrid-funktioner.

## Datahåndtering

Billeder indsamlet via denne spørgsmålstype er typisk:

1. Gemt i et almindeligt billedformat (f.eks. JPG, PNG)
2. Gemt ved siden af andre undersøgelsesdata, ofte i en separat mediemappe
3. Tilgængeligt for visning og analyse via undersøgelseshåndteringsplatformen

## Overvejelser for analyse

Når du bruger billedspørgsmål, bør du overveje:

1. Hvordan billederne vil blive analyseret (f.eks. manuel gennemgang, automatiseret billedanalyse)
2. Den yderligere lagerplads der kræves til billedfiler
3. Privatlivs- og databeskyttelsesforanstaltninger til lagring og håndtering af fotos
4. Potentielt behov for billedredigerings- eller organiseringsværktøjer i analysefasen

## rtSurvey appearance-udvidelser

rtSurvey udvider `image`-typen med to yderligere appearance-muligheder:

| Appearance | Beskrivelse |
|------------|-------------|
| `watermark("udtryk")` | Overlejrer et tekstvandmærke på optagne fotos. Argumentet er et XPath-udtryk, der evalueres ved optagelsestidspunktet. Eksempel: `watermark("${id} ${today()}")` |
| `editable` | Muliggør annotering/tegning oven på det optagne foto inden gemning |

### Eksempel: Vandmærke med respondent-ID og dato

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Tag et foto af stedet | `watermark("${respondent_id} ${today()}")` |

## Begrænsninger

- Billedfiler kan være store, hvilket kan påvirke dataoverførsel og lagring.
- Ikke alle enheder har højkvalitetskameraer eller tilstrækkelig lagerplads.
- Analyse af et stort antal billeder kan være tidskrævende.
- Der kan være privatlivsbekymringer ved optagelse af billeder, især på offentlige steder.
