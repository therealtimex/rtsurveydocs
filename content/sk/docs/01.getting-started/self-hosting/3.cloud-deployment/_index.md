---
weight: 3
title: "Cloudové nasadenie"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Nasadenie rtCloud na hlavných poskytovateľoch cloudu pomocou automatizovaných skriptov pre DigitalOcean, AWS EC2, Google Cloud a Linode."
---

Repozitár nasadenia obsahuje automatizované skripty zriaďovania pre hlavných poskytovateľov cloudu. Každý skript beží pri prvom spustení čerstvého servera **Ubuntu 22.04 LTS** a vykonáva plne bezobslužné nastavenie:

- Inštaluje Docker a Docker Compose
- Generuje bezpečné náhodné heslá pre všetky interné služby
- Zapisuje `docker-compose.production.yml` a `.env`
- Konfiguruje Nginx ako reverzný proxy
- Získava bezplatný TLS certifikát od Let's Encrypt (automaticky opakuje pokus, kým sa DNS nevyrieši)
- Konfiguruje firewall UFW
- Voliteľne nasadí vstavaný server SSO Keycloak
- Vypisuje úplný súhrn nasadenia so všetkými prihlasovacími údajmi

Nastavenie sa dokončí za **5–10 minút** na štandardnej inštancii.

---

## Výber skriptu

Existuje viacero variantov skriptov v závislosti od vášho poskytovateľa cloudu a nastavenia SSO:

| Skript | Poskytovateľ | Režim SSO | Najvhodnejší pre |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Vstavaný Keycloak | Jednoduché, samostatné SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak alebo externý OIDC | Plná kontrola |
| `linode-stackscript-keycloak-embed.sh` | Linode | Vstavaný Keycloak | Nastavenie cez formulár, najjednoduchšie |
| `linode-stackscript-oidc.sh` | Linode | Iba externý OIDC | Existujúci poskytovateľ identity |
| `linode-stackscript.sh` | Linode | Keycloak alebo externý OIDC | Plná kontrola |
| `aws-ec2.sh` | AWS EC2 | Keycloak alebo externý OIDC | Nasadenia AWS |
| `gcp-compute.sh` | Google Cloud | Keycloak alebo externý OIDC | Nasadenia GCP |

> **Odporúčané pre väčšinu používateľov:** Použite variant `keycloak-embed`. Obsahuje vstavaný server identity Keycloak a vyžaduje najmenej konfiguračných polí.

---

## Sprievodca dimenzovaním servera

| Prípad použitia | RAM | Disk | Príklad |
|----------|-----|------|---------|
| Hodnotenie / vývoj | 2 GB | 25 GB | DO Basic $18/mes., t3.small, e2-small |
| Malý tím (< 50 používateľov) | 4 GB | 40 GB | DO Basic $24/mes., t3.medium, e2-medium |
| Produkcia (> 50 používateľov) | 8 GB | 80 GB | DO General $48/mes., t3.large, n2-standard-2 |

> Vstavaný Keycloak vyžaduje aspoň **4 GB RAM**. Používajte 2 GB iba na hodnotenie bez Keycloak.

---

## Nastavenie DNS

Všetky skripty vyžadujú doménu so **záznamom A smerujúcim na IP adresu vášho servera** predtým, ako Let's Encrypt môže vydať certifikát.

Skript vypíše IP adresu vášho servera na začiatku procesu nastavenia:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

Skript **automaticky opakuje pokus** Let's Encrypt každých 60 sekúnd až do 1 hodiny. Stačí pridať záznam DNS a počkať — nie je potrebné reštartovanie.

> **Limit frekvencie:** Let's Encrypt umožňuje maximum **5 certifikátov na doménu za 7 dní**. Vyhnite sa opakovanému nasadzovaniu a ničeniu serverov s rovnakou doménou. Ak dosiahnete limit, skript zobrazí časovú pečiatku `retry after` a okamžite sa zastaví.

---

## Kontrolný zoznam po nasadení

- [ ] Aplikácia sa otvára na `https://vaša-doména.com`
- [ ] Prihláste sa s `admin` a heslom, ktoré ste nakonfigurovali
- [ ] Všetky kontajnery sú zdravé: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Obnova Let's Encrypt funguje: `certbot renew --dry-run`
- [ ] Port MySQL 3306 **nie je** vystavený: `ufw status`
- [ ] Nastavte dennú zálohu databázy (pozrite si [Údržba](../maintenance))

---

## Riešenie problémov

### Skontrolujte úplný protokol nastavenia

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Limit frekvencie Let's Encrypt

Ak v protokole vidíte `too many certificates`, dosiahli ste limit 5 certifikátov/7 dní. Protokol zobrazuje presný čas opätovného pokusu:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Počkajte do tohto času, potom znova nasaďte.

### Keycloak zostáva nezdravý

Uistite sa, že server má aspoň 4 GB RAM, potom skontrolujte protokoly:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### Konfigurácia SSL sa neaplikuje po certbot

Ak bol certifikát vydaný, ale Nginx stále zobrazuje iba HTTP, skontrolujte riadok chyby v protokole a manuálne znova načítajte Nginx:

```bash
nginx -t && systemctl reload nginx
```
