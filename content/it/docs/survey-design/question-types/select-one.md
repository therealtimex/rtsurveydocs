---
title: "Select_one"
description: "Le domande select_one permettono ai rispondenti di scegliere esattamente un'opzione da un elenco predefinito di scelte."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Il tipo di domanda `select_one` chiede al rispondente di scegliere **esattamente un'opzione** da un elenco predefinito. Per impostazione predefinita, le scelte vengono visualizzate come pulsanti radio, ma è disponibile un'ampia gamma di opzioni di appearance per cambiare il layout e il comportamento.

## Specifica XLSForm di base

**Foglio di lavoro survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Il rispondente ha dato il consenso? |

**Foglio di lavoro choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Sì |
| yesno | no | No |

Il `listname` in `select_one listname` deve corrispondere alla colonna `list_name` nel foglio di lavoro choices.

Per ulteriori dettagli vedere la [specifica XLSForm](https://xlsform.org/en/#question-types).

## Utilizzi

Le domande select_one vengono usate per:

1. Domande Sì/No
2. Scelta multipla a risposta singola (es. livello di istruzione, genere, stato civile)
3. Valutazioni categoriche (es. scarso / discreto / buono / eccellente)
4. Selezioni a cascata (collegate) in cui le scelte si filtrano in base a una risposta precedente
5. Selezione di paese, regione, distretto o altra unità amministrativa

## Opzioni di appearance

Specifica un valore nella colonna `appearance` per cambiare come vengono visualizzate le scelte:

{{< table >}}
| Appearance | Descrizione |
|------------|-------------|
| *(nessuna)* | Pulsanti radio predefiniti, uno per riga |
| `minimal` | Singolo menu a discesa/spinner invece dei pulsanti radio |
| `quick` | Avanza automaticamente alla domanda successiva immediatamente dopo la selezione (solo mobile) |
| `compact` | Griglia compatta di scelte — il numero di colonne si adatta alla larghezza dello schermo |
| `compact-N` | Griglia compatta forzata a N colonne (es. `compact-3`) |
| `quickcompact` | Combina `quick` e `compact` |
| `quickcompact-N` | Combina `quick` e `compact` con N colonne forzate |
| `horizontal` | Scelte disposte in una riga orizzontale (web) |
| `horizontal-compact` | Orizzontale, spaziatura compatta (web) |
| `likert` | Riga della scala Likert — etichette sopra, pulsanti radio sotto |
| `label` | Mostra solo le etichette delle scelte senza input (usa in coppia con `list-nolabel`) |
| `list-nolabel` | Mostra solo gli input senza etichette (usa in coppia con `label`) |
| `columns(N)` | Visualizza in N colonne (estensione rtSurvey, es. `columns(3)`) |
| `distress` | Widget di icone emotive Kessler Psychological Distress (K10) |
| `search-api(...)` | Ricerca dinamica — carica le scelte da un'API in fase di esecuzione |
{{< /table >}}

### Esempio: Scala Likert

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Quanto sei soddisfatto del servizio? | likert |

### Esempio: Griglia compatta a 3 colonne

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Seleziona regione | compact-3 |

## Selezioni a cascata

Una selezione a cascata (collegata) filtra le scelte in base al valore selezionato in una domanda precedente. Usa la colonna `choice_filter` con il nome di una colonna dal tuo foglio di lavoro choices.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Seleziona provincia | |
| select_one district | district | Seleziona distretto | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Quando il rispondente seleziona `nairobi`, solo `Westlands` e `Kasarani` appaiono nell'elenco dei distretti.

{{% alert icon=" " context="warning" %}}
Il nome della colonna usato in `choice_filter` (es. `province_name`) deve esistere nel foglio di lavoro choices. `${province}` fa riferimento al campo del modulo denominato `province`.
{{% /alert %}}

## Utilizzo del valore selezionato nelle espressioni

Fai riferimento al **valore** selezionato (non all'etichetta) con `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Per ottenere l'etichetta della scelta invece del valore, usa `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Opzione "Altro" con testo libero

Un pattern comune è includere un'opzione "altro" che rivela un campo di testo:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Qual è la tua occupazione? | |
| text | job_other | Specifica | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Agricoltore |
| occupation | trader | Commerciante |
| occupation | student | Studente |
| occupation | other | Altro (specifica) |

## Best practice

1. Mantieni gli elenchi brevi e mutuamente esclusivi — se i rispondenti potrebbero volere più di uno, usa `select_multiple` invece.
2. Metti la risposta più comune per prima, o ordina alfabeticamente per gli elenchi lunghi.
3. Includi sempre un'opzione "Non so" o "Preferisco non rispondere" dove rilevante.
4. Usa `minimal` (menu a discesa) per gli elenchi con più di 7–8 scelte su mobile per risparmiare spazio sullo schermo.
5. Per le selezioni a cascata, aggiungi tutte le colonne di filtro nel foglio di lavoro choices prima di creare il modulo.

## Limitazioni

- Un rispondente può selezionare solo una scelta — usa `select_multiple` per le domande a risposta multipla.
- L'appearance `likert` funziona meglio con 5–7 scelte che si adattano a una riga.
- `quick` auto-avanzamento è solo mobile; non ha effetto sui moduli web.
