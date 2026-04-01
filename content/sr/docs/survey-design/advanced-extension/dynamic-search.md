---
title: "Dinamička pretraga"
description: "Dinamička pretraga učitava opcije iz udaljenog API-ja u realnom vremenu dok anketar kuca, omogućavajući velike ili često ažurirane skupove podataka."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dinamička pretraga** (poznata i kao Search API) omogućava polju `select_one`, `select_multiple` ili `text` da učita opcije iz udaljenog veb servisa **u vreme izvođenja** dok anketar kuca. Ovo je pravi pristup kada je vaša lista opcija prevelika da se ugradi u CSV datoteku, često se ažurira, ili dolazi iz žive baze podataka.

---

## Izgled `search-api()`

Dinamička pretraga je konfigurisana putem kolone `appearance` koristeći funkciju `search-api()`:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametri

| Parametar | Opis |
|-----------|------|
| `method` | Uvek koristite `'POST'` |
| `url` | API krajnja tačka za upit |
| `post_body` | JSON telo poslato API-ju. Koristite `%__input__%` kao čuvar mesta za trenutni tekst pretrage anketara |
| `value_column` | Ključ u objektu odgovora koji se koristi kao sačuvana **vrednost** |
| `display` | Ključ (ili šablon) koji se koristi kao **oznaka** prikazana u padajućem meniju. Podržava `##ključ##` čuvare mesta i `@{func}` izraze |
| `data_path` | JSONPath do niza objekata rezultata u odgovoru (npr. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Naziv pod kojim se sirovi odgovor čuva za upotrebu od strane других polja |

---

## Osnovni primer

Pretraživanje zdravstvenih ustanova gde anketar kuca deo naziva ustanove:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Izaberite zdravstvenu ustanovu | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API prima `{"query": "nair"}` kada anketar kuca "nair" i vraća:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

Padajući meni prikazuje `Nairobi Central Clinic` i `Nairobi West Hospital`; sačuvana vrednost je `HF001` ili `HF002`.

---

## Napredno formatiranje prikaza

### Korišćenje šablona `##ključ##`

Prikazivanje više polja u oznaci:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Prikazuje se kao: `Nairobi Central Clinic (Nairobi)`.

### Korišćenje `@{func}` izraza

Primena uslovne logike u oznaci prikaza:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktivni rezultati prikazuju `✓ Naziv klinike`; neaktivni prikazuju `✗ Naziv klinike`.

---

## Postavljanje podrazumevane vrednosti: `search-default-api()`

Koristite `search-default-api()` posle `search-api()` za prethodno popunjavanje polja podrazumevanom opcijom učitanom iz zasebnog API poziva (npr. pri uređivanju postojećeg zapisa):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Prilagođeni separator za select_multiple: `search-default-separator()`

Za polja `select_multiple`, navedite kako se višestruko izabrane vrednosti spajaju u sačuvanom stringu:

```
appearance: search-api(...) search-default-separator(' || ')
```

Podrazumevani separator je razmak.

---

## Podržani tipovi pitanja

| Tip pitanja | Slučaj upotrebe |
|-------------|-----------------|
| `select_one` | Jednostruki izbor iz rezultata pretrage |
| `select_multiple` | Višestruki izbor iz rezultata pretrage |
| `text` | Autocomplete — anketar kuca slobodno ali može izabrati sugestiju |

---

## Korišćenje sačuvanih podataka odgovora

`save_path` čuva kompletan objekat API odgovora pod datim imenom. Druga polja ga mogu referencirati sa `pulldata()`:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Izaberite ustanovu | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Najbolje prakse

1. Osigurajte da vaša API krajnja tačka odgovara unutar 1–2 sekunde — spori API-ji čine pretragu neresponsivnom.
2. Koristite `%__input__%` u `post_body` tako da API vraća samo odgovarajuće rezultate, a ne ceo skup podataka.
3. Indeksirajte polje pretrage na strani servera (npr. Elasticsearch, full-text indeks baze podataka) za brze odgovore.
4. Ograničite rezultate na 20–50 stavki po upitu — vraćanje hiljada rezultata poražava svrhu pretrage.
5. Uključite zahtev za minimalnom dužinom unosa u API-ju da biste izbegli pokretanje širokih upita na unosima jednog karaktera.

## Ograničenja

- Dinamička pretraga zahteva mrežnu vezu — ne funkcioniše offline.
- Čuvar mesta `%__input__%` se ubacuje kao što jeste; čistite unose na strani servera da biste sprečili napade ubacivanjem.
- Složeni `@{func}` izrazi prikaza mogu imati ograničenu podršku na svim verzijama rtSurvey klijenta.
