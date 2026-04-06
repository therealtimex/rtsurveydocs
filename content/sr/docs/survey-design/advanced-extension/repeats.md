---
title: "Napredna ponavljanja"
description: "Napredni obrasci za grupe ponavljanja: dinamički broj, ugnežđena ponavljanja, sumiranje podataka ponavljanja i referenciranje vrednosti kroz ponavljanja."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Ova stranica pokriva napredne obrasce za rad sa grupama ponavljanja u rtSurvey-u. Za osnove postavljanja grupe ponavljanja, pogledajte [Grupisanje i ponavljanja](../repeats).

---

## Dinamički broj ponavljanja

Podrazumevano, anketar odlučuje koliko puta da ponovi. Možete fiksirati broj ponavljanja koristeći `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Član domaćinstva | `${num_members}` |
| text | member_name | Ime člana | |
| integer | member_age | Godine | |
| end_repeat | | | |

Ponavljanje se izvršava tačno `${num_members}` puta, gde je `num_members` prikupljeno ranije u formularu. Anketar ne može dodavati ili uklanjati instance.

---

## Indeksovani pristup: `indexed-repeat()`

Pristupite vrednosti polja specifične instance ponavljanja **izvan** grupe ponavljanja koristeći `indexed-repeat(repeated_polje, grupa_ponavljanja, indeks)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Ovo je korisno za izgradnju rezimea polja ili referenciranje podataka "primarnog" člana nakon ponavljanja.

---

## Pozicija trenutne instance: `index()`

Unutar grupe ponavljanja, `index()` vraća poziciju trenutne instance počevši od 1. Koristite je za označavanje svakog ponavljanja ili kreiranje jedinstvenih identifikatora:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Parcela |
| note | plot_label | Broj parcele ${index()} |
| text | plot_id | ID parcele |
| end_repeat | | |

---

## Referenciranje polja u istoj instanci

Unutar ponavljanja, koristite `${ime_polja}` za referenciranje drugog polja **u istoj instanci ponavljanja**. Nije potrebno koristiti `indexed-repeat()` unutar iste petlje:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Član | |
| text | member_name | Ime | |
| integer | member_age | Godine | |
| text | school_name | Naziv škole | `${member_age} < 18` |
| end_repeat | | | |

---

## Referenciranje roditeljskih polja unutar ponavljanja

Polja izvan (iznad) grupe ponavljanja mogu se normalno referencirati sa `${ime_polja}`:

| type | name | label |
|------|------|-------|
| text | village | Naziv sela |
| begin_repeat | plots | Poljoprivredna parcela |
| note | plot_context | Parcele u ${village} |
| end_repeat | | |

---

## Sumiranje podataka ponavljanja

Koristite agregate funkcije ponavljanja **izvan** grupe ponavljanja za sumiranje:

| Funkcija | Primer | Opis |
|----------|--------|----|
| `count(group)` | `count(${household_members})` | Broj instanci |
| `sum(field)` | `sum(${loan_amount})` | Zbir numeričkog polja |
| `min(field)` | `min(${member_age})` | Minimalna vrednost |
| `max(field)` | `max(${member_age})` | Maksimalna vrednost |
| `join(sep, field)` | `join(', ', ${member_name})` | Lista razdvojena zarezima |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Uslovni broj |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Uslovni zbir |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Uslovni spoj |

### Primer: Rezime domaćinstva

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Koliko članova? | |
| begin_repeat | members | Član | `${num_members}` |
| text | member_name | Ime | |
| integer | member_age | Godine | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} članova; ${children_count} ispod 18. Odrasli: ${adult_names} | |

---

## Ugnežđena ponavljanja

Grupa ponavljanja može sadržati drugu grupu ponavljanja. Koristite ovo pažljivo — ugnežđena ponavljanja dodaju složenost i mogu zbuniti anketare.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Domaćinstvo |
| text | hh_id | ID domaćinstva |
| begin_repeat | hh_members | Član |
| text | member_name | Ime člana |
| end_repeat | | |
| end_repeat | | |

Za referenciranje polja u spoljnom ponavljanju iz unutrašnjeg ponavljanja, koristite `${ime_polja}` — ono se razrešava na najbliži odgovarajući predak:

Unutar ponavljanja `hh_members`, `${hh_id}` vraća ID **trenutnog** domaćinstva, ne svih domaćinstava.

---

## Rangiranje unutar grupa ponavljanja: `rank-index()`

Kada polje `rank` postoji unutar ponavljanja, koristite `rank-index(instanceNumber, polje_ponavljanja)` izvan da dobijete redni rang specifične instance:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` vraća indeks instance sa najvišim skorom.

---

## Najbolje prakse

1. Uvek koristite `repeat_count` kada je broj ponavljanja unapred poznat — sprečava anketare da slučajno dodaju ili uklanjaju instance.
2. Zadržite grupe ponavljanja fokusiranima — ponavljanje sa 20+ pitanja po instanci je teško za navigaciju.
3. Jasno imenujte grupe ponavljanja (npr. `household_members`, ne `repeat1`) — ime se pojavljuje u pozivima funkcija i izvezenim podacima.
4. Testirajte sa maksimalnim očekivanim brojem instanci da biste proverili performanse.
5. Koristite izgled `field-list` na grupi ponavljanja za prikaz svih polja na jednom ekranu po instanci (mobilni).

---

## Ograničenja

- `indexed-repeat()` zahteva validan indeks (1 do broja instanci) — indeksi van opsega vraćaju prazan rezultat.
- Ugnežđena ponavljanja dublja od 2 nivoa nisu preporučena i mogu izazvati probleme sa prikazom na nekim klijentima.
- Agregate funkcije (`sum`, `count`, itd.) rade na celoj grupi ponavljanja — ne možete agregirati podskup instanci bez varijanti `*-if`.
