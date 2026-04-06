---
title: "Fragetypen"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey unterstützt alle Standard-XLSForm-Fragetypen sowie mehrere Erweiterungen. Jeder Fragetyp legt fest, welche Art von Daten erfasst wird und wie das Eingabe-Widget auf dem Gerät dargestellt wird.

Um den Fragetyp festzulegen, geben Sie den Typnamen in die Spalte `type` des **survey**-Arbeitsblatts in Ihrem XLSForm ein.

## Texteingabe

| Typ | Beschreibung |
|-----|-------------|
| [text](text) | Freitext-Antwort — alle Zeichen erlaubt |
| [integer](integer) | Ganzzahl (keine Dezimalstellen) |
| [decimal](decimal) | Zahl mit Dezimalstellen |
| [range](range) | Zahl, die über einen Schieberegler innerhalb eines definierten Min/Max-Bereichs gewählt wird |

## Auswahl

| Typ | Beschreibung |
|-----|-------------|
| [select_one listname](select-one) | Genau eine Option aus einer Liste auswählen |
| [select_multiple listname](select-multiple) | Eine oder mehrere Optionen aus einer Liste auswählen |
| [select_one_from_file filename](select-one-from-file) | Eine Option aus einer externen CSV-Datei auswählen |
| [rank listname](rank) | Auswahlmöglichkeiten nach Präferenz oder Priorität ordnen |

## Datum und Uhrzeit

| Typ | Beschreibung |
|-----|-------------|
| [date](date) | Kalenderdatum (Jahr, Monat, Tag) |
| [time](time) | Uhrzeit (Stunden, Minuten) |
| [datetime](datetime-date-time) | Kombiniertes Datum und Uhrzeit |

## Standort

| Typ | Beschreibung |
|-----|-------------|
| [geopoint](geopoint) | Einzelne GPS-Koordinate (Breitengrad, Längengrad, Höhe, Genauigkeit) |
| [geotrace](geotrace) | Ein Pfad — Reihe von GPS-Punkten, die eine Linie bilden |
| [geoshape](geoshape) | Eine Fläche — geschlossenes Polygon aus GPS-Punkten |

## Medien

| Typ | Beschreibung |
|-----|-------------|
| [image](image) | Fotoaufnahme oder Bild-Upload |
| [audio](audio) | Audioaufnahme |
| [video](video) | Videoaufnahme |
| [file](file) | Allgemeiner Datei-Upload (PDF, Dokument usw.) |

## Sonstige

| Typ | Beschreibung |
|-----|-------------|
| [barcode](barcode) | Barcode oder QR-Code scannen |
| [note](note) | Schreibgeschützter Anzeigetext — zeigt Anweisungen oder berechnete Zusammenfassungen |
| [calculate](calculate) | Verborgenes Feld, das einen berechneten Wert speichert |
| [hidden](hidden) | Verborgenes Feld, das einen statischen oder vorausgefüllten Wert speichert |
| [trigger / acknowledge](trigger) | Ein Kontrollkästchen, das der Interviewer aktivieren muss, um das Lesen einer Aussage zu bestätigen |
| [meta](meta) | Automatische Metadaten: Zeitstempel, Geräte-ID, Interviewer-Informationen |

## Zusammenspiel von Typ und Erscheinungsbild

Die Spalte `type` bestimmt, **welche Daten erfasst werden**. Die Spalte `appearance` steuert, **wie das Widget aussieht**. Viele Typen unterstützen mehrere Erscheinungsbilder — beispielsweise kann `select_one` als Optionsfelder, Dropdown-Menü, Likert-Skala oder kompaktes Raster dargestellt werden.

Unter [Erscheinungsbild](../appearance) finden Sie die vollständige Liste der Optionen.
