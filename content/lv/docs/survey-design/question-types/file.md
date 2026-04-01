---
title: "Fails"
description: "Failu jautājumi ļauj respondentiem augšupielādēt dokumentus un citus failus kā daļu no aptaujas atbildēm."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Jautājuma tips `file` ļauj respondentiem **augšupielādēt jebkuru failu** no savas ierīces — dokumentus, izklājlapas, PDF vai citus failu tipus. Atšķirībā no `image`, `audio` un `video`, kas palaiž specifiskus uzņemšanas rīkus, `file` atver vispārējas nozīmes failu izvēlētāju.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| file | consent_form | Augšupielādējiet parakstītu piekrišanas veidlapu |
| file | supporting_doc | Augšupielādējiet atbalsta dokumentu |

## Atbalstītie failu tipi

- Dokumenti: PDF, DOC, DOCX, RTF
- Izklājlapas: XLS, XLSX
- Arhīvi: ZIP
- Teksta faili: TXT

## Piezīmes

- Faila izmēra ierobežojumi var atšķirties atkarībā no servera konfigurācijas.
- Lielāki faili var palēnināt iesniegšanu zemas joslas platuma vidē.
- Apsveriet alternatīvus failu nodrošināšanas veidus ārkārtīgi lielajiem failiem.

## Labākā prakse

1. Norādiet pieļaujamos failu tipus etiķetē vai norādē.
2. Informējiet respondentus par faila izmēra ierobežojumiem.
3. Pārliecinieties, ka serveris ir konfigurēts, lai apstrādātu lielākus failu augšupielādes.
