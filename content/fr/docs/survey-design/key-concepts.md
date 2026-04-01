---
title: "Concepts clés"
description: "Aperçu de la conception de formulaires"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Qu'est-ce qu'un XLSForm ?
rtSurvey utilise une version étendue de la norme [XLSForm](https://xlsform.org/) pour la conception de formulaires, offrant des fonctionnalités puissantes pour créer des enquêtes sophistiquées. Ce guide vous présentera les concepts clés de la conception de formulaires dans rtSurvey, de la structure de base XLSForm aux fonctionnalités avancées spécifiques à rtSurvey.

Avec XLSForms, vous pouvez créer des formulaires dans un format lisible par l'homme en utilisant l'outil familier Excel, ce qui le rend accessible à presque tout le monde.
Cette norme permet un partage et une collaboration faciles sur la création de formulaires.

Bien que les XLSForms soient conviviaux pour les débutants, ils permettent également aux utilisateurs expérimentés de créer des formulaires complexes.

rtSurvey offre un moyen cohérent d'incorporer des fonctionnalités avancées telles que la logique de saut (skip logic) dans les formulaires sur diverses plateformes de collecte de données web et mobiles.

## Structure de l'XLSForm
Un XLSForm se compose généralement de deux feuilles de calcul principales :

1. **survey** : Définit la structure et le contenu de votre formulaire.
2. **choices** : Spécifie les choix de réponses pour les questions à choix multiples.

Une feuille de calcul optionnelle **settings** peut fournir des spécifications supplémentaires pour le formulaire.

Il est important de noter que les colonnes obligatoires dans les feuilles de calcul survey et choices doivent être présentes pour que le formulaire fonctionne correctement. Les colonnes optionnelles dans les deux feuilles offrent un contrôle supplémentaire sur le comportement de chaque entrée dans le formulaire mais ne sont pas essentielles.

Les colonnes de votre classeur Excel peuvent apparaître dans n'importe quel ordre, et les colonnes optionnelles peuvent être laissées vides. Cependant, il est crucial d'utiliser la syntaxe précise et les conventions de nommage spécifiées dans la documentation XLSForm pour que le formulaire fonctionne correctement.

### La feuille de calcul survey
La **feuille de calcul survey** est l'endroit où vous définissez la structure de votre formulaire et fournissez le contenu. Chaque ligne de la feuille survey représente une question ou un élément de votre formulaire. Les colonnes suivantes sont obligatoires dans la feuille survey :

- `type` : Spécifie le type d'entrée que vous attendez pour la question.
- `name` : Spécifie le nom de variable unique pour cette entrée. Les noms doivent commencer par une lettre ou un tiret bas et ne peuvent contenir que des lettres, des chiffres, des traits d'union, des tirets bas et des points. Les noms sont sensibles à la casse.
- `label` : Contient le texte réel que vous voyez pour la question dans le formulaire.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Respondent's gender? |
| integer             | age      | Respondent's age?    |

### La feuille de calcul choices
La feuille de calcul **`choices`** est utilisée pour spécifier les choix de réponses pour les questions à choix multiples.
Chaque ligne représente un choix de réponse. Les colonnes suivantes sont obligatoires dans la feuille choices :

- **`list_name`** : Regroupe un ensemble de choix de réponses liés.
- **`name`** : Spécifie le nom de variable unique pour ce choix de réponse.
- **`label`** : Affiche le choix de réponse exactement tel qu'il doit apparaître sur le formulaire.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgender          |
| gender              | female      | Female               |
| gender              | male        | Male                 |
| gender              | other       | Other                |

Les colonnes que vous ajoutez à votre classeur Excel, qu'elles soient obligatoires ou optionnelles, peuvent apparaître dans n'importe quel ordre. Les colonnes optionnelles peuvent être complètement omises. Des lignes ou des colonnes peuvent être laissées vides pour faciliter la lisibilité, mais les données après 20 colonnes ou lignes vides adjacentes sur une feuille ne seront pas traitées. Tout formatage de fichier .xlsx est ignoré, vous pouvez donc utiliser des lignes de division, des ombrages et d'autres formatages de police pour rendre le formulaire plus lisible.

Une chose à garder à l'esprit lors de la création de formulaires dans Excel est que la syntaxe que vous utilisez doit être précise. Par exemple, si vous écrivez **Choices** ou **choice** au lieu de **choices**, le formulaire ne fonctionnera pas.

### La feuille de calcul settings

La feuille de calcul settings est optionnelle mais vous permet de spécifier les métadonnées et le comportement au niveau du formulaire. Les colonnes courantes de la feuille settings incluent :

| Colonne | Description |
|--------|-------------|
| form_title | Le titre du formulaire tel qu'il apparaît aux utilisateurs |
| form_id | Un identifiant unique pour le formulaire, utilisé dans la gestion des données et les appels API |
| default_language | Le code de langue par défaut pour les formulaires multilingues (par exemple, 'fr' pour le français) |
| version | Le numéro de version du formulaire, utile pour le suivi des modifications |
| instance_name | Expression pour générer un nom unique pour chaque soumission de formulaire |
| generation | Nombre entier marquant la génération du formulaire. À incrémenter pour les changements structurels |
| family | Identifiant pour regrouper les formulaires liés à travers les changements structurels |

La feuille settings dans rtSurvey peut également inclure des configurations supplémentaires spécifiques aux fonctionnalités étendues de rtSurvey. Reportez-vous à la documentation de rtSurvey pour une liste complète des paramètres pris en charge.

## Composants Clés de la Feuille survey

La feuille de calcul survey est le cœur de la conception de votre formulaire. Voici un aperçu de ses composants clés :

| Composant | Description |
|-----------|-------------|
| [type](#question-types) | Spécifie le type de question (ex: text, integer, select_one) |
| [name](#naming-conventions) | Identifiant unique pour la question |
| [label](#labels-and-translations) | Le texte affiché au répondant |
| [hint](#hints-and-help-text) | Conseils supplémentaires pour le répondant |
| [appearance](#appearance-options) | Modifie la façon dont la question est affichée |
| [relevant](#relevance-and-skip-logic) | Détermine quand la question doit être posée (logique de saut) |
| [constraint](#constraints-and-validation) | Valide la réponse |
| [calculation](#calculations) | Calcule des valeurs basées sur d'autres réponses |
| [required](#required-fields) | Spécifie si la question doit obligatoirement être répondue |

Chacun de ces composants joue un rôle crucial dans la création d'enquêtes efficaces et performantes. Cliquez sur les liens dans la colonne "Composant" pour en savoir plus sur chacun d'eux.

### Types de questions
XLSForm prend en charge un certain nombre de types de questions. Voici quelques-unes des options que vous pouvez saisir dans la colonne **`type`** de la feuille **`survey`** de votre XLSForm :

| Type de question          | Entrée attendue                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| integer                   | Entrée d'un nombre entier.                                                                   |
| decimal                   | Entrée d'un nombre décimal.                                                                  |
| range                     | Entrée de type [Plage](#range) (y compris les évaluations).                                  |
| text                      | Réponse en texte libre.                                                                      |
| select_one [options]      | Question à [choix multiples](#multiple-choice) ; une seule réponse peut être sélectionnée.   |
| select_multiple [options] | Question à [choix multiples](#multiple-choice) ; plusieurs réponses peuvent être sélectionnées. |
| select_one_from_file [file]| [Choix multiples à partir d'un fichier](#multiple-choice-from-file) ; une seule réponse possible. |
| select_multiple_from_file [file]| [Choix multiples à partir d'un fichier](#multiple-choice-from-file) ; plusieurs réponses possibles.|
| rank [options]            | Question de [rang](#rank) ; ordonner une liste.                                              |
| note                      | Affiche une note à l'écran, ne prend aucune entrée. Raccourci pour type=text avec readonly=true. |
| geopoint                  | Collecter une [seule coordonnée GPS](#gps).                                                  |
| geotrace                  | Enregistrer une [ligne de deux coordonnées GPS ou plus](#gps).                               |
| geoshape                  | Enregistrer un [polygone de plusieurs coordonnées GPS](#gps) ; le dernier point est le même que le premier. |
| date                      | Entrée d'une date.                                                                           |
| time                      | Entrée d'une heure.                                                                          |
| dateTime                  | Accepte l'entrée d'une date et d'une heure.                                                  |
| image                     | Prendre une photo ou charger un [fichier image](#image).                                      |
| audio                     | Enregistrer un message audio ou charger un fichier audio.                                    |
| background-audio          | L'audio est enregistré en arrière-plan pendant le remplissage du formulaire.                |
| video                     | Enregistrer une vidéo ou charger un fichier vidéo.                                          |
| file                      | Entrée de fichier générique (txt, pdf, xls, xlsx, doc, docx, rtf, zip).                      |
| barcode                   | Scanner un code-barres, nécessite l'installation de l'application de lecture de codes-barres. |
| calculate                 | Effectuer un calcul ; voir la section [Calcul](#calculation) ci-dessous.                     |
| acknowledge               | Invite de confirmation qui définit la valeur sur "OK" si sélectionnée.                       |
| hidden                    | Un champ sans élément d'interface associé qui peut être utilisé pour stocker une constante.  |
| xml-external              | Ajoute une référence à un fichier de [données XML externes](#external-xml-data).             |

### Étiquettes (Labels)

Les étiquettes sont le texte affiché aux répondants pour chaque question. Elles sont cruciales pour une communication claire dans les enquêtes.

- **Utilisation de base** : Dans la colonne `label`, saisissez le texte de la question.
- **Plusieurs langues** : Utilisez des colonnes supplémentaires comme `label::English` et `label::French` pour les enquêtes multilingues.
- **Formatage** : rtSurvey prend en charge le formatage HTML de base dans les étiquettes pour l'accentuation ou la structure.

Exemple :
```
| type | name | label | label::French |
|------|------|-------|---------------|
| text | name | What is your name? | Quel est votre nom ? |
```

### Conseils (Hints)

Les conseils fournissent des indications supplémentaires aux répondants sans encombrer le texte principal de la question.

- **Utilisation** : Ajoutez des conseils dans la colonne `hint`.
- **Visibilité** : Les conseils sont généralement affichés sous le texte principal de la question.
- **Multilingue** : Comme les étiquettes, les conseils peuvent être spécifiés pour plusieurs langues à l'aide des colonnes `hint::Langue`.

Exemple :
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Quel âge avez-vous ? | Veuillez entrer votre âge en années |
```

### Apparence (Appearance)

La colonne `appearance` dans rtSurvey permet de personnaliser la façon dont les questions sont affichées.

- **Options standard** : Incluent 'multiline' pour le texte, 'horizontal' pour les questions à choix.
- **Extensions rtSurvey** :
  - Entrée de l'heure : Diverses options d'affichage de l'horloge (par exemple, `inline`, `inline-1line`)
  - Personnalisation des couleurs : Utilisez la fonction `colors()` pour changer les couleurs des icônes

Exemple :
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Entrer l'heure | inline-[%H:%M] |
```

### Pertinence (Relevant)

La colonne `relevant` implémente la logique de saut, déterminant quand une question doit être affichée.

- **Syntaxe** : Utilisez des expressions XPath pour définir les conditions.
- **Variables** : Référencez d'autres noms de questions en utilisant `${nom_question}`.

Exemple :
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Liste des allergies | ${a_des_allergies} = 'yes' |
```

### Obligatoire (Required)

La colonne `required` spécifie si une réponse à la question est obligatoire.

- **Utilisation de base** : Utilisez 'yes' ou 'true' pour rendre une question obligatoire.
- **Avancé** : Peut utiliser des expressions pour un caractère obligatoire conditionnel.

Exemple :
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | Adresse e-mail | yes |
```

### Répétitions (Repeats)

Les répétitions permettent à un groupe de questions d'être répondues plusieurs fois.

- **Utilisation** : Utilisez les lignes `begin repeat` et `end repeat` pour définir un groupe répétitif.
- **Nommage** : Donnez à chaque groupe de répétition un nom unique.

Exemple :
```
| type | name | label |
|------|------|-------|
| begin repeat | membre_foyer | Membre du foyer |
| text | nom_membre | Nom |
| integer | age_membre | Âge |
| end repeat | | |
```

### Médias (Media)

rtSurvey prend en charge divers types de médias dans les enquêtes, notamment les images, l'audio et la vidéo.

- **Types de questions** : Utilisez 'image', 'audio' ou 'video' dans la colonne type.
- **Médias dans les étiquettes** : Référencez des fichiers multimédias dans les étiquettes à l'aide de balises HTML.

Exemple :
```
| type | name | label |
|------|------|-------|
| image | photo_maison | Prendre une photo de la maison |
| note | | <img src="logo.jpg" /> Bienvenue dans l'enquête |
```

### Lecture seule (Read-only)

Les questions en lecture seule affichent des informations sans permettre la saisie de l'utilisateur.

- **Utilisation** : Ajoutez 'readonly' dans la colonne `appearance` ou utilisez la colonne `read_only`.
- **Calculs** : Souvent utilisé avec le type calculate pour afficher des valeurs calculées.

Exemple :
```
| type      | name | label | appearance | calculation |
|-----------|------|-------|------------|-------------|
| calculate | imc  | IMC   | readonly   | ${poids} / (${taille} * ${taille}) |
```

## Extensions rtSurvey

rtSurvey enrichit la norme XLSForm en prenant en charge des capacités supplémentaires telles que la mise en page en grille (`grid layout`), le format HTML (`html format`) et de nombreux nouveaux widgets.

### Mise en page en grille (Grid layout)
rtSurvey permet à votre formulaire d'imiter l'apparence des enquêtes papier traditionnelles en compactant plusieurs questions sur une seule ligne.

### Paramètres du formulaire

### Paramètres de données

### Style Typeform

### Extension de pulldata()

### Extensions basées sur l'apparence

### Extensions Webbox
