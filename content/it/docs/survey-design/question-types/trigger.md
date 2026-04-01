---
title: "Trigger / Acknowledge"
description: "Le domande trigger visualizzano una dichiarazione che l'enumeratore deve esplicitamente riconoscere prima di continuare."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Il tipo di domanda `trigger` (chiamato anche `acknowledge`) visualizza una **dichiarazione con una casella di controllo**. L'enumeratore deve spuntare la casella per confermare di aver letto e compreso la dichiarazione prima che il modulo consenta di continuare. Non viene memorizzato alcun valore dati — solo se la casella è stata spuntata.

## Specifica XLSForm di base

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Il rispondente ha fornito il consenso informato verbale. |

O usando l'alias `acknowledge`:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Il rispondente ha fornito il consenso informato verbale. |

Sia `trigger` che `acknowledge` sono equivalenti — usa quello che documenta la tua piattaforma.

## Utilizzi

Le domande trigger/acknowledge sono comunemente usate per:

1. **Consenso informato** — confermare che l'enumeratore ha ottenuto il consenso prima di registrare dati sensibili
2. **Avvisi non bloccanti** — avvisare di un valore insolito e richiedere una conferma esplicita prima di procedere
3. **Elementi di checklist** — confermare che è stata completata un'osservazione fisica (es. "Ho osservato direttamente la fonte d'acqua")
4. **Istruzioni** — forzare l'enumeratore a riconoscere un'istruzione a livello di sezione prima di continuare
5. **Controlli di qualità** — segnalare valori anomali e richiedere all'enumeratore di verificarli

## Esempio di utilizzo

### Riconoscimento del consenso

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Il rispondente ha dato il consenso informato verbale a partecipare a questo sondaggio. | yes |

### Avviso non bloccante per valori anomali

Usato insieme a un'espressione `relevant` per mostrare il trigger solo quando viene inserito un valore sospetto:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Numero di figli | | |
| trigger | children_confirm | Hai inserito ${children} figli. Verifica con il rispondente e tocca OK per confermare. | `${children} > 10` | `${children} > 10` |

### Riconoscimento delle istruzioni all'inizio della sezione

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Sezione B: Uso agricolo del suolo. Poni tutte le domande di questa sezione solo al capofamiglia. |

## Rendere il trigger obbligatorio

Aggiungi `required: yes` per impedire di avanzare finché la casella non è spuntata:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Tutto l'equipaggiamento di sicurezza è presente e funzionante. | yes | È necessario confermare prima di procedere. |

## Visualizzazione condizionale

Mostra il trigger solo quando una condizione è soddisfatta:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | La famiglia ha un pozzo? | |
| trigger | well_observation | Conferma di aver osservato direttamente le condizioni del pozzo. | `${has_well} = 'yes'` |

## Differenza da `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Visualizza testo | Sì | Sì |
| Richiede interazione | No | Sì (deve spuntare) |
| Memorizza dati | No | No (solo OK/spuntato) |
| Può bloccare l'avanzamento | No | Sì (con `required`) |

## Best practice

1. Mantieni le etichette del trigger concise e operative — l'enumeratore dovrebbe essere in grado di leggere e confermare in pochi secondi.
2. Aggiungi sempre `required: yes` quando il riconoscimento è obbligatorio.
3. Usa i trigger per i consensi e i controlli di sicurezza dove hai bisogno di un audit trail che l'enumeratore abbia confermato.
4. Combina con `relevant` per gli avvisi condizionali non bloccanti in modo che il trigger appaia solo quando un valore necessita di verifica.

## Limitazioni

- I campi trigger non memorizzano un valore dati significativo — registrano solo che la casella è stata spuntata.
- Il widget trigger viene visualizzato come una semplice casella di controllo/pulsante sulla maggior parte dei client; non è una firma elettronica completa.
