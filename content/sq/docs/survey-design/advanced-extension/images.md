---
title: "Imazhe të avancuara"
description: "Veçoritë e avancuara të imazheve në rtSurvey: ujëshënjimi, shfaqja e rrjetës media dhe shënimet e imazheve."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

Përtej llojit standard të pyetjes `image`, rtSurvey ofron zgjerime për **ujëshënjimin** e fotografive të kaptura dhe shfaqjen e imazheve të shumëfishta në **rrjetë media**. Këto janë të dobishme për sondazhet e bazuara në prova ku fotografitë duhet të shënohen me identitetin e numëruesit ose metadata e sondazhit, dhe për ndërfaqet e rishikimit vizual.

---

## Ujëshënjimi

Veçoria e ujëshënjimit mbivendos tekst ose imazh mbi fotografinë e kapur para se të ruhet. Kjo përdoret për të shënuar fotografitë e terrenit me datën, emrin e numëruesit, vendndodhjen GPS, ose çdo të dhënë tjetër sondazhi — duke e bërë më të vështirë paraqitjen e fotografive ekzistuese si prova të reja të kaptura.

### Konfigurimi

Përdorni `watermark()` në kolonën **`calculation`** të fushës `image`, i kombinuar me pamjen `callapi`:

```
watermark(type, size, distance, color, shadow, rotate, blur)
```

| Parametri | Përshkrimi |
|-----------|------------|
| `type` | `'text'` për ujëshënjim teksti; `'file'` për ujëshënjim imazhi |
| `size` | Madhësia e fontit në piksel (tekst) ose madhësia e ujëshënjimit si % e gjerësisë së imazhit (skedar) |
| `distance` | Hapësira midis pllakave të ujëshënjimit të përsëritur (piksel) |
| `color` | Ngjyra e tekstit (ngjyrë CSS ose hex). Nuk përdoret për llojin `file` |
| `shadow` | Ngjyra e hijes (ngjyrë CSS ose hex) |
| `rotate` | Këndi i rrotullimit në gradë (p.sh., `45` për diagonal) |
| `blur` | Opaciteti i ujëshënjimit (0 = i padukshëm, 100 = plotësisht opak) |

### Shembull i ujëshënjimit teksti

Mbivendosni emrin e numëruesit dhe datën e sotme diagonalisht nëpër çdo fotografi të kapur:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | wm_text | | | `concat(pulldata('app-api', 'user.name'), ' | ', format-date(today(), '%d/%m/%Y'))` |
| image | site_photo | Fotografoni vendin | watermark | `watermark('text', 20, 60, '#ffffff', '#000000', 45, 40)` |

Teksti i ujëshënjimit merret nga `${wm_text}`. Vendoseni fushën e tekstit të ujëshënjimit **para** fushës image në formular.

### Shembull i ujëshënjimit imazh/logo

Mbivendosni logon e organizatës (e bashkangjitur si skedar media me emrin `logo.png`):

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| image | evidence_photo | Fotografoni provat | watermark | `watermark('file', 25, 80, '', '#000000', 0, 50)` |

### Zhbëj/ribëj

Redaktuesi i ujëshënjimit mbështet zhbëj dhe ribëj — numëruesit mund të kthehen mbrapa nëpër historinë e redaktimit para se të konfirmojnë fotografinë.

### Pllakëzimi i ujëshënjimit

Ujëshënjimi përsëritet (pllakëzohet) nëpër gjithë imazhin automatikisht. Parametri `distance` kontrollon hapësirën midis pllakave; `rotate` kontrollon këndin e çdo pllake.

---

## Widget-i i rrjetës media

Widget-i i rrjetës media shfaq koleksionin e skedarëve media (imazhe, audio, video) në paraqitje rrjetë, duke lejuar rishikuesit ose numëruesit të shfletojnë skedarët e kapur vizualisht.

Ky widget aktivizohet nga pamja `mediagridwidget` dhe zakonisht përdoret në fushat `note` ose `calculate` për të shfaqur median e kapur më parë nga grupi i përsëritjes.

### Shembull: Tregoni të gjitha fotografitë nga përsëritja si rrjetë

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | photo_list | | | `join(' ', ${site_photo})` |
| note | photo_review | Rishikoni fotografitë e kaptura | mediagridwidget | |

---

## Praktikat më të mira për fotografitë e ujëshënjuara

1. Gjithmonë llogaritni tekstin e ujëshënjimit në fushën `calculate` **mbi** fushën image kështu të jetë i disponueshëm kur merret fotografia.
2. Përdorni këndin e rrotullimit (p.sh., 45°) për t'i bërë ujëshënimet më të vështira për t'u prerë.
3. Vendosni opacitetin (`blur`) midis 30-60% — i mjaftueshëm për t'u lexuar, i mjaftueshëm i ulët për të mos errësuar subjektin e fotografisë.
4. Përfshini emrin e numëruesit, datën dhe koordinatat GPS në tekstin e ujëshënjimit për të maksimizuar vlerën e auditit.
5. Testoni paraqitjen e ujëshënjimit në pajisjen me specifikimet më të ulëta në flotën tuaj — ujëshënjimi i bazuar në canvas mund të jetë i ngadalshëm në harduerët e vjetër.

## Kufizimet

- Ujëshënjimi zbatohet nga ana e klientit duke përdorur API Canvas HTML5 — kërkon shfletues ose WebView të aftë.
- Fotografitë me rezolucion shumë të lartë mund të marrin disa sekonda për të ujëshënjuar në pajisjet me nivel të ulët.
- Ujëshënimet bëhen pjesë e skedarit të imazhit — nuk mund të hiqen pas dorëzimit pa redaktim imazhi.
- Lloji i ujëshënjimit `file` kërkon që imazhi i logos të bashkëngjitur si skedar media me emrin saktësisht të pritur.
