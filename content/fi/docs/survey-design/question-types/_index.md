---
title: "Kysymystyypit"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey tukee kaikkia vakio XLSForm-kysymystyyppejä sekä useita laajennuksia. Jokainen kysymystyyppi määrittää, millaista tietoa kerätään ja miten syöttöwidgetti renderöidään laitteella.

Kysymystyypin asettamiseksi kirjoita tyypin nimi XLSFormisi **survey**-laskentataulukon `type`-sarakkeeseen.

## Tekstisyöte

| Tyyppi | Kuvaus |
|--------|--------|
| [text](text) | Vapaan tekstin vastaus — kaikki merkit sallittu |
| [integer](integer) | Kokonaisluku (ei desimaaleja) |
| [decimal](decimal) | Numero desimaalipaikoilla |
| [range](range) | Numero valittu liukusäätimellä määritetyllä min/max-alueella |

## Valinta

| Tyyppi | Kuvaus |
|--------|--------|
| [select_one listname](select-one) | Valitse täsmälleen yksi vaihtoehto listalta |
| [select_multiple listname](select-multiple) | Valitse yksi tai useampi vaihtoehto listalta |
| [rank listname](rank) | Järjestä valinnat tärkeysjärjestykseen tai prioriteetin mukaan |

## Päivämäärä ja aika

| Tyyppi | Kuvaus |
|--------|--------|
| [date](date) | Kalenteripäivämäärä (vuosi, kuukausi, päivä) |
| [time](time) | Vuorokaudenaika (tunnit, minuutit) |
| [datetime](datetime-date-time) | Yhdistetty päivämäärä ja aika |

## Sijainti

| Tyyppi | Kuvaus |
|--------|--------|
| [geopoint](geopoint) | Yksittäinen GPS-koordinaatti (leveys, pituus, korkeus, tarkkuus) |
| [geotrace](geotrace) | Reitti — sarja GPS-pisteitä muodostaen linjan |
| [geoshape](geoshape) | Alue — suljettu GPS-pisteiden monikulmio |

## Media

| Tyyppi | Kuvaus |
|--------|--------|
| [image](image) | Valokuvaus tai kuvan lataaminen |
| [audio](audio) | Äänen nauhoittaminen |
| [video](video) | Videon nauhoittaminen |
| [file](file) | Yleinen tiedoston lataaminen (PDF, asiakirja jne.) |

## Muut

| Tyyppi | Kuvaus |
|--------|--------|
| [barcode](barcode) | Viivakoodin tai QR-koodin skannaaminen |
| [note](note) | Vain luku -näyttöteksti — näyttää ohjeita tai laskettuja yhteenvetoja |
| [calculate](calculate) | Piilotettu kenttä, johon tallennetaan laskettu arvo |
| [hidden](hidden) | Piilotettu kenttä, johon tallennetaan staattinen tai esitäytetty arvo |
| [trigger / acknowledge](trigger) | Valintaruutu, jota luetteloijan on rastittava vahvistaakseen lukeneensa lausuman |
| [meta](meta) | Automaattiset metatiedot: aikaleima, laitteen tunnus, luetteloijan tiedot |

## rtSurvey-laajennukset

Nämä tyypit ovat rtSurvey-kohtaisia eivätkä ole osa XLSForm-standardimääritystä.

| Tyyppi | Kuvaus |
|--------|--------|
| [search-autocomplete](search-autocomplete) | Tekstisyöte, jossa on reaaliaikainen API-pohjainen automaattinen täydennys |
| [mentions](mentions) | Tekstikenttä `@`-maininta automaattisella täydennyksellä entiteettien tagittamiseen |
| [texttags](texttags) | Tagi-syötekenttä — jokainen merkintä muuttuu poistettavaksi chipiksi; tallennettu välilyönnein erotettu merkkijono |

Toistoryhmistä katso [Repeats](../advanced-extension/repeats)

## Miten tyyppi ja ulkoasu toimivat yhdessä

`type` määrittää **mitä tietoa kerätään**. `appearance`-sarake hallitsee **miten widget näyttää**. Monet tyypit tukevat useita ulkoasuja — esimerkiksi `select_one` voidaan näyttää radiopainikkeina, pudotusvalikkona, Likert-asteikkona tai kompaktina ruudukkona.

Katso täydellinen lista vaihtoehdoista [Ulkoasu](../appearance)-sivulta.
