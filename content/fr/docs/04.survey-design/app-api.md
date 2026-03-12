---
title: "API de l'App"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

L'AppAPI permet aux utilisateurs de charger des métadonnées système à partir de l'application en utilisant différentes méthodes dans le FormEngine et DMView. Elle donne accès à diverses clés de données pour récupérer des informations spécifiques de l'application.

Dans l'xlsform, vous pouvez utiliser la fonction `pulldata()` avec la syntaxe suivante :

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'` : Ce mot-clé informe le FormEngine de charger les données à partir de l'API de l'App.
- `'data-key'` : C'est la clé de la donnée que vous souhaitez charger à partir de l'API de l'App.
- Si la clé de données est invalide ou non prise en charge, le calcul renverra "n/a".

Voici les clés de données prises en charge que vous pouvez utiliser avec l'App-API :

`osPlatform` : Renvoie le nom de l'OS actuel (Android ou iOS) et la version de l'OS. Les plateformes Web renverront une valeur vide.

`appPlatform` : Renvoie le nom de la plateforme de l'application, qui est `rtSurvey`.

`appVersion` : Renvoie le nom de la version de l'application.

`getDisplayWidth` : Renvoie la largeur de l'écran de l'appareil en pixels.

`getDisplayHeight` : Renvoie la hauteur de l'écran de l'appareil en pixels.

`getScreenSize` : Renvoie la taille de l'écran de l'appareil en pouces.

`projectCode` : Renvoie le code du projet actuel du site auquel l'utilisateur est connecté.

`projectURL` : Renvoie l'URL du projet actuel du site auquel l'utilisateur est connecté. La valeur par défaut/de secours est un texte vide ("").

`startingPoint` : Renvoie le chemin du point qui démarre le formulaire. Reportez-vous au "Form starting point" pour plus de détails.

`serverTime` : Renvoie la meilleure approximation disponible de la date et de l'heure sur le serveur.

`user.[attribute]` : Renvoie les attributs de l'utilisateur actuel basés sur la clé d'attribut spécifiée. Reportez-vous au tableau "User attributes" pour les clés d'attribut disponibles.

Combinez les clés d'attribut ci-dessous avec "user." dans les paramètres de `pulldata()` pour récupérer les informations de l'utilisateur actuel. Par exemple, utilisez `user.username`, `user.email`, etc.

| Clé d'attribut        | Description                               |
|----------------------|-------------------------------------------|
| username             | Nom d'utilisateur                         |
| name                 | Nom complet de l'utilisateur              |
| staffCode            | Code personnel de l'utilisateur           |
| phone                | Numéro de téléphone                       |
| email                | Adresse e-mail                            |
| description          | Texte de description (infos utilisateur)  |
| organization_id      | ID de l'organisation d'appartenance      |
| organization_name    | Nom de l'organisation d'appartenance     |
| team_id              | ID de l'équipe d'appartenance             |
| supervisor_id        | ID du superviseur de l'utilisateur        |
| user_role            | Rôle de l'utilisateur                     |
| user_group           | Groupe de l'utilisateur                    |
| is_supervisor        | 1 si l'utilisateur est un superviseur, 0 sinon |
| auto_approve_edit_request | 1 si l'utilisateur peut approuver automatiquement les "demandes de modification", 0 sinon |
| ipcall.user          | Paramètre compte IP Call - nom d'utilisateur |
| ipcall.token         | Paramètre compte IP Call - jeton (token)    |
| ipcall.password      | Paramètre compte IP Call - mot de passe     |
| ipcall.url           | Paramètre compte IP Call - URL              |
| ipcall.auth          | Paramètre compte IP Call - auth (optionnel) |
| ipcall.port          | Paramètre compte IP Call - port (optionnel) |

`instancePath` : Renvoie le chemin du dossier de l'instance actuelle.

`appLanguage` : Renvoie la langue actuelle de l'application définie dans les paramètres (ex: vi, en, fr).

`openArgs.[attribute]` : Renvoie l'argument d'ouverture de formulaire passé depuis l'ActionButton (act_fill_form, act_get_instance). La valeur par défaut est un texte vide ("").

`primaryAppColor` : Récupère la couleur principale de l'application.
