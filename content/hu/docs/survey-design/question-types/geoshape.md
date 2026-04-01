---
title: "Geoshape"
description: "A geoshape kérdések lehetővé teszik a válaszadók számára, hogy alakzatokat rajzoljanak a térképre, összetett földrajzi adatokat rögzítve."
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

Az XLSForm és az rtSurvey geoshape kérdéstípusa lehetővé teszi a válaszadók számára, hogy alakzatokat (sokszögeket) rajzoljanak a térképre összetett földrajzi adatok rögzítéséhez. Ez a funkció különösen hasznos területek feltérképezéséhez, határok meghatározásához vagy térbeli felmérésekben érdekes régiók megjelöléséhez.

## Alapvető XLSForm-specifikáció

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Rajzolja meg a mező határát     |

A geoshape kérdéstípus alapvető részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A geoshape kérdések általánosan használt területei:

1. Mezőhatárok feltérképezése mezőgazdasági felmérésekben
2. Környezeti hatásterületek meghatározása
3. Zónák megjelölése városrendezési tanulmányokban
4. Geológiai felmérések területeinek körvonalazása
5. Összetett földrajzi jellemzők rögzítése térbeli elemzéshez

## Bevált módszerek

1. Győződjön meg arról, hogy az eszközön engedélyezve van a helymeghatározó szolgáltatás és megvannak az engedélyek.
2. Adjon egyértelmű utasításokat az alakzat rajzolásának módjáról és a belefoglalandó területről.
3. Fontolja meg műholdképek vagy alaptérképek használatát a válaszadók pontos alakzatrajzolásának segítéséhez.
4. Legyen tekintettel az alakzatok lehetséges összetettségére és annak hatására az adatok méretére és feldolgozására.

## Példa

Íme egy példa arra, hogyan lehet geoshape kérdést felhasználni egy felmérésben:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Rajzolja meg az erdőfolt határát           | Legalább 3 pontot használjon a zárt alakzat létrehozásához |

## rtSurvey-bővítések

Bár az alapvető XLSForm-specifikáció egyszerű a geoshape kérdéseknél, az rtSurvey további funkciókat kínálhat:

1. Integráció offline térképekkel távoli területeken
2. Az alakzat pontjainak minimális és maximális számát beállító lehetőségek
3. Az alakzatok szerkesztésének és finomításának képessége a kezdeti rajzolás után
4. Különböző alakzattípusok támogatása (pl. téglalapok, körök) a szabad sokszögek mellett

## Adatformátum

A geoshape adatok általában szóközzel elválasztott koordinátapárokból álló, zárójelbe tett karakterláncként kerülnek tárolásra:

```
(lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN)
```

Például:
```
(38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404; 38.253094215699576 21.756382658677467)
```

## Elemzési szempontok

A geoshape kérdések használatakor vegye figyelembe:

1. A földrajzi adatok vizualizálásának és elemzésének módját (pl. GIS-szoftver)
2. Az összetett alakzatok esetleges adattisztítási vagy -egyszerűsítési szükségletét
3. Az adatvédelmi és adatbiztonsági intézkedéseket a részletes térbeli adatok kezeléséhez
4. Integrációt más térbeli adatforrásokkal az átfogó elemzés érdekében

## Korlátozások

- Pontos alakzatok rajzolása kis mobilképernyőkön kihívást jelenthet.
- Az összetett alakzatok jelentős tárhelyet és feldolgozási kapacitást igényelhetnek.
- A geoshape kérdések nem minden típusú felméréshez vagy válaszadóhoz megfelelők.
- A részletes térbeli adatok gyűjtésével adatvédelmi aggályok merülhetnek fel.
