---
title: "Webbox"
description: "Webbox bettet eine externe Webseite in die Umfrage als modales iFrame ein, sodass Interviewer Referenzen ansehen oder mit externen Tools interagieren können, ohne das Formular zu verlassen."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** bettet eine externe Webseite als **modales Popup** (iFrame) in die Umfrage ein. Der Interviewer tippt auf eine Schaltfläche in der Beschriftung oder dem Notiztext, die Seite öffnet sich in einer Vollbild-Überlagerung innerhalb des Formulars, und beim Schließen kehrt er genau dorthin zurück, wo er war. Damit können Sie Referenzmaterial, Karten, Dashboards oder benutzerdefinierte Tools anzeigen, ohne einen separaten Browser-Tab zu öffnen.

---

## Syntax

Fügen Sie einen `<webbox>`-HTML-Tag direkt in eine `label`- oder `note`-Beschriftungsspalte ein:

```html
<webbox src='https://example.com/reference' title='Referenzleitfaden'>Referenzleitfaden öffnen</webbox>
```

| Attribut | Beschreibung |
|----------|-------------|
| `src` | Die im iFrame zu ladende URL. Unterstützt einfache und doppelte Anführungszeichen. |
| `title` | Text, der in der modalen Kopfzeile angezeigt wird. Unterstützt Klartext. |
| *(Inhalt)* | Die anklickbare Schaltflächenbeschriftung, die im Umfragefeld angezeigt wird |

---

## Grundlegendes Beispiel

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Feldleitfaden'>📖 Feldleitfaden öffnen</webbox>` |

Dies rendert eine Schaltfläche mit der Aufschrift "📖 Feldleitfaden öffnen". Beim Antippen öffnet sich ein Modal, das die Feldleitfaden-Website anzeigt.

---

## Eine Karte einbetten

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Umfragegebietskarte'>🗺 Karte anzeigen</webbox>` |

---

## Formularwerte an die eingebettete Seite übergeben

Hängen Sie Formularfeldwerte mit `concat()` in der Spalte `calculation` an die URL an und referenzieren Sie das Ergebnis in der Beschriftung:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Haushalts-Dashboard'>Dashboard öffnen</webbox>` |

{{% alert icon=" " context="warning" %}}
Das `src`-Attribut im `<webbox>`-Tag unterstützt `${fieldname}`-Referenzen, wenn die Beschriftung aus einem `calculate`-Feld berechnet wird. Erstellen Sie die vollständige URL in einem `calculate`-Feld und referenzieren Sie sie.
{{% /alert %}}

---

## Wiederholungsinteraktion: Löschen-Schaltflächen

Webbox unterstützt auch spezielle Aktions-Tags zur Verwaltung von Wiederholungsgruppen innerhalb von Beschriftungen:

```html
<delete-repeat-current>Diese Zeile entfernen</delete-repeat-current>
<delete-repeat-last>Letzte Zeile entfernen</delete-repeat-last>
```

Diese werden als Schaltflächen gerendert, die Wiederholungsinstanzen löschen, wenn sie angetippt werden. Platzieren Sie sie in einem `note`-Feld innerhalb (oder unmittelbar nach) der Wiederholungsgruppe:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Eintrag |
| text | item_name | Eintragsname |
| note | delete_btn | `<delete-repeat-current>✕ Diesen Eintrag entfernen</delete-repeat-current>` |
| end_repeat | | |

---

## Kommunikation mit der eingebetteten Seite (postMessage)

Das Webbox-iFrame und das übergeordnete Formular können über die `postMessage`-API des Browsers kommunizieren. Das übergeordnete Element sendet eine `init`-Nachricht an das iFrame, wenn es geöffnet wird. Die eingebettete Seite kann antworten mit:

- `delete-repeat-current` — löst die Löschung der aktuellen Wiederholungsinstanz aus
- `delete-repeat-last` — löst die Löschung der letzten Wiederholungsinstanz aus

Dies ermöglicht benutzerdefinierten Webtools (z. B. Zeichentools, interaktive Karten), Formularaktionen auszulösen, wenn der Benutzer eine Aktion innerhalb des iFrames bestätigt.

---

## Empfohlene Vorgehensweisen

1. Verwenden Sie Webbox für **Referenzmaterial** (Leitlinien, Nachschlagetabellen, Karten) — nicht für das Erfassen von Daten, die im Formular selbst sein sollten.
2. Stellen Sie sicher, dass die eingebettete URL vom Netzwerk des Geräts aus erreichbar ist — Webbox erfordert Konnektivität.
3. Halten Sie die eingebettete Seite mobilfreundlich — das Modal ist maximal 800px breit und 80% der Viewport-Höhe.
4. Verwenden Sie beschreibenden Schaltflächentext (z. B. "Dorfkarte anzeigen") statt generischen Beschriftungen ("Hier klicken").
5. Informieren Sie Interviewer darüber, dass das Schließen des Modals sie zur Umfrage zurückbringt — einige Benutzer wissen möglicherweise nicht, wie sie eine iFrame-Überlagerung schließen.

## Einschränkungen

- Webbox erfordert Netzwerkkonnektivität, um die eingebettete URL zu laden.
- Einige externe Websites blockieren das Einbetten in iFrames über `X-Frame-Options`- oder `Content-Security-Policy`-Header — diese Websites können nicht mit Webbox verwendet werden.
- Das Modal schließt sich, wenn der Interviewer von der Frage weg navigiert — nicht gespeicherter Zustand im iFrame geht verloren.
- Webbox ist eine rtSurvey-Webformular-Erweiterung und funktioniert möglicherweise nicht in anderen ODK-kompatiblen Clients.
