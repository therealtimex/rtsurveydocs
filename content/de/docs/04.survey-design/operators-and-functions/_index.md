---
title: "Operatoren und Funktionen"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Ausdrücke in rtSurvey werden in einer Teilmenge von **XPath 1.0** geschrieben, erweitert um JavaRosa/ODK-Funktionen und benutzerdefinierte rtSurvey-Funktionen. Sie verwenden Ausdrücke in den Spalten `calculate`, `constraint`, `relevant`, `required` und `default` Ihres XLSForm.

## Referenzierung von Feldwerten

Verwenden Sie `${fieldname}`, um auf den Wert eines anderen Feldes zu verweisen:

```
${age} > 18
```

Verwenden Sie `.` (ein einzelner Punkt), um auf den **Wert des aktuellen Feldes** zu verweisen — wird häufig in `constraint`-Ausdrücken verwendet:

```
. >= 0 and . <= 100
```

Verwenden Sie `..`, um auf die übergeordnete Gruppe zu verweisen (erweiterte Verwendung in Wiederholungen).

## Ausdruckssyntax

Ausdrücke folgen Standard-XPath-Regeln:

- **Zeichenketten** müssen in einfache Anführungszeichen eingeschlossen werden: `'yes'`
- **Zahlen** werden unverändert geschrieben: `42`, `3.14`
- **Boolesche** Ergebnisse werden für `relevant`, `required` und `constraint` verwendet — jeder nicht leere, nicht null Wert gilt als wahr
- Leerzeichen um Operatoren herum werden ignoriert

{{% alert icon=" " context="warning" %}}
Verwenden Sie immer gerade Anführungszeichen (`'` oder `"`) — niemals „typografische Anführungszeichen" (geschwungene Anführungszeichen). Rich-Text-Editoren konvertieren Anführungszeichen oft automatisch und können Ihre Ausdrücke zerstören.
{{% /alert %}}

## Abschnitte in diesem Kapitel

- **[Operatoren](operators)** — Vergleichsoperatoren (`=`, `!=`, `>`, `<`, `>=`, `<=`) und logische Operatoren (`and`, `or`, `not()`)
- **[Funktionen](functions)** — Zeichenketten-, Auswahl-, Zahl-, Datum/Uhrzeit-, Boolean-, Geo- und Hilfsfunktionen
- **[Referenzen](references)** — wie man Felder und Kontextwerte referenziert

## Schnellbeispiele

| Anwendungsfall | Ausdruck |
|----------------|----------|
| Anzeigen, wenn Alter über 18 | `${age} > 18` |
| Nur anzeigen, wenn "ja" ausgewählt wurde | `${consent} = 'yes'` |
| Erfordern, wenn ein anderes Feld nicht leer ist | `${name} != ''` |
| Gesamtsumme berechnen | `${adults} + ${children}` |
| Namen zusammensetzen | `concat(${first_name}, ' ', ${last_name})` |
| Heutiges Datum | `today()` |
| Prüfen, ob eine Option ausgewählt wurde | `selected(${interests}, 'sports')` |
