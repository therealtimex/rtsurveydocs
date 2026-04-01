---
title: "Range"
description: "Range-kysymykset antavat vastaajille mahdollisuuden valita numeron vetämällä liukusäädintä määritellyn minimi- ja maksimiarvon välillä."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

`range`-kysymystyyppi näyttää **liukusäätimen** (tai vastaavan syötteen), jonka avulla vastaajat voivat valita numeron määritellyn minimi- ja maksimiarvon väliltä. Se on ihanteellinen arviointien, tyytyväisyyspisteytyksen tai minkä tahansa numeerisen arvon keräämiseen, joissa haluat rajoittaa alueen visuaalisesti eikä pelkästään tekstisyöttörajoittein.

## XLSForm-perusmäärittely

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Kuinka tyytyväinen olet palveluun? | start=1 end=5 step=1 |

`parameters`-sarake määrittelee liukusäätimen rajat ja askelkoon:

| Parametri | Kuvaus | Oletus |
|-----------|--------|--------|
| `start` | Minimiarvo (sisältyvä) | 0 |
| `end` | Maksimiarvo (sisältyvä) | 10 |
| `step` | Askelinkrementti kelpaavien arvojen välillä | 1 |

Lisätietoja range-kysymystyypin standardista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Range-kysymyksiä käytetään yleisesti:

1. Tyytyväisyys- tai arviointiasteikkoihin (esim. 1–5 tai 0–10)
2. Likert-tyylisiin numeerisiin asteikkoihin
3. Mittausten keräämiseen, joissa vain diskreetit arvot ovat voimassa
4. Ikäluokkiin tai pistemääräalueisiin, joissa liukusäädin parantaa käytettävyyttä tekstikenttään verrattuna

## Esimerkkikäyttö

### Perusarviointiasteikko

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Kokonaisarviointi (0–10) | start=0 end=10 step=1 |

### Desimaalivaihe

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Paino (kg) | start=0 end=200 step=0.5 |

### Arvon käyttäminen laskussa

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Testipistemäärä (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Arvosanasi on: ${grade} | | |

## Ulkoasu

`range`-tyyppi renderöidään oletuksena liukusäätimenä. Peruskäyttöön ei tarvita lisäulkoasuarvoja. Voit yhdistää sen `horizontal`-asetuksen kanssa leveämpään asetteluun verkkolomakkeissa:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Kuinka todennäköistä on, että suosittelisit meitä? (0–10) | start=0 end=10 step=1 | horizontal |

## Parhaat käytännöt

1. Aseta aina merkitykselliset `start`-, `end`- ja `step`-arvot — älä luota oletusarvoihin.
2. Merkitse asteikon päät `hint`-sarakkeessa (esim. `hint: 0 = Erittäin tyytymätön, 10 = Erittäin tyytyväinen`) antaaksesi vastaajille kontekstin.
3. 5-pisteen Likert-asteikoille käytä `start=1 end=5 step=1` eikä 0–4:ää, koska vastaajat odottavat "1":n tarkoittavan alinta.
4. Käytä `range`-tyyppiä `integer`-tyypin + rajoitteen sijaan, kun syötteen rajattu luonne on osa kysymyssuunnittelua (liukusäädin viestii asteikon visuaalisesti).

## Rajoitukset

- Liukusäädinwidget ei välttämättä sovi erittäin laajoille alueille (esim. 0–10000) — teksti-`integer` rajoittein on käyttäjäystävällisempi näissä tapauksissa.
- Mobiililaitteilla hienot askelta (esim. `step=0.1`) voi olla vaikea hallita tarkasti kosketusnäytöllä.
