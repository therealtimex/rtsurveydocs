---
title: "Medier"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey støtter rik medieintegrasjon i spørreundersøkelser, noe som lar deg berike spørreskjemaene dine med bilder, lyd og video. Denne funksjonen kan forbedre respondentopplevelsen og kvaliteten på innsamlede data betydelig.

## Typer medier som støttes

rtSurvey støtter følgende medietyper:
- Bilder (jpg, png, gif)
- Lyd (mp3, wav)
- Video (mp4, webm)

## Legge til medier i spørreundersøkelsen

For å inkludere medier i rtSurvey-skjemaet, bruk følgende kolonner i XLSForm:

- `image`: For å vise bilder
- `audio`: For å spille av lydfiler
- `video`: For å spille av videofiler

Eksempel:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Medieeksempel | example.jpg  | sound.mp3   | clip.mp4    |
```

## Administrasjon av mediefiler

### Nettbaserte spørreundersøkelser
For nettbaserte spørreundersøkelser gir rtSurvey et medieadministrasjonsgrensesnitt der du kan laste opp og organisere mediefilene dine. Disse filene er deretter automatisk tilgjengelige for bruk i spørreundersøkelsene.

### Mobilapp
Når du bruker rtSurvey mobilapp:
1. Plasser mediefilene i mappen `/rtSurvey/forms/[skjemanavn]-media/` på enheten.
2. Referer til det nøyaktige filnavnet i XLSForm.

## rtSurvey-spesifikke funksjoner

### Dynamisk medielasting
rtSurvey støtter dynamisk lasting av medier basert på svar i spørreundersøkelsen:

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | Velg et dyr | ${animal}.jpg            |
```

### Media i svaralternativer
rtSurvey lar deg bruke medier i svaralternativer for select-spørsmål:

I choices-arket:
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | Hund  | dog.jpg      |
| animals   | cat   | Katt  | cat.jpg      |
```

### Medieopptak
rtSurvey utvider XLSForm med medieopptak:

```
| type  | name        | label               |
|-------|-------------|---------------------|
| image | photo       | Ta et bilde         |
| audio | voice_note  | Ta opp en lydnotat  |
| video | video_clip  | Ta opp en video     |
```

## Beste praksis for bruk av medier

1. **Optimaliser filstørrelser**: Store mediefiler kan bremse lasting og innsending av spørreundersøkelsen.
2. **Bruk passende formater**: Hold deg til mye støttede formater (jpg for bilder, mp3 for lyd, mp4 for video).
3. **Gi alternativer**: Inkluder alltid tekstalternativer for tilgjengelighet.
4. **Test grundig**: Sørg for at medier vises riktig på alle målenheter.
5. **Vurder frakoblet bruk**: For spørreundersøkelser som kan gjennomføres frakoblet, sørg for at alle medier er tilgjengelige lokalt.

## Flerspråklig mediestøtte

rtSurvey støtter språkspesifikke medier. Bruk `::language`-suffikset:

```
| type | name  | label      | image::English | image::Spanish |
|------|-------|------------|----------------|----------------|
| note | intro | Velkommen  | welcome_en.jpg | welcome_es.jpg |
```

## Avanserte mediefunksjoner

### Geo-tagging
rtSurvey kan automatisk geo-tagge medier som tas opp under spørreundersøkelser:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Ta et bilde  | geotag     |
```

### Bildeannotering
La respondenter annotere bilder:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Annoter bildet | annotate |
```

## Kjente begrensninger

- Noen eldre nettlesere støtter kanskje ikke alle medieformater.
- Svært store videofiler kan forårsake problemer i situasjoner med lav båndbredde.
