---
title: "Image"
description: "Image-kysymykset antavat vastaajille mahdollisuuden ottaa ja lähettää valokuvia osana kyselyä."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

XLSFormien ja rtSurveyn image-kysymystyyppi mahdollistaa vastaajien ottaa ja lähettää valokuvia osana kyselyvastaustaan. Tämä ominaisuus on erityisen hyödyllinen visuaalisen tiedon keräämiseen, havaintojen dokumentointiin tai todisteiden toimittamiseen kenttätutkimuksissa.

## XLSForm-perusmäärittely

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Ota kuva sijainnista            |

Lisätietoja image-kysymystyypin perusteista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Image-kysymyksiä käytetään yleisesti:

1. Kenttäolosuhteiden tai havaintojen dokumentointiin
2. Visuaalisten todisteiden tallentamiseen tutkimuksissa
3. Ennen/jälkeen-valokuvien keräämiseen vaikutusten arvioinneissa
4. Tehtävien suorittamisen tai sijainneissa oleskelun todentamiseen
5. Visuaalisten tietojen keräämiseen etäanalyysiä varten

## Parhaat käytännöt

1. Anna selkeät ohjeet siitä, mitä tulee valokuvata.
2. Harkitse yksityisyysasioita ja informoi vastaajia siitä, miten heidän valokuviaan käytetään.
3. Kiinnitä huomiota tiedostokokoihin ja tallennusrajoituksiin, erityisesti kyselyissä alueilla, joilla on rajoitettu Internet-yhteys.
4. Varmista, että laitteella on riittävästi tallennustilaa ja kameran luvat on myönnetty.

## Esimerkkikäyttö

Esimerkki kyselyssä:

| type  | name           | label                                       | hint                                             |
|-------|----------------|---------------------------------------------|--------------------------------------------------|
| image | storefront     | Ota kuva kaupan sisäänkäynnistä             | Varmista, että kaupan nimi on selvästi näkyvissä  |

## rtSurveyn laajennukset

Vaikka XLSForm-standardin image-kysymysten perusmäärittely on suoraviivainen, rtSurvey voi tarjota lisäominaisuuksia tai mukautuksia:

1. Kuvan laadun asetukset (esim. matala, keskitaso, korkea resoluutio)
2. Mahdollisuus lisätä kuvatekstejä tai tunnisteita kuviin
3. Useiden kuvien ottaminen yhdelle kysymykselle
4. Integraatio laitteen natiivin kamerasovelluksen tai gallerian kanssa

## Tietojen käsittely

Tämän kysymystyypin kautta kerätyt kuvat:

1. Tallennetaan yleiseen kuvamuotoon (esim. JPG, PNG)
2. Tallennetaan muiden kyselytietojen ohessa, usein erillisessä mediahakemistossa
3. Ovat tarkasteltavissa ja analysoitavissa kyselynhallintajärjestelmän kautta

## Analyysin näkökohtia

Image-kysymyksiä käytettäessä harkitse:

1. Miten kuvat analysoidaan (esim. manuaalinen tarkistus, automaattinen kuva-analyysi)
2. Kuvatiedostoihin tarvittava lisätallennustila
3. Yksityisyys ja tietosuojatoimenpiteet valokuvien tallentamiseen ja käsittelyyn
4. Mahdollinen tarve kuvanmuokkaus- tai järjestelytyökaluille analyysivaiheessa

## rtSurveyn ulkoasulaajennukset

rtSurvey laajentaa `image`-tyyppiä kahdella lisäulkoasuvaihtoehdolla:

| Ulkoasu | Kuvaus |
|---------|--------|
| `watermark("lauseke")` | Lisää tekstivesileiman otettuihin kuviin. Argumentti on XPath-lauseke, joka arvioidaan kuvaushetkellä. Esimerkki: `watermark("${id} ${today()}")` |
| `editable` | Mahdollistaa otetun valokuvan merkitsemisen/piirtämisen ennen tallentamista |

### Esimerkki: Vesileima vastaajan tunnuksella ja päivämäärällä

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Ota kuva sijainnista | `watermark("${respondent_id} ${today()}")` |

## Rajoitukset

- Kuvatiedostot voivat olla suuria, mikä voi vaikuttaa tiedonsiirtoon ja tallennukseen.
- Kaikilla laitteilla ei välttämättä ole korkealaatuisia kameroita tai riittävästi tallennustilaa.
- Suurten kuvamäärien analysoiminen voi olla aikaa vievää.
- Kuvien ottamiseen julkisissa paikoissa voi liittyä yksityisyyshuolenaiheita.
