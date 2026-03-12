---
title: "Text"
description: "Fragetyp für freie Textantworten in rtSurvey"
# Translation provided by AI.
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

## Übersicht

Der Fragetyp "text" in rtSurvey ermöglicht freie Textantworten und bietet so Flexibilität bei der Erfassung verschiedener Arten von Textdaten. Er basiert auf der standardmäßigen XLSForm-Spezifikation, enthält jedoch rtSurvey-spezifische Erweiterungen für einen größeren Funktionsumfang.

## XLSForm-Spezifikation

In XLSForm wird der Fragetyp "text" wie folgt angegeben:

```
type: text
```

Weitere Details zur standardmäßigen XLSForm-Syntax finden Sie in der [offiziellen XLSForm-Dokumentation](https://xlsform.org/en/#question-types).

## rtSurvey-spezifische Erweiterungen

rtSurvey erweitert die Funktionalität des Fragetyps "text" durch verschiedene Darstellungsoptionen (`appearance`), insbesondere für die Zeiteingabe:

### Erweiterungen für die Zeiteingabe

- `appearance:` - Zeigt eine Uhr zur Auswahl von Stunden und Minuten an
- `appearance: inline` - Zeigt die Uhr als Symbol an
- `appearance: inline colors("0099FF")` - Zeigt die Uhr als Symbol mit anpassbarer Farbe an
- `appearance: inline-1line` - Zeigt die Uhr zur Auswahl in einem einzeiligen Format an
- `appearance: inline-1line-0000FF` - Einzeiliges Format mit anpassbarer Farbe
- `appearance: inline-1line colors("0000FF","FFFF00")` - Einzeiliges Format mit mehreren Farboptionen
- `appearance: inline-onlyresult` - Zeigt die Uhr als Symbol am Ende der Zeile an, das nach der Auswahl verschwindet
- `appearance: inline-onlyresult colors("0099FF")` - Wie oben, mit anpassbarer Symbolfarbe

### Erweiterungen für das Zeitformat

- `appearance: inline-[%3]` - Zeigt Millisekunden an
- `appearance: inline-[%S]` - Zeigt Sekunden an
- `appearance: inline-[%M]` - Zeigt Minuten an
- `appearance: inline-[%h]` - Zeigt Stunden an (12-Stunden-Format)
- `appearance: inline-[%H]` - Zeigt Stunden an (24-Stunden-Format)
- `appearance: inline-[%H-%M-%S]` - Zeigt die Zeit im Format HH-MM-SS an
- `appearance: inline-[%H:%M:%3]` - Zeigt die Zeit im Format HH:MM:Millisekunden an
- `appearance: inline-[%h:%M:%S]` - Zeigt die Zeit im 12-Stunden-Format mit Sekunden an
- `appearance: inline-[%H:%M]` - Zeigt die Zeit im 24-Stunden-Format an
- `appearance: inline-[%h:%M]` - Zeigt die Zeit im 12-Stunden-Format an
- `appearance: inline-[%M:%S]` - Zeigt Minuten und Sekunden an
- `appearance: inline-[%M:%3]` - Zeigt Minuten und Millisekunden an

## Datenformat

Textdaten werden als Text gespeichert und exportiert. Bei zeitbasierten Eingaben werden die Daten in einem textbasierten Datetime-Format gespeichert.

## Hinweise zur mobilen App

Der Fragetyp "text" wird einschließlich all seiner Varianten und Darstellungsformen auf den Plattformen iOS, Android und Web vollständig unterstützt.

## Verwandte Fragetypen

- Ganzzahlen (Integers)
- Datum und Uhrzeit (Datetime)

## Best Practices

- Verwenden Sie klare und prägnante Beschriftungen für Textfragen, um die Befragten anzuleiten.
- Erwägen Sie die Verwendung von Einschränkungen (Constraints) oder Validierungsregeln, um die Datenqualität sicherzustellen.
- Wählen Sie bei Zeiteingaben die passende Darstellungsoption basierend auf der für Ihre Umfrage erforderlichen Genauigkeit.

## Bekannte Einschränkungen

Derzeit sind für den Fragetyp "text" in rtSurvey keine Einschränkungen bekannt.

## Screenshots

[Hinweis: Fügen Sie relevante Screenshots ein, um verschiedene Darstellungsformen und Varianten des Fragetyps "text" zu veranschaulichen.]
