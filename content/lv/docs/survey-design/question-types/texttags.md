---
title: "Text Tags"
description: "Tagu ievades lauks — respondenti ievada tekstu un nospiež Enter, lai izveidotu atsevišķus tagu tokenus."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

Jautājuma tips `texttags` (arī pazīstams kā `text_tags`) renderē ievades lauku, kur katra lietotāja ievadītā vērtība kļūst par atsevišķu **tagu tokenu**. Lietotāji ievada vērtību, nospiež Enter vai atdalītājtaustiņu, un vērtība tiek pievienota kā noņemams čips. Vienā atbildē var pievienot vairākus tagus.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| texttags | keywords | Ievadiet atslēgvārdus (nospiediet Enter pēc katra) |

## Uzvedība

- Katra apstiprinātā ievade kļūst par tagu, kas tiek attēlots kā pill/čips laukā.
- Tagus var noņemt atsevišķi, noklikšķinot uz × uz čipa.
- Saglabātā vērtība ir atstarpes atdalīta virkne no visiem ievadītajiem tagiem.

## Lietojums

1. Vairāku brīva teksta atslēgvārdu vai kodu vākšana bez iepriekš definēta saraksta
2. Marķēšanas vai kategoriju lauki, kur vērtību kopa ir atvērta
3. Jebkura vairāku vērtību brīva teksta ievade, kur `select_multiple` ir pārāk stingrs

## Datu formāts

Tagi tiek saglabāti kā viena atstarpes atdalīta virkne. Piemēram, ja lietotājs ievada `malārija`, `drudzis` un `klepus`, saglabātā vērtība ir `malārija drudzis klepus`.

## Platformas atbalsts

Atbalstīts tīmekļa formās.

## Ierobežojumi

- Nav daļa no standarta XLSForm specifikācijas — tikai rtSurvey paplašinājums.
- Tā kā vērtības ir brīvs teksts, turpmākai analīzei nepieciešama virknes sadalīšana ar atstarpēm.
