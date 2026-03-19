---
title: "Examens"
description: "La fonctionnalité examen ajoute un mode quiz chronométré à une enquête, avec des retours audio optionnels pour les réponses correctes et incorrectes."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

La fonctionnalité **Examen** transforme une enquête en quiz chronométré. Un minuteur de compte à rebours est affiché au répondant, et l'enquête enregistre le temps restant lorsqu'il a terminé. Optionnellement, des sons audio peuvent se déclencher pour les réponses correctes et incorrectes.

C'est utile pour les évaluations des connaissances, les tests d'alphabétisation, les contrôles de compétences du personnel de terrain, et toute enquête où le temps passé sur la tâche est une donnée significative.

---

## Fonction `check-exam()`

Configurez l'examen en utilisant `check-exam()` dans la colonne **`calculation`** d'un champ `calculate` placé au début du formulaire :

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Paramètres

| # | Paramètre | Description |
|---|-----------|-------------|
| 1 | `examTime` | Durée totale de l'examen en secondes |
| 2 | `questionToStoreRemainingTime` | Le `name` d'un champ `calculate` ou `integer` qui stockera le temps restant à la fin de l'examen |
| 3 | `rightSound` | *(Optionnel)* Nom du fichier audio à jouer lors d'une réponse correcte (à joindre au formulaire comme fichier média) |
| 4 | `wrongSound` | *(Optionnel)* Nom du fichier audio à jouer lors d'une réponse incorrecte |
| 5 | `excludeQuestion` | *(Optionnel)* Liste séparée par des virgules de noms de champs à exclure du minuteur (ex. : `'intro_note,consent'`) |

---

## Configuration de base

### Étape 1 : Ajouter les champs d'examen

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` déclenche le minuteur de 600 secondes (10 minutes). `remaining_time` est rempli automatiquement lorsque le répondant a terminé.

### Étape 2 : Ajouter vos questions

Le minuteur couvre toutes les questions du formulaire sauf celles listées dans `excludeQuestion`.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | La capitale du Kenya est Nairobi. Vrai ou faux ? |
| select_one choices | q2 | Quel organe pompe le sang dans le corps ? |
| select_one choices | q3 | L'eau bout à 100°C au niveau de la mer. Vrai ou faux ? |

### Étape 3 : Stocker le temps restant

Le champ nommé dans le paramètre 2 (`remaining_time`) est automatiquement défini au nombre de secondes restantes lorsque le répondant soumet. Une valeur de `0` signifie que le temps s'est écoulé ; une valeur élevée signifie qu'il a terminé rapidement.

---

## Avec retour audio

Joignez des fichiers sonores au formulaire (comme pièces jointes médias), puis référencez-les :

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` se joue lorsque le répondant sélectionne la bonne réponse
- `wrong.mp3` se joue lorsque le répondant sélectionne une mauvaise réponse

{{% alert icon=" " context="warning" %}}
Les fichiers sonores doivent être joints au formulaire comme fichiers médias et le nom de fichier doit correspondre exactement (sensible à la casse) y compris l'extension.
{{% /alert %}}

---

## Exclure des questions du minuteur

Passez une liste de noms de champs séparés par des virgules pour les exclure de l'examen (ex. : notes d'introduction ou questions de consentement) :

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Laissez `rightSound` et `wrongSound` comme chaînes vides `''` si vous n'avez pas besoin d'audio mais avez besoin d'exclusions.

---

## Exemple complet

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Bienvenue à l'évaluation des connaissances en santé. Vous avez 5 minutes pour répondre à toutes les questions. | |
| trigger | start_ack | Appuyez sur OK quand vous êtes prêt à commencer. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | Le lavage des mains prévient la propagation des maladies. | |
| select_one yesno | q2 | Vous devriez boire au moins 2 litres d'eau par jour. | |
| select_one yesno | q3 | Le paludisme est causé par un virus. | |

---

## Bonnes pratiques

1. Informez toujours les répondants de la limite de temps avant de commencer — utilisez une `note` ou un `trigger` avant le champ `check-exam()`.
2. Excluez les notes d'introduction et les questions de consentement du minuteur en utilisant le paramètre `excludeQuestion`.
3. Utilisez `remaining_time` dans un calcul de suivi pour détecter les expirations : `if(${remaining_time} = 0, 'Temps écoulé', 'Terminé')`.
4. Gardez le nombre de questions proportionnel au temps imparti — 2 à 3 minutes par question est une base raisonnable pour la plupart des évaluations de connaissances.
5. Testez avec des fichiers audio sur l'appareil réel avant le déploiement — la lecture audio varie selon les versions Android et les navigateurs.

## Limitations

- Le minuteur est uniquement indicatif — le formulaire ne se soumet pas automatiquement à l'expiration du temps ; le répondant doit toujours soumettre manuellement.
- Le retour audio nécessite que le volume de l'appareil soit activé et non mis en sourdine.
- La fonctionnalité examen est une extension rtSurvey et ne fait pas partie de la spécification XLSForm standard.
