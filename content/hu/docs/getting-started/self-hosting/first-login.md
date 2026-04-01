---
weight: 5
title: "Első bejelentkezés"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Hogyan jelentkezzen be az rtSurvey példányába az üzembe helyezés utáni első alkalommal."
---

> **Az SSL-t be kell állítani a bejelentkezés előtt.** Ha HTTP-n keresztül éri el az alkalmazást, biztonsági figyelmeztetést fog látni, és az SSO le lesz tiltva. Először fejezze be az [SSL beállítást](ssl-setup).

Miután az SSL aktív, nyissa meg böngészőjét a HTTPS URL-jén:

```
https://your-domain.com
```

---

## A bejelentkezési képernyő

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

A bejelentkezési oldal mutatja:

- **Felhasználónév** és **Jelszó** mezők
- Egy **Bejelentkezés** gomb
- Egy **Bejelentkezés SSO-val** gomb (elválasztó alatt) — SSO-fiókkal rendelkező csapattagok számára

---

## Alapértelmezett adminisztrátori hitelesítő adatok

Adja meg az alapértelmezett hitelesítő adatokat, és kattintson a **Bejelentkezés** gombra:

| Mező | Érték |
|------|-------|
| Felhasználónév | `admin` |
| Jelszó | `admin` |

> **Azonnal változtassa meg jelszavát az első bejelentkezés után.**

---

## Ha biztonsági figyelmeztetést lát

Ha HTTP-n keresztül éri el az alkalmazást (az SSL konfigurálása előtt), a következőket fogja látni:

- Sárga figyelmeztető szalag a bejelentkezési oldal tetején
- Egy modális ablak a **Bejelentkezés** kattintásakor, amely figyelmeztet, hogy a hitelesítő adatokat titkosítás nélkül küldi el

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Kattintson az **SSL beállítása** gombra a HTTPS konfigurálásához, vagy a **Folytatás mindenképpen** gombra az SSL nélküli bejelentkezéshez (nem ajánlott).

Az SSO-bejelentkezés teljesen le van tiltva HTTP-n keresztül — az **SSO-val bejelentkezés** gombra kattintva értesítés jelenik meg az átirányítás helyett.

---

## Bejelentkezés után

Bejelentkezés után az irányítópulton landol. Innen:

1. **Adminisztrátori jelszó módosítása** — fiókbeállítások → jelszó módosítása
2. **Első projekt létrehozása** — Projektek → Új projekt
3. **Űrlap feltöltése vagy készítése** — Űrlapok → XLSForm feltöltése vagy Form Builder megnyitása
4. **Felhasználók hozzáadása** — Felhasználók → Meghívás vagy fiókok létrehozása csapatának
