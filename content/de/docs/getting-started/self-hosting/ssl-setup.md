---
weight: 4
title: "SSL einrichten"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurieren Sie HTTPS für Ihren rtSurvey-Server. Erforderlich vor der Anmeldung."
---

SSL muss konfiguriert werden, bevor Sie sich anmelden können. Wenn Sie die App zum ersten Mal öffnen, werden Sie automatisch zum SSL-Einrichtungsbildschirm weitergeleitet.

---

## SSL-Einrichtungsoptionen

![SSL-Einrichtungsoptionen](/img/ssl-setup/ssl-setup-options.png)

Wählen Sie eine von drei Optionen:

| Option | Wann zu verwenden |
|--------|------------------|
| **Kostenlose rtsurvey.com-Subdomain** *(Empfohlen)* | Keine DNS-Einrichtung erforderlich. Wir erstellen den Eintrag für Sie. In 2–5 Minuten bereit. |
| **Eigene Domain** | Sie haben bereits eine Domain und deren DNS zeigt auf diesen Server. |
| **Zertifikat manuell installieren** | Unternehmen oder benutzerdefinierte CA. Erfordert SSH-Zugang. |

---

## Option 1 — Kostenlose rtsurvey.com-Subdomain *(Empfohlen)*

Dies ist die schnellste Option. Keine Domain-Registrierung oder DNS-Änderungen erforderlich.

1. Klicken Sie auf **Kostenlose rtsurvey.com-Subdomain**, um den Abschnitt zu erweitern
2. Geben Sie den gewünschten Subdomain-Namen im Eingabefeld ein

   > Verwenden Sie Kleinbuchstaben, Zahlen und Bindestriche. 3–30 Zeichen.
   > Beispiel: `myproject` → `myproject.rtsurvey.com`

3. Klicken Sie auf **https://[subdomain].rtsurvey.com erstellen**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Warten Sie 2–5 Minuten, während das Zertifikat ausgestellt wird

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Sobald das Zertifikat bereit ist, werden Sie automatisch zur neuen HTTPS-URL weitergeleitet

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — Eigene Domain

Verwenden Sie dies, wenn Sie eine vorhandene Domain haben und deren DNS `A`-Eintrag bereits auf die IP dieses Servers zeigt.

1. Klicken Sie auf **Eigene Domain**, um den Abschnitt zu erweitern
2. Geben Sie Ihren vollständigen Domainnamen ein (z.B. `survey.myorganization.org`)
3. Klicken Sie auf **Zertifikat erstellen**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt verifiziert Ihre Domain und stellt ein Zertifikat aus. DNS muss vorher korrekt eingerichtet sein — sonst schlägt die Anfrage fehl.

---

## Option 3 — Zertifikat manuell installieren

Für Unternehmensumgebungen mit einer benutzerdefinierten oder internen CA. Sie platzieren Ihre Zertifikatsdateien per SSH auf dem Server und geben dann Ihre Domain in der App ein.

### Voraussetzungen

- SSH-Zugang zum Server
- Gültiges Zertifikat und privater Schlüssel für Ihre Domain (PEM-Format)

### Schritt 1 — SSH auf den Server

```bash
ssh root@<server-ip>
```

### Schritt 2 — Zertifikatsdateien platzieren

Verzeichnis erstellen und Dateien kopieren:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Dateien mit diesen genauen Namen kopieren:

| Datei | Beschreibung |
|-------|-------------|
| `fullchain.pem` | Ihr Zertifikat + alle Zwischen-CA-Zertifikate (verkettet) |
| `privkey.pem` | Ihr privater Schlüssel |

Beispiel:

```bash
# Von Ihrem lokalen Rechner kopieren (lokal ausführen, nicht auf dem Server)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Korrekte Berechtigungen setzen:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Schritt 3 — Domain in der App eingeben

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Klicken Sie auf dem SSL-Einrichtungsbildschirm auf **Zertifikat manuell installieren**
2. Geben Sie Ihren Domainnamen ein (muss mit dem Common Name oder SAN des Zertifikats übereinstimmen)
3. Klicken Sie auf **Anwenden**

Der Server konfiguriert Nginx mit Ihrem Zertifikat und lädt automatisch neu.

---

## Nächster Schritt

Sobald SSL aktiv ist, fahren Sie mit der [Ersten Anmeldung](first-login) fort.
