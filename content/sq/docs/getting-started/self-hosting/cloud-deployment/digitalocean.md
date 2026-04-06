---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Vendosni rtCloud në një Droplet DigitalOcean duke përdorur skriptet e automatizuara të të dhënave të përdoruesit."
---

DigitalOcean përdor skriptet **Të dhënat e përdoruesit** që funksionojnë automatikisht në nisjen e parë. Ju plotësoni variablat e konfigurimit në krye të skriptit, pastaj ngjisni të gjithë skriptin kur krijoni një Droplet.

> Ndryshe nga Linode StackScripts, DigitalOcean nuk ka UI formë — duhet ta modifikoni skriptin direkt përpara se ta ngjitni.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Tastiera e integruar (rekomandohet)

Përdorni `digitalocean-droplet-keycloak-embed.sh` për konfigurimin më të thjeshtë me SSO të integruar.

### Hapi 1 - Plotësoni konfigurimin

Hapni skriptin dhe modifikoni bllokun "CONFIGURATION" në krye:

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

| Fusha | Kërkohet | Përshkrimi |
|-------|----------|-------------|
| `PROJECT_ID` | Po | Përdoret si emër i bazës së të dhënave dhe ID e klientit Keycloak. Shkronja të vogla, pa hapësira. |
| `ADMIN_PASSWORD` | Jo | Fjalëkalimi për hyrjen e administratorit të aplikacionit dhe tastierën e administratorit Keycloak. Parazgjedhjet në `admin` — **ndryshojnë pas hyrjes së parë**. |
| `DOMAIN` | Po | Emri juaj i domenit. DNS Një rekord duhet të tregojë në IP-në e pikës. |
| `LETSENCRYPT_EMAIL` | Po | Adresa e emailit për njoftimet e certifikatës Let's Encrypt. |
| `PROJECT_URL` | Jo | Anuloni URL-në publike. Lëreni bosh për të përdorur "DOMAIN". E dobishme pas Cloudflare. |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

### Hapi 2 - Krijoni një pikëz

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klikoni **Krijo** → **Pikat**
2. Zgjidhni **Ubuntu 22.04 LTS** si imazh
3. Zgjidhni **Basic, 4 GB RAM / 2 vCPU ** ose më të mëdha
4. Shkoni te **Opsionet e avancuara** → kontrolloni **Shto skriptet e inicializimit**
5. Ngjitni përmbajtjen e plotë të skriptit në zonën e tekstit
6. Klikoni **Krijo pikëz**

### Hapi 3 - Shtoni rekordin DNS

Ndërsa niset Droplet, shtoni një **A rekord** në ofruesin tuaj DNS:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Hapi 4 - Monitoroni progresin

SSH në Droplet dhe shikoni regjistrin:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skripti printon IP-në e serverit tuaj afër fillimit — shtoni rekordin DNS sapo ta shihni.

### Hapi 5 - Hyni në aplikacion

Kur përfundon konfigurimi, regjistri tregon një përmbledhje:

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

> **Ndrysho fjalëkalimin** menjëherë pas hyrjes nëpërmjet **Cilësimeve** në menynë lart djathtas.

---

## Pas vendosjes

### Ndrysho një fjalëkalim

SSH në Droplet, modifikoni `.env` dhe rinisni kontejnerin e prekur:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Përditëso domenin

Nëse caktoni një domen tjetër pas vendosjes, përditësoni `PROJECT_URL` në `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Shiko të gjithë kontejnerët

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
