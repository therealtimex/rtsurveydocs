---
title: "Video"
description: "Video-Fragen ermöglichen es den Befragten, Videodateien als Teil der Umfrage aufzunehmen und einzureichen."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Der `video`-Fragetyp in XLSForms und rtSurvey ermöglicht es Befragten, Videodateien als Teil ihrer Umfrageantworten aufzunehmen und einzureichen. Diese Funktion ist besonders nützlich für die Erfassung visueller Beweise, Demonstrationen oder Erfahrungsberichte im Rahmen der Umfrage.

## Grundlegende XLSForm-Spezifikation

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| video | demo_video  | Bitte nehmen Sie ein kurzes Demo-Video auf |

Weitere Details zum grundlegenden `video`-Fragetyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungen

Video-Fragen werden häufig verwendet für:

1. Erfassung visueller Beweise bei Außendiensteinsätzen
2. Aufzeichnung von Produktdemonstrationen oder Nutzungsszenarien
3. Erfassung von Video-Testimonials
4. Dokumentation von Prozessen oder Verfahren
5. Ermöglichen detaillierter visueller Erklärungen durch die Befragten

## Best Practices

1. Geben Sie klare Anweisungen dazu, was und wie lange aufgenommen werden soll.
2. Berücksichtigen Sie Datenschutzaspekte und informieren Sie die Befragten darüber, wie ihr Video verwendet wird.
3. Achten Sie auf Dateigrößen und Speicherbeschränkungen, insbesondere bei Umfragen in Gebieten mit eingeschränkter Internetverbindung.
4. Testen Sie die Videofunktion auf verschiedenen Geräten, um die Kompatibilität sicherzustellen.
5. Erwägen Sie, die gewünschte Videoqualität oder Auflösung in den Anweisungen anzugeben.

## Beispielhafte Verwendung

Hier ist ein Beispiel dafür, wie Sie eine Video-Frage in einer Umfrage verwenden könnten:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| video | product_demo   | Bitte nehmen Sie eine kurze Demo zur Nutzung des Produkts auf | Nehmen Sie 30-60 Sekunden auf und zeigen Sie die wichtigsten Funktionen |

## rtSurvey-Erweiterungen

Während die grundlegende XLSForm-Spezifikation für Video-Fragen einfach ist, bietet rtSurvey möglicherweise zusätzliche Funktionen oder Anpassungen:

1. Einstellung der maximalen Aufnahmedauer
2. Optionen für die Videoqualität (z. B. niedrig, mittel, hoch)
3. Wiedergabefunktion zur Überprüfung vor dem Absenden
4. Integration mit der nativen Video-App des Geräts
5. Option zum Hochladen vorhandener Videodateien anstelle einer Neuaufnahme

(Hinweis: Die spezifischen in rtSurvey verfügbaren Erweiterungen für Video-Fragen müssten hier bestätigt und detailliert werden.)

## Einschränkungen

- Videodateien können sehr groß sein, was die Datenübertragung und Speicherung erheblich beeinflussen kann.
- Nicht alle Geräte unterstützen Videoaufnahmen oder verfügen über begrenzten Speicherplatz.
- Die Analyse von Videoantworten kann zeitaufwendig sein und spezialisierte Software erfordern.
- Datenschutzbedenken können bei der Erhebung von Videodaten ausgeprägter sein.

## Datenhandhabung

Über diesen Fragetyp gesammelte Videodateien werden in der Regel:

1. In einem gängigen Videoformat gespeichert (z. B. MP4, MOV)
2. Zusammen mit anderen Umfragedaten gespeichert, oft in einem separaten Medienordner
3. Über die Umfrage-Management-Plattform zur Wiedergabe und Analyse zugänglich gemacht

## Überlegungen zur Analyse

Berücksichtigen Sie bei der Verwendung von Video-Fragen:

1. Wie die Videodaten analysiert werden (z. B. manuelle Überprüfung, automatisierte Videoanalyse)
2. Den zusätzlichen Zeit- und Ressourcenaufwand für die Verarbeitung von Videoantworten
3. Datenschutz- und Datensicherheitsmaßnahmen für die Speicherung und Handhabung von Videoaufnahmen
4. Potenzielle Notwendigkeit von Videobearbeitungs- oder Kompilierungswerkzeugen in der Analysephase
