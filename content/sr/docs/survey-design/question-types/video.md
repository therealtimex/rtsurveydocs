---
title: "Video"
description: "Pitanja tipa video dozvoljavaju ispitanicima da snime i pošalju video datoteke kao deo ankete."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Tip pitanja `video` omogućava ispitanicima da **snime video** ili otpreme postojeću video datoteku kao deo svog odgovora na anketu. Koristan je za hvatanje vizuelnih dokaza, demonstracija, uslova okoline ili bilo koje informacije od koje koristi kretanje i audio zajedno.

## Osnovna XLSForm specifikacija

| type  | name        | label                              |
|-------|-------------|-------------------------------------|
| video | demo_video  | Molimo snimite kratku demonstraciju |

Za više detalja o standardnom tipu pitanja video, pogledajte [XLSForm specifikaciju](https://xlsform.org/en/#question-types).

## Upotrebe

Pitanja tipa video se uobičajeno koriste za:

1. Dokumentovanje terenskih uslova — oštećenja puteva, stanje infrastrukture, zdravlje useva
2. Snimanje demonstracija proizvoda ili provera usklađenosti sa procedurama
3. Prikupljanje video svedočanstava od ispitanika
4. Hvatanje dokaza koji zahtevaju prostorni kontekst (npr. veličina i obim problematičnog područja)
5. Dokumentacija pre/posle za ankete praćenja i evaluacije

## Format podataka

Video datoteke se čuvaju kao binarne privitke:

- **Format:** MP4 ili MOV (mobilno snimanje)
- **Imenovanje:** `{instanceID}-{ime_polja}.mp4` (ili ekvivalent)
- **Skladište:** Otpremljeno na serversku medijsku fasciklu i povezano sa zapisom slanja
- **Pristup:** Dostupno za reprodukciju i preuzimanje iz interfejsa za upravljanje slanjima

## rtSurvey proširenja

### Maksimalno trajanje

Koristite kolonu `parameters` za ograničavanje dužine snimanja:

| type | name | label | parameters |
|------|------|-------|------------|
| video | site_visit | Snimite uslove na lokaciji | `max-duration=60` |

`max-duration` je u sekundama. Snimanje se automatski zaustavlja na granici.

### Kvalitet / rezolucija

Kontrolišite rezoluciju snimanja putem `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| video | evidence | Snimite video dokaz | `quality=low` |

Podržane vrednosti: `low` (brže otpremanje), `normal` (podrazumevano), `high`. Koristite `low` u područjima sa ograničenom vezom.

### Otpremanje postojećeg videa

Na mobilnom uređaju, ispitanik može izabrati da **otpremi postojeći video** iz galerije uređaja umesto da snimi novi. Ovo je podrazumevano omogućeno u nativnoj integraciji kamere/galerije.

### Reprodukcija pre slanja

Na mobilnom uređaju, snimljeni klip se može pregledati pre nastavka. Nije potrebna dodatna konfiguracija.

## Primer upotrebe

### Video inspekcije lokacije sa ograničenjem

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| video | site_video | Snimite vodnu tačku | Prošetajte oko celokupnog objekta. Maks. 90 sekundi. | `max-duration=90 quality=normal` |

### Uslovni video — samo ako je prijavljeno oštećenje

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | damage_found | Da li je pronađeno oštećenje? | | |
| video | damage_video | Snimite video oštećenja | `${damage_found} = 'yes'` | `${damage_found} = 'yes'` |

## Najbolje prakse

1. Postavite `max-duration` — neograničena video snimanja mogu lako premašiti 100 MB i ne uspeti da se otpreme na slabim vezama.
2. Koristite `quality=low` za ankete praćenja gde su vizuelni dokazi potrebni ali fini detalji nisu — dramatično smanjuje veličinu datoteke.
3. Napišite specifična uputstva za snimanje u koloni `hint` (npr. "Prošetajte oko cele zgrade, držite kameru mirno").
4. Razmotrite da li je video neophodan — fotografija (`image`) je obično dovoljna za statičke dokaze i proizvodi znatno manje datoteke.
5. Testirajte performanse otpremanja na stvarnoj terenskoj mreži pre primene.

## Ograničenja

- Video datoteke su veoma velike — 1-minutni video pri normalnom kvalitetu je obično 20–60 MB u zavisnosti od uređaja.
- Otpremanje velikih video datoteka zahteva dobru mrežnu vezu; razmotrite zahtevanje sinhronizacije putem Wi-Fi-ja za formulare sa puno videa.
- Nisu svi veb preglednici podržani za snimanje videa putem MediaRecorder — Chrome je najpouzdaniji.
- Analiza video odgovora je ručna i vremenski zahtevna; koristite štedljivo i samo kada video sadržaj dodaje jedinstvenu vrednost.
