---
title: "App-API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

Die App-API ermöglicht es Benutzern, Systemmetadaten aus der App über verschiedene Methoden im FormEngine und DMView zu laden. Sie bietet Zugriff auf verschiedene Datenschlüssel zum Abrufen spezifischer Informationen aus der App.

In der XLSForm können Sie die Funktion `pulldata()` mit der folgenden Syntax verwenden:

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Dieses Schlüsselwort weist die FormEngine an, die Daten von der App-API zu laden.
- `'data-key'`: Dies ist der Schlüssel der Daten, die Sie von der App-API laden möchten.
- Falls der Datenschlüssel ungültig oder nicht unterstützt wird, gibt die Berechnung "n/a" zurück.

Hier sind die unterstützten Datenschlüssel, die Sie mit der App-API verwenden können:

`osPlatform`: Gibt den aktuellen OS-Namen (Android oder iOS) und die OS-Version zurück. Web-Plattformen geben einen leeren Wert zurück.

`appPlatform`: Gibt den Namen der App-Plattform zurück, welcher `rtSurvey` lautet.

`appVersion`: Gibt den Versionsnamen der App zurück.

`getDisplayWidth`: Gibt die Breite des Gerätebildschirms in Pixeln zurück.

`getDisplayHeight`: Gibt die Höhe des Gerätebildschirms in Pixeln zurück.

`getScreenSize`: Gibt die Bildschirmgröße des Geräts in Zoll zurück.

`projectCode`: Gibt den aktuellen Projektcode der Site zurück, bei der der Benutzer angemeldet ist.

`projectURL`: Gibt die aktuelle Projekt-URL der Site zurück, bei der der Benutzer angemeldet ist. Der Standard-/Fallback-Wert ist ein leerer Text ("").

`startingPoint`: Gibt den Pfad des Punktes zurück, an dem das Formular startet. Weitere Details finden Sie unter "Form starting point".

`serverTime`: Gibt die bestmögliche Annäherung an Datum und Uhrzeit auf dem Server zurück.

`user.[attribute]`: Gibt die aktuellen Benutzerattribute basierend auf dem angegebenen Attributschlüssel zurück. Verfügbare Attributschlüssel finden Sie in der Tabelle "User attributes".

Kombinieren Sie die unten stehenden Attributschlüssel mit "user." in den `pulldata()`-Parametern, um aktuelle Benutzerinformationen abzurufen. Verwenden Sie zum Beispiel `user.username`, `user.email` usw.

| Attributschlüssel     | Beschreibung                          |
|----------------------|--------------------------------------|
| username             | Benutzername des Benutzers           |
| name                 | Vollständiger Name des Benutzers     |
| staffCode            | Personalcode des Benutzers           |
| phone                | Telefonnummer des Benutzers          |
| email                | E-Mail-Adresse des Benutzers         |
| description          | Beschreibungstext in den Benutzerinfos|
| organization_id      | Organisations-ID des Benutzers       |
| organization_name    | Organisationsname des Benutzers      |
| team_id              | Team-ID des Benutzers                |
| supervisor_id        | ID des Vorgesetzten des Benutzers    |
| user_role            | Benutzerrolle                        |
| user_group           | Benutzergruppe                       |
| is_supervisor        | 1, wenn der Benutzer ein Vorgesetzter ist, sonst 0 |
| auto_approve_edit_request | 1, wenn der Benutzer automatische Bearbeitungsanfragen genehmigen darf, sonst 0 |
| ipcall.user          | IP Call Account-Parameter - Benutzername |
| ipcall.token         | IP Call Account-Parameter - Token    |
| ipcall.password      | IP Call Account-Parameter - Passwort |
| ipcall.url           | IP Call Account-Parameter - URL      |
| ipcall.auth          | IP Call Account-Parameter - Auth (optional) |
| ipcall.port          | IP Call Account-Parameter - Port (optional) |

`instancePath`: Gibt den Pfad des aktuellen Instanzordners zurück.

`appLanguage`: Gibt die aktuelle App-Sprache zurück, die in den Einstellungen der App festgelegt ist (z. B. vi, en, de).

`openArgs.[attribute]`: Gibt das open-form-argument zurück, das vom ActionButton (act_fill_form, act_get_instance) übergeben wurde. Der Standardwert ist ein leerer Text ("").

`primaryAppColor`: Ruft die primäre Farbe der App ab.
