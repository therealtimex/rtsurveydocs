---
weight: 5
title: "Hyrja e parë"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Si të identifikoheni në instancën tuaj rtSurvey për herë të parë pas vendosjes."
---

> **SSL duhet konfiguruar para hyrjes.** Nëse aksesoni aplikacionin nëpërmjet HTTP, do të shihni një paralajmërim sigurie dhe SSO do të bllokohet. Plotësoni fillimisht [Konfigurimin e SSL](ssl-setup).

Pasi SSL të jetë aktiv, hapni shfletuesin tuaj në URL-in HTTPS:

```
https://your-domain.com
```

---

## Ekrani i hyrjes

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Faqja e hyrjes shfaq:

- Fushat **Emri i përdoruesit** dhe **Fjalëkalimi**
- Butonin **Hyr**
- Butonin **Hyr me SSO** (nën një ndarës) — për anëtarët e ekipit me llogari SSO

---

## Kredencialet e paracaktuara të administratorit

Vendosni kredencialet e paracaktuara dhe klikoni **Hyr**:

| Fusha | Vlera |
|-------|-------|
| Emri i përdoruesit | `admin` |
| Fjalëkalimi | `admin` |

> **Ndryshoni fjalëkalimin tuaj menjëherë pas hyrjes së parë.**

---

## Nëse shihni një paralajmërim sigurie

Nëse aksesoni aplikacionin nëpërmjet HTTP (para konfigurimit të SSL), do të shihni:

- Një baner paralajmërimi të verdhë në krye të faqes së hyrjes
- Një modal kur klikoni **Hyr**, që paralajmëron se kredencialet do të dërgohen të pashifruara

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klikoni **Konfiguro SSL** për të konfiguruar HTTPS, ose **Vazhdoni gjithsesi** për të hyrë pa SSL (nuk rekomandohet).

Hyrja SSO është bllokuar plotësisht nëpërmjet HTTP — klikimi i **Hyr me SSO** do të shfaqë një njoftim në vend të ridrejtimit.

---

## Pas hyrjes

Pasi të jeni brenda, do të arrini në panel. Nga këtu:

1. **Ndryshoni fjalëkalimin e administratorit** — cilësimet e llogarisë → ndrysho fjalëkalimin
2. **Krijoni projektin tuaj të parë** — Projektet → Projekt i ri
3. **Ngarkoni ose ndërtoni një formular** — Formularët → Ngarko XLSForm ose hapni Form Builder
4. **Shtoni përdorues** — Përdoruesit → Ftoni ose krijoni llogari për ekipin tuaj
