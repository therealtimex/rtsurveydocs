---
title: "Ponavljajuća pitanja"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Ponavljanja su moćna funkcija u rtSurvey-u koja vam dozvoljava da prikupite isti skup informacija više puta unutar jedne ankete. Ovo je posebno korisno za scenarije poput anketa o domaćinstvima, gde možda trebate prikupiti podatke o više članova domaćinstva.

## Osnovna struktura ponavljanja

Da biste kreirali ponavljanje u rtSurvey-u, koristite konstrukt `begin repeat` i `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Ime deteta           |
| decimal      | birthweight  | Porođajna težina     |
| select_one male_female | sex | Pol deteta          |
| end repeat   |              |                      |
```

U ovom primeru, korisnik može prikupiti informacije o više dece dodavanjem novih ponavljanja u formular.

## Označavanje ponavljanja

Dok je kolona `label` opciona za `begin repeat`, dodavanje oznake može poboljšati navigaciju:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Informacije o detetu |
| text         | name         | Ime deteta           |
| decimal      | birthweight  | Porođajna težina     |
| select_one male_female | sex | Pol deteta          |
| end repeat   |              |                      |
```

rtSurvey će prikazati "Informacije o detetu" kao naslov za svaku instancu ponavljanja.

## Fiksni broj ponavljanja

Da biste specificirali fiksni broj ponavljanja, koristite kolonu `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Informacije o detetu | 3            |
| text         | name         | Ime deteta           |              |
| decimal      | birthweight  | Porođajna težina     |              |
| end repeat   |              |                      |              |
```

Ovo će kreirati tačno 3 ponavljanja za dete.

## Dinamički broj ponavljanja

rtSurvey podržava dinamičke brojeve ponavljanja zasnovane na prethodnim odgovorima:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Broj članova domaćinstva?      |                    |
| begin repeat | hh_member  | Član domaćinstva               | ${num_hh_members}  |
| text     | name           | Ime                            |                    |
| integer  | age            | Starost                        |                    |
| end repeat |              |                                |                    |
```

## Uslovna ponavljanja

Možete koristiti kolonu `relevant` za uslovni prikaz ponavljanja:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Da li ovde žive deca?     |                     |
| begin repeat      | child_repeat| Informacije o detetu      | ${has_child} = 'yes'|
| text              | name        | Ime deteta                |                     |
| decimal           | birthweight | Porođajna težina          |                     |
| end repeat        |             |                           |                     |
```

## Funkcije specifične za rtSurvey

### Rezime ponavljanja

rtSurvey pruža rezimovani prikaz ponavljanja. Za prilagođavanje rezimea, koristite grupu unutar ponavljanja:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Ime                                      |
| text         | last_name    | Prezime                                  |
| integer      | age          | Starost                                  |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Opcije izgleda ponavljanja

rtSurvey nudi dodatne opcije izgleda za ponavljanja:

- `appearance: field-list` — Prikazuje sva pitanja u ponavljanju na jednom ekranu
- `appearance: table-list` — Prikazuje ponavljanja u tabelarnom formatu

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Informacije o detetu | table-list  |
| text         | name         | Ime               |             |
| integer      | age          | Starost           |             |
| end repeat   |              |                   |             |
```

### Ugniježđena ponavljanja

rtSurvey podržava ugniježđena ponavljanja za složene strukture podataka:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Domaćinstvo          |
| text         | hh_name        | Naziv domaćinstva    |
| begin repeat | hh_member      | Član domaćinstva     |
| text         | member_name    | Ime člana            |
| integer      | member_age     | Starost člana        |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Najbolje prakse za korišćenje ponavljanja u rtSurvey-u

1. Koristite smislena imena i oznake za ponavljanja radi poboljšanja analize podataka.
2. Razmotrite korišćenje dinamičkih brojeva ponavljanja za smanjenje grešaka pri unosu podataka.
3. Temeljno testirajte formular, posebno kada koristite složena ugniježđena ponavljanja.
4. Koristite funkciju rezimea kako biste pomogli anketarima da se kreću kroz dugačke liste ponavljanja.
5. Budite oprezni sa velikim brojem ponavljanja, jer mogu uticati na performanse formulara.

## Rukovanje nultim ponavljanjima

Za predstavljanje nultih ponavljanja u rtSurvey-u:

1. Obučite anketare da obrišu prvo ponavljanje ako nije potrebno.
2. Koristite dinamičke brojeve ponavljanja kada je tačan broj poznat.
3. Koristite `relevant` za uslovno prikazivanje ponavljanja.

## Razmatranja pri izvozu podataka

Kada izvozite podatke iz rtSurvey-a, podaci ponavljanja se obično spljoštavaju. Svaka instanca ponavljanja postaje poseban red u izvezenim podacima, sa podacima roditeljskog formulara koji se ponavljaju za svaku instancu.

## Razmatranja za mobilnu aplikaciju

- Ponavljanja u rtSurvey mobilnoj aplikaciji podržavaju prikupljanje podataka van mreže.
- Veliki broj ponavljanja može uticati na performanse aplikacije na uređajima nižeg ranga.

Efikasnim korišćenjem ponavljanja u rtSurvey-u, možete kreirati fleksibilne i moćne ankete sposobne za hvatanje složenih, hijerarhijskih struktura podataka uz zadržavanje korisničkog prijatnog interfejsa za anketare.
