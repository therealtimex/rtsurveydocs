---
title: "Calculate"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 236
---

Typ pytania `calculate` wykonuje obliczenia oparte na wartościach innych pól i przechowuje wynik. Pole jest ukryte przed respondentem.

## Podstawowa specyfikacja XLSForm

| type      | name   | label | calculation              |
|-----------|--------|-------|--------------------------|
| calculate | bmi    |       | `${weight} / (${height} * ${height})` |

## Typowe zastosowania

- Obliczenia matematyczne (np. BMI, wiek z daty urodzenia)
- Konkatenacja ciągów znaków
- Logika warunkowa wymagająca przechowania pośrednich wyników
- Wyodrębnianie danych z API przy użyciu `callapi()`
