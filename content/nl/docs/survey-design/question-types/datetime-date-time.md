---
title: "Datum/tijd, datum, tijd"
description: "Datum/tijdvragen staan respondenten toe zowel datum als tijd in te voeren in één veld."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Het datum/tijdvraagtype in XLSForms en rtSurvey stelt respondenten in staat zowel datum als tijd in te voeren in één veld. Dit vraagtype is nuttig wanneer u een specifiek moment in de tijd moet vastleggen, inclusief zowel de datum als de exacte tijd.

## Basis XLSForm-specificatie

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Wanneer vond het evenement plaats? |

## Toepassingen

Datum/tijdvragen worden veelgebruikt voor:

1. Tijdstempels van evenementen of observaties vastleggen
2. Afspraken of vergaderingen plannen
3. Begin- en eindtijden van activiteiten loggen
4. Nauwkeurige momenten vastleggen voor tijdkritische gegevensverzameling

## rtSurvey-uitbreidingen

rtSurvey breidt de functionaliteit van datum/tijdvragen uit met verschillende weergaven en aanpassingsopties:

### Weergaveopties

- `(standaard)`: Toon de kalender en klok voor het selecteren van datum en tijd
- `inline`: Toon de kalender en klok als pictogrammen
- `inline-1line`: Toon de kalender en klok voor selectie in een enkelerij-formaat
- `inline-onlyresult`: Toon de kalender en klok als pictogrammen aan het einde van de regel; pictogrammen verdwijnen na selectie

### Kleurcustomisatie

U kunt de kleur van de kalender- en klokpictogrammen aanpassen met de functie `colors()`:

- `inline colors("0099FF")`: Toon pictogrammen met aangepaste kleur
- `inline-1line-0000FF`: Toon in enkelerij-formaat met aangepaste kleur
- `inline-1line colors("0000FF","FFFF00")`: Toon in enkelerij-formaat met meerdere aangepaste kleuren

### Aangepaste datum- en tijdformaten

rtSurvey maakt aangepaste datum- en tijdformaten mogelijk met speciale syntaxis:

- `inline-[%Y-%m-%d %H:%M:%S]`: Aangepast formaatvoorbeeld (Jaar-Maand-Dag Uur:Minuut:Seconde)
- `inline-[%d/%m/%Y %I:%M %p]`: Aangepast formaatvoorbeeld (Dag/Maand/Jaar Uur:Minuut AM/PM)

## Voorbeeldgebruik

| type     | name           | label                              | appearance                    |
|----------|----------------|------------------------------------|-----------------------------|
| datetime | incident_time  | Wanneer vond het incident plaats?  | inline-[%d/%m/%Y %I:%M %p]  |

## Aanbevolen werkwijzen

1. Geef duidelijke instructies over het verwachte datum- en tijdformaat.
2. Overweeg de weergave `inline` te gebruiken voor een compactere weergave.
3. Gebruik aangepaste formaten wanneer u specifieke datum- en tijdcomponenten of opmaak nodig heeft.
4. Wees bewust van tijdzones bij het verzamelen van datum/tijdgegevens in verschillende regio's.

## Beperkingen

- Sommige weergaven of aangepaste formaten worden mogelijk niet ondersteund op alle apparaten of platforms.
- Gebruikers hebben mogelijk begeleiding nodig bij het correct invoeren van datum en tijd, vooral met aangepaste formaten.
- Tijdzoneverschillen kunnen gegevensanalyse compliceren als ze niet goed worden verantwoord.
