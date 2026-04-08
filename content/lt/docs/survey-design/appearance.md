---
title: "Išvaizda"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Stulpelis `appearance` rtSurvey sistemoje leidžia tinkinti klausimų vizualinę pateiktį ir elgseną jūsų apklausose. Ši funkcija pagerina naudotojo patirtį ir gali žymiai pagerinti duomenų rinkimo efektyvumą. rtSurvey palaiko standartinius XLSForm išvaizdos atributus ir juos papildo papildomomis parinktimis.

## Standartiniai XLSForm išvaizdos atributai

rtSurvey palaiko šiuos standartinius XLSForm išvaizdos atributus:

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| multiline | text | Sukuria kelių eilučių teksto lauką (geriausiai tinka žiniatinklio klientams) |
| minimal | select_one, select_multiple | Rodo pasirinkimus išskleidžiamajame sąraše |
| quick | select_one | Automatiškai pereina prie kito klausimo po pasirinkimo (tik mobiliuosiuose) |
| no-calendar | date | Paslepia kalendoriaus rodymą (tik mobiliuosiuose) |
| month-year | date | Leidžia pasirinkti tik mėnesį ir metus |
| year | date | Leidžia pasirinkti tik metus |
| horizontal-compact | select_one, select_multiple | Rodo pasirinkimus horizontaliai (tik žiniatinklyje) |
| horizontal | select_one, select_multiple | Rodo pasirinkimus horizontaliai stulpeliuose (tik žiniatinklyje) |
| likert | select_one | Pateikia pasirinkimus kaip Likerto skalę |
| compact | select_one, select_multiple | Rodo pasirinkimus greta su minimaliu tarpeliu |
| quickcompact | select_one | Sujungia kompaktinį rodymą su automatinio perėjimo funkcija (tik mobiliuosiuose) |
| field-list | groups | Rodo visą grupę viename ekrane (tik mobiliuosiuose) |
| label | select_one, select_multiple | Rodo pasirinkimų etiketes be įvesties laukų |
| list-nolabel | select_one, select_multiple | Rodo įvesties laukus be etikečių (naudokite su `label`) |
| table-list | groups | Rodo klausimus lentelės formatu |
| signature | image | Įgalina parašo fiksavimą (tik mobiliuosiuose) |
| draw | image | Leidžia piešti laisvai (tik mobiliuosiuose) |
| map, quick map | select_one, select_one_from_file | Įgalina pasirinkimą iš žemėlapio elementų |

## Geriausios išvaizdos naudojimo praktikos

1. **Nuoseklumas**: naudokite išvaizdos atributus nuosekliai visoje apklausoje vienodam atrodymui.
2. **Mobilieji ir žiniatinklis**: atsižvelkite į tai, kaip išvaizda bus atvaizduojama skirtinguose įrenginiuose ir platformose.
3. **Našumas**: būkite atsargūs su išvaizdos atributais, kurie gali sulėtinti formos įkėlimą (pvz., `table-list` didelėms grupėms).
4. **Naudotojo patirtis**: pasirinkite išvaizdas, kurios palengvina duomenų įvedimą ir daro jį intuityvesnį respondentams.
5. **Testavimas**: visada patikrinkite savo formą tiksliniais įrenginiais, kad užtikrintumėte, jog išvaizdos veikia kaip tikimasi.

## Pažangios technikos

### Išvaizdų derinimas

Kai kurie išvaizdos atributai gali būti derinami sudėtingesniems išdėstymams:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Pasirinkite vieną: | minimal compact |
```

### Dinaminė išvaizda

rtSurvey leidžia dinamiškai keisti išvaizdą pagal formos logiką:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Įveskite laiką: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobiliosios programos svarstymai

- Kai kurios išvaizados (pvz., `quick`, `signature`) yra būdingos mobiliesiems įrenginiams.
- Temkingai patikrinkite tiek „Android", tiek „iOS", kad užtikrintumėte nuoseklią elgseną.

## rtSurvey išplėstiniai išvaizdos atributai

Be standartinių XLSForm išvaizadų, rtSurvey palaiko šias platformai būdingas parinktis:

### Duomenų ir rodinio valdymas

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `invisible` | bet koks | Paslepia lauką nuo peržiūros, tuo pačiu vis dar renkant ar skaičiuojant jo reikšmę. Skiriasi nuo tipo `hidden` — laukas vis dar dalyvauja logikoje. |
| `displaytitle` | bet koks | Priverčia rodyti lauko etiketę/pavadinimą net tada, kai jis kitu atveju būtų nuslopinamas. |
| `autopull` | select_one, select_multiple | Automatiškai gauna išorinius duomenis pasirinkimams užpildyti, kai forma įkeliama arba pasikeičia aktyviklio laukas. |
| `floating_hint` | text, integer, decimal | Rodo patarimo tekstą kaip slankiąją etiketę virš įvesties lauko, o ne žemiau jo. |
| `calculate-button` | calculate | Prideda matomą mygtuką, kuris aktyvina lauko perskaičiavimą pagal poreikį, o ne skaičiuoja automatiškai. |

### Išdėstymas

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `1screen` | group | Priverčia visą grupę rodyti viename ekrane, nepaisant grupės dydžio. |
| `columns(n)` | select_one, select_multiple | Rodo pasirinkimus `n` stulpeliuose. Pavyzdys: `columns(3)` rodo tris radijo mygtukų stulpelius. |
| `gridformat<row=R col=C colspan=S align=center>` | bet koks | Nustato lauką CSS-tinklelio išdėstyme eilutėje `R`, stulpelyje `C`, apimant `S` stulpelius. Naudojama su `advanced-extension/grid-layout`. |
| `ignore-simplify` | bet koks | Nurodo formos vaizdinimui praleisti automatinį šio lauko išdėstymo supaprastinimą ar suspaudimą. |
| `required-but-simplify` | bet koks | Laukas yra privalomas, bet jo išdėstymas vis tiek supaprastinamas vaizdintojo (nepaiso numatytosios elgsenos, kai privalomi laukai atmetami iš supaprastinimo). |
| `embed` | bet koks | Renderuoja lauką įterptame/inline rodymo režime, slopinant jo išorinį apvalkalą ir etiketės konteinerį — naudojama, kai klausimas yra įterpiamas į pasirinktinį HTML. |
| `popup` | select_one, select_multiple | Renderuoja pasirinkimų sąrašą popup/modal perdangoje, o ne inline. |
| `auto-hide-empty` | boxtag, select | Paslepia visą klausimo valdiklį, kai pasirinkimų sąrašas yra tuščias (pvz., grąžintų API rezultatų nėra). |
| `text-nolabel` | select_one, select_multiple | Paslepia teksto etiketę kiekvienam pasirinkimui, rodydamas tik įvesties valdiklį. Panašus į `list-nolabel`, bet taikomas kiekvienam pasirinkimui, o ne kaip stulpelio padalijimas. |

### Valdikliai

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `likert` | select_one | Pateikia pasirinkimus kaip Likerto skalės eilutę (jau standartinėje lentelėje aukščiau; patvirtinta, kad palaikoma). |
| `distress` | select_one | Vaizduoja pasirinkimus kaip Keslerio psichologinio distreso skalės (K10) vizualinį valdiklį su emocinėmis piktogramomis. |

### Pasirinkimo vizualiniai valdikliai

Šie išvaizdos variantai keičia visą pasirinkimų sąrašų renderavimą.

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Pasirinkimai renderuojami kaip spustelėjami pill formos žymų čipsai. |
| `boxtag` | select_one, select_multiple | Pasirinkimai renderuojami kaip stilizuoti stačiakampiai laukeliai, kuriuos vartotojas paliečia. |
| `boxtag -search` | select_one, select_multiple | Boxtag išdėstymas su gyvu paieškos/filtravimo įvedimu virš laukelių. |
| `duolingo-style1` | select_one, select_multiple | Duolingo įkvėptas kortelių išdėstymas — tinkamas trumpiems sąrašams su piktogramomis. |
| `rating_box` | select_one, select_multiple | Paliečiamų sunumeruotų laukelių tinklelis — tinkamas skalės ar NPS klausimams. |
| `star_rating` | select_one | Pasirinkimai renderuojami kaip žvaigždės; žvaigždžių skaičius lygus pasirinkimų skaičiui. |
| `choices-noshow` | select_one, select_multiple | Iš pradžių rodo tik pirmus 10 pasirinkimų su valdikliu „Rodyti daugiau". |
| `noshow` | select_one, select_multiple | Visiškai slepia pasirinkimų sąrašą; reikšmė nustatoma programatiškai per `calculate` ar API. |
| `checkall` | select_multiple | Prideda „Pasirinkti visus" sparčiąją nuorodą pasirinkimų sąrašo viršuje. |
| `max-items(N)` | select_one, select_multiple | Apriboja matomą pasirinkimų sąrašą iki N elementų. Pavyzdys: `max-items(5)`. |

### Teksto vizualiniai valdikliai

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `richtext` | text | Pakeičia paprastą teksto lauką raiškiojo teksto redaktoriumi (paryškintas, kursyvinis, sąrašai, nuorodos). Saugo HTML. |
| `typingtest` | text | Rašymo testo valdiklis — etiketės tekstas yra ištrauka; valdiklis įrašo surinktą atsakymą ir laiką. |

### Medijų plėtiniai

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Uždeda teksto vandens ženklą ant užfiksuotų nuotraukų. Arguments yra XPath išraiška, įvertinta fiksavimo metu. Pavyzdys: `watermark("${id} ${today()}")`. |
| `editable` | image | Įgalina anotaciją/piešimą ant užfiksuotos nuotraukos prieš išsaugojimą. |

### Inline rodinio konfigūracija

Modifikatoriai `display{}` ir `results{}` gali būti pridedami prie `inline` išvaizdos variantų, siekiant kontroliuoti piktogramų išlygiavimą ir rezultatų rodymą.

#### `display{}` parametrai

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametras | Reikšmės | Aprašymas |
|------------|----------|-----------|
| Išlygiavimas | `left`, `right`, `top`, `bottom`, `center` | Piktogramos padėtis įvesties lauko atžvilgiu |
| Dydis | `small`, `medium`, `large` | Piktogramos dydis (atitinkamai 2,5 rem, 5 rem, 8 rem) |
| Režimas | `inline-icon` | Renderuoja aktyviklį tik kaip piktogramą (be mygtuko kraštinės) |
| Režimas | `inline-button` | Renderuoja aktyviklį kaip visą mygtuką |

#### `results{}` parametrai

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametras | Reikšmės | Aprašymas |
|------------|----------|-----------|
| Išlygiavimas | `left`, `right`, `top`, `bottom`, `center` | Rezultato reikšmės rodymo padėtis |
| `hide(field)` | bet koks sublauko pavadinimas | Paslepia konkretų rezultato komponentą (pvz., `hide(seconds)`) |

### API integracija

| Išvaizdos atributas | Klausimų tipai | Aprašymas |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Įgalina API skambučio integraciją šiam laukui. Skaičiavimo stulpelyje turi būti `callapi()` išraiška. Žr. [API skambutis](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Aktyvina API patikrinimo skambutį naudojant statinius parametrus. Forma blokuoja pažangą, kol API patvirtina reikšmę. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Tas pats kaip `callapi-verify`, bet su parametrais, gautais iš kitų lauko reikšmių vykdymo metu. |

### Įterptas datos/laiko formatas

`date`, `time` ir `datetime` laukams galite nurodyti pasirinktinį rodinio formatą naudodami formato eilutę, pridedamą prie išvaizdos:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Formato žymės yra tokios pačios kaip `format-date()` ir `format-date-time()`. Žr. [Funkcijos — Datos ir laiko funkcijos](operators-and-functions/functions#date-and-time-functions).

Pavyzdys:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Renginio data ir laikas | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Gimimo data | inline-[%d/%m/%Y] |

## Žinomos apribojimai

- Sudėtingos išvaizados gali ne vienodai atvaizduotis visose platformose.
- Kai kurios pažangios rtSurvey išvaizados gali būti nepalaikomos neprisijungusiame režime.

## Išvaizdos problemų šalinimas

1. **Išvaizda nepritaikyta**: patikrinkite, ar nėra rašybos klaidų išvaizdos stulpelyje.
2. **Nesuderinamas atvaizdavimas**: patikrinkite suderinamumą su klausimo tipu ir platforma.
3. **Našumo problemos**: apsvarstykite galimybę supaprastinti sudėtingas išvaizadas, ypač didelėms apklausoms.
