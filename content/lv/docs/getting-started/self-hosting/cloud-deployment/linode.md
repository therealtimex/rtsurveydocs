---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Izvietojiet rtCloud uz Linode, izmantojot StackScripts ar formu bāzētu konfigurācijas UI."
---

Linode izmanto **StackScripts** — skriptus ar formu bāzētu UI, kur konfigurācijas laukus aizpildāt tieši Linode pārvaldniekā, nerediģējot kodu.

> Linode StackScripts ir vienkāršākā izvietošanas metode. Lauki parādās kā forma, veidojot Linode — skripta rediģēšana nav nepieciešama.

---

## Iebūvētais Keycloak (Ieteicams)

### 1. solis — Atrodiet StackScript

StackScript ir publiski pieejams Linode kopienā — manuāla iestatīšana nav nepieciešama:

1. Dodieties uz **Linodes** → **Create Linode**
2. Sadaļā **Choose a Distribution** atlasiet **StackScripts** → **Community StackScripts**
3. Meklējiet **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Atlasiet to un aizpildiet konfigurācijas formu:

> Alternatīvi, [lejupielādējiet skriptu](/scripts/linode-stackscript-keycloak-embed.sh) un izveidojiet savu StackScript sadaļā **StackScripts** → **Create StackScript**.

| Lauks | Obligāts | Apraksts |
|-------|----------|-------------|
| Projekta ID | Nē | Unikāls identifikators (noklusējums: `rtsurvey`). Izmanto kā datu bāzes nosaukumu un Keycloak klienta ID. |
| Keycloak administratora parole | Nē | Parole Keycloak administratora konsolei un lietotnes administratora pieteikšanāi. Noklusējums ir `admin` — **mainiet pēc pirmās pieteikšanās**. |
| Domēns | Jā | Jūsu domēna nosaukums. DNS A ierakstam jānorāda uz šī Linode IP. Nepieciešams HTTPS un Keycloak. |
| Let's Encrypt e-pasts | Jā | E-pasts Let's Encrypt sertifikātu paziņojumiem. |
| Docker attēla tags | Nē | Attēls izvietošanai (noklusējums: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Drošība:** Visas paroles pēc noklusējuma ir `admin`. Mainiet tās nekavējoties pēc pirmās pieteikšanās.

5. Atlasiet **Ubuntu 22.04 LTS** kā attēlu
6. Atlasiet **Shared CPU 4 GB** plānu vai lielāku
7. Noklikšķiniet uz **Create Linode**

### 2. solis — Pievienojiet DNS ierakstu

Kamēr Linode sāknējas, pievienojiet **A ierakstu** sava DNS nodrošinātāja panelī:

```
Tips  : A
Nosaukums  : myapp          (vai @ saknes domēnam)
Vērtība : <linode-ip>
TTL   : 300
```

### 3. solis — Uzraugiet progresu

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Skripts drīz pēc sākuma izdrukā jūsu servera IP — pievienojiet DNS ierakstu, tiklīdz to redzat.

### 4. solis — Piekļūstiet lietotnei

Kad iestatīšana ir pabeigta, žurnāls rāda kopsavilkumu:

```
============================================================
 rtCloud izvietošana pabeigta! (Iebūvētais Keycloak)
============================================================
 Lietotnes URL   : https://myapp.example.com
 Administrators     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! DROŠĪBA: Visas paroles pēc noklusējuma ir 'admin'.
    Mainiet tās nekavējoties pēc pirmās pieteikšanās.
============================================================
```

Piesakieties ar lietotājvārdu `admin` un paroli `admin`, pēc tam nekavējoties mainiet savu paroli.

---

## Pēc izvietošanas

### Paroles maiņa

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visu konteineru skatīšana

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Žurnāla pārbaude

```bash
tail -200 /var/log/stackscript.log
```
