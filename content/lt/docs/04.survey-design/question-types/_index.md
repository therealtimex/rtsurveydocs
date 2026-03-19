---
title: "Klausimų tipai"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey palaiko visus standartinius XLSForm klausimų tipus, taip pat kelis plėtinius. Kiekvienas klausimo tipas kontroliuoja, kokie duomenys renkami ir kaip įvesties valdiklis atvaizduojamas įrenginyje.

Norėdami nustatyti klausimo tipą, įveskite tipo pavadinimą stulpelyje `type` savo XLSForm **apklausos** darbalapyje.

## Teksto įvestis

| Tipas | Aprašymas |
|------|-------------|
| [text](text) | Laisvo teksto atsakymas — leidžiami bet kokie simboliai |
| [integer](integer) | Sveikasis skaičius (be dešimtainių) |
| [decimal](decimal) | Skaičius su dešimtainėmis vietomis |
| [range](range) | Skaičius, pasirinktas iš slankiklio apibrėžtoje min/maks riboje |

## Pasirinkimas

| Tipas | Aprašymas |
|------|-------------|
| [select_one sąrašo_pavadinimas](select-one) | Pasirinkite tiksliai vieną parinktį iš sąrašo |
| [select_multiple sąrašo_pavadinimas](select-multiple) | Pasirinkite vieną ar daugiau parinkčių iš sąrašo |
| [select_one_from_file failo_pavadinimas](select-one-from-file) | Pasirinkite vieną parinktį, įkeltą iš išorinio CSV failo |
| [rank sąrašo_pavadinimas](rank) | Suranguokite pasirinkimus pagal pirmenybę ar prioritetą |

## Data ir laikas

| Tipas | Aprašymas |
|------|-------------|
| [date](datetime-date-time) | Kalendorinė data (metai, mėnuo, diena) |
| [time](datetime-date-time) | Paros laikas (valandos, minutės) |
| [datetime](datetime-date-time) | Sujungta data ir laikas |

## Vieta

| Tipas | Aprašymas |
|------|-------------|
| [geopoint](geopoint) | Viena GPS koordinatė (platuma, ilguma, aukštis, tikslumas) |
| [geotrace](geotrace) | Maršrutas — GPS taškų seka, sudaranti liniją |
| [geoshape](geoshape) | Plotas — uždaro GPS taškų daugiakampis |

## Medija

| Tipas | Aprašymas |
|------|-------------|
| [image](image) | Nuotraukos fiksavimas arba vaizdo įkėlimas |
| [audio](audio) | Garso įrašymas |
| [video](video) | Vaizdo įrašymas |
| [file](file) | Bendro failo įkėlimas (PDF, dokumentas ir kt.) |

## Kita

| Tipas | Aprašymas |
|------|-------------|
| [barcode](barcode) | Brūkšninio kodo arba QR kodo skenavimas |
| [note](note) | Tik skaitymo rodymo tekstas — rodo instrukcijas ar apskaičiuotas suvestines |
| [calculate](calculate) | Paslėptas laukas, saugantis apskaičiuotą reikšmę |
| [hidden](hidden) | Paslėptas laukas, saugantis statinę arba iš anksto užpildytą reikšmę |
| [trigger / acknowledge](trigger) | Žymimasis langelis, kurį surašytojas turi pažymėti patvirtindamas, kad perskaitė pareiškimą |
| [meta](meta) | Automatiniai metaduomenys: laiko žymės, įrenginio ID, surašytojo informacija |

## Kaip tipo ir išvaizdos sąveika veikia

`type` nustato **kokie duomenys renkami**. Stulpelis `appearance` kontroliuoja **kaip atrodo valdiklis**. Daugelis tipų palaiko kelias išvaizdas — pvz., `select_one` gali atrodyti kaip radijo mygtukai, išskleidžiamasis sąrašas, Likerto skalė ar kompaktinis tinklelis.

Pilną parinkčių sąrašą rasite [Išvaizda](../appearance).
