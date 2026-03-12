---
title: "Datei (File)"
description: "Datei-Fragen ermöglichen es den Befragten, Dateien als Teil ihrer Umfrageantworten hochzuladen."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Der `file`-Fragetyp in XLSForms und rtSurvey ermöglicht es Befragten, Dateien als Teil ihrer Umfrageantworten hochzuladen. Diese Funktion ist besonders nützlich für die Erfassung von Dokumenten, Bildern oder anderen für die Umfrage relevanten Dateitypen.

## Grundlegende XLSForm-Spezifikation

| type | name      | label                       |
|------|-----------|----------------------------|
| file | document  | Bitte laden Sie Ihr Dokument hoch |

Weitere Details zum grundlegenden `file`-Fragetyp finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Anwendungen

Datei-Fragen werden häufig verwendet für:

1. Sammlung von Belegen (z. B. Quittungen, Zertifikate)
2. Einholung visueller Beweise (z. B. Fotos von Bedingungen vor Ort)
3. Hochladen ausgefüllter Formulare oder Tabellen
4. Sammlung jeder Art von digitaler Datei, die für die Umfrage relevant ist

## Best Practices

1. Geben Sie klare Anweisungen dazu, welche Art von Datei hochgeladen werden soll und ob es Größenbeschränkungen gibt.
2. Berücksichtigen Sie Datenschutzaspekte und informieren Sie die Befragten darüber, wie ihre Dateien verwendet und gespeichert werden.
3. Achten Sie auf Dateigrößen und Speicherbeschränkungen, insbesondere bei Umfragen in Gebieten mit eingeschränkter Internetverbindung.
4. Geben Sie bei Bedarf die akzeptierten Dateiformate an.

## Beispielhafte Verwendung

Hier ist ein Beispiel dafür, wie Sie eine Datei-Frage in einer Umfrage verwenden könnten:

| type | name           | label                                      | hint                                        |
|------|----------------|--------------------------------------------|--------------------------------------------|
| file | receipt_upload | Bitte laden Sie ein Foto Ihrer Quittung hoch | Akzeptierte Formate: JPG, PNG. Max. Größe: 5MB |

## rtSurvey-Erweiterungen

Während die grundlegende XLSForm-Spezifikation für Datei-Fragen einfach ist, bietet rtSurvey möglicherweise zusätzliche Funktionen oder Anpassungen:

1. Dateityp-Beschränkungen (z. B. nur Bilder, nur PDFs)
2. Dateigrößenbeschränkungen
3. Möglichkeit zum Hochladen mehrerer Dateien
4. Integration mit dem Dateisystem des Geräts oder Cloud-Speicherdiensten

(Hinweis: Die spezifischen in rtSurvey verfügbaren Erweiterungen für Datei-Fragen müssten hier bestätigt und detailliert werden.)

## Datenhandhabung

Über diesen Fragetyp gesammelte Dateien werden in der Regel:

1. In ihrem Originalformat gespeichert
2. Zusammen mit anderen Umfragedaten gespeichert, oft in einem separaten Medienordner
3. Über die Umfrage-Management-Plattform zum Download und zur Analyse zugänglich gemacht

## Überlegungen zur Analyse

Berücksichtigen Sie bei der Verwendung von Datei-Fragen:

1. Wie die hochgeladenen Dateien verarbeitet und analysiert werden
2. Den zusätzlichen Speicherplatzbedarf für Dateianhänge
3. Datenschutz- und Datensicherheitsmaßnahmen für die Speicherung und Handhabung hochgeladener Dateien
4. Potenziellen Bedarf an spezialisierter Software zum Öffnen oder Analysieren bestimmter Dateitypen

## Einschränkungen

- Große Dateien können die Datenübertragung und den Speicherbedarf erheblich beeinflussen.
- Nicht alle Geräte haben möglicherweise einfachen Zugriff auf Dateien zum Hochladen.
- Die Analyse von Dateianhängen kann zeitaufwendiger sein als bei textbasierten Antworten.
- Es kann Kompatibilitätsprobleme mit bestimmten Dateitypen zwischen verschiedenen Systemen geben.
