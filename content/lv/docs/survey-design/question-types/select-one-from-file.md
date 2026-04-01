---
title: "Atlase no faila"
description: "select_one_from_file un select_multiple_from_file dinamiski ielādē izvēles no ārēja CSV vai XML faila, kas pievienots formai."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` un `select_multiple_from_file` darbojas kā `select_one` un `select_multiple`, bet izvēles tiek ielādētas no **ārēja CSV vai XML faila**, kas pievienots formai, nevis definētas darblapā **choices**. Tas ir noderīgi, ja izvēļu saraksts ir ļoti garš, bieži mainās vai jāatjauno, nepārbūvējot visu formu.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| select_one_from_file villages.csv | village | Atlasiet ciemu |
| select_multiple_from_file services.csv | services | Kurus pakalpojumus izmantojāt? |

## CSV faila formāts

CSV failam ir jābūt šādām kolonnām:

| name | label |
|------|-------|
| village_001 | Rīga |
| village_002 | Daugavpils |
| village_003 | Jelgava |

## Labākā prakse

1. Izmantojiet `select_one_from_file` izvēļu sarakstiem ar vairāk nekā 100 vienumiem.
2. Pārliecinieties, ka CSV failu nosaukumi ir precīzi — reģistrs ir svarīgs.
3. Iekļaujiet CSV failu formas multivides pakotnes ietvaros.
