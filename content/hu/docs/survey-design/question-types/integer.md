---
title: "Integer"
description: "Az integer kérdések egész számok bevitelét teszik lehetővé a felmérésben."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

Az XLSForm és az rtSurvey integer kérdéstípusa egész számú válaszok gyűjtésére szolgál. Ez a kérdéstípus elengedhetetlen tizedesjegyek nélküli numerikus adatok – például darabszámok, korhatárok vagy évszámok – gyűjtéséhez.

## Alapvető XLSForm-specifikáció

| type    | name  | label                      |
|---------|-------|----------------------------|
| integer | age   | Adja meg korát években     |

Az integer kérdéstípus alapvető részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

Az integer kérdések általánosan használt területei:

1. Kor megadása
2. Elemek számlálása (pl. gyerekek, háztartási tagok száma)
3. Évszám megadása (pl. születési év)
4. Numerikus skálán végzett értékelések
5. Bármilyen egész számot igénylő numerikus adatgyűjtés

## rtSurvey-bővítések

Bár az alapvető XLSForm-specifikáció egyszerű az integer kérdéseknél, az rtSurvey további funkciókat kínálhat:

1. Tartomány-érvényesítés
2. Egyéni hibaüzenetek
3. Megjelenési lehetőségek a számbevitelhez

## Bevált módszerek

1. Használjon egyértelmű és tömör feliratokat a várt bevitel és formátum megjelöléséhez.
2. Alkalmazzon tartomány-korlátokat az irreális vagy hibás bevitelek megelőzéséhez.
3. Fontolja meg súgószöveg hozzáadását a várt formátum példáinak megadásához.
4. Nagy számok esetén jelezze a várható nagyságrendet a feliratban vagy súgóban (pl. „Adja meg a népességet (legfeljebb 1 000 000)").

## Korlátok és ellenőrzés

Korlátokat adhat hozzá, hogy biztosítsa, hogy a megadott érték egy adott tartományba essen:

| type    | name  | label                      | constraint        | constraint_message                       |
|---------|-------|----------------------------|-------------------|------------------------------------------|
| integer | age   | Adja meg korát években     | .>0 and .<=120    | A kornak 1 és 120 év közé kell esnie     |

## Példa

Íme egy példa arra, hogyan lehet integer kérdéseket felhasználni egy háztartási felmérésben:

| type    | name           | label                                       | constraint           | constraint_message                            |
|---------|----------------|---------------------------------------------|----------------------|-----------------------------------------------|
| integer | household_size | Hányan laknak a háztartásban?               | .>0                  | A háztartás mérete legalább 1 kell legyen      |
| integer | num_children   | Hány 18 év alatti gyermek él a háztartásban? | .>=0               | A gyermekek száma nem lehet negatív            |
| integer | year_built     | Melyik évben épült a háza?                  | .>1800 and .<=2023   | Az évnek 1800 és 2023 közé kell esnie         |

## Számítás integer értékekkel

Az integer értékek felhasználhatók számításokban. Íme egy példa:

| type    | name           | label                                       |
|---------|----------------|---------------------------------------------|
| integer | num_adults     | Felnőttek száma a háztartásban              |
| integer | num_children   | Gyermekek száma a háztartásban              |
| calculate | total_members | |

A calculate sorban a következőt használhatja:

```
calculation | ${num_adults} + ${num_children}
```

Ez a felnőttek és gyermekek számát összeadva adja meg a háztartás összlétszámát.
