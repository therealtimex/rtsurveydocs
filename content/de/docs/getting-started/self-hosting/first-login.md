---
weight: 5
title: "Erste Anmeldung"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "So melden Sie sich nach der Bereitstellung zum ersten Mal bei Ihrer rtSurvey-Instanz an."
---

> **SSL muss vor der Anmeldung konfiguriert werden.** Wenn Sie über HTTP auf die App zugreifen, wird eine Sicherheitswarnung angezeigt und SSO wird blockiert. Schließen Sie zuerst [SSL einrichten](ssl-setup) ab.

Nachdem SSL aktiv ist, öffnen Sie Ihren Browser unter Ihrer HTTPS-URL:

```
https://your-domain.com
```

---

## Der Anmeldebildschirm

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Die Anmeldeseite zeigt:

- Felder für **Benutzername** und **Passwort**
- Eine **Anmelden**-Schaltfläche
- Eine **Mit SSO anmelden**-Schaltfläche (unter einem Trennstrich) — für Teammitglieder mit SSO-Konten

---

## Standard-Administratorzugangsdaten

Geben Sie die Standardzugangsdaten ein und klicken Sie auf **Anmelden**:

| Feld | Wert |
|------|------|
| Benutzername | `admin` |
| Passwort | `admin` |

> **Ändern Sie Ihr Passwort unmittelbar nach der ersten Anmeldung.**

---

## Wenn eine Sicherheitswarnung angezeigt wird

Wenn Sie über HTTP auf die App zugreifen (bevor SSL konfiguriert ist), sehen Sie:

- Ein gelbes Warnbanner oben auf der Anmeldeseite
- Ein Modal beim Klicken auf **Anmelden**, das warnt, dass Zugangsdaten unverschlüsselt gesendet werden

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Klicken Sie auf **SSL einrichten**, um HTTPS zu konfigurieren, oder auf **Trotzdem fortfahren**, um sich ohne SSL anzumelden (nicht empfohlen).

Die SSO-Anmeldung ist über HTTP vollständig blockiert — ein Klick auf **Mit SSO anmelden** zeigt einen Hinweis anstelle einer Weiterleitung.

---

## Nach der Anmeldung

Nach der Anmeldung landen Sie auf dem Dashboard. Von hier aus:

1. **Administratorpasswort ändern** — Kontoeinstellungen → Passwort ändern
2. **Erstes Projekt erstellen** — Projekte → Neues Projekt
3. **Formular hochladen oder erstellen** — Formulare → XLSForm hochladen oder Form Builder öffnen
4. **Benutzer hinzufügen** — Benutzer → Einladen oder Konten für Ihr Team erstellen
