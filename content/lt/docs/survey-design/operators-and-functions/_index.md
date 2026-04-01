---
title: "Operatoriai ir funkcijos"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Išraiškos rtSurvey sistemoje rašomos **XPath 1.0** poaibiu, išplėstu JavaRosa/ODK funkcijomis ir pasirinktinėmis rtSurvey funkcijomis. Išraiškas naudojate stulpeliuose `calculate`, `constraint`, `relevant`, `required` ir `default` savo XLSForm.

## Lauko reikšmių nuoroda

Naudokite `${lauko_pavadinimas}`, kad nurodytumėte kito lauko reikšmę:

```
${age} > 18
```

Naudokite `.` (vieną tašką), kad nurodytumėte **dabartinio lauko reikšmę** — dažniausiai naudojama `constraint` išraiškose:

```
. >= 0 and . <= 100
```

Naudokite `..`, kad nurodytumėte pirminę grupę (pažangus naudojimas kartojimose).

## Išraiškų sintaksė

Išraiškos laikosi standartinių XPath taisyklių:

- **Eilutės** turi būti uždarytos viengubomis kabutėmis: `'yes'`
- **Skaičiai** rašomi tokie, kokie yra: `42`, `3.14`
- **Loginiai** rezultatai naudojami `relevant`, `required` ir `constraint` — bet kuri netuščia, ne nulinė reikšmė yra tiesa
- Tarpas aplink operatorius ignoruojamas

{{% alert icon=" " context="warning" %}}
Visada naudokite tiesias kabutes (`'` arba `"`) — niekada „išmanias kabutes" (garbanoti). Turtingo teksto redaktoriai dažnai automatiškai konvertuoja kabutes ir sugadins jūsų išraiškas.
{{% /alert %}}

## Šio skyriaus sekcijos

- **[Operatoriai](operators)** — palyginimo operatoriai (`=`, `!=`, `>`, `<`, `>=`, `<=`) ir loginiai operatoriai (`and`, `or`, `not()`)
- **[Funkcijos](functions)** — eilutės, pasirinkimo, skaičių, datos/laiko, loginės, geografinės ir pagalbinės funkcijos
- **[Nuorodos](references)** — kaip nurodyti laukus ir konteksto reikšmes

## Greiti pavyzdžiai

| Naudojimo atvejis | Išraiška |
|----------|------------|
| Rodyti, jei amžius viršija 18 | `${age} > 18` |
| Rodyti tik jei pasirinkta „taip" | `${consent} = 'yes'` |
| Reikalauti, jei kitas laukas nėra tuščias | `${name} != ''` |
| Skaičiuoti bendrą sumą | `${adults} + ${children}` |
| Sujungti vardą | `concat(${first_name}, ' ', ${last_name})` |
| Šiandienos data | `today()` |
| Patikrinti, ar parinktis pasirinkta | `selected(${interests}, 'sports')` |
