---
title: "Auswahl aus Datei"
description: "select_one_from_file und select_multiple_from_file laden Auswahlmöglichkeiten dynamisch aus einer externen CSV- oder XML-Datei, die dem Formular beigefügt ist."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` und `select_multiple_from_file` funktionieren wie `select_one` und `select_multiple`, aber anstatt die Auswahlmöglichkeiten im **choices-Arbeitsblatt** zu definieren, werden die Auswahlmöglichkeiten aus einer **externen CSV- oder XML-Datei** geladen, die dem Formular beigefügt ist. Dies ist nützlich, wenn Ihre Auswahlliste sehr lang ist, sich häufig ändert oder aktualisiert werden muss, ohne das gesamte Formular neu zu erstellen.

## Grundlegende XLSForm-Spezifikation

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Gesundheitseinrichtung auswählen |
| select_multiple_from_file crops.csv | crops | Welche Kulturen baut der Haushalt an? |

Der Dateiname nach dem Typnamen muss mit dem Namen der Datei übereinstimmen, die Sie beim Hochladen des Formulars anhängen.

## CSV-Dateiformat

Ihre CSV-Datei muss mindestens zwei Spalten haben: `name` (der gespeicherte Wert) und `label` (der angezeigte Text). Sie können beliebig viele zusätzliche Spalten für die Filterung hinzufügen.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Auswahlmöglichkeiten filtern

Verwenden Sie die Spalte `choice_filter`, um nur die Auswahlmöglichkeiten anzuzeigen, die dem aktuellen Kontext entsprechen. Referenzieren Sie CSV-Spalten direkt mit ihrem Spaltennamen (ohne `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Bezirk auswählen | |
| select_one_from_file health_facilities.csv | facility | Einrichtung auswählen | district = ${district} |

In diesem Beispiel werden nur Einrichtungen im ausgewählten Bezirk angezeigt. Das `district` in `choice_filter` bezieht sich auf die Spalte `district` in der CSV-Datei; `${district}` bezieht sich auf das Formularfeld namens `district`.

## Anwendungsbereiche

Auswahl-aus-Datei-Fragen werden häufig verwendet für:

1. **Lange Auswahllisten** — Gesundheitseinrichtungen, Schulen, Dörfer, Artenlisten (Hunderte oder Tausende von Einträgen)
2. **Häufig aktualisierte Listen** — wenn sich die Hauptliste zwischen Umfragerunden ändert, nur die CSV aktualisieren, ohne das Formular neu zu erstellen
3. **Gemeinsame Referenzdaten** — eine CSV-Datei, die über mehrere Formulare hinweg verwendet wird
4. **Gefilterte kaskadierende Auswahlmenüs** — alle Regionen/Bezirke/Dörfer in einer Datei laden, dann nach der übergeordneten Auswahl filtern

## Datei anhängen

Wenn Sie Ihr Formular in rtSurvey hochladen, fügen Sie die CSV-Datei als **Medienanhang** hinzu. Der Dateiname in der Formulardefinition muss genau mit dem Dateinamen des Anhangs übereinstimmen.

{{% alert icon=" " context="warning" %}}
Dateinamen unterscheiden zwischen Groß- und Kleinschreibung. `Health_Facilities.csv` und `health_facilities.csv` werden als unterschiedliche Dateien behandelt.
{{% /alert %}}

## Verwendung von `choice-label()` mit from-file

Um die Beschriftung einer ausgewählten Auswahlmöglichkeit in einer Notiz oder einem Berechnungsfeld anzuzeigen:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Einrichtung auswählen | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Ausgewählte Einrichtung: ${facility_label} | |

## Empfohlene Vorgehensweisen

1. Halten Sie Ihre CSV-Dateien unter 5.000 Zeilen für gute Leistung auf mobilen Geräten.
2. Fügen Sie immer eine `name`- und `label`-Spalte hinzu — zusätzliche Spalten sind optional.
3. Verwenden Sie bei kaskadierenden Auswahlmenüs eine einzige CSV mit einer übergeordneten Spalte und filtern Sie mit `choice_filter`.
4. Versionieren Sie Ihre CSV-Dateinamen (z. B. `facilities_v3.csv`), wenn Sie grundlegende Änderungen an der Spaltenstruktur vornehmen.
5. Testen Sie Filterausdrücke sorgfältig — ein Tippfehler in `choice_filter` zeigt stillschweigend keine Auswahlmöglichkeiten an.

## Einschränkungen

- Sehr große CSV-Dateien (10.000+ Zeilen) können das Laden des Formulars verlangsamen, insbesondere auf Low-End-Geräten.
- CSV-Dateien müssen zusammen mit dem Formular hochgeladen werden — sie können nicht zur Laufzeit von einer URL abgerufen werden (verwenden Sie `search()` oder `pulldata()` für dynamische Nachschlagvorgänge).
- `select_multiple_from_file` wird von Clients weniger häufig unterstützt — überprüfen Sie die Kompatibilität vor der Verwendung.

## Vergleich mit `search()`

| | `select_one_from_file` | `search()`-Erscheinungsbild |
|--|----------------------|----------------------|
| Auswahlquelle | Angehängte CSV/XML-Datei | Serverseitige Datenbankabfrage |
| Offline nutzbar | Ja (Datei ist gebündelt) | Erfordert Konnektivität |
| Anzahl der Auswahlmöglichkeiten | Durch Gerätespeicher begrenzt | Unbegrenzt (paginiert) |
| Echtzeitdaten | Nein | Ja |

Für große, häufig wechselnde oder serverseitige Datensätze siehe [Dynamische Suche](../advanced-extension/dynamic-search).
