---
title: "Pagrindinės sąvokos"
description: "Formų kūrimo apžvalga"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Kas yra XLSForm?
rtSurvey naudoja išplėstinę [XLSForm](https://xlsform.org/) standarto versiją formų kūrimui, siūlydama galingas sudėtingų apklausų kūrimo galimybes. Šis vadovas supažindins jus su pagrindinėmis rtSurvey formų kūrimo sąvokomis – nuo pagrindinės XLSForm struktūros iki pažangių rtSurvey specifinių funkcijų.

Su XLSForms galite kurti formas žmogui suprantamu formatu naudodami pažįstamą „Excel" įrankį, todėl tai prieinama beveik visiems. Šis standartas leidžia lengvai dalintis formų kūrimo darbais ir bendradarbiauti.

Nors XLSForms yra patogios pradedantiesiems, jos taip pat leidžia patyrusiems naudotojams kurti sudėtingas formas.

rtSurvey suteikia nuoseklų būdą įtraukti pažangias funkcijas, pvz., praleistų klausimų logiką, į formas įvairiose žiniatinklio ir mobiliojo duomenų rinkimo platformose.

## XLSForm struktūra
XLSForm paprastai susideda iš dviejų pagrindinių darbalapių:

1. **survey** (apklausa): apibrėžia jūsų formos struktūrą ir turinį.
2. **choices** (pasirinkimai): nurodo atsakymų pasirinkimus daugybinės atrankai klausimams.

Neprivalomas **settings** (nustatymų) darbalaapis gali pateikti papildomas formos specifikacijas.

Svarbu pažymėti, kad privalomi stulpeliai apklausos ir pasirinkimų darbalapyje turi būti, kad forma veiktų tinkamai. Neprivalomi stulpeliai abiejuose darbalapyje suteikia papildomą kiekvieno įrašo elgesio kontrolę, tačiau jie nėra būtini.

Jūsų „Excel" darbaknygiuje stulpeliai gali būti bet kuria tvarka, o neprivalomi stulpeliai gali būti palikti tušti. Tačiau labai svarbu naudoti tikslią sintaksę ir pavadinimų konvencijas, nurodytas XLSForm dokumentacijoje, kad forma veiktų teisingai.

### Apklausos darbalaapis
**Apklausos darbalaapis** yra vieta, kur apibrėžiate formos struktūrą ir pateikiate turinį. Kiekviena apklausos darbaknygės eilutė atitinka klausimą ar elementą jūsų formoje. Šie stulpeliai yra privalomi apklausos darbalapyje:

- `type` (tipas): nurodo tikimamo atsakymo tipą.
- `name` (vardas): nurodo unikalų kintamojo pavadinimą. Pavadinimai turi prasidėti raide ar pabraukimu ir gali turėti tik raides, skaitmenis, brūkšnelius, pabraukimus ir taškus. Pavadinimai skiria didžiąsias ir mažąsias raides.
- `label` (etiketė): apima tikrąjį tekstą, kurį matote klausimuose formoje.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Respondento lytis?   |
| integer             | age      | Respondento amžius?  |

### Pasirinkimų darbalaapis
**`choices`** darbalaapis naudojamas atsakymų pasirinkimams daugybinės atrankai klausimams nurodyti. Kiekviena eilutė atitinka atsakymo pasirinkimą. Šie stulpeliai yra privalomi pasirinkimų darbalapyje:

- **`list_name`**: grupuoja susijusių atsakymų pasirinkimų rinkinį.
- **`name`**: nurodo unikalų to atsakymo pasirinkimo kintamojo pavadinimą.
- **`label`**: rodo atsakymo pasirinkimą lygiai taip, kaip norite, kad jis pasirodytų formoje.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgenderis        |
| gender              | female      | Moteris              |
| gender              | male        | Vyras                |
| gender              | other       | Kita                 |

Stulpeliai, kuriuos pridedate prie savo „Excel" darbaknygio, nesvarbu, ar jie privalomi, ar neprivalomi, gali būti bet kokia tvarka. Neprivalomi stulpeliai gali būti visiškai praleisti. Eilutės ar stulpeliai gali būti palikti tušti skaityti palengvinti, tačiau duomenys po 20 gretimų tuščių stulpelių ar eilučių lape nebus apdorojami. Visas .xlsx failo formatavimas nepaisomas, todėl galite naudoti dalijančias linijas, atspalvius ir kita šriftų formatavimą, kad forma būtų lengviau skaitoma.

Vienas dalykas, kurį reikia turėti omenyje kuriant formas „Excel" programoje, yra tai, kad naudojama sintaksė turi būti tiksli. Pavyzdžiui, jei rašote **Choices** ar **choice** vietoj **choices**, forma neveiks.

### Nustatymų darbalaapis

Nustatymų darbalaapis yra neprivalomas, bet leidžia nurodyti formos lygio metaduomenis ir elgesį. Dažniausiai naudojami stulpeliai nustatymų darbalapyje:

| Stulpelis | Aprašymas |
|--------|-------------|
| form_title | Formos pavadinimas, kaip jis rodomas naudotojams |
| form_id | Unikalus formos identifikatorius, naudojamas duomenų valdymo ir API skambučiuose |
| default_language | Numatytasis daugiakalbių formų kalbos kodas (pvz., „en" anglų kalbai) |
| version | Formos versijos numeris, naudingas pokyčiams stebėti |
| instance_name | Išraiška kiekvienam formos pateikimui unikaliam pavadinimui generuoti |
| generation | Sveikasis skaičius, žymintis formos kartą. Padidinkite struktūriniams pokyčiams |
| family | Identifikatorius susijusioms formoms grupuoti per struktūrinius pokyčius |

rtSurvey nustatymų darbalaapis taip pat gali apimti papildomas konfigūracijas, specifines rtSurvey išplėstinėms funkcijoms. Visą palaikomų nustatymų sąrašą rasite rtSurvey dokumentacijoje.

## Pagrindiniai apklausos darbaknygės komponentai

Apklausos darbalaapis yra jūsų formos kūrimo pagrindas. Štai pagrindinių komponentų apžvalga:

| Komponentas | Aprašymas |
|-----------|-------------|
| [type](#question-types) | Nurodo klausimo tipą (pvz., text, integer, select_one) |
| [name](#naming-conventions) | Unikalus klausimo identifikatorius |
| [label](#labels-and-translations) | Respondentui rodomas tekstas |
| [hint](#hints-and-help-text) | Papildomas respondento patarimas |
| [appearance](#appearance-options) | Keičia klausimo rodymą |
| [relevant](#relevance-and-skip-logic) | Nustato, kada klausimas turėtų būti užduodamas (praleistų klausimų logika) |
| [constraint](#constraints-and-validation) | Tikrina atsakymą |
| [calculation](#calculations) | Apskaičiuoja reikšmes pagal kitus atsakymus |
| [required](#required-fields) | Nurodo, ar klausimas turi būti atsakytas |

Kiekvienas iš šių komponentų atlieka svarbų vaidmenį kuriant efektyvias ir veiksmingas apklausas.

### Klausimų tipai
XLSForm palaiko daug klausimų tipų. Štai kai kurios parinktys, kurias galite įvesti stulpelyje **`type`** savo XLSForm **`survey`** darbalapyje:

| Klausimo tipas            | Atsakymo įvedimas                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| integer                   | Sveikojo skaičiaus įvedimas.                                                                     |
| decimal                   | Dešimtainio skaičiaus įvedimas.                                                                  |
| range                     | Diapazono įvedimas (įskaitant įvertinimą)                                                        |
| text                      | Laisvo teksto atsakymas.                                                                         |
| select_one [options]      | Daugybinės atrankas klausimas; galima pasirinkti tik vieną atsakymą.                            |
| select_multiple [options] | Daugybinės atrankas klausimas; galima pasirinkti kelis atsakymus.                               |
| select_one_from_file [file]| Daugybinė atranka iš failo; galima pasirinkti tik vieną atsakymą.                              |
| select_multiple_from_file [file]| Daugybinė atranka iš failo; galima pasirinkti kelis atsakymus.                           |
| rank [options]            | Reitingo klausimas; suranguokite sąrašą.                                                        |
| note                      | Rodo pastabą ekrane, nenaudoja įvesties.                                                        |
| geopoint                  | Renka vieną GPS koordinatę.                                                                     |
| geotrace                  | Įrašo dviejų ar daugiau GPS koordinačių liniją.                                                |
| geoshape                  | Įrašo kelių GPS koordinačių daugiakampį.                                                       |
| date                      | Datos įvedimas.                                                                                 |
| time                      | Laiko įvedimas.                                                                                 |
| dateTime                  | Priima datos ir laiko įvedimą.                                                                  |
| image                     | Fotografuoja arba įkelia vaizdo failą.                                                          |
| audio                     | Įrašo garso įrašą arba įkelia garso failą.                                                     |
| background-audio          | Garso įrašas daromas fone pildant formą.                                                       |
| video                     | Įrašo vaizdo įrašą arba įkelia vaizdo failą.                                                   |
| file                      | Bendrasis failo įvedimas (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                            |
| barcode                   | Nuskaito brūkšninį kodą, reikia brūkšninio kodo skaitytuvo programos.                         |
| calculate                 | Atlieka skaičiavimą.                                                                            |
| acknowledge               | Patvirtinimo raginimas, nustatantis reikšmę į "OK", jei pasirinktas.                           |
| hidden                    | Laukas be susietos sąsajos elemento, naudojamas konstantai saugoti                             |
| xml-external              | Prideda nuorodą į išorinį XML duomenų failą                                                    |

### Etiketės

Etiketės yra tekstas, rodomas respondentams kiekvienam klausimui. Jos labai svarbios aiškiam bendravimui apklausose.

- **Pagrindinis naudojimas**: stulpelyje `label` įveskite klausimo tekstą.
- **Kelios kalbos**: naudokite papildomus stulpelius, pvz., `label::English` ir `label::French`, daugiakalbėms apklausoms.
- **Formatavimas**: rtSurvey palaiko pagrindinį HTML formatavimą etiketėse.

### Patarimai

Patarimai suteikia papildomus nurodymus respondentams nesugriaudami pagrindinio klausimo teksto.

- **Naudojimas**: pridėkite patarimų stulpelyje `hint`.
- **Matomumas**: patarimai paprastai rodomi po pagrindinio klausimo tekstu.
- **Daugiakalbiai**: kaip etiketės, patarimai gali būti nurodyti keliomis kalbomis naudojant `hint::Language` stulpelius.

### Išvaizda

Stulpelis `appearance` rtSurvey sistemoje leidžia tinkinti klausimų rodymą.

- **Standartinės parinktys**: apima `multiline` tekstui, `horizontal` atrankos klausimams.
- **rtSurvey plėtiniai**: 
  - Laiko įvedimas: įvairūs laikrodžio rodymų parametrai (pvz., `inline`, `inline-1line`)
  - Spalvų tinkinimas: naudokite funkciją `colors()` piktogramų spalvoms keisti

### Aktualumas

Stulpelis `relevant` įgyvendina praleistų klausimų logiką, nustatydamas, kada klausimas turėtų būti rodomas.

- **Sintaksė**: naudokite XPath išraiškas sąlygoms apibrėžti.
- **Kintamieji**: nuorodas į kitus klausimų pavadinimus naudokite su `${question_name}`.

### Privalomi

Stulpelis `required` nurodo, ar klausimas turi būti atsakytas.

- **Pagrindinis naudojimas**: naudokite `yes` arba `true`, kad klausimas būtų privalomas.
- **Išplėstinis**: gali naudoti išraiškas sąlyginiam poreikiui.

### Kartojimai

Kartojimai leidžia atsakyti į klausimų grupę kelis kartus.

- **Naudojimas**: naudokite eilutes `begin repeat` ir `end repeat`, kad apibrėžtumėte kartojimosi grupę.
- **Pavadinimas**: kiekvienai kartojimosi grupei suteikite unikalų pavadinimą.

### Medija

rtSurvey apklausose palaiko įvairius medijos tipus, įskaitant vaizdus, garso ir vaizdo įrašus.

- **Klausimų tipai**: stulpelyje tipas naudokite `image`, `audio` arba `video`.
- **Medija etiketėse**: medijos failus etiketėse nurodykite naudodami HTML žymes.

### Tik skaitymui

Tik skaitymui skirtų klausimų atveju informacija rodoma neleidžiant naudotojo įvedimo.

- **Naudojimas**: į stulpelį `appearance` pridėkite `readonly`.
- **Skaičiavimai**: dažnai naudojama su `calculate` tipu apskaičiuotoms reikšmėms rodyti.

## rtSurvey plėtiniai

rtSurvey išplečia XLSForm standartą palaikydama papildomas galimybes, pvz., `tinklelio išdėstymą`, `HTML formatavimą` ir daugybę naujų `valdiklių`.

### Tinklelio išdėstymas
rtSurvey leidžia jūsų formai imituoti tradicinių popierinių apklausų išvaizdą, suglaudinant kelis klausimus į vieną eilutę.

### Formos nustatymai

### Duomenų nustatymai

### Typeform stilius

### pulldata() plėtinys

### Išvaizdos plėtiniai

### Webbox plėtiniai
