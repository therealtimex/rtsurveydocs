---
title: "Datums un laiks, datums, laiks"
description: "Datuma un laika jautājumi ļauj respondentiem ievadīt gan datumu, gan laiku vienā laukā."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Datuma un laika jautājumu tipi XLSForms un rtSurvey ļauj vākt datumu un/vai laiku.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| date | survey_date | Aptaujas datums |
| time | interview_time | Intervijas laiks |
| datetime | event_datetime | Notikuma datums un laiks |

## Datu formāts

- **date**: Glabā kā `YYYY-MM-DD` (piemēram, `2024-03-15`)
- **time**: Glabā kā `HH:MM:SS` (piemēram, `14:32:00`)
- **datetime**: Glabā kā ISO 8601 (piemēram, `2024-03-15T14:32:00`)

## Datumu aprēķini

Lai aprēķinātu dienas starp diviem datumiem:

```
decimal-date-time(${end_date}) - decimal-date-time(${start_date})
```

## Izskata iespējas

| Izskats | Apraksts |
|---------|----------|
| `no-calendar` | Slēpj kalendāru (tikai mobilais) |
| `month-year` | Ļauj atlasīt tikai mēnesi un gadu |
| `year` | Ļauj atlasīt tikai gadu |
| `inline-[%d/%m/%Y]` | Rāda formatētu datumu |

## Labākā prakse

1. Izmantojiet `today()` kā noklusējuma vērtību datuma laukiem, ja iespējams.
2. Apsveriet laika joslas, vācot starptautiskos datos.
3. Validējiet datumu loģiku (piemēram, beigu datums pēc sākuma datuma) ar ierobežojumiem.
