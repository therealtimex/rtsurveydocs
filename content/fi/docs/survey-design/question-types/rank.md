---
title: "Rank"
description: "Rank-kysymykset antavat vastaajille mahdollisuuden järjestää valinnat mieltymysten tai prioriteetin mukaan."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

`rank`-kysymystyyppi esittää valintaluettelon, jonka vastaajan on **vedettävä järjestykseen** (tai muuten sijoitettava ensimmäisestä viimeiseen). Se tallentaa tuloksen välilyönneillä eroteltuna listana valintojen arvoista valitussa järjestyksessä, korkeimman prioriteetin valinta ensin.

## XLSForm-perusmäärittely

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Sijoita nämä yhteisön tarpeet tärkeimmästä vähiten tärkeimpään |

Valinnat määritellään **choices-laskentataulukossa** kuten `select_one`:ssa:

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Sijoita nämä tarpeet tärkeimmästä vähiten tärkeimpään |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Puhdas vesi |
| priorities | health | Terveydenhuolto |
| priorities | education | Koulutus |
| priorities | roads | Tiet |
| priorities | electricity | Sähkö |

## Tallennetun arvon muoto

Tallennettu arvo on **välilyönneillä eroteltu lista** valintojen arvoista sijoitusjärjestyksessä (ensimmäinen = korkein prioriteetti):

```
water education health roads electricity
```

## Sijoitettujen positioiden poimiminen

Käytä `selected-at()`:a saadaksesi tietyssä sijoituksessa olevan valinnan:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Sijoita yhteisön tarpeet | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` palauttaa **ensimmäiselle** sijalle asetetun arvon (indeksi 0 = korkein sijoitus).

## `rank-index()`-funktion käyttö toistoryhmissä

Kun `rank`-tyyppiä käytetään toistoryhmässä, `rank-index()` antaa sinulle viitata ordinaaliseen sijoitukseen toiston ulkopuolelta:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_ranked | | rank-index(1, ${score}) |

Katso täydelliset tiedot `rank-index()`- ja `rank-index-if()`-funktioista [Funktiot — Toistettujen kenttien funktiot](../operators-and-functions/functions#repeated-field-functions).

## Käyttötarkoitukset

Rank-kysymyksiä käytetään yleisesti:

1. **Prioriteettiluokitus** — yhteisöjen pyytäminen sijoittamaan kehitystarpeet tärkeysjärjestykseen
2. **Mieltymysjärjestys** — tuotteen ominaisuuksien, palveluattribuuttien tai politiikkavaihtoehtojen sijoittaminen
3. **Koevaiheiden järjestys** — prosessin vaiheiden järjestäminen
4. **Top-N-valinta** — yhdistettynä `selected-at()`-funktion kanssa vain ylimmän 1, 2 tai 3 valinnan poimimiseen

## Parhaat käytännöt

1. Pidä lista lyhyenä (3–7 kohdetta) — sijoittaminen muuttuu kognitiivisesti raskaaksi yli 7–8 valinnan jälkeen.
2. Käytä selkeitä, toisiaan poissulkevia valintojen otsikoita sekaannusten välttämiseksi siitä, mitä "ensimmäinen" tarkoittaa.
3. Lisää ohjeteksti, jossa selitetään sijoitussuunta (esim. "Vedä järjestykseen: ensimmäinen = tärkein").
4. Validoi käyttäen `count-selected(.) = x`, jos sinun on varmistettava, että kaikki valinnat on sijoitettu.

## Rajoitukset

- Vedä-sijoitusaktiivisuus vaatii kosketusnäytön tai hiiren — se ei ehkä toimi hyvin pelkkää näppäimistöä käytettäessä.
- Joillakin vanhemmilla mobiiliasiakasohjelmilla rank-widget voi palautua numeroituun syöttöliittymään.
- Ei voi sijoittaa osittain (eli sijoittaa vain joitain valintoja) — kaikki valinnat on järjestettävä.
