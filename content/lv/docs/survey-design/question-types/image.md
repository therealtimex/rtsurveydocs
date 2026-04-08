---
title: "Attēls"
description: "Attēlu jautājumi ļauj respondentiem uzņemt un iesniegt fotoattēlus kā daļu no aptaujas."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Jautājuma tips image XLSForms un rtSurvey ļauj respondentiem uzņemt un iesniegt fotoattēlus kā daļu no aptaujas atbildēm. Šī funkcija ir īpaši noderīga vizuālo datu vākšanai, novērojumu dokumentēšanai vai pierādījumu sniegšanai lauka aptaujās.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| image | house_photo | Uzņemiet mājokļa fotoattēlu |
| image | damage_photo | Fotografējiet bojājumu |

## Izskata iespējas

| Izskats | Apraksts |
|---------|----------|
| *(nav)* | Kameras ievade (uzņem fotoattēlu vai augšupielādē) |
| `signature` | Paraksta uztvere (tikai mobilais) |
| `draw` | Brīvas zīmēšanas apgabals (tikai mobilais) |
| `annotate` | Ļauj anotēt attēlu |
| `geotag` | Automātiski pievieno GPS koordinātas attēlam |

## Datu formāts

Saglabātā vērtība ir faila nosaukums. Pats fails tiek saglabāts atsevišķā multivides pielikumā.

## Labākā prakse

1. Optimizējiet attēlu izšķirtspēju, lai samazinātu lejupielādes izmērus.
2. Apsveriet privātumu — informējiet respondentus par fotoattēlu uzņemšanu.
3. Pārbaudiet kameras funkcionalitāti gan priekšējā, gan aizmugurējā kamerā.
4. Nodrošiniet pietiekami daudz uzglabāšanas vietas ierīcē.

## rtSurvey attēla paplašinājumi

### watermark()

Izskata variants `watermark()` pārklāj teksta ūdenszīmi uz fotoattēliem, kas uzņemti ar šo lauku. Ūdenszīme parasti satur metadatus, piemēram, enumeratora vārdu, datumu/laiku vai GPS koordinātas, kas tiek iespiesti tieši uz attēla pirms saglabāšanas.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Uzņemiet objekta fotoattēlu | `watermark("${enumerator_id} ${today()}")` |

Arguments `watermark()` funkcijai ir XPath izteiksme, kas tiek novērtēta uzņemšanas brīdī. Iegūtā virkne tiek renderēta kā ūdenszīmes teksts.

### editable

Izskata variants `editable` ļauj respondentam anotēt vai zīmēt uz uzņemtā fotoattēla pēc tā uzņemšanas. Virs attēla parādās zīmēšanas rīkjosla.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Fotografējiet un atzīmējiet problēmu zonas | editable |

{{% alert icon=" " context="info" %}}
`editable` var kombinēt ar `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
