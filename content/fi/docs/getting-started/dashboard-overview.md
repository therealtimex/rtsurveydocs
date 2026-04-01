---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Koontinäytön yleiskatsaus"
icon: "home"
toc: true
description: "RT-CPMS-järjestelmän koontinäytön ja projektin seurantatyökalujen ymmärtäminen."
tags: ["Dashboard", "Overview", "Monitoring"]
---

# Järjestelmän koontinäyttö

Koontinäyttö (`/cpms/cpmsDashBoard/indexNew`) toimii hallinnollisena komentokeskuksena ja Real-Time Survey -alustan (RT-CPMS) ensisijaisena aloitussivuna.

![Järjestelmän koontinäyttö](/images/dashboard_overview.png)

Se on suunniteltu antamaan kyselyn hallitsijoille välitön yleiskuva aktiivisista projekteista, pikavalinnat olennaisiin työkaluihin ja keskitetty solmupiste kaikkien tärkeimpien alustamoduulien välillä navigoimiseen.

## Tärkeimmät ominaisuudet

### 1. Projektin ja lomakkeen valinta
Vasemmanpuoleinen paneeli sisältää **Lomakkeet ja raportit** -navigaattorin. Tämä alue listaa kaikki työtilassasi olevat aktiiviset kyselyt.
* Valitsemalla tietyn kyselyn (esim. *RTA - SURVEY 02*) ohjaat koontinäytön keskittämään seurannan ja mittarit yksinomaan kyseiseen projektiin.

### 2. Visualisointi- ja mittarisuodattimet
Projektiluettelon yläpuolella voit vaihtaa useiden kriittisten datanäkymien välillä reaaliaikaisen kenttätyön edistymisen seuraamiseksi:
* **Lukumäärä aloitusajan mukaan / lopetusajan mukaan**: Seuraa, milloin haastattelijat aloittavat ja lopettavat kyselyistuntonsa.
* **Lukumäärä lähetyspäivämäärän mukaan**: Seuraa palvelimelle saapuvien tietojen päivittäistä kokonaismäärää.
* **Lukumäärä käyttäjänimen mukaan**: Arvioi yksittäisten haastattelijoiden tuottavuutta ja suorituskykyä.
* **Haastattelukartta**: Tarkastele kyselyvastausten GPS-sijainnin maantieteellistä (GIS) jakaumaa varmistaaksesi, että alueelliset kattavuusvaatimukset täyttyvät.

### 3. Sovellusportaalit
Koontinäytön keskikohta tarjoaa välittömän pääsyn tiedonkeruun käyttöliittymiin. Haastattelijoiden laitteistosta riippuen voit käynnistää tai ohjata heidät:
* **Verkkosovellus**: Selauspohjainen tiedonkeruu.
* **Android-sovellus**: Linkki Google Play Storeen tai APK:hon.
* **iOS-sovellus**: Linkki Apple App Storeen.

### 4. Suorat moduulipikavalinnat
Kolme näkyvää toimintopainiketta mahdollistavat nopean siirtymisen eniten käytettyihin toiminnallisiin moduuleihin:
* **Lomake ja tiedonsyöttö**: Siirry suoraan kerättyjen tietojen manuaaliseen hallintaan.
* **Analytiikka ja raportit**: Avaa Business Intelligence (BI) -ohjelmisto kyselyvastausten ristiintaulukointiin ja kaavioihin.
* **Oikeuksien määritykset**: Säädä, kenellä on pääsy aktiiviseen kyselyyn ja mitä rooleja heillä on.

### 5. Globaali navigointipalkki
Tiivistettävä vasen sivupalkki tarjoaa pääsyn RT-CPMS-taustamoduulien koko ekosysteemiin. Täältä voit syventyä:
* **Asetukset**: Henkilöstön ja aktiivisten laitteiden hallinta.
* **Kenttätyön hallinta**: Haastattelijoiden päivittäisen toiminnan seuranta.
* **Laadunvarmistus**: QA-sääntöjen ja -merkintöjen käyttöönotto ja tarkistus.
* **Lopputuotokset**: Puhdistettujen tietojoukkojen vienti CSV-, PDF- tai Stata-muodossa.
