---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Vendosni rtCloud në Linode duke përdorur StackScripts me një UI konfigurimi bazuar në formular."
---

Linode përdor **StackScripts** — skripte me UI bazuar në formular ku plotësoni fushat e konfigurimit direkt në Linode Manager pa edituar asnjë kod.

> StackScripts të Linode janë metoda më e lehtë e vendosjes. Fushat shfaqen si formular kur krijoni një Linode — nuk kërkohet editim i skriptit.

---

## Keycloak i Integruar (I Rekomanduar)

### Hapi 1 — Gjeni StackScript-in

StackScript-i është i disponueshëm publikisht në komunitetin Linode — nuk nevojitet konfigurim manual:

1. Shkoni te **Linodes** → **Krijo Linode**
2. Nën **Zgjidhni një Shpërndarje**, zgjidhni **StackScripts** → **StackScripts Komuniteti**
3. Kërkoni **`RTA rtSurvey - Vetjake me Keycloak SSO`**
4. Zgjidheni dhe plotësoni formularin e konfigurimit:

> Përndryshe, [shkarkoni skriptin](/scripts/linode-stackscript-keycloak-embed.sh) dhe krijoni StackScript-in tuaj nën **StackScripts** → **Krijo StackScript**.

| Fusha | E detyrueshme | Përshkrimi |
|-------|----------|-------------|
| ID Projekti | Jo | Identifikues unik (parazgjedhja: `rtsurvey`). Përdoret si emri i bazës së të dhënave dhe ID klientit Keycloak. |
| Fjalëkalimi Admin Keycloak | Jo | Fjalëkalimi për konsolën administrative Keycloak dhe hyrjen e adminit të aplikacionit. Parazgjedhja `admin` — **ndryshojeni pas hyrjes së parë**. |
| Domeni | Po | Emri i domenit tuaj. Rekord DNS A duhet të tregojë IP-në e këtij Linode. Kërkohet për HTTPS dhe Keycloak. |
| Email Let's Encrypt | Po | Email për njoftimet e certifikatave Let's Encrypt. |
| Etiketa e Imazhit Docker | Jo | Imazhi për të vendosur (parazgjedhja: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Siguria:** Të gjitha fjalëkalimet parazgjidhen me `admin`. Ndryshojini menjëherë pas hyrjes suaj të parë.

5. Zgjidhni **Ubuntu 22.04 LTS** si imazhin
6. Zgjidhni planin **Shared CPU 4 GB** ose më të madh
7. Klikoni **Krijo Linode**

### Hapi 2 — Shtoni rekordin DNS

Ndërkohë që Linode-i po niset, shtoni një **rekord A** te ofruesi juaj DNS:

```
Tipi  : A
Emri  : myapp          (ose @ për domenin rrënjë)
Vlera : <linode-ip>
TTL   : 300
```

### Hapi 3 — Monitoroni progresin

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Skripti printon IP-në e serverit tuaj afër fillimit — shtoni rekordin DNS sapo ta shihni.

### Hapi 4 — Aksesoni aplikacionin

Kur konfigurimi përfundon, regjistri tregon një përmbledhje:

```
============================================================
 Vendosja rtCloud u kompletua! (Keycloak i Integruar)
============================================================
 URL Aplikacioni   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SIGURIA: Të gjitha fjalëkalimet parazgjidhen me 'admin'.
    Ndryshojini menjëherë pas hyrjes së parë.
============================================================
```

Hyni me emrin e përdoruesit `admin` dhe fjalëkalimin `admin`, pastaj ndryshoni fjalëkalimin menjëherë.

---

## Pas Vendosjes

### Ndryshoni një fjalëkalim

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Shikoni të gjithë kontejnerët

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Kontrolloni regjistrin

```bash
tail -200 /var/log/stackscript.log
```
