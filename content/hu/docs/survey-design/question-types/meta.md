---
title: "Meta"
description: "A meta kérdéstípusok automatikusan rögzítik az eszközzel, a kérdezőbiztossal és az időzítéssel kapcsolatos információkat a válaszadó közreműködése nélkül."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

A meta kérdéstípusok speciális mezők, amelyek **automatikusan** kerülnek kitöltésre – a válaszadó soha nem látja őket. A beküldés kontextusát rögzítik: mikor gyűjtötték, melyik eszközzel, és ki gyűjtötte. Adja hozzá őket a `survey` munkalapon, mint bármely más kérdéstípust; egyszerűen nem jelennek meg a képernyőn.

## Alapvető XLSForm-specifikáció

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

A meta mezőknél nem szükséges felirat, mivel soha nem jelennek meg.

---

## Időzítési meta mezők

### `start`

Rögzíti az **űrlap megnyitásának dátumát és időpontját**. ISO 8601 formátumban tárolódik (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Rögzíti az **űrlap beküldésének dátumát és időpontját**. A `start` mezővel együtt kiszámítható az űrlap kitöltéséhez szükséges idő:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Rögzíti az **aktuális dátumot** (időpont-komponens nélkül). `YYYY-MM-DD` formátumban tárolódik. Hasznos, ha csak a dátumra van szükség a teljes időbélyeg nélkül.

```
type  | name  | label
today | today |
```

---

## Eszköz meta mezők

### `deviceid`

Rögzíti az **adatgyűjtéshez használt eszköz egyedi azonosítóját**. Androidon ez általában az IMEI vagy az Android ID. Hasznos annak nyomon követéséhez, hogy melyik eszköz nyújtotta be az egyes űrlapokat, és az ugyanarról az eszközről érkező ismétlődő beküldések észleléséhez.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Rögzíti az **eszközben lévő SIM-kártya telefonszámát** (ha elérhető). Üres lehet, ha az eszköznek nincs SIM-kártyája, vagy ha a szám nincs tárolva a SIM-en.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Rögzíti a **SIM-kártya sorozatszámát** (ICCID). Hasznos annak azonosításához, melyik SIM/szolgáltató volt használatban.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Rögzíti az **IMSI-t (International Mobile Subscriber Identity)** – a SIM-kártyán lévő egyedi előfizetői azonosítót.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Kérdezőbiztosi meta mezők

### `username`

Rögzíti a **bejelentkezett kérdezőbiztos felhasználónevét** (az rtSurvey alkalmazásban használt fiókot). Ez a legmegbízhatóbb módja annak nyomon követésére, ki gyűjtötte az egyes beküldéseket.

```
type     | name     | label
username | username |
```

### `email`

Rögzíti a **bejelentkezett kérdezőbiztos e-mail-címét**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Rögzíti a **kérdezőbiztos fiókjához tartozó telefonszámot** (ha konfigurált).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Audit napló

### `audit`

Az `audit` meta mező részletes **audit naplózást** tesz lehetővé – rögzíti az összes kérdés időbélyegzett naplóját, amelyet a kérdezőbiztos meglátogatott, mennyi időt töltött mindegyiknél, és (opcionálisan) az egyes lépéseken a GPS-pozícióját. Az audit napló külön `audit.csv` fájlként kerül mentésre minden beküldés mellé.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Audit paraméterek

| Paraméter | Leírás |
|-----------|--------|
| `location-priority` | GPS pontossági szint: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Minimális másodpercek száma helymeghatározások között |
| `location-max-age` | A gyorsítótárazott helymeghatározás maximális kora (másodperc) |

Az audit napló rögzíti:
- A kérdés nevét és eseménytípusát (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Az egyes események kezdési és befejezési időbélyegét
- GPS-koordinátákat (ha a `location-priority` be van állítva)

{{% alert icon=" " context="warning" %}}
Az `audit` mező beküldésenként külön fájlt generál. Győződjön meg arról, hogy az adatfeldolgozási folyamata mind a főűrlap adatait, mind az audit CSV-t feldolgozza.
{{% /alert %}}

---

## Teljes példa

Egy tipikus háztartási felmérés tartalmaz minden időzítési és kérdezőbiztosi meta mezőt:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Háztartásazonosító |
| ... | ... | ... |

---

## Bevált módszerek

1. Mindig foglalja bele a `start` és `end` mezőket – ingyenesek, automatikusak, és felbecsülhetetlen értékűek a minőségellenőrzéshez.
2. Mindig foglalja bele a `username` mezőt a kérdezőbiztosok nyomon követéséhez.
3. Foglalja bele a `deviceid` mezőt, ha ismétlődő beküldéseket szeretne felderíteni vagy terepi eszközöket nyomon követni.
4. Használja az `audit` mezőt nagy elszámoltathatóságot igénylő felmérésekben, ahol ellenőrizni kell, hogy a kérdezőbiztosok valóban meglátogattak-e minden kérdést.
5. A SIM-rel kapcsolatos mezők (`simserial`, `subscriberid`, `devicephonenum`) csak aktív SIM-kártyával rendelkező Android-eszközökön megbízhatók – hagyja ki őket kizárólag táblagépet használó telepítéseknél.

---

## Korlátozások

- Minden meta mező **csak olvasható** – más számítások nem hivatkozhatnak rájuk és nem módosíthatják őket.
- A `username` és `email` mezőkhöz be kell jelentkeznie a kérdezőbiztosnak; névtelen beküldéseknél üresek lesznek.
- A SIM/telefon meta mezők Wi-Fi-only táblagépeken és egyes Android-verziókon üres értékeket adhatnak vissza engedélykorlátozások miatt.
