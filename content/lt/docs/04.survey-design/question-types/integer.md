---
title: "Sveikasis skaičius"
description: "Sveikojo skaičiaus klausimai leidžia įvesti sveikuosius skaičius apklausoje."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

XLSForm ir rtSurvey sveikojo skaičiaus klausimo tipas naudojamas sveikojo skaičiaus atsakymams rinkti. Šis klausimo tipas yra būtinas skaičių duomenims be dešimtainių vietų rinkti, pvz., skaičiams, amžiui ar metams.

## Pagrindinė XLSForm specifikacija

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Įveskite savo amžių metais |

## Naudojimo atvejai

Sveikojo skaičiaus klausimai dažnai naudojami:

1. Amžiaus įvedimui
2. Elementų skaičiavimui (pvz., vaikų skaičius, namų ūkio nariai)
3. Metų įvedimui (pvz., gimimo metai)
4. Vertinimams skaitmenine skale
5. Bet kokiems sveikojo skaičiaus duomenims rinkti

## Geriausios praktikos

1. Naudokite aiškias ir glaustas etiketes, nurodančias tikėtinamą įvestį.
2. Įdiekite diapazono apribojimus, kad išvengtumėte nerealingų ar klaidingų įvesčių.
3. Apsvarstykite galimybę naudoti patarimo tekstą pavyzdžiams pateikti ar tikėtinam formatui paaiškinti.
4. Dideliems skaičiams apsvarstykite galimybę naudoti kableliais ar tarpais etiketėje skaitomumui pagerinti.

## Apribojimai ir tikrinimas

Galite pridėti apribojimų, kad užtikrintumėte, jog įvesta reikšmė yra nurodytame diapazone:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Įveskite savo amžių metais | .>0 and .<=120 | Amžius turi būti nuo 1 iki 120 metų |

## Naudojimo pavyzdys

Štai pavyzdys, kaip galima naudoti sveikojo skaičiaus klausimus namų ūkio apklausoje:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | Kiek žmonių gyvena jūsų namų ūkyje?       | .>0        | Namų ūkio dydis turi būti bent 1 |
| integer | num_children   | Kiek vaikų iki 18 metų yra namų ūkyje?    | .>=0       | Vaikų skaičius negali būti neigiamas |
| integer | year_built     | Kuriais metais buvo pastatytas jūsų namas? | .>1800 and .<=2023 | Metai turi būti nuo 1800 iki 2023 |

## Skaičiavimai su sveikojo skaičiaus reikšmėmis

Sveikojo skaičiaus reikšmės gali būti naudojamos skaičiavimuose. Štai pavyzdys:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Suaugusiųjų skaičius namų ūkyje           |
| integer | num_children   | Vaikų skaičius namų ūkyje                 |
| calculate | total_members | | 

Skaičiavimo eilutėje galite naudoti:

```
calculation | ${num_adults} + ${num_children}
```

Tai susumuos suaugusiųjų ir vaikų skaičių, kad gautumėte bendrą namų ūkio narių skaičių.
