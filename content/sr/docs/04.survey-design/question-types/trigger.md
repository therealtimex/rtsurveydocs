---
title: "Trigger / Acknowledge"
description: "Pitanja tipa trigger prikazuju izjavu koju anketar mora eksplicitno potvrditi pre nastavka."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Tip pitanja `trigger` (poznat i kao `acknowledge`) prikazuje **izjavu sa potvrdnim okvirom**. Anketar mora označiti potvrdni okvir da bi potvrdio da je pročitao i razumeo izjavu pre nego što mu formular dozvoli nastavak. Nijedna podatkovna vrednost se ne čuva — samo da li je potvrdni okvir označen.

## Osnovna XLSForm specifikacija

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Ispitanik je dao usmenu informisanu saglasnost. |

Ili koristeći pseudonim `acknowledge`:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Ispitanik je dao usmenu informisanu saglasnost. |

I `trigger` i `acknowledge` su ekvivalentni — koristite koji god vaša platforma dokumentuje.

## Upotrebe

Pitanja tipa trigger/acknowledge se uobičajeno koriste za:

1. **Informisana saglasnost** — potvrda da je anketar dobio saglasnost pre beleženja osetljivih podataka
2. **Meka upozorenja** — upozorenje o neobičnoj vrednosti i zahtevanje eksplicitne potvrde pre nastavka
3. **Stavke kontrolne liste** — potvrda da je fizičko posmatranje završeno (npr. "Direktno sam posmatrao izvor vode")
4. **Uputstva** — primoravanje anketara da potvrdi uputstvo na nivou sekcije pre nastavka
5. **Provere kvaliteta** — označavanje vrednosti van granica i zahtevanje od anketara da ih verifikuje

## Primer upotrebe

### Potvrda saglasnosti

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Ispitanik je dao usmenu informisanu saglasnost za učešće u ovoj anketi. | yes |

### Meko upozorenje za vrednosti van granica

Koristi se zajedno sa izrazom `relevant` da se trigger prikaže samo kada se unese sumnjiva vrednost:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Broj dece | | |
| trigger | children_confirm | Uneli ste ${children} dece. Molimo verifikujte sa ispitanikom i tapnite OK za potvrdu. | `${children} > 10` | `${children} > 10` |

### Potvrda uputstva na početku sekcije

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Sekcija B: Korišćenje poljoprivrednog zemljišta. Postavite sva pitanja u ovoj sekciji samo nosiocu domaćinstva. |

## Pravljenje trigger-a obaveznim

Dodajte `required: yes` da biste sprečili napredovanje dok se okvir ne označi:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Sva bezbednosna oprema je prisutna i funkcionalna. | yes | Morate potvrditi pre nastavka. |

## Uslovni prikaz

Prikazujte trigger samo kada je ispunjen uslov:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Da li domaćinstvo ima bunar? | |
| trigger | well_observation | Potvrdite da ste direktno posmatrali stanje bunara. | `${has_well} = 'yes'` |

## Razlika u odnosu na `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Prikazuje tekst | Da | Da |
| Zahteva interakciju | Ne | Da (mora biti označen) |
| Čuva podatke | Ne | Ne (samo OK/označeno) |
| Može blokirati napredovanje | Ne | Da (sa `required`) |

## Najbolje prakse

1. Zadržite oznake trigger-a konciznim i operativnim — anketar treba moći da pročita i potvrdi za nekoliko sekundi.
2. Uvek dodajte `required: yes` kada je potvrda obavezna.
3. Koristite trigger-e za saglasnost i bezbednosne provere gde vam treba revizijski trag da je anketar potvrdio.
4. Kombinujte sa `relevant` za uslovne meke alarme kako bi se trigger pojavio samo kada vrednost zahteva verifikaciju.

## Ograničenja

- Polja trigger ne čuvaju smislenu podatkovu vrednost — samo beleže da je okvir označen.
- Widget trigger se prikazuje kao jednostavan potvrdni okvir/dugme na većini klijenata; nije potpuni elektronski potpis.
