---
title: "Brūkšninis kodas"
description: "Brūkšninio kodo klausimai leidžia nuskaityti ir fiksuoti brūkšninio kodo duomenis apklausoje."
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

XLSForm ir rtSurvey brūkšninio kodo klausimo tipas leidžia naudotojams nuskaityti ir fiksuoti brūkšninio kodo duomenis tiesiogiai apklausos metu. Ši funkcija ypač naudinga inventorizacijos valdymui, produktų sekimui ar bet kuriam scenarijui, kuriame reikia greito ir tikslaus koduotos informacijos įvedimo.

## Pagrindinė XLSForm specifikacija

| type    | name          | label                       |
|---------|---------------|-----------------------------|
| barcode | product_code  | Nuskenuokite produkto brūkšninį kodą |

## Naudojimo atvejai

Brūkšninio kodo klausimai dažnai naudojami:

1. Produktų identifikavimui inventorizacijos apklausose
2. Turto sekimui lauko operacijose
3. Bilietų ar ID patvirtinimui renginiuose
4. Greitam koduotos informacijos duomenų įvedimui

## rtSurvey plėtiniai

Nors pagrindinė XLSForm specifikacija brūkšninio kodo klausimams yra paprasta, rtSurvey gali pasiūlyti papildomų funkcijų ar tinkinimų, įskaitant:

1. Kelių brūkšninio kodo formatų palaikymą (pvz., QR kodai, UPC, EAN)
2. Integraciją su įrenginio kamera brūkšniniam kodui nuskaityti
3. Rankinio įvedimo parinktį, jei brūkšninis kodas yra pažeistas ar negali būti nuskaitytas

## Geriausios praktikos

1. Užtikrinkite tinkamas apšvietimo sąlygas tiksliam brūkšninio kodo nuskaitymui.
2. Pateikite aiškias instrukcijas naudotojams, kaip pozicionuoti įrenginį nuskaitymui.
3. Įtraukite rankinio įvedimo parinktį kaip atsarginį variantą nuskaitymo sunkumų atveju.
4. Prieš diegiant apklausą, patikrinkite brūkšninio kodo nuskaitymo funkciją su įvairiais įrenginiais ir brūkšninio kodo tipais.

## Apribojimai

- Brūkšninio kodo nuskaitymo tikslumas gali skirtis priklausomai nuo įrenginio fotoaparato kokybės ir aplinkos sąlygų.
- Kai kurie senesni ar žemesnės klasės įrenginiai gali nepalaikyti brūkšninio kodo nuskaitymo.
- Tam tikri brūkšninio kodo tipai gali būti nepalaikomi, priklausomai nuo įdiegimo.

## Naudojimo pavyzdys

Štai pavyzdys, kaip galima naudoti brūkšninio kodo klausimą inventorizacijos apklausoje:

| type    | name          | label                       | hint                                      |
|---------|---------------|-----------------------------|-------------------------------------------|
| barcode | product_code  | Nuskenuokite produkto brūkšninį kodą | Padėkite brūkšninį kodą rėmelio viduje |
| integer | quantity      | Įveskite produkto kiekį     |                                           |
| note    | confirmation  | Nuskaitytas produktas: ${product_code}. Kiekis: ${quantity} |           |

Šiame pavyzdyje apklausa fiksuoja produkto brūkšninį kodą, klausia kiekio ir tada rodo patvirtinimo pastabą su nuskaityta informacija.
