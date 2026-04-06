---
title: "Berekenen"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Berekeningsvragen in XLSForms en rtSurvey worden gebruikt om berekeningen uit te voeren op basis van andere velden of waarden in uw formulier. Deze vragen worden niet weergegeven aan de gebruiker maar draaien op de achtergrond en slaan hun resultaten op voor later gebruik of indiening.

## Syntaxis

In de XLSForm wordt een berekeningsvraag als volgt gedefinieerd:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Altijd "calculate" voor dit vraagtype.
- **name**: Een unieke naam voor de berekeningsvraag.
- **label**: Gewoonlijk leeg gelaten omdat berekeningsvragen niet worden weergegeven aan gebruikers.
- **calculation**: De te evalueren formule.

## Toepassingen

Berekeningsvragen worden veelgebruikt voor:

1. Rekenkundige bewerkingen uitvoeren
2. Tekenreeksen samenvoegen
3. Complexe logica of functies toepassen
4. Tussenresultaten opslaan voor later gebruik

## Voorbeelden

### Basis rekenkunde

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Tekenreekssamenvoegen

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Functies gebruiken

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Geavanceerd gebruik in rtSurvey

### `pulldata()`-functie

rtSurvey ondersteunt de functie `pulldata()` in berekeningsvelden, waarmee u gegevens kunt ophalen uit externe CSV-bestanden:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Syntaxis

De basissyntaxis voor pulldata() is:

```
pulldata('csv_bestandsnaam', 'kolom_om_terug_te_geven', 'sleutelkolom', ${overeenkomende_waarde})
```

- 'csv_bestandsnaam': Naam van het CSV-bestand (zonder .csv-extensie)
- 'kolom_om_terug_te_geven': Kolomnaam die de gegevens bevat die u wilt ophalen
- 'sleutelkolom': Kolomnaam om tegen te matchen
- ${overeenkomende_waarde}: Waarde om op te zoeken in de sleutelkolom (vaak een variabele uit het formulier)

#### Belangrijke notities

1. Het CSV-bestand moet worden geüpload samen met uw XLSForm bij het implementeren van de enquête.
2. Gebruik komma's als scheidingstekens in uw CSV-bestand, niet puntkomma's.
3. Vermijd komma's in de gegevensvelden van uw CSV, omdat ze parseerprobleem kunnen veroorzaken.
4. pulldata() ondersteunt alleen 1-op-1 relaties. Als er meerdere overeenkomsten worden gevonden, retourneert het alleen de eerste.
5. Er kunnen beperkingen zijn op de tekstlengte die kan worden opgehaald (ongeveer 76 tekens).

### Voorwaardelijke berekeningen

U kunt if()-instructies gebruiken voor voorwaardelijke berekeningen:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Aanbevolen werkwijzen

1. Gebruik betekenisvolle namen voor berekeningsvelden om de leesbaarheid van formulieren te verbeteren.
2. Vermijd overmatig complexe berekeningen in één veld; splits ze op indien nodig.
3. Test uw berekeningen grondig, vooral bij gebruik van complexe formules of externe gegevens.
4. Onthoud dat berekeningsvelden worden uitgevoerd elke keer dat het formulier wordt geëvalueerd.

## Beperkingen

- Berekeningsvelden zijn niet rechtstreeks bewerkbaar door gebruikers.
- Het resultaat van een berekeningsveld is niet onmiddellijk zichtbaar tenzij het wordt verwezen in een weergaveveld of gebruikt in formulierlogica.
