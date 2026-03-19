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

rtSurvey obsługuje bogatą integrację mediów w ankietach, umożliwiając wzbogacenie kwestionariuszy o obrazy, dźwięk i wideo. Ta funkcja może znacznie poprawić doświadczenie respondenta i jakość zbieranych danych.

## Obsługiwane typy mediów

rtSurvey obsługuje następujące typy mediów:
- Obrazy (jpg, png, gif)
- Audio (mp3, wav)
- Wideo (mp4, webm)

## Dodawanie mediów do ankiety

Aby dołączyć media do formularza rtSurvey, użyj następujących kolumn w XLSForm:

- `image`: Do wyświetlania obrazów
- `audio`: Do odtwarzania plików audio
- `video`: Do odtwarzania plików wideo

Przykład:

```
| type | name          | label          | image        | audio       | video       |
|------|---------------|----------------|--------------|-------------|-------------|
| note | media_example | Przykład mediów| example.jpg  | sound.mp3   | clip.mp4    |
```

## Zarządzanie plikami mediów

### Ankiety internetowe
Dla ankiet internetowych rtSurvey zapewnia interfejs zarządzania mediami, w którym można przesyłać i organizować pliki mediów. Pliki te są następnie automatycznie dostępne do użycia w ankietach.

### Aplikacja mobilna
Przy korzystaniu z aplikacji mobilnej rtSurvey:
1. Umieść pliki mediów w folderze `/rtSurvey/forms/[nazwa-formularza]-media/` na urządzeniu.
2. Odwołaj się do dokładnej nazwy pliku w XLSForm.

## Najlepsze praktyki używania mediów

1. **Optymalizuj rozmiary plików**: Duże pliki mediów mogą spowalniać ładowanie i przesyłanie ankiety.
2. **Używaj odpowiednich formatów**: Trzymaj się powszechnie obsługiwanych formatów (jpg dla obrazów, mp3 dla audio, mp4 dla wideo).
3. **Zapewnij alternatywy**: Zawsze dołączaj alternatywy tekstowe dla dostępności.
4. **Testuj dokładnie**: Upewnij się, że media wyświetlają się prawidłowo na wszystkich docelowych urządzeniach.
5. **Rozważ użycie offline**: Dla ankiet, które mogą być przeprowadzane offline, upewnij się, że wszystkie media są dostępne lokalnie.

## Obsługa mediów wielojęzycznych

rtSurvey obsługuje media specyficzne dla języka. Użyj sufiksu `::language`:

```
| type | name  | label      | image::English | image::Polish |
|------|-------|------------|----------------|----------------|
| note | intro | Powitanie  | welcome_en.jpg | welcome_pl.jpg |
```
