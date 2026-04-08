---
title: "Tekst"
description: "Vrij tekstantwoord vraagtype in rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Het vraagtype `text` verzamelt een vrij tekstantwoord — een willekeurige reeks tekens. Het is het meest flexibele invoertype en wordt gebruikt voor namen, adressen, beschrijvingen, codes en alles wat niet in een meer specifiek type past.

rtSurvey breidt `text` ook uit met **tijdinvoerwidgets** die nauwkeurige tijdinvoer mogelijk maken met een klokpicker.

## Basis XLSForm-specificatie

| type | name | label |
|------|------|-------|
| text | respondent_name | Volledige naam van respondent |
| text | address | Thuisadres |

## Toepassingen

Tekstvragen worden gebruikt voor:

1. Namen, adressen, vrije beschrijvingen
2. Open-ended opmerkingen of feedback
3. Codes, ID's of referentienummers die niet in integer/decimal passen
4. Het verzamelen van tijdwaarden met de tijdinvoerextensies van rtSurvey
5. Velden met automatisch aanvullen (via `search-autocomplete-noedit-v2()`)

## Standaard weergaveopties

| Weergave | Beschrijving |
|----------|-------------|
| *(geen)* | Enkelregelige tekstinvoer |
| `multiline` | Meerregelig tekstgebied — het beste voor langere vrije tekst op web |
| `richtext` | RTF-editor — werkbalk met vet, cursief, lijsten en koppelingen |
| `typingtest` | Typtestinterface — toont een passage en meet typsnelheid en nauwkeurigheid |

## rtSurvey tijdinvoerextensies

rtSurvey breidt `text` uit met een **klokpicker-widget** voor het verzamelen van tijdwaarden. Deze weergaveopties tonen een klokpictogram waarop de enumerator kan tikken om uren, minuten, seconden of milliseconden te selecteren.

### Weergavevarianten

| Weergave | Beschrijving |
|----------|-------------|
| `inline` | Klokpictogram weergegeven naast het veld |
| `inline colors("RRGGBB")` | Klokpictogram met aangepaste hexkleur |
| `inline-1line` | Klok weergegeven in een compact enkelerij-formaat |
| `inline-1line-RRGGBB` | Enkelrij met aangepaste pictogramkleur (hex, zonder `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Enkelrij met twee kleuren |
| `inline-onlyresult` | Klokpictogram verdwijnt na selectie; alleen de waarde wordt getoond |
| `inline-onlyresult colors("RRGGBB")` | Hetzelfde, met aangepaste pictogramkleur |

### Tijdformaattokens

Voeg een formaattekenreeks tussen haakjes toe om te bepalen welke tijdcomponenten worden weergegeven:

| Formaattekenreeks | Geeft weer |
|-------------------|-----------|
| `inline-[%H:%M]` | Uren en minuten (24-uurs) |
| `inline-[%h:%M]` | Uren en minuten (12-uurs) |
| `inline-[%H:%M:%S]` | Uren, minuten, seconden (24-uurs) |
| `inline-[%h:%M:%S]` | Uren, minuten, seconden (12-uurs) |
| `inline-[%H:%M:%3]` | Uren, minuten, milliseconden |
| `inline-[%M:%S]` | Alleen minuten en seconden |
| `inline-[%M:%3]` | Alleen minuten en milliseconden |
| `inline-[%S]` | Alleen seconden |
| `inline-[%3]` | Alleen milliseconden |
| `inline-[%H]` | Alleen uren (24-uurs) |
| `inline-[%h]` | Alleen uren (12-uurs) |

### Voorbeeld: Een taakduur in minuten en seconden vastleggen

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Tijd nodig om de taak te voltooien | `inline-[%M:%S]` |

### Voorbeeld: Een evenementtijd in 24-uurs formaat met aangepaste kleur vastleggen

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Tijd van het evenement | `inline-1line colors("0099FF")` |

## Gegevensformaat

Tekstgegevens worden opgeslagen en geëxporteerd als een gewone tekenreeks. Voor tijdgebaseerde invoer met de inline klokwidget wordt de waarde opgeslagen in het formaat dat overeenkomt met de gekozen formaattekenreeks (bijv. `14:32` voor `%H:%M`).

## Beperkingen en validatie

Pas beperkingen toe om formaat, lengte of patroon te handhaven:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Volledige naam | `string-length(.) >= 2` | Naam moet minimaal 2 tekens hebben |
| text | code | Referentiecode | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Voer 2 hoofdletters in gevolgd door 4 cijfers |
| text | phone | Telefoonnummer | `regex(., '^[0-9]{9,15}$')` | Voer een geldig telefoonnummer in |

## Aanbevolen werkwijzen

1. Gebruik specifiekere typen (`integer`, `decimal`, `date`) wanneer de gegevens een bekende structuur hebben — dit voorkomt ongeldige invoer en vereenvoudigt analyse.
2. Voeg `constraint` toe met `string-length()` of `regex()` om codes of ID's te valideren.
3. Gebruik de weergave `multiline` voor open-ended vragen waarbij respondenten meerdere zinnen kunnen schrijven.
4. Kies voor tijdverzameling de tijdformaattokens die overeenkomen met de precisie die uw analyse vereist.

## Platformondersteuning

Het tekstvraagtype en alle tijdinvoerweergaven worden ondersteund op iOS, Android en webplatforms.

## Beperkingen

- Tekstantwoorden zijn vrije-vorm — er is geen ingebouwde spellingcontrole of woordenschatbeperking buiten regex-patronen.
- De inline tijdwidget is een rtSurvey-uitbreiding en maakt geen deel uit van de standaard XLSForm-specificatie.
