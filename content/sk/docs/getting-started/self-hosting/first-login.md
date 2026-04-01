---
weight: 5
title: "Prvé prihlásenie"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Ako sa prihlásiť do vašej inštancie rtSurvey po prvýkrát po nasadení."
---

> **Pred prihlásením musí byť nakonfigurovaný SSL.** Ak pristupujete k aplikácii cez HTTP, zobrazí sa bezpečnostné upozornenie a SSO bude zablokované. Najprv dokončite [Nastavenie SSL](ssl-setup).

Po aktivácii SSL otvorte prehliadač na vašej HTTPS adrese:

```
https://your-domain.com
```

---

## Prihlasovacia obrazovka

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Prihlasovacia stránka zobrazuje:

- Polia **Používateľské meno** a **Heslo**
- Tlačidlo **Prihlásiť sa**
- Tlačidlo **Prihlásiť sa cez SSO** (pod oddeľovačom) — pre členov tímu s SSO účtami

---

## Predvolené prihlasovacie údaje správcu

Zadajte predvolené prihlasovacie údaje a kliknite na **Prihlásiť sa**:

| Pole | Hodnota |
|------|---------|
| Používateľské meno | `admin` |
| Heslo | `admin` |

> **Zmeňte heslo ihneď po prvom prihlásení.**

---

## Ak sa zobrazí bezpečnostné upozornenie

Ak pristupujete k aplikácii cez HTTP (pred konfiguráciou SSL), uvidíte:

- Žltý varovný banner v hornej časti prihlasovacej stránky
- Modálne okno pri kliknutí na **Prihlásiť sa**, upozorňujúce, že prihlasovacie údaje budú odoslané nešifrovane

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Kliknite na **Nastaviť SSL** pre konfiguráciu HTTPS alebo **Pokračovať napriek tomu** pre prihlásenie bez SSL (neodporúča sa).

Prihlásenie cez SSO je cez HTTP úplne zablokované — kliknutím na **Prihlásiť sa cez SSO** sa zobrazí oznámenie namiesto presmerovania.

---

## Po prihlásení

Po prihlásení pristanete na dashboarde. Odtiaľ:

1. **Zmeniť heslo správcu** — nastavenia účtu → zmeniť heslo
2. **Vytvoriť prvý projekt** — Projekty → Nový projekt
3. **Nahrať alebo vytvoriť formulár** — Formuláre → Nahrať XLSForm alebo otvoriť Form Builder
4. **Pridať používateľov** — Používatelia → Pozvať alebo vytvoriť účty pre váš tím
