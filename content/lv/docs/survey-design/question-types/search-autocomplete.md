---
title: "Search Autocomplete"
description: "Teksta lauks ar automātisko pabeigšanu, kas rakstīšanas laikā meklē opcijas no attālā API."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

Jautājuma tips `search-autocomplete` renderē teksta ievades lauku, kas vaicā attālo API, kamēr lietotājs raksta, un parāda atbilstošos rezultātus kā nolaižamo sarakstu. Atlasītā vērtība tiek saglabāta kā teksta virkne. Atšķirībā no `select_one` ar `search-api()`, `search-autocomplete` uzskata rezultātu par vienkāršu tekstu — XLSForm nav fiksēta izvēļu saraksta.

## Pamata XLSForm specifikācija

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | Meklēt iestādi | `searchApi("/api/facilities", "name")` |

`searchApi()` izteiksme tiek ievietota kolonnā `appearance` un kontrolē, kura API galapunkts tiek vaicāts un kurš lauks no atbildes tiek izmantots kā attēlojamā vērtība.

## `searchApi()` sintakse

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| Parametrs | Obligāts | Apraksts |
|-----------|----------|----------|
| `url` | Jā | Galapunkta URL. Pievienojiet vaicājuma parametrus ar `?q=##QUERY##` — `##QUERY##` tiek aizstāts ar ierakstīto tekstu izpildes laikā |
| `display_field` | Jā | JSON lauka nosaukums no API atbildes, lai parādītu nolaižamajā sarakstā |
| `value_field` | Nē | JSON lauka nosaukums, lai saglabātu kā atbildes vērtību (pēc noklusējuma `display_field`) |

### Piemērs: meklēt iestādes, saglabāt iestādes ID

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | Iestādes nosaukums | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## Variants: `search-autocomplete-noedit`

Variants `search-autocomplete-noedit` novērš to, ka lietotājs iesniedz vērtību, kas netika atlasīta no automātiskās pabeigšanas rezultātiem. Lietotājam jāizvēlas no saraksta.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | Pacienta ID | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## Lietojums

1. Lielu atsauces datu kopu meklēšana (iestādes, darbinieki, produkti) neievietojot visas izvēles XLSForm
2. Brīva teksta lauki ar izvēles ieteikumiem (ja `search-autocomplete-noedit` netiek izmantots)
3. Saistītas uzmeklēšanas, kur atlasītā vērtība aizpilda citus laukus ar `calculate`

## Datu formāts

Saglabātā vērtība ir vienkārša virkne — vai nu `value_field` atgrieztā vērtība, vai attēlojamais teksts, ja nav norādīts `value_field`.

## Platformas atbalsts

Atbalstīts tīmekļa formās. Mobilais atbalsts ir atkarīgs no tīkla savienojamības ar API galapunktu.

## Ierobežojumi

- Datu vākšanas laikā nepieciešams tīklā pieejams API galapunkts.
- Nav daļa no standarta XLSForm specifikācijas — tikai rtSurvey paplašinājums.
- Neatbalsta bezsaistes izvēļu kešatmiņu; izmantojiet `select_one` ar `search-api()`, ja nepieciešama bezsaistes rezerve.
