---
title: "Mentions"
description: "Teksta lauks ar @-pieminēšanas automātisko pabeigšanu lietotāju vai entitāšu atzīmēšanai iekšrindiski."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

Jautājuma tips `mentions` ir teksta ievade, kas aktivizē automātiskās pabeigšanas nolaižamo sarakstu, kad lietotājs raksta `@`. To izmanto, lai atzīmētu lietotājus, darbinieku vārdus, kodus vai jebkuru entitāti iekšrindiski brīva teksta atbildē.

## Pamata XLSForm specifikācija

| type | name | label |
|------|------|-------|
| mentions | note_text | Ievadiet novērojumu piezīmes (izmantojiet @ lai atzīmētu darbinieku) |

## Uzvedība

- Standarta rakstīšana rada parasto tekstu.
- Rakstot `@` kam seko rakstzīmes, tiek aktivizēta automātiskās pabeigšanas meklēšana pret konfigurētu sarakstu vai API.
- Atlasot ieteikumu, teksts tiek ievietots kā pieminēšanas tokens.
- Saglabātā vērtība ir pilna teksta virkne, ieskaitot visus iegultus pieminēšanas tokenus.

## Lietojums

1. Kvalitatīvas piezīmes, kas atsaucas uz konkrētiem darbiniekiem vai entitātēm pēc nosaukuma
2. Novērojumu ieraksti, kur jāatzīmē vairākas personas vai atrašanās vietas
3. Jebkurš brīva teksta lauks, kur kontrolētas iekšrindas atsauces uzlabo turpmāko analīzi

## Platformas atbalsts

Atbalstīts tīmekļa formās.

## Ierobežojumi

- Nav daļa no standarta XLSForm specifikācijas — tikai rtSurvey paplašinājums.
- Pieminēšanu saraksta avots (statisks vai API virzīts) tiek konfigurēts servera līmenī, nevis XLSForm.
