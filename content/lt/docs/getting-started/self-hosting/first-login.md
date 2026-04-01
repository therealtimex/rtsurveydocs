---
weight: 5
title: "Pirmasis prisijungimas"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Kaip prisijungti prie savo rtSurvey egzemplioriaus pirmą kartą po diegimo."
---

> **Prieš prisijungimą turi būti sukonfigūruotas SSL.** Jei pasiekiate programą per HTTP, pamatysite saugos įspėjimą ir SSO bus užblokuotas. Pirmiausia užbaikite [SSL nustatymą](ssl-setup).

Kai SSL aktyvus, atidarykite naršyklę savo HTTPS URL:

```
https://your-domain.com
```

---

## Prisijungimo ekranas

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Prisijungimo puslapis rodo:

- **Vartotojo vardas** ir **Slaptažodis** laukai
- **Prisijungti** mygtukas
- **Prisijungti per SSO** mygtukas (žemiau skyriklio) — komandos nariams su SSO paskyromis

---

## Numatytieji administratoriaus duomenys

Įveskite numatytuosius duomenis ir spustelėkite **Prisijungti**:

| Laukas | Reikšmė |
|--------|---------|
| Vartotojo vardas | `admin` |
| Slaptažodis | `admin` |

> **Nedelsdami pakeiskite slaptažodį po pirmojo prisijungimo.**

---

## Jei matote saugos įspėjimą

Jei pasiekiate programą per HTTP (prieš SSL konfigūraciją), pamatysite:

- Geltoną įspėjimo juostą prisijungimo puslapio viršuje
- Modalinį langą paspaudus **Prisijungti**, įspėjantį, kad duomenys bus siunčiami nešifruoti

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Spustelėkite **Nustatyti SSL** HTTPS konfigūravimui arba **Tęsti bet kokiu atveju** prisijungimui be SSL (nerekomenduojama).

SSO prisijungimas visiškai užblokuotas per HTTP — paspaudus **Prisijungti per SSO** bus rodomas pranešimas vietoj nukreipimo.

---

## Po prisijungimo

Prisijungę pateksite į prietaisų skydelį. Iš čia:

1. **Keisti administratoriaus slaptažodį** — paskyros nustatymai → keisti slaptažodį
2. **Kurti pirmąjį projektą** — Projektai → Naujas projektas
3. **Įkelti arba kurti formą** — Formos → Įkelti XLSForm arba atidaryti Form Builder
4. **Pridėti vartotojus** — Vartotojai → Pakviesti arba sukurti paskyras jūsų komandai
