---
title: "Datetime, date, time (Datum und Uhrzeit)"
description: "Datetime-Fragen ermöglichen es den Befragten, sowohl Datum als auch Uhrzeit in einem einzigen Feld einzugeben."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Der `datetime`-Fragetyp in XLSForms und rtSurvey ermöglicht es Befragten, sowohl Datum als auch Uhrzeit in einem einzigen Feld einzugeben. Dieser Fragetyp ist nützlich, wenn Sie einen bestimmten Zeitpunkt erfassen müssen, der sowohl das Datum als auch die exakte Uhrzeit umfasst.

## Grundlegende XLSForm-Spezifikation

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Wann ist das Ereignis eingetreten?|

Weitere Details zum grundlegenden `datetime`-Fragetyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungen

`Datetime`-Fragen werden häufig verwendet für:

1. Aufzeichnung von Zeitstempeln von Ereignissen oder Beobachtungen
2. Planung von Terminen oder Besprechungen
3. Protokollierung von Start- und Endzeiten von Aktivitäten
4. Erfassung präziser Momente für zeitkritische Datenerhebungen

## rtSurvey-Erweiterungen

rtSurvey erweitert die Funktionalität von `datetime`-Fragen um verschiedene Darstellungsformen (Appearances) und Anpassungsoptionen:

### Darstellungsoptionen (Appearances)

- `(Standard)`: Zeigt den Kalender und die Uhr zur Auswahl von Datum und Uhrzeit an
- `inline`: Zeigt den Kalender und die Uhr als Symbole an
- `inline-1line`: Zeigt den Kalender und die Uhr zur Auswahl in einem einzeiligen Format an
- `inline-onlyresult`: Zeigt den Kalender und die Uhr als Symbole am Ende der Zeile an; Symbole verschwinden nach der Auswahl

### Farbanpassung

Sie können die Farbe der Kalender- und Uhr-Symbole mit der Funktion `colors()` anpassen:

- `inline colors("0099FF")`: Zeigt Symbole mit benutzerdefinierter Farbe an
- `inline-1line-0000FF`: Anzeige im einzeiligen Format mit benutzerdefinierter Farbe
- `inline-1line colors("0000FF","FFFF00")`: Anzeige im einzeiligen Format mit mehreren benutzerdefinierten Farben
- `inline-onlyresult colors("0099FF")`: Zeigt Symbole an, die nach der Auswahl verschwinden, mit benutzerdefinierter Farbe

### Benutzerdefinierte Datums- und Zeitformate

rtSurvey ermöglicht benutzerdefinierte Datums- und Zeitformate durch eine spezielle Syntax:

- `inline-[%Y-%m-%d %H:%M:%S]`: Beispiel für ein benutzerdefiniertes Format (Jahr-Monat-Tag Stunde:Minute:Sekunde)
- `inline-[%d/%m/%Y %I:%M %p]`: Beispiel für ein benutzerdefiniertes Format (Tag/Monat/Jahr Stunde:Minute AM/PM)

## Beispielhafte Verwendung

Hier ist ein Beispiel dafür, wie Sie eine `datetime`-Frage in einer Umfrage verwenden könnten:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Wann ist der Vorfall eingetreten?          | inline-[%d/%m/%Y %I:%M %p]  |

## Best Practices

1. Geben Sie klare Anweisungen zum erwarteten Datums- und Zeitformat.
2. Erwägen Sie die Verwendung der `inline`-Darstellung für eine kompaktere Anzeige.
3. Verwenden Sie benutzerdefinierte Formate, wenn Sie spezifische Datums- und Zeitkomponenten oder Formatierungen benötigen.
4. Achten Sie auf Zeitzonen, wenn Sie Datums- und Zeitdaten über verschiedene Regionen hinweg sammeln.

## Einschränkungen

- Einige Darstellungsformen oder benutzerdefinierte Formate werden möglicherweise nicht auf allen Geräten oder Plattformen unterstützt.
- Benutzer benötigen möglicherweise Hilfe bei der korrekten Eingabe von Datum und Uhrzeit, insbesondere bei benutzerdefinierten Formaten.
- Zeitzonenunterschiede können die Datenanalyse erschweren, wenn sie nicht ordnungsgemäß berücksichtigt werden.
