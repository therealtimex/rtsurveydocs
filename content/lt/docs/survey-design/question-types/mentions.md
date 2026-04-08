---
title: "Mentions"
description: "Teksto laukas su @-paminėjimų automatiniu papildymu vartotojų ar objektų žymėjimui eilutėje."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

Klausimo tipas `mentions` yra teksto įvestis, kuri aktyvina automatinio papildymo išskleidžiamąjį sąrašą, kai vartotojas įveda `@`. Jis naudojamas žymėti vartotojus, darbuotojų vardus, kodus arba bet kurį objektą eilutėje laisvo teksto atsakyme.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| mentions | note_text | Įveskite stebėjimo pastabas (naudokite @ darbuotojui pažymėti) |

## Elgsena

- Standartinis rašymas sukuria įprastą tekstą.
- Rašant `@` ir po to simbolius, aktyvinama automatinio papildymo paieška pagal sukonfigūruotą sąrašą arba API.
- Pasirinkus pasiūlymą, paminėjimo žetonas įterpiamas į tekstą.
- Saugoma reikšmė yra visa teksto eilutė, įskaitant bet kokius įterptus paminėjimo žetonus.

## Naudojimo atvejai

1. Kokybinės pastabos, nurodančios konkrečius darbuotojus ar objektus vardais
2. Stebėjimo įrašai, kuriuose reikia žymėti kelis asmenis ar vietas
3. Bet kuris laisvo teksto laukas, kur kontroliuojamos eilutinės nuorodos pagerina tolesnę analizę

## Platformos palaikymas

Palaikoma žiniatinklio formose.

## Apribojimai

- Nėra standartinės XLSForm specifikacijos dalis — tik rtSurvey plėtinys.
- Paminėjimų sąrašo šaltinis (statinis arba API valdomas) konfigūruojamas serverio lygiu, o ne XLSForm.
