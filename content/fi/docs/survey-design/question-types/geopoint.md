---
title: "Geopoint"
description: "Geopoint-kysymykset tallentavat maantieteelliset koordinaatit (leveys, pituus, korkeus ja tarkkuus) osana kyselyä."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

XLSFormien ja rtSurveyn geopoint-kysymystyyppi mahdollistaa maantieteellisten koordinaattien keräämisen laitteen GPS:n tai muiden sijaintipalveluiden avulla. Tämä ominaisuus on erityisen hyödyllinen kyselyvastausten kartoittamiseen, kenttätoimintojen seuraamiseen tai tietojen yhdistämiseen tiettyihin sijainteihin.

## XLSForm-perusmäärittely

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Tallenna nykyinen sijainti      |

Lisätietoja geopoint-kysymystyypin perusteista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Geopoint-kysymyksiä käytetään yleisesti:

1. Kyselyvastausten maantieteelliseen kartoittamiseen
2. Kenttätoimintojen sijainnin varmistamiseen
3. Luetteloijien reitin seuraamiseen
4. Ympäristö- tai sosiaalitietojen yhdistämiseen tiettyihin sijainteihin
5. Etäisyyksien tai alueiden laskemiseen maantieteellisissä analyyseissä

## Parhaat käytännöt

1. Varmista, että laitteen sijaintipalvelut ovat käytössä ja luvat myönnetty.
2. Anna GPS:lle riittävästi aikaa tarkan sijainnin hankkimiseen.
3. Harkitse yksityisyysasioita ja informoi vastaajia sijaintitietojen keräämisestä.
4. Käytä muiden kysymystyyppien yhteydessä sijaintitietojen asiayhteyden tarjoamiseksi.

## Esimerkkikäyttö

Esimerkki kyselyssä:

| type     | name           | label                                          | hint                                             |
|----------|----------------|------------------------------------------------|--------------------------------------------------|
| geopoint | sample_location| Tallenna näytteenoton sijainti                 | Seiso avoimella alueella paremman GPS-signaalin saamiseksi |

## rtSurveyn laajennukset

Vaikka XLSForm-standardin geopoint-kysymysten perusmäärittely on suoraviivainen, rtSurvey voi tarjota lisäominaisuuksia tai mukautuksia:

1. Karttaintegraatio tallennetun sijainnin visuaaliseen vahvistamiseen
2. Tarkkuuskynnysasetukset
3. Mahdollisuus syöttää koordinaatit manuaalisesti
4. Integraatio offline-karttojen kanssa syrjäisillä alueilla

## Tietomuoto

Geopoint-tiedot tallennetaan tyypillisesti neljän välilyönnillä erotetun arvon merkkijonona:

```
leveysaste pituusaste korkeus tarkkuus
```

Esimerkiksi:
```
41.40338 2.17403 30.5 10
```

## Analyysin näkökohtia

Geopoint-kysymyksiä käytettäessä harkitse:

1. Miten maantieteelliset tiedot visualisoidaan (esim. karttaohjelmisto)
2. Kerättyjen koordinaattien tarkkuus ja sen vaikutus analyysiin
3. Sijaintitietojen yksityisyys ja tietosuojatoimenpiteet
4. Mahdollinen integraatio GIS-työkalujen kanssa

## Rajoitukset

- Tarkkuus voi vaihdella laitteen ja ympäristöolosuhteiden mukaan.
- GPS-signaalit voivat olla heikkoja tai puuttua sisätiloissa tai alueilla, joilla on esteitä.
- Sijaintitietojen kerääminen voi merkittävästi kuluttaa laitteen akkua.
- Tarkkoihin sijaintitietoihin liittyy yksityisyyshuolenaiheita.
