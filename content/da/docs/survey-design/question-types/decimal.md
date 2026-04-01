---
title: "Decimal"
description: "Decimalspørgsmål giver mulighed for numerisk input med brøkdele i din undersøgelse."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

Spørgsmålstypen decimal i XLSForms og rtSurvey bruges til at indsamle numeriske svar, der kan indeholde brøkdele. Denne spørgsmålstype er essentiel til at indsamle præcise numeriske data som målinger, priser eller procentsatser.

## Grundlæggende XLSForm-specifikation

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Indtast din vægt i kg  |

For flere detaljer om den grundlæggende decimal-spørgsmålstype, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Anvendelser

Decimalspørgsmål bruges typisk til:

1. Målinger (f.eks. vægt, højde, afstand)
2. Finansielle data (f.eks. priser, lønninger)
3. Procentsatser
4. Videnskabelig dataindsamling
5. Enhver numerisk data, der kræver præcision ud over heltal

## Bedste praksis

1. Brug klare og præcise labels til at angive det forventede input og måleenhed.
2. Implementer intervalrestriktioner for at forhindre urealistiske eller fejlagtige input.
3. Overvej at bruge hinttekst til at give eksempler eller præcisere det forventede format.
4. Angiv det ønskede antal decimaler i labelen eller hintet, hvis præcision er vigtig.

## Restriktioner og validering

Du kan tilføje restriktioner for at sikre, at den indtastede værdi falder inden for et bestemt interval:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Indtast din højde i meter | .>0 and .<=3    | Højde skal være mellem 0 og 3 meter |

## Eksempel på brug

Her er et eksempel på, hvordan du kan bruge decimalspørgsmål i en sundhedsundersøgelse:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Indtast din vægt i kg                   | .>0 and .<=500 | Vægt skal være mellem 0 og 500 kg |
| decimal | height         | Indtast din højde i meter               | .>0 and .<=3 | Højde skal være mellem 0 og 3 meter |
| decimal | body_temp      | Indtast din kropstemperatur i Celsius    | .>=35 and .<=42 | Temperatur skal være mellem 35°C og 42°C |
| calculate | bmi          |                                           |            |                                   |

I beregningsrækken for BMI kan du bruge:

```
calculation | ${weight} / (${height} * ${height})
```

Dette beregner BMI ved hjælp af den indtastede vægt og højde.

## rtSurvey-udvidelser

Mens den grundlæggende XLSForm-specifikation for decimalspørgsmål er enkel, kan rtSurvey tilbyde yderligere funktioner eller tilpasninger:

1. Præcisionsstyring (antal decimaler)
2. Brugerdefinerede inputformater (f.eks. procent, valuta)
3. Avancerede valideringsregler

## Begrænsninger

- Præcisionen af decimaltal kan være begrænset af det underliggende system eller database.
- Brugere kan have brug for vejledning om det forventede decimalseparatortegn (punktum eller komma) afhængigt af deres lokale indstillinger.
- Store decimaltal kan være svære at læse eller indtaste præcist på mobilenheder.
