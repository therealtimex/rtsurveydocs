---
title: "Webbox"
description: "Webbox ugrađuje spoljnu veb stranicu unutar ankete kao modalni iframe, dozvoljavajući anketarima da pregledaju reference ili interaguju sa spoljnim alatima bez napuštanja formulara."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** ugrađuje spoljnu veb stranicu unutar ankete kao **modalni iskačući prozor** (iframe). Anketar tapkne dugme u tekstu oznake ili napomene, stranica se otvara u overlay-u celog ekrana unutar formulara, i kada je zatvore vraćaju se na tačno isto mesto gde su bili. Ovo vam omogućava da prikazujete referentni materijal, mape, kontrolne table ili prilagođene alate bez otvaranja zasebne kartice pregledača.

---

## Sintaksa

Ubacite HTML tag `<webbox>` direktno u kolonu `label` napomene ili polja:

```html
<webbox src='https://example.com/reference' title='Referentni vodič'>Otvori referentni vodič</webbox>
```

| Atribut | Opis |
|---------|------|
| `src` | URL za učitavanje u iframe-u. Podržava i jednostruke i dvostruke navodnike. |
| `title` | Tekst prikazan u traci zaglavlja modala. Podržava čisti tekst. |
| *(sadržaj)* | Oznaka dugmeta koje se može kliknuti, prikazana u polju ankete |

---

## Osnovni primer

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Terenski vodič'>Otvori terenski vodič</webbox>` |

Ovo prikazuje dugme sa oznakom "Otvori terenski vodič". Kada se tapkne, otvara se modal koji prikazuje veb stranicu terenskog vodiča.

---

## Ugrađivanje mape

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Mapa područja ankete'>Pogledajte mapu</webbox>` |

---

## Prosleđivanje vrednosti formulara ugraženoj stranici

Dodajte vrednosti polja formulara URL-u koristeći `concat()` u koloni `calculation` i referencirajte rezultat u oznaci:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Kontrolna tabla domaćinstva'>Otvori kontrolnu tablu</webbox>` |

{{% alert icon=" " context="warning" %}}
Atribut `src` u tagu `<webbox>` podržava reference `${ime_polja}` kada je oznaka izračunata iz polja `calculate`. Konstruišite kompletan URL u polju `calculate` i referencirajte ga.
{{% /alert %}}

---

## Interakcija sa ponavljanjem: dugmad za brisanje

Webbox takođe podržava posebne akcione tagove za upravljanje grupama ponavljanja unutar oznaka:

```html
<delete-repeat-current>Ukloni ovaj red</delete-repeat-current>
<delete-repeat-last>Ukloni poslednji red</delete-repeat-last>
```

Ovi se prikazuju kao dugmad koja brišu instance ponavljanja kada se tapknu. Postavite ih u polje `note` unutar (ili odmah posle) grupe ponavljanja:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Stavka |
| text | item_name | Naziv stavke |
| note | delete_btn | `<delete-repeat-current>Ukloni ovu stavku</delete-repeat-current>` |
| end_repeat | | |

---

## Komunikacija sa ugrađenom stranicom (postMessage)

Iframe webbox-a i nadređeni formular mogu komunicirati koristeći API `postMessage` pregledača. Roditelj šalje `init` poruku iframe-u kada se otvori. Ugrađena stranica može odgovoriti sa:

- `delete-repeat-current` — pokreće brisanje trenutne instance ponavljanja
- `delete-repeat-last` — pokreće brisanje poslednje instance ponavljanja

Ovo omogućava prilagođenim veb alatima (npr. alati za crtanje, interaktivne mape) da pokreću radnje formulara kada korisnik potvrdi radnju unutar iframe-a.

---

## Najbolje prakse

1. Koristite webbox za **referentni materijal** (smernice, tabele pretraživanja, mape) — ne za prikupljanje podataka koji treba biti u samom formularu.
2. Osigurajte da je ugrađeni URL dostupan sa mreže uređaja — webbox zahteva vezu.
3. Čuvajte ugrađenu stranicu prilagođenom za mobilne uređaje — modal je maksimalno 800px širok i 80% visine vidljivog prostora.
4. Koristite opisni tekst dugmeta (npr. "Pogledajte mapu sela") umesto generičkih oznaka ("Kliknite ovde").
5. Informišite anketare da zatvaranje modala vraća ih na anketu — neki korisnici možda ne znaju kako da zatvore overlay iframe-a.

## Ograničenja

- Webbox zahteva mrežnu vezu za učitavanje ugrađenog URL-a.
- Neke spoljne stranice blokiraju ugrađivanje u iframe-ove putem zaglavlja `X-Frame-Options` ili `Content-Security-Policy` — te stranice ne mogu biti korišćene sa webbox-om.
- Modal se zatvara kada anketar navigira dalje od pitanja — svako nesačuvano stanje u iframe-u se gubi.
- Webbox je rtSurvey proširenje veb formulara i možda neće raditi u drugim ODK-kompatibilnim klijentima.
