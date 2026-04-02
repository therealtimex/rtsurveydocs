---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuera rtCloud på Linode med ett StackScript. Ingen konfiguration behövs – skapa bara servern och följ stegen efter distributionen."
---

## Steg 1 — Starta StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Detta öppnar StackScript-sidan i Linode Cloud Manager. Klicka på **Distribuera ny Linode**.

---

## Steg 2 — Fyll i Linodes formulär

Fyll i Linodes standardformulär för skapande av server:

| Fält | Rekommenderat värde |
|-------|------------------------|
| **Bild** | Ubuntu 22.04 LTS |
| **Region** | Närmast dina användare |
| **Planera** | Delad CPU 4 GB eller större |
| **Root-lösenord** | Ange ett starkt lösenord |
| **Tidszon** *(vårt enda fält)* | Din servertidszon (standard: `Asia/Ho_Chi_Minh`) |

Klicka på **Skapa Linode** när du är klar.

---

## Steg 3 — Vänta tills installationen är klar

Skriptet körs automatiskt vid första uppstart. Den installerar Docker, hämtar rtSurvey-bilden, initierar databasen och startar alla tjänster. Detta tar **5–10 minuter**.

Du kan se framstegen direkt i **Linode Cloud Manager** — ingen SSH krävs:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klicka på din nyskapade Linode
3. Klicka på **Starta LISH Console** (överst till höger på Linodes detaljsida)

En webbläsarterminal öppnas och visar livestartloggen — fliken **Weblish** fungerar direkt i din webbläsare, ingen SSH-klient behövs.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Vänta tills du ser:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Loggen visar också din server-IP - du behöver den för nästa steg.

---

## Steg 4 — Konfigurera SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Följ **[Set Up SSL guide →](../ssl-setup)** för att konfigurera HTTPS. Den kostnadsfria **rtsurvey.com-underdomänen** är det snabbaste alternativet – ingen DNS-installation behövs.

---

## Steg 5 — Första inloggningen

När SSL är aktivt, följ **[First Login Guide →](../first-login)** för att komma åt administratörskontot.

---

## Steg 6 — Ändra standardlösenordet

Alla lösenord är som standard "admin". Ändra dem direkt efter din första inloggning:

- **Appadministratörslösenord** — kontoinställningar i appen
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Brandväggsregler (Linode Cloud Firewall)

Om du ansluter en Linode Cloud Firewall till den här servern, använd följande regler:

### Inkommande

| Etikett | Åtgärd | Protokoll | Hamn | Källor | Anteckningar |
|-------|--------|--------|------|--------|-------|
| `accept-inbound-ssh` | Acceptera | TCP | 22 | Alla IPv4, Alla IPv6 | SSH-åtkomst |
| `acceptera-inkommande-http` | Acceptera | TCP | 80 | Alla IPv4, Alla IPv6 | Nginx (HTTP + ACME utmaning) |
| `acceptera-inkommande-https` | Acceptera | TCP | 443 | Alla IPv4, Alla IPv6 | Nginx (HTTPS efter SSL-installation) |
| `acceptera-inkommande-glänsande` | Acceptera | TCP | 3838 | Alla IPv4, Alla IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Acceptera | ICMP | — | Alla IPv4, Alla IPv6 | Ping / diagnostik |
| Standard inkommande policy | **Släpp** | | | | Blockera allt annat |

### Utgående

| Etikett | Åtgärd | Anteckningar |
|-------|--------|-------|
| Standard utgående policy | **Acceptera** | Tillåt alla utgående (Docker pulls, certbot, GoDaddy API, etc.) |

### Portar behövs INTE externt

Dessa portar är endast bundna till "127.0.0.1" och kan aldrig nås utanför servern:

| Hamn | Service | Anledning |
|------|--------|--------|
| 8080 | Appbehållare | Nginx fullmakter till det internt |
| 8090 | Keycloak container | Nginx fullmakter till det internt |
| 3306 | MySQL | Endast internt Docker-nätverk |

---

## Felsökning

### Kontrollera inställningsloggen

```bash
tail -200 /var/log/stackscript.log
```

### Kontrollera SSL-loggen

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Visa containerstatus

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
