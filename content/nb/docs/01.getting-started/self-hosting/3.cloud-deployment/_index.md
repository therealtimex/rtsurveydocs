---
weight: 3
title: "Skydistribusjon"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Distribuer rtCloud til store skyleverandører med automatiserte skript for DigitalOcean, AWS EC2, Google Cloud og Linode."
---

Distribusjonslageret inkluderer automatiserte klargjøringsskript for store skyleverandører. Hvert skript kjøres ved første oppstart av en fersk **Ubuntu 22.04 LTS**-server og utfører et fullstendig uovervåket oppsett:

- Installerer Docker og Docker Compose
- Genererer sikre tilfeldige passord for alle interne tjenester
- Skriver `docker-compose.production.yml` og `.env`
- Konfigurerer Nginx som omvendt proxy
- Skaffer et gratis TLS-sertifikat fra Let's Encrypt (prøver automatisk på nytt til DNS løses)
- Konfigurerer UFW-brannmuren
- Distribuerer valgfritt den innebygde Keycloak SSO-serveren
- Viser et fullstendig distribusjonssammendrag med alle legitimasjonsopplysninger

Oppsettet fullføres på **5–10 minutter** på en standard instans.

---

## Velge et skript

Det finnes flere skriptvarianter avhengig av skyleverandør og SSO-oppsett:

| Skript | Leverandør | SSO-modus | Best for |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Innebygd Keycloak | Enkelt, selvstendig SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak eller ekstern OIDC | Full kontroll |
| `linode-stackscript-keycloak-embed.sh` | Linode | Innebygd Keycloak | Skjemabasert oppsett, enklest |
| `linode-stackscript-oidc.sh` | Linode | Kun ekstern OIDC | Eksisterende identitetsleverandør |
| `linode-stackscript.sh` | Linode | Keycloak eller ekstern OIDC | Full kontroll |
| `aws-ec2.sh` | AWS EC2 | Keycloak eller ekstern OIDC | AWS-distribusjoner |
| `gcp-compute.sh` | Google Cloud | Keycloak eller ekstern OIDC | GCP-distribusjoner |

> **Anbefalt for de fleste brukere:** Bruk `keycloak-embed`-varianten. Den inkluderer en innebygd Keycloak-identitetsserver og krever færrest konfigurasjonsfelt.

---

## Veiledning for serverstørrelse

| Brukstilfelle | RAM | Disk | Eksempel |
|----------|-----|------|---------|
| Evaluering / utvikling | 2 GB | 25 GB | DO Basic $18/md, t3.small, e2-small |
| Lite team (< 50 brukere) | 4 GB | 40 GB | DO Basic $24/md, t3.medium, e2-medium |
| Produksjon (> 50 brukere) | 8 GB | 80 GB | DO General $48/md, t3.large, n2-standard-2 |

> Innebygd Keycloak krever minst **4 GB RAM**. Bruk 2 GB kun for evaluering uten Keycloak.

---

## DNS-oppsett

Alle skript krever et domene med en **A-post som peker til serverens IP** før Let's Encrypt kan utstede et sertifikat.

Skriptet skriver ut server-IP-en tidlig i oppsettsprosessen:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

Skriptet **prøver automatisk på nytt** mot Let's Encrypt hvert 60. sekund i opptil 1 time. Bare legg til DNS-posten og vent — ingen omstart nødvendig.

> **Hastighetsbegrensning:** Let's Encrypt tillater maksimalt **5 sertifikater per domene per 7 dager**. Unngå å distribuere og slette servere gjentatte ganger med samme domene. Hvis du treffer grensen, viser skriptet et `retry after`-tidsstempel og stopper umiddelbart.

---

## Sjekkliste etter distribusjon

- [ ] Appen åpner på `https://ditt-domene.com`
- [ ] Logg inn med `admin` og passordet du konfigurerte
- [ ] Alle containere er sunne: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt-fornyelse fungerer: `certbot renew --dry-run`
- [ ] MySQL-port 3306 er **ikke** eksponert: `ufw status`
- [ ] Sett opp daglig sikkerhetskopiering av databasen (se [Vedlikehold](../maintenance))

---

## Feilsøking

### Sjekk den fullstendige oppsettsloggen

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt hastighetsbegrensning

Hvis du ser `too many certificates` i loggen, har du nådd grensen på 5 sertifikater/7 dager. Loggen viser nøyaktig prøvetid:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Vent til det tidspunktet, og distribuer på nytt.

### Keycloak forblir usunn

Kontroller at serveren har minst 4 GB RAM, og sjekk deretter loggene:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL-konfigurasjon ikke brukt etter certbot

Hvis sertifikatet ble utstedt men Nginx fortsatt viser kun HTTP, sjekk loggen for feillinjen og last inn Nginx på nytt manuelt:

```bash
nginx -t && systemctl reload nginx
```
