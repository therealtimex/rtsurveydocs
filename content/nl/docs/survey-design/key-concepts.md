---
title: "Belangrijkste concepten"
description: "Overzicht van formulierontwerp"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Wat is een XLSForm?
rtSurvey gebruikt een uitgebreide versie van de [XLSForm](https://xlsform.org/)-standaard voor formulierontwerp en biedt krachtige functies voor het maken van geavanceerde enquêtes. Deze gids introduceert u de belangrijkste concepten van formulierontwerp in rtSurvey, van de basisstructuur van XLSForm tot geavanceerde rtSurvey-specifieke functies.

Met XLSForms kunt u formulieren ontwerpen in een voor mensen leesbaar formaat met het bekende Excel-hulpmiddel, waardoor het voor bijna iedereen toegankelijk is.
Deze standaard maakt eenvoudig delen en samenwerken aan formulierontwerp mogelijk.

Hoewel XLSForms beginnersvriendelijk zijn, stellen ze ervaren gebruikers ook in staat om complexe formulieren te maken.

rtSurvey biedt een consistente manier om geavanceerde functionaliteiten zoals sla-logica op te nemen in formulieren voor verschillende web- en mobiele platforms voor gegevensverzameling.

## XLSForm-structuur
Een XLSForm bestaat doorgaans uit twee hoofdwerkbladen:

1. **survey**: Definieert de structuur en inhoud van uw formulier.
2. **choices**: Specificeert antwoordkeuzes voor meerkeuzevragen.

Een optioneel **settings**-werkblad kan aanvullende formulierspecificaties bieden.

Het is belangrijk op te merken dat de verplichte kolommen in de werkbladen survey en choices aanwezig moeten zijn om het formulier correct te laten werken. Optionele kolommen in beide werkbladen bieden verdere controle over het gedrag van elk item in het formulier, maar zijn niet essentieel.

De kolommen in uw Excel-werkboek kunnen in willekeurige volgorde staan en optionele kolommen kunnen leeg worden gelaten. Het is echter cruciaal om de precieze syntaxis en naamconventies te gebruiken die zijn gespecificeerd in de XLSForm-documentatie om het formulier correct te laten werken.

### Het survey-werkblad
Het **survey-werkblad** is waar u de structuur van uw formulier definieert en de inhoud levert. Elke rij in het survey-werkblad vertegenwoordigt een vraag of element in uw formulier. De volgende kolommen zijn verplicht in het survey-werkblad:

- `type`: Specificeert het type invoer dat u verwacht voor de vraag.
- `name`: Specificeert de unieke variabelenaam voor dat item. Namen moeten beginnen met een letter of een onderstrepingsteken en mogen alleen letters, cijfers, koppeltekens, onderstrepingstekens en punten bevatten. Namen zijn hoofdlettergevoelig.
- `label`: Bevat de eigenlijke tekst die u ziet voor de vraag in het formulier.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Geslacht respondent? |
| integer             | age      | Leeftijd respondent? |

### Het choices-werkblad
Het **`choices`**-werkblad wordt gebruikt om de antwoordkeuzes voor meerkeuzevragen te specificeren.
Elke rij vertegenwoordigt een antwoordkeuze. De volgende kolommen zijn verplicht in het choices-werkblad:

- **`list_name`**: Groepeert een set gerelateerde antwoordkeuzes.
- **`name`**: Specificeert de unieke variabelenaam voor die antwoordkeuze.
- **`label`**: Toont de antwoordkeuze precies zoals u wilt dat deze op het formulier verschijnt.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgender          |
| gender              | female      | Vrouwelijk           |
| gender              | male        | Mannelijk            |
| gender              | other       | Overig               |

De kolommen die u toevoegt aan uw Excel-werkboek, of ze nu verplicht of optioneel zijn, kunnen in willekeurige volgorde staan. Optionele kolommen kunnen volledig worden weggelaten. Rijen of kolommen kunnen leeg worden gelaten om de leesbaarheid te verbeteren, maar gegevens na 20 aangrenzende lege kolommen of rijen op een blad worden niet verwerkt. Alle .xlsx-bestandsopmaak wordt genegeerd, zodat u scheidingslijnen, arcering en andere lettertypeopmaak kunt gebruiken om het formulier beter leesbaar te maken.

Een ding om in gedachten te houden bij het ontwerpen van formulieren in Excel is dat de syntaxis die u gebruikt precies moet zijn. Als u bijvoorbeeld **Choices** of **choice** schrijft in plaats van **choices**, werkt het formulier niet.

### Het settings-werkblad

Het settings-werkblad is optioneel maar stelt u in staat om metagegevens en gedrag op formulierniveau te specificeren. Veelgebruikte kolommen in het settings-werkblad zijn:

| Kolom | Beschrijving |
|--------|-------------|
| form_title | De titel van het formulier zoals die aan gebruikers verschijnt |
| form_id | Een unieke identificator voor het formulier, gebruikt in gegevensbeheer en API-aanroepen |
| default_language | De standaard taalcode voor meertalige formulieren (bijv. 'nl' voor Nederlands) |
| version | Het versienummer van het formulier, nuttig voor het bijhouden van wijzigingen |
| instance_name | Expressie om een unieke naam te genereren voor elke formulierinzending |
| generation | Integer die de generatie van het formulier aangeeft. Verhoog voor structurele wijzigingen |
| family | Identificator om gerelateerde formulieren te groeperen over structurele wijzigingen |

Het settings-werkblad in rtSurvey kan ook aanvullende configuraties bevatten die specifiek zijn voor de uitgebreide functionaliteiten van rtSurvey. Raadpleeg de rtSurvey-documentatie voor een volledige lijst van ondersteunde instellingen.

## Belangrijkste componenten van het survey-werkblad

Het survey-werkblad is de kern van uw formulierontwerp. Hier volgt een overzicht van de belangrijkste componenten:

| Component | Beschrijving |
|-----------|-------------|
| [type](#question-types) | Specificeert het vraagtype (bijv. text, integer, select_one) |
| [name](#naming-conventions) | Unieke identificator voor de vraag |
| [label](#labels-and-translations) | De tekst die aan de respondent wordt weergegeven |
| [hint](#hints-and-help-text) | Aanvullende begeleiding voor de respondent |
| [appearance](#appearance-options) | Wijzigt hoe de vraag wordt weergegeven |
| [relevant](#relevance-and-skip-logic) | Bepaalt wanneer de vraag moet worden gesteld (sla-logica) |
| [constraint](#constraints-and-validation) | Valideert het antwoord |
| [calculation](#calculations) | Berekent waarden op basis van andere antwoorden |
| [required](#required-fields) | Specificeert of de vraag moet worden beantwoord |


### Vraagtypen
XLSForm ondersteunt een aantal vraagtypen. Dit zijn slechts enkele van de opties die u kunt invoeren in de **`type`**-kolom in het **`survey`**-werkblad in uw XLSForm:

| Vraagtype                 | Invoer                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------|
| integer                   | Geheel getal (d.w.z. heel getal) invoer.                                                    |
| decimal                   | Decimale invoer.                                                                            |
| range                     | [Bereik](#range)-invoer (inclusief beoordeling)                                             |
| text                      | Vrije tekstrespons.                                                                         |
| select_one [options]      | [Meerkeuze](#multiple-choice) vraag; slechts één antwoord kan worden geselecteerd.          |
| select_multiple [options] | [Meerkeuze](#multiple-choice) vraag; meerdere antwoorden kunnen worden geselecteerd.        |
| select_one_from_file [file]| [Meerkeuze uit bestand](#multiple-choice-from-file); slechts één antwoord kan worden geselecteerd. |
| select_multiple_from_file [file]| [Meerkeuze uit bestand](#multiple-choice-from-file); meerdere antwoorden kunnen worden geselecteerd.|
| rank [options]            | [Rangschikking](#rank)-vraag; orden een lijst.                                              |
| note                      | Toon een notitie op het scherm, neemt geen invoer aan.                                      |
| geopoint                  | Verzamel een [enkele GPS-coördinaat](#gps).                                                 |
| geotrace                  | Registreer een [lijn van twee of meer GPS-coördinaten](#gps).                               |
| geoshape                  | Registreer een [veelhoek van meerdere GPS-coördinaten](#gps); het laatste punt is hetzelfde als het eerste punt. |
| date                      | Datuminvoer.                                                                                |
| time                      | Tijdinvoer.                                                                                 |
| dateTime                  | Accepteert een datum- en tijdinvoer.                                                        |
| image                     | Maak een foto of upload een [afbeeldingsbestand](#image).                                   |
| audio                     | Maak een audio-opname of upload een audiobestand.                                           |
| background-audio          | Audio wordt op de achtergrond opgenomen tijdens het invullen van het formulier.             |
| video                     | Maak een video-opname of upload een videobestand.                                           |
| file                      | Generieke bestandsinvoer (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                        |
| barcode                   | Scan een barcode, vereist de barcode-scannerapp.                                            |
| calculate                 | Voer een berekening uit; zie de [Berekeningssectie](#calculation) hieronder.                |
| acknowledge               | Bevestigingsprompt die de waarde instelt op "OK" indien geselecteerd.                       |
| hidden                    | Een veld zonder bijbehorend UI-element dat kan worden gebruikt om een constante op te slaan |
| xml-external              | Voegt een verwijzing toe naar een [extern XML-gegevensbestand](#external-xml-data)          |

### Labels

Labels zijn de tekst die aan respondenten wordt weergegeven voor elke vraag. Ze zijn cruciaal voor duidelijke communicatie in enquêtes.

- **Basisgebruik**: Voer in de `label`-kolom de vraagtekst in.
- **Meerdere talen**: Gebruik aanvullende kolommen zoals `label::Nederlands` en `label::Frans` voor meertalige enquêtes.
- **Opmaak**: rtSurvey ondersteunt basisopmaak in HTML in labels voor nadruk of structuur.

Voorbeeld:
```
| type | name | label | label::Frans |
|------|------|-------|--------------|
| text | name | Wat is uw naam? | Quel est votre nom? |
```

### Hints

Hints bieden aanvullende begeleiding aan respondenten zonder de hoofdvraagstekst te overbelasten.

- **Gebruik**: Voeg hints toe in de `hint`-kolom.
- **Zichtbaarheid**: Hints worden doorgaans weergegeven onder de hoofdvraagstekst.
- **Meertalig**: Net als labels kunnen hints worden gespecificeerd voor meerdere talen met `hint::Taal`-kolommen.

Voorbeeld:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Hoe oud bent u? | Voer uw leeftijd in jaren in |
```

### Weergave

De `appearance`-kolom in rtSurvey maakt aanpassing mogelijk van hoe vragen worden weergegeven.

- **Standaard opties**: Inclusief 'multiline' voor tekst, 'horizontal' voor selectievragen.
- **rtSurvey-uitbreidingen**:
  - Tijdinvoer: Verschillende klokweergaveopties (bijv. `inline`, `inline-1line`)
  - Kleurpersonalisatie: Gebruik de functie `colors()` om pictogramkleuren te wijzigen

Voorbeeld:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Voer tijd in | inline-[%H:%M] |
```

### Relevant

De `relevant`-kolom implementeert sla-logica en bepaalt wanneer een vraag moet worden weergegeven.

- **Syntaxis**: Gebruik XPath-expressies om voorwaarden te definiëren.
- **Variabelen**: Verwijs naar andere vraagnamen met `${question_name}`.

Voorbeeld:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Lijst allergieën op | ${has_allergies} = 'yes' |
```

### Vereist

De `required`-kolom specificeert of een vraag moet worden beantwoord.

- **Basisgebruik**: Gebruik 'yes' of 'true' om een vraag verplicht te maken.
- **Geavanceerd**: Kan expressies gebruiken voor voorwaardelijke vereiste.

Voorbeeld:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | E-mailadres | yes |
```

### Herhalingen

Herhalingen stellen een groep vragen in staat om meerdere keren te worden beantwoord.

- **Gebruik**: Gebruik `begin repeat`- en `end repeat`-rijen om een herhalende groep te definiëren.
- **Naamgeving**: Geef elke herhalingsgroep een unieke naam.

Voorbeeld:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | Huishoudlid |
| text | member_name | Naam |
| integer | member_age | Leeftijd |
| end repeat | | |
```

### Media

rtSurvey ondersteunt verschillende mediatypen in enquêtes, inclusief afbeeldingen, audio en video.

- **Vraagtypen**: Gebruik 'image', 'audio' of 'video' in de typekolom.
- **Media in labels**: Verwijs naar mediabestanden in labels met HTML-tags.

Voorbeeld:
```
| type | name | label |
|------|------|-------|
| image | house_photo | Maak een foto van het huis |
| note | | <img src="logo.jpg" /> Welkom bij de enquête |
```

### Alleen-lezen

Alleen-lezenvragen tonen informatie zonder gebruikersinvoer toe te staan.

- **Gebruik**: Voeg 'readonly' toe aan de `appearance`-kolom.
- **Berekeningen**: Vaak gebruikt met het calculate-type voor het weergeven van berekende waarden.

Voorbeeld:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | BMI | readonly | ${weight} / (${height} * ${height}) |
```

## rtSurvey-uitbreidingen

rtSurvey breidt de XLSForm-standaard uit door extra mogelijkheden te ondersteunen zoals `rasterindeling`, `HTML-opmaak` en vele nieuwe `widgets`.

### Rasterindeling
rtSurvey stelt uw formulier in staat de weergave van traditionele papieren enquêtes na te bootsen door meerdere vragen in één rij samen te voegen.

### Formulierinstellingen

### Gegevensinstellingen

### Typeform-stijl

### Uitbreiding van pulldata()

### Op weergave gebaseerde uitbreidingen

### Webbox-uitbreidingen
