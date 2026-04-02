---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Nasaďte rtCloud na Linode pomocou skriptu StackScript. Nie je potrebná žiadna konfigurácia – stačí vytvoriť server a postupovať podľa krokov po nasadení."
---

## Krok 1 — Spustite StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tým sa otvorí stránka StackScript v Linode Cloud Manager. Kliknite na **Nasadiť nový Linode**.

---

## Krok 2 — Vyplňte formulár Linode

Vyplňte štandardný formulár na vytvorenie servera Linode:

| Pole | Odporúčaná hodnota |
|-------|------------------|
| **Obrázok** | Ubuntu 22.04 LTS |
| **Región** | Najbližšie k vašim používateľom |
| **Plán** | Zdieľaný CPU 4 GB alebo viac |
| **Heslo root** | Nastavte si silné heslo |
| **Časové pásmo** *(naše jediné pole)* | Časové pásmo vášho servera (predvolené: `Asia/Ho_Chi_Minh`) |

Po dokončení kliknite na **Vytvoriť Linode**.

---

## Krok 3 — Počkajte na dokončenie nastavenia

Skript sa spustí automaticky pri prvom spustení. Nainštaluje Docker, stiahne obraz rtSurvey, inicializuje databázu a spustí všetky služby. Trvá to **5–10 minút**.

Priebeh môžete sledovať priamo v **Linode Cloud Manager** — nevyžaduje sa SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Kliknite na svoj novovytvorený Linode
3. Kliknite na **Spustiť konzolu LISH** (vpravo hore na stránke podrobností Linode)

Otvorí sa terminál prehliadača so záznamom živého zavádzania – karta **Weblish** funguje priamo vo vašom prehliadači, nie je potrebný žiadny klient SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Počkajte, kým neuvidíte:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Protokol tiež zobrazuje IP adresu vášho servera – budete ju potrebovať v ďalšom kroku.

---

## Krok 4 – Nastavte SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Pri konfigurácii HTTPS postupujte podľa **[Sprievodca nastavením SSL →](../ssl-setup)**. Bezplatná subdoména **rtsurvey.com** je najrýchlejšou možnosťou – nie je potrebné žiadne nastavenie DNS.

---

## Krok 5 — Prvé prihlásenie

Keď je SSL aktívny, postupujte podľa **[Príručky prvého prihlásenia →](../first-login)**, aby ste získali prístup k účtu správcu.

---

## Krok 6 — Zmeňte predvolené heslo

Všetky heslá sú štandardne nastavené na `admin`. Zmeňte ich ihneď po prvom prihlásení:

- **Heslo správcu aplikácie** – nastavenia účtu v aplikácii
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Pravidlá brány firewall (Linode Cloud Firewall)

Ak k tomuto serveru pripojíte Linode Cloud Firewall, použite nasledujúce pravidlá:

### Prichádzajúce

| Označenie | Akcia | Protokol | Prístav | Zdroje | Poznámky |
|-------|--------|----------|------|---------|-------|
| `accept-inbound-ssh` | Prijať | TCP | 22 | Všetky IPv4, všetky IPv6 | SSH prístup |
| `prijať-prichádzajúce-http` | Prijať | TCP | 80 | Všetky IPv4, všetky IPv6 | Nginx (výzva HTTP + ACME) |
| "prijať-prichádzajúce-https" | Prijať | TCP | 443 | Všetky IPv4, všetky IPv6 | Nginx (HTTPS po nastavení SSL) |
| "prijať-prichádzajúce-lesklé" | Prijať | TCP | 3838 | Všetky IPv4, všetky IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Prijať | ICMP | — | Všetky IPv4, všetky IPv6 | Ping / diagnostika |
| Predvolená vstupná politika | **Drop** | | | | Blokovať všetko ostatné |

### Odchádzajúci

| Označenie | Akcia | Poznámky |
|-------|--------|-------|
| Predvolená odchádzajúce politika | **Prijať** | Povoliť všetky odchádzajúce (Docker pulls, certbot, GoDaddy API atď.) |

### Porty nie sú potrebné externe

Tieto porty sú viazané iba na `127.0.0.1` a nikdy nie sú dosiahnuteľné mimo servera:

| Prístav | Služba | Dôvod |
|------|---------|--------|
| 8080 | Kontajner aplikácie | Nginx sa k nemu interne pripája |
| 8090 | Zásobník na kľúčenky | Nginx sa k nemu interne pripája |
| 3306 | MySQL | Len interná sieť Docker |

---

## Riešenie problémov

### Skontrolujte denník nastavenia

```bash
tail -200 /var/log/stackscript.log
```

### Skontrolujte protokol SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Zobraziť stav kontajnera

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
