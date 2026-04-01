---
weight: 5
title: "Første innlogging"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Slik logger du inn på rtSurvey-instansen din for første gang etter distribusjon."
---

> **SSL må konfigureres før du logger inn.** Hvis du åpner appen via HTTP, vil du se en sikkerhetsadvarsel og SSO vil bli blokkert. Fullfør [Oppsett av SSL](ssl-setup) først.

Når SSL er aktivt, åpne nettleseren på HTTPS-adressen din:

```
https://your-domain.com
```

---

## Innloggingsskjermen

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Innloggingssiden viser:

- Feltene **Brukernavn** og **Passord**
- En **Logg inn** knapp
- En **Logg inn med SSO** knapp (under en skillelinje) — for teammedlemmer med SSO-kontoer

---

## Standard administratorlegitimasjon

Skriv inn standardlegitimasjonen og klikk **Logg inn**:

| Felt | Verdi |
|------|-------|
| Brukernavn | `admin` |
| Passord | `admin` |

> **Endre passordet ditt umiddelbart etter første innlogging.**

---

## Hvis du ser en sikkerhetsadvarsel

Hvis du åpner appen via HTTP (før SSL er konfigurert), vil du se:

- Et gult advarselsbanner øverst på innloggingssiden
- En modal når du klikker **Logg inn**, som advarer om at legitimasjon vil sendes ukryptert

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klikk **Sett opp SSL** for å konfigurere HTTPS, eller **Fortsett uansett** for å logge inn uten SSL (anbefales ikke).

SSO-innlogging er fullstendig blokkert via HTTP — å klikke **Logg inn med SSO** vil vise et varsel i stedet for å omdirigere.

---

## Etter innlogging

Når du er inne, lander du på dashbordet. Herfra:

1. **Endre administratorpassord** — kontoinnstillinger → endre passord
2. **Opprett ditt første prosjekt** — Prosjekter → Nytt prosjekt
3. **Last opp eller bygg et skjema** — Skjemaer → Last opp XLSForm eller åpne Form Builder
4. **Legg til brukere** — Brukere → Inviter eller opprett kontoer for teamet ditt
