---
title: "Geoshape"
description: "Geoshape-kysymykset antavat vastaajille mahdollisuuden piirtää muotoja kartalle, tallentaen monimutkaisia maantieteellisiä tietoja osana kyselyä."
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

XLSFormien ja rtSurveyn geoshape-kysymystyyppi mahdollistaa vastaajien piirtää muotoja (monikulmioita) kartalle, tallentaen monimutkaisia maantieteellisiä tietoja. Tämä ominaisuus on erityisen hyödyllinen alueiden kartoittamiseen, rajojen määrittelemiseen tai kiinnostusalueiden merkitsemiseen paikalliskyselyissä.

## XLSForm-perusmäärittely

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Piirrä pellon raja              |

Lisätietoja geoshape-kysymystyypin perusteista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Geoshape-kysymyksiä käytetään yleisesti:

1. Peltorajojen kartoittamiseen maatalouskyselyissä
2. Ympäristövaikutusalueiden määrittelemiseen
3. Vyöhykkeiden merkitsemiseen kaupunkisuunnittelututkimuksissa
4. Alueiden hahmottamiseen geologisissa tutkimuksissa
5. Monimutkaisten maantieteellisten piirteiden tallentamiseen paikallisanalyysiä varten

## Parhaat käytännöt

1. Varmista, että laitteen sijaintipalvelut ovat käytössä ja luvat myönnetty.
2. Anna selkeät ohjeet muodon piirtämiseen ja mitkä alueet tulee sisällyttää.
3. Harkitse satelliittikuvien tai pohjakarttojen käyttöä vastaajien auttamiseksi piirtämään muodot tarkasti.
4. Kiinnitä huomiota muotojen mahdolliseen monimutkaisuuteen ja sen vaikutukseen tiedon kokoon ja käsittelyyn.

## Esimerkkikäyttö

Esimerkki kyselyssä:

| type     | name           | label                                           | hint                                              |
|----------|-----------------|-------------------------------------------------|---------------------------------------------------|
| geoshape | forest_area    | Hahmottele metsälaikun raja                     | Käytä vähintään 3 pistettä suljetun muodon luomiseen |

## rtSurveyn laajennukset

Vaikka XLSForm-standardin geoshape-kysymysten perusmäärittely on suoraviivainen, rtSurvey voi tarjota lisäominaisuuksia tai mukautuksia:

1. Integraatio offline-karttojen kanssa syrjäisillä alueilla
2. Vaihtoehdot muodon pisteiden vähimmäis- ja enimmäismäärän asettamiseen
3. Mahdollisuus muokata tai tarkentaa muotoja alkuperäisen piirtämisen jälkeen
4. Tuki eri muototyypeille (esim. suorakulmiot, ympyrät) vapaamuotoisten monikulmioiden lisäksi

## Tietomuoto

Geoshape-tiedot tallennetaan tyypillisesti välilyönnillä erotettuina koordinaattiparien merkkijonona, suljettuina sulkeisiin:

```
(lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN)
```

Esimerkiksi:
```
(38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404; 38.253094215699576 21.756382658677467)
```

## Analyysin näkökohtia

Geoshape-kysymyksiä käytettäessä harkitse:

1. Miten maantieteelliset tiedot visualisoidaan ja analysoidaan (esim. GIS-ohjelmisto)
2. Mahdollinen tarve tietojen puhdistamiseen tai monimutkaisten muotojen yksinkertaistamiseen
3. Yksityisyys ja tietosuojatoimenpiteet yksityiskohtaisten paikkatietojen käsittelyyn
4. Integraatio muiden paikkatietolähteiden kanssa kattavaa analyysia varten

## Rajoitukset

- Tarkkoja muotoja voi olla vaikea piirtää pienillä mobiiliruuduilla.
- Monimutkaiset muodot voivat vaatia merkittävästi tallennustilaa ja käsittelykapasiteettia.
- Geoshape-kysymykset eivät sovi kaikentyyppisiin kyselyihin tai vastaajille.
- Yksityiskohtaisten paikkatietojen keräämiseen liittyy yksityisyyshuolenaiheita.
