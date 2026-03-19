---
title: "Reitingas"
description: "Reitingo klausimai leidžia respondentams surikiuoti pasirinkimų rinkinį pagal pirmenybę ar prioritetą."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

Klausimo tipas `rank` pateikia pasirinkimų sąrašą, kurį respondentas turi **pertempti į tvarką** (arba kitaip ranguoti nuo pirmo iki paskutinio). Rezultatas saugomas kaip tarpais atskirtų pasirinkimų reikšmių sąrašas pasirinkta tvarka, aukščiausio prioriteto pasirinkimas pirmas.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Suranguokite šiuos bendruomenės poreikius nuo svarbiausio iki mažiausiai svarbaus |

Pasirinkimai apibrėžiami **pasirinkimų darbalapyje** lygiai taip pat kaip `select_one`:

**apklausa:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Suranguokite šiuos poreikius nuo svarbiausio iki mažiausiai svarbaus |

**pasirinkimai:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Švarus vanduo |
| priorities | health | Sveikatos priežiūra |
| priorities | education | Švietimas |
| priorities | roads | Keliai |
| priorities | electricity | Elektra |

## Saugomos reikšmės formatas

Saugoma reikšmė yra **tarpais atskirtų** pasirinkimų reikšmių sąrašas reitinguota tvarka (pirmas = aukščiausias prioritetas):

```
water education health roads electricity
```

## Rangiruotų pozicijų ištraukimas

Naudokite `selected-at()`, kad gautumėte pasirinkimą konkrečiame reitinge:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Suranguokite bendruomenės poreikius | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` grąžina reikšmę, pateiktą **pirmoje** vietoje (indeksas 0 = aukščiausias reitingas).

## Naudojimo atvejai

Reitingo klausimai dažnai naudojami:

1. **Prioritetų reitingavimui** — prašant bendruomenių ranguoti plėtros poreikius
2. **Pirmenybių sutvarkymui** — produkto funkcijų, paslaugų atributų ar politikos parinkčių ranguotas
3. **Egzamino elementų sutvarkymui** — proceso žingsnių sutvarkymui
4. **Geriausių N pasirinkimui** — kartu su `selected-at()` tik geriausių 1, 2 ar 3 pasirinkimų ištraukimui

## Geriausios praktikos

1. Laikykite sąrašą trumpą (3–7 elementai) — ranguoti tampa kognityviai sunku virš 7–8 pasirinkimų.
2. Naudokite aiškias, tarpusavyje nesuderinamas pasirinkimų etiketes, kad išvengtumėte painiavos dėl to, ką reiškia „pirmas".
3. Pridėkite patarimo tekstą, paaiškinantį ranguotavimo kryptį (pvz., „Tempkite norėdami sutvarkyti: pirmas = svarbiausias").
4. Tikrinkite naudodami `count-selected(.) = x`, jei reikia užtikrinti, kad visi pasirinkimai būtų suranguoti.

## Apribojimai

- Vilkimo ranguotavimo valdiklis reikalauja jutiklinio ekrano arba pelės — jis gali blogai veikti tik klaviatūros aplinkose.
- Kai kuriuose senesniuose mobiliuosiuose klientuose, reitingo valdiklis gali pereiti prie sunumeruoto įvesties sąsajos.
- Negalima dalinai ranguoti (t.y., ranguoti tik kai kuriuos pasirinkimus) — visi pasirinkimai turi būti sutvarkyti.
