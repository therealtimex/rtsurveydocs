---
weight: 3
title: "Debesies diegimas"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Diekite rtCloud pas pagrindinius debesijos teikėjus naudodami automatizuotus scenarijus „DigitalOcean", AWS EC2, „Google Cloud" ir Linode."
---

Diegimo saugykloje yra automatizuoti parengimo scenarijai pagrindiniams debesijos teikėjams. Kiekvienas scenarijus veikia pirmą kartą paleidžiant naują **Ubuntu 22.04 LTS** serverį ir atlieka visiškai neprižiūrimą sąranką:

- Įdiegiama „Docker" ir „Docker Compose"
- Sugeneruojami saugūs atsitiktiniai slaptažodžiai visoms vidinėms paslaugoms
- Parašomi `docker-compose.production.yml` ir `.env`
- Sukonfigūruotas Nginx kaip atvirkštinis tarpinis serveris
- Gaunamas nemokamas TLS sertifikatas iš „Let's Encrypt" (automatiškai kartojama, kol DNS išsprendžiama)
- Sukonfigūruotas UFW ugniasienė
- Neprivaloma – įdiegiamas integruotas Keycloak SSO serveris
- Išvedama pilna diegimo santrauka su visais prisijungimo duomenimis

Sąranka baigiama per **5–10 minučių** standartinėje instancijoje.

---

## Scenarijaus pasirinkimas

Yra kelios scenarijų variantes priklausomai nuo jūsų debesijos teikėjo ir SSO sąrankos:

| Scenarijus | Teikėjas | SSO režimas | Geriausiai tinka |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Integruotas Keycloak | Paprastas, savarankiškas SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak arba išorinis OIDC | Pilnas valdymas |
| `linode-stackscript-keycloak-embed.sh` | Linode | Integruotas Keycloak | Formos pagrindu, paprasčiausias |
| `linode-stackscript-oidc.sh` | Linode | Tik išorinis OIDC | Esamas tapatybės teikėjas |
| `linode-stackscript.sh` | Linode | Keycloak arba išorinis OIDC | Pilnas valdymas |
| `aws-ec2.sh` | AWS EC2 | Keycloak arba išorinis OIDC | AWS diegimai |
| `gcp-compute.sh` | Google Cloud | Keycloak arba išorinis OIDC | GCP diegimai |

> **Rekomenduojama daugumai naudotojų:** naudokite `keycloak-embed` variantą. Jame yra integruotas Keycloak tapatybės serveris ir reikia mažiausiai konfigūracijos laukų.

---

## Serverio dydžio vadovas

| Naudojimo atvejis | RAM | Diskas | Pavyzdys |
|----------|-----|------|---------|
| Vertinimas / kūrimas | 2 GB | 25 GB | DO Basic 18 USD/mėn., t3.small, e2-small |
| Maža komanda (< 50 naudotojų) | 4 GB | 40 GB | DO Basic 24 USD/mėn., t3.medium, e2-medium |
| Gamyba (> 50 naudotojų) | 8 GB | 80 GB | DO General 48 USD/mėn., t3.large, n2-standard-2 |

> Integruotam Keycloak reikia mažiausiai **4 GB RAM**. Naudokite 2 GB tik vertinimui be Keycloak.

---

## DNS sąranka

Visiems scenarijams reikalingas domenas su **A įrašu, nukreiptu į jūsų serverio IP**, prieš „Let's Encrypt" išduodant sertifikatą.

Scenarijus anksti sąrankos proceso metu išveda jūsų serverio IP:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

Scenarijus **automatiškai kartoja** „Let's Encrypt" bandymus kas 60 sekundžių iki 1 valandos. Tiesiog pridėkite DNS įrašą ir palaukite – paleidimo iš naujo nereikia.

> **Greičio ribojimas:** „Let's Encrypt" leidžia daugiausiai **5 sertifikatus vienam domenui per 7 dienas**. Venkite pakartotinai diegti ir naikinti serverius su tuo pačiu domenu. Pasiekus limitą, scenarijus parodys `retry after` laiko žymą ir iš karto sustabdys darbą.

---

## Diegimo po tikrinimo sąrašas

- [ ] Programa atidaroma adresu `https://your-domain.com`
- [ ] Prisijungta naudojant `admin` ir sukonfigūruotą slaptažodį
- [ ] Visi konteineriai sveiki: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] „Let's Encrypt" atnaujinimas veikia: `certbot renew --dry-run`
- [ ] MySQL prievadas 3306 **neatsidarytas**: `ufw status`
- [ ] Nustatykite kasdienę duomenų bazės atsarginę kopiją (žr. [Priežiūra](../maintenance))

---

## Trikčių šalinimas

### Patikrinkite pilną sąrankos žurnalą

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### „Let's Encrypt" greičio ribojimas

Jei žurnale matote `too many certificates`, pasiekėte 5 sertifikatų per 7 dienas limitą. Žurnale rodomas tikslus pakartojimo laikas:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Palaukite iki to laiko, tada vėl diekite.

### Keycloak lieka nesveika

Įsitikinkite, kad serveris turi mažiausiai 4 GB RAM, tada patikrinkite žurnalus:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL konfigūracija nepritaikyta po certbot

Jei sertifikatas buvo išduotas, bet Nginx vis tiek rodo tik HTTP, patikrinkite žurnalą dėl klaidos eilutės ir neautomatiniu būdu perkraukite Nginx:

```bash
nginx -t && systemctl reload nginx
```
