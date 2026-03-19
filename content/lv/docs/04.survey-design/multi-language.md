---
title: "Daudzvalodu atbalsts"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey nodrošina stabilu daudzvalodu atbalstu, ļaujot izveidot aptaujas vairākās valodās. Šī funkcija ir būtiska pētījumu veikšanai dažādās lingvistiskās populācijās vai daudzvalodu vidēs.

## Daudzvalodu aptauju iestatīšana

Lai izveidotu daudzvalodu aptauju rtSurvey, XLSForm jāpievieno valodai specifiskas kolonnas. Lūk, kā:

1. **Etiķešu tulkojumi**: Pievienojiet kolonnas katrai valodai, izmantojot formātu `label::Language (code)`.
2. **Norādījumu tulkojumi**: Izmantojiet `hint::Language (code)` norādījumu tulkošanai.
3. **Multivides failu tulkojumi**: Valodai specifiskai multividei izmantojiet `media::Language (code)`.

Piemērs:

```
| type    | name | label::English (en) | label::Español (es) | hint::English (en) | hint::Español (es) |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | How old are you?    | ¿Cuántos años tienes?| Enter your age      | Ingrese su edad     |
```

## Valodas kodi

Ieteicams izmantot oficiālos 2 rakstzīmju valodu kodus (apakštagus) pēc valodas nosaukuma. Tas atvieglo formas valodas saskaņošanu ar lietotāja saskarnes valodu. Oficiālos kodus varat atrast [šeit](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

## Noklusējuma valodas iestatīšana

Lai iestatītu noklusējuma valodu datu vākšanai, XLSForm izmantojiet darblapu `settings`:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | French (fr)       |
```

## rtSurvey specifiskās funkcijas

### Dinamiskā valodas maiņa

rtSurvey ļauj lietotājiem dinamiski mainīt valodas datu vākšanas laikā:

- Tīmekļa saskarnē izmantojiet valodas nolaižamo izvēlni augšējā navigācijas joslā.
- Mobilajā lietotnē piekļūstiet valodas opcijām caur iestatījumu izvēlni.

### Valodai specifiskās validācijas ziņojumi

rtSurvey paplašina daudzvalodu atbalstu uz validācijas ziņojumiem:

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Español (es) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | La edad debe ser 150 o menos     |
```

### LTR valodu atbalsts

Valodām no labās uz kreiso (RTL) kā arābu vai ebreju, rtSurvey automātiski pielāgo izkārtojumu:

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

### Valodai specifiskais izskats

rtSurvey ļauj norādīt dažādus izskata variantus dažādām valodām:

```
| type | name | label::English (en) | label::Chinese (zh) | appearance::English (en) | appearance::Chinese (zh) |
|------|------|---------------------|---------------------|--------------------------|---------------------------|
| text | address | Address          | 地址                 | multiline                | textarea                  |
```

## Labākā prakse daudzvalodu aptaujām

1. **Konsekventa nosaukšana**: Izmantojiet konsekventus valodu kodus visā formā.
2. **Profesionāls tulkojums**: Piesaistiet profesionālus tulkotājus, kas pārzina aptaujas kontekstu.
3. **Konteksta piezīmes**: Nodrošiniet konteksta piezīmes tulkotājiem precīzu tulkojumu nodrošināšanai.
4. **Testēšana**: Testējiet formu visās valodās pirms izvietošanas.
5. **Unicode atbalsts**: Nodrošiniet, ka datu vākšanas ierīces atbalsta Unicode nelatīņu rakstiem.
6. **Valodai specifiskā multivide**: Izmantojiet katrai valodai kulturāli atbilstošus attēlus vai audio.
7. **Izvairieties no teksta attēlos**: Ja izmantojat attēlus ar tekstu, izveidojiet atsevišķus attēlus katrai valodai.

## Īpašo gadījumu apstrāde

### Jauktas valodas atbildes

rtSurvey ļauj respondentiem ievadīt tekstu jebkurā rakstā neatkarīgi no atlasītās formas valodas. Tas ir noderīgi, lai fiksētu vārdus vai adreses to oriģinālajā rakstā.

### Valodai specifiskie jautājumu tipi

Daži jautājumu tipi var būt piemērotāki noteiktām valodām. rtSurvey ļauj izmantot dažādus jautājumu tipus dažādām valodām:

```
| type::English (en) | type::Japanese (ja) | name | label::English (en) | label::Japanese (ja) |
|--------------------|---------------------|------|---------------------|----------------------|
| text               | select_one kanji    | name | Enter your name     | 名前を選んでください    |
```

## Daudzvalodu datu eksports

Eksportējot datus no rtSurvey:

- Izvēlieties eksportu konkrētā valodā vai iekļaujiet visas valodu versijas.
- Eksportā tiek iekļauti valodas metadati, norādot, kura valoda tika izmantota katrai atbildei.

## Mobilās lietotnes apsvērumi

- rtSurvey mobilā lietotne atbalsta bezsaistes valodas maiņu.
- Nodrošiniet, ka visi nepieciešamie valodas faili ir lejupielādēti pirms bezsaistes darba.

## Zināmie ierobežojumi

- Dažas uzlabotas funkcijas var nebūt pieejamas visās valodās.
- Ārkārtīgi gari tulkojumi var ietekmēt izkārtojumu mazākos ekrānos.

Izmantojot rtSurvey daudzvalodu iespējas, varat izveidot iekļaujošas, pieejamas aptaujas, kas sasniedz dažādas iedzīvotāju grupas un nodrošina augstvērtīgus, lingvistiski precīzus datus.
