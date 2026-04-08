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

Die Spalte `appearance` in rtSurvey ermöglicht es Ihnen, die visuelle Darstellung und das Verhalten von Fragen in Ihren Umfragen anzupassen. Diese Funktion verbessert die Benutzererfahrung und kann die Effizienz der Datenerhebung erheblich steigern. rtSurvey unterstützt Standard-XLSForm-Erscheinungsattribute und erweitert diese um zusätzliche Optionen.

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

## Empfohlene Vorgehensweisen für die Verwendung des Erscheinungsbilds

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

## Erweiterte rtSurvey-Erscheinungsattribute

Zusätzlich zu den Standard-XLSForm-Erscheinungsbildern unterstützt rtSurvey folgende plattformspezifische Optionen:

### Daten- und Anzeigesteuerung

| Erscheinungsattribut | Fragetypen | Beschreibung |
|----------------------|----------------|-------------|
| `invisible` | beliebig | Blendet das Feld aus der Ansicht aus, erfasst oder berechnet seinen Wert aber weiterhin. Anders als der Typ `hidden` — das Feld nimmt weiterhin an der Logik teil. |
| `displaytitle` | beliebig | Erzwingt die Anzeige der Feldbeschriftung/des Titels, auch wenn dieser normalerweise unterdrückt würde. |
| `autopull` | select_one, select_multiple | Ruft automatisch externe Daten ab, um Auswahlmöglichkeiten zu befüllen, wenn das Formular geladen wird oder sich ein Auslöserfeld ändert. |
| `floating_hint` | text, integer, decimal | Zeigt den Hinweistext als schwebende Beschriftung über dem Eingabefeld an, statt darunter. |
| `calculate-button` | calculate | Fügt eine sichtbare Schaltfläche hinzu, die bei Bedarf eine Neuberechnung des Feldes auslöst, statt automatisch zu berechnen. |

### Layout

| Erscheinungsattribut | Fragetypen | Beschreibung |
|----------------------|----------------|-------------|
| `1screen` | group | Erzwingt die Anzeige der gesamten Gruppe auf einem einzigen Bildschirm, unabhängig von der Gruppengröße. |
| `columns(n)` | select_one, select_multiple | Zeigt Auswahlmöglichkeiten in `n` Spalten an. Beispiel: `columns(3)` zeigt drei Spalten von Optionsfeldern. |
| `gridformat<row=R col=C colspan=S align=center>` | beliebig | Positioniert das Feld in einem CSS-Grid-Layout bei Zeile `R`, Spalte `C`, über `S` Spalten. Wird mit `advanced-extension/grid-layout` verwendet. |
| `ignore-simplify` | beliebig | Weist den Formular-Renderer an, die automatische Vereinfachung oder Komprimierung des Layouts dieses Feldes zu überspringen. |
| `required-but-simplify` | beliebig | Das Feld ist erforderlich, aber sein Layout wird trotzdem vom Renderer vereinfacht |
| `embed` | beliebig | Rendert das Feld im eingebetteten/Inline-Anzeigemodus und unterdrückt seinen äußeren Wrapper und Label-Container |
| `popup` | select_one, select_multiple | Rendert die Auswahlliste in einem Popup/Modal-Overlay statt inline |
| `auto-hide-empty` | boxtag, select | Blendet das gesamte Frage-Widget aus, wenn die Auswahlliste leer ist |
| `text-nolabel` | select_one, select_multiple | Blendet die Textbeschriftung für jede Auswahl aus und zeigt nur das Eingabe-Steuerelement |

### Widgets

| Erscheinungsattribut | Fragetypen | Beschreibung |
|----------------------|----------------|-------------|
| `likert` | select_one | Präsentiert Auswahlmöglichkeiten als Likert-Skalenreihe (bereits in der Standardtabelle oben; Unterstützung bestätigt). |
| `distress` | select_one | Stellt Auswahlmöglichkeiten als Kessler Psychological Distress Scale (K10) visuelles Widget mit emotionalen Symbolen dar. |

### Visuelle Auswahl-Widgets

Diese Erscheinungsbilder ändern die gesamte Darstellung von Auswahl-Choice-Listen.

| Erscheinungsbild | Fragetypen | Beschreibung |
|-----------------|-----------|-------------|
| `tagging` | select_one, select_multiple | Auswahlmöglichkeiten werden als pillenförmige anklickbare Tag-Chips dargestellt. |
| `boxtag` | select_one, select_multiple | Auswahlmöglichkeiten werden als gestaltete rechteckige Boxen dargestellt, die der Benutzer antippt. |
| `boxtag -search` | select_one, select_multiple | Boxtag-Layout mit einer Live-Such-/Filtereingabe über den Boxen. |
| `duolingo-style1` | select_one, select_multiple | Großes Kartenlayout nach Duolingo-Vorbild — geeignet für kurze Listen mit Symbolen. |
| `rating_box` | select_one, select_multiple | Raster tippbarer nummerierter Boxen — geeignet für Skalen- oder NPS-Fragen. |
| `star_rating` | select_one | Auswahlmöglichkeiten werden als Sterne dargestellt; die Anzahl der Sterne entspricht der Anzahl der Optionen. |
| `choices-noshow` | select_one, select_multiple | Zeigt zunächst nur die ersten 10 Optionen mit einem "Mehr anzeigen"-Steuerelement. |
| `noshow` | select_one, select_multiple | Blendet die Auswahlliste vollständig aus; der Wert wird programmatisch via calculate oder API gesetzt. |
| `checkall` | select_multiple | Fügt oben in der Auswahlliste eine "Alle auswählen"-Schaltfläche hinzu. |
| `max-items(N)` | select_one, select_multiple | Begrenzt die sichtbare Auswahlliste auf N Einträge. Beispiel: max-items(5). |

### Visuelle Text-Widgets

| Erscheinungsbild | Fragetypen | Beschreibung |
|-----------------|-----------|-------------|
| `richtext` | text | Ersetzt das einfache Textfeld durch einen Rich-Text-Editor (Fett, Kursiv, Listen, Links). Speichert HTML. |
| `typingtest` | text | Tipptest-Widget — der Label-Text ist der Passage; das Widget zeichnet die getippte Antwort und die Zeit auf. |

### Medienerweiterungen

| Erscheinungsbild | Fragetypen | Beschreibung |
|-----------------|-----------|-------------|
| `watermark("expression")` | image | Legt ein Text-Wasserzeichen auf aufgenommene Fotos. Das Argument ist ein XPath-Ausdruck, der zum Aufnahmezeitpunkt ausgewertet wird. |
| `editable` | image | Ermöglicht Annotation/Zeichnen über dem aufgenommenen Foto vor dem Speichern. |

### Inline-Anzeigeformat-Konfiguration

Die Modifier `display{}` und `results{}` steuern Symbolausrichtung und Ergebnisanzeige für Inline-Widgets.

#### `display{}`-Parameter

| Parameter | Werte | Beschreibung |
|-----------|-------|-------------|
| Ausrichtung | `left`, `right`, `top`, `bottom`, `center` | Position des Symbols relativ zum Eingabefeld |
| Größe | `small`, `medium`, `large` | Symbolgröße |
| Modus | `inline-icon` | Rendert den Trigger nur als Symbol |
| Modus | `inline-button` | Rendert den Trigger als vollständige Schaltfläche |

#### `results{}`-Parameter

| Parameter | Werte | Beschreibung |
|-----------|-------|-------------|
| Ausrichtung | `left`, `right`, `top`, `bottom`, `center` | Position der Ergebniswertanzeige |
| `hide(field)` | beliebiger Teilfeldname | Blendet eine bestimmte Komponente des Ergebnisses aus |

### API-Integration

| Erscheinungsattribut | Fragetypen | Beschreibung |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Aktiviert die API-Aufruf-Integration für dieses Feld. Die Berechnungsspalte sollte einen `callapi()`-Ausdruck enthalten. Siehe [API-Aufruf](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Löst einen API-Verifizierungsaufruf mit statischen Parametern aus. Das Formular blockiert den Fortschritt, bis die API den Wert bestätigt. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Gleich wie `callapi-verify`, aber mit Parametern, die zur Laufzeit aus anderen Feldwerten abgeleitet werden. |

### Inline-Datum/Uhrzeit-Format

Für Felder `date`, `time` und `datetime` können Sie ein benutzerdefiniertes Anzeigeformat mit einer an das Erscheinungsbild angehängten Formatzeichenkette angeben:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Format-Token sind dieselben wie bei `format-date()` und `format-date-time()`. Siehe [Funktionen — Datums- und Uhrzeitfunktionen](operators-and-functions/functions#date-and-time-functions).

Beispiel:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Ereignisdatum und -uhrzeit | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Geburtsdatum | inline-[%d/%m/%Y] |

## Bekannte Einschränkungen

- Komplexe Erscheinungsbilder werden möglicherweise nicht auf allen Plattformen identisch gerendert.
- Einige fortgeschrittene rtSurvey-Erscheinungsbilder werden im Offline-Modus möglicherweise nicht unterstützt.

## Fehlerbehebung bei Darstellungsproblemen

1. **Darstellung nicht angewendet**: Überprüfen Sie die Spalte appearance auf Tippfehler.
2. **Inkonsistentes Rendering**: Überprüfen Sie die Kompatibilität mit dem Fragetyp und der Plattform.
3. **Leistungsprobleme**: Erwägen Sie die Vereinfachung komplexer Darstellungen, insbesondere bei umfangreichen Umfragen.
