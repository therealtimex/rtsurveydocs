---
title: "Garsas"
description: "Garso klausimai leidžia respondentams įrašyti ir pateikti garso failus kaip apklausos dalį."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Klausimo tipas `audio` leidžia respondentams **įrašyti garsą** arba įkelti esamą garso failą kaip savo apklausos atsakymo dalį. Tai naudinga žodinėms ataskaitoms, aplinkos garsams, liudijimams ar bet kokiai informacijai, kurią geriau perteikti balsu nei tekstu.

## Pagrindinė XLSForm specifikacija

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Įrašykite savo komentarus    |

## Naudojimo atvejai

Garso klausimai dažnai naudojami:

1. Atviro pobūdžio žodiniams atsakymams fiksuoti, sumažinant surašytojo rašymo naštą
2. Liudijimams, asmeninėms istorijoms ar žodinei istorijai įrašyti
3. Aplinkos garsams dokumentuoti (pvz., triukšmo lygiai prie infrastruktūros)
4. Balso mėginiams lingvistiniams ar sveikatos tyrimams rinkti
5. Respondentams leidžiant pridėti žodines patikslinimus prie skaitinių ar pasirinkimo atsakymų

## Duomenų formatas

Garso failai saugomi kaip dvejetainiai priedai kartu su formos pateikimu, paprastai:

- **Formatas:** MP3 arba AAC (mobiliųjų įrenginių įrašymas); WAV (aukštos kokybės įrašymas)
- **Pavadinimas:** `{egzemplioriausID}-{lauko_pavadinimas}.mp3` (arba atitinkamas)
- **Saugykla:** Įkeltas į serverio medijos aplanką ir susietas su pateikimo įrašu
- **Prieiga:** Galima groti ir atsisiųsti iš pateikimų valdymo sąsajos

## rtSurvey plėtiniai

### Maksimali trukmė

Naudokite stulpelį `parameters`, kad apribotumėte įrašymo ilgį:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Įrašykite interviu | `max-duration=120` |

`max-duration` yra sekundėmis. Įrašytuvas automatiškai sustoja pasiekus limitą.

### Kokybės nustatymai

Įrašymo kokybę galima nustatyti per `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Įrašykite atsiliepimą | `quality=normal` |

Palaikomos reikšmės: `low`, `normal` (numatytasis), `voice-only`. `voice-only` optimizuoja kalbamąjį garsą su triukšmo mažinimu.

### Atkūrimas prieš pateikimą

Mobiliajame įrenginyje surašytojas gali atkurti įrašytą klipą prieš tęsiant. Tai įgalinta pagal numatymą — jokios konfigūracijos nereikia.

### Natyvios garso programos integracija

Android ir iOS sistemose `audio` paleidžia įrenginio natyvią įrašymo programą. Žiniatinklyje naudoja naršyklės integruotą MediaRecorder API.

## Naudojimo pavyzdžiai

### Su maksimalia trukme ir patarimu

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Papasakokite apie incidentą savo žodžiais | Kalbėkite aiškiai. Įrašymas sustoja po 3 minučių. | `max-duration=180` |

### Sąlyginis garsas — tik jei buvo pranešta apie problemą

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Ar buvo rasta problema? | | |
| audio | issue_audio | Įrašykite problemos aprašymą | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Geriausios praktikos

1. Aiškiai nurodykite etiketėje ar patarimo stulpelyje, ką surašytojas turėtų sakyti ir kiek laiko.
2. Naudokite `max-duration`, kad išvengtumėte pernelyg didelių failų vietovėse su lėtu įkėlimo greičiu.
3. Prieš pradedant įrašymą informuokite respondentus — netikėtas įrašymas gali sukelti privatumo rūpesčių.
4. Prieš diegimą patikrinkite įrašymą tiksliniais įrenginiais ir tinklo sąlygomis.
5. Naudokite `quality=voice-only` interviu stiliaus įrašymams, kad sumažintumėte failo dydį neprarandant suprantamumo.

## Apribojimai

- Garso failai gali būti dideli (2 minučių įrašas normalios kokybės yra apie 2–4 MB) — atsižvelkite į tai vertindami duomenų planą ir įkėlimo laiko sąmatas.
- Ne visos naršyklės palaiko MediaRecorder API — Chrome ir Firefox veikia patikimai; Safari senesnėse iOS versijose gali turėti problemų.
- Garso atsakymų transkribavimas reikalauja papildomo poapdorojimo (rankinio arba automatinio kalbos-teksto).
- Privatumo taisyklės gali apriboti balsų įrašymą — patikrinkite vietos duomenų apsaugos reikalavimus.
