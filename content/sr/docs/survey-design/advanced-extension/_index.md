---
title: "Napredna proširenja"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Kolona `appearance` u rtSurvey-u vam omogućava da prilagodite vizuelni prikaz i ponašanje pitanja u vašim anketama. Ova funkcija poboljšava korisničko iskustvo i može značajno poboljšati efikasnost prikupljanja podataka. rtSurvey podržava standardne XLSForm atribute izgleda i proširuje ih dodatnim opcijama.

## rtSurvey-specifična proširenja izgleda

rtSurvey proširuje standardne opcije izgleda sledećim:

### Prilagođavanje unosa vremena

Za pitanja tipa `text` koja se koriste za unos vremena:

- `appearance:` — Prikazuje sat za odabir sati i minuta
- `appearance: inline` — Prikazuje sat kao ikonu
- `appearance: inline-1line` — Prikazuje sat u formatu jednog reda
- `appearance: inline-onlyresult` — Prikazuje ikonu sata koja nestaje nakon odabira
- `appearance: inline-[FORMAT]` — Prilagođava prikaz formata vremena (npr. `[%H:%M]`, `[%h:%M:%S]`)

### Prilagođavanje boja

rtSurvey dozvoljava prilagođavanje boja za različite izglede:

- `appearance: inline colors("0099FF")` — Prilagođava boju ikone
- `appearance: inline-1line colors("0000FF","FFFF00")` — Prilagođava boje u formatu jednog reda

### Raspored u mreži

rtSurvey uvodi raspored u mreži za kompaktne, tabelarne prikaze:

- `appearance: grid` — Primenjuje se na grupe za kreiranje rasporeda u mreži

### Sklopive grupe

- `appearance: collapsible` — Kreira proširive/sklopive grupe

## Najbolje prakse za korišćenje izgleda

1. **Doslednost**: Koristite atribute izgleda dosljedno u celoj anketi za jednoobrazni izgled.
2. **Mobilni vs. veb**: Razmotrite kako će se izgledi prikazivati na različitim uređajima i platformama.
3. **Performanse**: Budite oprezni sa atributima izgleda koji mogu usporiti učitavanje formulara (npr. `table-list` za velike grupe).
4. **Korisničko iskustvo**: Birajte izglede koji olakšavaju unos podataka i čine ga intuitivnijim za ispitanike.
5. **Testiranje**: Uvek testirajte formular na ciljnim uređajima da biste osigurali da izgledi funkcionišu kako se očekuje.

## Napredne tehnike

### Kombinovanje izgleda

Neki atributi izgleda mogu biti kombinovani za složenije rasporede:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Izaberite jedan: | minimal compact |
```

### Dinamički izgledi

rtSurvey dozvoljava dinamičke promene izgleda zasnovane na logici formulara:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Unesite vreme: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Razmatranja za mobilne aplikacije

- Neki izgledi (npr. `quick`, `signature`) su specifični za mobilne uređaje.
- Temeljno testirajte na Android-u i iOS-u radi doslednog ponašanja.

## Poznata ograničenja

- Složeni izgledi se možda neće prikazivati identično na svim platformama.
- Neka napredna rtSurvey proširenja izgleda možda nisu podržana u offline modu.

## Otklanjanje grešaka u prikazu

1. **Izgled nije primenjen**: Proverite greške u kucanju u koloni appearance.
2. **Nedosledan prikaz**: Proverite kompatibilnost sa tipom pitanja i platformom.
3. **Problemi s performansama**: Razmotrite pojednostavljivanje složenih izgleda, posebno za velike ankete.
