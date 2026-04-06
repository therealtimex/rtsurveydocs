---
title: "Programos API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI leidžia naudotojams įkelti sistemos metaduomenis iš programos naudojant skirtingus metodus FormEngine ir DMView. Ji suteikia prieigą prie įvairių duomenų raktų konkrečiai informacijai gauti iš programos.

XLSForm galite naudoti funkciją `pulldata()` su šia sintakse:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: šis raktažodis informuoja FormEngine, kad duomenis reikia įkelti iš App API.
- `'data-key'`: tai yra duomenų raktas, kurį norite įkelti iš App API.
- Jei duomenų raktas yra neteisingas arba nepalaikomas, skaičiavimas grąžins „n/a".

Čia pateikiami palaikomi duomenų raktai, kuriuos galite naudoti su App API:

`osPlatform`: grąžina dabartinį OS pavadinimą (Android arba iOS) ir OS versiją. Žiniatinklio platformos grąžins tuščią reikšmę.

`appPlatform`: grąžina programos platformos pavadinimą, kuris yra `rtSurvey`.

`appVersion`: grąžina programos versijos pavadinimą.

`getDisplayWidth`: grąžina įrenginio ekrano plotį pikseliais.

`getDisplayHeight`: grąžina įrenginio ekrano aukštį pikseliais.

`getScreenSize`: grąžina įrenginio ekrano dydį coliais.

`projectCode`: grąžina dabartinio projekto kodą svetainės, prie kurios naudotojas prisijungė.

`projectURL`: grąžina dabartinio projekto URL svetainės, prie kurios naudotojas prisijungė. Numatytoji/atsarginė reikšmė yra tuščias tekstas ("").

`startingPoint`: grąžina taško, kuris paleidžia formą, kelią. Daugiau informacijos rasite skyriuje „Formos pradžios taškas".

`serverTime`: grąžina geriausią galimą serverio datos ir laiko aproksimaciją.

`user.[attribute]`: grąžina dabartinio naudotojo atributus pagal nurodytą atributo raktą. Galimus atributų raktus rasite lentelėje „Naudotojo atributai".

Derinkite toliau pateiktus atributų raktus su „user." funkcijoje `pulldata()` parametruose, kad gautumėte dabartinio naudotojo informaciją. Pavyzdžiui, naudokite `user.username`, `user.email` ir kt.

| Atributo raktas      | Aprašymas                            |
|----------------------|--------------------------------------|
| username             | Naudotojo vardas                      |
| name                 | Pilnas naudotojo vardas               |
| staffCode            | Naudotojo personalo kodas             |
| phone                | Naudotojo telefono numeris            |
| email                | Naudotojo el. pašto adresas           |
| description          | Aprašymo tekstas naudotojo informacijoje |
| organization_id      | Organizacijos ID, kuriai priklauso naudotojas |
| organization_name    | Organizacijos pavadinimas, kuriai priklauso naudotojas |
| team_id              | Komandos ID, kuriai priklauso naudotojas |
| supervisor_id        | Naudotojo supervisoriaus ID           |
| is_supervisor        | 1 jei naudotojas yra supervisorius, 0 jei ne |

`instancePath`: grąžina dabartinio egzemplioriaus aplanko kelią.

`appLanguage`: grąžina dabartinę programos kalbą, nustatytą programos nustatymuose (pvz., vi, en).

`openArgs.[attribute]`: grąžina atviros formos argumentą, perduotą iš ActionButton (act_fill_form, act_get_instance). Numatytoji/atsarginė reikšmė yra tuščias tekstas ("").

`primaryAppColor`: nuskaito pagrindinę programos spalvą.

---

## Naudojimo pavyzdžiai

### Surašytojo vardo ir organizacijos saugojimas

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Naudokite juos pastabų etiketėse audito tikslais:
```
note | interviewer_info | Apklausėjas: ${enumerator_name} (${enumerator_org})
```

### Įrenginio ir ekrano informacija

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Naudinga trikčių šalinimui: eksportuokite `device_platform` ir `app_ver` kartu su savo duomenimis, kad nustatytumėte, kurios įrenginio versijos buvo naudotos kiekvienam pateikimui.

### Serverio laikas vietoj įrenginio laiko

Įrenginių laikrodžiai gali būti netikslūs. Patikimesniam laiko žymei naudokite `serverTime`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Sąlyginė logika pagal naudotojo vaidmenį

Rodyti tik supervisoriams skirtą sekciją tik supervisoriams:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Supervisoriaus peržiūra | `${is_supervisor} = '1'` |
| text | supervisor_notes | Supervisoriaus pastabos | |
| end_group | | | |

### Argumentų perdavimas iš veiksmo mygtuko

Kai forma paleidžiama iš `act_fill_form` veiksmo mygtuko su pasirinktiniais argumentais:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Veiksmo mygtukas turi perduoti argumentus su atitinkamais raktais (pvz., `household_id`, `task_code`).

### Projekto informacijos naudojimas

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Pastabos

- Visi `pulldata('app-api', ...)` kvietimai įvertinami atidarius formą ir neįvertinami dinamiškai sesijos metu (išskyrus `serverTime` ir `now()`).
- Jei raktas nepalaikomas arba duomenys nepasiekiami, funkcija grąžina `'n/a'` (ne tuščią eilutę — tikrinkite su `!= 'n/a'`, o ne su `!= ''`).
- `openArgs` reikšmės pasiekiamos tik tada, kai forma paleidžiama iš veiksmo mygtuko; kitu atveju jos grąžina tuščią eilutę.
