---
title: "Validation des réponses"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Un moyen d'assurer la qualité des données est d'ajouter des contraintes aux champs de données de votre formulaire. Les contraintes aident à empêcher les utilisateurs de saisir des réponses invalides ou impossibles. Par exemple, lors de la demande de revenus d'une personne, vous voulez éviter des valeurs irréalistes, telles que des nombres négatifs ou des valeurs extrêmement élevées. Ajouter des contraintes de données dans votre formulaire est facile. Suivez simplement les étapes ci-dessous :

1. Ajoutez une nouvelle colonne appelée "constraint" à votre formulaire.
2. Dans la colonne "constraint", entrez une formule qui spécifie les limites de la réponse.

### Exemple

Considérons un exemple où nous voulons ajouter une contrainte pour les revenus d'une personne. La contrainte exige que les revenus soient compris entre 0 $ et 1 000 000 $. Voici comment vous pouvez configurer la contrainte :

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

Dans l'exemple ci-dessus, le "." dans la formule fait référence à la variable de la question, qui représente la valeur saisie par l'utilisateur pour la question "Income". La contrainte ". >= 0 && . <= 1000000" garantit que le revenu saisi est supérieur ou égal à 0 et inférieur ou égal à 1 000 000.

### Contrainte stricte (Hard constraint)

### Alerte souple (Soft alert)
