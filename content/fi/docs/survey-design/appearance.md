---
title: "Ulkoasu"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

`appearance`-sarake rtSurveyssa mahdollistaa kysymysten visuaalisen esittämistavan ja toiminnan mukauttamisen kyselyissäsi. Tämä ominaisuus parantaa käyttökokemusta ja voi merkittävästi tehostaa tiedonkeruuta. rtSurvey tukee XLSFormin vakioulkoasuattribuutteja ja laajentaa niitä lisäasetuksilla.

## Vakio XLSForm-ulkoasuattribuutit

rtSurvey tukee seuraavia vakio XLSForm-ulkoasuattribuutteja:

| Ulkoasuattribuutti | Kysymystyypit | Kuvaus |
|-------------------|---------------|--------|
| multiline | text | Luo monirivisentekstiruudun (parhaiten webissä) |
| minimal | select_one, select_multiple | Näyttää valinnat pudotusvalikossa |
| quick | select_one | Siirtyy automaattisesti seuraavaan kysymykseen valinnan jälkeen (vain mobiili) |
| no-calendar | date | Estää kalenterin näyttämisen (vain mobiili) |
| month-year | date | Mahdollistaa kuukauden ja vuoden valinnan |
| year | date | Mahdollistaa vain vuoden valinnan |
| horizontal-compact | select_one, select_multiple | Näyttää valinnat vaakasuoraan (vain web) |
| horizontal | select_one, select_multiple | Näyttää valinnat vaakasuoraan sarakkeissa (vain web) |
| likert | select_one | Esittää valinnat Likert-asteikkona |
| compact | select_one, select_multiple | Näyttää valinnat vierekkäin minimaalisella täytteellä |
| quickcompact | select_one | Yhdistää tiiviin näytön ja automaattisen etenemisen (vain mobiili) |
| field-list | groups | Näyttää koko ryhmän yhdellä näytöllä (vain mobiili) |
| label | select_one, select_multiple | Näyttää valintojen otsikot ilman syöttöelementtejä |
| list-nolabel | select_one, select_multiple | Näyttää syöttöelementit ilman otsikoita (käytä `label`:n kanssa) |
| table-list | groups | Näyttää kysymykset taulukkona |
| signature | image | Mahdollistaa allekirjoituksen tallentamisen (vain mobiili) |
| draw | image | Mahdollistaa vapaamuotoisen piirroksen (vain mobiili) |
| map, quick map | select_one, select_one_from_file | Mahdollistaa valinnan kartalta |

## Ulkoasun käytön parhaat käytännöt

1. **Johdonmukaisuus**: Käytä ulkoasuattribuutteja johdonmukaisesti koko kyselyssä yhtenäisen ulkoasun saavuttamiseksi.
2. **Mobiili vs. web**: Harkitse miten ulkoasut renderöityvät eri laitteilla ja alustoilla.
3. **Suorituskyky**: Ole varovainen ulkoasuattribuuttien kanssa, jotka saattavat hidastaa lomakkeen latautumista (esim. `table-list` suurille ryhmille).
4. **Käyttökokemus**: Valitse ulkoasut, jotka tekevät tietojensyötöstä helpompaa ja intuitiivisempaa vastaajille.
5. **Testaus**: Testaa aina lomakkeesi kohdejaitteilla varmistaaksesi ulkoasujen toimivuuden.

## Edistyneet tekniikat

### Ulkoasujen yhdistäminen

Joitain ulkoasuattribuutteja voidaan yhdistää monimutkaisempien asettelujen saavuttamiseksi:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Valitse yksi: | minimal compact |
```

### Dynaamiset ulkoasut

rtSurvey mahdollistaa dynaamiset ulkoasumuutokset lomakelogiikan perusteella:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Anna aika: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobiilisovelluksen huomioiminen

- Jotkut ulkoasut (esim. `quick`, `signature`) ovat mobiililaitekohtaisia.
- Testaa perusteellisesti sekä Androidilla että iOS:llä yhdenmukaisen toiminnan varmistamiseksi.

## rtSurvey-laajennetut ulkoasuattribuutit

Vakio XLSForm-ulkoasujen lisäksi rtSurvey tukee seuraavia alustakompatiisia asetuksia:

### Tietojen hallinta ja näyttö

| Ulkoasuattribuutti | Kysymystyypit | Kuvaus |
|-------------------|---------------|--------|
| `invisible` | mikä tahansa | Piilottaa kentän näkyvistä keräten tai laskien silti sen arvon. Eroaa `hidden`-tyypistä — kenttä osallistuu silti logiikkaan. |
| `displaytitle` | mikä tahansa | Pakottaa kentän otsikon/nimen näyttämisen, vaikka se muuten olisi piilotettu. |
| `autopull` | select_one, select_multiple | Hakee automaattisesti ulkoisen datan täyttääkseen valinnat lomakkeen latautuessa tai triggerikentän muuttuessa. |
| `floating_hint` | text, integer, decimal | Näyttää vihjeen tekstin kelluvana tunnisteena syöttökentän yläpuolella sen sijaan, että se olisi alla. |
| `calculate-button` | calculate | Lisää näkyvän painikkeen, joka käynnistää kentän uudelleenlaskennan pyydettäessä automaattisen laskennan sijaan. |

### Asettelu

| Ulkoasuattribuutti | Kysymystyypit | Kuvaus |
|-------------------|---------------|--------|
| `1screen` | group | Pakottaa koko ryhmän näkymään yhdellä näytöllä ryhmän koosta riippumatta. |
| `columns(n)` | select_one, select_multiple | Näyttää valinnat `n` sarakkeessa. Esimerkki: `columns(3)` näyttää kolme saraketta valintapainikkeita. |
| `gridformat<row=R col=C colspan=S align=center>` | mikä tahansa | Sijoittaa kentän CSS-ruudukkoon riville `R`, sarakkeeseen `C`, ulottuen `S` saraketta. Käytetään `advanced-extension/grid-layout`:n kanssa. |
| `ignore-simplify` | mikä tahansa | Ohjaa lomakkeen renderöijää ohittamaan automaattinen yksinkertaistaminen tai tämän kentän asettelun tiivistäminen. |

### Widgetit

| Ulkoasuattribuutti | Kysymystyypit | Kuvaus |
|-------------------|---------------|--------|
| `likert` | select_one | Esittää valinnat Likert-asteikkoriveinä. |
| `distress` | select_one | Renderöi valinnat Kessler Psychological Distress Scale (K10) -visuaalisena widgettinä tunneikoneineen. |

### API-integraatio

| Ulkoasuattribuutti | Kysymystyypit | Kuvaus |
|-------------------|---------------|--------|
| `callapi` | text, integer, decimal, select_one | Mahdollistaa API-kutsuintegraation tälle kentälle. Calculation-sarakkeen tulee sisältää `callapi()`-lauseke. Katso [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Käynnistää API-varmistuskutsun staattisilla parametreilla. Lomake estää etenemisen, kunnes API vahvistaa arvon. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Sama kuin `callapi-verify`, mutta parametrit johdetaan muiden kenttien arvoista suorituksen aikana. |

### Sisäinen päivämäärä/aika-muoto

`date`-, `time`- ja `datetime`-kentille voit määrittää mukautetun näyttömuodon lisäämällä muotoilujonon ulkoasuun:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Muotoilutunnukset ovat samat kuin `format-date()` ja `format-date-time()`. Katso [Funktiot — Päivämäärä- ja aikafunktiot](operators-and-functions/functions#date-and-time-functions).

Esimerkki:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Tapahtuman päivämäärä ja aika | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Syntymäpäivä | inline-[%d/%m/%Y] |

## Tunnetut rajoitukset

- Monimutkaiset ulkoasut eivät välttämättä renderöidy identtisesti kaikilla alustoilla.
- Jotkut edistyneet rtSurvey-ulkoasut eivät välttämättä tue offline-tilaa.

## Ulkoasuongelmien vianmääritys

1. **Ulkoasua ei sovelleta**: Tarkista ulkoasu-sarakkeessa olevat kirjoitusvirheet.
2. **Epäjohdonmukainen renderöinti**: Tarkista yhteensopivuus kysymystyypin ja alustan kanssa.
3. **Suorituskykyongelmat**: Harkitse monimutkaisten ulkoasujen yksinkertaistamista erityisesti suurille kyselyille.
