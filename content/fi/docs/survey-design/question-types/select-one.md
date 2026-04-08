---
title: "Select_one"
description: "Select_one-kysymykset antavat vastaajille mahdollisuuden valita täsmälleen yhden vaihtoehdon ennalta määritetystä luettelosta."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

`select_one`-kysymystyyppi pyytää vastaajaa valitsemaan **täsmälleen yhden vaihtoehdon** ennalta määritetystä luettelosta. Oletuksena valinnat näytetään radiopainikkeina, mutta laajan ulkoasuvaihtoehtojen valikoiman avulla asettelua ja toimintaa voidaan muuttaa.

## XLSForm-perusmäärittely

**survey-laskentataulukko:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Antiko vastaaja suostumuksen? |

**choices-laskentataulukko:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Kyllä |
| yesno | no | Ei |

`select_one listname` -kohdan `listname` täytyy vastata choices-laskentataulukon `list_name`-saraketta.

Lisätietoja löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Select_one-kysymyksiä käytetään:

1. Kyllä/Ei-kysymyksiin
2. Yhden vastauksen monivalintakysymyksiin (esim. koulutustaso, sukupuoli, siviilisääty)
3. Kategorisiin arviointeihin (esim. heikko / kohtalainen / hyvä / erinomainen)
4. Kaskaadisiin (linkitettyihin) valintoihin, joissa valinnat suodatetaan edellisen vastauksen perusteella
5. Maan, alueen, piirikunnan tai muun hallinnollisen yksikön valintaan

## Ulkoasuvaihtoehdot

Määritä arvo `appearance`-sarakkeessa muuttaaksesi, miten valinnat näytetään:

{{< table >}}
| Ulkoasu | Kuvaus |
|---------|--------|
| *(ei mitään)* | Oletusradiopainikkeet, yksi per rivi |
| `minimal` | Yksi pudotusvalikko/spinner radiopainikkeiden sijaan |
| `quick` | Siirtyy automaattisesti seuraavaan kysymykseen heti valinnan jälkeen (vain mobiili) |
| `compact` | Kompakti valintojen ruudukko — sarakkeiden määrä mukautuu näytön leveyteen |
| `compact-N` | Kompakti ruudukko pakotettuna N sarakkeeseen (esim. `compact-3`) |
| `quickcompact` | Yhdistää `quick`- ja `compact`-ominaisuudet |
| `quickcompact-N` | Yhdistää `quick`- ja `compact`-ominaisuudet N pakotetuilla sarakkeilla |
| `horizontal` | Valinnat järjestetty vaakasuoraan riviin (verkko) |
| `horizontal-compact` | Vaakasuora, kompakti välistys (verkko) |
| `likert` | Likert-asteikkorivi — otsikot ylhäällä, radiopainikkeet alla |
| `label` | Näyttää vain valintojen otsikot ilman syötteitä (käytä parissa `list-nolabel` kanssa) |
| `list-nolabel` | Näyttää vain syötteet ilman otsikoita (käytä parissa `label` kanssa) |
| `columns(N)` | Näyttää N sarakkeessa (rtSurvey-laajennus, esim. `columns(3)`) |
| `distress` | Kessler Psychological Distress (K10) emotionaalinen ikoniwidget |
| `search-api(...)` | Dynaaminen haku — lataa valinnat API:lta ajonaikana |
| `tagging` | Näyttää valinnat klikattavina tagi-chipeinä radiopainikkeiden sijaan |
| `boxtag` | Näyttää valinnat tyylikäs suorakulmainen bokseina, joita käyttäjä napauttaa valitakseen |
| `boxtag -search` | Boxtag-asettelu haku-/suodatussyötteellä boksien yläpuolella |
| `duolingo-style1` | Duolingo-inspiroitu korttiasettelu — suuret napautettavat kortit ikoneilla |
| `rating_box` | Ruudukkopohjainen arviointiboxi — parhaiten numeerisille tai asteikkovaihtoehdoille |
| `star_rating` | Tähtiarviointiwidget — valinnat näytetään 1–N tähtinä |
| `choices-noshow` | Näyttää aluksi vain ensimmäiset 10 vaihtoehtoa; paljastaa loput tarvittaessa |
| `noshow` | Piilottaa valikaluettelon kokonaan; arvo asetetaan ohjelmallisesti |
| `checkall` | Lisää "Valitse kaikki" -vaihtoehdon luettelon alkuun |
| `max-items(N)` | Rajoittaa näkyvien valintojen määrän N:ään |
{{< /table >}}

### Esimerkki: Likert-asteikko

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Kuinka tyytyväinen olet palveluun? | likert |

### Esimerkki: Kompakti 3 saraketta

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Valitse alue | compact-3 |

## Kaskaadivalinnat

Kaskaadi (linkitetty) valinta suodattaa valinnat edellisessä kysymyksessä valitun arvon perusteella. Käytä `choice_filter`-saraketta choices-laskentataulukon sarakkeen nimellä.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Valitse maakunta | |
| select_one district | district | Valitse piiri | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Kun vastaaja valitsee `nairobi`, vain `Westlands` ja `Kasarani` näkyvät piiriluettelossa.

{{% alert icon=" " context="warning" %}}
`choice_filter`-sarakkeessa käytetyn sarakkeen nimen (esim. `province_name`) on oltava choices-laskentataulukossa. `${province}` viittaa lomakekentän nimeltä `province` arvoon.
{{% /alert %}}

## Valitun arvon käyttäminen lausekkeissa

Viittaa valittuun **arvoon** (ei otsikkoon) `${fieldname}`-syntaksilla:

```
relevant: ${consent} = 'yes'
```

Saadaksesi valinnan otsikon arvon sijaan, käytä `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## "Muu"-vaihtoehto vapaalla tekstillä

Yleinen malli on sisällyttää "muu"-vaihtoehto, joka paljastaa tekstikentän:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Mikä on ammattisi? | |
| text | job_other | Täsmennä | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Maanviljelijä |
| occupation | trader | Kauppias |
| occupation | student | Opiskelija |
| occupation | other | Muu (täsmennä) |

## Parhaat käytännöt

1. Pidä luettelot lyhyinä ja toisiaan poissulkevina — jos vastaajat haluavat ehkä useamman kuin yhden, käytä `select_multiple`-tyyppiä.
2. Laita yleisin vastaus ensimmäiseksi tai järjestä aakkosjärjestykseen pitkissä luetteloissa.
3. Sisällytä aina "En tiedä"- tai "En halua vastata"-vaihtoehto tarvittaessa.
4. Käytä `minimal`-ulkoasua (pudotusvalikko) yli 7–8 valinnan luetteloihin mobiilissa näyttötilan säästämiseksi.
5. Kaskaadivalinnoissa lisää kaikki suodatussarakkeet choices-laskentataulukkoon ennen lomakkeen rakentamista.

## Rajoitukset

- Vastaaja voi valita vain yhden valinnan — käytä `select_multiple`-tyyppiä useamman vastauksen kysymyksiin.
- `likert`-ulkoasu toimii parhaiten 5–7 valinnan kanssa, jotka mahtuvat yhdelle riville.
- `quick`-automaattisiirtyminen toimii vain mobiilissa; sillä ei ole vaikutusta verkkolomakkeisiin.
