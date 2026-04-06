---
title: "Media"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey stöder rik medieintegration i undersökningar, vilket låter dig förbättra dina frågeformulär med bilder, ljud och video. Denna funktion kan avsevärt förbättra respondentupplevelsen och kvaliteten på insamlade data.

## Mediatyper som stöds

rtSurvey stöder följande mediatyper:
- Bilder (jpg, png, gif)
- Ljud (mp3, wav)
- Video (mp4, webm)

## Lägga till media i din undersökning

För att inkludera media i ditt rtSurvey-formulär, använd följande kolumner i ditt XLSForm:

- `image`: För att visa bilder
- `audio`: För att spela upp ljudfiler
- `video`: För att spela upp videofiler

Exempel:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Medieexempel  | example.jpg  | sound.mp3   | clip.mp4    |
```

## Mediefilhantering

### Webbaserade undersökningar
För webbaserade undersökningar tillhandahåller rtSurvey ett mediehanteringsgränssnitt där du kan ladda upp och organisera dina mediefiler. Dessa filer är sedan automatiskt tillgängliga för användning i dina undersökningar.

### Mobilapp
När du använder rtSurvey-mobilappen:
1. Placera dina mediefiler i mappen `/rtSurvey/forms/[formulärnamn]-media/` på din enhet.
2. Referera till det exakta filnamnet i ditt XLSForm.

## rtSurvey-specifika funktioner

### Dynamisk medieladdning
rtSurvey stöder dynamisk laddning av media baserat på undersökningssvar:

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | Välj ett djur   | ${animal}.jpg            |
```

### Bästa praxis för att använda media

1. **Optimera filstorlekar**: Stora mediefiler kan sakta ned undersökningsladdning och inlämning.
2. **Använd lämpliga format**: Håll dig till allmänt stödda format (jpg för bilder, mp3 för ljud, mp4 för video).
3. **Tillhandahåll alternativ**: Inkludera alltid textalternativ för tillgänglighet.
4. **Testa noggrant**: Se till att media visas korrekt på alla målenheter.
5. **Tänk på offlineanvändning**: För undersökningar som kan genomföras offline, se till att all media finns tillgänglig lokalt.

## Kända begränsningar

- Vissa äldre webbläsare kanske inte stöder alla mediaformat.
- Mycket stora videofiler kan orsaka problem i situationer med låg bandbredd.

## Felsökning av mediaproblem

1. **Media visas inte**: Kontrollera filsökvägar och namn för noggrannhet.
2. **Uppspelningsproblem**: Se till att medieformatet stöds av målenheterna.
3. **Långsam laddning**: Överväg att optimera filstorlekar eller förladda media.
