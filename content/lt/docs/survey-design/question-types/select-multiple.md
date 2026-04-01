---
title: "Select_multiple"
description: "Select_multiple klausimai leidžia respondentams pasirinkti vieną ar daugiau parinkčių iš iš anksto apibrėžto sąrašo."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Klausimo tipas `select_multiple` rodo sąrašą, kuriame respondentas gali pasirinkti **vieną ar daugiau parinkčių**. Pagal numatymą pasirinkimai atvaizduojami kaip žymimieji langeliai. Saugoma reikšmė yra **tarpais atskirtų** visų pasirinktų pasirinkimų reikšmių sąrašas.

## Pagrindinė XLSForm specifikacija

**apklausos darbalaapis:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Kokias kultūras augina namų ūkis? |

**pasirinkimų darbalaapis:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Kukurūzai |
| crops | beans | Pupelės |
| crops | rice | Ryžiai |
| crops | vegetables | Daržovės |
| crops | other | Kita |

## Saugomų duomenų formatas

Eksportuotame stulpelyje pateikiamas tarpais atskirtų pasirinktų reikšmių sąrašas:

```
maize beans vegetables
```

Naudokite funkciją `selected()` — ne `=` — tikrinant select_multiple reikšmes išraiškose (žr. žemiau).

## Naudojimo atvejai

Select_multiple klausimai naudojami:

1. Kelių tinkamų atsakymų rinkimui (pvz., pajamų šaltiniai, auginamos kultūros, simptomai)
2. Žymimojo langelio stiliaus sutikimo elementams (pvz., „Pasirinkite viską, kas taikoma")
3. Kalbos ar įgūdžių inventoriams
4. Bet kuriam klausimui, kur keli atsakymai vienu metu yra galiojantys

## Išvaizdos parinktys

{{< table >}}
| Išvaizda | Aprašymas |
|------------|-------------|
| *(nė viena)* | Numatytieji žymimieji langeliai, po vieną eilutėje |
| `minimal` | Išskleidžiamasis kelių pasirinkimų valdiklis |
| `compact` | Kompaktiška tinklelis, stulpeliai prisitaiko prie ekrano pločio |
| `compact-N` | Kompaktiška tinklelis, fiksuotas N stulpelių skaičius |
| `horizontal` | Pasirinkimai išdėstyti horizontaliai eilutėje (žiniatinklis) |
| `horizontal-compact` | Horizontalus, kompaktiška tarpas (žiniatinklis) |
| `label` | Rodo tik etiketes, be žymimųjų langelių (naudokite su `list-nolabel`) |
| `list-nolabel` | Rodo tik žymimuosius langelius, be etikečių (naudokite su `label`) |
| `columns(N)` | Rodyti N stulpeliuose (rtSurvey plėtinys) |
{{< /table >}}

### Pavyzdys: 3 stulpelių kompaktiška išdėstymas

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Pasirinkite visus stebimus simptomus | compact-3 |

## `selected()` naudojimas išraiškose

Kadangi saugoma reikšmė yra tarpais atskirtą eilutė, **būtina** naudoti `selected()`, kad patikrintumėte, ar konkretus pasirinkimas buvo pasirinktas. `=` naudojimas neveiks teisingai.

### `relevant` stulpelyje

Rodyti tolesni klausimą tik jei „kita" buvo pasirinktas:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Kokios kultūros auginamos? | |
| text | crops_other | Nurodykite kitas kultūras | `selected(${crops_grown}, 'other')` |

### `constraint` stulpelyje

Reikalauti bent 2 pasirinkimų:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Pasirinkite bent 2 problemas |

Apriboti iki maks. 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Pasirinkite ne daugiau kaip 3 prioritetus |

## „Nė vienas iš pateiktų" / išskirtinė parinktis

Dažnas modelis yra viena parinktis, nesuderinama su visomis kitomis. Naudokite `constraint` ją taikyti:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Pasirinkite visas esamas problemas | `not(selected(., 'none') and count-selected(.) > 1)` | „Nė vienas" negali būti pasirinktas kartu su kitomis parinktimis |

**pasirinkimai:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Vandens trūkumas |
| issues | roads | Blogi keliai |
| issues | health | Sveikatos paslaugų stoka |
| issues | none | Nė vienas iš pateiktų |

## Pasirinkimų skaičiavimas ir apibendrinimas

| Funkcija | Pavyzdys | Rezultatas |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Pasirinktų pasirinkimų skaičius |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | tiesa/melas |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Pirmoji pasirinkta reikšmė |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Reikšmės etiketė |

## Geriausios praktikos

1. Visada naudokite `selected()` stulpeliuose `relevant`, `constraint` ir `calculate` — niekada `=` ar `!=`.
2. Pridėkite apribojimą, kad apribotumėte maksimalų pasirinkimų skaičių, jei klausimo dizainas to reikalauja.
3. Įtraukite parinktį „Nė vienas" ar „Netaikoma", kai nulis pasirinkimų yra galiojantis atsakymas.
4. Ilgiems sąrašams (15+ pasirinkimų) naudokite `minimal` (kelių pasirinkimų išskleidžiamąjį), kad išvengtumėte per didelio slinkimo.
5. Eksportuojant duomenis, naudokite eilutės padalijimą savo analizės įrankyje — tarpais atskirtas formatas reikalauja padalijimo prieš sukimą.

## Apribojimai

- Select_multiple reikšmių negalima tiesiogiai lyginti su `=`. Visada naudokite `selected()`.
- Kompaktiška išvaizda gali netinkamai atvaizduotis labai ilgoms pasirinkimų etiketėms.
- Filtruojant pasirinkimus su `choice_filter`, filtravimas taikomas visiems rodomiems pasirinkimams, lygiai taip pat kaip `select_one`.
