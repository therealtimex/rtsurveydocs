---
title: "Geopoint"
description: "Pytania geopoint przechwytują współrzędne geograficzne (szerokość, długość, wysokość i dokładność) jako część ankiety."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 243
---

Typ pytania `geopoint` przechwytuje pojedynczą współrzędną GPS: szerokość geograficzną, długość geograficzną, wysokość i dokładność.

## Podstawowa specyfikacja XLSForm

| type     | name     | label                          |
|----------|----------|--------------------------------|
| geopoint | location | Zarejestruj bieżącą lokalizację |

## Dane wyjściowe

Geopoint przechowuje cztery wartości oddzielone spacją: `szerokość długość wysokość dokładność`

Przykład: `21.0285 105.8542 10.5 4.3`
