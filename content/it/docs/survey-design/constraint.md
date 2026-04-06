---
title: "Validazione delle risposte"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Un modo per garantire la qualità dei dati è aggiungere vincoli ai campi dati nel tuo modulo. I vincoli aiutano a prevenire che gli utenti inseriscano risposte non valide o impossibili. Ad esempio, quando si chiede il reddito di una persona, vuoi evitare valori non realistici, come numeri negativi o valori estremamente alti. Aggiungere vincoli ai dati nel tuo modulo è facile da fare. Segui semplicemente i passaggi seguenti:

1. Aggiungi una nuova colonna chiamata "constraint" al tuo modulo.
2. Nella colonna "constraint", inserisci una formula che specifica i limiti sulla risposta.

### Esempio

Consideriamo un esempio dove vogliamo aggiungere un vincolo per il reddito della persona. Il vincolo richiede che il reddito sia compreso tra $0 e $1.000.000. Ecco come puoi impostare il vincolo:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Reddito       | . >= 0 & . <= 1000000      |
{{< /table >}}

Nell'esempio sopra, il "." nella formula si riferisce alla variabile della domanda, che rappresenta il valore inserito dall'utente per la domanda "Reddito". Il vincolo ". >= 0 && . <= 1000000" garantisce che il reddito inserito sia maggiore o uguale a 0 e minore o uguale a 1.000.000.


### Vincolo rigido

Un **vincolo rigido** blocca completamente l'invio del modulo se il valore inserito non soddisfa l'espressione. L'intervistatore non può procedere finché non inserisce un valore valido.

Per aggiungere un vincolo rigido, inserisci la tua espressione nella colonna `constraint`. Facoltativamente aggiungi un messaggio leggibile dall'uomo in `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Età del rispondente | `. > 0 and . <= 120` | L'età deve essere compresa tra 1 e 120 |
{{< /table >}}

### Vincolo morbido

Un **vincolo morbido** mostra un avviso all'intervistatore ma consente comunque l'avanzamento. Il valore viene comunque memorizzato.

Per aggiungere un vincolo morbido, usa `constraint_soft` invece di `constraint` (o usa l'appearance `soft-constraint`):

{{< table >}}
| `type` | `name` | `label` | `constraint_soft` | `constraint_message` |
|--------|--------|---------|-------------------|----------------------|
| integer | height | Altezza (cm) | `. > 100 and . < 250` | L'altezza sembra insolita. Verificare prima di continuare. |
{{< /table >}}

### Messaggi di vincolo

Aggiungi messaggi di vincolo leggibili dall'uomo nella colonna `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Età | `. > 0 and . <= 120` | L'età deve essere compresa tra 1 e 120 |
{{< /table >}}

I messaggi di vincolo supportano più lingue usando i tag lingua:

```
<en>Age must be between 1 and 120</en><it>L'età deve essere compresa tra 1 e 120</it>
```

## Best practice

1. Usa vincoli sensati che riflettano la realtà del campo — vincoli troppo restrittivi bloccano i dati validi.
2. Fornisci sempre un `constraint_message` chiaro in modo che l'intervistatore sappia come correggere il valore.
3. Testa i vincoli con valori di confine (es. il valore minimo e massimo esatti) per assicurarti che le espressioni siano corrette.
4. Considera l'uso di vincoli morbidi per i valori che sembrano anomali ma sono tecnicamente possibili.
5. Documenta la logica di business dietro i vincoli complessi nei commenti o nelle note del modulo.

## Esempi comuni di vincolo

| Caso d'uso | Espressione |
|----------|------------|
| Età positiva | `. > 0` |
| Età ragionevole | `. > 0 and . <= 120` |
| Percentuale | `. >= 0 and . <= 100` |
| Data non futura | `. <= today()` |
| Non vuoto | `. != ''` |
| Lunghezza minima del testo | `string-length(.) >= 3` |
