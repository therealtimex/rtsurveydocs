---
title: "Medien"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey unterstützt die Integration reichhaltiger Medien in Umfragen, sodass Sie Ihre Fragebögen mit Bildern, Audio und Video aufwerten können. Diese Funktion kann die Erfahrung der Befragten und die Qualität der erfassten Daten erheblich verbessern.

## Unterstützte Medientypen

rtSurvey unterstützt die folgenden Medientypen:
- Bilder (jpg, png, gif)
- Audio (mp3, wav)
- Video (mp4, webm)

## Medien zu Ihrer Umfrage hinzufügen

Um Medien in Ihr rtSurvey-Formular einzubinden, verwenden Sie die folgenden Spalten in Ihrem XLSForm:

- `image`: Zum Anzeigen von Bildern
- `audio`: Zum Abspielen von Audiodateien
- `video`: Zum Abspielen von Videodateien

Beispiel:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Medienbeispiel | example.jpg  | sound.mp3   | clip.mp4    |
```

## Medien-Dateiverwaltung

### Webbasierte Umfragen
Für webbasierte Umfragen bietet rtSurvey eine Schnittstelle zur Medienverwaltung, über die Sie Ihre Mediendateien hochladen und organisieren können. Diese Dateien stehen dann automatisch für die Verwendung in Ihren Umfragen zur Verfügung.

### Mobile App
Bei Verwendung der rtSurvey-Mobil-App:
1. Legen Sie Ihre Mediendateien im Ordner `/rtSurvey/forms/[Formularname]-media/` auf Ihrem Gerät ab.
2. Geben Sie den exakten Dateinamen in Ihrem XLSForm an.

## rtSurvey-spezifische Funktionen

### Dynamisches Laden von Medien
rtSurvey unterstützt das dynamische Laden von Medien basierend auf Umfrageantworten:

```
| type         | name      | label               | image                    |
|--------------|-----------|---------------------|--------------------------| 
| select_one species | animal | Tier auswählen     | ${animal}.jpg            |
```

### Medien in Auswahloptionen
rtSurvey ermöglicht die Verwendung von Medien in Auswahloptionen für Auswahlfragen:

```
| type                | name    | label           | media::image |
|---------------------|---------|-----------------|--------------|
| select_one_from_file animals | Tier wählen     |              |
```

Im Choices-Blatt:
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | Hund  | dog.jpg      |
| animals   | cat   | Katze | cat.jpg      |
```

### Medienerfassung
rtSurvey erweitert XLSForm um Funktionen zur Medienerfassung:

```
| type  | name        | label                  |
|-------|-------------|------------------------|
| image | photo       | Foto aufnehmen         |
| audio | voice_note  | Sprachnotiz aufzeichnen|
| video | video_clip  | Video aufnehmen        |
```

## Best Practices für die Verwendung von Medien

1. **Dateigrößen optimieren**: Große Mediendateien können das Laden und Übermitteln der Umfrage verlangsamen.
2. **Geeignete Formate verwenden**: Halten Sie sich an weit verbreitete Formate (jpg für Bilder, mp3 für Audio, mp4 für Video).
3. **Alternativen bereitstellen**: Fügen Sie für die Barrierefreiheit immer Textalternativen hinzu.
4. **Gründlich testen**: Stellen Sie sicher, dass Medien auf allen Zielgeräten korrekt angezeigt werden.
5. **Offline-Nutzung berücksichtigen**: Stellen Sie bei Umfragen, die offline durchgeführt werden könnten, sicher, dass alle Medien lokal verfügbar sind.

## Mehrsprachige Medienunterstützung

rtSurvey unterstützt sprachspezifische Medien. Verwenden Sie das Suffix `::Sprache`:

```
| type | name  | label        | image::English | image::Deutsch |
|------|-------|--------------|----------------|----------------|
| note | intro | Willkommen   | welcome_en.jpg | welcome_de.jpg |
```

## Medien beim Datenexport

Beim Exportieren von Daten aus rtSurvey:
- Bei Web-Umfragen sind Medien-URLs im Export enthalten.
- Bei Mobil-App-Umfragen sind Dateipfade enthalten.

## Überlegungen zur mobilen App

- Stellen Sie sicher, dass auf den Geräten genügend Speicherplatz für medienintensive Umfragen vorhanden ist.
- Die rtSurvey-Mobil-App unterstützt die Offline-Wiedergabe und -Erfassung von Medien.
- Große Mediendateien können die App-Leistung auf leistungsschwachen Geräten beeinträchtigen.

## Bekannte Einschränkungen

- Einige ältere Browser unterstützen möglicherweise nicht alle Medienformate.
- Sehr große Videodateien können in Situationen mit geringer Bandbreite Probleme verursachen.

## Fehlerbehebung bei Medienproblemen

1. **Medien werden nicht angezeigt**: Überprüfen Sie Dateipfade und Namen auf Richtigkeit.
2. **Wiedergabeprobleme**: Stellen Sie sicher, dass das Medienformat von den Zielgeräten unterstützt wird.
3. **Langsames Laden**: Erwägen Sie die Optimierung der Dateigrößen oder das Vorabladen von Medien.

## Fortgeschrittene Medienfunktionen

### Geotagging
rtSurvey kann bei Umfragen aufgenommene Medien automatisch mit Geotags versehen:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Foto aufnehmen| geotag     |
```

### Medien-Annotationen
Befragten das Annotieren von Bildern ermöglichen:

```
| type  | name        | label           | appearance |
|-------|-------------|-----------------|------------|
| image | photo       | Bild annotieren | annotate   |
```

Durch den effektiven Einsatz von Medien in Ihren rtSurvey-Formularen können Sie ansprechendere, informativere und präzisere Umfragen erstellen. Denken Sie daran, die Vorteile der Medieneinbindung mit Leistungsaspekten abzuwägen, insbesondere bei Umfragen in Gebieten mit eingeschränkter Internetverbindung oder auf leistungsschwächeren Geräten.
