---
weight: 3
title: "Vendosja në Cloud"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Vendosni rtCloud te ofruesit kryesorë cloud me skripte të automatizuara për DigitalOcean, AWS EC2, Google Cloud dhe Linode."
---

Depozita e vendosjes përfshin skripte të automatizuara të aprovizionimit për ofruesit kryesorë cloud. Çdo skript ekzekutohet në nisjen e parë të një serveri të ri **Ubuntu 22.04 LTS** dhe kryen një konfigurim plotësisht pa mbikëqyrje:

- Instalimt Docker dhe Docker Compose
- Gjeneron fjalëkalime të rastësishme të sigurta për të gjitha shërbimet e brendshme
- Shkruan `docker-compose.production.yml` dhe `.env`
- Konfiguron Nginx si proxy të kundërt
- Merr një certifikatë TLS falas nga Let's Encrypt (riprovon automatikisht derisa DNS të zgjidhet)
- Konfiguron murin e zjarrit UFW
- Opsionalisht vendos serverin e integruar Keycloak SSO
- Nxjerr një përmbledhje të plotë vendosjeje me të gjitha kredencialet

Konfigurimi përfundon brenda **5–10 minutave** në një instancë standarde.

---

## Zgjedhja e një Skripti

Ka variante të shumta skripti varësisht nga ofruesi cloud dhe konfigurimi SSO:

| Skripti | Ofruesi | Mënyra SSO | Më i Mirë Për |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Keycloak i integruar | SSO i thjeshtë, i vetë-mjaftueshëm |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak ose OIDC i jashtëm | Kontroll i plotë |
| `linode-stackscript-keycloak-embed.sh` | Linode | Keycloak i integruar | Konfigurim bazuar në formular, më i thjeshtë |
| `linode-stackscript-oidc.sh` | Linode | Vetëm OIDC i jashtëm | Ofrues ekzistues identiteti |
| `linode-stackscript.sh` | Linode | Keycloak ose OIDC i jashtëm | Kontroll i plotë |
| `aws-ec2.sh` | AWS EC2 | Keycloak ose OIDC i jashtëm | Vendosjet AWS |
| `gcp-compute.sh` | Google Cloud | Keycloak ose OIDC i jashtëm | Vendosjet GCP |

> **I rekomanduar për shumicën e përdoruesve:** Përdorni variantin `keycloak-embed`. Përfshin një server të integruar identiteti Keycloak dhe kërkon fushat më të pakëta të konfigurimit.

---

## Udhëzuesi i Madhësisë së Serverit

| Rasti i Përdorimit | RAM | Disku | Shembull |
|----------|-----|------|---------|
| Vlerësim / zhvillim | 2 GB | 25 GB | DO Basic $18/muaj, t3.small, e2-small |
| Ekip i vogël (< 50 përdorues) | 4 GB | 40 GB | DO Basic $24/muaj, t3.medium, e2-medium |
| Prodhim (> 50 përdorues) | 8 GB | 80 GB | DO General $48/muaj, t3.large, n2-standard-2 |

> Keycloak i integruar kërkon të paktën **4 GB RAM**. Përdorni 2 GB vetëm për vlerësim pa Keycloak.

---

## Konfigurimi DNS

Të gjitha skriptet kërkojnë një domen me një **rekord A që tregon IP-në e serverit tuaj** para se Let's Encrypt të mund të lëshojë një certifikatë.

Skripti printon IP-në e serverit tuaj herët në procesin e konfigurimit:

```
============================================================
 IP e Serverit : 139.162.51.85
 Shtoni tani këtë rekord DNS A nëse nuk e keni bërë ende:
   myapp.example.com  ->  139.162.51.85
 Skripti do të riprovojë Certbot çdo 60 sekonda derisa DNS të zgjidhet.
============================================================
```

Skripti **riprovohet automatikisht** Let's Encrypt çdo 60 sekonda për deri në 1 orë. Thjesht shtoni rekordin DNS dhe prisni — nuk nevojitet rinis.

> **Kufiri i shkallës:** Let's Encrypt lejon maksimalisht **5 certifikata për domen në 7 ditë**. Shmangni vendosjen dhe shkatërrimin e serverëve vazhdimisht me të njëjtin domen. Nëse arrini kufirin, skripti do të shfaqë një shenjë kohore `riprovo pas` dhe do të ndalojë menjëherë.

---

## Lista e Kontrollit Pas Vendosjes

- [ ] Aplikacioni hapet te `https://domeni-juaj.com`
- [ ] Hyni me `admin` dhe fjalëkalimin që konfiguruat
- [ ] Të gjithë kontejnerët janë të shëndetshëm: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Rinovimi i Let's Encrypt funksionon: `certbot renew --dry-run`
- [ ] Porta MySQL 3306 **nuk** është e ekspozuar: `ufw status`
- [ ] Konfiguroni një rezervim ditor të bazës së të dhënave (shikoni [Mirëmbajtja](../maintenance))

---

## Zgjidhja e Problemeve

### Kontrolloni regjistrin e plotë të konfigurimit

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Kufiri i shkallës Let's Encrypt

Nëse shihni `shumë certifikata` në regjistër, keni arritur kufirin prej 5 certifikatash / 7 ditë. Regjistri tregon kohën e saktë të riprovimit:

```
[SSL] GABIM: Arritur kufiri i shkallës Let's Encrypt. riprovo pas 2026-03-15 16:22 UTC.
```

Prisni deri në atë kohë, pastaj ri-vendosni.

### Keycloak mbetet jo i shëndetshëm

Sigurohuni që serveri ka të paktën 4 GB RAM, pastaj kontrolloni regjistrat:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### Konfigurimi SSL nuk aplikohet pas certbot

Nëse certifikata u lëshua por Nginx ende tregon vetëm HTTP, kontrolloni regjistrin për rreshtin e gabimit dhe ringarkoni Nginx manualisht:

```bash
nginx -t && systemctl reload nginx
```
