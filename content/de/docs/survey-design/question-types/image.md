---
title: "Image (Bild)"
description: "Image-Fragen ermöglichen es den Befragten, Fotos als Teil der Umfrage aufzunehmen und einzureichen."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Der `image`-Fragetyp in XLSForms und rtSurvey ermöglicht es Befragten, Fotos als Teil ihrer Umfrageantworten aufzunehmen und einzureichen. Diese Funktion ist besonders nützlich für die Erfassung visueller Daten, die Dokumentation von Beobachtungen oder die Erbringung von Nachweisen bei Außendiensteinsätzen.

## Grundlegende XLSForm-Spezifikation

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Machen Sie ein Foto vom Standort|

Weitere Details zum grundlegenden `image`-Fragetyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungen

`Image`-Fragen werden häufig verwendet für:

1. Dokumentation von Bedingungen vor Ort oder Beobachtungen
2. Erfassung visueller Beweise in Forschungsstudien
3. Sammlung von Vorher-Nachher-Fotos bei Wirkungsanalysen
4. Überprüfung des Abschlusses von Aufgaben oder der Anwesenheit an Standorten
5. Sammlung visueller Daten für die Fernanalyse

## Best Practices

1. Geben Sie klare Anweisungen dazu, was fotografiert werden soll.
2. Berücksichtigen Sie Datenschutzaspekte und informieren Sie die Befragten darüber, wie ihre Fotos verwendet werden.
3. Achten Sie auf Dateigrößen und Speicherbeschränkungen, insbesondere bei Umfragen in Gebieten mit eingeschränkter Internetverbindung.
4. Stellen Sie sicher, dass das Gerät über ausreichend Speicherplatz verfügt und die Kameraberechtigungen erteilt sind.

## Beispielhafte Verwendung

Hier ist ein Beispiel dafür, wie Sie eine `image`-Frage in einer Umfrage verwenden könnten:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Machen Sie ein Foto vom Ladeneingang       | Stellen Sie sicher, dass der Ladenname deutlich sichtbar ist |

## rtSurvey-Erweiterungen

Während die grundlegende XLSForm-Spezifikation für `image`-Fragen einfach ist, bietet rtSurvey möglicherweise zusätzliche Funktionen oder Anpassungen:

1. Bildqualitätseinstellungen (z. B. niedrige, mittlere, hohe Auflösung)
2. Option zum Hinzufügen von Bildunterschriften oder Tags zu Bildern
3. Aufnahme mehrerer Bilder für eine einzige Frage
4. Integration mit der nativen Kamera-App oder der Galerie des Geräts

(Hinweis: Die spezifischen in rtSurvey verfügbaren Erweiterungen für `image`-Fragen müssten hier bestätigt und detailliert werden.)

## Datenhandhabung

Über diesen Fragetyp gesammelte Bilder werden in der Regel:

1. In einem gängigen Bildformat gespeichert (z. B. JPG, PNG)
2. Zusammen mit anderen Umfragedaten gespeichert, oft in einem separaten Medienordner
3. Über die Umfrage-Management-Plattform zum Betrachten und zur Analyse zugänglich gemacht

## Überlegungen zur Analyse

Berücksichtigen Sie bei der Verwendung von `image`-Fragen:

1. Wie die Bilder analysiert werden (z. B. manuelle Überprüfung, automatisierte Bildanalyse)
2. Den zusätzlichen Speicherplatzbedarf für Bilddateien
3. Datenschutz- und Datensicherheitsmaßnahmen für die Speicherung und Handhabung von Fotos
4. Potenzielle Notwendigkeit von Bildbearbeitungs- oder Organisationswerkzeugen in der Analysephase

## Einschränkungen

- Bilddateien können groß sein, was sich auf die Datenübertragung und Speicherung auswirken kann.
- Nicht alle Geräte verfügen über hochwertige Kameras oder ausreichend Speicherplatz.
- Die Analyse einer großen Anzahl von Bildern kann zeitaufwendig sein.
- Beim Aufnehmen von Bildern können Datenschutzbedenken aufkommen, insbesondere im öffentlichen Raum.

## rtSurvey-Bild-Erweiterungen

### watermark()

Das Erscheinungsbild `watermark()` legt ein Text-Wasserzeichen auf mit diesem Feld aufgenommene Fotos. Das Wasserzeichen enthält typischerweise Metadaten wie den Namen des Interviewers, Datum/Uhrzeit oder GPS-Koordinaten, die direkt vor dem Speichern auf das Bild gestempelt werden.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Foto vom Standort aufnehmen | `watermark("${enumerator_id} ${today()}")` |

Das Argument von `watermark()` ist ein XPath-Ausdruck, der zum Zeitpunkt der Aufnahme ausgewertet wird. Die resultierende Zeichenkette wird als Wasserzeichen-Text gerendert.

### editable

Das Erscheinungsbild `editable` ermöglicht es dem Befragten, das aufgenommene Foto nach der Aufnahme zu kommentieren oder darauf zu zeichnen. Eine Zeichenwerkzeugleiste erscheint über dem Bild.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Foto aufnehmen und Problembereiche markieren | editable |

{{% alert icon=" " context="info" %}}
`editable` kann mit `watermark()` kombiniert werden: `appearance: editable watermark("${id}")`
{{% /alert %}}
