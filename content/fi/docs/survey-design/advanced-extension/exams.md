---
title: "Kokeet"
description: "Koetoiminto lisää kyselyyn ajastetun visailutilan, valinnaisella äänipalautteella oikeisiin ja vääriin vastauksiin."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

**Koe**-ominaisuus muuttaa kyselyn ajastetuksi visailuksi. Vastaajalle näytetään lähtölaskentatajastin ja kysely kirjaa kuinka paljon aikaa on jäljellä heidän lopettaessaan. Valinnaisesti oikeiden ja väärien vastausten yhteydessä voidaan toistaa ääniä.

Tämä on hyödyllinen tietotason arvioinneissa, lukutaitotesteissä, kenttähenkilöstön pätevyyden tarkistuksissa ja kaikissa kyselyissä, joissa tehtävänaika on mielekäs data.

---

## `check-exam()`-funktio

Konfiguroi koe käyttämällä `check-exam()`:tä lomakkeen alkuun sijoitetun `calculate`-kentän **`calculation`**-sarakkeessa:

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Parametrit

| # | Parametri | Kuvaus |
|---|-----------|--------|
| 1 | `examTime` | Kokeen kokonaiskesto sekunteina |
| 2 | `questionToStoreRemainingTime` | `calculate`- tai `integer`-kentän `name`, johon tallennetaan jäljellä oleva aika kokeen päättyessä |
| 3 | `rightSound` | *(Valinnainen)* Oikean vastauksen yhteydessä toistettavan äänitiedoston tiedostonimi (liitä lomakkeeseen mediatiedostona) |
| 4 | `wrongSound` | *(Valinnainen)* Väärän vastauksen yhteydessä toistettavan äänitiedoston tiedostonimi |
| 5 | `excludeQuestion` | *(Valinnainen)* Pilkuilla eroteltu lista kenttänimistä, jotka jätetään pois koetajastimesta (esim. `'intro_note,consent'`) |

---

## Perusasetus

### Vaihe 1: Lisää koekenttä

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` käynnistää 600 sekunnin (10 minuutin) ajastimen. `remaining_time` täytetään automaattisesti, kun vastaaja lopettaa.

### Vaihe 2: Lisää kysymyksesi

Koetajastin kattaa kaikki lomakkeen kysymykset paitsi `excludeQuestion`:ssa luetellut.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | Kenian pääkaupunki on Nairobi. Totta vai tarua? |
| select_one choices | q2 | Mikä elin pumppaa verta kehossa? |
| select_one choices | q3 | Vesi kiehuu 100°C:ssa merenpinnan tasolla. Totta vai tarua? |

### Vaihe 3: Tallenna jäljellä oleva aika

Parametri 2:ssa nimetty kenttä (`remaining_time`) asetetaan automaattisesti jäljellä olevien sekuntien määrään, kun vastaaja lähettää. Arvo `0` tarkoittaa, että aika loppui; korkea arvo tarkoittaa, että he suorittivat nopeasti.

---

## Äänipalautteen kanssa

Liitä äänitiedostot lomakkeeseen (medialitteinä) ja viittaa niihin:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` toistetaan, kun vastaaja valitsee oikean vastauksen
- `wrong.mp3` toistetaan, kun vastaaja valitsee väärän vastauksen

{{% alert icon=" " context="warning" %}}
Äänitiedostot on liitettävä lomakkeeseen mediatiedostoina ja tiedostonimen on vastattava täsmälleen (kirjainkooherkkä), mukaan lukien tarkenne.
{{% /alert %}}

---

## Kysymysten jättäminen pois ajastimesta

Välitä pilkuilla eroteltu lista kenttänimistä, jotka jätetään pois kokeesta (esim. johdantoviimaajat tai suostumusoikysymykset):

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Jätä `rightSound` ja `wrongSound` tyhjiksi merkkijonoiksi `''`, jos et tarvitse ääntä mutta tarvitset poissulkuja.

---

## Täydellinen esimerkki

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Tervetuloa terveystietojen arviointiin. Sinulla on 5 minuuttia aikaa vastata kaikkiin kysymyksiin. | |
| trigger | start_ack | Napauta OK, kun olet valmis aloittamaan. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | Käsien pesu estää sairauksien leviämistä. | |
| select_one yesno | q2 | Sinun tulisi juoda vähintään 2 litraa vettä päivässä. | |
| select_one yesno | q3 | Malaria on viruksen aiheuttama. | |

---

## Parhaat käytännöt

1. Ilmoita aina vastaajille aikarajasta ennen aloittamista — käytä `note`- tai `trigger`-elementtiä ennen `check-exam()`-kenttää.
2. Jätä johdantoviimaajat ja suostumusoikysymykset pois ajastimesta käyttämällä `excludeQuestion`-parametria.
3. Käytä `remaining_time`:tä jälkilaskennassa aikakatkaisujen havaitsemiseen: `if(${remaining_time} = 0, 'Aikakatkaisu', 'Suoritettu')`.
4. Pidä kysymysten määrä suhteessa sallittuun aikaan — 2–3 minuuttia per kysymys on kohtuullinen lähtöarvo useimmille tietotason arvioinneille.
5. Testaa äänitiedostoilla varsinaisella laitteella ennen käyttöönottoa — äänentoisto vaihtelee eri Android-versioissa ja selaimissa.

## Rajoitukset

- Ajastin on vain näyttö — lomake ei lähetä automaattisesti ajan loppuessa; vastaajan on silti lähetettävä manuaalisesti.
- Äänipalautteen toimintaan vaaditaan, että laitteen äänenvoimakkuus on päällä eikä mykistetty.
- Koetoiminto on rtSurvey-laajennus eikä se ole osa vakio XLSForm-spesifikaatiota.
