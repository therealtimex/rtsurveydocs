---
title: "Text"
description: "Fragetyp für freie Textantworten in rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Der Fragetyp `text` erfasst eine freie Textantwort — jede beliebige Zeichenkette. Er ist der flexibelste Eingabetyp und wird für Namen, Adressen, Beschreibungen, Codes und alles verwendet, was nicht in einen spezifischeren Typ passt.

rtSurvey erweitert `text` zusätzlich mit **Zeiteingabe-Widgets**, die eine präzise Zeiteingabe über eine Uhranzeige ermöglichen.

## Grundlegende XLSForm-Spezifikation

| type | name | label |
|------|------|-------|
| text | respondent_name | Vollständiger Name des Befragten |
| text | address | Wohnadresse |

Weitere Details zum Standard-XLSForm-Texttyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungsbereiche

Text-Fragen werden verwendet für:

1. Namen, Adressen, freie Beschreibungen
2. Offene Kommentare oder Rückmeldungen
3. Codes, IDs oder Referenznummern, die nicht in integer/decimal passen
4. Erfassung von Zeitwerten mit den Zeiteingabe-Erweiterungen von rtSurvey
5. Autovervollständigungs-Textfelder (über `search-autocomplete-noedit-v2()`)

## Standard-Erscheinungsoptionen

| Erscheinungsbild | Beschreibung |
|-----------------|-------------|
| *(keine)* | Einzeiliges Texteingabefeld |
| `multiline` | Mehrzeiliges Textfeld — am besten für längere Freitexte im Web |
| `richtext` | Rich-Text-Editor — Symbolleiste mit Fett, Kursiv, Listen und Links |
| `typingtest` | Tipptest-Oberfläche — zeigt einen Text und misst Tippgeschwindigkeit und -genauigkeit |

## rtSurvey-Zeiteingabe-Erweiterungen

rtSurvey erweitert `text` mit einem **Uhr-Picker-Widget** zur Erfassung von Zeitwerten. Diese Erscheinungsoptionen zeigen ein Uhrsymbol an, das der Interviewer antippen kann, um Stunden, Minuten, Sekunden oder Millisekunden auszuwählen.

### Erscheinungsvarianten

| Erscheinungsbild | Beschreibung |
|-----------------|-------------|
| `inline` | Uhrsymbol neben dem Feld angezeigt |
| `inline colors("RRGGBB")` | Uhrsymbol mit benutzerdefinierter Hex-Farbe |
| `inline-1line` | Uhr im kompakten einzeiligen Format dargestellt |
| `inline-1line-RRGGBB` | Einzeiliges Format mit benutzerdefinierter Symbolfarbe (Hex, ohne `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Einzeiliges Format mit zwei Farben |
| `inline-onlyresult` | Uhrsymbol verschwindet nach der Auswahl; nur der Wert wird angezeigt |
| `inline-onlyresult colors("RRGGBB")` | Gleich wie oben, mit benutzerdefinierter Symbolfarbe |

### Zeitformat-Token

Hängen Sie eine Formatzeichenkette in eckigen Klammern an, um zu steuern, welche Zeitkomponenten angezeigt werden:

| Formatzeichenkette | Zeigt an |
|-------------------|---------|
| `inline-[%H:%M]` | Stunden und Minuten (24-Stunden-Format) |
| `inline-[%h:%M]` | Stunden und Minuten (12-Stunden-Format) |
| `inline-[%H:%M:%S]` | Stunden, Minuten, Sekunden (24-Stunden-Format) |
| `inline-[%h:%M:%S]` | Stunden, Minuten, Sekunden (12-Stunden-Format) |
| `inline-[%H:%M:%3]` | Stunden, Minuten, Millisekunden |
| `inline-[%M:%S]` | Nur Minuten und Sekunden |
| `inline-[%M:%3]` | Nur Minuten und Millisekunden |
| `inline-[%S]` | Nur Sekunden |
| `inline-[%3]` | Nur Millisekunden |
| `inline-[%H]` | Nur Stunden (24-Stunden-Format) |
| `inline-[%h]` | Nur Stunden (12-Stunden-Format) |

### Beispiel: Aufgabendauer in Minuten und Sekunden aufzeichnen

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Benötigte Zeit für die Aufgabe | `inline-[%M:%S]` |

### Beispiel: Ereigniszeit im 24-Stunden-Format mit benutzerdefinierter Farbe aufzeichnen

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Ereigniszeitpunkt | `inline-1line colors("0099FF")` |

## Datenformat

Textdaten werden als einfache Zeichenkette gespeichert und exportiert. Bei zeitbasierten Eingaben mit dem Inline-Uhr-Widget wird der Wert im Format der gewählten Formatzeichenkette gespeichert (z. B. `14:32` für `%H:%M`).

## Einschränkungen und Validierung

Wenden Sie Einschränkungen an, um Format, Länge oder Muster zu erzwingen:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Vollständiger Name | `string-length(.) >= 2` | Name muss mindestens 2 Zeichen lang sein |
| text | code | Referenzcode | `regex(., '^[A-Z]{2}[0-9]{4}$')` | 2 Großbuchstaben gefolgt von 4 Ziffern eingeben |
| text | phone | Telefonnummer | `regex(., '^[0-9]{9,15}$')` | Gültige Telefonnummer eingeben |

## Empfohlene Vorgehensweisen

1. Verwenden Sie spezifischere Typen (`integer`, `decimal`, `date`), wenn die Daten eine bekannte Struktur haben — dies verhindert ungültige Einträge und vereinfacht die Analyse.
2. Fügen Sie `constraint` mit `string-length()` oder `regex()` hinzu, um Codes oder IDs zu validieren.
3. Verwenden Sie die Erscheinung `multiline` bei offenen Fragen, bei denen Befragte mehrere Sätze schreiben könnten.
4. Wählen Sie bei der Zeiterfassung die Zeitformat-Token, die der für Ihre Analyse erforderlichen Präzision entsprechen — das Erfassen von Millisekunden, wenn nur Minuten benötigt werden, belastet die Interviewer unnötig.

## Plattform-Unterstützung

Der Fragetyp text und alle Zeiteingabe-Erscheinungsbilder werden auf iOS-, Android- und Web-Plattformen unterstützt.

## Einschränkungen

- Textantworten sind freigestellt — es gibt keine eingebaute Rechtschreibprüfung oder Wortschatzeinschränkung über Regex-Muster hinaus.
- Das Inline-Uhr-Widget ist eine rtSurvey-Erweiterung und ist nicht Teil der Standard-XLSForm-Spezifikation.
