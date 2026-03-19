---
title: "Geotrace"
description: "Geotrace-vragen staan respondenten toe een reeks verbonden punten op een kaart vast te leggen, waarmee lijnen of paden worden gecreëerd als onderdeel van de enquête."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Het geotrace-vraagtype in XLSForms en rtSurvey stelt respondenten in staat een reeks verbonden punten op een kaart vast te leggen, waarmee lijnen of paden worden gecreëerd. Deze functie is bijzonder nuttig voor het in kaart brengen van routes, grenzen of lineaire kenmerken in ruimtelijke enquêtes.

## Basis XLSForm-specificatie

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Teken het pad van de rivier     |

## Toepassingen

Geotrace-vragen worden veelgebruikt voor:

1. Routes of paden in kaart brengen tijdens veldsurveys
2. Lineaire kenmerken traceren zoals wegen, rivieren of grenzen
3. De omvang van lineaire infrastructuur vastleggen (bijv. pijpleidingen, stroomlijnen)
4. Reispaden vastleggen in transportstudies
5. Transecten definiëren in ecologische surveys

## Gegevensformaat

Geotrace-gegevens worden doorgaans opgeslagen als een tekenreeks van door spaties gescheiden coördinatenparen:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

## Beperkingen

- Nauwkeurige paden traceren op kleine mobiele schermen kan uitdagend zijn.
- Complexe traces kunnen aanzienlijke opslag- en verwerkingscapaciteit vereisen.
- Continu GPS-gebruik voor automatisch traceren kan apparaatbatterijen snel leegtrekken.
