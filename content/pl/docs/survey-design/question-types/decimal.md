---
title: "Decimal"
description: "Pytania decimal umożliwiają wpisywanie liczb z częścią dziesiętną w ankiecie."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

Typ pytania `decimal` służy do zbierania odpowiedzi numerycznych zawierających części dziesiętne. Jest niezbędny do gromadzenia precyzyjnych danych numerycznych takich jak pomiary, ceny lub wartości procentowe.

## Podstawowa specyfikacja XLSForm

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Podaj swoją wagę w kg    |

## Typowe zastosowania

1. Pomiary (np. waga, wzrost, odległość)
2. Dane finansowe (np. ceny, pensje)
3. Wartości procentowe
4. Dane naukowe

## Walidacja

| type    | name   | label                       | constraint          | constraint_message                      |
|---------|--------|-----------------------------|---------------------|-----------------------------------------|
| decimal | height | Podaj swój wzrost w metrach | `.>0 and .<=3`      | Wzrost musi wynosić od 0 do 3 metrów   |
