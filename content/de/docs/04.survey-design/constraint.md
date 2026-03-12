---
title: "Antworten validieren"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Eine Möglichkeit, die Datenqualität sicherzustellen, besteht darin, Einschränkungen (Constraints) für die Datenfelder in Ihrem Formular hinzuzufügen. Constraints helfen zu verhindern, dass Benutzer ungültige oder unmögliche Antworten eingeben. Wenn Sie beispielsweise nach dem Einkommen einer Person fragen, möchten Sie unrealistische Werte wie negative Zahlen oder extrem hohe Werte vermeiden. Das Hinzufügen von Dateneinschränkungen in Ihrem Formular ist einfach. Folgen Sie einfach den unten stehenden Schritten:

1. Fügen Sie eine neue Spalte namens "constraint" zu Ihrem Formular hinzu.
2. Geben Sie in der Spalte "constraint" eine Formel ein, die die Grenzen für die Antwort festlegt.

### Beispiel

Betrachten wir ein Beispiel, bei dem wir eine Einschränkung für das Einkommen einer Person hinzufügen möchten. Die Einschränkung erfordert, dass das Einkommen zwischen 0 $ und 1.000.000 $ liegt. So können Sie die Einschränkung einrichten:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

Im obigen Beispiel bezieht sich der Punkt "." in der Formel auf die Fragevariable, die den vom Benutzer für die Frage "Income" eingegebenen Wert darstellt. Die Einschränkung ". >= 0 && . <= 1000000" stellt sicher, dass das eingegebene Einkommen größer oder gleich 0 und kleiner oder gleich 1.000.000 ist.

### Strikte Einschränkung (Hard constraint)

### Sanfter Hinweis (Soft alert)
