---
title: "Trigera / Atzīšana"
description: "Trigera jautājumi parāda paziņojumu, kuru enumeratoram ir skaidri jāapstiprina pirms turpināšanas."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Jautājuma tips `trigger` (saukts arī `acknowledge`) parāda **paziņojumu ar izvēles rūtiņu**. Enumeratoram ir jāatzīmē izvēles rūtiņa, apstiprinot, ka ir izlasījis un sapratis paziņojumu, pirms forma ļauj turpināt. Netiek glabāta nekāda datu vērtība — tikai tas, vai izvēles rūtiņa tika atzīmēta.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Es esmu paskaidrojis respondentam aptaujas mērķi un saņēmis mutvārdu piekrišanu. |
| acknowledge | safety_check | Esmu izpildījis drošības pārbaudi pirms procedūras sākšanas. |

## Lietojums

Trigera jautājumi tiek izmantoti:
- Piekrišanas procesa dokumentēšanai
- Drošības pārbaužu apstiprināšanai
- Procesuālo soļu verificēšanai
- Brīdinājumu vai svarīgu paziņojumu atzīmēšanai

## Piezīmes

- `trigger` un `acknowledge` ir sinonīmi — abi darbojas vienādi.
- Saglabātā vērtība ir `OK`, ja atzīmēts, vai tukša, ja nav atzīmēts.
- Izmantojiet `required` = `yes`, lai piespiestu enumeratoru atzīmēt rūtiņu pirms turpināšanas.

## Labākā prakse

1. Skaidri formulējiet apstiprinājuma paziņojumu.
2. Izmantojiet `required = yes`, lai nodrošinātu atzīmēšanu.
3. Apsveriet audita vajadzības — trigera jautājumi rada pierādījumus piekrišanai.
