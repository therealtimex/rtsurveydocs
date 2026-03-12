---
title: "Select_one"
description: ""
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---
  
  
### select_one listname
  
Der Befehl `select_one listname` fordert den Benutzer auf, eine einzelne Option aus einer vordefinierten Liste auszuwählen. In einer XLSForm-Definition sollte der `listname` einem Wert entsprechen, der in der Spalte `list_name` des Arbeitsblatts `choices` aufgeführt ist (z. B. "yesno").

Standardmäßig werden die Auswahlmöglichkeiten als Radiobuttons angezeigt, wobei jeder Button eine einzelne statische Auswahl aus der angegebenen Liste darstellt. Es stehen jedoch verschiedene Darstellungsoptionen (`appearance`) zur Verfügung, um das Aussehen, das Verhalten und die Auswahlliste selbst anzupassen. Weitere Informationen zu diesen Optionen finden Sie in den folgenden Unterabschnitten.

In der XLSForm-Definition:
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance |
|------------------|-----------|----------------|------------|
| select_one listname | fieldname | Fragetext     |            |
{{</ table >}}
  
### Grundlegende Darstellungsoptionen (Appearance)

Geben Sie die folgenden Werte in der Spalte `appearance` an, um das Erscheinungsbild des Feldes `select_one listname` zu ändern:

- "quick": Springt automatisch zur nächsten Frage, sobald eine Option ausgewählt wurde, ohne darauf zu warten, dass der Benutzer weiterwischt (Swipe).
- "minimal": Zeigt eine einzelne Dropdown-Auswahl anstelle von Radiobuttons an.
- "compact": Zeigt eine kompakte Tabelle mit Optionen an. Die Anzahl der Spalten hängt von der Displaybreite ab.
- "compact-#": Erzwingt eine bestimmte Anzahl von Spalten in der kompakten Tabelle, wobei "#" für die gewünschte Anzahl der Spalten steht.
- "quickcompact": Kombiniert die Darstellungen "quick" und "compact".
- "quickcompact-#": Kombiniert die Darstellungen "quick" und "compact" und erzwingt eine bestimmte Anzahl von Spalten.

In der XLSForm-Definition:  
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance       |
|------------------|-----------|----------------|------------------|
| select_one listname | fieldname | Fragetext      | quick            |
| select_one listname | fieldname | Fragetext      | minimal          |
| select_one listname | fieldname | Fragetext      | compact          |
| select_one listname | fieldname | Fragetext      | compact-#        |
| select_one listname | fieldname | Fragetext      | quickcompact     |
| select_one listname | fieldname | Fragetext      | quickcompact-#   |
{{</ table >}}
