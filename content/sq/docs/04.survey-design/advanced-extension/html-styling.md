---
title: "Stilimi HTML"
description: "rtSurvey mbështet etiketat HTML në etiketa dhe hints, duke lejuar formatim të pasur teksti, lidhje dhe teming dinamik ngjyrash."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey paraqet tekstin e **etiketës** dhe **hint-it** si HTML në formularët web. Kjo nënkupton se mund të përdorni etiketat standarde HTML për të formatuar tekstin, shtuar ndërprerje rreshtash, krijuar lidhje dhe aplikuar ngjyra. Kjo është veçanërisht e dobishme për fushat note, udhëzimet e seksioneve dhe përmbledhjet dinamike.

{{% alert icon=" " context="warning" %}}
HTML në etiketa paraqitet në **formularin web** dhe aplikacionet mobile rtSurvey. Mund të mos paraqitet në të gjithë klientët e përputhshëm me ODK. Gjithmonë testoni në platformën tuaj të synuar.
{{% /alert %}}

---

## Etiketat HTML të mbështetura

### Formatimi i tekstit

| Etiketa | Rezultati |
|---------|-----------|
| `<strong>tekst</strong>` ose `<b>tekst</b>` | **Tekst i trashë** |
| `<em>tekst</em>` ose `<i>tekst</i>` | *Tekst kursiv* |
| `<u>tekst</u>` | Tekst i nënvizuar |
| `<br>` | Ndërprerje rreshti |
| `<span style="...">tekst</span>` | Stilimi inline |

### Lidhjet

```html
<a href="https://example.com" target="_blank">Klikoni këtu</a>
```

Hapet në skedë të re. Përdoreni për dokumentet e referencës, udhëzimet, ose burimet e jashtme që numëruesi duhet t'i konsultojë.

### Ngjyrat

Përdorni `<span>` me stile inline:

```html
<span style="color: red;">Paralajmërim: vlera është jashtë diapazonit</span>
<span style="color: #009688;">Seksioni u plotësua</span>
```

---

## Variablat e temës së ngjyrave

rtSurvey mbështet **shenjat e temës së ngjyrave** që adaptohen me temën e konfiguruar të aplikacionit. Përdorni sintaksën `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Tekst me ngjyrë primare</span>
```

Ose duke përdorur shkurtimin e shenjës në tekstin e etiketës:

```
<font color="var(--COLOR_THEME_PRIMARY)">Shënim i rëndësishëm</font>
```

Kjo konvertohet automatikisht në `<span>` ekuivalent me variabël CSS gjatë paraqitjes.

---

## Etiketat shumëgjuhëshe

Mbështillni përmbajtjen në etiketa gjuhe për të mbështetur gjuhë të shumëfishta në qelizën e etiketës:

```
<en>Shkruani madhësinë e familjes</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey nxjerr përmbajtjen që përputhet me gjuhën aktuale të aplikacionit. Nëse asnjë etiketë gjuhe përputhëse nuk gjendet, vargu i plotë shfaqet siç është.

---

## Shembuj në fushat note

### Udhëzim seksioni me tekst të trashë dhe ndërprerje rreshti

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Seksioni 3: Përdorimi i Tokës</strong><br>Bëni të gjitha pyetjet në këtë seksion vetëm kryetarit të familjes.` |

### Përmbledhje dinamike me referencë llogaritjeje

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Numri total i anëtarëve të familjes: <strong>${total}</strong><br><span style="color: gray;">Të rritur: ${adults} · Fëmijë: ${children}</span>` |

### Paralajmërim në të kuq

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Paralajmërim:</strong> Mosha e futur (${age}) është jashtëzakonisht e lartë. Ju lutemi verifikoni.</span>` | `${age} > 100` |

### Lidhje me dokument reference

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Referojuni <a href="https://docs.example.com/guidelines" target="_blank">Udhëzimeve të Terrenit</a> para se të filloni këtë seksion.` |

---

## Etiketat speciale HTML të rtSurvey

### `<webbox src='url' title='titull'>...</webbox>`

Ngulitni butonin që hap URL-n në modal brenda formularit. Shikoni [Webbox](webbox) për detaje të plota.

### `<delete-repeat-current>etiketa</delete-repeat-current>`

Paraqet butonin brenda grupit të përsëritjes që fshin instancën aktuale të përsëritjes kur shtyp.

### `<delete-repeat-last>etiketa</delete-repeat-last>`

Paraqet butonin që fshin instancën e fundit të përsëritjes.

Shembull i përdorimit në grupin e përsëritjes:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Hiqni këtë anëtar</delete-repeat-current>` |

---

## Praktikat më të mira

1. Përdorni HTML me kursim — etiketat tepër të formatuara janë më të vështira për t'u lexuar, jo më të lehta.
2. Preferoni `<strong>` për të trashë dhe `<em>` për kursiv ndaj `<b>` dhe `<i>` të vjetruara.
3. Mbajeni përdorimin e ngjyrave kuptimplote — përdorni të kuqen për paralajmërime, jo për dekorim.
4. Gjithmonë testoni paraqitjen HTML si në aplikacionin mobile ashtu edhe në formularin web, pasi paraqitja mund të ndryshojë pak.
5. Shmangni etiketat `<table>` brenda etiketave — rrallë paraqiten mirë në ekranet mobile.
6. Mos përdorni JavaScript (`<script>`) — do të hiqet ose do të shkaktojë gabime.

## Kufizimet

- HTML komplekse (tabela, formularë, skripte) nuk mbështeten dhe mund të prishin paraqitjen.
- Disa klientë mobile më të vjetër mund të shfaqin etiketat HTML si tekst literal — testoni në të gjitha pajisjet e synuara.
- Lidhjet `<a>` hapen në shfletues ose WebView — numëruesi largohet nga formulari, gjë që mund të jetë ndërprerëse në mobile.
