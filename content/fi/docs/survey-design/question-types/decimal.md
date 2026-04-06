---
title: "Decimal"
description: "Decimal-kysymykset mahdollistavat numeerisen syötteen desimaaliosalla kyselyssä."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

XLSFormien ja rtSurveyn decimal-kysymystyyppiä käytetään keräämään numeerisia vastauksia, joihin voi sisältyä desimaaliosia. Tämä kysymystyyppi on välttämätön tarkan numeerisen tiedon keräämiseen, kuten mittauksiin, hintoihin tai prosenttiosuuksiin.

## XLSForm-perusmäärittely

| type    | name   | label                       |
|---------|--------|-----------------------------|
| decimal | weight | Syötä painosi kilogrammoina |

Lisätietoja decimal-kysymystyypin perusteista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Decimal-kysymyksiä käytetään yleisesti:

1. Mittauksiin (esim. paino, pituus, etäisyys)
2. Taloudelliseen tietoon (esim. hinnat, palkat)
3. Prosenttiosuuksiin
4. Tieteelliseen tiedon keräämiseen
5. Mihin tahansa numeeriseen tietoon, joka vaatii tarkkuutta kokonaislukujen yli

## Parhaat käytännöt

1. Käytä selkeitä ja ytimekkäitä otsikoita odotetun syötteen ja mittayksikön määrittelemiseksi.
2. Toteuta aluerajoitteet epärealististen tai virheellisten syötteiden estämiseksi.
3. Harkitse ohjetekstin käyttöä esimerkkien antamiseksi tai odotetun muodon selventämiseksi.
4. Määrittele haluttu desimaalien määrä otsikossa tai vihjeessä, jos tarkkuus on tärkeää.

## Rajoitteet ja validointi

Voit lisätä rajoitteita varmistaaksesi, että syötetty arvo on tietyllä alueella:

| type    | name   | label                          | constraint        | constraint_message                       |
|---------|--------|--------------------------------|-------------------|------------------------------------------|
| decimal | height | Syötä pituutesi metreissä      | .>0 and .<=3      | Pituuden on oltava 0 ja 3 metrin välillä |

## Esimerkkikäyttö

Esimerkki terveyskyselyssä:

| type    | name           | label                                        | constraint          | constraint_message                          |
|---------|----------------|----------------------------------------------|---------------------|---------------------------------------------|
| decimal | weight         | Syötä painosi kilogrammoina                  | .>0 and .<=500      | Painon on oltava 0 ja 500 kg:n välillä      |
| decimal | height         | Syötä pituutesi metreissä                    | .>0 and .<=3        | Pituuden on oltava 0 ja 3 metrin välillä    |
| decimal | body_temp      | Syötä kehon lämpötila Celsius-asteissa       | .>=35 and .<=42     | Lämpötilan on oltava 35 °C ja 42 °C välillä |
| calculate | bmi          |                                              |                     |                                             |

BMI-laskentarivillä voidaan käyttää:

```
calculation | ${weight} / (${height} * ${height})
```

Tämä laskee BMI:n syötetyn painon ja pituuden avulla.

## rtSurveyn laajennukset

Vaikka XLSForm-standardin decimal-kysymysten perusmäärittely on suoraviivainen, rtSurvey voi tarjota lisäominaisuuksia tai mukautuksia:

1. Tarkkuuden hallinta (desimaalien lukumäärä)
2. Mukautetut syötemuodot (esim. prosentti, valuutta)
3. Edistyneet validointisäännöt

## Rajoitukset

- Desimaalilukujen tarkkuus voi olla rajoitettu taustajärjestelmän tai tietokannan toimesta.
- Käyttäjät saattavat tarvita ohjausta odotetusta desimaalierottimesta (piste tai pilkku) riippuen heidän alueasetuistaan.
- Suuret desimaaliluvut voivat olla vaikeita lukea tai syöttää tarkasti mobiililaitteilla.
