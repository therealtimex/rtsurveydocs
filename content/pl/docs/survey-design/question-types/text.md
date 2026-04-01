---
title: "Text"
description: "Typ pytania z wolną odpowiedzią tekstową w rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Typ pytania `text` zbiera odpowiedzi w postaci wolnego tekstu. Dopuszcza dowolne znaki i nie nakłada żadnych ograniczeń na format danych wejściowych.

## Podstawowa specyfikacja XLSForm

| type | name | label |
|------|------|-------|
| text | name | Jak masz na imię? |

## Typowe zastosowania

- Zbieranie imion i nazwisk
- Adresów
- Komentarzy i opisów
- Numerów identyfikacyjnych (gdy nie wymagana walidacja formatu)
- Wszelkich odpowiedzi bez ustrukturyzowanego formatu

## Wygląd

Dodaj `multiline` do kolumny `appearance`, aby wyświetlić wieloliniowe pole tekstowe (zalecane dla odpowiedzi otwartych):

| type | name    | label           | appearance |
|------|---------|-----------------|------------|
| text | comment | Twoje komentarze | multiline  |

## Walidacja

Używaj `constraint` z `regex()` do walidacji wzorców:

| type | name  | label         | constraint                      | constraint_message |
|------|-------|---------------|---------------------------------|--------------------|
| text | email | Adres email   | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Wprowadź prawidłowy adres email |
| text | phone | Numer telefonu | `regex(., '^[0-9]{9,10}$')`    | Wprowadź 9-10 cyfrowy numer |
