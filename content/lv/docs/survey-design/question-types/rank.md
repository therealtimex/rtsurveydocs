---
title: "Ranžēšana"
description: "Ranžēšanas jautājumi ļauj respondentiem sakārtot izvēļu kopu pēc priekšrocībām vai prioritātes."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

Jautājuma tips `rank` sniedz izvēļu sarakstu, kuras respondentam ir jāsakārto **velkot secībā** (no pirmās līdz pēdējai). Rezultāts tiek glabāts kā atstarpes atdalīts izvēles vērtību saraksts izvēlētajā secībā, ar augstākās prioritātes izvēli pirmajā vietā.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| rank priorities | important_factors | Sakārtojiet šos faktorus pēc svarīguma |

Choices darblapā:

| list_name | name | label |
|-----------|------|-------|
| priorities | cost | Izmaksas |
| priorities | quality | Kvalitāte |
| priorities | speed | Ātrums |
| priorities | support | Atbalsts |

## Datu formāts

Saglabātā vērtība ir atstarpes atdalīts izvēles vērtību saraksts izvēlētajā secībā:
`quality cost support speed`

## Labākā prakse

1. Ierobežojiet ranžēšanas sarakstu līdz 5–7 vienumiem — garāki saraksti ir apgrūtinoši respondentiem.
2. Skaidri norādiet, vai ranžē no augstākā uz zemāko vai otrādi.
3. Pārbaudiet veiktspēju mobilajās ierīcēs ar gariem sarakstiem.
