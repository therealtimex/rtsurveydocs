---
weight: 3
title: "Primena u oblaku"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Primenite rtCloud kod glavnih pružalaca oblaka uz automatizovane skripte za DigitalOcean, AWS EC2, Google Cloud i Linode."
---

Repozitorijum za primenu uključuje automatizovane skripte za obezbeđivanje za glavne pružaoce oblaka. Svaka skripta se izvršava pri prvom pokretanju novog **Ubuntu 22.04 LTS** servera i vrši potpuno automatizovano podešavanje:

- Instalira Docker i Docker Compose
- Generiše sigurne nasumične lozinke za sve interne servise
- Piše `docker-compose.production.yml` i `.env`
- Konfiguriše Nginx kao reverzni proksi
- Pribavlja besplatni TLS sertifikat od Let's Encrypt (automatski ponavljanje dok DNS ne bude razrešen)
- Konfiguriše UFW firewall
- Opciono primenjuje ugrađeni Keycloak SSO server
- Ispisuje kompletan rezime primene sa svim akreditivima

Podešavanje se završava za **5–10 minuta** na standardnoj instanci.

---

## Izbor skripte

Postoji više varijanti skripti u zavisnosti od vašeg pružaoca oblaka i SSO podešavanja:

| Skripta | Pružalac | SSO režim | Najpogodnije za |
|---------|----------|-----------|-----------------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Ugrađeni Keycloak | Jednostavan, samoobuhvatan SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak ili spoljni OIDC | Potpuna kontrola |
| `linode-stackscript-keycloak-embed.sh` | Linode | Ugrađeni Keycloak | Podešavanje putem forme, najjednostavnije |
| `linode-stackscript-oidc.sh` | Linode | Samo spoljni OIDC | Postojeći pružalac identiteta |
| `linode-stackscript.sh` | Linode | Keycloak ili spoljni OIDC | Potpuna kontrola |
| `aws-ec2.sh` | AWS EC2 | Keycloak ili spoljni OIDC | AWS primene |
| `gcp-compute.sh` | Google Cloud | Keycloak ili spoljni OIDC | GCP primene |

> **Preporučeno za većinu korisnika:** Koristite `keycloak-embed` varijantu. Uključuje ugrađeni Keycloak server za identitet i zahteva najmanje konfiguracijskih polja.

---

## Vodič za dimenzionisanje servera

| Slučaj upotrebe | RAM | Disk | Primer |
|-----------------|-----|------|--------|
| Procena / razvoj | 2 GB | 25 GB | DO Basic 18$/mes., t3.small, e2-small |
| Mala ekipa (< 50 korisnika) | 4 GB | 40 GB | DO Basic 24$/mes., t3.medium, e2-medium |
| Produkcija (> 50 korisnika) | 8 GB | 80 GB | DO General 48$/mes., t3.large, n2-standard-2 |

> Ugrađeni Keycloak zahteva najmanje **4 GB RAM**. Koristite 2 GB samo za procenu bez Keycloak-a.

---

## Podešavanje DNS-a

Sve skripte zahtevaju domen sa **A zapisom koji pokazuje na IP vašeg servera** pre nego što Let's Encrypt može da izda sertifikat.

Skripta ispisuje IP vašeg servera rano u toku procesa podešavanja:

```
============================================================
 Server IP : 139.162.51.85
 Dodajte ovaj DNS A zapis sada ako već niste:
   myapp.example.com  ->  139.162.51.85
 Skripta će ponavljati Certbot svakih 60s dok DNS ne bude razrešen.
============================================================
```

Skripta **automatski ponavlja** Let's Encrypt na svakih 60 sekundi do 1 sat. Samo dodajte DNS zapis i sačekajte — nije potrebno ponovo pokretanje.

> **Ograničenje brzine:** Let's Encrypt dozvoljava maksimalno **5 sertifikata po domenu na 7 dana**. Izbegavajte višestruko postavljanje i uklanjanje servera sa istim domenom. Ako dostignete ograničenje, skripta će prikazati vremensku oznaku `retry after` i odmah se zaustaviti.

---

## Lista provera nakon primene

- [ ] Aplikacija se otvara na `https://your-domain.com`
- [ ] Prijavite se sa `admin` i lozinkom koju ste konfigurisali
- [ ] Svi kontejneri su zdravi: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Obnavljanje Let's Encrypt radi: `certbot renew --dry-run`
- [ ] MySQL port 3306 **nije** izložen: `ufw status`
- [ ] Podesite dnevne rezervne kopije baze podataka (pogledajte [Održavanje](../maintenance))

---

## Rešavanje problema

### Proverite kompletan evidencioni fajl podešavanja

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Ograničenje brzine Let's Encrypt

Ako vidite `too many certificates` u evidenciji, dostigli ste ograničenje od 5 sertifikata/7 dana. Evidencija prikazuje tačno vreme ponovnog pokušaja:

```
[SSL] GREŠKA: Dostiglo ograničenje brzine Let's Encrypt. ponovite posle 2026-03-15 16:22 UTC.
```

Sačekajte do tog vremena, zatim ponovo primenite.

### Keycloak ostaje nezdrav

Proverite da server ima najmanje 4 GB RAM, zatim proverite evidencije:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL konfiguracija nije primenjena nakon certbot-a

Ako je sertifikat izdat ali Nginx i dalje prikazuje samo HTTP, proverite evidencijski fajl za liniju greške i ručno ponovo učitajte Nginx:

```bash
nginx -t && systemctl reload nginx
```
