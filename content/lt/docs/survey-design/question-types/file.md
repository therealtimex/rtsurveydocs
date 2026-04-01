---
title: "Failas"
description: "Failų klausimai leidžia respondentams įkelti dokumentus ir kitus failus kaip apklausos atsakymų dalį."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Klausimo tipas `file` leidžia respondentams **įkelti bet kokį failą** iš savo įrenginio — dokumentus, skaičiuokles, PDF failus ar kitus tipų failus. Skirtingai nei `image`, `audio` ir `video`, paleidžiančios specifines fiksavimo priemones, `file` atidaro bendros paskirties failų parinkiklį.

## Pagrindinė XLSForm specifikacija

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Įkelkite savo dokumentą      |

## Naudojimo atvejai

Failų klausimai dažnai naudojami:

1. Patvirtinančių dokumentų rinkimui (kvitai, sertifikatai, sutartys, ataskaitos)
2. Užpildytų popieriaus formų, kurios buvo nuskaitytos, įkėlimui
3. Skaičiuoklių ar duomenų eksportų iš kitų sistemų rinkimui
4. Bet kokio skaitmeninio failo tipo, kurio neapima vaizdas/garsas/vaizdo įrašas

## Duomenų formatas

Įkelti failai saugomi kaip dvejetainiai priedai:

- **Formatas:** Išsaugomas originaliu formatu (PDF, XLSX, DOCX ir kt.)
- **Pavadinimas:** `{egzemplioriausID}-{lauko_pavadinimas}.{plėtinys}`
- **Saugykla:** Įkeltas į serverio medijos aplanką kartu su pateikimu
- **Prieiga:** Atsisiunčiamas iš pateikimų valdymo sąsajos

## rtSurvey plėtiniai

### Priimami failų tipai

Naudokite stulpelį `parameters`, kad apribotumėte, kurie failų tipai gali būti pasirinkti:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Įkelkite patikrinimo ataskaitą | `accept=.pdf` |
| file | spreadsheet | Įkelkite duomenų failą | `accept=.xlsx,.csv` |

Parametras `accept` naudoja standartinę failo plėtinio sintaksę (atskirta kableliais).

### Failo dydžio nurodymai

rtSurvey nenustatymo griežto failo dydžio limito klausimo lygyje, tačiau taikomas serverio įkėlimo limitas. Naudokite `hint`, kad perduotumėte lūkesčius surašytojui:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Įkelkite mokėjimo kvitą | Priimami: PDF arba vaizdas. Maksimalus failo dydis: 5 MB |

## Naudojimo pavyzdžiai

### Privalomas PDF įkėlimas

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Įkelkite pasirašytą sutikimo formą | Tik PDF, maks. 2 MB | yes | Sutikimo forma yra privaloma |

### Sąlyginis dokumento įkėlimas

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Ar namų ūkis turi žemės nuosavybės dokumentą? | |
| file | land_title_doc | Įkelkite žemės nuosavybės dokumento nuotrauką ar nuskaitymą | `${has_land_title} = 'yes'` |

## Geriausios praktikos

1. Naudokite `accept`, kad apribotumėte failų tipus — tai neleidžia surašytojams atsitiktinai įkelti netinkamų failų.
2. Visada įtraukite dydžio ir formato nurodymus stulpelyje `hint`.
3. Nuotraukoms ir vaizdams naudokite tipą `image` — jis siūlo geresnę suspaudimą ir nuoseklų formato tvarkymą.
4. Didelėms apklausoms su failų priedais, atitinkamai planuokite duomenų saugyklą ir atsisiuntimo pralaidumą.
5. Prieš diegimą patikrinkite failų parinkiklį tikslinių įrenginių tipuose (Android vs. iOS vs. žiniatinklis) — prieiga prie debesies diskų skiriasi.

## Apribojimai

- Failų klausimai netikrina failų turinio — tik failo plėtinio patikrinimas per `accept` taikomas UI lygyje.
- Labai dideli failai (100 MB+) gali baigti laiką įkeliant žemo ryšio aplinkoje.
- Neprisijungę surašytojai gali pridėti failus, bet jie nebus įkelti, kol bus atstatytas ryšys.
- Kai kurios įrenginių konfigūracijos riboja prieigą prie tam tikrų saugyklos vietų (pvz., įmonės MDM politikos).
