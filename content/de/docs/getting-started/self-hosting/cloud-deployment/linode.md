---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Stellen Sie rtCloud mit einem StackScript auf Linode bereit. Keine Konfiguration erforderlich – erstellen Sie einfach den Server und befolgen Sie die Schritte nach der Bereitstellung."
---

## Schritt 1 – Starten Sie StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Dadurch wird die StackScript-Seite im Linode Cloud Manager geöffnet. Klicken Sie auf **Neuen Linode bereitstellen**.

---

## Schritt 2 – Füllen Sie das Linode-Formular aus

Füllen Sie das Standardformular zur Servererstellung von Linode aus:

| Feld | Empfohlener Wert |
|-------|----|
| **Bild** | Ubuntu 22.04 LTS |
| **Region** | Am nächsten an Ihren Benutzern |
| **Plan** | Gemeinsam genutzte CPU 4 GB oder mehr |
| **Root-Passwort** | Legen Sie ein sicheres Passwort fest |
| **Zeitzone** *(unser einziges Feld)* | Ihre Server-Zeitzone (Standard: „Asia/Ho_Chi_Minh“) |

Klicken Sie abschließend auf **Linode erstellen**.

---

## Schritt 3 – Warten Sie, bis die Einrichtung abgeschlossen ist

Das Skript wird beim ersten Start automatisch ausgeführt. Es installiert Docker, ruft das rtSurvey-Image ab, initialisiert die Datenbank und startet alle Dienste. Dies dauert **5–10 Minuten**.

Sie können den Fortschritt direkt im **Linode Cloud Manager** verfolgen – kein SSH erforderlich:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klicken Sie auf Ihren neu erstellten Linode
3. Klicken Sie auf **LISH-Konsole starten** (oben rechts auf der Linode-Detailseite).

Es öffnet sich ein Browser-Terminal mit dem Live-Boot-Protokoll – die Registerkarte **Weblish** funktioniert direkt in Ihrem Browser, kein SSH-Client erforderlich.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Warten Sie, bis Sie Folgendes sehen:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Das Protokoll zeigt auch Ihre Server-IP – Sie benötigen sie für den nächsten Schritt.

---

## Schritt 4 – SSL einrichten

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Befolgen Sie die **[Anleitung zum Einrichten von SSL →](../ssl-setup)**, um HTTPS zu konfigurieren. Die kostenlose Subdomain **rtsurvey.com** ist die schnellste Option – es ist keine DNS-Einrichtung erforderlich.

---

## Schritt 5 – Erster Login

Sobald SSL aktiv ist, folgen Sie der **[Anleitung zur ersten Anmeldung →](../first-login)**, um auf das Administratorkonto zuzugreifen.

---

## Schritt 6 – Ändern Sie das Standardkennwort

Alle Passwörter lauten standardmäßig „admin“. Ändern Sie diese sofort nach Ihrem ersten Login:

- **App-Administratorkennwort** – Kontoeinstellungen innerhalb der App
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Firewall-Regeln (Linode Cloud Firewall)

Wenn Sie eine Linode Cloud Firewall an diesen Server anschließen, verwenden Sie die folgenden Regeln:

### Eingehend

| Etikett | Aktion | Protokoll | Hafen | Quellen | Notizen |
|-------|--------|----------|------|---------|-------|
| `accept-inbound-ssh` | Akzeptieren | TCP | 22 | Alle IPv4, Alle IPv6 | SSH-Zugriff |
| `accept-inbound-http` | Akzeptieren | TCP | 80 | Alle IPv4, Alle IPv6 | Nginx (HTTP + ACME-Herausforderung) |
| `accept-inbound-https` | Akzeptieren | TCP | 443 | Alle IPv4, Alle IPv6 | Nginx (HTTPS nach SSL-Einrichtung) |
| `accept-inbound-shiny` | Akzeptieren | TCP | 3838 | Alle IPv4, Alle IPv6 | Shiny Server (R-Analyse) |
| `accept-inbound-icmp` | Akzeptieren | ICMP | — | Alle IPv4, Alle IPv6 | Ping / Diagnose |
| Standard-Eingangsrichtlinie | **Tropfen** | | | | Alles andere blockieren |

### Ausgehend

| Etikett | Aktion | Notizen |
|-------|--------|-------|
| Standard-Ausgangsrichtlinie | **Akzeptieren** | Alle ausgehenden Daten zulassen (Docker-Pulls, Certbot, GoDaddy-API usw.) |

### Ports werden extern NICHT benötigt

Diese Ports sind nur an „127.0.0.1“ gebunden und niemals von außerhalb des Servers erreichbar:

| Hafen | Service | Grund |
|------|---------|--------|
| 8080 | App-Container | Nginx stellt intern einen Proxy her |
| 8090 | Keycloak-Behälter | Nginx stellt intern einen Proxy her |
| 3306 | MySQL | Nur internes Docker-Netzwerk |

---

## Fehlerbehebung

### Überprüfen Sie das Setup-Protokoll

```bash
tail -200 /var/log/stackscript.log
```

### Überprüfen Sie das SSL-Protokoll

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Containerstatus anzeigen

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
