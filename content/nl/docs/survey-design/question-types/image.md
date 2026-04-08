---
title: "Afbeelding"
description: "Afbeeldingsvragen staan respondenten toe foto's vast te leggen en in te dienen als onderdeel van de enquête."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Het afbeeldingsvraagtype in XLSForms en rtSurvey stelt respondenten in staat foto's vast te leggen en in te dienen als onderdeel van hun enquêteresponsen. Deze functie is bijzonder nuttig voor het verzamelen van visuele gegevens, het documenteren van observaties of het verstrekken van bewijs in veldsurveys.

## Basis XLSForm-specificatie

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Maak een foto van de locatie    |

## Toepassingen

Afbeeldingsvragen worden veelgebruikt voor:

1. Veldomstandigheden of observaties documenteren
2. Visueel bewijs vastleggen in onderzoeksstudies
3. Voor-en-na foto's verzamelen in impactbeoordelingen
4. De voltooiing van taken of aanwezigheid op locaties verifiëren
5. Visuele gegevens verzamelen voor externe analyse

## Aanbevolen werkwijzen

1. Geef duidelijke instructies over wat gefotografeerd moet worden.
2. Overweeg privacyimplicaties en informeer respondenten over hoe hun foto's worden gebruikt.
3. Houd rekening met bestandsgroottes en opslagbeperkingen, vooral voor enquêtes in gebieden met beperkte internetverbinding.
4. Zorg ervoor dat het apparaat voldoende opslagruimte heeft en cameramachtigingen zijn verleend.

## Beperkingen

- Afbeeldingsbestanden kunnen groot zijn, wat gegevensoverdracht en -opslag kan beïnvloeden.
- Niet alle apparaten hebben camera's van hoge kwaliteit of voldoende opslagruimte.
- Het analyseren van grote aantallen afbeeldingen kan tijdrovend zijn.
- Er kunnen privacyproblemen zijn bij het vastleggen van afbeeldingen, vooral in openbare ruimten.

## rtSurvey afbeeldingsuitbreidingen

### watermark()

De `watermark()`-weergave plaatst een tekstwatermerk over foto's die met dit veld zijn gemaakt. Het watermerk bevat doorgaans metadata zoals de naam van de enumerator, datum/tijd of GPS-coördinaten, direct op de afbeelding gestempeld voordat deze wordt opgeslagen.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Maak een foto van de locatie | `watermark("${enumerator_id} ${today()}")` |

Het argument van `watermark()` is een XPath-expressie die wordt geëvalueerd op het moment van vastleggen. De resulterende string wordt weergegeven als watermerktekst.

### editable

De `editable`-weergave stelt de respondent in staat om de gemaakte foto na het nemen ervan te annoteren of op te tekenen. Een tekeningwerkbalk verschijnt over de afbeelding.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Fotografeer en markeer aandachtsgebieden | editable |

{{% alert icon=" " context="info" %}}
`editable` kan worden gecombineerd met `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
