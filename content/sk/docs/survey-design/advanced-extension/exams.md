---
title: "Skúšky"
description: "Funkcia skúšky pridáva do prieskumu režim časovaného kvízu s voliteľnou zvukovou spätnou väzbou pre správne a nesprávne odpovede."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

Funkcia **Skúška** premení prieskum na časovaný kvíz. Respondentovi sa zobrazí odpočítavač a prieskum zaznamená, koľko času zostalo keď skončili. Voliteľne môžu zvukové signály hrať pre správne a nesprávne odpovede.

Je to užitočné pre hodnotenia vedomostí, testy gramotnosti, kontroly kompetencie terénneho personálu a akýkoľvek prieskum, kde je čas strávený pri úlohe zmysluplným dátom.

---

## Funkcia `check-exam()`

Nakonfigurujte skúšku pomocou `check-exam()` v stĺpci **`calculation`** poľa `calculate` umiestneného na začiatku formulára:

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Parametre

| # | Parameter | Popis |
|---|-----------|-------------|
| 1 | `examTime` | Celkové trvanie skúšky v sekundách |
| 2 | `questionToStoreRemainingTime` | `name` poľa `calculate` alebo `integer`, ktoré uloží zostatok času po skončení skúšky |
| 3 | `rightSound` | *(Voliteľné)* Názov súboru zvuku na prehranie pri správnej odpovedi (priložiť k formuláru ako mediálny súbor) |
| 4 | `wrongSound` | *(Voliteľné)* Názov súboru zvuku na prehranie pri nesprávnej odpovedi |
| 5 | `excludeQuestion` | *(Voliteľné)* Zoznam názvov polí oddelený čiarkami na vylúčenie z časovača skúšky (napr. `'intro_note,consent'`) |

---

## Základné nastavenie

### Krok 1: Pridanie polí skúšky

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` spustí 600-sekundový (10-minútový) časovač. `remaining_time` sa automaticky vyplní keď respondent skončí.

### Krok 2: Pridanie otázok

Časovač skúšky pokrýva všetky otázky vo formulári okrem tých uvedených v `excludeQuestion`.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | Hlavné mesto Slovenska je Bratislava. Pravda alebo lož? |
| select_one choices | q2 | Ktorý orgán pumpuje krv po tele? |
| select_one choices | q3 | Voda sa varí pri 100°C na hladine mora. Pravda alebo lož? |

### Krok 3: Uloženie zostatkového času

Pole pomenované v parametri 2 (`remaining_time`) sa automaticky nastaví na počet sekúnd zostávajúcich keď respondent odošle. Hodnota `0` znamená, že čas vypršal; vysoká hodnota znamená, že skončili rýchlo.

---

## So zvukovou spätnou väzbou

Priložte zvukové súbory k formuláru (ako mediálne prílohy), potom ich odkazujte:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` hrá keď respondent vyberie správnu odpoveď
- `wrong.mp3` hrá keď respondent vyberie nesprávnu odpoveď

{{% alert icon=" " context="warning" %}}
Zvukové súbory musia byť priložené k formuláru ako mediálne súbory a názov súboru sa musí presne zhodovať (rozlišuje veľkosť písmen) vrátane prípony.
{{% /alert %}}

---

## Vylučovanie otázok z časovača

Odovzdajte zoznam názvov polí oddelený čiarkami na vylúčenie z skúšky (napr. úvodné poznámky alebo otázky súhlasu):

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Nechajte `rightSound` a `wrongSound` ako prázdne reťazce `''` ak nepotrebujete zvuk, ale potrebujete vylúčenia.

---

## Úplný príklad

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Vitajte na hodnotení zdravotných znalostí. Na zodpovedanie všetkých otázok máte 5 minút. | |
| trigger | start_ack | Keď ste pripravení začať, ťuknite OK. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | Umývanie rúk zabraňuje šíreniu chorôb. | |
| select_one yesno | q2 | Mali by ste piť aspoň 2 litre vody denne. | |
| select_one yesno | q3 | Malária je spôsobená vírusom. | |

---

## Najlepšie postupy

1. Vždy informujte respondentov o časovom limite pred začatím — použite `note` alebo `trigger` pred poľom `check-exam()`.
2. Vylúčte úvodné poznámky a otázky súhlasu z časovača pomocou parametra `excludeQuestion`.
3. Použite `remaining_time` v následnom výpočte na detekciu vypršania času: `if(${remaining_time} = 0, 'Čas vypršal', 'Dokončené')`.
4. Udržujte počet otázok primeraný k povolenému času — 2–3 minúty na otázku je rozumný základ pre väčšinu hodnotení vedomostí.
5. Pred nasadením testujte so zvukovými súbormi na skutočnom zariadení — prehrávanie zvuku sa líši naprieč verziami Androidu a prehliadačmi.

## Obmedzenia

- Časovač je iba na zobrazenie — formulár sa automaticky neodošle keď čas vypršal; respondent musí stále odoslať manuálne.
- Zvuková spätná väzba vyžaduje, aby hlasitosť zariadenia bola zapnutá a nebola stlmená.
- Funkcia skúšky je rozšírením rtSurvey a nie je súčasťou štandardnej špecifikácie XLSForm.
