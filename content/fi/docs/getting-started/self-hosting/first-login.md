---
weight: 5
title: "Ensimmäinen kirjautuminen"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Kuinka kirjautua rtSurvey-instanssiisi ensimmäistä kertaa käyttöönoton jälkeen."
---

> **SSL täytyy määrittää ennen kirjautumista.** Jos käytät sovellusta HTTP:n kautta, näet tietoturvawarauksen ja SSO estetään. Suorita ensin [SSL:n asennus](ssl-setup).

Kun SSL on aktiivinen, avaa selain HTTPS-osoitteessasi:

```
https://your-domain.com
```

---

## Kirjautumissivu

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Kirjautumissivulla näkyy:

- **Käyttäjänimi** ja **Salasana** -kentät
- **Kirjaudu sisään** -painike
- **Kirjaudu SSO:lla** -painike (jakajan alla) — tiimin jäsenille, joilla on SSO-tilit

---

## Oletusarvoinen ylläpitäjän tunniste

Anna oletustunnisteet ja napsauta **Kirjaudu sisään**:

| Kenttä | Arvo |
|--------|------|
| Käyttäjänimi | `admin` |
| Salasana | `admin` |

> **Vaihda salasanasi välittömästi ensimmäisen kirjautumisen jälkeen.**

---

## Jos näet tietoturvawarauksen

Jos käytät sovellusta HTTP:n kautta (ennen SSL:n määrittämistä), näet:

- Keltainen varoitusbanneri kirjautumissivun yläosassa
- Modaali-ikkuna, kun napsautat **Kirjaudu sisään**, varoittaen, että tunnisteet lähetetään salaamattomina

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Napsauta **Asenna SSL** määrittääksesi HTTPS tai **Jatka joka tapauksessa** kirjautuaksesi ilman SSL:ää (ei suositella).

SSO-kirjautuminen on täysin estetty HTTP:n kautta — **Kirjaudu SSO:lla** -painikkeen napsauttaminen näyttää ilmoituksen uudelleenohjauksen sijaan.

---

## Kirjautumisen jälkeen

Kirjautumisen jälkeen pääset kojelautaan. Sieltä:

1. **Vaihda ylläpitäjän salasana** — tilin asetukset → vaihda salasana
2. **Luo ensimmäinen projektisi** — Projektit → Uusi projekti
3. **Lataa tai luo lomake** — Lomakkeet → Lataa XLSForm tai avaa Form Builder
4. **Lisää käyttäjiä** — Käyttäjät → Kutsu tai luo tiimisi jäsenille tilit
