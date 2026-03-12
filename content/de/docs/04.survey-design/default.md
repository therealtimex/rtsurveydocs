---
title: "Standardwerte"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Standardwerte (Default Values) in rtSurvey ermöglichen es Ihnen, Fragen mit Antworten vorzubefüllen, wenn ein Befragter sie zum ersten Mal sieht. Diese Funktion kann die Effizienz der Umfrage und die Datenqualität erheblich steigern, indem sie Initialwerte bereitstellt, die entweder häufig ausgewählt werden oder als Beispiele für die erwartete Eingabe dienen.

## Grundlegende Verwendung

Um einen Standardwert festzulegen, verwenden Sie die Spalte `default` in Ihrem XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Umfragedatum                  | 2024-07-04 |
| decimal | weight      | Gewicht des Befragten (in kg) | 51.3       |
```

In diesem Beispiel wird das Umfragedatum mit dem 4. Juli 2024 vorbefüllt, und das Gewichtsfeld startet mit 51,3 kg.

## Dynamische Standardwerte

rtSurvey unterstützt dynamische Standardwerte mittels Funktionen:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Wann fand das Ereignis statt?     | today()  |
```

Hier setzt die Funktion `today()` den Standardwert automatisch auf das aktuelle Datum.

## rtSurvey-spezifische Funktionen

### Kontextbewusste Standardwerte

rtSurvey erweitert die Standardfunktionalität um kontextbewusste Werte:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Aktueller Ort   | ${current_location} |
```

Dies nutzt die rtSurvey-Variable `${current_location}`, um den Standort basierend auf dem GPS des Geräts vorzubefüllen.

### Kaskadierende Standardwerte

rtSurvey ermöglicht Standardwerte basierend auf vorherigen Antworten:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Stadt           |                 |
| text    | district | Bezirk          | ${city}-district|
```

Hier wird das Bezirksfeld basierend auf der eingegebenen Stadt vorbefüllt.

### Standardwerte in Wiederholungen (Repeats)

Bei Fragen innerhalb einer Wiederholungsgruppe wird der Standardwert berechnet, wenn die Wiederholung hinzugefügt wird:

```
| type         | name      | label            | default                |
|--------------|-----------|------------------|------------------------|
| begin repeat | visits    | Klinikbesuche    |                        |
| date         | visit_date| Besuchsdatum     | ${previous_visit_date} |
| end repeat   |           |                  |                        |
```

Dies setzt das Standard-Besuchsdatum auf das Datum des vorherigen Besuchs.

## Best Practices für die Verwendung von Standardwerten

1. **Sparsam einsetzen**: Verwenden Sie Standardwerte nur dort, wo sie die Effizienz oder Datenqualität deutlich verbessern.
2. **Genauigkeit sicherstellen**: Überprüfen und aktualisieren Sie statistische Standardwerte regelmäßig.
3. **Gründlich testen**: Besonders bei der Verwendung von dynamischen oder berechneten Standardwerten.
4. **Benutzererfahrung berücksichtigen**: Stellen Sie sicher, dass Standardwerte die Befragten nicht in die Irre führen oder Verzerrungen (Bias) einführen.
5. **Klar dokumentieren**: Sorgen Sie dafür, dass alle Teammitglieder die Logik hinter den Standardwerten verstehen.

## Fortgeschrittene Techniken für Standardwerte

### Zufällige Standardwerte

rtSurvey unterstützt zufällige Standardwerte für bestimmte Fragetypen:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Auswahl:     | random(options)   |
```

Dies wählt zufällig eine Standardoption aus der Liste 'options' aus.

### Bedingte Standardwerte

Verwenden Sie Relevanz, um bedingte Standardwerte festzulegen:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------| ---------|-----------------|
| text    | other    | Bitte angeben | N/A | ${q1} = 'other' |
```

Hier ist 'N/A' nur dann der Standardwert, wenn in einer vorherigen Frage 'other' ausgewählt wurde.

## Überlegungen zur Datenverwaltung

- Standardwerte sind in Datenexporten enthalten, normalerweise mit einem Flag, das sie als Standardwerte kennzeichnet.
- Die Audit-Trail-Funktion von rtSurvey verfolgt, wenn Standardwerte von Befragten geändert werden.

## Verhalten der mobilen App

- Die rtSurvey-Mobil-App unterstützt alle Standardwert-Funktionalitäten, einschließlich dynamischer und kontextbewusster Werte.
- Der Offline-Modus kann einige dynamische Standardwerte beeinträchtigen, die auf Echtzeitdaten angewiesen sind.

## Bekannte Einschränkungen

- Komplexe berechnete Standardwerte können die Ladezeit des Formulars beeinflussen, besonders auf leistungsschwächeren Geräten.
- Einige dynamische Standardwerte funktionieren im Vorschaumodus möglicherweise nicht wie erwartet.

## Fehlerbehebung bei Standardwerten

1. **Standardwert erscheint nicht**: Überprüfen Sie den Standard-Ausdruck auf Syntaxfehler.
2. **Unerwartete Werte**: Überprüfen Sie die Berechnungslogik und testen Sie verschiedene Szenarien.
3. **Leistungsprobleme**: Optimieren Sie komplexe Standardberechnungen oder erwägen Sie alternative Ansätze zur Anzeige von Standarddaten.
