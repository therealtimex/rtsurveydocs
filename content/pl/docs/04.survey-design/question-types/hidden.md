---
title: "Hidden"
description: "Ukryte pola przechowują wartości, które nigdy nie są pokazywane respondentowi — używane do przekazywania kontekstu, wstępnego wypełniania danych lub przechowywania wyników pośrednich."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Typ `hidden` przechowuje statyczną lub wstępnie wypełnioną wartość niewidoczną dla respondenta.

## Podstawowa specyfikacja XLSForm

| type   | name       | label | default                           |
|--------|------------|-------|-----------------------------------|
| hidden | enumerator |       | `pulldata('app-api', 'user.name')` |

## Typowe zastosowania

- Przechowywanie informacji o ankieterze
- Przekazywanie argumentów z przycisków akcji
- Wstępne wypełnianie pól kontekstowych
