---
weight: 3
title: "Felhőtelepítés"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Az rtCloud telepítése a főbb felhőszolgáltatókhoz automatizált szkriptekkel DigitalOcean, AWS EC2, Google Cloud és Linode platformokon."
---

A telepítési tároló automatizált üzembehelyezési szkripteket tartalmaz a főbb felhőszolgáltatókhoz. Minden szkript egy friss **Ubuntu 22.04 LTS** kiszolgáló első indításakor fut, és teljesen felügyelet nélküli beállítást végez:

- Telepíti a Dockert és a Docker Compose-t
- Biztonságos véletlenszerű jelszavakat generál az összes belső szolgáltatáshoz
- Létrehozza a `docker-compose.production.yml` és `.env` fájlokat
- Konfigurációja Nginxet fordított proxyként
- Ingyenes TLS-tanúsítványt szerez be a Let's Encrypt-től (automatikusan újrapróbálkozik, amíg a DNS fel nem oldódik)
- Konfigurálja az UFW tűzfalat
- Opcionálisan telepíti a beágyazott Keycloak SSO-szervert
- Kimenete egy teljes telepítési összefoglalót az összes hitelesítő adattal

A beállítás **5–10 percen** belül befejeződik egy szabványos példányon.

---

## Szkript kiválasztása

A felhőszolgáltatótól és az SSO-beállítástól függően több szkriptváltozat áll rendelkezésre:

| Szkript | Szolgáltató | SSO mód | A legjobb |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Beépített Keycloak | Egyszerű, önálló SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak vagy külső OIDC | Teljes irányítás |
| `linode-stackscript-keycloak-embed.sh` | Linode | Beépített Keycloak | Űrlapalapú beállítás, legegyszerűbb |
| `linode-stackscript-oidc.sh` | Linode | Csak külső OIDC | Meglévő identitásszolgáltató |
| `linode-stackscript.sh` | Linode | Keycloak vagy külső OIDC | Teljes irányítás |
| `aws-ec2.sh` | AWS EC2 | Keycloak vagy külső OIDC | AWS-telepítések |
| `gcp-compute.sh` | Google Cloud | Keycloak vagy külső OIDC | GCP-telepítések |

> **A legtöbb felhasználónak ajánlott:** Használja a `keycloak-embed` változatot. Tartalmaz egy beépített Keycloak identitásszervert, és a legkevesebb konfigurációs mezőt igényli.

---

## Kiszolgálóméretezési útmutató

| Felhasználási eset | RAM | Lemez | Példa |
|----------|-----|------|---------|
| Értékelés / fejlesztés | 2 GB | 25 GB | DO Basic $18/hó, t3.small, e2-small |
| Kis csapat (< 50 felhasználó) | 4 GB | 40 GB | DO Basic $24/hó, t3.medium, e2-medium |
| Éles (> 50 felhasználó) | 8 GB | 80 GB | DO General $48/hó, t3.large, n2-standard-2 |

> A beágyazott Keycloak legalább **4 GB RAM-ot** igényel. A 2 GB-ot csak Keycloak nélküli értékeléshez használja.

---

## DNS-beállítás

Minden szkript egy **A-rekordot igényel, amely a kiszolgáló IP-címére mutat**, mielőtt a Let's Encrypt tanúsítványt tud kiállítani.

A szkript a beállítási folyamat elején kinyomtatja a kiszolgáló IP-címét:

```
============================================================
 Kiszolgáló IP : 139.162.51.85
 Adja hozzá ezt a DNS A-rekordot most, ha még nem tette meg:
   myapp.example.com  ->  139.162.51.85
 A szkript 60 másodpercenként újrapróbálkozik a Certbot-tal, amíg a DNS fel nem oldódik.
============================================================
```

A szkript **automatikusan újrapróbálkozik** a Let's Encrypt-tel 60 másodpercenként, legfeljebb 1 óráig. Csak adja hozzá a DNS-rekordot és várjon — nincs szükség újraindításra.

> **Sebességkorlát:** A Let's Encrypt legfeljebb **5 tanúsítványt engedélyez domainenként 7 napon belül**. Ne telepítse és törölje a kiszolgálókat ismételten ugyanazzal a domainnel. Ha eléri a korlátot, a szkript megjelenít egy `retry after` időbélyeget és azonnal leáll.

---

## Telepítés utáni ellenőrzőlista

- [ ] Az alkalmazás megnyílik a `https://your-domain.com` címen
- [ ] Bejelentkezés `admin` felhasználóval és a konfigurált jelszóval
- [ ] Minden konténer egészséges: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] A Let's Encrypt megújítás működik: `certbot renew --dry-run`
- [ ] A MySQL 3306-os port **nem** érhető el: `ufw status`
- [ ] Napi adatbázis-biztonsági mentés beállítása (lásd [Karbantartás](../maintenance))

---

## Hibaelhárítás

### A teljes beállítási napló ellenőrzése

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt sebességkorlát

Ha a naplóban `too many certificates` üzenetet lát, elérte az 5 tanúsítvány/7 nap korlátot. A napló mutatja a pontos újrapróbálkozási időt:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Várjon addig az időpontig, majd telepítse újra.

### A Keycloak nem egészséges állapotban marad

Győződjön meg arról, hogy a kiszolgálónak legalább 4 GB RAM-ja van, majd ellenőrizze a naplókat:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### Az SSL-konfiguráció nem kerül alkalmazásra a certbot után

Ha a tanúsítvány kiállításra kerül, de az Nginx még mindig csak HTTP-t mutat, ellenőrizze a naplóban a hibasort, és töltse be manuálisan az Nginxet:

```bash
nginx -t && systemctl reload nginx
```
