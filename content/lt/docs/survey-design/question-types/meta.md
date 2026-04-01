---
title: "Meta"
description: "Meta klausimų tipai automatiškai fiksuoja įrenginio, surašytojo ir laiko informaciją be respondento įvesties."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Meta klausimų tipai yra specialūs laukai, kurie užpildomi **automatiškai** — respondentas jų niekada nemato. Jie fiksuoja kontekstą apie pateikimą: kada jis buvo surinktas, kuris įrenginys buvo naudojamas ir kas jį surinko. Pridėkite juos darbalapyje `survey` kaip bet kurį kitą klausimų tipą; jie tiesiog nerodomi ekrane.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Meta laukams etiketės nėra būtinos, nes jos niekada nerodoma.

---

## Laiko meta laukai

### `start`

Įrašo **datą ir laiką, kada forma buvo atidaryta**. Saugoma ISO 8601 formatu (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Įrašo **datą ir laiką, kada forma buvo pateikta**. Kartu su `start` galite apskaičiuoti laiką, praleistą pildant formą:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Įrašo **dabartinę datą** (be laiko komponento). Saugoma kaip `YYYY-MM-DD`. Naudinga, kai reikia tik datos be pilno laiko žymos.

```
type  | name  | label
today | today |
```

---

## Įrenginio meta laukai

### `deviceid`

Įrašo **unikalų duomenų rinkimui naudojamo įrenginio identifikatorių**. Android sistemoje tai paprastai yra IMEI arba Android ID. Naudinga stebėti, kuris įrenginys pateikė kiekvieną formą, ir aptikti pasikartojančius pateikimus iš to paties įrenginio.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Įrašo **įrenginyje esančios SIM kortelės telefono numerį** (jei prieinamas). Gali būti tuščias, jei įrenginys neturi SIM kortelės arba numeris nėra saugomas SIM kortelėje.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Įrašo **SIM kortelės serijos numerį** (ICCID). Naudinga nustatyti, kuri SIM/operatorius buvo naudojamas.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Įrašo **IMSI (Tarptautinį Mobiliojo Abonento Identifikatorių)** — unikalų abonento identifikatorių SIM kortelėje.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Surašytojo meta laukai

### `username`

Įrašo **prisijungusio surašytojo naudotojo vardą** (paskyra, naudojama rtSurvey programoje). Tai patikimiausias būdas sekti, kas surinko kiekvieną pateikimą.

```
type     | name     | label
username | username |
```

### `email`

Įrašo **prisijungusio surašytojo el. pašto adresą**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Įrašo **telefono numerį, susietą su surašytojo paskyra** (jei sukonfigūruotas).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Audito žurnalas

### `audit`

Meta laukas `audit` įgalina **išsamų audito registravimą** — jis įrašo laiko žymėmis pažymėtą žurnalą kiekvieno klausimo, kurį aplankė surašytojas, kiek laiko jie praleido ties kiekvienu, ir (pasirinktinai) jų GPS vietą kiekviename žingsnyje. Audito žurnalas išsaugomas kaip atskiras `audit.csv` failas kartu su kiekvienu pateikimu.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Audito parametrai

| Parametras | Aprašymas |
|-----------|-------------|
| `location-priority` | GPS tikslumo lygis: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Minimali sekundžių trukmė tarp vietos fiksavimų |
| `location-max-age` | Maksimalus amžius (sekundėmis) talpykloje saugomos vietos, kurią priimti |

Audito žurnalas fiksuoja:
- Klausimo pavadinimą ir įvykio tipą (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Pradžios ir pabaigos laiko žymes kiekvienam įvykiui
- GPS koordinates (jei `location-priority` yra nustatytas)

{{% alert icon=" " context="warning" %}}
Laukas `audit` generuoja atskirą failą kiekvienam pateikimui. Įsitikinkite, kad jūsų duomenų apdirbimo procesas apdoroja tiek pagrindinį formos duomenų failą, tiek audito CSV.
{{% /alert %}}

---

## Pilnas pavyzdys

Tipinė namų ūkio apklausa gali apimti visus laiko ir surašytojo meta laukus:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Namų ūkio ID |
| ... | ... | ... |

---

## Geriausios praktikos

1. Visada įtraukite `start` ir `end` — jie yra nemokami, automatiniai ir neįkainojami kokybės stebėjimui.
2. Visada įtraukite `username` surašytojams sekti.
3. Įtraukite `deviceid`, kai norite aptikti pasikartojančius pateikimus ar sekti lauko įrenginius.
4. Naudokite `audit` apklausose su aukšta atsakomybe, kur reikia patikrinti, ar surašytojai iš tikrųjų aplankė kiekvieną klausimą.
5. SIM susiję laukai (`simserial`, `subscriberid`, `devicephonenum`) yra patikimi tik Android įrenginiuose su aktyviomis SIM kortelėmis — praleiskite juos tik planšetinių kompiuterių diegimams.

---

## Apribojimai

- Visi meta laukai yra **tik skaitymui** — jų negalima nurodyti ar modifikuoti kitais skaičiavimais.
- `username` ir `email` reikalauja, kad surašytojas būtų prisijungęs; jie bus tušti anoniminių pateikimų atveju.
- SIM/telefono meta laukai gali grąžinti tuščias reikšmes tik Wi-Fi planšetiniuose kompiuteriuose ir kai kuriose Android versijose dėl teisių apribojimų.
