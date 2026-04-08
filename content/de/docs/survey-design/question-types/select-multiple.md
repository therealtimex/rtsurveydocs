---
title: "Select_multiple"
description: "Select_multiple-Fragen ermöglichen es Befragten, eine oder mehrere Optionen aus einer vordefinierten Liste auszuwählen."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Der Fragetyp `select_multiple` zeigt eine Liste an, aus der der Befragte **eine oder mehrere Optionen** auswählen kann. Standardmäßig werden die Auswahlmöglichkeiten als Kontrollkästchen dargestellt. Der gespeicherte Wert ist eine **leerzeichengetrennte Liste** aller ausgewählten Werte.

## Grundlegende XLSForm-Spezifikation

**survey-Arbeitsblatt:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Welche Kulturen baut der Haushalt an? |

**choices-Arbeitsblatt:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Mais |
| crops | beans | Bohnen |
| crops | rice | Reis |
| crops | vegetables | Gemüse |
| crops | other | Sonstiges |

Weitere Details finden Sie in der [XLSForm-Spezifikation](https://xlsform.org/en/#question-types).

## Gespeichertes Datenformat

Die exportierte Spalte enthält eine leerzeichengetrennte Liste der ausgewählten Werte:

```
maize beans vegetables
```

Verwenden Sie die Funktion `selected()` — nicht `=` — wenn Sie select_multiple-Werte in Ausdrücken prüfen (siehe unten).

## Anwendungsbereiche

Select_multiple-Fragen werden verwendet für:

1. Erfassung mehrerer zutreffender Antworten (z. B. Einkommensquellen, angebaute Kulturen, Symptome)
2. Kontrollkästchen-Zustimmungspunkte (z. B. "Alle zutreffenden auswählen")
3. Sprach- oder Kompetenzkataloge
4. Jede Frage, bei der mehrere Antworten gleichzeitig gültig sind

## Erscheinungsoptionen

{{< table >}}
| Erscheinungsbild | Beschreibung |
|-----------------|-------------|
| *(keine)* | Standard-Kontrollkästchen, eines pro Zeile |
| `minimal` | Dropdown-Mehrfachauswahl-Widget |
| `compact` | Kompaktes Raster, Spalten passen sich der Bildschirmbreite an |
| `compact-N` | Kompaktes Raster mit N erzwungenen Spalten |
| `horizontal` | Auswahlmöglichkeiten horizontal in einer Reihe (Web) |
| `horizontal-compact` | Horizontal, kompakter Abstand (Web) |
| `label` | Zeigt nur Beschriftungen, keine Kontrollkästchen (zusammen mit `list-nolabel` verwenden) |
| `list-nolabel` | Zeigt nur Kontrollkästchen, keine Beschriftungen (zusammen mit `label` verwenden) |
| `columns(N)` | Anzeige in N Spalten (rtSurvey-Erweiterung) |
| `tagging` | Auswahlmöglichkeiten werden als pillenförmige Tag-Chips dargestellt |
| `boxtag` | Auswahlmöglichkeiten werden als gestaltete rechteckige Boxen dargestellt |
| `boxtag -search` | Boxtag-Layout mit Such-/Filtereingabe über den Boxen |
| `duolingo-style1` | Großes Kartenlayout — am besten für kurze Auswahllisten |
| `rating_box` | Rasterbasierte Bewertungsboxen |
| `choices-noshow` | Zeigt zunächst die ersten 10 Optionen; blendet den Rest auf Anfrage ein |
| `checkall` | Fügt oben in der Liste eine Option "Alle auswählen" hinzu |
| `max-items(N)` | Begrenzt die sichtbaren Auswahlmöglichkeiten auf N |
{{< /table >}}

### Beispiel: 3-Spalten-kompaktes Layout

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Alle beobachteten Symptome auswählen | compact-3 |

## Verwendung von `selected()` in Ausdrücken

Da der gespeicherte Wert eine leerzeichengetrennte Zeichenkette ist, **müssen** Sie `selected()` verwenden, um zu prüfen, ob eine bestimmte Option ausgewählt wurde. Die Verwendung von `=` funktioniert nicht korrekt.

### In `relevant`

Folgefrage nur anzeigen, wenn "Sonstiges" ausgewählt wurde:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Welche Kulturen werden angebaut? | |
| text | crops_other | Bitte andere Kulturen angeben | `selected(${crops_grown}, 'other')` |

### In `constraint`

Mindestens 2 Auswahlmöglichkeiten erfordern:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Mindestens 2 Punkte auswählen |

Auf maximal 3 begrenzen:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Nicht mehr als 3 Prioritäten auswählen |

### In `calculate` — Ausgewählte Beschriftungen verbinden

Kombinieren Sie `selected-at()`, `count-selected()` und `choice-label()` für eine lesbare Zusammenfassung:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Option "Keine der oben genannten" / exklusive Option

Ein verbreitetes Muster ist es, eine Option gegenseitig ausschließend mit allen anderen zu machen. Verwenden Sie eine `constraint`, um dies zu erzwingen:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Alle vorhandenen Probleme auswählen | `not(selected(., 'none') and count-selected(.) > 1)` | "Keine" kann nicht zusammen mit anderen Optionen ausgewählt werden |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Wasserknappheit |
| issues | roads | Schlechte Straßen |
| issues | health | Mangelnde Gesundheitsversorgung |
| issues | none | Keine der oben genannten |

## Auswahlen zählen und zusammenfassen

| Funktion | Beispiel | Ergebnis |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Anzahl der ausgewählten Optionen |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | wahr/falsch |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Erster ausgewählter Wert |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Beschriftung für einen Wert |

## Empfohlene Vorgehensweisen

1. Verwenden Sie immer `selected()` in `relevant`, `constraint` und `calculate` — niemals `=` oder `!=`.
2. Fügen Sie eine Einschränkung hinzu, um die maximale Anzahl der Auswahlen zu begrenzen, wenn das Fragedesign dies erfordert.
3. Fügen Sie eine Option "Keine" oder "Nicht zutreffend" hinzu, wenn null Auswahlen eine gültige Antwort ist.
4. Verwenden Sie bei langen Listen (15+ Optionen) `minimal` (Mehrfachauswahl-Dropdown), um übermäßiges Scrollen zu vermeiden.
5. Exportieren Sie Daten und verwenden Sie String-Splitting in Ihrem Analysetool — das leerzeichengetrennte Format erfordert eine Aufteilung vor der Auswertung.

## Einschränkungen

- Select_multiple-Werte können nicht direkt mit `=` verglichen werden. Verwenden Sie immer `selected()`.
- Das kompakte Erscheinungsbild wird bei sehr langen Auswahlbeschriftungen möglicherweise nicht gut gerendert.
- Bei der Filterung von Auswahlmöglichkeiten mit `choice_filter` gilt die Filterung für alle angezeigten Optionen, genau wie bei `select_one`.
