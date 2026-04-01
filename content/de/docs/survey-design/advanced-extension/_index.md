---
title: "Erweiterte Erweiterungen"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Die Spalte `appearance` in rtSurvey ermöglicht es Ihnen, die visuelle Darstellung und das Verhalten von Fragen in Ihren Umfragen anzupassen. Diese Funktion verbessert die Benutzererfahrung und kann die Effizienz der Datenerhebung erheblich steigern. rtSurvey unterstützt standardmäßige XLSForm-Darstellungsattribute und erweitert diese um zusätzliche Optionen.

## rtSurvey-spezifische Darstellungs-Erweiterungen (Appearance)

rtSurvey erweitert die Standard-Darstellungsoptionen um folgende Punkte:

### Anpassung der Zeiteingabe

Für Fragen vom Typ `text`, die zur Zeiteingabe verwendet werden:

- `appearance:` - Zeigt eine Uhr zur Auswahl von Stunden und Minuten an
- `appearance: inline` - Zeigt die Uhr als Symbol an
- `appearance: inline-1line` - Zeigt die Uhr in einem einzeiligen Format an
- `appearance: inline-onlyresult` - Zeigt das Uhrsymbol an, verschwindet nach der Auswahl
- `appearance: inline-[FORMAT]` - Passt die Anzeige des Zeitformats an (z. B. `[%H:%M]`, `[%h:%M:%S]`)

### Farbanpassung

rtSurvey ermöglicht die Farbanpassung für verschiedene Darstellungsformen:

- `appearance: inline colors("0099FF")` - Passt die Symbolfarbe an
- `appearance: inline-1line colors("0000FF","FFFF00")` - Passt die Farben im einzeiligen Format an

### Grid-Layout (Gitter-Layout)

rtSurvey führt ein Grid-Layout für kompakte, tabellenartige Darstellungen ein:

- `appearance: grid` - Wird auf Gruppen angewendet, um ein Gitter-Layout zu erstellen

### Ausklappbare Gruppen (Collapsible Groups)

- `appearance: collapsible` - Erstellt erweiterbare/ausklappbare Gruppen

## Best Practices für die Verwendung von Appearance

1. **Konsistenz**: Verwenden Sie Darstellungsattribute konsistent in Ihrer Umfrage für ein einheitliches Erscheinungsbild.
2. **Mobil vs. Web**: Berücksichtigen Sie, wie die Darstellungen auf verschiedenen Geräten und Plattformen wiedergegeben werden.
3. **Leistung**: Seien Sie vorsichtig mit Darstellungsattributen, die das Laden des Formulars verlangsamen könnten (z. B. `table-list` für große Gruppen).
4. **Benutzererfahrung**: Wählen Sie Darstellungen, die die Dateneingabe für die Befragten einfacher und intuitiver machen.
5. **Testen**: Testen Sie Ihr Formular immer auf den Zielgeräten, um sicherzustellen, dass die Darstellungen wie erwartet funktionieren.

## Fortgeschrittene Techniken

### Kombinieren von Darstellungen (Appearances)

Einige Darstellungsattribute können für komplexere Layouts kombiniert werden:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Eins auswählen: | minimal compact |
```

### Dynamische Darstellungen

rtSurvey ermöglicht dynamische Änderungen der Darstellung basierend auf der Formularlogik:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Zeit eingeben: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Hinweise zur mobilen App

- Einige Darstellungen (z. B. `quick`, `signature`) sind spezifisch für mobile Geräte.
- Testen Sie gründlich sowohl auf Android als auch auf iOS, um ein konsistentes Verhalten sicherzustellen.

## Bekannte Einschränkungen

- Komplexe Darstellungen werden möglicherweise nicht auf allen Plattformen identisch gerendert.
- Einige erweiterte rtSurvey-Darstellungen werden im Offline-Modus möglicherweise nicht unterstützt.

## Fehlerbehebung bei Darstellungsproblemen

1. **Darstellung nicht angewendet**: Prüfen Sie auf Tippfehler in der Spalte `appearance`.
2. **Inkonsistentes Rendering**: Überprüfen Sie die Kompatibilität mit dem Fragetyp und der Plattform.
3. **Leistungsprobleme**: Erwägen Sie die Vereinfachung komplexer Darstellungen, insbesondere bei großen Umfragen.
