---
title: "Erscheinungsbild"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Die Spalte `appearance` in rtSurvey ermöglicht es Ihnen, die visuelle Darstellung und das Verhalten von Fragen in Ihren Umfragen anzupassen. Diese Funktion verbessert die Benutzererfahrung und kann die Effizienz der Datenerfassung erheblich steigern. rtSurvey unterstützt Standard-XLSForm-Erscheinungsattribute und erweitert diese um zusätzliche Optionen.

## Standard-XLSForm-Erscheinungsattribute

rtSurvey unterstützt die folgenden Standard-XLSForm-Erscheinungsattribute:

| Erscheinungsattribut | Fragetypen | Beschreibung |
|----------------------|----------------|-------------|
| multiline | text | Erstellt ein mehrzeiliges Textfeld (am besten für Web-Clients) |
| minimal | select_one, select_multiple | Zeigt Auswahlmöglichkeiten in einem Dropdown-Menü an |
| quick | select_one | Springt nach der Auswahl automatisch zur nächsten Frage (nur mobil) |
| no-calendar | date | Unterdrückt die Kalenderanzeige (nur mobil) |
| month-year | date | Ermöglicht nur die Auswahl von Monat und Jahr |
| year | date | Ermöglicht nur die Auswahl des Jahres |
| horizontal-compact | select_one, select_multiple | Zeigt Auswahlmöglichkeiten horizontal an (nur Web) |
| horizontal | select_one, select_multiple | Zeigt Auswahlmöglichkeiten horizontal in Spalten an (nur Web) |
| likert | select_one | Präsentiert Auswahlmöglichkeiten als Likert-Skala |
| compact | select_one, select_multiple | Zeigt Auswahlmöglichkeiten nebeneinander mit minimalem Abstand an |
| quickcompact | select_one | Kombiniert kompakte Anzeige mit automatischem Weiterspringen (nur mobil) |
| field-list | groups | Zeigt die gesamte Gruppe auf einem Bildschirm an (nur mobil) |
| label | select_one, select_multiple | Zeigt Auswahlbeschriftungen ohne Eingabefelder an |
| list-nolabel | select_one, select_multiple | Zeigt Eingabefelder ohne Beschriftungen an (zusammen mit `label` verwenden) |
| table-list | groups | Zeigt Fragen in einem Tabellenformat an |
| signature | image | Ermöglicht die Erfassung einer Unterschrift (nur mobil) |
| draw | image | Ermöglicht Freihandzeichnen (nur mobil) |
| map, quick map | select_one, select_one_from_file | Ermöglicht die Auswahl aus Kartenmerkmalen |

## Best Practices für die Verwendung des Erscheinungsbilds

1. **Konsistenz**: Verwenden Sie Erscheinungsattribute konsistent in Ihrer gesamten Umfrage für ein einheitliches Erscheinungsbild.
2. **Mobil vs. Web**: Berücksichtigen Sie, wie das Erscheinungsbild auf verschiedenen Geräten und Plattformen gerendert wird.
3. **Leistung**: Seien Sie vorsichtig mit Erscheinungsattributen, die das Laden des Formulars verlangsamen könnten (z. B. `table-list` bei großen Gruppen).
4. **Benutzererfahrung**: Wählen Sie Darstellungen, die die Dateneingabe für die Befragten einfacher und intuitiver machen.
5. **Testen**: Testen Sie Ihr Formular immer auf den Zielgeräten, um sicherzustellen, dass die Darstellungen wie erwartet funktionieren.

## Fortgeschrittene Techniken

### Kombinieren von Erscheinungsbildern

Einige Erscheinungsattribute können für komplexere Layouts kombiniert werden:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Auswahl: | minimal compact |
```

### Dynamische Erscheinungsbilder

rtSurvey ermöglicht dynamische Änderungen des Erscheinungsbilds basierend auf der Formularlogik:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Zeit eingeben: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Überlegungen zur mobilen App

- Einige Darstellungen (z. B. `quick`, `signature`) sind spezifisch für mobile Geräte.
- Testen Sie gründlich auf Android und iOS, um ein konsistentes Verhalten sicherzustellen.

## Bekannte Einschränkungen

- Komplexe Erscheinungsbilder werden möglicherweise nicht auf allen Plattformen identisch gerendert.
- Einige fortgeschrittene rtSurvey-Erscheinungsbilder werden im Offline-Modus möglicherweise nicht unterstützt.

## Fehlerbehebung bei Darstellungsproblemen

1. **Darstellung nicht angewendet**: Überprüfen Sie die Spalte appearance auf Tippfehler.
2. **Inkonsistentes Rendering**: Überprüfen Sie die Kompatibilität mit dem Fragetyp und der Plattform.
3. **Leistungsprobleme**: Erwägen Sie die Vereinfachung komplexer Darstellungen, insbesondere bei umfangreichen Umfragen.
