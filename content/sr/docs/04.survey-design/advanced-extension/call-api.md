---
title: "Call API"
description: "Call API omogućava vašoj anketi da preuzme podatke iz spoljnog veb servisa i koristi odgovor za popunjavanje polja ili validaciju odgovora."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

Funkcija **Call API** omogućava polju ankete da uputi HTTP zahtev spoljnoj usluzi i koristi odgovor za popunjavanje izračunate vrednosti ili validaciju korisničkog unosa. Ovo omogućava pretraživanja u realnom vremenu, verifikaciju identiteta, pretraživanje barkodova i bilo koje druge provere na strani servera tokom prikupljanja podataka.

Postoje dve funkcije:

- `callapi()` — preuzima vrednost iz API-ja i čuva je u polju `calculate` ili `text`
- `callapi-verify()` — poziva API i blokira napredovanje ako odgovor ne odgovara očekivanoj vrednosti (koristi se u `constraint`)

---

## `callapi()` — Preuzimanje i čuvanje API odgovora

### Sintaksa

Postavite `callapi()` u kolonu **`calculation`** polja `calculate` ili `text`:

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```

### Parametri

| # | Parametar | Opis |
|---|-----------|------|
| 1 | `method` | HTTP metoda: `'GET'` ili `'POST'` |
| 2 | `url` | URL API krajnje tačke |
| 3 | `allowed_auto` | `1` za automatski poziv kada se polje dostigne; `0` za zahtevanje dugmeta za ručno pokretanje |
| 4 | `max_retry` | Maksimalan broj ponovnih pokušaja pri neuspehu |
| 5 | `no_overwrite` | `1` za zadržavanje postojeće vrednosti ako polje već ima jednu; `0` za uvek prepisivanje |
| 6 | `extract_expr` | JSONPath izraz za izvlačenje željene vrednosti iz odgovora (npr. `$.data.name`) |
| 7 | `timeout` | Vremensko ograničenje zahteva u milisekundama |
| 8 | `lifetime` | Koliko dugo (ms) keširani odgovor ostaje validan pre ponovnog preuzimanja |
| 9 | `response_q` | Naziv polja za čuvanje sirovog HTTP koda odgovora (npr. `${response_status}`) |
| 10 | `call_type` | *(Opciono)* Poseban mod poziva: `'lazy-upload'` ili `'lazy-upload-multiple'` |
| 11 | `post_body` | *(Opciono)* String POST tela. Referencirajte polja formulara sa `##ime_polja##` |

### Primer: GET zahtev za pretraživanje domaćinstva po ID-u

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| text | household_id | ID domaćinstva | | |
| calculate | hh_name | | callapi | `callapi('GET', concat('https://api.example.com/households/', ${household_id}), 1, 3, 0, '$.name', 10000, 0, '')` |
| note | hh_display | Domaćinstvo: ${hh_name} | | |

### Primer: POST zahtev sa JSON telom

```
callapi('POST', 'https://api.example.com/lookup', 1, 2, 0, '$.result.value', 15000, 0, '', '', '{"id": "##household_id##"}')
```

U `post_body`, koristite `##ime_polja##` za ubacivanje trenutne vrednosti bilo kojeg polja formulara.

### Izgled: `callapi`

Dodajte `callapi` u kolonu `appearance` polja da biste omogućili integraciju API poziva:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | api_result | | callapi | `callapi('GET', ...)` |

Kada je `allowed_auto` `0`, rtSurvey prikazuje **dugme "Preuzmi"** koje anketar ručno tapka.

---

## `callapi-verify()` — Validacija vrednosti putem API-ja

`callapi-verify()` blokira slanje polja dok API ne potvrdi da je uneta vrednost validna. Koristite je u koloni **`constraint`**.

### Sintaksa

```
callapi-verify(method, url, extract_expr, match_expr, timeout, constraint_mode, post_body, message)
```

### Parametri

| # | Parametar | Opis |
|---|-----------|------|
| 1 | `method` | HTTP metoda: `'GET'` ili `'POST'` |
| 2 | `url` | API krajnja tačka za verifikaciju |
| 3 | `extract_expr` | JSONPath za izvlačenje očekivane vrednosti iz odgovora |
| 4 | `match_expr` | Izraz koji poredi izvučenu vrednost sa vrednošću polja (npr. `$.status = 'valid'`) |
| 5 | `timeout` | Vremensko ograničenje zahteva u milisekundama |
| 6 | `constraint_mode` | `'soft'` za samo upozorenje; `'hard'` za blokiranje napredovanja |
| 7 | `post_body` | *(Opciono)* POST telo sa zamenom `##ime_polja##` |
| 8 | `message` | *(Opciono)* Poruka greške. Podržava više jezika: `<en>Invalid!</en><vi>Không hợp lệ!</vi>` |

### Primer: Verifikacija barkoda u registru imovine

| type | name | label | appearance | constraint | constraint_message |
|------|------|-------|------------|------------|-------------------|
| barcode | asset_code | Skenirajte barkod imovine | callapi-verify | `callapi-verify('POST', 'https://api.example.com/assets/verify', '$.valid', ". = 'true'", 10000, 'hard', '{"code": "##asset_code##"}')` | Imovina nije pronađena u registru |

### Izgled: `callapi-verify(...)`

Kolona `appearance` na polju sa `callapi-verify()` u constraint-u treba da sadrži `callapi-verify(params)` ili `callapi-verify(dynamicParams)` da signalizira rtSurvey-u da ovo polje koristi API verifikaciju.

---

## Korišćenje App API podataka zajedno sa callapi

Kombinujte `callapi()` sa `pulldata('app-api', 'user.token')` za ubacivanje tokena autentifikovanjog korisnika u vaš API zahtev:

```
callapi('POST', 'https://api.example.com/data', 1, 2, 0, '$.value', 10000, 0, '', '',
  concat('{"token":"', pulldata('app-api','user.token'), '","id":"##item_id##"}'))
```

## Najbolje prakse

1. Uvek postavite razumno `timeout` (5000–15000 ms) — ne koristite 0 ili veoma visoke vrednosti.
2. Postavite `allowed_auto=0` za verifikacije koje anketar treba svesno da pokrene (npr. provere identiteta).
3. Postavite `no_overwrite=1` kada polje može biti naknadno uređivano i ne želite da ponovljeno preuzimanje prepiše ručne ispravke.
4. Koristite `extract_expr` sa specifičnim JSONPath-om umesto oslanjanja na sirovi tekst odgovora.
5. Testirajte API pozive u offline modu — callapi će elegantno pasti i prikazati grešku, ali formular i dalje treba biti popunjiv za nekritična polja.

## Ograničenja

- Zahteva mrežnu vezu u vreme poziva — pozivi će pasti kada je uređaj offline.
- API odgovori moraju biti JSON — XML ili odgovori u čistom tekstu zahtevaju dodatno parsiranje.
- Visoka frekvencija poziva (npr. jedan API poziv po instanci ponavljanja) može usporiti navigaciju kroz formular.
