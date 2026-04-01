---
title: "Toistuvat kysymykset"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Toistot ovat rtSurveyn tehokas ominaisuus, jonka avulla voit kerätä samoja tietoja useita kertoja yhden kyselyn sisällä. Tämä on erityisen hyödyllistä esimerkiksi kotitalouskyselyissä, joissa saatat tarvita tietoja useista kotitalouden jäsenistä.

## Perus toisto-rakenne

Toiston luomiseksi rtSurveyssa käytä `begin repeat`- ja `end repeat`-rakennetta:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Lapsen nimi          |
| decimal      | birthweight  | Lapsen syntymäpaino  |
| select_one male_female | sex | Lapsen sukupuoli   |
| end repeat   |              |                      |
```

Tässä esimerkissä käyttäjä voi kerätä tietoja useista lapsista lisäämällä uusia toistoja lomakkeeseen.

## Toistojen nimeäminen

Vaikka `label`-sarake on valinnainen `begin repeat`:lle, otsikon lisääminen voi parantaa navigointia:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Lapsen tiedot        |
| text         | name         | Lapsen nimi          |
| decimal      | birthweight  | Lapsen syntymäpaino  |
| select_one male_female | sex | Lapsen sukupuoli   |
| end repeat   |              |                      |
```

rtSurvey näyttää "Lapsen tiedot" otsikkona kullekin toistotapaukselle.

## Kiinteät toistomäärät

Kiinteän toistojen lukumäärän määrittämiseksi käytä `repeat_count`-saraketta:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Lapsen tiedot        | 3            |
| text         | name         | Lapsen nimi          |              |
| decimal      | birthweight  | Lapsen syntymäpaino  |              |
| end repeat   |              |                      |              |
```

Tämä luo täsmälleen 3 lapsitoistoa.

## Dynaamiset toistomäärät

rtSurvey tukee dynaamisia toistomääriä aiempien vastausten perusteella:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Kotitalouden jäsenten lukumäärä?|                   |
| begin repeat | hh_member  | Kotitalouden jäsen             | ${num_hh_members}  |
| text     | name           | Nimi                           |                    |
| integer  | age            | Ikä                            |                    |
| end repeat |              |                                |                    |
```

## Ehdolliset toistot

Voit käyttää `relevant`-saraketta toistojen ehdolliseen näyttämiseen:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Asuuko täällä lapsia?     |                     |
| begin repeat      | child_repeat| Lapsen tiedot             | ${has_child} = 'yes'|
| text              | name        | Lapsen nimi               |                     |
| decimal           | birthweight | Lapsen syntymäpaino       |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-kohtaiset ominaisuudet

### Toiston yhteenveto

rtSurvey tarjoaa yhteenvetonäkymän toistoista. Yhteenvedon mukauttamiseksi käytä ryhmää toiston sisällä:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Etunimi                                  |
| text         | last_name    | Sukunimi                                 |
| integer      | age          | Ikä                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Toiston ulkoasuvaihtoehdot

rtSurvey tarjoaa lisäulkoasuvaihtoehtoja toistoille:

- `appearance: field-list` - Näyttää kaikki toiston kysymykset yhdellä näytöllä
- `appearance: table-list` - Esittää toistot taulukkomuodossa

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Lapsen tiedot     | table-list  |
| text         | name         | Nimi              |             |
| integer      | age          | Ikä               |             |
| end repeat   |              |                   |             |
```

### Sisäkkäiset toistot

rtSurvey tukee sisäkkäisiä toistoja monimutkaisille tietorakenteille:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Kotitalous           |
| text         | hh_name        | Kotitalouden nimi    |
| begin repeat | hh_member      | Kotitalouden jäsen   |
| text         | member_name    | Jäsenen nimi         |
| integer      | member_age     | Jäsenen ikä          |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Parhaat käytännöt toistojen käytössä rtSurveyssa

1. Käytä merkityksellisiä nimiä ja otsikoita toistoille data-analyysin parantamiseksi.
2. Harkitse dynaamisten toistomäärien käyttöä tiedonkirjausvirheiden vähentämiseksi.
3. Testaa lomakkeesi perusteellisesti, erityisesti käyttäessäsi monimutkaisia sisäkkäisiä toistoja.
4. Käytä yhteenvetoominaisuutta auttaaksesi luetteloijia navigoimaan pitkissä toistoluetteloissa.
5. Ole varovainen suurten toistomäärien kanssa, sillä ne voivat vaikuttaa lomakkeen suorituskykyyn.

## Nollatoistojen käsittely

Nollatoistojen esittämiseksi rtSurveyssa:

1. Kouluta luetteloijat poistamaan ensimmäinen toisto, jos sitä ei tarvita.
2. Käytä dynaamisia toistomääriä, kun tarkka lukumäärä tiedetään.
3. Käytä `relevant`-ominaisuutta toistojen ehdolliseen näyttämiseen.

## Tietojen vientiin liittyvät huomiot

Tietoja rtSurveysta vietäessä toistotieto litistetään tyypillisesti. Jokainen toistotapaus muuttuu erilliseksi riviksi viedyissä tiedoissa, päälomakkeen tiedot toistettuna jokaiselle tapaukselle.

## Mobiilisovelluksen huomioiminen

- rtSurveyn mobiilisovelluksen toistot tukevat offline-tiedonkeruuta.
- Suuret toistomäärät saattavat vaikuttaa sovelluksen suorituskykyyn alempitasoisilla laitteilla.

Käyttämällä toistoja tehokkaasti rtSurveyssa voit luoda joustavia ja tehokkaita kyselyitä, jotka pystyvät tallentamaan monimutkaisia, hierarkkisia tietorakenteita säilyttäen samalla käyttäjäystävällisen liittymän luetteloijille.
