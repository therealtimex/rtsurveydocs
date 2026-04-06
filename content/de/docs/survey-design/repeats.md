---
title: "Fragen wiederholen"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Wiederholungen (Repeats) sind eine leistungsstarke Funktion in rtSurvey, die es Ihnen ermöglicht, denselben Satz von Informationen mehrmals innerhalb einer einzigen Umfrage zu erfassen. Dies ist besonders nützlich für Szenarien wie Haushaltsbefragungen, bei denen Sie Daten über mehrere Haushaltsmitglieder sammeln müssen.

## Grundlegende Wiederholungsstruktur

Um eine Wiederholung in rtSurvey zu erstellen, verwenden Sie das Konstrukt `begin_repeat` und `end_repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Name des Kindes      |
| decimal      | birthweight  | Geburtsgewicht       |
| select_one male_female | sex | Geschlecht des Kindes|
| end repeat   |              |                      |
```

In diesem Beispiel kann der Benutzer Informationen über mehrere Kinder sammeln, indem er im Formular neue Wiederholungen hinzufügt.

## Beschriftung von Wiederholungen

Obwohl die Spalte `label` für `begin repeat` optional ist, kann das Hinzufügen einer Beschriftung die Navigation verbessern:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Kinder-Informationen |
| text         | name         | Name des Kindes      |
| decimal      | birthweight  | Geburtsgewicht       |
| select_one male_female | sex | Geschlecht des Kindes|
| end repeat   |              |                      |
```

rtSurvey zeigt "Kinder-Informationen" als Titel für jede Wiederholunginstanz an.

## Feste Anzahl von Wiederholungen

Um eine feste Anzahl von Wiederholungen anzugeben, verwenden Sie die Spalte `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Kinder-Informationen | 3            |
| text         | name         | Name des Kindes      |              |
| decimal      | birthweight  | Geburtsgewicht       |              |
| end repeat   |              |                      |              |
```

Dies erstellt genau 3 Kinder-Wiederholungen.

## Dynamische Anzahl von Wiederholungen

rtSurvey unterstützt dynamische Wiederholungszahlen basierend auf vorherigen Antworten:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Anzahl der Haushaltsmitglieder?|                    |
| begin repeat | hh_member  | Haushaltsmitglied              | ${num_hh_members}  |
| text     | name           | Name                           |                    |
| integer  | age            | Alter                          |                    |
| end repeat |              |                                |                    |
```

## Bedingte Wiederholungen

Sie können die Spalte `relevant` verwenden, um Wiederholungen bedingt anzuzeigen:

```
| type              | name        | label                     | relevant            |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Leben hier Kinder?        |                     |
| begin repeat      | child_repeat| Kinder-Informationen      | ${has_child} = 'yes'|
| text              | name        | Name des Kindes           |                     |
| decimal           | birthweight | Geburtsgewicht            |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-spezifische Funktionen

### Wiederholungs-Zusammenfassung

rtSurvey bietet eine Zusammenfassungs-Ansicht für Wiederholungen. Um die Zusammenfassung anzupassen, verwenden Sie eine Gruppe innerhalb der Wiederholung:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Vorname                                  |
| text         | last_name    | Nachname                                 |
| integer      | age          | Alter                                    |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Anzeigeoptionen für Wiederholungen

rtSurvey bietet zusätzliche Anzeigeoptionen (Appearances) für Wiederholungen:

- `appearance: field-list` - Zeigt alle Fragen einer Wiederholung auf einem Bildschirm an.
- `appearance: table-list` - Stellt Wiederholungen in tabellarischer Form dar.

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Kinder-Infos      | table-list  |
| text         | name         | Name              |             |
| integer      | age          | Alter             |             |
| end repeat   |              |                   |             |
```

### Verschachtelte Wiederholungen (Nested Repeats)

rtSurvey unterstützt verschachtelte Wiederholungen für komplexe Datenstrukturen:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Haushalt             |
| text         | hh_name        | Haushaltsname        |
| begin repeat | hh_member      | Haushaltsmitglied    |
| text         | member_name    | Name des Mitglieds   |
| integer      | member_age     | Alter des Mitglieds  |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Best Practices für die Verwendung von Wiederholungen in rtSurvey

1. Verwenden Sie aussagekräftige Namen und Beschriftungen für Wiederholungen, um die Datenanalyse zu erleichtern.
2. Erwägen Sie die Verwendung dynamischer Wiederholungszahlen, um Dateneingabefehler à reduzieren.
3. Testen Sie Ihr Formular gründlich, insbesondere bei der Verwendung komplexer verschachtelter Wiederholungen.
4. Nutzen Sie die Zusammenfassungs-Funktion, um Enumeratoren die Navigation durch lange Wiederholungslisten zu erleichtern.
5. Seien Sie vorsichtig mit einer großen Anzahl von Wiederholungen, da diese die Formularleistung beeinträchtigen können.

## Umgang mit Null Wiederholungen

Um null Wiederholungen in rtSurvey darzustellen:

1. Schulen Sie Enumeratoren darin, die erste Wiederholung zu löschen, wenn sie nicht benötigt wird.
2. Verwenden Sie dynamische Wiederholungszahlen, wenn die genaue Anzahl bekannt ist.
3. Nutzen Sie `relevant`, um Wiederholungen bedingt anzuzeigen.

## Überlegungen zum Datenexport

Beim Exportieren von Daten aus rtSurvey werden Wiederholungsdaten normalerweise "geflacht". Jede Wiederholungsinstanz wird zu einer separaten Zeile in den exportierten Daten, wobei die Daten des übergeordneten Formulars für jede Instanz wiederholt werden.

## Überlegungen zur mobilen App

- Wiederholungen in der rtSurvey-Mobil-App unterstützen die Offline-Datenerfassung.
- Eine große Anzahl von Wiederholungen kann die App-Leistung auf leistungsschwächeren Geräten beeinträchtigen.

Durch den effektiven Einsatz von Wiederholungen in rtSurvey können Sie flexible und leistungsstarke Umfragen erstellen, die in der Lage sind, komplexe, hierarchische Datenstrukturen zu erfassen und gleichzeitig eine benutzerfreundliche Oberfläche für Enumeratoren beizubehalten.
