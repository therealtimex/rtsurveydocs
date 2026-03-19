---
title: "Dinaminis klausimo tipas"
description: "Dinaminis klausimo tipas leidžia lauko klausimo tipui ir valdikliui būti nustatytam vykdymo metu pagal API atsakymą ar apskaičiuotą reikšmę."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Funkcija **Dinaminis klausimo tipas** leidžia lauko įvesties valdikliui ir tikrinimo elgsenai būti nustatytam **vykdymo metu**, o ne formos kūrimo metu. Tai pažangus rtSurvey plėtinys, naudojamas, kai renkamų duomenų tipas priklauso nuo serverio konfigūracijos, API atsakymo ar ankstesnio lauko reikšmės.

Dažnas naudojimo atvejis — konfigūruojamas patikrinimo kontrolinis sąrašas, kuriame serveris apibrėžia, kurie laukai yra privalomi, koks jų tipas (text, integer, select ir kt.) ir kokios parinktys yra prieinamos — nereikia atstatyti formos kiekvienai konfigūracijai.

---

## Kaip tai veikia

Laukas, pažymėtas kaip dinaminis klausimo tipas, naudoja `callapi()`, kad gautų konfigūraciją iš API. API atsakymas apibrėžia:

- Atvaizdinti įvesties tipą (text, integer, select_one ir kt.)
- Prieinamus pasirinkimus (pasirinkimo tipams)
- Tikrinimo taisykles

Laukas viduje pažymimas `specialFeature: isDynamicQuestionType`, kas nurodo formos varikliu naudoti API atsakymą valdikliui sukonstruoti, o ne statinę formos apibrėžtį.

---

## Konfigūracija

### 1 žingsnis: lauko konfigūracijos gavimas

Naudokite `calculate` lauką su `callapi()` dinaminei konfigūracijai gauti:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### 2 žingsnis: konfigūracijos nuoroda dinaminiame lauke

Dinaminis laukas naudoja `callapi-verify()` savo `appearance` arba `constraint`, kad susietų su gauta konfigūracija:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Patikrinimo rezultatas | `callapi-verify(dynamicParams)` |

Formos variklis nuskaito `field_config` ir dinamiškai nustato, ar `inspection_result` atvaizduoti kaip `text`, `integer` ar `select_one` lauką.

---

## API atsakymo formatas

API turėtų grąžinti JSON objektą, aprašantį lauko konfigūraciją. Tipiškas atsakymas:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Praėjo"},
      {"value": "fail", "label": "Nepraėjo"},
      {"value": "na", "label": "Netaikoma"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Pavyzdys: konfigūruojama patikrinimo forma

Patikrinimo forma, kurioje kontrolinio sąrašo elementai ir jų atsakymų tipai gaunami iš serverio pagal patikrinimo kategoriją:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Patikrinimo tipas | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | 1 elementas | `callapi-verify(dynamicParams)` | |
| text | item_2 | 2 elementas | `callapi-verify(dynamicParams)` | |
| text | item_3 | 3 elementas | `callapi-verify(dynamicParams)` | |

Serveris grąžina tinkamą valdiklio tipą, etiketę, pasirinkimus ir tikrinimą kiekvienam elementui pagal `insp_type`.

---

## Geriausios praktikos

1. Naudokite dinaminius klausimų tipus tik tada, kai lauko struktūra iš tikrųjų keičiasi vykdymo metu — statinėms formoms naudokite standartinius klausimų tipus.
2. Užtikrinkite, kad konfigūracijos API reaguoja greitai (per 2 sekundes) ir yra prieinama lauke.
3. Visada apibrėžkite prasmingą atsarginį variantą formoje, kai API nepasiekiama — paprastas `text` laukas su pastaba yra geresnis nei sugedęs valdiklis.
4. Versijuokite savo API atsakymo schemą — atsakymo formato pakeitimai turės įtakos visoms aktyviosioms formoms, naudojančioms tą galiuklį.
5. Prieš diegimą patikrinkite kiekvieną lauko tipų derinį, kurį API gali grąžinti.

## Apribojimai

- Dinaminiai klausimų tipai reikalauja tinklo ryšio konfigūracijai gauti.
- Pilnas valdiklių tipų diapazonas, dinamiškai prieinamas, priklauso nuo rtSurvey kliento versijos — patikrinkite savo tikslinio versijos.
- Tai pažangus rtSurvey plėtinys, neturintis atitikmens standartinėje XLSForm specifikacijoje.
- Derinimo klaidos sunkiau atsekamos, nes lauko apibrėžtis iš dalies yra formoje ir iš dalies API atsakyme.
