---
title: "Izskats"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolonna `appearance` rtSurvey ļauj pielāgot jautājumu vizuālo noformējumu un uzvedību aptaujās. Šī funkcija uzlabo lietotāja pieredzi un var ievērojami uzlabot datu vākšanas efektivitāti. rtSurvey atbalsta standarta XLSForm izskata atribūtus un paplašina tos ar papildu opcijām.

## Standarta XLSForm izskata atribūti

rtSurvey atbalsta šādus standarta XLSForm izskata atribūtus:

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| multiline | text | Izveido daudzrindu teksta lodziņu (vislabākais tīmekļa klientiem) |
| minimal | select_one, select_multiple | Parāda izvēles nolaižamā izvēlnē |
| quick | select_one | Automātiski pāriet uz nākamo jautājumu pēc atlases (tikai mobilajiem) |
| no-calendar | date | Apspiež kalendāra attēlojumu (tikai mobilajiem) |
| month-year | date | Ļauj atlasīt tikai mēnesi un gadu |
| year | date | Ļauj atlasīt tikai gadu |
| horizontal-compact | select_one, select_multiple | Parāda izvēles horizontāli (tikai tīmeklim) |
| horizontal | select_one, select_multiple | Parāda izvēles horizontāli kolonnās (tikai tīmeklim) |
| likert | select_one | Piedāvā izvēles kā Likerta skalu |
| compact | select_one, select_multiple | Parāda izvēles blakus ar minimālu iekšējo polsterjumu |
| quickcompact | select_one | Apvieno kompakto attēlojumu ar automātisko pāreju (tikai mobilajiem) |
| field-list | groups | Parāda visu grupu vienā ekrānā (tikai mobilajiem) |
| label | select_one, select_multiple | Rāda izvēļu etiķetes bez ievades laukiem |
| list-nolabel | select_one, select_multiple | Rāda ievades laukus bez etiķetēm (izmantot ar `label`) |
| table-list | groups | Parāda jautājumus tabulas formātā |
| signature | image | Iespējo paraksta tveršanu (tikai mobilajiem) |
| draw | image | Ļauj brīvroku zīmēšanu (tikai mobilajiem) |
| map, quick map | select_one, select_one_from_file | Iespējo atlasi no kartes objektiem |

## Labākā prakse izskata izmantošanā

1. **Konsekvence**: Izmantojiet izskata atribūtus konsekventi visā aptaujā vienmērīgam izskatam.
2. **Mobilais vs. tīmeklis**: Apsveriet, kā izskata varianti tiks renderēti dažādās ierīcēs un platformās.
3. **Veiktspēja**: Esiet uzmanīgi ar izskata atribūtiem, kas varētu palēnināt formas ielādi (piem., `table-list` lielām grupām).
4. **Lietotāja pieredze**: Izvēlieties izskata variantus, kas atvieglo un padara datu ievadi intuitīvāku respondentiem.
5. **Testēšana**: Vienmēr pārbaudiet formu mērķierīcēs, lai nodrošinātu, ka izskata varianti darbojas kā paredzēts.

## Uzlabotas tehnikas

### Izskata varianta apvienošana

Dažus izskata atribūtus var apvienot sarežģītākiem izkārtojumiem:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Atlasiet vienu: | minimal compact |
```

### Dinamiskais izskats

rtSurvey ļauj dinamiski mainīt izskata variantus, pamatojoties uz formas loģiku:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Ievadiet laiku: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobilās lietotnes apsvērumi

- Daži izskata varianti (piem., `quick`, `signature`) ir specifiski mobilajām ierīcēm.
- Rūpīgi pārbaudiet gan uz Android, gan iOS, lai nodrošinātu konsekventu uzvedību.

## rtSurvey paplašinātie izskata atribūti

Papildus standarta XLSForm izskata variantiem, rtSurvey atbalsta šādas platformai specifiskas opcijas:

### Datu un attēlojuma vadība

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `invisible` | jebkuri | Slēpj lauku no skata, vienlaikus joprojām vācot vai aprēķinot tā vērtību. Atšķiras no tipa `hidden` — lauks joprojām piedalās loģikā. |
| `displaytitle` | jebkuri | Liek parādīt lauka etiķeti/nosaukumu pat tad, kad tas citādi tiktu nomākts. |
| `autopull` | select_one, select_multiple | Automātiski iegūst ārējos datus, lai aizpildītu izvēles, kad forma ielādējas vai mainās aktivatora lauks. |
| `floating_hint` | text, integer, decimal | Rāda norādījumu tekstu kā peldošu etiķeti virs ievades lauka, nevis zem tā. |
| `calculate-button` | calculate | Pievieno redzamu pogu, kas aktivizē lauka pārrēķinēšanu pēc pieprasījuma, nevis aprēķina automātiski. |

### Izkārtojums

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `1screen` | group | Liek visai grupai attēloties vienā ekrānā neatkarīgi no grupas lieluma. |
| `columns(n)` | select_one, select_multiple | Parāda izvēles `n` kolonnās. Piemērs: `columns(3)` rāda trīs radio pogu kolonnas. |
| `gridformat<row=R col=C colspan=S align=center>` | jebkuri | Novieto lauku CSS-grid izkārtojumā rindā `R`, kolonnā `C`, aptverot `S` kolonnas. Izmanto ar `advanced-extension/grid-layout`. |
| `ignore-simplify` | jebkuri | Instruē formas renderētāju izlaist šī lauka izkārtojuma automātisko vienkāršošanu vai saīsināšanu. |
| `required-but-simplify` | jebkuri | Lauks ir obligāts, bet tā izkārtojums renderētājs joprojām vienkāršo (ignorē noklusējuma uzvedību, kad obligātie lauki tiek izslēgti no vienkāršošanas). |
| `embed` | jebkuri | Renderē lauku iegultā/inline attēlojuma režīmā, nomācot tā ārējo apvalku un etiķetes konteineru — izmanto, kad jautājums ir iegults pielāgotā HTML. |
| `popup` | select_one, select_multiple | Renderē izvēļu sarakstu popup/modal pārklājumā, nevis inline. |
| `auto-hide-empty` | boxtag, select | Paslēpj visu jautājuma logrīku, kad izvēļu saraksts ir tukšs (piemēram, nav atgrieztu API rezultātu). |
| `text-nolabel` | select_one, select_multiple | Paslēpj teksta etiķeti katrai izvēlei, rādot tikai ievades vadību. Līdzīgs `list-nolabel`, bet tiek piemērots katrai izvēlei, nevis kā kolonnu sadalījums. |

### Logrīki

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `likert` | select_one | Piedāvā izvēles kā Likerta skalas rindu. |
| `distress` | select_one | Renderē izvēles kā Kesslera psiholoģiskā distresa skalas (K10) vizuālo logrīku ar emocionālām ikonām. |

### Izvēles vizuālie logrīki

Šie izskata varianti maina visu atlases izvēļu sarakstu renderēšanu.

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Izvēles renderējas kā noklikšķināmi pill formas tagu čipsi. |
| `boxtag` | select_one, select_multiple | Izvēles renderējas kā stilizēti taisnstūrveida lodziņi, kurus lietotājs pieskaras. |
| `boxtag -search` | select_one, select_multiple | Boxtag izkārtojums ar dzīvas meklēšanas/filtrēšanas ievadi virs lodziņiem. |
| `duolingo-style1` | select_one, select_multiple | Duolingo iedvesmots karšu izkārtojums — piemērots īsiem sarakstiem ar ikonām. |
| `rating_box` | select_one, select_multiple | Skaitļotu pieskaramās lodziņu tīkls — piemērots skalas vai NPS jautājumiem. |
| `star_rating` | select_one | Izvēles renderējas kā zvaigznes; zvaigžņu skaits vienāds ar izvēļu skaitu. |
| `choices-noshow` | select_one, select_multiple | Sākotnēji rāda tikai pirmās 10 izvēles ar vadīklu "Rādīt vairāk". |
| `noshow` | select_one, select_multiple | Pilnīgi slēpj izvēļu sarakstu; vērtību iestata programmatiski ar `calculate` vai API. |
| `checkall` | select_multiple | Pievieno "Atlasīt visas" saīsni izvēļu saraksta augšdaļā. |
| `max-items(N)` | select_one, select_multiple | Ierobežo redzamo izvēļu sarakstu līdz N elementiem. Piemērs: `max-items(5)`. |

### Teksta vizuālie logrīki

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `richtext` | text | Aizstāj vienkāršo teksta lodziņu ar bagātā teksta redaktoru (treknraksts, slīpraksts, saraksti, saites). Saglabā HTML. |
| `typingtest` | text | Rakstīšanas testa logrīks — etiķetes teksts ir fragments; logrīks reģistrē ierakstīto atbildi un laiku. |

### Multivides paplašinājumi

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Pārklāj teksta ūdenszīmi uz uzņemtajiem fotoattēliem. Arguments ir XPath izteiksme, kas tiek novērtēta uzņemšanas brīdī. Piemērs: `watermark("${id} ${today()}")`. |
| `editable` | image | Iespējo anotāciju/zīmēšanu virs uzņemtā fotoattēla pirms saglabāšanas. |

### Inline attēlojuma konfigurācija

Modifikatori `display{}` un `results{}` var tikt pievienoti `inline` izskata variantiem, lai kontrolētu ikonas izlīdzinājumu un rezultātu attēlojumu.

#### `display{}` parametri

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametrs | Vērtības | Apraksts |
|-----------|----------|----------|
| Izlīdzinājums | `left`, `right`, `top`, `bottom`, `center` | Ikonas pozīcija attiecībā pret ievades lauku |
| Izmērs | `small`, `medium`, `large` | Ikonas izmērs (attiecīgi 2,5 rem, 5 rem, 8 rem) |
| Režīms | `inline-icon` | Renderē aktivizētāju tikai kā ikonu (bez pogas apmales) |
| Režīms | `inline-button` | Renderē aktivizētāju kā pilnu pogu |

#### `results{}` parametri

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametrs | Vērtības | Apraksts |
|-----------|----------|----------|
| Izlīdzinājums | `left`, `right`, `top`, `bottom`, `center` | Rezultāta vērtības attēlojuma pozīcija |
| `hide(field)` | jebkurš apakšlauka nosaukums | Paslēpj konkrētu rezultāta komponentu (piemēram, `hide(seconds)`) |

### API integrācija

| Izskata atribūts | Jautājumu tipi | Apraksts |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Iespējo API izsaukumu integrāciju šim laukam. Aprēķina kolonnā jāietver `callapi()` izteiksme. Skatiet [API izsaukums](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Aktivizē API verifikācijas izsaukumu, izmantojot statiskus parametrus. Forma bloķē virzību, līdz API apstiprina vērtību. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Tāpat kā `callapi-verify`, bet ar parametriem, kas izriet no citiem lauku vērtībām izpildes laikā. |

### Iekļautais datuma/laika formāts

Laukiem `date`, `time` un `datetime` varat norādīt pielāgotu attēlojuma formātu, izmantojot formāta virkni, kas pievienota izskatam:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Formāta pilnvaru ir tās pašas kā `format-date()` un `format-date-time()`. Skatiet [Funkcijas — Datuma un laika funkcijas](operators-and-functions/functions#date-and-time-functions).

Piemērs:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Pasākuma datums un laiks | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Dzimšanas datums | inline-[%d/%m/%Y] |

## Zināmie ierobežojumi

- Sarežģīti izskata varianti var neatainot identisko visu platformu ietvaros.
- Daži uzlabotie rtSurvey izskata varianti var nebūt atbalstīti bezsaistes režīmā.

## Izskata problēmu novēršana

1. **Izskats netiek piemērots**: Pārbaudiet drukas kļūdas izskata kolonnā.
2. **Nekonsekvents renderējums**: Pārbaudiet saderību ar jautājuma tipu un platformu.
3. **Veiktspējas problēmas**: Apsveriet sarežģītu izskata variantu vienkāršošanu, īpaši lielām aptaujām.
