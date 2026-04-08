---
title: "Pamja"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolona `appearance` në rtSurvey ju lejon të personalizoni prezantimin vizual dhe sjelljen e pyetjeve në sondazhet tuaja. Kjo veçori rrit eksperiencën e përdoruesit dhe mund të përmirësojë ndjeshëm efikasitetin e mbledhjes së të dhënave. rtSurvey mbështet atributet standarde të pamjes XLSForm dhe i zgjeron ato me opsione shtesë.

## Atributet Standarde të Pamjes XLSForm

rtSurvey mbështet atributet e mëposhtme standarde të pamjes XLSForm:

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| multiline | text | Krijon një kuti teksti me shumë rreshta (më e mirë për klientët ueb) |
| minimal | select_one, select_multiple | Shfaq zgjedhjet në një menu rënëse |
| quick | select_one | Kalon automatikisht te pyetja tjetër pas zgjedhjes (vetëm celular) |
| no-calendar | date | Fshin shfaqjen e kalendarit (vetëm celular) |
| month-year | date | Lejon zgjedhjen e muajit dhe vitit vetëm |
| year | date | Lejon zgjedhjen e vitit vetëm |
| horizontal-compact | select_one, select_multiple | Shfaq zgjedhjet horizontalisht (vetëm ueb) |
| horizontal | select_one, select_multiple | Shfaq zgjedhjet horizontalisht në kolona (vetëm ueb) |
| likert | select_one | Paraqet zgjedhjet si një shkallë Likert |
| compact | select_one, select_multiple | Shfaq zgjedhjet anë për anë me mbushje minimale |
| quickcompact | select_one | Kombinon shfaqjen kompakte me avancim automatik (vetëm celular) |
| field-list | groups | Shfaq të gjithë grupin në një ekran (vetëm celular) |
| label | select_one, select_multiple | Tregon etiketat e zgjedhjes pa hyrje |
| list-nolabel | select_one, select_multiple | Tregon hyrjet pa etiketa (përdorni me `label`) |
| table-list | groups | Shfaq pyetjet në format tabele |
| signature | image | Aktivizon kapjen e nënshkrimit (vetëm celular) |
| draw | image | Lejon vizatim me dorë të lirë (vetëm celular) |
| map, quick map | select_one, select_one_from_file | Mundëson zgjedhjen nga veçoritë e hartës |

## Praktikat Më të Mira për Përdorimin e Pamjes

1. **Qëndrueshmëria**: Përdorni atributet e pamjes qëndrueshëm në të gjithë sondazhin tuaj për një pamje uniforme.
2. **Celular kundrejt Ueb**: Konsideroni si do të shfaqen pamjet në pajisje dhe platforma të ndryshme.
3. **Performanca**: Bëni kujdes me atributet e pamjes që mund të ngadalësojnë ngarkimin e formularit (p.sh., `table-list` për grupe të mëdha).
4. **Eksperienca e Përdoruesit**: Zgjidhni pamjet që e bëjnë hyrjen e të dhënave më të lehtë dhe intuitivisht për të anketuarit.
5. **Testimi**: Gjithmonë testoni formularin tuaj në pajisjet e shënjestruara për të garantuar që pamjet funksionojnë sipas pritjeve.

## Teknikat e Avancuara

### Kombinimi i Pamjeve

Disa atribute pamjeje mund të kombinohen për paraqitje më komplekse:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Zgjidhni një: | minimal compact |
```

### Pamjet Dinamike

rtSurvey lejon ndryshimet dinamike të pamjes bazuar në logjikën e formularit:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Futni orën: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Konsideratat e Aplikacionit Celular

- Disa pamje (p.sh., `quick`, `signature`) janë specifike për pajisjet celulare.
- Testoni tërësisht si në Android ashtu edhe në iOS për të garantuar sjellje të qëndrueshme.

## Atributet e Zgjeruara të Pamjes rtSurvey

Përveç pamjeve standarde XLSForm, rtSurvey mbështet opsionet e mëposhtme specifike për platformën:

### Kontrolli i të dhënave dhe shfaqjes

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `invisible` | çdo | Fsheh fushën nga pamja ndërkohë që vazhdon të mbledhë ose llogarisë vlerën e saj. Ndryshe nga tipi `hidden` — fusha vazhdon të marrë pjesë në logjikë. |
| `displaytitle` | çdo | Detyron shfaqjen e etiketës/titullit të fushës edhe kur do të fshihej ndryshe. |
| `autopull` | select_one, select_multiple | Merr automatikisht të dhëna të jashtme për të populluar zgjedhjet kur formulari ngarkohet ose ndryshon fusha nxitëse. |
| `floating_hint` | text, integer, decimal | Tregon tekstin e udhëzimit si etiketë lundruese mbi fushën e hyrjes në vend se nën të. |
| `calculate-button` | calculate | Shton një buton të dukshëm që nxit rillogaritjen e fushës me kërkesë, në vend se të llogarisë automatikisht. |

### Paraqitja

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `1screen` | group | Detyron të gjithë grupin të shfaqet në një ekran të vetëm pavarësisht madhësisë së grupit. |
| `columns(n)` | select_one, select_multiple | Shfaq zgjedhjet në `n` kolona. Shembull: `columns(3)` tregon tre kolona butonaesh radio. |
| `gridformat<row=R col=C colspan=S align=center>` | çdo | Pozicionon fushën në një paraqitje CSS-grid në rreshtin `R`, kolonën `C`, duke shtrirë `S` kolona. Përdoret me `advanced-extension/grid-layout`. |
| `ignore-simplify` | çdo | Instrukton renderin e formularit të kapërcejë thjeshtimin ose ngjeshjen automatike të paraqitjes së kësaj fushe. |
| `required-but-simplify` | çdo | Fusha është e detyrueshme por paraqitja e saj thjeshtësohet gjithsesi nga rendereri (anashkalon sjelljen e parazgjedhur ku fushat e detyrueshme përjashtohen nga thjeshtimi). |
| `embed` | çdo | Renderueson fushën në modalitetin e shfaqjes së ngulitur/inline, duke fshehur mbështjellësin e jashtëm dhe kontejnerin e etiketës — përdoret kur pyetja është e ngulitur brenda HTML-it të personalizuar. |
| `popup` | select_one, select_multiple | Renderueson listën e zgjedhjeve në një mbishtresë popup/modal në vend se inline. |
| `auto-hide-empty` | boxtag, select | Fsheh të gjithë widget-in e pyetjes kur lista e zgjedhjeve është e zbrazët (p.sh., nuk kthehen rezultate API). |
| `text-nolabel` | select_one, select_multiple | Fsheh etiketën e tekstit për çdo zgjedhje, duke treguar vetëm kontrollin e hyrjes. E ngjashme me `list-nolabel` por e aplikuar për çdo zgjedhje dhe jo si ndarje kolonash. |

### Widget-et

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `likert` | select_one | Paraqet zgjedhjet si një rresht shkalle Likert (tashmë në tabelën standarde; i konfirmuar si i mbështetur). |
| `distress` | select_one | Renderueson zgjedhjet si widget-in vizual të Shkallës Psikologjike të Shqetësimit Kessler (K10) me ikona emocionale. |

### Widget-et vizuale të zgjedhjes

Këto pamje ndryshojnë renderimin e plotë të listave të zgjedhjeve të zgjedhjes.

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Zgjedhjet renderohen si chip-e etikete të klikueshme në formë pill. |
| `boxtag` | select_one, select_multiple | Zgjedhjet renderohen si kuti të stilizuara drejtkëndore që përdoruesi troket. |
| `boxtag -search` | select_one, select_multiple | Paraqitja boxtag me hyrje kërkimi/filtrimi të drejtpërdrejtë mbi kutitë. |
| `duolingo-style1` | select_one, select_multiple | Paraqitje karte e frymëzuar nga Duolingo — e përshtatshme për lista të shkurtra me ikona. |
| `rating_box` | select_one, select_multiple | Rrjetë kutish të numëruara të troketshme — e përshtatshme për pyetje me shkallë ose NPS. |
| `star_rating` | select_one | Zgjedhjet renderohen si yje; numri i yjeve barazohet me numrin e zgjedhjeve. |
| `choices-noshow` | select_one, select_multiple | Fillimisht tregon vetëm 10 zgjedhjet e para me kontroll "Shfaq më shumë". |
| `noshow` | select_one, select_multiple | Fsheh plotësisht listën e zgjedhjeve; vlera vendoset programatikisht nëpërmjet `calculate` ose API. |
| `checkall` | select_multiple | Shton një shkurtore "Zgjidhni të gjitha" në krye të listës së zgjedhjeve. |
| `max-items(N)` | select_one, select_multiple | Kufizon listën e dukshme të zgjedhjeve në N artikuj. Shembull: `max-items(5)`. |

### Widget-et vizuale të tekstit

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `richtext` | text | Zëvendëson kutinë e tekstit të thjeshtë me redaktues teksti të pasur (të theksuar, kursiv, lista, lidhje). Ruan HTML. |
| `typingtest` | text | Widget testi shtypi — teksti i etiketës është pasazhi; widget-i regjistron përgjigjen e shtypur dhe kohën. |

### Zgjerime media

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Mbivendos një filigran teksti mbi fotografitë e kapturuara. Argumenti është një shprehje XPath e vlerësuar në kohën e kapjes. Shembull: `watermark("${id} ${today()}")`. |
| `editable` | image | Aktivizon komentimin/vizatimin mbi fotografinë e kapur para ruajtjes. |

### Konfigurimi i shfaqjes inline

Modifikuesit `display{}` dhe `results{}` mund t'i shtohen pamjeve `inline` për të kontrolluar rreshtimin e ikonave dhe shfaqjen e rezultateve.

#### Parametrat `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametri | Vlerat | Përshkrimi |
|-----------|--------|------------|
| Rreshtimi | `left`, `right`, `top`, `bottom`, `center` | Pozicioni i ikonës relative me fushën e hyrjes |
| Madhësia | `small`, `medium`, `large` | Madhësia e ikonës (2,5 rem, 5 rem, 8 rem respektivisht) |
| Modaliteti | `inline-icon` | Renderueson nxitësin si ikonë vetëm (pa kufi butoni) |
| Modaliteti | `inline-button` | Renderueson nxitësin si buton të plotë |

#### Parametrat `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametri | Vlerat | Përshkrimi |
|-----------|--------|------------|
| Rreshtimi | `left`, `right`, `top`, `bottom`, `center` | Pozicioni i shfaqjes së vlerës së rezultatit |
| `hide(field)` | çdo emër nënfushe | Fsheh një komponent specifik të rezultatit (p.sh., `hide(seconds)`) |

### Integrimi API

| Atributi i Pamjes | Llojet e Pyetjeve | Përshkrimi |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Mundëson integrimin e thirrjes API për këtë fushë. Kolona calculation duhet të përmbajë një shprehje `callapi()`. Shikoni [Thirrja API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Nxit një thirrje verifikimi API duke përdorur parametra statikë. Formulari bllokon progresin derisa API të konfirmojë vlerën. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | E njëjta si `callapi-verify` por me parametra të nxjerrë nga vlerat e tjera të fushës në kohën e ekzekutimit. |

### Formati i brendshëm datë/orë

Për fushat `date`, `time` dhe `datetime`, mund të specifikoni një format shfaqjeje të personalizuar duke përdorur një varg formati të bashkëngjitur me pamjen:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Shenjat e formatit janë të njëjta si `format-date()` dhe `format-date-time()`. Shikoni [Funksionet — Funksionet e datës dhe orës](operators-and-functions/functions#date-and-time-functions).

Shembull:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Data dhe ora e ngjarjes | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Data e lindjes | inline-[%d/%m/%Y] |

## Kufizimet e Njohura

- Pamjet komplekse mund të mos renderohen njëlloj nëpërmjet të gjitha platformave.
- Disa pamje të avancuara rtSurvey mund të mos mbështeten në mënyrën offline.

## Zgjidhja e Problemeve të Pamjes

1. **Pamja Nuk Aplikohet**: Kontrolloni gabimet e shtypjes në kolonën e pamjes.
2. **Renderim i Paqëndrueshëm**: Verifikoni përputhshmërinë me llojin e pyetjes dhe platformën.
3. **Probleme Performancë**: Konsideroni thjeshtimin e pamjeve komplekse, veçanërisht për sondazhe të mëdha.
