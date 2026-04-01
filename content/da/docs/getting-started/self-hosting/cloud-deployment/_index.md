---
weight: 3
title: "Cloud-implementering"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Implementér rtCloud hos større cloud-udbydere med automatiserede scripts til DigitalOcean, AWS EC2, Google Cloud og Linode."
---

Implementeringslageret indeholder automatiserede provisioneringsscripts til større cloud-udbydere. Hvert script kører ved første opstart af en ny **Ubuntu 22.04 LTS**-server og udfører en fuldt automatiseret opsætning:

- Installerer Docker og Docker Compose
- Genererer sikre tilfældige adgangskoder til alle interne tjenester
- Skriver `docker-compose.production.yml` og `.env`
- Konfigurerer Nginx som en omvendt proxy
- Henter et gratis TLS-certifikat fra Let's Encrypt (prøver automatisk igen, til DNS er løst)
- Konfigurerer UFW-firewallen
- Implementerer valgfrit den indlejrede Keycloak SSO-server
- Udskriver en komplet implementeringsoversigt med alle legitimationsoplysninger

Opsætningen afsluttes på **5–10 minutter** på en standardinstans.

---

## Valg af script

Der er flere scriptvarianter afhængigt af din cloud-udbyder og SSO-opsætning:

| Script | Udbyder | SSO-tilstand | Bedst til |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Indbygget Keycloak | Simpelt, selvstændigt SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak eller ekstern OIDC | Fuld kontrol |
| `linode-stackscript-keycloak-embed.sh` | Linode | Indbygget Keycloak | Formularbaseret opsætning, enklest |
| `linode-stackscript-oidc.sh` | Linode | Kun ekstern OIDC | Eksisterende identitetsudbyder |
| `linode-stackscript.sh` | Linode | Keycloak eller ekstern OIDC | Fuld kontrol |
| `aws-ec2.sh` | AWS EC2 | Keycloak eller ekstern OIDC | AWS-implementeringer |
| `gcp-compute.sh` | Google Cloud | Keycloak eller ekstern OIDC | GCP-implementeringer |

> **Anbefalet til de fleste brugere:** Brug varianten `keycloak-embed`. Den inkluderer en indbygget Keycloak-identitetsserver og kræver færrest konfigurationsfelter.

---

## Vejledning til serverstørrelse

| Anvendelsestilfælde | RAM | Disk | Eksempel |
|----------|-----|------|---------|
| Evaluering / udvikling | 2 GB | 25 GB | DO Basic $18/md., t3.small, e2-small |
| Lille team (< 50 brugere) | 4 GB | 40 GB | DO Basic $24/md., t3.medium, e2-medium |
| Produktion (> 50 brugere) | 8 GB | 80 GB | DO General $48/md., t3.large, n2-standard-2 |

> Indlejret Keycloak kræver mindst **4 GB RAM**. Brug kun 2 GB til evaluering uden Keycloak.

---

## DNS-opsætning

Alle scripts kræver et domæne med en **A-post, der peger på din servers IP**, inden Let's Encrypt kan udstede et certifikat.

Scriptet udskriver din servers IP tidligt i opsætningsprocessen:

```
============================================================
 Server IP : 139.162.51.85
 Tilføj denne DNS A-post nu, hvis du ikke allerede har:
   myapp.example.com  ->  139.162.51.85
 Scriptet prøver Certbot igen hvert 60. sekund, til DNS er løst.
============================================================
```

Scriptet **prøver automatisk igen** Let's Encrypt hvert 60. sekund i op til 1 time. Tilføj blot DNS-posten og vent – ingen genstart nødvendig.

> **Hastighedsbegrænsning:** Let's Encrypt tillader maksimalt **5 certifikater pr. domæne pr. 7 dage**. Undgå at implementere og ødelægge servere gentagne gange med det samme domæne. Hvis du rammer grænsen, viser scriptet et tidsstempel for `prøv igen` og stopper øjeblikkeligt.

---

## Tjekliste efter implementering

- [ ] App åbner på `https://dit-domæne.com`
- [ ] Log ind med `admin` og den adgangskode, du konfigurerede
- [ ] Alle containere er sunde: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt-fornyelse virker: `certbot renew --dry-run`
- [ ] MySQL-port 3306 er **ikke** eksponeret: `ufw status`
- [ ] Opsæt en daglig database-sikkerhedskopi (se [Vedligeholdelse](../maintenance))

---

## Fejlfinding

### Kontrollér den fulde opsætningslog

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt-hastighedsbegrænsning

Hvis du ser `too many certificates` i loggen, har du ramt grænsen på 5 certifikater/7 dage. Loggen viser den præcise tid for næste forsøg:

```
[SSL] FEJL: Let's Encrypt-hastighedsbegrænsning ramt. prøv igen efter 2026-03-15 16:22 UTC.
```

Vent til det tidspunkt, og implementér derefter igen.

### Keycloak forbliver usund

Sørg for, at serveren har mindst 4 GB RAM, og kontrollér derefter logs:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL-konfiguration ikke anvendt efter certbot

Hvis certifikatet blev udstedt, men Nginx stadig viser kun HTTP, kontrollér loggen for fejllinjen og genindlæs Nginx manuelt:

```bash
nginx -t && systemctl reload nginx
```
