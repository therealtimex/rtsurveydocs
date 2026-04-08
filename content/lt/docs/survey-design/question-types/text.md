---
title: "Tekstas"
description: "Laisvo teksto atsakymo klausimo tipas rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Klausimo tipas `text` renka laisvo teksto atsakymą — bet kokią simbolių eilutę. Tai lanksčiausias įvesties tipas, naudojamas vardams, adresams, aprašymams, kodams ir viskam, kas netinka labiau specifiniam tipui.

rtSurvey taip pat praplečia `text` **laiko įvesties valdikliais**, leidžiančiais tiksliai įvesti laiką naudojant laikrodžio rinkiklį.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| text | respondent_name | Visas respondento vardas |
| text | address | Namų adresas |

Daugiau informacijos apie standartinį XLSForm teksto tipą rasite [XLSForm specifikacijoje](https://xlsform.org/en/#question-types).

## Naudojimo atvejai

Teksto klausimai naudojami:

1. Vardams, adresams, laisviems aprašymams
2. Atviroms pastaboms ar atsiliepimams
3. Kodams, ID ar nuorodos numeriams, netinkantiems integer/decimal
4. Laiko reikšmių rinkimui naudojant rtSurvey laiko įvesties plėtinius
5. Automatiškai užbaigiamo teksto laukams (per `search-autocomplete-noedit-v2()`)

## Standartinės išvaizdos parinktys

| Išvaizda | Aprašymas |
|------------|-------------|
| *(nė viena)* | Vienos eilutės teksto įvestis |
| `multiline` | Kelių eilučių teksto sritis — geriausiai tinka ilgesniam laisvam tekstui žiniatinklyje |
| `richtext` | Raiškiojo teksto redaktorius — įrankių juosta su paryškintu, kursyviniu tekstu, sąrašais ir nuorodomis |
| `typingtest` | Rašymo testo sąsaja — pateikia ištrauką ir matuoja respondento rašymo greitį ir tikslumą |

## rtSurvey laiko įvesties plėtiniai

rtSurvey praplečia `text` **laikrodžio rinkiklio valdikliu**, skirtu laiko reikšmių rinkimui. Šios išvaizdos parinktys rodo laikrodžio piktogramą, kurią surašytojas gali paliesti, norėdamas pasirinkti valandas, minutes, sekundes ar milisekundes.

### Išvaizdos variantai

| Išvaizda | Aprašymas |
|------------|-------------|
| `inline` | Laikrodžio piktograma rodoma šalia lauko |
| `inline colors("RRGGBB")` | Laikrodžio piktograma su pasirinktine hex spalva |
| `inline-1line` | Laikrodis atvaizduojamas kompaktiškame vienos eilutės formate |
| `inline-1line-RRGGBB` | Viena eilutė su pasirinktine piktogramos spalva (hex, be `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Viena eilutė su dviem spalvomis |
| `inline-onlyresult` | Laikrodžio piktograma dingsta po pasirinkimo; rodoma tik reikšmė |
| `inline-onlyresult colors("RRGGBB")` | Tas pats, su pasirinktine piktogramos spalva |

### Laiko formato žetonai

Pridėkite formato eilutę skliaustuose, kad kontroliuotumėte, kurie laiko komponentai rodomi:

| Formato eilutė | Rodo |
|---------------|----------|
| `inline-[%H:%M]` | Valandos ir minutės (24 val.) |
| `inline-[%h:%M]` | Valandos ir minutės (12 val.) |
| `inline-[%H:%M:%S]` | Valandos, minutės, sekundės (24 val.) |
| `inline-[%h:%M:%S]` | Valandos, minutės, sekundės (12 val.) |
| `inline-[%H:%M:%3]` | Valandos, minutės, milisekundės |
| `inline-[%M:%S]` | Tik minutės ir sekundės |
| `inline-[%M:%3]` | Tik minutės ir milisekundės |
| `inline-[%S]` | Tik sekundės |
| `inline-[%3]` | Tik milisekundės |
| `inline-[%H]` | Tik valandos (24 val.) |
| `inline-[%h]` | Tik valandos (12 val.) |

### Pavyzdys: Užduoties trukmės įrašymas minutėmis ir sekundėmis

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Laikas, praleistas atliekant užduotį | `inline-[%M:%S]` |

### Pavyzdys: Įvykio laiko įrašymas 24 val. formatu su pasirinktine spalva

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Įvykio laikas | `inline-1line colors("0099FF")` |

## Duomenų formatas

Teksto duomenys saugomi ir eksportuojami kaip paprasta eilutė. Laiku pagrįstoms įvestims, naudojant inline laikrodžio valdiklį, reikšmė saugoma formate, atitinkančiame pasirinktą formato eilutę (pvz., `14:32` `%H:%M`).

## Apribojimai ir tikrinimas

Taikykite apribojimus formato, ilgio ar modelio užtikrinimui:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Visas vardas | `string-length(.) >= 2` | Vardas turi būti bent 2 simbolių |
| text | code | Nuorodos kodas | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Įveskite 2 didžiąsias raides, po kurių seka 4 skaitmenys |
| text | phone | Telefono numeris | `regex(., '^[0-9]{9,15}$')` | Įveskite galiojantį telefono numerį |

## Geriausios praktikos

1. Naudokite specifinesnius tipus (`integer`, `decimal`, `date`), kai duomenys turi žinomą struktūrą — tai neleidžia įvesti netinkamų įrašų ir supaprastina analizę.
2. Pridėkite `constraint` su `string-length()` arba `regex()` kodams ar ID tikrinti.
3. Naudokite `multiline` išvaizdą atviroms klausimams, kur respondentai gali rašyti keletą sakinių.
4. Laiko rinkimui pasirinkite laiko formato žetonus, atitinkančius jūsų analizės reikalingą tikslumą — milisekundžių rinkimas, kai reikia tik minučių, iššvaisto surašytojo pastangas.

## Platformos palaikymas

Teksto klausimo tipas ir visi laiko įvesties išvaizdos variantai yra palaikomi iOS, Android ir žiniatinklio platformose.

## Apribojimai

- Teksto atsakymai yra laisvos formos — nėra integruoto rašybos tikrinimo ar žodyno apribojimo, išskyrus regex modelius.
- Inline laiko valdiklis yra rtSurvey plėtinys ir nėra standartinės XLSForm specifikacijos dalis.
