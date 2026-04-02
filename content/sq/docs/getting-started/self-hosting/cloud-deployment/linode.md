---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Vendosni rtCloud në Linode duke përdorur një StackScript. Nuk nevojitet konfigurim - thjesht krijoni serverin dhe ndiqni hapat pas vendosjes."
---

## Hapi 1 - Nisni StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Kjo hap faqen StackScript në Linode Cloud Manager. Klikoni **Deploy New Linode**.

---

## Hapi 2 - Plotësoni formularin e Linode

Plotësoni formularin standard të krijimit të serverit Linode:

| Fusha | Vlera e rekomanduar |
|-------|------------------|
| **Imazhi** | Ubuntu 22.04 LTS |
| **Rajoni ** | Më afër përdoruesve tuaj |
| **Plani ** | CPU e përbashkët 4 GB ose më e madhe |
| **Fjalëkalimi rrënjë** | Vendosni një fjalëkalim të fortë |
| **Zona kohore** *(fusha jonë e vetme)* | Zona kohore e serverit tuaj (e parazgjedhur: `Asia/Ho_Chi_Minh`) |

Klikoni **Krijo Linode** kur të keni mbaruar.

---

## Hapi 3 - Prisni që konfigurimi të përfundojë

Skripti funksionon automatikisht në nisjen e parë. Ai instalon Docker, tërheq imazhin rtSurvey, inicializon bazën e të dhënave dhe nis të gjitha shërbimet. Kjo zgjat **5–10 minuta**.

Mund të shikoni progresin drejtpërdrejt në **Linode Cloud Manager** — nuk kërkohet SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klikoni në Linode tuaj të sapokrijuar
3. Klikoni **Launch LISH Console** (lart djathtas i faqes së detajeve Linode)

Hapet një terminal shfletuesi që tregon regjistrin e drejtpërdrejtë të nisjes - skeda **Weblish** funksionon drejtpërdrejt në shfletuesin tuaj, nuk nevojitet klient SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Prisni derisa të shihni:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Regjistri gjithashtu tregon IP-në e serverit tuaj - do t'ju duhet për hapin tjetër.

---

## Hapi 4 - Konfiguro SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Ndiqni **[Konfiguro udhëzuesin SSL →](../ssl-setup)** për të konfiguruar HTTPS. Nëndomeni falas **rtsurvey.com** është opsioni më i shpejtë – nuk nevojitet konfigurim DNS.

---

## Hapi 5 - Hyrja e parë

Pasi SSL të jetë aktiv, ndiqni **[Udhëzuesin e hyrjes së parë →](../first-login)** për të hyrë në llogarinë e administratorit.

---

## Hapi 6 - Ndryshoni fjalëkalimin e paracaktuar

Të gjitha fjalëkalimet e paracaktuara janë "admin". Ndryshoni ato menjëherë pas hyrjes tuaj të parë:

- **Fjalëkalimi i administratorit të aplikacionit** — cilësimet e llogarisë brenda aplikacionit
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Rregullat e Firewall-it (Linode Cloud Firewall)

Nëse bashkëngjitni një Linode Cloud Firewall në këtë server, përdorni rregullat e mëposhtme:

### Inbound

| Label | Action | Protocol | Port | Sources | Notes |
|-------|--------|----------|------|---------|-------|
| `pranoj-inbound-ssh` | Prano | TCP | 22 | Të gjitha IPv4, Të gjitha IPv6 | Qasja SSH |
| "pranoj-përbrenda-http" | Prano | TCP | 80 | Të gjitha IPv4, Të gjitha IPv6 | Nginx (Sfida HTTP + ACME) |
| "pranoj-përbrenda-https" | Prano | TCP | 443 | Të gjitha IPv4, Të gjitha IPv6 | Nginx (HTTPS pas konfigurimit SSL) |
| `pranoj-përbrenda-shkëlqim` | Prano | TCP | 3838 | Të gjitha IPv4, Të gjitha IPv6 | Serveri i ndritshëm (analitika R) |
| "pranoj-inbound-icmp" | Prano | ICMP | — | Të gjitha IPv4, Të gjitha IPv6 | Ping / diagnostikim |
| Default inbound policy | **Drop** | | | | Blloko gjithçka tjetër |

### Jashtë

| Label | Veprimi | Shënime |
|-------|--------|-------|
| Politika e parazgjedhur e daljes | **Prano ** | Lejo të gjitha jashtë (Docker pulls, certbot, GoDaddy API, etj.) |

### Portet NUK nevojiten nga jashtë

Këto porte janë të lidhura vetëm me "127.0.0.1" dhe nuk mund të arrihen kurrë nga jashtë serverit:

| Port | Shërbimi | Arsyeja |
|------|---------|--------|
| 8080 | Kontejneri i aplikacionit | Nginx proxies për të brenda |
| 8090 | Enë me mantel | Nginx proxies për të brenda |
| 3306 | MySQL | Internal Docker network only |

---

## Zgjidhja e problemeve

### Kontrollo regjistrin e konfigurimit

```bash
tail -200 /var/log/stackscript.log
```

### Kontrollo regjistrin SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Shiko statusin e kontejnerit

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
