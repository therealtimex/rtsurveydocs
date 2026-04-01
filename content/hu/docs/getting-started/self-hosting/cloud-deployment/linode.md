---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Az rtCloud telepítése Linode-on StackScriptekkel, amelyek űrlapalapú konfigurációs felhasználói felülettel rendelkeznek."
---

A Linode **StackScripteket** használ — olyan szkripteket, amelyekhez űrlapalapú felhasználói felület tartozik, ahol a konfigurációs mezőket közvetlenül a Linode Managerben töltheti ki kód szerkesztése nélkül.

> A Linode StackScriptek a legegyszerűbb telepítési módszer. A mezők űrlapként jelennek meg egy Linode létrehozásakor — nincs szükség szkriptszerkesztésre.

---

## Beágyazott Keycloak (ajánlott)

### 1. lépés — A StackScript megkeresése

A StackScript nyilvánosan elérhető a Linode közösségben — nincs szükség kézi beállításra:

1. Lépjen a **Linodes** → **Create Linode** menüpontra
2. A **Choose a Distribution** alatt válassza a **StackScripts** → **Community StackScripts** lehetőséget
3. Keresse az **`RTA rtSurvey - Self-Hosted with Keycloak SSO`** szkriptet
4. Válassza ki, és töltse ki a konfigurációs űrlapot:

> Alternatív megoldásként [töltse le a szkriptet](/scripts/linode-stackscript-keycloak-embed.sh), és hozzon létre saját StackScriptet a **StackScripts** → **Create StackScript** menüpont alatt.

| Mező | Kötelező | Leírás |
|-------|----------|-------------|
| Project ID | Nem | Egyedi azonosító (alapértelmezett: `rtsurvey`). Adatbázis nevként és Keycloak kliens azonosítóként használatos. |
| Keycloak Admin Password | Nem | Jelszó a Keycloak adminisztrátori konzolhoz és az alkalmazás rendszergazdai bejelentkezéséhez. Alapértéke `admin` — **az első bejelentkezés után változtassa meg**. |
| Domain | Igen | Az Ön domain neve. A DNS A-rekordnak erre a Linode IP-jére kell mutatnia. HTTPS-hez és Keycloakhoz szükséges. |
| Let's Encrypt Email | Igen | E-mail a Let's Encrypt tanúsítványértesítésekhez. |
| Docker Image Tag | Nem | Telepítendő képfájl (alapértelmezett: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Biztonság:** Minden jelszó alapértéke `admin`. Az első bejelentkezés után azonnal változtassa meg őket.

5. Válassza az **Ubuntu 22.04 LTS** képfájlt
6. Válassza a **Shared CPU 4 GB** csomagot vagy nagyobbat
7. Kattintson a **Create Linode** lehetőségre

### 2. lépés — A DNS-rekord hozzáadása

Miközben a Linode elindul, adjon hozzá egy **A-rekordot** a DNS-szolgáltatójánál:

```
Típus  : A
Név    : myapp          (vagy @ a gyökér domainhez)
Érték  : <linode-ip>
TTL    : 300
```

### 3. lépés — Folyamat figyelése

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

A szkript a kezdet közelében nyomtatja ki a kiszolgáló IP-jét — adja hozzá a DNS-rekordot, amint megjelenik.

### 4. lépés — Az alkalmazás elérése

A beállítás befejezésekor a napló összefoglalót mutat:

```
============================================================
 rtCloud telepítés kész! (Beágyazott Keycloak)
============================================================
 Alkalmazás URL   : https://myapp.example.com
 Rendszergazda    : admin / admin
 Keycloak         : https://myapp.example.com/auth/admin

 !! BIZTONSÁG: Minden jelszó alapértéke 'admin'.
    Az első bejelentkezés után azonnal változtassa meg őket.
============================================================
```

Jelentkezzen be `admin` felhasználónévvel és `admin` jelszóval, majd azonnal változtassa meg jelszavát.

---

## Telepítés után

### Jelszó megváltoztatása

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Az összes konténer megtekintése

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### A napló ellenőrzése

```bash
tail -200 /var/log/stackscript.log
```
