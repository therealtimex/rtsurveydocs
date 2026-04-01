---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI umožňuje používateľom načítavať systémové metadáta z aplikácie pomocou rôznych metód vo FormEngine a DMView. Poskytuje prístup k rôznym dátovým kľúčom na načítanie špecifických informácií z aplikácie.

V xlsform môžete použiť funkciu `pulldata()` s nasledujúcou syntaxou:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Toto kľúčové slovo informuje FormEngine, aby načítal dáta z App API.
- `'data-key'`: Toto je kľúč dát, ktoré chcete načítať z App API.
- Ak je dátový kľúč neplatný alebo nepodporovaný, výpočet vráti „n/a".

Tu sú podporované dátové kľúče, ktoré môžete použiť s App-API:

`osPlatform`: Vráti aktuálny názov OS (Android alebo iOS) a verziu OS. Webové platformy vrátia prázdnu hodnotu.

`appPlatform`: Vráti názov platformy aplikácie, čo je `rtSurvey`.

`appVersion`: Vráti názov verzie aplikácie.

`getDisplayWidth`: Vráti šírku obrazovky zariadenia v pixeloch.

`getDisplayHeight`: Vráti výšku obrazovky zariadenia v pixeloch.

`getScreenSize`: Vráti veľkosť obrazovky zariadenia v palcoch.

`projectCode`: Vráti aktuálny kód projektu stránky, na ktorú sa používateľ prihlasuje.

`projectURL`: Vráti aktuálnu URL projektu stránky, na ktorú sa používateľ prihlasuje. Predvolená/záložná hodnota je prázdny text ("").

`startingPoint`: Vráti cestu bodu, ktorý spúšťa formulár. Pre viac podrobností pozrite „Počiatočný bod formulára".

`serverTime`: Vráti najlepšiu dostupnú aproximáciu dátumu a času na serveri.

`user.[attribute]`: Vráti aktuálne atribúty používateľa na základe zadaného kľúča atribútu. Pre dostupné kľúče atribútov pozrite tabuľku „Atribúty používateľa".

Kombinujte nižšie uvedené kľúče atribútov s „user." v parametroch `pulldata()` na načítanie informácií o aktuálnom používateľovi. Napríklad použite `user.username`, `user.email` atď.

| Kľúč atribútu        | Popis                          |
|----------------------|--------------------------------------|
| username             | Používateľské meno používateľa                  |
| name                 | Celé meno používateľa                 |
| staffCode            | Kód zamestnanca používateľa                     |
| phone                | Telefónne číslo používateľa              |
| email                | E-mailová adresa používateľa             |
| description          | Text popisu v informáciách o používateľovi  |
| organization_id      | ID organizácie, do ktorej používateľ patrí    |
| organization_name    | Názov organizácie, do ktorej používateľ patrí  |
| team_id              | ID tímu, do ktorého používateľ patrí            |
| supervisor_id        | ID nadriadeného používateľa            |
| is_supervisor        | 1, ak je používateľ nadriadený, 0 ak nie|

`instancePath`: Vráti aktuálnu cestu priečinka inštancie.

`appLanguage`: Vráti aktuálny jazyk aplikácie nastavený v nastaveniach aplikácie (napr. sk, en).

`openArgs.[attribute]`: Vráti argument otvorenia-formulára odoslaný z ActionButton (act_fill_form, act_get_instance). Predvolená/záložná hodnota je prázdny text ("").

`primaryAppColor`: Načíta primárnu farbu aplikácie.

---

## Príklady použitia

### Uloženie mena anketára a organizácie

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Použite ich v popisoch poznámok na účely auditu:
```
note | interviewer_info | Anketár: ${enumerator_name} (${enumerator_org})
```

### Informácie o zariadení a obrazovke

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Užitočné pri riešení problémov: exportujte `device_platform` a `app_ver` spolu s vašimi dátami na identifikáciu, ktorá verzia zariadenia bola použitá pre každé odoslanie.

### Čas servera namiesto času zariadenia

Hodiny zariadenia môžu byť nesprávne. Pre spoľahlivejší časový razítok použite `serverTime`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Podmienená logika na základe roly používateľa

Zobrazte sekciu len pre nadriadených iba nadriadeným:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Hodnotenie nadriadeného | `${is_supervisor} = '1'` |
| text | supervisor_notes | Poznámky nadriadeného | |
| end_group | | | |

### Odovzdanie argumentov z tlačidla akcie

Keď je formulár spustený z tlačidla akcie `act_fill_form` s vlastnými argumentmi:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Tlačidlo akcie musí odovzdávať argumenty so zodpovedajúcimi kľúčmi (napr. `household_id`, `task_code`).

### Použitie informácií o projekte

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Poznámky

- Všetky volania `pulldata('app-api', ...)` sú vyhodnocované pri otvorení formulára a nie sú znovu vyhodnocované dynamicky počas relácie (okrem `serverTime` a `now()`).
- Ak je kľúč nepodporovaný alebo dáta nie sú dostupné, funkcia vráti `'n/a'` (nie prázdny reťazec — testujte s `!= 'n/a'` namiesto `!= ''`).
- Hodnoty `openArgs` sú dostupné iba keď je formulár spustený z tlačidla akcie; inak vrátia prázdny reťazec.
