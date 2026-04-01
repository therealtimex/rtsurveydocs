---
title: "Dátum-idő, dátum, idő"
description: "A dátum-idő kérdések lehetővé teszik a válaszadók számára, hogy egyetlen mezőben adjanak meg dátumot és időpontot."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Az XLSForm és az rtSurvey datetime kérdéstípusa lehetővé teszi a válaszadók számára, hogy egyetlen mezőben adjanak meg dátumot és időpontot. Ez a kérdéstípus hasznos, ha az idő egy adott pillanatát kell rögzíteni, beleértve a dátumot és a pontos időpontot.

## Alapvető XLSForm-specifikáció

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Mikor történt az esemény?       |

A datetime kérdéstípus alapvető részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A dátum-idő kérdések általánosan használt területei:

1. Események vagy megfigyelések időbélyegeinek rögzítése
2. Találkozók vagy megbeszélések ütemezése
3. Tevékenységek kezdő és záró időpontjainak naplózása
4. Pontos pillanatok rögzítése időérzékeny adatgyűjtéshez

## rtSurvey-bővítések

Az rtSurvey kiterjeszti a datetime kérdések funkcionalitását különböző megjelenési és testreszabási lehetőségekkel:

### Megjelenési lehetőségek

- `(alapértelmezett)`: Naptár és óra megjelenítése dátum és idő kiválasztásához
- `inline`: Naptár és óra megjelenítése ikonként
- `inline-1line`: Naptár és óra megjelenítése egysoros formátumban
- `inline-onlyresult`: Naptár és óra megjelenítése ikonként a sor végén; az ikonok eltűnnek a kiválasztás után

### Szín testreszabása

A naptár és az óra ikonok színe testreszabható a `colors()` függvénnyel:

- `inline colors("0099FF")`: Ikonok megjelenítése egyedi színnel
- `inline-1line-0000FF`: Megjelenítés egysoros formátumban egyedi színnel
- `inline-1line colors("0000FF","FFFF00")`: Megjelenítés egysoros formátumban több egyedi színnel
- `inline-onlyresult colors("0099FF")`: A kiválasztás után eltűnő ikonok megjelenítése egyedi színnel

### Egyedi dátum és idő formátumok

Az rtSurvey speciális szintaxissal lehetővé teszi az egyedi dátum és idő formátumokat:

- `inline-[%Y-%m-%d %H:%M:%S]`: Egyedi formátum példa (Év-Hónap-Nap Óra:Perc:Másodperc)
- `inline-[%d/%m/%Y %I:%M %p]`: Egyedi formátum példa (Nap/Hónap/Év Óra:Perc DE/DU)

## Példa

Íme egy példa arra, hogyan lehet datetime kérdést felhasználni egy felmérésben:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Mikor történt az incidens?                 | inline-[%d/%m/%Y %I:%M %p]  |

## Bevált módszerek

1. Adjon egyértelmű utasításokat a várt dátum és idő formátumról.
2. Fontolja meg az `inline` megjelenés használatát kompaktabb megjelenítéshez.
3. Akkor használjon egyedi formátumokat, ha meghatározott dátum és idő összetevőkre vagy formázásra van szüksége.
4. Különböző régiókra kiterjedő dátum-idő adatok gyűjtésekor legyen tekintettel az időzónákra.

## Korlátozások

- Egyes megjelenések vagy egyedi formátumok esetleg nem támogatottak minden eszközön vagy platformon.
- A felhasználóknak útmutatásra lehet szükségük a dátum és idő helyes megadásához, különösen egyedi formátumokkal.
- Az időzóna-különbségek bonyolíthatják az adatelemzést, ha nem megfelelően figyelembe vett.
