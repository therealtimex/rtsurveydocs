---
title: "Pažangūs kartojimai"
description: "Pažangūs kartojimų grupių modeliai: dinaminis skaičius, įdėtiniai kartojimai, kartojimų duomenų apibendrinimas ir reikšmių nuoroda per kartojimus."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Šiame puslapyje aprašomi pažangūs kartojimų grupių naudojimo modeliai rtSurvey sistemoje. Pagrindinę informaciją apie kartojimų grupių konfigūravimą rasite [Grupavimas ir kartojimai](../repeats).

---

## Dinaminis kartojimų skaičius

Pagal numatymą surašytojas nusprendžia, kiek kartų kartoti. Galite fiksuoti kartojimų skaičių naudodami `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Namų ūkio narys | `${num_members}` |
| text | member_name | Nario vardas | |
| integer | member_age | Amžius | |
| end_repeat | | | |

Kartojimas vykdomas tiksliai `${num_members}` kartų, kur `num_members` buvo surinkta anksčiau formoje. Surašytojas negali pridėti ar pašalinti egzempliorių.

---

## Indeksuota prieiga: `indexed-repeat()`

Pasiekite konkretaus kartojimo egzemplioriaus lauko reikšmę **iš kartojimų grupės išorės** naudodami `indexed-repeat(kartotasLaukas, kartojimųGrupė, indeksas)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Tai naudinga kuriant suvestinių laukus arba nurodant „pagrindinio" nario duomenis po kartojimo.

---

## Dabartinio egzemplioriaus pozicija: `index()`

Kartojimų grupės viduje `index()` grąžina dabartinio egzemplioriaus 1 nuo pradžios skaičiuojamą poziciją. Naudokite jį kiekvienam kartojimui žymėti arba unikalių identifikatorių kūrimui:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Sklypas |
| note | plot_label | Sklypo numeris ${index()} |
| text | plot_id | Sklypo ID |
| end_repeat | | |

---

## Laukų nuoroda tame pačiame egzemplioriuje

Kartojimo viduje naudokite `${lauko_pavadinimas}`, kad nurodytumėte kitą lauką **tame pačiame kartojimo egzemplioriuje**. Nereikia `indexed-repeat()` toje pačioje kilpoje:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Narys | |
| text | member_name | Vardas | |
| integer | member_age | Amžius | |
| text | school_name | Mokyklos pavadinimas | `${member_age} < 18` |
| end_repeat | | | |

---

## Pirminių laukų nuoroda iš kartojimo vidaus

Laukai už kartojimų grupės ribų (aukščiau) gali būti nurodomi normaliai su `${lauko_pavadinimas}`:

| type | name | label |
|------|------|-------|
| text | village | Kaimo pavadinimas |
| begin_repeat | plots | Žemės ūkio sklypas |
| note | plot_context | Sklypai ${village} kaime |
| end_repeat | | |

---

## Kartojimų duomenų apibendrinimas

Naudokite kartojimų agregavimo funkcijas **kartojimų grupės išorėje** apibendrinimui:

| Funkcija | Pavyzdys | Aprašymas |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | Egzempliorių skaičius |
| `sum(field)` | `sum(${loan_amount})` | Skaitinio lauko suma |
| `min(field)` | `min(${member_age})` | Minimali reikšmė |
| `max(field)` | `max(${member_age})` | Maksimali reikšmė |
| `join(sep, field)` | `join(', ', ${member_name})` | Kableliais atskirtas sąrašas |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Sąlyginis skaičius |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Sąlyginė suma |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Sąlyginis sujungimas |

### Pavyzdys: namų ūkio suvestinė

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Kiek narių? | |
| begin_repeat | members | Narys | `${num_members}` |
| text | member_name | Vardas | |
| integer | member_age | Amžius | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} nariai; ${children_count} iki 18 metų. Suaugusieji: ${adult_names} | |

---

## Įdėtiniai kartojimai

Kartojimų grupė gali turėti kitą kartojimų grupę. Naudokite tai atsargiai — įdėtiniai kartojimai prideda sudėtingumo ir gali klaidinti surašytojus.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Namų ūkis |
| text | hh_id | Namų ūkio ID |
| begin_repeat | hh_members | Narys |
| text | member_name | Nario vardas |
| end_repeat | | |
| end_repeat | | |

Norėdami nurodyt lauką išoriniame kartojime iš vidinio kartojimo, naudokite `${lauko_pavadinimas}` — jis išsprendžia iki artimiausio atitinkančio pirminio:

`hh_members` kartojimo viduje `${hh_id}` grąžina **dabartinio** namų ūkio ID, o ne visų namų ūkių.

---

## Reitingas kartojimų grupėse: `rank-index()`

Kai kartojimo viduje yra `rank` laukas, naudokite `rank-index(egzemplioriausNumeris, kartotasLaukas)` iš išorės, kad gautumėte konkretaus egzemplioriaus eilinį reitingą:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` grąžina aukščiausio balo egzemplioriaus indeksą.

---

## Geriausios praktikos

1. Visada naudokite `repeat_count`, kai kartojimų skaičius yra žinomas iš anksto — tai neleidžia surašytojams atsitiktinai pridėti ar pašalinti egzempliorių.
2. Laikykite kartojimų grupes sutelktas — kartojimas su 20+ klausimų kiekvienam egzemplioriui yra sunku naršyti.
3. Aiškiai pavadinkite kartojimų grupes (pvz., `household_members`, o ne `repeat1`) — pavadinimas rodomas funkcijų skambučiuose ir eksportuotų duomenų.
4. Patikrinkite su maksimaliu tikėtinu egzempliorių skaičiumi, kad patikrintumėte našumą.
5. Naudokite `field-list` išvaizdą kartojimų grupėje, kad rodytumėte visus laukus viename ekrane kiekvienam egzemplioriui (mobilieji).

---

## Apribojimai

- `indexed-repeat()` reikalauja galiojančio indekso (nuo 1 iki egzempliorių skaičiaus) — už diapazono ribų esantys indeksai grąžina tuščią reikšmę.
- Įdėtiniai kartojimai daugiau nei 2 lygių nerekomenduojami ir gali sukelti ekrano problemų kai kuriuose klientuose.
- Agregavimo funkcijos (`sum`, `count` ir kt.) veikia visoje kartojimų grupėje — negalite agreguoti egzempliorių pogrupį be `*-if` variantų.
