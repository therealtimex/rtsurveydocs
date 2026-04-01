---
title: "Rank"
description: "Pitanja tipa rank dozvoljavaju ispitanicima da poređaju skup opcija po preferenciji ili prioritetu."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

Tip pitanja `rank` prikazuje listu opcija koje ispitanik mora **prevlačenjem poređati** (ili na drugi način rangirati od prvog do poslednjeg). Čuva rezultat kao listu vrednosti opcija razdvojenu razmacima u izabranom redosledu, sa opcijom najvišeg prioriteta na prvom mestu.

## Osnovna XLSForm specifikacija

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Rangirajte ove potrebe zajednice od najvažnijeg do najmanje važnog |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Čista voda |
| priorities | health | Zdravstvena zaštita |
| priorities | education | Obrazovanje |
| priorities | roads | Putevi |
| priorities | electricity | Struja |

## Format sačuvane vrednosti

Sačuvana vrednost je **lista vrednosti opcija razdvojena razmacima** u rangiranom redosledu (prvo = najviši prioritet):

```
water education health roads electricity
```

## Izvlačenje rangiranih pozicija

Koristite `selected-at()` da dobijete opciju na specifičnom rangu:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Rangirajte potrebe zajednice | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` vraća vrednost postavljenu **na prvom mestu** (indeks 0 = najviši rang).

## Upotrebe

Pitanja tipa rank se uobičajeno koriste za:

1. **Rangiranje prioriteta** — traženje od zajednica da rangiraju razvojne potrebe
2. **Poređanje preferencija** — rangiranje karakteristika proizvoda, atributa usluga ili opcija politike
3. **Poređanje stavki ispita** — raspoređivanje koraka u procesu
4. **Izbor prvih N** — u kombinaciji sa `selected-at()` za izvlačenje samo prvih 1, 2 ili 3 izbora

## Najbolje prakse

1. Zadržite listu kratku (3–7 stavki) — rangiranje postaje kognitivno iscrpljujuće izvan 7–8 opcija.
2. Koristite jasne, međusobno isključive oznake opcija.
3. Dodajte tekst napomene koji objašnjava smer rangiranja (npr. "Prevucite za poređanje: prvo = najvažnije").
4. Validirajte koristeći `count-selected(.) = x` ako trebate osigurati da su sve opcije rangirane.

## Ograničenja

- Widget za prevlačenje radi rang zahteva dodirni ekran ili miš.
- Na nekim starijim mobilnim klijentima, rank widget može pasti na interfejs za numerički unos.
- Ne možete delimično rangirati — sve opcije moraju biti poređane.
