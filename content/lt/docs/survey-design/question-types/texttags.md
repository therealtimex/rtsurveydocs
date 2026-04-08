---
title: "Text Tags"
description: "Žymų įvedimo laukas — respondentai rašo ir spaudžia Enter, kad sukurtų atskirus žymų žetonus."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

Klausimo tipas `texttags` (taip pat žinomas kaip `text_tags`) renderuoja įvesties lauką, kuriame kiekviena vartotojo įvesta reikšmė tampa atskiru **žymų žetonu**. Vartotojai įveda reikšmę, paspaudžia Enter arba atskyrimo klavišą, ir reikšmė pridedama kaip pašalinamas čipas. Viename atsakyme galima pridėti kelias žymas.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| texttags | keywords | Įveskite raktažodžius (po kiekvieno spauskite Enter) |

## Elgsena

- Kiekvienas patvirtintas įrašas tampa žyma, rodoma kaip pill/čipas lauke.
- Žymas galima pašalinti atskirai spustelėjus × ant čipo.
- Saugoma reikšmė yra tarpais atskirtų visų įvestų žymų eilutė.

## Naudojimo atvejai

1. Kelių laisvo teksto raktažodžių ar kodų rinkimas be iš anksto apibrėžto sąrašo
2. Žymėjimo ar kategorijų laukai, kur reikšmių rinkinys yra atviras
3. Bet kuri kelių reikšmių laisvo teksto įvestis, kur `select_multiple` yra per griežtas

## Duomenų formatas

Žymos saugomos kaip viena tarpais atskirtų eilutė. Pavyzdžiui, jei vartotojas įveda `maliarija`, `karščiavimas` ir `kosulys`, saugoma reikšmė yra `maliarija karščiavimas kosulys`.

## Platformos palaikymas

Palaikoma žiniatinklio formose.

## Apribojimai

- Nėra standartinės XLSForm specifikacijos dalis — tik rtSurvey plėtinys.
- Kadangi reikšmės yra laisvas tekstas, tolesnei analizei reikalingas eilutės skaidymas pagal tarpus.
