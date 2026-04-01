---
weight: 3
title: "Pilvikäyttöönotto"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Ota rtCloud käyttöön suurimmilla pilvipalveluntarjoajilla automaattisten skriptien avulla DigitalOceanille, AWS EC2:lle, Google Cloudille ja Linodelle."
---

Käyttöönottovarasto sisältää automaattiset provisiointiskriptit suurimmille pilvipalveluntarjoajille. Jokainen skripti ajetaan uuden **Ubuntu 22.04 LTS** -palvelimen ensimmäisellä käynnistyksellä ja suorittaa täysin ilman valvontaa tapahtuvan asennuksen:

- Asentaa Dockerin ja Docker Composen
- Luo satunnaiset salasanat kaikille sisäisille palveluille
- Kirjoittaa `docker-compose.production.yml`:n ja `.env`:n
- Konfiguroi Nginxin käänteiseksi välityspalvelimeksi
- Hankkii ilmaisen TLS-sertifikaatin Let's Encryptiltä (yrittää automaattisesti uudelleen, kunnes DNS ratkeaa)
- Konfiguroi UFW-palomuurin
- Ottaa valinnaisesti käyttöön upotetun Keycloak SSO -palvelimen
- Tulostaa täydellisen käyttöönoton yhteenvedon kaikkine tunnistetietoineen

Asennus valmistuu **5–10 minuutissa** standardiinstanssilla.

---

## Skriptin valitseminen

Käytettävissä on useita skriptivariaaatteja pilvipalveluntarjoajasi ja SSO-asetusten mukaan:

| Skripti | Tarjoaja | SSO-tila | Sopii parhaiten |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Sisäänrakennettu Keycloak | Yksinkertainen, itsenäinen SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak tai ulkoinen OIDC | Täysi hallinta |
| `linode-stackscript-keycloak-embed.sh` | Linode | Sisäänrakennettu Keycloak | Lomakepohjainen asennus, yksinkertaisin |
| `linode-stackscript-oidc.sh` | Linode | Vain ulkoinen OIDC | Olemassa oleva identiteetintarjoaja |
| `linode-stackscript.sh` | Linode | Keycloak tai ulkoinen OIDC | Täysi hallinta |
| `aws-ec2.sh` | AWS EC2 | Keycloak tai ulkoinen OIDC | AWS-käyttöönotot |
| `gcp-compute.sh` | Google Cloud | Keycloak tai ulkoinen OIDC | GCP-käyttöönotot |

> **Suositeltu useimmille käyttäjille:** Käytä `keycloak-embed`-varianttia. Se sisältää sisäänrakennetun Keycloak-identiteettipalvelimen ja vaatii vähiten konfiguraatiokenttiä.

---

## Palvelimen mitoitusopas

| Käyttötapaus | RAM | Levy | Esimerkki |
|----------|-----|------|---------|
| Arviointi / kehitys | 2 Gt | 25 Gt | DO Basic 18 $/kk, t3.small, e2-small |
| Pieni tiimi (< 50 käyttäjää) | 4 Gt | 40 Gt | DO Basic 24 $/kk, t3.medium, e2-medium |
| Tuotanto (> 50 käyttäjää) | 8 Gt | 80 Gt | DO General 48 $/kk, t3.large, n2-standard-2 |

> Upotettu Keycloak vaatii vähintään **4 Gt RAM**. Käytä 2 Gt:a vain arviointiin ilman Keycloakia.

---

## DNS-asetukset

Kaikki skriptit vaativat verkkotunnuksen, jossa on **A-tietue, joka osoittaa palvelimesi IP-osoitteeseen** ennen kuin Let's Encrypt voi myöntää sertifikaatin.

Skripti tulostaa palvelimesi IP-osoitteen asennusprosessin alussa:

```
============================================================
 Palvelimen IP : 139.162.51.85
 Lisää tämä DNS A-tietue nyt, jos et ole jo lisännyt:
   myapp.example.com  ->  139.162.51.85
 Skripti yrittää Certbotia uudelleen joka 60s, kunnes DNS ratkeaa.
============================================================
```

Skripti **yrittää automaattisesti uudelleen** Let's Encryptillä joka 60 sekunnin välein enintään 1 tunnin ajan. Lisää vain DNS-tietue ja odota — uudelleenkäynnistystä ei tarvita.

> **Nopeudenrajoitus:** Let's Encrypt sallii enintään **5 sertifikaattia verkkotunnusta kohti 7 päivän aikana**. Vältä palvelimien toistuvaa käyttöönottoa ja tuhoamista samalla verkkotunnuksella. Jos osut rajoitukseen, skripti näyttää `yritä uudelleen` -aikaleiman ja pysähtyy välittömästi.

---

## Käyttöönottotarkistuslista

- [ ] Sovellus avautuu osoitteessa `https://your-domain.com`
- [ ] Kirjaudu sisään `admin`-tunnuksella ja määrittämälläsi salasanalla
- [ ] Kaikki kontit ovat terveitä: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encryptin uusiminen toimii: `certbot renew --dry-run`
- [ ] MySQL-portti 3306 **ei** ole esillä: `ufw status`
- [ ] Aseta päivittäinen tietokantavarmuuskopiointi (katso [Ylläpito](../maintenance))

---

## Vianmääritys

### Tarkista koko asennusloki

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encryptin nopeudenrajoitus

Jos näet lokissa `too many certificates`, olet saavuttanut 5 sertifikaatin/7 päivää rajan. Loki näyttää tarkan uudelleenyritysajan:

```
[SSL] VIRHE: Let's Encryptin nopeudenrajoitus saavutettu. yritä uudelleen 2026-03-15 16:22 UTC jälkeen.
```

Odota kyseiseen aikaan ja käytä sitten uudelleen.

### Keycloak pysyy epäterveenä

Varmista, että palvelimessa on vähintään 4 Gt RAM, ja tarkista lokit:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL-konfiguraatiota ei sovellettu certbotin jälkeen

Jos sertifikaatti myönnettiin, mutta Nginx näyttää edelleen vain HTTP:n, tarkista lokin virherivi ja lataa Nginx manuaalisesti uudelleen:

```bash
nginx -t && systemctl reload nginx
```
