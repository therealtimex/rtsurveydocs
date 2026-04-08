---
title: "Tipovi pitanja"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey podržava sve standardne XLSForm tipove pitanja, plus nekoliko proširenja. Svaki tip pitanja kontroliše koje vrste podataka se prikupljaju i kako se widget za unos prikazuje na uređaju.

Da biste postavili tip pitanja, unesite naziv tipa u kolonu `type` radnog lista **survey** u vašem XLSForm-u.

## Tekstualni unos

| Tip | Opis |
|-----|------|
| [text](text) | Odgovor slobodnim tekstom — dozvoljeni su svi znakovi |
| [integer](integer) | Ceo broj (bez decimala) |
| [decimal](decimal) | Broj sa decimalnim mestima |
| [range](range) | Broj izabran sa klizača unutar definisanog min/max opsega |

## Izbor

| Tip | Opis |
|-----|------|
| [select_one listname](select-one) | Izaberite tačno jednu opciju sa liste |
| [select_multiple listname](select-multiple) | Izaberite jednu ili više opcija sa liste |
| [rank listname](rank) | Poredajte opcije po preferenciji ili prioritetu |

## Datum i vreme

| Tip | Opis |
|-----|------|
| [date](date) | Datum kalendara (godina, mesec, dan) |
| [time](time) | Doba dana (sati, minuti) |
| [datetime](datetime-date-time) | Kombinovani datum i vreme |

## Lokacija

| Tip | Opis |
|-----|------|
| [geopoint](geopoint) | Jedna GPS koordinata (geografska širina, dužina, nadmorska visina, tačnost) |
| [geotrace](geotrace) | Putanja — niz GPS tačaka koje čine liniju |
| [geoshape](geoshape) | Oblast — zatvoreni poligon GPS tačaka |

## Mediji

| Tip | Opis |
|-----|------|
| [image](image) | Snimanje fotografije ili otpremanje slike |
| [audio](audio) | Audio snimanje |
| [video](video) | Video snimanje |
| [file](file) | Generičko otpremanje datoteke (PDF, dokument, itd.) |

## Ostalo

| Tip | Opis |
|-----|------|
| [barcode](barcode) | Skeniranje barcode-a ili QR koda |
| [note](note) | Tekst samo za čitanje — prikazuje uputstva ili izračunate rezimee |
| [calculate](calculate) | Skriveno polje koje čuva izračunatu vrednost |
| [hidden](hidden) | Skriveno polje koje čuva statičku ili unapred popunjenu vrednost |
| [trigger / acknowledge](trigger) | Potvrdni okvir koji anketar mora označiti da potvrdi da je pročitao izjavu |
| [meta](meta) | Automatski metapodaci: vremenske oznake, ID uređaja, informacije o anketaru |

## rtSurvey проширења

Ови типови су специфични за rtSurvey и нису дeo стандардне XLSForm спецификације.

| Тип | Опис |
|-----|------|
| [search-autocomplete](search-autocomplete) | Текстуални унос са предлозима аутоматског довршавања на основу API-ја у реалном времену |
| [mentions](mentions) | Текстуално поље са аутоматским довршавањем `@`-помена за означавање ентитета |
| [texttags](texttags) | Поље за унос ознака — сваки унос постаје уклоњиви чип; чува се као низ раздвојен размацима |

За понављајуће групе погледајте [Repeats](../advanced-extension/repeats)

## Kako tip i izgled funkcionišu zajedno

`type` određuje **koje podatke se prikupljaju**. Kolona `appearance` kontroliše **kako widget izgleda**. Mnogi tipovi podržavaju više izgleda — na primer `select_one` može se pojaviti kao radio dugmići, padajući meni, Likertova skala ili kompaktna mreža.

Pogledajte [Izgled](../appearance) za kompletnu listu opcija.
