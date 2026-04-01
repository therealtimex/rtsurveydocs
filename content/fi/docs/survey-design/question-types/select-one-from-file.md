---
title: "Select from file"
description: "select_one_from_file ja select_multiple_from_file lataavat valinnat dynaamisesti ulkoisesta CSV- tai XML-tiedostosta, joka on liitetty lomakkeeseen."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` ja `select_multiple_from_file` toimivat kuten `select_one` ja `select_multiple`, mutta valintojen määrittelemisen sijaan **choices-laskentataulukossa**, valinnat ladataan **ulkoisesta CSV- tai XML-tiedostosta**, joka on liitetty lomakkeeseen. Tästä on hyötyä, kun valintaluettelosi on erittäin pitkä, muuttuu usein tai sen on päivityttävä ilman koko lomakkeen uudelleenrakentamista.

## XLSForm-perusmäärittely

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Valitse terveyskeskus |
| select_multiple_from_file crops.csv | crops | Mitä viljelyskasveja kotitalous kasvattaa? |

Tyyppinimen jälkeisen tiedostonimen on vastattava lomakkeen lataamisessa liitettävän tiedoston nimeä.

## CSV-tiedostomuoto

CSV-tiedostossasi on oltava vähintään kaksi saraketta: `name` (tallennettu arvo) ja `label` (näytettävä teksti). Voit lisätä minkä tahansa määrän lisäsarakkeita suodatusta varten.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Valintojen suodattaminen

Käytä `choice_filter`-saraketta näyttämään vain ne valinnat, jotka vastaavat nykyistä asiayhteyttä. Viittaa CSV-sarakkeisiin suoraan niiden sarakkeen nimellä (ei `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Valitse piiri | |
| select_one_from_file health_facilities.csv | facility | Valitse terveyskeskus | district = ${district} |

Tässä esimerkissä näytetään vain valitun piirin terveyskeskukset. `district` `choice_filter`-sarakkeessa viittaa `district`-sarakkeeseen CSV-tiedostossa; `${district}` viittaa lomakekentän nimeltä `district` arvoon.

## Käyttötarkoitukset

Select-from-file-kysymyksiä käytetään yleisesti:

1. **Pitkiin valintaluetteloihin** — terveyskeskukset, koulut, kylät, lajilistat (satoja tai tuhansia kohteita)
2. **Usein päivitettäviin listoihin** — kun pääluettelo muuttuu tutkimuskierrosten välillä, päivitä vain CSV ilman lomakkeen uudelleenrakentamista
3. **Jaettuihin viitetietoihin** — yksi CSV-tiedosto useiden lomakkeiden käytössä
4. **Suodatettuihin kaskaadivalintoihin** — lataa kaikki alueet/piirikunnat/kylät yhdessä tiedostossa, suodata sitten ylätason valinnan mukaan

## Tiedoston liittäminen

Kun lataat lomakkeesi rtSurveyhin, liitä CSV-tiedosto **medialiitteenä**. Lomakemäärittelyssä olevan tiedostonimen on täsmällisesti vastattava liitteen tiedostonimeä.

{{% alert icon=" " context="warning" %}}
Tiedostonimet ovat kirjainkokoherkkiä. `Health_Facilities.csv` ja `health_facilities.csv` tulkitaan eri tiedostoiksi.
{{% /alert %}}

## `choice-label()`-funktion käyttö from-file-tyypin kanssa

Näyttääksesi valitun valinnan otsikon note- tai calculate-kentässä:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Valitse terveyskeskus | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Valittu terveyskeskus: ${facility_label} | |

## Parhaat käytännöt

1. Pidä CSV-tiedostot alle 5 000 rivin hyvän suorituskyvyn takaamiseksi mobiililaitteilla.
2. Sisällytä aina `name`- ja `label`-sarake — lisäsarakkeet ovat valinnaisia.
3. Kaskaadivalinnoille käytä yhtä CSV-tiedostoa ylätason sarakkeella ja suodata `choice_filter`:llä.
4. Versioi CSV-tiedostonimet (esim. `facilities_v3.csv`) tehdessäsi merkittäviä muutoksia sarakerakenteeseen.
5. Testaa suodatuslausekkeet huolellisesti — kirjoitusvirhe `choice_filter`-sarakkeessa näyttää hiljaisesti ei mitään valintoja.

## Rajoitukset

- Erittäin suuret CSV-tiedostot (10 000+ riviä) voivat hidastaa lomakkeen lataamista, erityisesti heikotehoisilla laitteilla.
- CSV-tiedostot on ladattava yhdessä lomakkeen kanssa — niitä ei voi hakea URL:lta ajonaikana (käytä `search()`:a tai `pulldata()`:a dynaamisiin hakuihin).
- `select_multiple_from_file`-tyyppiä tuetaan harvemmin eri asiakkaissa — tarkista yhteensopivuus ennen käyttöä.

## Vertailu `search()`:n kanssa

| | `select_one_from_file` | `search()`-ulkoasu |
|--|----------------------|----------------------|
| Valintojen lähde | Liitetty CSV/XML-tiedosto | Palvelinpuolen tietokantakysely |
| Toimii offline | Kyllä (tiedosto on mukana) | Vaatii yhteyden |
| Valintojen määrä | Rajoitettu laitteen muistilla | Rajoittamaton (sivutettu) |
| Reaaliaikaiset tiedot | Ei | Kyllä |

Suurille, usein muuttuville tai palvelinpuolen tietojoukoille, katso [Dynaaminen haku](../advanced-extension/dynamic-search).
