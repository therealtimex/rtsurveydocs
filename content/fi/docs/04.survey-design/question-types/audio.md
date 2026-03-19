---
title: "Audio"
description: "Audio-kysymykset antavat vastaajille mahdollisuuden nauhoittaa ja lähettää äänitiedostoja osana kyselyä."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

`audio`-kysymystyyppi mahdollistaa vastaajien **nauhoittaa ääntä** tai ladata olemassa olevan äänitiedoston osana kyselyvastaustaan. Se on hyödyllinen suullisten kertomusten, ympäristöäänien, suositusten tai tietojen tallentamiseen, jotka välittyvät parhaiten äänen kautta tekstin sijaan.

## XLSForm-perusmäärittely

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| audio | voice_note  | Nauhoita kommenttisi           |

Lisätietoja audio-kysymystyypin standardista löytyy [XLSForm-spesifikaatiosta](https://xlsform.org/en/#question-types).

## Käyttötarkoitukset

Audio-kysymyksiä käytetään yleisesti:

1. Avoimien suullisten vastausten tallentamiseen luetteloijan kirjoitustaakan vähentämiseksi
2. Suositusten, henkilökohtaisten tarinoiden tai suullisten historioiden nauhoittamiseen
3. Ympäristöäänien dokumentointiin (esim. melutasot infrastruktuurin lähellä)
4. Äänentäytteiden keräämiseen kielelliseen tai terveystutkimukseen
5. Vastaajien mahdollistaminen lisätä suullisia selvennyksiä numeerisiin tai valintavastauksiin

## Tietomuoto

Äänitiedostot tallennetaan binääriliitteinä lomakkeen lähetyksen ohessa, tyypillisesti:

- **Muoto:** MP3 tai AAC (mobiilinauhiointi); WAV (korkealaatuinen nauhoitus)
- **Nimeäminen:** `{instanceID}-{fieldname}.mp3` (tai vastaava)
- **Tallennus:** Ladataan palvelimen mediahakemistoon ja yhdistetään lähetystietueeseen
- **Käyttö:** Toistettavissa ja ladattavissa lähetysten hallintaliittymästä

## rtSurveyn laajennukset

### Enimmäiskesto

Käytä `parameters`-saraketta nauhoituksen pituuden rajoittamiseen:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Nauhoita haastattelu | `max-duration=120` |

`max-duration` on sekunneissa. Tallennin pysähtyy automaattisesti rajalla.

### Laadun asetukset

Nauhoituksen laatu voidaan asettaa `parameters`-sarakkeen kautta:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Nauhoita palaute | `quality=normal` |

Tuetut arvot: `low`, `normal` (oletus), `voice-only`. `voice-only` optimoi puheäänelle melunvaimennuksella.

### Toisto ennen lähettämistä

Mobiililla luetteloija voi toistaa nauhoitetun klipin ennen jatkamista. Tämä on käytössä oletuksena — konfigurointia ei tarvita.

### Natiivi tallennin-integraatio

Androidilla ja iOS:llä `audio` käynnistää laitteen natiivin tallennussovelluksen. Verkossa se käyttää selaimen sisäänrakennettua MediaRecorder-API:a.

## Esimerkkikäyttö

### Enimmäiskeston ja vihjeen kanssa

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Kerro meille tapahtumasta omin sanoin | Puhu selkeästi. Nauhoitus pysähtyy 3 minuutin jälkeen. | `max-duration=180` |

### Ehdollinen ääni — vain jos ongelma on raportoitu

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Löytyikö ongelma? | | |
| audio | issue_audio | Nauhoita kuvaus ongelmasta | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Parhaat käytännöt

1. Ilmoita selkeästi `label`- tai `hint`-sarakkeessa, mitä luetteloijan tulisi sanoa ja kuinka kauan.
2. Käytä `max-duration`-parametria liian suurten tiedostojen estämiseksi alueilla, joilla on hidas latausnopeus.
3. Informoi vastaajia ennen nauhoituksen aloittamista — odottamaton nauhoitus voi herättää yksityisyyshuolenaiheita.
4. Testaa nauhoittaminen kohdelaitteella ja verkon olosuhteissa ennen käyttöönottoa.
5. Aseta `quality=voice-only` haastattelutyylisiin nauhoituksiin tiedostokoon pienentämiseksi ilman ymmärrettävyyden heikkenemistä.

## Rajoitukset

- Äänitiedostot voivat olla suuria (2 minuutin nauhoitus normaalilla laadulla on ~2–4 Mt) — ota tämä huomioon datasuunnitelmassa ja latausajan arvioissa.
- Kaikki selaimet eivät tue MediaRecorder-API:a — Chrome ja Firefox toimivat luotettavasti; Safari vanhemmilla iOS-versioilla voi olla ongelmia.
- Äänivastaausten litterointi vaatii lisäjälkikäsittelyä (manuaalinen tai automatisoitu puheesta tekstiksi).
- Yksityisyysmääräykset voivat rajoittaa äänten nauhoittamista — tarkista paikalliset tietosuojavaatimukset.
