---
title: "Kérdéstípusok"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

Az rtSurvey az összes standard XLSForm-kérdéstípust támogatja, valamint számos bővítménnyel rendelkezik. Minden kérdéstípus meghatározza, hogy milyen típusú adatot gyűjt, és hogyan jelenik meg a beviteli widget az eszközön.

A kérdéstípus beállításához írja be a típus nevét az XLSForm **survey** munkalapjának `type` oszlopába.

## Szöveges bevitel

| Típus | Leírás |
|------|-------------|
| [text](text) | Szabad szöveges válasz – bármilyen karakter megengedett |
| [integer](integer) | Egész szám (tizedes jegy nélkül) |
| [decimal](decimal) | Tizedes jegyeket tartalmazó szám |
| [range](range) | Meghatározott minimum és maximum értékek közötti csúszka |

## Kiválasztás

| Típus | Leírás |
|------|-------------|
| [select_one listanév](select-one) | Pontosan egy lehetőség kiválasztása a listából |
| [select_multiple listanév](select-multiple) | Egy vagy több lehetőség kiválasztása a listából |
| [select_one_from_file fájlnév](select-one-from-file) | Egy lehetőség kiválasztása külső CSV-fájlból |
| [rank listanév](rank) | Lehetőségek sorrendbe helyezése preferencia vagy prioritás szerint |

## Dátum és idő

| Típus | Leírás |
|------|-------------|
| [date](date) | Naptári dátum (év, hónap, nap) |
| [time](time) | Napszak (óra, perc) |
| [datetime](datetime-date-time) | Kombinált dátum és időpont |

## Helyszín

| Típus | Leírás |
|------|-------------|
| [geopoint](geopoint) | Egyetlen GPS-koordináta (szélességi fok, hosszúsági fok, tengerszint feletti magasság, pontosság) |
| [geotrace](geotrace) | Útvonal – GPS-pontok sorozata vonallá alkotva |
| [geoshape](geoshape) | Terület – GPS-pontokból alkotott zárt sokszög |

## Média

| Típus | Leírás |
|------|-------------|
| [image](image) | Fotórögzítés vagy képfeltöltés |
| [audio](audio) | Hangfelvétel |
| [video](video) | Videófelvétel |
| [file](file) | Általános fájlfeltöltés (PDF, dokumentum stb.) |

## Egyéb

| Típus | Leírás |
|------|-------------|
| [barcode](barcode) | Vonalkód vagy QR-kód beolvasása |
| [note](note) | Csak olvasható megjelenítési szöveg – utasítások vagy számított összefoglalók megjelenítése |
| [calculate](calculate) | Rejtett mező, amely számított értéket tárol |
| [hidden](hidden) | Rejtett mező, amely statikus vagy előzetesen kitöltött értéket tárol |
| [trigger / acknowledge](trigger) | Jelölőnégyzet, amelyet a kérdezőnek be kell pipálnia egy kijelentés elolvasásának megerősítéséhez |
| [meta](meta) | Automatikus metaadatok: időbélyegek, eszközazonosító, kérdező adatai |

## A típus és a megjelenés együttműködése

A `type` meghatározza, **milyen adatot gyűjt**. Az `appearance` oszlop szabályozza, **hogyan néz ki a widget**. Sok típus több megjelenést is támogat – például a `select_one` megjelenhet rádiógombokként, legördülő menüként, Likert-skálaként vagy kompakt rácsban.

A lehetőségek teljes listájáért lásd: [Megjelenés](../appearance).
