---
title: "Note"
description: "Note-kysymykset näyttävät vain luku -tekstiä tai mediaa tiedon tai ohjeiden antamiseksi kyselyssä."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

XLSFormien ja rtSurveyn note-kysymystyyppiä käytetään näyttämään vain luku -tekstiä tai mediaa kyselyn vastaajalle. Se ei ole kysymys, joka vaatii vastausta, vaan tapa tarjota tietoja, ohjeita tai asiayhteyttä kyselyn sisällä.

## XLSForm-perusmäärittely

| type | name | label |
|------|------|-------|
| note | info_text | Tämä kysely koskee lukutottumuksiasi. |

Lisätietoja note-kysymystyypin perusteista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Note-kysymyksiä käytetään yleisesti:

1. Ohjeiden tai asiayhteyden tarjoamiseen tuleviin kysymyksiin
2. Laskettujen tulosten tai yhteenvetojen näyttämiseen
3. Kuvien tai muun median näyttämiseen
4. Kyselyn osien erottamiseen toisistaan
5. Palautteen antamiseen aiempien vastausten perusteella

## Parhaat käytännöt

1. Pidä note-teksti tiiviinä ja selkeänä vastaajan sitoutumisen ylläpitämiseksi.
2. Käytä muotoilua (lihavointi, kursivointi) tärkeän tiedon korostamiseen.
3. Harkitse median (kuvat, ääni) käyttöä ymmärtämisen parantamiseksi tarvittaessa.
4. Käytä noteja säästeliäästi kyselun täyttymisen välttämiseksi.

## Esimerkkikäyttö

Esimerkki kyselyssä:

| type | name | label |
|------|------|-------|
| note | intro | Tervetuloa lukutottumuskyselyn. Kysymme mieltymyksistäsi ja lukutaajuudestasi. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | Luet noin ${books_per_month} kirjaa kuukaudessa. |

Tässä esimerkissä käytämme noteja esittelemään kyselyä ja tarjoamaan yhteenveto lasketuista tuloksista.

## rtSurveyn laajennukset

Vaikka XLSForm-standardin note-kysymysten perusmäärittely on suoraviivainen, rtSurvey voi tarjota lisäominaisuuksia tai mukautuksia:

1. Rikastekstimuotoilu
2. Tuki upotettuun mediaan (kuvat, ääni, video)
3. Dynaamiseen sisältöön perustuen aiempiin vastauksiin
4. Mukautetut tyyliasetukset

## Edistynyt käyttö

### Ehdollinen näyttö

Voit käyttää relevant-lausekkeita notien ehdolliseen näyttämiseen:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | Olet ahkera lukija! | ${books_per_month} > 5 |

### Laskentojen sisällyttäminen

Notet voivat sisältää laskentoja dynaamisen palautteen tarjoamiseksi:

| type | name | label |
|------|------|-------|
| note | reading_time | Vastaustesi perusteella käytät noin ${books_per_month} * 5 tuntia lukemiseen kuukaudessa. |

## Rajoitukset

- Notet eivät kerää tietoja, joten niitä ei tulisi käyttää, kun tarvitset tietoja vastaajilta.
- Notien liiallinen käyttö voi tehdä kyselystä sekavan tai liian pitkän.
- Jotkut edistyneet muotoilu- tai mediavaihtoehdot eivät välttämättä tue kaikkia laitteita tai alustoja.
