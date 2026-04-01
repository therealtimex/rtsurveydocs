---
weight: 5
title: "Første login"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Sådan logger du ind på din rtSurvey-instans for første gang efter installation."
---

> **SSL skal konfigureres, før du logger ind.** Hvis du tilgår appen via HTTP, vil du se en sikkerhedsadvarsel, og SSO vil blive blokeret. Fuldfør [Opsætning af SSL](ssl-setup) først.

Når SSL er aktivt, åbn din browser på din HTTPS-adresse:

```
https://your-domain.com
```

---

## Login-skærmen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Login-siden viser:

- **Brugernavn** og **Adgangskode** felter
- En **Log ind** knap
- En **Log ind med SSO** knap (under en skillelinje) — for teammedlemmer med SSO-konti

---

## Standard administratorlegitimationsoplysninger

Indtast standardlegitimationsoplysningerne og klik på **Log ind**:

| Felt | Værdi |
|------|-------|
| Brugernavn | `admin` |
| Adgangskode | `admin` |

> **Skift din adgangskode straks efter dit første login.**

---

## Hvis du ser en sikkerhedsadvarsel

Hvis du tilgår appen via HTTP (før SSL er konfigureret), vil du se:

- Et gult advarselsbanner øverst på login-siden
- En modal, når du klikker på **Log ind**, der advarer om, at legitimationsoplysninger vil blive sendt ukrypteret

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klik på **Opsæt SSL** for at konfigurere HTTPS, eller **Fortsæt alligevel** for at logge ind uden SSL (anbefales ikke).

SSO-login er fuldstændigt blokeret via HTTP — klik på **Log ind med SSO** vil vise en meddelelse i stedet for at omdirigere.

---

## Efter login

Når du er inde, lander du på dashboardet. Herfra:

1. **Skift administratoradgangskode** — kontoindstillinger → skift adgangskode
2. **Opret dit første projekt** — Projekter → Nyt projekt
3. **Upload eller byg en formular** — Formularer → Upload XLSForm eller åbn Form Builder
4. **Tilføj brugere** — Brugere → Inviter eller opret konti til dit team
