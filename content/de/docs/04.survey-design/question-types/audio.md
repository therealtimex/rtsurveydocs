---
title: "Audio"
description: "Audio-Fragen ermöglichen es den Befragten, Audiodateien als Teil der Umfrage aufzunehmen und einzureichen."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Der Audio-Fragetyp in XLSForms und rtSurvey ermöglicht es Befragten, Audiodateien als Teil ihrer Umfrageantworten aufzunehmen und einzureichen. Diese Funktion ist besonders nützlich für die Erfassung von verbalen Antworten, Erfahrungsberichten oder umgebungsrelevanten Geräuschen für die Umfrage.

## Grundlegende XLSForm-Spezifikation

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| audio | voice_note  | Bitte nehmen Sie Ihre Kommentare auf |

Weitere Details zum grundlegenden Audio-Fragetyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungen

Audio-Fragen werden häufig verwendet für:

1. Erfassung verbaler Antworten auf offene Fragen
2. Aufnahme von Erfahrungsberichten oder persönlichen Geschichten
3. Dokumentation von Umgebungsgeräuschen oder Lärmpegeln
4. Sammlung von Sprachproben für Forschungszwecke
5. Ermöglichung detaillierter Erklärungen durch die Befragten

## Best Practices

1. Geben Sie klare Anweisungen dazu, was und wie lange aufgenommen werden soll.
2. Berücksichtigen Sie Datenschutzaspekte und informieren Sie die Befragten darüber, wie ihre Audioaufnahmen verwendet werden.
3. Achten Sie auf Dateigrößen und Speicherbeschränkungen, insbesondere bei Umfragen in Gebieten mit eingeschränkter Internetverbindung.
4. Testen Sie die Audioaufnahmefunktion auf verschiedenen Geräten, um die Kompatibilität sicherzustellen.

## Beispielhafte Verwendung

Hier ist ein Beispiel dafür, wie Sie eine Audio-Frage in einer Umfrage verwenden könnten:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| audio | feedback_audio | Bitte nehmen Sie Ihr Feedback zum Produkt auf        | Sprechen Sie deutlich für bis zu 60 Sekunden |

## rtSurvey-Erweiterungen

Während die grundlegende XLSForm-Spezifikation für Audio-Fragen einfach ist, bietet rtSurvey möglicherweise zusätzliche Funktionen oder Anpassungen:

1. Einstellung der maximalen Aufnahmedauer
2. Audioqualitätsoptionen (z. B. niedrig, mittel, hoch)
3. Wiedergabefunktion zur Überprüfung vor dem Absenden
4. Integration mit der nativen Audioaufnahme-App des Geräts

(Hinweis: Die spezifischen in rtSurvey verfügbaren Erweiterungen für Audio-Fragen müssten hier bestätigt und detailliert werden.)

## Einschränkungen

- Audiodateien können groß sein, was die Datenübertragung und Speicherung beeinflussen kann.
- Nicht alle Geräte unterstützen möglicherweise Audioaufnahmefunktionen.
- Eine Transkription von Audioantworten kann für die Analyse erforderlich sein, was zeitaufwendig sein kann.
- Bei der Erhebung von Sprachdaten können Datenschutzbedenken aufkommen.

## Datenhandhabung

Über diesen Fragetyp gesammelte Audiodateien werden in der Regel:

1. In einem gängigen Audioformat gespeichert (z. B. MP3, WAV)
2. Zusammen mit anderen Umfragedaten gespeichert
3. Über die Umfrage-Management-Plattform zur Wiedergabe und Analyse zugänglich gemacht

## Überlegungen zur Analyse

Berücksichtigen Sie bei der Verwendung von Audio-Fragen:

1. Wie die Audiodaten analysiert werden (z. B. manuelle Transkription, automatisierte Sprache-zu-Text-Umwandlung)
2. Den zusätzlichen Zeit- und Ressourcenaufwand für die Verarbeitung von Audioantworten
3. Datenschutz- und Datensicherheitsmaßnahmen für die Speicherung und Handhabung von Sprachaufnahmen
