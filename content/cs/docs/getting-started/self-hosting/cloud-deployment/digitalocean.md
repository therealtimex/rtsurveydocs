---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Nasaďte rtCloud na DigitalOcean Droplet pomocí automatických skriptů uživatelských dat."
---

DigitalOcean používá skripty **User Data**, které se spouštějí automaticky při prvním spuštění. Vyplníte konfigurační proměnné v horní části skriptu a poté vložíte celý skript při vytváření Droplet.

> Na rozdíl od Linode StackScripts nemá DigitalOcean uživatelské rozhraní formuláře – skript musíte upravit přímo před vložením.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Vestavěná maska ​​na klíče (doporučeno)

Pro nejjednodušší nastavení s vestavěným SSO použijte `digitalocean-droplet-keycloak-embed.sh`.

### Krok 1 — Vyplňte konfiguraci

Otevřete skript a upravte blok `CONFIGURATION` v horní části:

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

| Pole | Povinné | Popis |
|-------|----------|-------------|
| `PROJECT_ID` | Ano | Používá se jako název databáze a ID klienta Keycloak. Malá písmena, žádné mezery. |
| `ADMIN_PASSWORD` | Ne | Heslo pro přihlášení správce aplikace a administrátorskou konzoli Keycloak. Výchozí hodnota je `admin` — **změna po prvním přihlášení**. |
| `DOMÉNA` | Ano | Název vaší domény. DNS Záznam musí ukazovat na IP Droplet. |
| `LETSENCRYPT_EMAIL` | Ano | E-mailová adresa pro oznámení certifikátu Let's Encrypt. |
| `PROJECT_URL` | Ne | Přepište veřejnou adresu URL. Chcete-li použít `DOMAIN`, ponechte prázdné. Užitečné za Cloudflare. |

> **Zabezpečení:** Všechna hesla mají výchozí hodnotu `admin`. Změňte je ihned po prvním přihlášení.

### Krok 2 — Vytvořte kapku

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klikněte na **Vytvořit** → **Kapky**
2. Jako obrázek vyberte **Ubuntu 22.04 LTS**
3. Vyberte **Základní, 4 GB RAM / 2 vCPU** nebo větší
4. Přejděte na **Pokročilé možnosti** → zaškrtněte **Přidat inicializační skripty**
5. Vložte celý obsah skriptu do textové oblasti
6. Klikněte na **Vytvořit kapku**

### Krok 3 — Přidejte záznam DNS

Zatímco se Droplet spouští, přidejte záznam **A** do svého poskytovatele DNS:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Krok 4 – Sledujte pokrok

SSH do Dropletu a sledujte protokol:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skript vytiskne IP adresu vašeho serveru blízko začátku – přidejte záznam DNS, jakmile jej uvidíte.

### Krok 5 — Přístup k aplikaci

Po dokončení nastavení se v protokolu zobrazí souhrn:

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

> **Změňte své heslo** ihned po přihlášení přes **Nastavení** v menu vpravo nahoře.

---

## Po nasazení

### Změňte heslo

SSH do Dropletu, upravte soubor `.env` a restartujte dotčený kontejner:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aktualizujte doménu

Pokud po nasazení přiřadíte jinou doménu, aktualizujte `PROJECT_URL` v `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Zobrazit všechny kontejnery

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
