---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Az rtCloud telepítése DigitalOcean Droplet-en automatizált user-data szkriptekkel."
---

A DigitalOcean **User Data** szkripteket használ, amelyek az első indításkor automatikusan futnak. Töltse ki a konfigurációs változókat a szkript tetején, majd illessze be a teljes szkriptet egy Droplet létrehozásakor.

> A Linode StackScriptekkel ellentétben a DigitalOcean-nek nincs űrlap felhasználói felülete — a szkriptet közvetlenül kell szerkeszteni beillesztés előtt.

**Szkript letöltése:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Beágyazott Keycloak (ajánlott)

A `digitalocean-droplet-keycloak-embed.sh` szkriptet használja a beépített SSO-val rendelkező legegyszerűbb beállításhoz.

### 1. lépés — A konfiguráció kitöltése

Nyissa meg a szkriptet, és szerkessze a tetején lévő `CONFIGURATION` blokkot:

```bash
# --- Kötelező ---
PROJECT_ID="rtsurvey"                  # A projekt egyedi azonosítója (szóközök nélkül)
ADMIN_PASSWORD="admin"                 # Jelszó az alkalmazás rendszergazdájához és a Keycloakhoz — az első bejelentkezés után változtassa meg

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Az Ön domainje — a DNS A-rekordnak ide kell mutatnia
PROJECT_URL=""                         # Hagyja üresen, hacsak nincs Cloudflare/proxy mögött
LETSENCRYPT_EMAIL="admin@example.com" # E-mail a Let's Encrypt értesítésekhez

# --- Opcionális ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Mező | Kötelező | Leírás |
|-------|----------|-------------|
| `PROJECT_ID` | Igen | Adatbázis nevként és Keycloak kliens azonosítóként használatos. Kisbetűs, szóközök nélkül. |
| `ADMIN_PASSWORD` | Nem | Jelszó az alkalmazás rendszergazdájához és a Keycloak adminisztrátori konzolhoz. Alapértéke `admin` — **az első bejelentkezés után változtassa meg**. |
| `DOMAIN` | Igen | Az Ön domain neve. A DNS A-rekordnak a Droplet IP-jére kell mutatnia. |
| `LETSENCRYPT_EMAIL` | Igen | E-mail cím a Let's Encrypt tanúsítványértesítésekhez. |
| `PROJECT_URL` | Nem | A nyilvános URL felülírása. Hagyja üresen a `DOMAIN` használatához. Cloudflare mögött hasznos. |

> **Biztonság:** Minden jelszó alapértéke `admin`. Az első bejelentkezés után azonnal változtassa meg őket.

### 2. lépés — Droplet létrehozása

A [DigitalOcean vezérlőpanelen](https://cloud.digitalocean.com):

1. Kattintson a **Create** → **Droplets** lehetőségre
2. Válassza az **Ubuntu 22.04 LTS** képfájlt
3. Válassza a **Basic, 4 GB RAM / 2 vCPU** vagy nagyobb lehetőséget
4. Görgessen az **Advanced Options** → jelölje be az **Add Initialization scripts** lehetőséget
5. Illessze be a szkript teljes tartalmát a szövegmezőbe
6. Kattintson a **Create Droplet** lehetőségre

### 3. lépés — A DNS-rekord hozzáadása

Miközben a Droplet elindul, adjon hozzá egy **A-rekordot** a DNS-szolgáltatójánál:

```
Típus  : A
Név    : myapp          (vagy @ a gyökér domainhez)
Érték  : <droplet-ip>
TTL    : 300
```

### 4. lépés — Folyamat figyelése

SSH-val csatlakozzon a Droplet-hez, és figyelje a naplót:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

A szkript a kezdet közelében nyomtatja ki a kiszolgáló IP-jét — adja hozzá a DNS-rekordot, amint megjelenik.

### 5. lépés — Az alkalmazás elérése

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

Nyissa meg a `https://myapp.example.com` oldalt a böngészőjében, és jelentkezzen be `admin` felhasználónévvel és `admin` jelszóval.

> **Változtassa meg jelszavát** azonnal a bejelentkezés után a jobb felső sarokban lévő **Beállítások** menüponton keresztül.

---

## Telepítés után

### Jelszó megváltoztatása

SSH-val csatlakozzon a Droplet-hez, szerkessze a `.env` fájlt, és indítsa újra az érintett konténert:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### A domain frissítése

Ha a telepítés után más domaint rendel hozzá, frissítse a `PROJECT_URL` értékét a `.env` fájlban:

```bash
nano /opt/rtcloud/.env   # frissítse a PROJECT_URL= értéket
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Az összes konténer megtekintése

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
