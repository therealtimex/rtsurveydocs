---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Nasaďte rtCloud na Linode pomocí StackScript. Není potřeba žádná konfigurace – stačí vytvořit server a postupovat podle kroků po nasazení."
---

## Krok 1 — Spusťte StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tím se otevře stránka StackScript v Linode Cloud Manager. Klikněte na **Nasadit nový Linode**.

---

## Krok 2 — Vyplňte formulář Linode

Vyplňte standardní formulář pro vytvoření serveru Linode:

| Pole | Doporučená hodnota |
|-------|------------------|
| **Obrázek** | Ubuntu 22.04 LTS |
| **Region** | Nejblíže vašim uživatelům |
| **Plán** | Sdílený CPU 4 GB nebo větší |
| **Heslo root** | Nastavte silné heslo |
| **Firewall** | Žádný firewall *(doporučeno)* |
| **Časové pásmo** *(naše jediné pole)* | Vaše časové pásmo serveru (výchozí: `Asia/Ho_Chi_Minh`) |

> **Proč žádný firewall?** Instalační skript potřebuje odchozí přístup k internetu (Docker pulls, Let's Encrypt). Blokování portů během prvního spuštění může způsobit selhání nasazení. Po dokončení nastavení můžete připojit bránu firewall — správná pravidla naleznete níže v části [Pravidla brány firewall](#firewall-rules-linode-cloud-firewall).

Po dokončení klikněte na **Vytvořit Linode**.

---

## Krok 3 — Počkejte na dokončení nastavení

Skript se automaticky spustí při prvním spuštění. Nainstaluje Docker, stáhne obraz rtSurvey, inicializuje databázi a spustí všechny služby. To trvá **5–10 minut**.

Průběh můžete sledovat přímo v **Linode Cloud Manager** – není potřeba SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klikněte na svůj nově vytvořený Linode
3. Klikněte na **Spustit konzolu LISH** (vpravo nahoře na stránce s podrobnostmi o Linode)

Otevře se terminál prohlížeče se záznamem živého spouštění – karta **Weblish** funguje přímo ve vašem prohlížeči, není potřeba žádný klient SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Počkejte, až uvidíte:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Protokol také zobrazuje IP adresu vašeho serveru – budete ji potřebovat pro další krok.

---

## Krok 4 — Nastavte SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Při konfiguraci HTTPS postupujte podle **[Průvodce nastavením SSL →](../ssl-setup)**. Bezplatná subdoména **rtsurvey.com** je nejrychlejší možností – není potřeba žádné nastavení DNS.

---

## Krok 5 — Změňte výchozí heslo

Výchozí nastavení všech hesel je `admin`. Změňte je ihned po prvním přihlášení:

- **Heslo správce aplikace** – nastavení účtu v aplikaci
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Pravidla brány firewall (Linode Cloud Firewall)

Pokud k tomuto serveru připojíte Linode Cloud Firewall, použijte následující pravidla:

### Příchozí

| Štítek | Akce | Protokol | Přístav | Zdroje | Poznámky |
|-------|--------|----------|------|---------|-------|
| `accept-inbound-ssh` | Přijmout | TCP | 22 | Všechny IPv4, všechny IPv6 | SSH přístup |
| `accept-inbound-http` | Přijmout | TCP | 80 | Všechny IPv4, všechny IPv6 | Nginx (výzva HTTP + ACME) |
| `přijmout-příchozí-https` | Přijmout | TCP | 443 | Všechny IPv4, všechny IPv6 | Nginx (HTTPS po nastavení SSL) |
| `přijmout-příchozí-lesklý` | Přijmout | TCP | 3838 | Všechny IPv4, všechny IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Přijmout | ICMP | — | Všechny IPv4, všechny IPv6 | Ping / diagnostika |
| Výchozí zásady pro příchozí hovory | **Drop** | | | | Blokovat vše ostatní |

### Odchozí

| Štítek | Akce | Poznámky |
|-------|--------|-------|
| Výchozí odchozí politika | **Přijmout** | Povolit všechny odchozí (Docker pulls, certbot, GoDaddy API atd.) |

### Porty nejsou potřeba externě

Tyto porty jsou vázány pouze na `127.0.0.1` a nejsou nikdy dosažitelné zvenčí serveru:

| Přístav | Služba | Důvod |
|------|---------|--------|
| 8080 | Kontejner aplikace | Nginx k němu interně proxy |
| 8090 | Keycloak kontejner | Nginx k němu interně proxy |
| 3306 | MySQL | Pouze interní síť Docker |

---

## Odstraňování problémů

### Zkontrolujte protokol nastavení

```bash
tail -200 /var/log/stackscript.log
```

### Zkontrolujte protokol SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Zobrazit stav kontejneru

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
