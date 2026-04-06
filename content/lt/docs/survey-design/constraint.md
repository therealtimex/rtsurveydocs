---
title: "Atsakymų tikrinimas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Vienas iš būdų užtikrinti duomenų kokybę yra pridėti apribojimus prie formos duomenų laukų. Apribojimai padeda išvengti to, kad naudotojai įvestų netinkamus ar neįmanomus atsakymus. Pavyzdžiui, klausinėjant apie asmens pajamas, norite išvengti nerealingų reikšmių, tokių kaip neigiami skaičiai ar itin didelės reikšmės. Duomenų apribojimų pridėjimas formoje yra paprastas. Tiesiog atlikite toliau nurodytus veiksmus:

1. Pridėkite naują stulpelį pavadinimu „constraint" į savo formą.
2. Stulpelyje „constraint" įveskite formulę, nurodančią atsakymo ribas.

### Pavyzdys

Apsvarstykime pavyzdį, kuriame norime pridėti asmens pajamų apribojimą. Apribojimas reikalauja, kad pajamos būtų nuo 0 iki 1 000 000 USD. Štai kaip galite nustatyti apribojimą:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Pajamos       | . >= 0 & . <= 1000000      |
{{< /table >}}

Aukščiau pateiktame pavyzdyje „." formulėje nurodo atgal į klausimo kintamąjį, kuris atspindi naudotojo įvestą reikšmę klausimui „Pajamos". Apribojimas „. >= 0 && . <= 1000000" užtikrina, kad įvestos pajamos būtų didesnės arba lygios 0 ir mažesnės arba lygios 1 000 000.


### Griežtas apribojimas

**Griežtas apribojimas** visiškai blokuoja formos pateikimą, jei įvesta reikšmė neatitinka išraiškos. Surašytojas negali tęsti, kol neįves tinkamos reikšmės.

Norėdami pridėti griežtą apribojimą, įveskite savo išraišką stulpelyje `constraint`. Pasirinktinai pridėkite žmogui suprantamą pranešimą stulpelyje `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Respondento amžius | `. > 0 and . <= 120` | Amžius turi būti nuo 1 iki 120 |
| decimal | temperature | Kūno temperatūra (°C) | `. >= 35 and . <= 42` | Temperatūra turi būti nuo 35°C iki 42°C |
| text | phone | Telefono numeris | `regex(., '^[0-9]{10}$')` | Įveskite 10 skaitmenų telefono numerį |
{{< /table >}}

#### Kelios sąlygos

Sujunkite sąlygas su `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### `regex()` naudojimas šablono tikrinimui

Funkcija `regex(value, pattern)` tikrina reikšmę pagal reguliariąją išraišką:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | El. pašto adresas | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Įveskite tinkamą el. pašto adresą |
| text | zip_code | Pašto kodas | `regex(., '^[0-9]{5}$')` | Įveskite 5 skaitmenų pašto kodą |
{{< /table >}}

#### Kitų laukų nuoroda apribojime

Naudokite `${fieldname}`, kad nurodytumėte reikšmes iš kitų klausimų:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | Pabaigos metai | `. >= ${start_year}` | Pabaigos metai turi būti po pradžios metų |
| decimal | loan_repaid | Grąžinta suma | `. <= ${loan_amount}` | Negalima grąžinti daugiau nei paskolos suma |
{{< /table >}}

### Švelnus perspėjimas

**Švelnus perspėjimas** (taip pat vadinamas švelniu apribojimu arba įspėjimu) įspėja surašytoją, kad reikšmė atrodo neįprasta, tačiau vis tiek leidžia tęsti. Tai naudinga, kai reikšmė yra techniškai galiojanti, bet statistiškai mažai tikėtina.

rtSurvey palaiko švelnius perspėjimus naudojant stulpelį `constraint` su specialiu `constraint_type` požiūriu arba per išvaizdą `soft` kartu su pastabos lauku.

Dažniausias modelis yra naudoti **pastabą** su `relevant` išraiška, kuri pažymi įtartiną reikšmę, kartu su **patvirtinimo** klausimu:

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Vaikų skaičius | |
| note | children_warning | Įspėjimas: Įvedėte ${children} vaikus. Patvirtinkite, kad tai teisinga. | `. > 15` |
| trigger | children_confirm | Patvirtinkite, kad vaikų skaičius yra teisingas | `${children} > 15` |
{{< /table >}}

#### Švelnus perspėjimas tik su constraint_message

Paprastesniam švelniajam perspėjimui galite suformuluoti apribojimą, kad perspėtų apie ekstremalias reikšmes, tačiau vis tiek leistų platų diapazoną:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | children | Vaikų skaičius | `. >= 0 and . <= 30` | Ši reikšmė atrodo labai didelė. Prašome patikrinti. |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
Skirtumas tarp griežtų ir švelniųjų apribojimų svarbus duomenų kokybei. Naudokite **griežtus apribojimus** logiškai neįmanomoms reikšmėms (neigiamam amžiui, temperatūroms virš 100°C). Naudokite **švelnius perspėjimus** statistiškai mažai tikėtinoms, bet ne neįmanomoms reikšmėms — nenorite blokuoti teisėtų ribinių atvejų.
{{% /alert %}}
