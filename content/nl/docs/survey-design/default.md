---
title: "Standaardwaarden"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Standaardwaarden in rtSurvey stellen u in staat vragen vooraf in te vullen met antwoorden wanneer een respondent ze voor het eerst tegenkomt. Deze functie kan de efficiëntie van enquêtes en de gegevenskwaliteit aanzienlijk verbeteren door beginwaarden te bieden die veelgekozen zijn of als voorbeeld dienen van verwachte invoer.

## Basisgebruik

Om een standaardwaarde in te stellen, gebruikt u de kolom `default` in uw XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Enquêtedatum                  | 2024-07-04 |
| decimal | weight      | Gewicht van respondent? (in kg)| 51.3       |
```

In dit voorbeeld wordt de enquêtedatum vooraf ingevuld met 4 juli 2024, en begint het gewichtsveld met 51,3 kg.

## Dynamische standaardwaarden

rtSurvey ondersteunt dynamische standaardwaarden met behulp van functies:

```
| type | name | label                                   | default  |
|------|------|-----------------------------------------| ---------|
| date | d    | Voer de datum in waarop het event plaatsvond | today()  |
```

Hier stelt de functie `today()` de standaardwaarde automatisch in op de huidige datum.

## rtSurvey-specifieke functies

### Contextbewuste standaardwaarden

rtSurvey breidt de standaardfunctionaliteit uit met contextbewuste standaardwaarden:

```
| type    | name     | label              | default            |
|---------|----------|--------------------|--------------------|
| text    | location | Huidige locatie    | ${current_location}|
```

Dit gebruikt de variabele `${current_location}` van rtSurvey om de locatie vooraf in te vullen op basis van de GPS van het apparaat.

### Cascaderende standaardwaarden

rtSurvey staat standaardwaarden op basis van eerdere antwoorden toe:

```
| type    | name     | label       | default          |
|---------|----------|-------------|------------------|
| text    | city     | Stad        |                  |
| text    | district | District    | ${city}-district |
```

Hier wordt het districtveld vooraf ingevuld op basis van de ingevoerde stad.

### Standaardwaarden in herhalingen

Voor vragen binnen een herhalingsgroep wordt de standaardwaarde berekend wanneer de herhaling wordt toegevoegd:

```
| type         | name       | label              | default                |
|--------------|------------|--------------------|------------------------|
| begin repeat | visits     | Kliniekbezoeken    |                        |
| date         | visit_date | Bezoekdatum        | ${previous_visit_date} |
| end repeat   |            |                    |                        |
```

Dit stelt de standaard bezoekdatum in op de datum van het vorige bezoek.

## Aanbevolen werkwijzen voor het gebruik van standaardwaarden

1. **Gebruik spaarzaam**: Gebruik standaardwaarden alleen waar ze de efficiëntie of gegevenskwaliteit aanzienlijk verbeteren.
2. **Zorg voor nauwkeurigheid**: Controleer en update statische standaardwaarden regelmatig.
3. **Test grondig**: Vooral bij het gebruik van dynamische of berekende standaardwaarden.
4. **Denk aan de gebruikerservaring**: Zorg ervoor dat standaardwaarden respondenten niet misleiden of vooringenomenheid introduceren.
5. **Documenteer duidelijk**: Zorg dat alle teamleden de redenering achter standaardwaarden begrijpen.

## Geavanceerde standaardtechnieken

### Willekeurige standaardwaarden

rtSurvey ondersteunt willekeurige standaardwaarden voor bepaalde vraagtypen:

```
| type              | name    | label         | default         |
|-------------------|---------|---------------|-----------------|
| select_one options| choice  | Selecteer één:| random(options) |
```

Hiermee wordt willekeurig een standaardoptie geselecteerd uit de lijst 'options'.

### Voorwaardelijke standaardwaarden

Gebruik relevantie om voorwaardelijke standaardwaarden in te stellen:

```
| type    | name     | label        | default | relevant        |
|---------|----------|--------------|---------|-----------------|
| text    | other    | Specificeer  | N/A     | ${q1} = 'other' |
```

Hier is 'N/A' de standaardwaarde alleen wanneer 'other' is geselecteerd in een vorige vraag.

## Overwegingen voor gegevensbeheer

- Standaardwaarden worden opgenomen in gegevensexports, doorgaans met een markering die aangeeft dat het standaardwaarden waren.
- De audittrailfunctie van rtSurvey houdt bij wanneer standaardwaarden door respondenten worden gewijzigd.

## Gedrag in de mobiele app

- De mobiele app van rtSurvey ondersteunt alle standaardfunctionaliteiten, inclusief dynamische en contextbewuste standaardwaarden.
- De offlinemodus kan invloed hebben op sommige dynamische standaardwaarden die afhankelijk zijn van realtime gegevens.

## Bekende beperkingen

- Complexe berekende standaardwaarden kunnen de laadtijd van formulieren beïnvloeden, vooral op apparaten aan de onderkant van de markt.
- Sommige dynamische standaardwaarden werken mogelijk niet zoals verwacht in de voorbeeldmodus.

## Problemen met standaardwaarden oplossen

1. **Standaardwaarde verschijnt niet**: Controleer op syntaxfouten in de standaardexpressie.
2. **Onverwachte waarden**: Verifieer de berekeningslogica en test met verschillende scenario's.
3. **Prestatieproblemen**: Optimaliseer complexe standaardberekeningen of overweeg alternatieve benaderingen.
