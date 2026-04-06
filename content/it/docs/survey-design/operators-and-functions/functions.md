---
title: "Funzioni"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Funzioni stringa

{{% alert icon=" " context="warning" %}}
Quando si lavora con le stringhe nelle espressioni, è importante usare virgolette singole ('') per racchiudere le stringhe letterali. Tuttavia, si presenta un'eccezione quando si vuole includere virgolette singole all'interno di una stringa letterale. In tal caso, puoi usare le virgolette doppie ("") per racchiudere l'intera stringa.

Per esempio:
- Corretto: if(${yesno} = 1, "una stringa con 'virgolette singole' al suo interno", "nessuna virgoletta singola qui")
- Errato: if(${yesno} = 1, 'una stringa con 'virgolette singole' al suo interno', 'nessuna virgoletta singola qui')

Per quanto riguarda le smart quotes, è fondamentale essere consapevoli della loro presenza, poiché possono causare problemi nelle espressioni. Molti editor di testo formattato convertono automaticamente le virgolette diritte ("" o '') in smart quotes o virgolette curve ("" o ''), che possono causare errori di sintassi o comportamenti imprevisti. Per evitare ciò, assicurati di usare sempre virgolette diritte ('') nelle tue espressioni.
{{% /alert %}}

rtSurvey supporta varie funzioni, tra cui:

1. `string(field)`: Converte un campo in una stringa.
   - Esempio: `string(34.8)` verrà convertito in `'34.8'`.

2. `string-length(field)`: Restituisce la lunghezza di un campo stringa.
   - Esempio: `string-length(.) > 3 and string-length(.) < 10` può essere usato per assicurarsi che il campo corrente abbia tra 3 e 10 caratteri.

3. `substr(fieldorstring, startindex, endindex)`: Restituisce una sottostringa che inizia a `startindex` e termina appena prima di `endindex`. Gli indici partono da 0 per il primo carattere nella stringa.
   - Esempio: `substr(${phone}, 0, 3)` restituirà le prime tre cifre di un numero di telefono.

4. `concat(a, b, c, ...)`: Concatena campi (e/o stringhe) insieme.
   - Esempio: `concat(${firstname}, ' ', ${lastname})` restituirà il nome completo combinando i valori nei campi `firstname` e `lastname`.

5. `linebreak()`: Restituisce un carattere di interruzione di riga.
   - Esempio: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` restituirà un elenco di tre valori di campo con interruzioni di riga tra di essi.

6. `lower()`: Converte una stringa in tutti caratteri minuscoli.
   - Esempio: `lower('Nome della Via')` restituirà "nome della via".

7. `upper()`: Converte una stringa in tutti caratteri maiuscoli.
   - Esempio: `upper('Nome della Via')` restituirà "NOME DELLA VIA".

### Funzioni select_one e select_multiple

1. `count-selected(field)`: Restituisce il numero di elementi selezionati in un campo select_multiple.
   - Esempio: `count-selected(.) = 3` può essere usato come espressione di vincolo per assicurarsi che vengano selezionate esattamente tre scelte.

2. `selected(field, value)`: Restituisce true o false a seconda che il valore specificato sia stato selezionato nel campo select_one o select_multiple.
   - Esempio: `selected(${color}, 'Blue')` può essere usato come espressione di rilevanza per mostrare un gruppo o un campo solo se il rispondente ha selezionato "Blue" come colore preferito.
   - Nota: Il secondo parametro deve sempre specificare il valore della scelta, non l'etichetta della scelta. Usa il valore dalla colonna value nel foglio choices della definizione del modulo.

3. `selected-at(field, number)`: Restituisce l'elemento selezionato alla posizione specificata in un campo select_multiple. Quando il numero passato è 0, restituisce il primo elemento selezionato; quando il numero è 1, restituisce il secondo elemento selezionato, e così via.
   - Esempio: `selected-at(${fruits}, 0) = 'Apple'` può essere usato come espressione di rilevanza per mostrare un gruppo o un campo solo se la prima scelta selezionata è "Apple".
   - Nota: Il valore restituito sarà il valore della scelta, non l'etichetta della scelta.

4. `choice-label(field, value)`: Restituisce l'etichetta per una scelta di un campo select_one o select_multiple, come definita nel foglio choices della definizione del modulo.
   - Esempio 1: `choice-label(${country}, ${country})` restituirà l'etichetta della scelta per la scelta attualmente selezionata nel campo denominato `country`.
   - Esempio 2: `choice-label(${languages}, selected-at(${languages}, 0))` restituirà l'etichetta per la prima scelta selezionata nel campo denominato `languages`.
   - Nota: Questa funzione recupera l'etichetta della scelta, non il valore.

### Funzioni per i campi ripetuti

In rtSurvey, se vuoi fare la stessa domanda più volte, puoi inserire un campo all'interno di un gruppo repeat. Questo genera più istanze dello stesso campo. Le seguenti funzioni possono aiutarti a gestire questi campi ripetuti e i dati ripetuti che producono.

1. `join(string, repeatedfield)`: Per un campo all'interno di un gruppo repeat, genera una lista di valori separata da stringhe. Il primo parametro specifica il delimitatore da usare per separare i valori.
   - Esempio: `join(', ', ${member_name})` genererà un singolo elenco separato da virgole da tutti i nomi inseriti.

2. `join-if(string, repeatedfield, expression)`: Funziona esattamente come `join()`, tranne che controlla ogni istanza nel gruppo repeat usando l'espressione fornita. Se l'espressione restituisce false, l'elemento verrà omesso dall'output.
   - Esempio: `join-if(', ', ${member_name}, ${age} >= 18)` genererà un elenco separato da virgole dei nomi dei soli membri adulti (quelli con età 18 e più).

3. `count(repeatgroup)`: Restituisce il numero corrente di volte che un gruppo repeat si è ripetuto.
   - Esempio: `count(${groupname})` restituirà il numero di istanze del gruppo.

4. `count-if(repeatgroup, expression)`: Funziona esattamente come `count()`, tranne che controlla ogni istanza nel gruppo repeat usando l'espressione fornita. Se l'espressione restituisce false, l'elemento verrà omesso dall'output.
   - Esempio: `count-if(${members}, ${age} >= 18)` restituirà il conteggio dei membri adulti basato sul campo age all'interno del gruppo repeat "members".

5. `sum(repeatedfield)`: Per un campo all'interno di un gruppo repeat, calcola la somma di tutti i valori.
   - Esempio: `sum(${loan_amount})` restituirà il valore totale di tutti i prestiti.

6. `sum-if(repeatedfield, expression)`: Funziona esattamente come `sum()`, tranne che controlla ogni istanza nel gruppo repeat usando l'espressione fornita. Se l'espressione restituisce false, l'elemento verrà omesso dall'output.
   - Esempio: `sum-if(${loan_amount}, ${loan_amount} > 500)` restituirà il valore totale di tutti i prestiti superiori a 500. I prestiti più piccoli verranno ignorati.

7. `min(repeatedfield)`: Per un campo all'interno di un gruppo repeat, calcola il minimo di tutti i valori.
   - Esempio: `min(${member_age})` restituirà l'età del membro più giovane del gruppo.

8. `min-if(repeatedfield, expression)`: Funziona esattamente come `min()`, tranne che controlla ogni istanza nel gruppo repeat usando l'espressione fornita.
   - Esempio: `min-if(${member_age}, ${member_age} >= 18)` restituirà l'età dell'adulto più giovane del gruppo. Quelli con meno di 18 anni verranno ignorati.

9. `max(repeatedfield)`: Per un campo all'interno di un gruppo repeat, calcola il massimo di tutti i valori.
   - Esempio: `max(${member_age})` restituirà l'età del membro più anziano del gruppo.

10. `max-if(repeatedfield, expression)`: Funziona esattamente come `max()`, tranne che controlla ogni istanza nel gruppo repeat usando l'espressione fornita.
    - Esempio: `max-if(${member_age}, ${member_age} >= 18)` restituirà l'età dell'adulto più anziano del gruppo. Quelli con meno di 18 anni verranno ignorati.

11. `index()`: Chiamata all'interno di un gruppo repeat, restituisce il numero di indice per il gruppo o l'istanza corrente.
    - Esempio: `index()` usato all'interno di un gruppo repeat restituirà 1 per la prima istanza, 2 per la seconda, e così via.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Fa riferimento a un campo o gruppo che si trova all'interno di un gruppo repeat dall'esterno di quel repeat. Il primo parametro specifica il campo o gruppo ripetuto di interesse, il secondo specifica il gruppo repeat all'interno del quale si trova il campo o gruppo, e il terzo specifica il numero di istanza all'interno del gruppo repeat da usare.
    - Esempio 1: `indexed-repeat(${name}, ${names}, 1)` restituirà il primo nome disponibile quando il campo name si trova all'interno di un gruppo repeat precedente denominato "names".
    - Esempio 2: `indexed-repeat(${name}, ${names}, index())` recupererà il nome corrispondente al numero di istanza del gruppo repeat corrente.

13. `rank-index(index, repeatedfield)`: Questa funzione calcola il rango ordinale dell'istanza specificata di un campo ripetuto per l'uso al di fuori del gruppo repeat. Il rango 1 è assegnato all'istanza con il valore più alto, il rango 2 all'istanza con il valore successivo più alto, e così via. Se si passa un indice non valido o un indice a un'istanza con un valore non numerico, verrà restituito un rango di 999.
    - Esempio: `rank-index(1, ${random_draw})` calcola il rango della prima istanza in base al valore del suo campo `random_draw` rispetto ai valori delle altre istanze.

14. `rank-index-if(index, repeatedfield, expression)`: Questa funzione funziona in modo simile a `rank-index()`, ma controlla ogni istanza nel gruppo repeat del campo ripetuto usando l'espressione fornita. Se l'espressione restituisce false, l'elemento verrà omesso dal calcolo.
    - Esempio: `rank-index-if(1, ${age}, ${age} >= 18)` calcola il rango per età all'interno del gruppo degli adulti, considerando solo le istanze in cui l'età è maggiore o uguale a 18.

### Funzioni numeriche

{{< table >}}
| Operatore | Operazione | Esempio | Risposta di esempio |
|----------|-----------|---------|----------------|
| `+` | Addizione | 1 + 1 | 2 |
| `-` | Sottrazione | 3 - 2 | 1 |
| `*` | Moltiplicazione | 3 * 2 | 6 |
| `div` | Divisione | 10 div 2 | 5 |
| `mod` | Modulo | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey supporta funzioni numeriche, tra cui:
- `number(field)`: Converte il valore del campo in un numero.
  - Esempio: `number('34.8')` = 34.8

- `int(field)`: Converte il valore del campo in un intero.
  - Esempio: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Restituisce il valore minimo tra i campi passati.
  - Esempio: `min(${father_age}, ${mother_age})` restituirà l'età del padre o della madre, a seconda di quale sia minore.

- `max(field1, ..., fieldx)`: Restituisce il valore massimo tra i campi passati.
  - Esempio: `max(${father_age}, ${mother_age})` restituirà l'età del padre o della madre, a seconda di quale sia maggiore.

- `format-number(field)`: Formatta il valore di un campo intero o decimale secondo le impostazioni locali dell'utente.
  - Esempio: `format-number(${income})` potrebbe formattare "120000" come "120.000".

- `round(field, digits)`: Arrotonda il valore numerico del campo al numero specificato di cifre dopo il punto decimale.
  - Esempio: `round(${interest_rate}, 2)`

- `abs(number)`: Restituisce il valore assoluto di un numero.
  
- `pow(base, exponent)`: Restituisce il valore del primo parametro elevato alla potenza del secondo parametro.
  - Ogni parametro può essere un campo, un numero o un'espressione.

- `log10(fieldorvalue)`: Restituisce il logaritmo in base dieci del campo o valore passato.

- `sin(fieldorvalue)`: Restituisce il seno del campo o valore passato, espresso in radianti.
  
- `cos(fieldorvalue)`: Restituisce il coseno del campo o valore passato, espresso in radianti.

- `tan(fieldorvalue)`: Restituisce la tangente del campo o valore passato, espresso in radianti.

- `asin(fieldorvalue)`: Restituisce l'arcoseno del campo o valore passato, espresso in radianti.

- `acos(fieldorvalue)`: Restituisce l'arcocoseno del campo o valore passato, espresso in radianti.

- `atan(fieldorvalue)`: Restituisce l'arcotangente del campo o valore passato, espresso in radianti.

- `atan2(x, y)`: Restituisce l'angolo in radianti sotteso all'origine dal punto con coordinate (x, y) e l'asse x positivo. Il risultato è nell'intervallo -pi() a pi().

- `sqrt(fieldorvalue)`: Restituisce la radice quadrata non negativa del campo o valore passato.

- `exp(x)`: Restituisce il valore di e^x.

- `pi()`: Restituisce il valore di pi greco.

### Funzioni di data e ora

{{% alert icon=" " context="warning" %}}
I valori data in rtSurvey sono memorizzati come stringhe nel formato `YYYY-MM-DD`. I valori datetime sono memorizzati come stringhe ISO 8601 (`YYYY-MM-DDTHH:MM:SS`). Usa `decimal-date-time()` per convertire in un numero per l'aritmetica (ad esempio, calcolare durate).
{{% /alert %}}

1. `today()`: Restituisce la data odierna come stringa nel formato `YYYY-MM-DD`. Valutata una volta quando il modulo si apre.
   - Esempio: `today()` → `'2024-03-15'`
   - Uso comune: colonna `default` per pre-compilare la data odierna, o in `relevant`/`constraint` per confrontare con un campo data.

2. `now()`: Restituisce la data e l'ora correnti come stringa ISO 8601. Valutata ogni volta che l'espressione viene calcolata.
   - Esempio: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Uso comune: Registrare il timestamp esatto di un evento specifico durante il sondaggio.

3. `date(value)`: Converte un valore (stringa o numero) in una stringa data. Utile per convertire valori calcolati in un tipo data.
   - Esempio: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Converte un valore in una stringa datetime.
   - Esempio: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Converte una stringa data o datetime in un numero decimale che rappresenta i millisecondi dall'epoca Unix divisi per 86400000 (cioè, giorni frazionari dal 1970-01-01). Usalo per eseguire operazioni aritmetiche sulle date.
   - Esempio: Durata in giorni tra due date:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Esempio: Durata in minuti tra due datetime:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Formatta un valore data usando una stringa di pattern.
   - Token di formato: `%Y` (anno a 4 cifre), `%y` (anno a 2 cifre), `%m` (mese 01–12), `%d` (giorno 01–31), `%a` (giorno della settimana abbreviato), `%b` (nome del mese abbreviato)
   - Esempio: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`

7. `format-date-time(datetime, format)`: Formatta un valore datetime usando una stringa di pattern. Accetta tutti i token di `format-date` più:
   - `%H` (ora 00–23), `%h` (ora 01–12), `%M` (minuti 00–59), `%S` (secondi 00–59), `%3` (millisecondi), `%P` (AM/PM)
   - Esempio: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`

---

### Funzioni booleane

1. `boolean(value)`: Converte qualsiasi valore in un booleano. Restituisce `true` per stringhe non vuote, numeri diversi da zero e `true`; restituisce `false` per stringhe vuote, `0` e `false`.
   - Esempio: `boolean(${name})` restituisce `true` se `name` non è vuoto.

2. `boolean-from-string(string)`: Restituisce `true` se la stringa è `'1'` o `'true'` (non sensibile alle maiuscole); restituisce `false` altrimenti.
   - Esempio: `boolean-from-string(${enabled_flag})` — utile quando un campo memorizza `'true'`/`'false'` come testo.

3. `true()`: Restituisce il valore booleano `true`.
   - Esempio: Nella colonna `required`, `true()` è equivalente a `yes`.

4. `false()`: Restituisce il valore booleano `false`.
   - Esempio: `if(${skip_section} = 'yes', false(), true())` — imposta dinamicamente il campo come obbligatorio.

5. `not(expression)`: Restituisce la negazione logica dell'espressione. Restituisce `true` se l'espressione è falsa, e viceversa.
   - Esempio: `not(${consent} = 'yes')` — mostra un avviso quando il consenso NON è stato dato.
   - Esempio: `not(selected(${issues}, 'none'))` — richiede dettagli solo se "nessuno" non è stato selezionato.

---

### Funzioni stringa aggiuntive

1. `starts-with(string, prefix)`: Restituisce `true` se `string` inizia con `prefix`.
   - Esempio: `starts-with(${phone}, '+254')` controlla se il numero di telefono inizia con il prefisso del Kenya.

2. `contains(string, substring)`: Restituisce `true` se `string` contiene `substring`.
   - Esempio: `contains(${email}, '@')` controlla che un indirizzo email abbia un segno `@`.
   - Esempio: `contains(${notes}, 'urgente')` attiva una domanda di follow-up se le note menzionano "urgente".

3. `substring-before(string, needle)`: Restituisce la parte di `string` che appare prima della prima occorrenza di `needle`.
   - Esempio: `substring-before(${full_name}, ' ')` estrae la prima parola (nome).

4. `substring-after(string, needle)`: Restituisce la parte di `string` che appare dopo la prima occorrenza di `needle`.
   - Esempio: `substring-after(${email}, '@')` estrae la parte del dominio di un indirizzo email.

5. `normalize-space(string)`: Rimuove gli spazi iniziali e finali e riduce tutte le sequenze di spazi interni a un singolo spazio.
   - Esempio: `normalize-space(${name})` — pulisce un nome che potrebbe essere stato digitato con spazi extra.

6. `translate(string, search_chars, replace_chars)`: Sostituisce ogni carattere in `string` che appare in `search_chars` con il carattere corrispondente in `replace_chars`. I caratteri in `search_chars` senza carattere corrispondente in `replace_chars` vengono eliminati.
   - Esempio: `translate(${phone}, ' -()', '')` rimuove spazi, trattini e parentesi da un numero di telefono.

---

### Funzioni matematiche aggiuntive

1. `floor(number)`: Restituisce il più grande intero minore o uguale a `number` (arrotonda verso meno infinito).
   - Esempio: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Restituisce il più piccolo intero maggiore o uguale a `number` (arrotonda verso più infinito).
   - Esempio: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Restituisce un numero decimale casuale tra 0.0 (incluso) e 1.0 (escluso). Tipicamente usato nei campi `calculate` per assegnare valori casuali o randomizzare l'ordine delle domande.
   - Esempio: `random()` → es. `0.7341`
   - Esempio: `int(random() * 6) + 1` → numero casuale 1–6 (lancio del dado)

4. `coalesce(a, b)`: Restituisce `a` se `a` non è vuoto; altrimenti restituisce `b`. Utile come fallback quando un campo potrebbe essere vuoto.
   - Esempio: `coalesce(${preferred_name}, ${full_name})` — usa il nome preferito se impostato, altrimenti ricorre al nome completo.

5. `once(value)`: Valuta `value` e lo memorizza, ma solo se il campo corrente è **vuoto**. Se il campo ha già un valore (ad esempio, è stato impostato in precedenza), `once()` restituisce il valore esistente invariato. Questo impedisce al ricalcolo di sovrascrivere l'input dell'utente.
   - Esempio: `once(today())` nella colonna `default` imposta la data odierna una volta e non si aggiorna se l'enumeratore riapre il modulo.
   - Esempio: `once(uuid())` genera un UUID una volta e lo mantiene stabile tra le modifiche successive.

---

### Funzioni geografiche

1. `area(geoshape_value)`: Calcola l'**area in metri quadrati** racchiusa da un valore geoshape (poligono).
   - Il parametro è un valore di campo geoshape nel formato `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Esempio: `area(${field_boundary})` — calcola l'area di un campo rilevato in m².
   - Esempio: `round(area(${field_boundary}) div 10000, 2)` — converti in ettari.

2. `distance(coordinates)`: Calcola la **lunghezza totale del percorso in metri** di un geotrace (linea), o la distanza tra due geopoint.
   - Per un geotrace: `distance(${route})` restituisce la lunghezza totale del percorso in metri.
   - Per due geopoint: `distance(concat(${point_a}, ' ', ${point_b}))` restituisce la distanza tra loro.
   - Esempio: `round(distance(${road_trace}) div 1000, 3)` — lunghezza della strada in chilometri.

---

### Funzioni di validazione

1. `regex(value, pattern)`: Restituisce `true` se `value` corrisponde all'espressione regolare `pattern`. Usalo nella colonna `constraint` per la validazione basata su pattern.
   - Il pattern usa la sintassi regex standard (sottoinsieme POSIX ERE).
   - Esempio: `regex(., '^[0-9]{10}$')` — valida un numero a 10 cifre.
   - Esempio: `regex(., '^[A-Z]{2}[0-9]{6}$')` — valida il formato di un numero di passaporto (2 lettere maiuscole seguite da 6 cifre).
   - Esempio: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — verifica di base del formato email.

2. `checklist(min, max, v1, v2, ...)`: Valuta un elenco di espressioni booleane e restituisce `true` se il numero di valori `true` è compreso tra `min` e `max` (inclusi). Passa `-1` per `min` o `max` per saltare quel limite.
   - Esempio: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — passa se esattamente 2 o 3 delle tre condizioni sono vere.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Come `checklist()`, ma ogni valore ha un peso. La somma dei pesi per i valori `true` deve essere compresa tra `min` e `max`.
   - Esempio: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — la somma dei pesi delle strutture presenti deve essere almeno 10.

---

### Funzioni di utilità

1. `uuid()`: Genera un UUID casuale (formato RFC 4122 v4) come stringa.
   - Esempio: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Tipicamente usato con `once()` per generare un ID univoco stabile: `once(uuid())`

2. `version()`: Restituisce il valore dell'attributo `version` del modulo come impostato nel foglio settings.
   - Esempio: `version()` → `'3.1'`
   - Utile nei campi `calculate` per incorporare la versione del modulo nei dati esportati.

3. `position()`: Chiamata all'interno di un **gruppo repeat**, restituisce l'indice a base 1 dell'istanza corrente del repeat.
   - Esempio: `position()` nella prima istanza restituisce `1`, nella seconda restituisce `2`, e così via.
   - Vedi anche: `index()` (alias), `indexed-repeat()` per fare riferimento ai valori del repeat dall'esterno del gruppo.

4. `thousandsep(length, separator, value)`: Formatta un numero con un separatore delle migliaia. `length` è la lunghezza minima totale della stringa (riempita con spazi se più corta), `separator` è il carattere da usare (ad esempio, `','`), e `value` è il numero da formattare.
   - Esempio: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Esempio: `thousandsep(0, '.', ${income})` → formatta il reddito con il punto come separatore delle migliaia.

5. `substr-jsonpath(value, jsonpath)`: Estrae una sottostringa da una stringa JSON usando un'espressione JSONPath.
   - Esempio: `substr-jsonpath(${api_response}, '$.data.name')` — estrae il campo `name` da una stringa JSON memorizzata in `api_response`.
   - Tipicamente usato insieme a `callapi()` per estrarre valori specifici dalle risposte API.
