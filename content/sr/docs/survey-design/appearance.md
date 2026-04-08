---
title: "Izgled"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolona `appearance` u rtSurvey-u vam dozvoljava da prilagodite vizuelni prikaz i ponašanje pitanja u anketama. Ova funkcija poboljšava korisničko iskustvo i može značajno unaprediti efikasnost prikupljanja podataka. rtSurvey podržava standardne atribute izgleda XLSForm-a i proširuje ih dodatnim opcijama.

## Standardni atributi izgleda XLSForm-a

rtSurvey podržava sledeće standardne atribute izgleda XLSForm-a:

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| multiline | text | Kreira višeredni tekstualni okvir (best za veb klijente) |
| minimal | select_one, select_multiple | Prikazuje opcije u padajućem meniju |
| quick | select_one | Automatski prelazi na sledeće pitanje nakon izbora (samo mobilni) |
| no-calendar | date | Potiskuje prikaz kalendara (samo mobilni) |
| month-year | date | Dozvoljava izbor samo meseca i godine |
| year | date | Dozvoljava izbor samo godine |
| horizontal-compact | select_one, select_multiple | Prikazuje opcije horizontalno (samo veb) |
| horizontal | select_one, select_multiple | Prikazuje opcije horizontalno u kolonama (samo veb) |
| likert | select_one | Prikazuje opcije kao Likertovu skalu |
| compact | select_one, select_multiple | Prikazuje opcije jednu pored druge sa minimalnim razmacima |
| quickcompact | select_one | Kombinuje kompaktni prikaz sa automatskim prelaskom (samo mobilni) |
| field-list | groups | Prikazuje celu grupu na jednom ekranu (samo mobilni) |
| label | select_one, select_multiple | Prikazuje oznake opcija bez unosa |
| list-nolabel | select_one, select_multiple | Prikazuje unose bez oznaka (koristiti sa `label`) |
| table-list | groups | Prikazuje pitanja u tabelarnom formatu |
| signature | image | Omogućava hvatanje potpisa (samo mobilni) |
| draw | image | Dozvoljava crtanje slobodnom rukom (samo mobilni) |
| map, quick map | select_one, select_one_from_file | Omogućava izbor sa mapnih elemenata |

## Najbolje prakse za korišćenje izgleda

1. **Konzistentnost**: Koristite atribute izgleda konzistentno u celoj anketi za uniforman izgled.
2. **Mobilni vs. veb**: Razmatrajte kako će se izgledi prikazivati na različitim uređajima i platformama.
3. **Performanse**: Budite oprezni sa atributima izgleda koji mogu usporiti učitavanje formulara (npr. `table-list` za velike grupe).
4. **Korisničko iskustvo**: Odaberite izglede koji olakšavaju unos podataka i čine ga intuitivnijim za ispitanike.
5. **Testiranje**: Uvek testirajte formular na ciljnim uređajima kako biste osigurali da izgledi rade prema očekivanjima.

## Napredne tehnike

### Kombinovanje izgleda

Neki atributi izgleda se mogu kombinovati za složenije rasporede:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Izaberite jedno: | minimal compact |
```

### Dinamički izgledi

rtSurvey dozvoljava dinamičke promene izgleda na osnovu logike formulara:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Unesite vreme: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Razmatranja za mobilnu aplikaciju

- Neki izgledi (npr. `quick`, `signature`) su specifični za mobilne uređaje.
- Temeljno testirajte na i Android-u i iOS-u kako biste osigurali konzistentno ponašanje.

## rtSurvey prošireni atributi izgleda

Pored standardnih izgleda XLSForm-a, rtSurvey podržava sledeće opcije specifične za platformu:

### Kontrola podataka i prikaza

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `invisible` | bilo koji | Skriva polje iz prikaza, ali i dalje prikuplja ili izračunava vrednost. Razlikuje se od tipa `hidden` — polje i dalje učestvuje u logici. |
| `displaytitle` | bilo koji | Primorava prikaz oznake/naslova polja čak i kada bi inače bio potisnut. |
| `autopull` | select_one, select_multiple | Automatski dohvata spoljne podatke za popunjavanje opcija kada se formular učita ili promeni polje okidač. |
| `floating_hint` | text, integer, decimal | Prikazuje tekst napomene kao plivajuću oznaku iznad polja unosa umesto ispod. |
| `calculate-button` | calculate | Dodaje vidljivo dugme koje pokreće ponovni proračun polja na zahtev, umesto automatskog izračunavanja. |

### Raspored

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `1screen` | group | Primorava celu grupu da se prikaže na jednom ekranu bez obzira na veličinu grupe. |
| `columns(n)` | select_one, select_multiple | Prikazuje opcije u `n` kolona. Primer: `columns(3)` prikazuje tri kolone radio dugmića. |
| `gridformat<row=R col=C colspan=S align=center>` | bilo koji | Pozicionira polje u CSS-grid raspored na redu `R`, koloni `C`, prostirući se na `S` kolona. Koristi se sa `advanced-extension/grid-layout`. |
| `ignore-simplify` | bilo koji | Nalaže rendereru formulara da preskoči automatsko pojednostavljivanje ili kondenzovanje rasporeda ovog polja. |
| `required-but-simplify` | bilo koji | Polje je obavezno, ali se njegov raspored i dalje pojednostavlja od strane renderera (zamenjuje podrazumevano ponašanje gde su obavezna polja isključena iz pojednostavljivanja). |
| `embed` | bilo koji | Prikazuje polje u ugrađenom/inline režimu prikaza, potiskujući njegov spoljni omotač i kontejner oznake — koristi se kada je pitanje ugnežđeno unutar prilagođenog HTML-a. |
| `popup` | select_one, select_multiple | Prikazuje listu opcija u iskačućem/modalnom preklapaču umesto inline. |
| `auto-hide-empty` | boxtag, select | Skriva ceo widget pitanja kada je lista opcija prazna (npr. API nije vratio rezultate). |
| `text-nolabel` | select_one, select_multiple | Skriva tekstualnu oznaku za svaku opciju, prikazujući samo kontrolu unosa. Slično `list-nolabel`, ali primenjeno po opciji, a ne kao podela kolona. |

### Widgeti

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `likert` | select_one | Prikazuje opcije kao red Likertove skale (već u standardnoj tabeli iznad; potvrđeno podržano). |
| `distress` | select_one | Prikazuje opcije kao Kesslerovu skalu psihološkog distresa (K10) vizuelni widget sa emocionalnim ikonama. |

### Vizuelni widgeti za izbor

Ovi izgledi menjaju celokupno prikazivanje lista opcija za izbor.

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `tagging` | select_one, select_multiple | Opcije se prikazuju kao klikabilni čipovi u obliku pilule sa oznakama. |
| `boxtag` | select_one, select_multiple | Opcije se prikazuju kao pravougaone stilizovane kutije koje korisnik dodiruje. |
| `boxtag -search` | select_one, select_multiple | Raspored boxtag sa živim poljem za pretragu/filter iznad kutija. |
| `duolingo-style1` | select_one, select_multiple | Raspored velikih kartica inspirisan Duolingom — pogodan za kratke liste sa ikonama. |
| `rating_box` | select_one, select_multiple | Mreža klikabilnih numerisanih kutija — pogodna za skalarna ili NPS pitanja. |
| `star_rating` | select_one | Opcije se prikazuju kao zvezde; broj zvezda je jednak broju opcija. |
| `choices-noshow` | select_one, select_multiple | Inicijalno prikazuje samo prvih 10 opcija sa kontrolom „Prikaži više". |
| `noshow` | select_one, select_multiple | Potpuno skriva listu opcija; vrednost se postavlja programski putem `calculate` ili API-ja. |
| `checkall` | select_multiple | Dodaje prečicu „Izaberi sve" na vrh liste opcija. |
| `max-items(N)` | select_one, select_multiple | Ograničava vidljivu listu opcija na N stavki. Primer: `max-items(5)`. |

### Vizuelni widgeti za tekst

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `richtext` | text | Zamenjuje obično tekstualno polje editorom bogatog teksta (podebljano, kurziv, liste, veze). Čuva HTML. |
| `typingtest` | text | Widget za test kucanja — tekst oznake je pasaž; widget beleži ukucani odgovor i vremenski raspored. |

### Medijska proširenja

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `watermark("izraz")` | image | Prekriva tekstualni vodeni žig na snimljenim fotografijama. Argument je XPath izraz koji se procenjuje u trenutku snimanja. Primer: `watermark("${id} ${today()}")`. |
| `editable` | image | Omogućava anotaciju/crtanje preko snimljene fotografije pre čuvanja. |

### Konfigurisanje inline prikaza

Modifikatori `display{}` i `results{}` mogu se dodati uz `inline` izglede za kontrolu poravnanja ikona i prikaza rezultata. Koriste se zajedno sa `inline` proširenjem za unos vremena na `text` poljima i sa widgetima za hvatanje medija.

#### Parametri `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametar | Vrednosti | Opis |
|-----------|-----------|------|
| Poravnanje | `left`, `right`, `top`, `bottom`, `center` | Pozicija ikone u odnosu na polje unosa |
| Veličina | `small`, `medium`, `large` | Veličina ikone (odgovara 2,5 rem, 5 rem, 8 rem) |
| Režim | `inline-icon` | Prikazuje okidač samo kao ikonu (bez ivice dugmeta) |
| Režim | `inline-button` | Prikazuje okidač kao puno dugme |

#### Parametri `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametar | Vrednosti | Opis |
|-----------|-----------|------|
| Poravnanje | `left`, `right`, `top`, `bottom`, `center` | Pozicija prikaza rezultatne vrednosti |
| `hide(polje)` | bilo koje podpolje | Skriva određenu komponentu rezultata (npr. `hide(seconds)`) |

### API integracija

| Atribut izgleda | Tipovi pitanja | Opis |
|-----------------|----------------|------|
| `callapi` | text, integer, decimal, select_one | Omogućava integraciju API poziva za ovo polje. Kolona calculation treba da sadrži izraz `callapi()`. Pogledajte [Poziv API-ja](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Pokreće API poziv za verifikaciju koristeći statičke parametre. Formular blokira napredak dok API ne potvrdi vrednost. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Isto kao `callapi-verify`, ali sa parametrima izvedenim iz vrednosti других polja u vreme izvođenja. |

### Inline format datuma/vremena

Za polja `date`, `time` i `datetime`, možete specificirati prilagođeni format prikaza koristeći format string dodat u izgled:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Tokeni formata su isti kao za `format-date()` i `format-date-time()`. Pogledajte [Funkcije — Funkcije datuma i vremena](operators-and-functions/functions#date-and-time-functions).

Primer:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Datum i vreme događaja | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Datum rođenja | inline-[%d/%m/%Y] |

## Poznata ograničenja

- Složeni izgledi možda neće biti identično prikazani na svim platformama.
- Neki napredni rtSurvey izgledi možda nisu podržani u režimu van mreže.

## Rešavanje problema sa izgledom

1. **Izgled nije primenjen**: Proverite da nema grešaka u pisanju u koloni appearance.
2. **Nekonzistentno prikazivanje**: Proverite kompatibilnost sa tipom pitanja i platformom.
3. **Problemi sa performansama**: Razmotrite pojednostavljivanje složenih izgleda, posebno za velike ankete.
