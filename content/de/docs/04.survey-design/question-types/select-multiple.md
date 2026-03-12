---
title: "Select_multiple"
description: ""
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

### select_multiple listname

Der Befehl `select_multiple listname` fordert den Benutzer auf, eine oder mehrere Auswahlmöglichkeiten aus einer vordefinierten Liste auszuwählen. In einer XLSForm-Definition sollte der `listname` einem Wert entsprechen, der in der Spalte `list_name` des Arbeitsblatts `choices` aufgeführt ist (z. B. "country").

Standardmäßig werden die Auswahlmöglichkeiten als Kontrollkästchen (Checkboxes) angezeigt, wobei jedes Kontrollkästchen eine einzelne statische Auswahl aus der angegebenen Liste darstellt. Es stehen jedoch verschiedene Darstellungsoptionen (`appearance`) zur Verfügung, um das Aussehen, die Funktionalität und sogar die Auswahlliste selbst anzupassen. Weitere Informationen zu diesen Optionen finden Sie in den folgenden Unterabschnitten.

Beim Exportieren der Daten enthält jede Zeile eine Spalte mit einer durch Leerzeichen getrennten Liste aller gewählten Antwortwerte für jedes `select_multiple`-Feld.

Wenn ein `select_multiple`-Feld in der Feldvalidierung oder in Sprungmustern verwendet wird (Constraint- oder Relevanz-Ausdrücke), muss die Funktion `selected()` verwendet werden, um zu prüfen, ob eine bestimmte Auswahl getroffen wurde. Weitere Informationen zu Constraint- und Relevanz-Ausdrücken finden Sie in den Hilfethemen.

In der XLSForm-Definition:

| Type                  | Name      | Label          | Appearance |
|-----------------------|-----------|----------------|------------|
| select_multiple listname | fieldname | Fragetext     |            |
