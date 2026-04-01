---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Järjestelmäkäyttäjä"
icon: "people"
toc: true
description: "Hallitse rooleja, oikeuksia ja kaikkien alustan osallistujien perehdyttämistä."
tags: ["Users", "Access Control", "Onboarding", "Roles"]
---

# Järjestelmäkäyttäjien hallinta

**Järjestelmäkäyttäjä**-moduuli (`/cpms/cpmsSystemUser/admin`) on kattava hallintakäyttöliittymä, jolla voidaan hallita, kenellä on pääsy Real-Time Survey -alustallesi (RT-CPMS) ja mitä toimintoja he voivat suorittaa.

![Järjestelmäkäyttäjän käyttöliittymä](/images/system_user.png)

## Yhtenäinen hallintamenetelmä

RT-CPMS:ssä **haastattelija** on yksinkertaisesti tietty rooli, joka on määritetty järjestelmäkäyttäjälle. Erillistä "haastattelija"-tietokantaa ei ole. Oli käyttäjä sitten korkean tason järjestelmänvalvoja, joka seuraa verkkoportaalia, tai kenttähaastattelija, joka kerää tietoja mobiilisovelluksella, heitä kaikkia hallitaan tässä yhdessä yhtenäisessä kehyksessä.

## Tärkeimmät ominaisuudet

### 1. Käyttäjähakemisto ja ruudukkonäkymä
Pääkäyttöliittymä näyttää sivutetun luettelon kaikista työtilaan liitetyistä käyttäjistä. Tärkeimmät attribuutit ovat:
* **Organisaation tunnus ja nimi**: Käyttäjien looginen ryhmittely tiettyjen organisaatioyksiköiden alle (esim. `rta`, `partner_org`).
* **Rooli**: Määrittää käyttäjän käyttöoikeustason (esim. `Järjestelmänvalvoja`, `Tiimin johtaja`, `Haastattelija`).
* **Ryhmä**: Alueelliset tai loogiset ryhmämääritykset (esim. tietyt alueet tai operatiiviset tiimit).
* **On synkronoitu**: Ilmaisee, onko tili onnistuneesti integroitu keskitettyyn kertakirjautumis-(SSO)-järjestelmään.
* **Tila**: Visuaaliset indikaattorit, jotka vahvistavat, onko tili `Aktiivinen`, `Epäaktiivinen`, `Poistettu` tai `Estetty`.

**Yleiset toiminnot:**
* **Lisää järjestelmäkäyttäjä**: Luo manuaalisesti yksittäinen profiili.
* **Tuo järjestelmäkäyttäjiä**: Joukkolataustileistä Excel-mallilla. Ristiriidat voidaan ratkaista `Ohita`- tai `Korvaa`-tilassa ja synkronoida suoraan SSO:n kanssa.
* **Joukkopoisto**: Monivalintatuki tilien joukkopoistoon.

### 2. Pääsynhallinta ja turvallisuus
Käyttäjäprofiilia luotaessa tai muokattaessa on käytettävissä useita kriittisiä turvallisuus- ja työnkulkukenttiä:
* **Käyttäjäkoodi**: Yksilöllinen tunniste, joka yhdistää paikallisen CPMS-tilin keskitettyyn SSO-tietovarastoon.
* **Laitteen vaihtokoodi**: Vankka suojaustunnus, jota tarvitaan, kun haastattelija haluaa vaihtaa tiedonkeruuseen käyttämäänsä mobiililaitetta.
* **Käyttöoikeustaso**: Yksityiskohtainen prioriteetti-/käyttöoikeusasteikko välillä 0 (alin) – 20 (korkein).
* **Valvontatoiminto**: Valintaruutu, joka välittömästi korottaa tavallisen käyttäjän hallintotasolle.
* **Työnkulun automatisointi**: Vaihtoehto "Hyväksy muutospyyntö automaattisesti", mikä tehostaa luotettujen käyttäjien tietojen puhdistus- ja varmistusprosessia.

### 3. Koodien hallinta (automatisoitu perehdyttäminen)
"Koodi"-välilehdeltä löytyvä ominaisuus hallitsee hajautuspohjaisia rekisteröinti- ja kutsulinkejä, mikä tehostaa suurten tiimien perehdyttämistä.

* **Rekisteröinti vs. kutsu**: Valitse, voivatko käyttäjät rekisteröityä itse jaetun linkin kautta vai tarvitsevatko he suoran järjestelmänvalvojan kutsun.
* **Vanhentumispäivät**: Rajaa perehdyttäminen tiettyihin aikaikkunoihin.
* **Käyttörajoitukset**: Rajoita yhdellä generoidulla koodilla liittyvien käyttäjien määrää.
* **Ennalta määritetyt roolit**: Näiden koodien kautta liittyvät käyttäjät perivät automaattisesti ennalta määritetyn roolin ja käyttöoikeustason, mikä varmistaa heidän valmiutensa toimia välittömästi ilman manuaalista järjestelmänvalvojan väliintuloa.
