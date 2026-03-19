---
title: "Erweiterte Wiederholungen"
description: "Fortgeschrittene Muster für Wiederholungsgruppen: dynamische Zählung, verschachtelte Wiederholungen, Zusammenfassung von Wiederholungsdaten und Referenzierung von Werten über Wiederholungen hinweg."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Diese Seite behandelt fortgeschrittene Muster für die Arbeit mit Wiederholungsgruppen in rtSurvey. Für die Grundlagen zur Einrichtung einer Wiederholungsgruppe, siehe [Gruppierung und Wiederholungen](../repeats).

---

## Dynamische Wiederholungsanzahl

Standardmäßig entscheidet der Interviewer, wie oft er wiederholt. Sie können die Anzahl der Wiederholungen mit `repeat_count` festlegen:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Haushaltsmitglied | `${num_members}` |
| text | member_name | Name des Mitglieds | |
| integer | member_age | Alter | |
| end_repeat | | | |

Die Wiederholung läuft genau `${num_members}` Mal, wobei `num_members` zuvor im Formular erfasst wurde. Der Interviewer kann keine Instanzen hinzufügen oder entfernen.

---

## Indiziierter Zugriff: `indexed-repeat()`

Greifen Sie auf den Feldwert einer bestimmten Wiederholungsinstanz von **außerhalb** der Wiederholungsgruppe zu mit `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Dies ist nützlich für das Erstellen von Zusammenfassungsfeldern oder für die Referenzierung der Daten des "primären" Mitglieds nach der Wiederholung.

---

## Aktuelle Instanzposition: `index()`

Innerhalb einer Wiederholungsgruppe gibt `index()` die 1-basierte Position der aktuellen Instanz zurück. Verwenden Sie es, um jede Wiederholung zu beschriften oder eindeutige Bezeichner zu erstellen:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Parzelle |
| note | plot_label | Parzellennummer ${index()} |
| text | plot_id | Parzellen-ID |
| end_repeat | | |

---

## Felder in derselben Instanz referenzieren

Innerhalb einer Wiederholung verwenden Sie `${fieldname}`, um ein anderes Feld **in derselben Wiederholungsinstanz** zu referenzieren. `indexed-repeat()` ist innerhalb derselben Schleife nicht erforderlich:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Mitglied | |
| text | member_name | Name | |
| integer | member_age | Alter | |
| text | school_name | Schulname | `${member_age} < 18` |
| end_repeat | | | |

---

## Übergeordnete Felder von innerhalb einer Wiederholung referenzieren

Felder außerhalb (oberhalb) der Wiederholungsgruppe können normal mit `${fieldname}` referenziert werden:

| type | name | label |
|------|------|-------|
| text | village | Dorfname |
| begin_repeat | plots | Landwirtschaftliche Parzelle |
| note | plot_context | Parzellen in ${village} |
| end_repeat | | |

---

## Wiederholungsdaten zusammenfassen

Verwenden Sie Wiederholungs-Aggregatfunktionen **außerhalb** der Wiederholungsgruppe zur Zusammenfassung:

| Funktion | Beispiel | Beschreibung |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | Anzahl der Instanzen |
| `sum(field)` | `sum(${loan_amount})` | Summe eines numerischen Feldes |
| `min(field)` | `min(${member_age})` | Minimalwert |
| `max(field)` | `max(${member_age})` | Maximalwert |
| `join(sep, field)` | `join(', ', ${member_name})` | Kommagetrennte Liste |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Bedingte Zählung |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Bedingte Summe |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Bedingtes Verbinden |

### Beispiel: Haushaltszusammenfassung

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Wie viele Mitglieder? | |
| begin_repeat | members | Mitglied | `${num_members}` |
| text | member_name | Name | |
| integer | member_age | Alter | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} Mitglieder; ${children_count} unter 18. Erwachsene: ${adult_names} | |

---

## Verschachtelte Wiederholungen

Eine Wiederholungsgruppe kann eine weitere Wiederholungsgruppe enthalten. Verwenden Sie dies sorgfältig — verschachtelte Wiederholungen erhöhen die Komplexität und können für Interviewer verwirrend sein.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Haushalt |
| text | hh_id | Haushalts-ID |
| begin_repeat | hh_members | Mitglied |
| text | member_name | Mitgliedsname |
| end_repeat | | |
| end_repeat | | |

Um ein Feld in einer äußeren Wiederholung von der inneren Wiederholung aus zu referenzieren, verwenden Sie `${fieldname}` — es löst sich zum nächsten passenden Vorfahren auf:

Innerhalb der `hh_members`-Wiederholung gibt `${hh_id}` die ID des **aktuellen** Haushalts zurück, nicht aller Haushalte.

---

## Rank innerhalb von Wiederholungsgruppen: `rank-index()`

Wenn ein `rank`-Feld innerhalb einer Wiederholung vorhanden ist, verwenden Sie `rank-index(instanceNumber, repeatedField)` von außen, um den ordinalen Rang einer bestimmten Instanz zu erhalten:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` gibt den Instanzindex der höchsten Punktzahl zurück.

---

## Empfohlene Vorgehensweisen

1. Verwenden Sie immer `repeat_count`, wenn die Anzahl der Wiederholungen im Voraus bekannt ist — dies verhindert, dass Interviewer versehentlich Instanzen hinzufügen oder entfernen.
2. Halten Sie Wiederholungsgruppen fokussiert — eine Wiederholung mit 20+ Fragen pro Instanz ist schwer zu navigieren.
3. Benennen Sie Wiederholungsgruppen klar (z. B. `household_members`, nicht `repeat1`) — der Name erscheint in Funktionsaufrufen und exportierten Daten.
4. Testen Sie mit der maximal erwarteten Anzahl von Instanzen, um die Leistung zu überprüfen.
5. Verwenden Sie das `field-list`-Erscheinungsbild für die Wiederholungsgruppe, um alle Felder auf einem Bildschirm pro Instanz anzuzeigen (mobil).

---

## Einschränkungen

- `indexed-repeat()` erfordert einen gültigen Index (1 bis Instanzanzahl) — Indizes außerhalb des Bereichs geben leer zurück.
- Verschachtelte Wiederholungen über 2 Ebenen hinaus werden nicht empfohlen und können bei einigen Clients Anzeigeprobleme verursachen.
- Aggregatfunktionen (`sum`, `count` usw.) arbeiten auf der gesamten Wiederholungsgruppe — Sie können keine Teilmenge von Instanzen ohne die `*-if`-Varianten aggregieren.
