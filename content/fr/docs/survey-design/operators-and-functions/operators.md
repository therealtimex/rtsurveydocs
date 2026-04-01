---
title: "Opérateurs"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Opérateurs de comparaison

{{< table >}}
Opérateur | Opération      | Exemple              | Résultat de l'exemple
-------- | -------------- | -------------------- | --------------
`=`        | Égal          | ${age} = 25     | vrai ou faux
`!=`       | Différent      | ${age} != 25    | vrai ou faux
`>`        | Supérieur à   | ${age} > 25     | vrai ou faux
`>=`       | Supérieur ou égal | ${age} >= 25 | vrai ou faux
`<`        | Inférieur à      | ${age} < 25     | vrai ou faux
`<=`       | Inférieur ou égal | ${age} <= 25  | vrai ou faux
{{< /table >}}

Dans les exemples ci-dessus, ${age} représente la valeur du champ actuel, et l'opérateur est utilisé pour la comparer à la valeur 25. La contrainte sera évaluée à vrai ou faux selon que la comparaison est satisfaite ou non.

### Opérateurs logiques

Les opérateurs logiques sont utilisés pour combiner plusieurs expressions dans des contraintes. Voici les opérateurs logiques couramment utilisés avec leurs opérations et exemples :

Opérateur | Opération      | Exemple
-------- | -------------- | --------------------------------------------------
`or`       | Retourne vrai si l'une des expressions est vraie | ${age} = 3 or ${age} = 4
`and`      | Retourne vrai uniquement si les deux expressions sont vraies | ${age} > 3 and ${age} < 5
`not()`    | Retourne vrai si l'expression n'est pas vraie | not(${age} > 3 and ${age} < 5)

Dans les exemples ci-dessus, ${age} représente la valeur du champ actuel, et les opérateurs logiques sont utilisés pour combiner les expressions. La contrainte sera évaluée à vrai ou faux selon les conditions spécifiées.

Exemple 1 :
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` retournera `true` si l'âge est 3 ou 4." />}}

Exemple 2 :
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` retournera `true` si l'âge est entre 3 et 5." />}}

Exemple 3 :
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` retournera `true` si l'âge n'est pas entre 3 et 5." />}}
