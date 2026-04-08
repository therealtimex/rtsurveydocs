---
title: "Jautājumu tipi"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey atbalsta visus standarta XLSForm jautājumu tipus, kā arī vairākus paplašinājumus. Katrs jautājuma tips kontrolē, kāda veida dati tiek savākti un kā ievades logrīks tiek renderēts ierīcē.

Lai iestatītu jautājuma tipu, ievadiet tipa nosaukumu kolonnā `type` darblapā **survey** jūsu XLSForm.

## Teksta ievade

| Tips | Apraksts |
|------|-------------|
| [text](text) | Brīva teksta atbilde — atļautas jebkādas rakstzīmes |
| [integer](integer) | Vesels skaitlis (bez decimāldaļām) |
| [decimal](decimal) | Skaitlis ar decimāldaļām |
| [range](range) | Skaitlis, kas atlasīts no slīdņa definētā minimuma/maksimuma diapazonā |

## Atlase

| Tips | Apraksts |
|------|-------------|
| [select_one listname](select-one) | Izvēlieties tieši vienu iespēju no saraksta |
| [select_multiple listname](select-multiple) | Izvēlieties vienu vai vairākas iespējas no saraksta |
| [rank listname](rank) | Sakārtojiet izvēles pēc priekšrocībām vai prioritātes |

## Datums un laiks

| Tips | Apraksts |
|------|-------------|
| [date](date) | Kalendāra datums (gads, mēnesis, diena) |
| [time](time) | Diennakts laiks (stundas, minūtes) |
| [datetime](datetime-date-time) | Kombinēts datums un laiks |

## Atrašanās vieta

| Tips | Apraksts |
|------|-------------|
| [geopoint](geopoint) | Viena GPS koordināta (platums, garums, augstums, precizitāte) |
| [geotrace](geotrace) | Ceļš — GPS punktu virkne, kas veido līniju |
| [geoshape](geoshape) | Apgabals — slēgts GPS punktu daudzstūris |

## Multivide

| Tips | Apraksts |
|------|-------------|
| [image](image) | Foto uzņemšana vai attēla augšupielāde |
| [audio](audio) | Audio ierakstīšana |
| [video](video) | Video ierakstīšana |
| [file](file) | Vispārēja faila augšupielāde (PDF, dokuments u.c.) |

## Citi

| Tips | Apraksts |
|------|-------------|
| [barcode](barcode) | Svītrkoda vai QR koda skenēšana |
| [note](note) | Tikai lasāms teksts — rāda norādījumus vai aprēķinātus kopsavilkumus |
| [calculate](calculate) | Slēpts lauks, kas glabā aprēķinātu vērtību |
| [hidden](hidden) | Slēpts lauks, kas glabā statisku vai iepriekš aizpildītu vērtību |
| [trigger / acknowledge](trigger) | Izvēles rūtiņa, kuru enumeratoram jāatzīmē, apstiprinot, ka ir izlasījis paziņojumu |
| [meta](meta) | Automātiski metadati: laika zīmogi, ierīces ID, enumeratora informācija |

## rtSurvey paplašinājumi

Šie tipi ir rtSurvey specifiski un nav daļa no standarta XLSForm specifikācijas.

| Tips | Apraksts |
|------|----------|
| [search-autocomplete](search-autocomplete) | Teksta ievade ar reāllaika API balstītiem automātiskās pabeigšanas ieteikumiem |
| [mentions](mentions) | Teksta lauks ar `@`-pieminēšanas automātisko pabeigšanu entitāšu atzīmēšanai iekšrindiski |
| [texttags](texttags) | Tagu ievades lauks — katrs ieraksts kļūst par noņemamu žetonu; saglabāts kā atstarpi atdalīta virkne |

Par atkārtojumu grupām skatiet [Repeats](../advanced-extension/repeats)

## Kā tips un izskats darbojas kopā

`type` nosaka **kāda veida dati tiek savākti**. Kolonna `appearance` kontrolē **kā logrīks izskatās**. Daudzi tipi atbalsta vairākus izskata variantus — piemēram, `select_one` var parādīties kā radio pogas, nolaižamais saraksts, Likerta skala vai kompakts režģis.

Skatiet [Izskatu](../appearance) pilnam iespēju sarakstam.
