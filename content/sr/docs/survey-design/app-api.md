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

AppAPI dozvoljava korisnicima da učitavaju sistemske metapodatke iz aplikacije koristeći različite metode u FormEngine-u i DMView-u. Pruža pristup raznim ključevima podataka za preuzimanje specifičnih informacija iz aplikacije.

U xlsform-u možete koristiti funkciju `pulldata()` sa sledećom sintaksom:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Ova ključna reč informiše FormEngine da učita podatke iz App API-ja.
- `'data-key'`: Ovo je ključ podataka koje želite da učitate iz App API-ja.
- Ako je ključ podataka nevažeći ili nije podržan, proračun će vratiti "n/a".

Evo podržanih ključeva podataka koje možete koristiti sa App-API-jem:

`osPlatform`: Vraća naziv trenutnog OS sistema (Android ili iOS) i verziju OS sistema. Veb platforme vraćaju praznu vrednost.

`appPlatform`: Vraća naziv platforme aplikacije, što je `rtSurvey`.

`appVersion`: Vraća naziv verzije aplikacije.

`getDisplayWidth`: Vraća širinu ekrana uređaja u pikselima.

`getDisplayHeight`: Vraća visinu ekrana uređaja u pikselima.

`getScreenSize`: Vraća veličinu ekrana uređaja u inčima.

`projectCode`: Vraća trenutni kod projekta sajta na koji se korisnik prijavljuje.

`projectURL`: Vraća trenutni URL projekta sajta na koji se korisnik prijavljuje. Podrazumevana/rezervna vrednost je prazan tekst ("").

`startingPoint`: Vraća putanju tačke koja pokreće formular. Pogledajte "Početna tačka formulara" za više detalja.

`serverTime`: Vraća najboljу dostupnu aproksimaciju datuma i vremena na serveru.

`user.[attribute]`: Vraća atribute trenutnog korisnika zasnovane na specificiranom ključu atributa. Pogledajte tabelu "Atributi korisnika" za dostupne ključeve atributa.

Kombinirajte dolje navedene ključeve atributa sa "user." u parametrima `pulldata()` da biste preuzeli informacije o trenutnom korisniku. Na primer, koristite `user.username`, `user.email`, itd.

| Ključ atributa       | Opis                                 |
|----------------------|--------------------------------------|
| username             | Korisničko ime korisnika              |
| name                 | Puno ime korisnika                    |
| staffCode            | Kod osoblja korisnika                 |
| phone                | Broj telefona korisnika               |
| email                | Email adresa korisnika                |
| description          | Tekst opisa u informacijama korisnika |
| organization_id      | ID organizacije kojoj korisnik pripada |
| organization_name    | Naziv organizacije kojoj korisnik pripada |
| team_id              | ID tima kojoj korisnik pripada        |
| supervisor_id        | ID supervizora korisnika              |
| is_supervisor        | 1 ako je korisnik supervizor, 0 ako nije |

`instancePath`: Vraća putanju fascikle trenutne instance.

`appLanguage`: Vraća trenutni jezik aplikacije postavljen u podešavanjima aplikacije (npr. vi, en).

`openArgs.[attribute]`: Vraća argument otvorene forme prosleđen od ActionButton-a (act_fill_form, act_get_instance). Podrazumevana/rezervna vrednost je prazan tekst ("").

`primaryAppColor`: Preuzima primarnu boju aplikacije.

---

## Primeri upotrebe

### Čuvanje korisničkog imena i organizacije anketara

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Koristite ovo u oznakama napomena za svrhe revizije:
```
note | interviewer_info | Anketar: ${enumerator_name} (${enumerator_org})
```

### Informacije o uređaju i ekranu

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Korisno za rešavanje problema: izvezite `device_platform` i `app_ver` zajedno sa podacima da biste identifikovali koja je verzija uređaja korišćena za svako slanje.

### Vreme servera umesto vremena uređaja

Satovi uređaja mogu biti pogrešni. Koristite `serverTime` za pouzdaniju vremensku oznaku:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Uslovna logika zasnovana na ulozi korisnika

Prikazujte odeljak samo za supervizore isključivo supervizorima:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Pregled supervizora | `${is_supervisor} = '1'` |
| text | supervisor_notes | Napomene supervizora | |
| end_group | | | |

### Prosleđivanje argumenata iz dugmeta za akciju

Kada je formular pokrenut iz `act_fill_form` dugmeta za akciju sa prilagođenim argumentima:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Dugme za akciju mora prosleđivati argumente sa odgovarajućim ključevima (npr. `household_id`, `task_code`).

### Korišćenje informacija o projektu

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Napomene

- Svi pozivi `pulldata('app-api', ...)` se procenjuju kada se formular otvori i ne procenjuju se ponovo dinamički tokom sesije (osim `serverTime` i `now()`).
- Ako ključ nije podržan ili podaci nisu dostupni, funkcija vraća `'n/a'` (ne prazan string — testirajte sa `!= 'n/a'` umesto `!= ''`).
- Vrednosti `openArgs` su dostupne samo kada je formular pokrenut iz dugmeta za akciju; inače vraćaju prazan string.
