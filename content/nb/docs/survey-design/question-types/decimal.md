---
title: "Desimaltall"
description: "Desimaltallsspørsmål tillater numeriske inndataer med brøkdeler i spørreundersøkelsen."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

Desimaltallsspørsmålstypen i XLSForm og rtSurvey brukes til å samle inn numeriske svar som kan inneholde brøkdeler. Denne spørsmålstypen er nødvendig for å samle inn presise numeriske data som målinger, priser eller prosentandeler.

## Grunnleggende XLSForm-spesifikasjon

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Skriv inn vekten din i kg|

## Brukstilfeller

Desimaltallsspørsmål brukes vanligvis for:

1. Målinger (f.eks. vekt, høyde, avstand)
2. Finansielle data (f.eks. priser, lønninger)
3. Prosentandeler
4. Vitenskapelig datainnsamling
5. Numeriske data som krever presisjon utover hele tall

## Beste praksis

1. Bruk klare og konsise etiketter for å angi forventet inndata og måleenhet.
2. Implementer områdespesifiseringer for å forhindre urealistiske eller feilaktige inndataer.
3. Vurder å bruke hinttekst for å gi eksempler eller tydeliggjøre forventet format.
4. Angi ønsket antall desimaler i etiketten eller hintet hvis presisjon er viktig.

## Begrensninger og validering

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Skriv inn høyden din i meter | .>0 and .<=3    | Høyden må være mellom 0 og 3 meter |

## Eksempelbruk

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Skriv inn vekten din i kg                 | .>0 and .<=500 | Vekten må være mellom 0 og 500 kg |
| decimal | height         | Skriv inn høyden din i meter              | .>0 and .<=3 | Høyden må være mellom 0 og 3 meter |
| decimal | body_temp      | Skriv inn kroppstemperaturen din i Celsius| .>=35 and .<=42 | Temperaturen må være mellom 35°C og 42°C |
| calculate | bmi          |                                           |            |                                   |

I calculate-raden for BMI kan du bruke:

```
calculation | ${weight} / (${height} * ${height})
```

## Begrensninger

- Presisjonen til desimaltall kan begrenses av det underliggende systemet eller databasen.
- Brukere kan trenge veiledning om forventet desimalskilletegn (punktum eller komma) avhengig av lokalitet.
- Store desimaltall kan være vanskelige å lese eller angi nøyaktig på mobile enheter.
