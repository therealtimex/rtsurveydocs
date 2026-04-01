---
title: "Diapazons"
description: "Diapazona jautājumi ļauj respondentiem izvēlēties skaitli, velkot slīdni starp definēto minimālo un maksimālo vērtību."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

Jautājuma tips `range` parāda **slīdni** (vai līdzvērtīgu ievadi), kas ļauj respondentiem izvēlēties skaitli definētajā minimuma un maksimuma diapazonā. Tas ir ideāls vērtējumu, apmierinātības rezultātu vai jebkuras skaitliskas vērtības vākšanai, kur vēlaties vizuāli ierobežot diapazonu, nevis paļauties uz teksta ievadi ar ierobežojumiem.

## Pamata XLSForm specifikācija

| type | name | label | parameters |
|------|------|-------|-----------|
| range | satisfaction | Cik apmierināts esat ar pakalpojumu? | start=1 end=10 step=1 |

## Parametri

| Parametrs | Apraksts |
|-----------|-------------|
| `start` | Minimālā vērtība (noklusējums: 1) |
| `end` | Maksimālā vērtība (noklusējums: 10) |
| `step` | Solis starp vērtībām (noklusējums: 1) |

## Lietojums

Diapazona jautājumi tiek izmantoti:
- Apmierinātības vērtējumiem (piemēram, 1–10 skala)
- Intensitātes vai biežuma mērīšanai
- Jebkurai skaitliskai vērtībai ar zināmu diapazonu

## Labākā prakse

1. Skaidri norādiet skalas minimumu un maksimumu etiķetē vai norādē.
2. Izmantojiet diapazona soļi, kas ir intuitīvi respondentiem.
3. Apsveriet Likerta skalu jautājumu kopsavilkumam.
