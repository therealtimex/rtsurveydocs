---
weight: 5
title: "Première connexion"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Comment se connecter à votre instance rtSurvey pour la première fois après le déploiement."
---

> **Le SSL doit être configuré avant de vous connecter.** Si vous accédez à l'application via HTTP, vous verrez un avertissement de sécurité et le SSO sera bloqué. Terminez d'abord la [configuration SSL](ssl-setup).

Une fois SSL actif, ouvrez votre navigateur à votre URL HTTPS :

```
https://your-domain.com
```

---

## L'écran de connexion

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

La page de connexion affiche :

- Les champs **Nom d'utilisateur** et **Mot de passe**
- Un bouton **Se connecter**
- Un bouton **Se connecter avec SSO** (sous un séparateur) — pour les membres de l'équipe avec des comptes SSO

---

## Identifiants administrateur par défaut

Entrez les identifiants par défaut et cliquez sur **Se connecter** :

| Champ | Valeur |
|-------|--------|
| Nom d'utilisateur | `admin` |
| Mot de passe | `admin` |

> **Changez votre mot de passe immédiatement après votre première connexion.**

---

## Si vous voyez un avertissement de sécurité

Si vous accédez à l'application via HTTP (avant la configuration SSL), vous verrez :

- Une bannière d'avertissement jaune en haut de la page de connexion
- Un modal en cliquant sur **Se connecter**, avertissant que les identifiants seront envoyés non chiffrés

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Cliquez sur **Configurer SSL** pour configurer HTTPS, ou sur **Continuer quand même** pour vous connecter sans SSL (non recommandé).

La connexion SSO est entièrement bloquée via HTTP — cliquer sur **Se connecter avec SSO** affichera un avis au lieu de rediriger.

---

## Après la connexion

Une fois connecté, vous arriverez sur le tableau de bord. De là :

1. **Changer le mot de passe administrateur** — paramètres du compte → changer le mot de passe
2. **Créer votre premier projet** — Projets → Nouveau projet
3. **Télécharger ou créer un formulaire** — Formulaires → Télécharger XLSForm ou ouvrir Form Builder
4. **Ajouter des utilisateurs** — Utilisateurs → Inviter ou créer des comptes pour votre équipe
