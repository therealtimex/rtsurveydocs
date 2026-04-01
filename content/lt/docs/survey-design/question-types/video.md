---
title: "Vaizdo įrašas"
description: "Vaizdo įrašo klausimai leidžia respondentams įrašyti ir pateikti vaizdo failus kaip apklausos dalį."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Klausimo tipas `video` leidžia respondentams **įrašyti vaizdo įrašą** arba įkelti esamą vaizdo failą kaip apklausos atsakymo dalį. Jis naudingas vizualiniams įrodymams fiksuoti, demonstracijoms, aplinkos sąlygoms ar bet kokiai informacijai, kuriai naudinga judėjimas ir garsas kartu.

## Pagrindinė XLSForm specifikacija

| type  | name        | label                              |
|-------|-------------|-------------------------------------|
| video | demo_video  | Įrašykite trumpą demonstraciją |

Daugiau informacijos apie standartinį vaizdo klausimo tipą rasite [XLSForm specifikacijoje](https://xlsform.org/en/#question-types).

## Naudojimo atvejai

Vaizdo klausimams dažnai naudojami:

1. Lauko sąlygų dokumentavimui — kelio žala, infrastruktūros būklė, pasėlių sveikata
2. Produktų demonstracijų ar procedūrinės atitikties patikrinimų įrašymui
3. Respondentų vaizdo atsiliepimų rinkimui
4. Įrodymų, reikalaujančių erdvinio konteksto, fiksavimui (pvz., problemos srities dydis ir apimtis)
5. „Prieš/po" dokumentavimui stebėsenos ir vertinimo apklausose

## Duomenų formatas

Vaizdo failai saugomi kaip dvejetainiai priedai:

- **Formatas:** MP4 arba MOV (mobiliojo įrašymo)
- **Pavadinimas:** `{instanceID}-{fieldname}.mp4` (arba lygiavertis)
- **Saugojimas:** Įkeliamas į serverio medijos aplanką ir susiejamas su pateikimo įrašu
- **Prieiga:** Galima paleisti ir atsisiųsti iš pateikimų valdymo sąsajos

## rtSurvey plėtiniai

### Maksimali trukmė

Naudokite stulpelį `parameters`, kad apribotumėte įrašymo ilgį:

| type | name | label | parameters |
|------|------|-------|------------|
| video | site_visit | Įrašykite vietovės sąlygas | `max-duration=60` |

`max-duration` yra sekundėmis. Įrašymas automatiškai sustoja pasiekus limitą.

### Kokybė / raiška

Valdykite įrašymo raišką per `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| video | evidence | Įrašykite vaizdo įrodymą | `quality=low` |

Palaikomos reikšmės: `low` (greitesnis įkėlimas), `normal` (numatytasis), `high`. Naudokite `low` vietovėse su ribotu ryšiu.

### Esamo vaizdo įrašo įkėlimas

Mobiliajame įrenginyje respondentas gali pasirinkti **įkelti esamą vaizdo įrašą** iš įrenginio galerijos vietoje naujo įrašymo. Tai įgalinta pagal numatymą vietinėje fotoaparato/galerijos integracijoje.

### Atkūrimas prieš pateikimą

Mobiliajame įrenginyje įrašytą klipą galima peržiūrėti prieš tęsiant. Papildomos konfigūracijos nereikia.

## Naudojimo pavyzdžiai

### Vietovės apžiūros vaizdo įrašas su limitu

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| video | site_video | Įrašykite vandens tašką | Apvaikščiokite visą įrenginį. Maks. 90 sekundžių. | `max-duration=90 quality=normal` |

### Sąlyginis vaizdo įrašas — tik jei pranešama apie žalą

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | damage_found | Ar rasta žalos? | | |
| video | damage_video | Įrašykite žalos vaizdo įrašą | `${damage_found} = 'yes'` | `${damage_found} = 'yes'` |

## Geriausios praktikos

1. Nustatykite `max-duration` — neapriboti vaizdo įrašai gali lengvai viršyti 100 MB ir nepavyksta įkelti esant silpnam ryšiui.
2. Naudokite `quality=low` stebėsenos apklausoms, kur reikalingas vizualinis įrodymas, bet smulkios detalės nereikia — tai dramatiškai sumažina failo dydį.
3. Parašykite konkrečias įrašymo instrukcijas stulpelyje `hint` (pvz., „Apvaikščiokite visą pastatą, laikykite kamerą stabiliai").
4. Apsvarstykite, ar vaizdo įrašas yra būtinas — nuotrauka (`image`) dažniausiai pakanka statiniams įrodymams ir sukuria daug mažesnius failus.
5. Prieš diegimą išbandykite įkėlimo veikimą faktiniame lauko tinkle.

## Apribojimai

- Vaizdo failai yra labai dideli — 1 minutės vaizdo įrašas normalios kokybės paprastai sudaro 20–60 MB priklausomai nuo įrenginio.
- Didelių vaizdo failų įkėlimas reikalauja gero tinklo ryšio; apsvarstykite Wi-Fi sinchronizavimo reikalavimą vaizdo įrašų turtingoms formoms.
- Ne visos žiniatinklio naršyklės palaiko vaizdo įrašymą per MediaRecorder — Chrome yra patikimiausias.
- Vaizdo atsakymų analizė yra rankinė ir daug laiko reikalaujanti; naudokite taupiai ir tik tada, kai vaizdo turinys suteikia unikalią vertę.
