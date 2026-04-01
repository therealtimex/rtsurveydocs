---
title: "Meta"
description: "Meta-vraagtypen leggen automatisch apparaat-, enumerator- en tijdinformatie vast zonder invoer van de respondent."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Meta-vraagtypen zijn speciale velden die **automatisch** worden ingevuld — de respondent ziet ze nooit. Ze leggen context vast over de indiening: wanneer het werd verzameld, welk apparaat werd gebruikt en wie het heeft verzameld. Voeg ze toe in het werkblad `survey` zoals elk ander vraagtype; ze verschijnen simpelweg niet op het scherm.

## Basis XLSForm-specificatie

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Labels zijn optioneel voor metavelden omdat ze nooit worden weergegeven.

---

## Tijdmetavelden

### `start`

Registreert de **datum en tijd waarop het formulier werd geopend**. Opgeslagen in ISO 8601-formaat (`JJJJ-MM-DDTHH:MM:SS.sss+HH:MM`).

### `end`

Registreert de **datum en tijd waarop het formulier werd ingediend**. Samen met `start` kunt u de tijd berekenen die is besteed aan het invullen van het formulier:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Registreert de **huidige datum** (geen tijdcomponent). Opgeslagen als `JJJJ-MM-DD`. Nuttig wanneer u alleen de datum nodig heeft zonder de volledige tijdstempel.

---

## Apparaatmetavelden

### `deviceid`

Registreert de **unieke identificator van het apparaat** dat wordt gebruikt voor gegevensverzameling. Op Android is dit doorgaans de IMEI of Android ID.

### `devicephonenum`

Registreert het **telefoonnummer van de SIM-kaart** in het apparaat (indien beschikbaar).

### `simserial`

Registreert het **serienummer van de SIM-kaart** (ICCID).

### `subscriberid`

Registreert de **IMSI (International Mobile Subscriber Identity)** — de unieke abonnee-identificator op de SIM-kaart.

---

## Enumeratormetavelden

### `username`

Registreert de **gebruikersnaam van de ingelogde enumerator** (het account dat wordt gebruikt in de rtSurvey-app). Dit is de meest betrouwbare manier om bij te houden wie elke indiening heeft verzameld.

### `email`

Registreert het **e-mailadres van de ingelogde enumerator**.

### `phonenumber`

Registreert het **telefoonnummer dat is gekoppeld aan het account van de enumerator** (indien geconfigureerd).

---

## Auditlog

### `audit`

Het metaveld `audit` maakt **gedetailleerde auditlogging** mogelijk — het registreert een tijdgestempeld log van elke vraag die de enumerator heeft bezocht, hoe lang ze op elke vraag hebben doorgebracht, en (optioneel) hun GPS-locatie bij elke stap.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Auditparameters

| Parameter | Beschrijving |
|-----------|-------------|
| `location-priority` | GPS-nauwkeurigheidsniveau: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Minimale seconden tussen locatievastleggingen |
| `location-max-age` | Maximale leeftijd (seconden) van een gecachede locatie die acceptabel is |

{{% alert icon=" " context="warning" %}}
Het veld `audit` genereert een apart bestand per indiening. Zorg ervoor dat uw datapipeline zowel de hoofdformuliergegevens als de audit-CSV verwerkt.
{{% /alert %}}

---

## Volledig voorbeeld

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Huishoud-ID |

---

## Aanbevolen werkwijzen

1. Neem altijd `start` en `end` op — ze zijn gratis, automatisch en van onschatbare waarde voor kwaliteitsbewaking.
2. Neem altijd `username` op om enumeratoren bij te houden.
3. Neem `deviceid` op wanneer u dubbele indieningen wilt detecteren of veldapparaten wilt volgen.
4. Gebruik `audit` in enquêtes met hoge verantwoording waarbij u moet verifiëren dat enumeratoren elke vraag daadwerkelijk hebben bezocht.

---

## Beperkingen

- Alle metavelden zijn **alleen-lezen** — ze kunnen niet worden verwezen of gewijzigd door andere berekeningen.
- `username` en `email` vereisen dat de enumerator is ingelogd; ze zijn leeg voor anonieme indieningen.
- SIM/telefoonmetavelden kunnen lege waarden retourneren op Wi-Fi-only tablets en sommige Android-versies.
