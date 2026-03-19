---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuer rtCloud på Linode med StackScripts og et skjemabasert konfigurasjonsgrensesnitt."
---

Linode bruker **StackScripts** — skript med et skjemabasert grensesnitt der du fyller inn konfigurasjonsfelt direkte i Linode Manager uten å redigere kode.

> Linode StackScripts er den enkleste distribusjonsmetoden. Feltene vises som et skjema når du oppretter en Linode — ingen skriptredigering kreves.

---

## Innebygd Keycloak (anbefalt)

### Trinn 1 — Finn StackScript-en

StackScript-en er offentlig tilgjengelig i Linode-fellesskapet — ingen manuelt oppsett nødvendig:

1. Gå til **Linodes** → **Opprett Linode**
2. Under **Velg en distribusjon**, velg **StackScripts** → **Community StackScripts**
3. Søk etter **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Velg den og fyll inn konfigurasjonsskjemaet:

> Alternativt kan du [laste ned skriptet](/scripts/linode-stackscript-keycloak-embed.sh) og opprette din egen StackScript under **StackScripts** → **Opprett StackScript**.

| Felt | Påkrevd | Beskrivelse |
|-------|----------|-------------|
| Prosjekt-ID | Nei | Unik identifikator (standard: `rtsurvey`). Brukes som databasenavn og Keycloak klient-ID. |
| Keycloak Admin-passord | Nei | Passord for både Keycloak admin-konsoll og app-admininnlogging. Standard er `admin` — **endre etter første innlogging**. |
| Domene | Ja | Domenenavnet ditt. DNS A-post må peke til denne Linode-IP-en. Kreves for HTTPS og Keycloak. |
| Let's Encrypt e-post | Ja | E-post for Let's Encrypt-sertifikatvarsler. |
| Docker-bildetag | Nei | Bilde som skal distribueres (standard: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Sikkerhet:** Alle passord er standard `admin`. Endre dem umiddelbart etter første innlogging.

5. Velg **Ubuntu 22.04 LTS** som bilde
6. Velg plan **Shared CPU 4 GB** eller større
7. Klikk **Opprett Linode**

### Trinn 2 — Legg til DNS-posten

Mens Linode-en starter opp, legg til en **A-post** hos DNS-leverandøren din:

```
Type  : A
Navn  : myapp          (eller @ for rotdomene)
Verdi : <linode-ip>
TTL   : 300
```

### Trinn 3 — Overvåk fremdriften

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Skriptet skriver ut server-IP-en i begynnelsen — legg til DNS-posten så snart du ser den.

### Trinn 4 — Åpne appen

Når oppsettet er ferdig, viser loggen et sammendrag:

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

Logg inn med brukernavn `admin` og passord `admin`, og endre passordet umiddelbart.

---

## Etter distribusjon

### Endre et passord

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Se alle containere

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Sjekk loggen

```bash
tail -200 /var/log/stackscript.log
```
