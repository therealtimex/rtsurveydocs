---
title: "Flerspråklig støtte"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey gir robust flerspråklig støtte, slik at du kan lage spørreundersøkelser på flere språk. Denne funksjonen er avgjørende for å gjennomføre forskning på tvers av ulike språklige befolkninger eller i flerspråklige miljøer.

## Sette opp flerspråklige spørreundersøkelser

For å lage en flerspråklig spørreundersøkelse i rtSurvey, må du legge til språkspesifikke kolonner i XLSForm. Slik gjør du det:

1. **Etikettoversettelser**: Legg til kolonner for hvert språk ved hjelp av formatet `label::Språk (kode)`.
2. **Hintoversettelser**: Bruk `hint::Språk (kode)` for å oversette hint.
3. **Mediefiltranslations**: For språkspesifikke medier, bruk `media::Språk (kode)`.

Eksempel:

```
| type    | name | label::English (en) | label::Español (es) | hint::English (en) | hint::Español (es) |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | How old are you?    | ¿Cuántos años tienes?| Enter your age      | Ingrese su edad     |
```

## Språkkoder

Det anbefales å bruke de offisielle 2-tegns språkkodene (subtagger) etter språknavnet. Dette gjør det enklere å matche skjemaspråk med brukergrensesnittspråk. Du finner de offisielle kodene [her](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

## Angi et standardspråk

For å angi et standardspråk for datainnsamling, bruk `settings`-regnearket i XLSForm:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | French (fr)       |
```

## rtSurvey-spesifikke funksjoner

### Dynamisk språkbytte

rtSurvey lar brukere bytte språk dynamisk under datainnsamling:

- I nettgrensesnittet, bruk språknedtrekkmenyen i den øvre navigasjonslinjen.
- I mobilappen, gå til språkalternativer gjennom innstillingsmenyen.

### Språkspesifikke valideringsmeldinger

rtSurvey utvider flerspråklig støtte til valideringsmeldinger:

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Español (es) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | La edad debe ser 150 o menos     |
```

### RTL-språkstøtte

For høyre-til-venstre (RTL)-språk som arabisk eller hebraisk justerer rtSurvey automatisk oppsettet:

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

## Beste praksis for flerspråklige spørreundersøkelser

1. **Konsekvent navngivning**: Bruk konsekvente språkkoder i hele skjemaet.
2. **Profesjonell oversettelse**: Bruk profesjonelle oversettere som kjenner surveykonteksten.
3. **Kontekstnotater**: Gi kontekstnotater til oversettere for å sikre nøyaktige oversettelser.
4. **Testing**: Test skjemaet på alle språk før distribusjon.
5. **Unicode-støtte**: Sørg for at datainnsamlingsenhetene støtter Unicode for ikke-latinske skrifter.
6. **Språkspesifikke medier**: Bruk kulturelt passende bilder eller lyd for hvert språk.
7. **Unngå tekst i bilder**: Hvis du bruker bilder med tekst, lag separate bilder for hvert språk.

## Kjente begrensninger

- Noen avanserte funksjoner er kanskje ikke tilgjengelige på alle språk.
- Ekstremt lange oversettelser kan påvirke oppsettet på mindre skjermer.
