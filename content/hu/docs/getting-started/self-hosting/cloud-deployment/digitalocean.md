---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Telepítse az rtCloud-ot egy DigitalOcean Droplet-en automatizált felhasználói adatszkriptek segítségével."
---

A DigitalOcean **User Data** szkripteket használ, amelyek automatikusan futnak az első rendszerindításkor. A parancsfájl tetején töltse ki a konfigurációs változókat, majd a Droplet létrehozásakor beilleszti a teljes szkriptet.

> A Linode StackScripts-től eltérően a DigitalOceannek nincs űrlapos felhasználói felülete – közvetlenül a beillesztés előtt kell szerkesztenie a szkriptet.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Beágyazott kulcsköpeny (ajánlott)

Használja a "digitalocean-droplet-keycloak-embed.sh" fájlt a legegyszerűbb beállításhoz a beépített SSO-val.

### 1. lépés – Töltse ki a konfigurációt

Nyissa meg a szkriptet, és szerkessze felül a `CONFIGURATION' blokkot:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Mező | Kötelező | Leírás |
|-------|----------|--------------|
| "PROJECT_ID" | Igen | Adatbázisnévként és Keycloak ügyfélazonosítóként használatos. Kisbetűk, szóközök nélkül. |
| `ADMIN_PASSWORD` | Nem | Jelszó az alkalmazás adminisztrátori bejelentkezéséhez és a Keycloak felügyeleti konzolhoz. Alapértelmezésben az „admin” – **módosítás az első bejelentkezés után**. |
| "DOMAIN" | Igen | Az Ön domain neve. DNS A rekordnak a Droplet IP-re kell mutatnia. |
| `LETSENCRYPT_EMAIL` | Igen | E-mail cím a Let's Encrypt tanúsítványértesítésekhez. |
| `PROJECT_URL` | Nem | A nyilvános URL felülbírálása. Hagyja üresen a "DOMAIN" használatához. Hasznos a Cloudflare mögött. |

> **Biztonság:** Minden jelszó alapértelmezés szerint "admin". Az első bejelentkezés után azonnal módosítsa őket.

### 2. lépés – Hozzon létre egy cseppet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Kattintson a **Létrehozás** → **Cseppek** lehetőségre.
2. Válassza ki képként az **Ubuntu 22.04 LTS** lehetőséget
3. Válassza az **Alap, 4 GB RAM / 2 vCPU** vagy nagyobb lehetőséget
4. Görgessen a **Speciális beállítások** elemhez → jelölje be az **Inicializálási szkriptek hozzáadása** lehetőséget.
5. Illessze be a teljes szkript tartalmát a szövegmezőbe
6. Kattintson a **Csepp létrehozása** lehetőségre.

### 3. lépés – Adja hozzá a DNS-rekordot

Amíg a Droplet elindul, adjon hozzá egy **A rekordot** a DNS-szolgáltatóhoz:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### 4. lépés – Kövesse nyomon a folyamatot

SSH-t a cseppbe, és nézze meg a naplót:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

A szkript kinyomtatja a szerver IP-címét a kezdet közelében – amint látja, adja hozzá a DNS-rekordot.

### 5. lépés – Nyissa meg az alkalmazást

Amikor a telepítés befejeződött, a napló összefoglalót mutat:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Változtassa meg jelszavát** azonnal bejelentkezés után a jobb felső menü **Beállítások** menüpontjában.

---

## A telepítés után

### Jelszó módosítása

SSH-t a Dropletbe, szerkessze a ".env" fájlt, és indítsa újra az érintett tárolót:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Frissítse a tartományt

Ha a telepítés után másik domaint rendel hozzá, frissítse a `PROJECT_URL-t a `.env'-ben:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Az összes tároló megtekintése

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
