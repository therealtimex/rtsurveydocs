---
weight: 5
title: "Pirmā pieteikšanās"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Kā pirmo reizi pieteikties savā rtSurvey instancē pēc izvietošanas."
---

> **Pirms pieteikšanās jākonfigurē SSL.** Ja piekļūstat lietotnei caur HTTP, tiks parādīts drošības brīdinājums un SSO tiks bloķēts. Vispirms pabeidziet [SSL iestatīšanu](ssl-setup).

Kad SSL ir aktīvs, atveriet pārlūkprogrammu savā HTTPS URL:

```
https://your-domain.com
```

---

## Pieteikšanās ekrāns

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Pieteikšanās lapā redzams:

- **Lietotājvārds** un **Parole** lauki
- **Pierakstīties** poga
- **Pierakstīties ar SSO** poga (zem atdalītāja) — komandas locekļiem ar SSO kontiem

---

## Noklusējuma administratora akreditācijas dati

Ievadiet noklusējuma akreditācijas datus un noklikšķiniet uz **Pierakstīties**:

| Lauks | Vērtība |
|-------|---------|
| Lietotājvārds | `admin` |
| Parole | `admin` |

> **Nomainiet paroli uzreiz pēc pirmās pieteikšanās.**

---

## Ja tiek parādīts drošības brīdinājums

Ja piekļūstat lietotnei caur HTTP (pirms SSL konfigurēšanas), redzēsit:

- Dzeltenu brīdinājuma joslu pieteikšanās lapas augšā
- Modālo logu, noklikšķinot uz **Pierakstīties**, brīdinot, ka akreditācijas dati tiks nosūtīti nešifrēti

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Noklikšķiniet uz **Iestatīt SSL**, lai konfigurētu HTTPS, vai uz **Turpināt tāpat** pieteikšanās bez SSL (nav ieteicams).

SSO pieteikšanās caur HTTP ir pilnībā bloķēta — noklikšķinot uz **Pierakstīties ar SSO**, tiks parādīts paziņojums, nevis novirzīšana.

---

## Pēc pieteikšanās

Pēc pieteikšanās nokļūsit informācijas panelī. No šejienes:

1. **Mainīt administratora paroli** — konta iestatījumi → mainīt paroli
2. **Izveidot pirmo projektu** — Projekti → Jauns projekts
3. **Augšupielādēt vai izveidot veidlapu** — Veidlapas → Augšupielādēt XLSForm vai atvērt Form Builder
4. **Pievienot lietotājus** — Lietotāji → Uzaicināt vai izveidot kontus jūsu komandai
