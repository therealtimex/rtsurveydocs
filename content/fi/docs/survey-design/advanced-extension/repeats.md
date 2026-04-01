---
title: "Edistyneet toistot"
description: "Edistyneet mallit toistoryhmille: dynaamiset määrät, sisäkkäiset toistot, toistodatan yhteenveto ja arvojen viittaaminen toistojen välillä."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Tällä sivulla käsitellään edistyneitä malleja toistoryhmien käyttöön rtSurveyssa. Toistoryhmien perusteista katso [Ryhmittely ja toistot](../repeats).

---

## Dynaaminen toistomäärä

Oletuksena luetteloija päättää kuinka monta kertaa toistaa. Voit kiinnittää toistojen lukumäärän käyttämällä `repeat_count`:tia:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Kotitalouden jäsen | `${num_members}` |
| text | member_name | Jäsenen nimi | |
| integer | member_age | Ikä | |
| end_repeat | | | |

Toisto suoritetaan täsmälleen `${num_members}` kertaa, jossa `num_members` kerättiin aiemmin lomakkeessa. Luetteloija ei voi lisätä tai poistaa tapauksia.

---

## Indeksoitu pääsy: `indexed-repeat()`

Pääse tietyn toistotapauksen kenttäarvoon **toistoryhmän ulkopuolelta** käyttämällä `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Tämä on hyödyllinen yhteenvetokenttien rakentamisessa tai "ensisijaisen" jäsenen tietojen viittaamisessa toiston jälkeen.

---

## Nykyinen tapausnumero: `index()`

Toistoryhmän sisällä `index()` palauttaa nykyisen tapauksen 1-pohjaisen sijainnin. Käytä sitä kunkin toiston nimeämiseen tai ainutlaatuisten tunnisteiden luomiseen:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Pelto |
| note | plot_label | Pelto numero ${index()} |
| text | plot_id | Pellon tunnus |
| end_repeat | | |

---

## Saman tapauksen kenttien viittaaminen

Toiston sisällä käytä `${fieldname}` viittaaksesi toiseen kenttään **samassa toistotapauksessa**. `indexed-repeat()`:ia ei tarvita saman silmukan sisällä:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Jäsen | |
| text | member_name | Nimi | |
| integer | member_age | Ikä | |
| text | school_name | Koulun nimi | `${member_age} < 18` |
| end_repeat | | | |

---

## Päivittävien kenttien viittaaminen toiston sisältä

Toistoryhmän ulkopuolella (yläpuolella) olevia kenttiä voidaan viitata normaalisti `${fieldname}`:lla:

| type | name | label |
|------|------|-------|
| text | village | Kylän nimi |
| begin_repeat | plots | Maatalousmaa |
| note | plot_context | Pellot kylässä ${village} |
| end_repeat | | |

---

## Toistodatan yhteenveto

Käytä toiston koostefunktioita **toistoryhmän ulkopuolella** yhteenvedon luomiseen:

| Funktio | Esimerkki | Kuvaus |
|---------|---------|--------|
| `count(group)` | `count(${household_members})` | Tapausten lukumäärä |
| `sum(field)` | `sum(${loan_amount})` | Numeerisen kentän summa |
| `min(field)` | `min(${member_age})` | Pienin arvo |
| `max(field)` | `max(${member_age})` | Suurin arvo |
| `join(sep, field)` | `join(', ', ${member_name})` | Pilkuilla eroteltu lista |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Ehdollinen lukumäärä |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Ehdollinen summa |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Ehdollinen liittäminen |

### Esimerkki: Kotitalousyhteenveto

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Kuinka monta jäsentä? | |
| begin_repeat | members | Jäsen | `${num_members}` |
| text | member_name | Nimi | |
| integer | member_age | Ikä | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} jäsentä; ${children_count} alle 18-vuotiasta. Aikuiset: ${adult_names} | |

---

## Sisäkkäiset toistot

Toistoryhmä voi sisältää toisen toistoryhmän. Käytä tätä harkiten — sisäkkäiset toistot lisäävät monimutkaisuutta ja voivat olla hämmentäviä luetteloijille.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Kotitalous |
| text | hh_id | Kotitaloustunnus |
| begin_repeat | hh_members | Jäsen |
| text | member_name | Jäsenen nimi |
| end_repeat | | |
| end_repeat | | |

Viitattaessa ulomman toiston kenttään sisemmästä toistosta, käytä `${fieldname}` — se ratkaisee lähimpään vastaavaan yläisäntään:

`hh_members`-toiston sisällä `${hh_id}` palauttaa **nykyisen** kotitalouden tunnuksen, ei kaikkien kotitalouksien tunnuksia.

---

## Järjestys toistoryhmissä: `rank-index()`

Kun `rank`-kenttä on toiston sisällä, käytä `rank-index(instanceNumber, repeatedField)` ulkopuolelta saadaksesi tietyn tapauksen ordinaalijarjestyksen:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` palauttaa korkeimman pistemäärän tapausindeksin.

---

## Parhaat käytännöt

1. Käytä aina `repeat_count`:ia, kun toistojen lukumäärä tiedetään etukäteen — se estää luetteloijia lisäämästä tai poistamasta tapauksia vahingossa.
2. Pidä toistoryhmät fokusoiduina — 20+ kysymyksen toisto per tapaus on vaikea navigoida.
3. Nimeä toistoryhmät selkeästi (esim. `household_members`, ei `repeat1`) — nimi näkyy funktiokutsuissa ja viedyissä tiedoissa.
4. Testaa maksimaalisen odotetun tapausmäärän kanssa suorituskyvyn tarkistamiseksi.
5. Käytä `field-list`-ulkoasua toistoryhmässä näyttääksesi kaikki kentät yhdellä näytöllä per tapaus (mobiili).

---

## Rajoitukset

- `indexed-repeat()` vaatii kelvollisen indeksin (1 tapausmäärään asti) — alueen ulkopuoliset indeksit palauttavat tyhjän.
- Sisäkkäiset toistot yli 2 tasoa eivät ole suositeltuja ja saattavat aiheuttaa näyttöongelmia joillakin asiakkailla.
- Koostefunktiot (`sum`, `count` jne.) toimivat koko toistoryhmälle — et voi koota osajoukkoa tapauksista ilman `*-if`-variantteja.
