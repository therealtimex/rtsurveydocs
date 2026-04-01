---
title: "Ģeopunkts"
description: "Ģeopunkta jautājumi uztver ģeogrāfiskās koordinātas (platumu, garumu, augstumu un precizitāti) kā daļu no aptaujas."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

Jautājuma tips geopoint XLSForms un rtSurvey ļauj vākt ģeogrāfiskās koordinātas, izmantojot ierīces GPS vai citus atrašanās vietas pakalpojumus. Šī funkcija ir īpaši noderīga aptaujas atbilžu kartēšanai, lauka darbību izsekošanai vai datu saistīšanai ar konkrētām atrašanās vietām.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| geopoint | household_location | Ierakstiet mājsaimniecības atrašanās vietu |
| geopoint | facility_coords | Uztveriet šīs iestādes GPS koordinātas |

## Datu formāts

Geopoint vērtība tiek saglabāta kā četras atstarpes atdalītas vērtības:
`platums garums augstums precizitāte`

Piemērs: `56.9460 24.1059 15.5 3.2`

## Izskata iespējas

| Izskats | Apraksts |
|---------|----------|
| *(nav)* | Noklusējuma GPS uztvērējs |
| `placement-map` | Interaktīva karte punkta manuālai izvietošanai |

## Labākā prakse

1. Informējiet enumeratorus, cik ilgi GPS koordinātu uztvere var aizņemt.
2. Iestatiet precizitātes slieksni ar `constraint` (piemēram, `. < 10` metriem).
3. Apsveriet bezsaistes kartēšanas vajadzības lauka jomā.

## Ģeogrāfisko funkciju izmantošana

```
area(${field_boundary})    → Aprēķina laukumu kvadrātmetros
distance(${route})         → Aprēķina kopējo ceļa garumu metros
```
