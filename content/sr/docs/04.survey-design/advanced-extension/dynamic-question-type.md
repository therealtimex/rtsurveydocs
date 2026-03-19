---
title: "Dinamički tip pitanja"
description: "Dinamički tip pitanja omogućava da tip pitanja i widget polja budu određeni u vreme izvođenja na osnovu API odgovora ili izračunate vrednosti."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Funkcija **Dinamički tip pitanja** omogućava da ulazni widget i ponašanje validacije polja budu određeni **u vreme izvođenja** a ne u vreme dizajniranja formulara. Ovo je napredno rtSurvey proširenje koje se koristi kada tip podataka za prikupljanje zavisi od konfiguracije na strani servera, API odgovora ili vrednosti prethodnog polja.

Uobičajen slučaj upotrebe je konfigurabilan kontrolni spisak za inspekciju gde server definiše koja polja su obavezna, kog su tipa (tekst, integer, izbor, itd.) i koje su opcije dostupne — bez ponovne izgradnje formulara za svaku konfiguraciju.

---

## Kako funkcioniše

Polje označeno kao dinamički tip pitanja koristi `callapi()` za preuzimanje konfiguracije iz API-ja. API odgovor definiše:

- Ulazni tip za prikaz (tekst, integer, select_one, itd.)
- Dostupne opcije (za tipove sa izborom)
- Pravila validacije

Polje je interno označeno sa `specialFeature: isDynamicQuestionType`, što govori engine formulara da koristi API odgovor za konstruisanje widgeta umesto statičke definicije formulara.

---

## Podešavanje

### Korak 1: Preuzimanje konfiguracije polja

Koristite polje `calculate` sa `callapi()` za preuzimanje dinamičke konfiguracije:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Korak 2: Referenciranje konfiguracije u dinamičkom polju

Dinamičko polje koristi `callapi-verify()` u svom `appearance` ili `constraint` za povezivanje sa preuzetom konfiguracijom:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Rezultat inspekcije | `callapi-verify(dynamicParams)` |

Engine formulara čita `field_config` i dinamički određuje da li da prikaže `inspection_result` kao `text`, `integer` ili `select_one` polje.

---

## Format API odgovora

API treba da vrati JSON objekat koji opisuje konfiguraciju polja. Tipičan odgovor:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Prošao"},
      {"value": "fail", "label": "Pao"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Primer: Konfigurabilan formular za inspekciju

Formular za inspekciju gde su stavke kontrolnog spiska i njihovi tipovi odgovora preuzeti sa servera na osnovu kategorije inspekcije:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Tip inspekcije | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Stavka 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Stavka 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Stavka 3 | `callapi-verify(dynamicParams)` | |

Server vraća ispravan tip widgeta, oznaku, opcije i validaciju za svaku stavku na osnovu `insp_type`.

---

## Najbolje prakse

1. Koristite dinamičke tipove pitanja samo kada se struktura polja zaista razlikuje u vreme izvođenja — za statičke formulare koristite standardne tipove pitanja.
2. Osigurajte da API za konfiguraciju odgovara brzo (ispod 2 sekunde) i da je dostupan na terenskoj mreži.
3. Uvek definišite razumnu alternativu u formularu za slučaj kada API nije dostupan — jednostavno `text` polje sa napomenom je bolje od pokvarenog widgeta.
4. Verzionirajte šemu API odgovora — promene u formatu odgovora će uticati na sve aktivne formulare koji koriste tu krajnju tačku.
5. Testirajte svaku kombinaciju tipova polja koje API može vratiti pre primene.

## Ograničenja

- Dinamički tipovi pitanja zahtevaju mrežnu vezu za preuzimanje konfiguracije.
- Pun opseg tipova widgeta dostupnih dinamički zavisi od verzije rtSurvey klijenta — testirajte svoju ciljnu verziju.
- Ovo je napredno rtSurvey proširenje bez ekvivalenta u standardnoj XLSForm specifikaciji.
- Greške su teže za praćenje jer definicija polja delom živi u formularu a delom u API odgovoru.
