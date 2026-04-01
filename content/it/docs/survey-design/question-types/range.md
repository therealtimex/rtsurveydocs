---
title: "Range"
description: "Le domande range permettono ai rispondenti di selezionare un numero trascinando uno slider tra un valore minimo e massimo definito."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

Il tipo di domanda `range` visualizza uno **slider** (o input equivalente) che consente ai rispondenti di scegliere un numero all'interno di un minimo e massimo definiti. È ideale per raccogliere valutazioni, punteggi di soddisfazione, o qualsiasi valore numerico in cui si voglia limitare visivamente l'intervallo piuttosto che affidarsi a un input di testo con vincoli.

## Specifica XLSForm di base

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Quanto sei soddisfatto del servizio? | start=1 end=5 step=1 |

La colonna `parameters` definisce i limiti e il passo dello slider:

| Parametro | Descrizione | Predefinito |
|-----------|-------------|---------|
| `start` | Valore minimo (incluso) | 0 |
| `end` | Valore massimo (incluso) | 10 |
| `step` | Incremento tra valori validi | 1 |

Per ulteriori dettagli sul tipo di domanda range standard, vedere la [specifica XLSForm](https://xlsform.org/en/#question-types).

## Utilizzi

Le domande range sono comunemente usate per:

1. Scale di soddisfazione o valutazione (es. 1–5 o 0–10)
2. Scale numeriche in stile Likert
3. Raccolta di misurazioni dove sono validi solo valori discreti
4. Fasce di età o intervalli di punteggio dove uno slider migliora l'usabilità rispetto a un campo di testo

## Esempio di utilizzo

### Scala di valutazione di base

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Valutazione complessiva (0–10) | start=0 end=10 step=1 |

### Passo decimale

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Peso (kg) | start=0 end=200 step=0.5 |

### Utilizzo del valore in un calcolo

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Punteggio del test (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Il tuo voto è: ${grade} | | |

## Appearance

Il tipo `range` viene visualizzato come uno slider per impostazione predefinita. Non sono necessari ulteriori valori di appearance per l'uso di base. Puoi combinarlo con `horizontal` per un layout più ampio sui moduli web:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Quanto è probabile che ci raccomandi? (0–10) | start=0 end=10 step=1 | horizontal |

## Best practice

1. Imposta sempre valori significativi per `start`, `end` e `step` — non fare affidamento sui valori predefiniti.
2. Etichetta le estremità della tua scala nella colonna `hint` (es. `hint: 0 = Molto insoddisfatto, 10 = Molto soddisfatto`) per dare contesto ai rispondenti.
3. Per le scale Likert a 5 punti, usa `start=1 end=5 step=1` piuttosto che 0–4, poiché i rispondenti si aspettano che "1" significhi il livello più basso.
4. Usa `range` invece di `integer` + vincolo quando la natura delimitata dell'input fa parte del design della domanda (lo slider comunica visivamente la scala).

## Limitazioni

- Il widget slider potrebbe non essere ideale per intervalli molto ampi (es. 0–10000) — un `integer` testuale con vincoli è più facile da usare in quei casi.
- Su dispositivi mobili, i valori di passo molto piccoli (es. `step=0.1`) possono essere difficili da controllare con precisione con uno slider touch.
