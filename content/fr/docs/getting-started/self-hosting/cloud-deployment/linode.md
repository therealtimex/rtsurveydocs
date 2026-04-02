---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Déployez rtCloud sur Linode à l'aide d'un StackScript. Aucune configuration nécessaire : créez simplement le serveur et suivez les étapes post-déploiement."
---

## Étape 1 — Lancez le StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Cela ouvre la page StackScript dans Linode Cloud Manager. Cliquez sur **Déployer un nouveau Linode**.

---

## Étape 2 — Remplissez le formulaire de Linode

Remplissez le formulaire standard de création de serveur de Linode :

| Champ | Valeur recommandée |
|-------|------------------|
| **Image** | Ubuntu 22.04 LTS |
| **Région** | Au plus proche de vos utilisateurs |
| **Plan** | CPU partagé 4 Go ou plus |
| **Mot de passe racine** | Définir un mot de passe fort |
| **Fuseau horaire** *(notre seul champ)* | Le fuseau horaire de votre serveur (par défaut : `Asia/Ho_Chi_Minh`) |

Cliquez sur **Créer Linode** lorsque vous avez terminé.

---

## Étape 3 — Attendez la fin de la configuration

Le script s'exécute automatiquement au premier démarrage. Il installe Docker, extrait l'image rtSurvey, initialise la base de données et démarre tous les services. Cela prend **5 à 10 minutes**.

Vous pouvez suivre la progression directement dans **Linode Cloud Manager** — aucun SSH requis :

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Cliquez sur votre Linode nouvellement créé
3. Cliquez sur **Lancer la console LISH** (en haut à droite de la page de détails de Linode)

Un terminal de navigateur s'ouvre et affiche le journal de démarrage en direct : l'onglet **Weblish** fonctionne directement dans votre navigateur, aucun client SSH n'est nécessaire.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Attendez de voir :

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Le journal affiche également l’adresse IP de votre serveur – vous en aurez besoin pour l’étape suivante.

---

## Étape 4 — Configurer SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Suivez le **[Guide de configuration SSL →](../ssl-setup)** pour configurer HTTPS. Le sous-domaine gratuit **rtsurvey.com** est l'option la plus rapide : aucune configuration DNS n'est nécessaire.

---

## Étape 5 — Première connexion

Une fois SSL actif, suivez le **[Guide de première connexion →](../first-login)** pour accéder au compte administrateur.

---

## Étape 6 — Changer le mot de passe par défaut

Tous les mots de passe par défaut sont « admin ». Modifiez-les immédiatement après votre première connexion :

- **Mot de passe administrateur de l'application** — paramètres du compte dans l'application
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Règles de pare-feu (Linode Cloud Firewall)

Si vous attachez un pare-feu Linode Cloud à ce serveur, utilisez les règles suivantes :

### Entrant

| Étiquette | Actions | Protocole | Port | Sources | Remarques |
|-------|--------|----------|------|---------|-------|
| `accepter-inbound-ssh` | Accepter | TCP | 22 | Tout IPv4, Tout IPv6 | Accès SSH |
| `accepter-entrant-http` | Accepter | TCP | 80 | Tout IPv4, Tout IPv6 | Nginx (défi HTTP + ACME) |
| `accepter-entrant-https` | Accepter | TCP | 443 | Tout IPv4, Tout IPv6 | Nginx (HTTPS après configuration SSL) |
| `accepter-entrant-brillant` | Accepter | TCP | 3838 | Tout IPv4, Tout IPv6 | Serveur Shiny (analyse R) |
| `accepter-inbound-icmp` | Accepter | ICMP | — | Tout IPv4, Tout IPv6 | Ping/diagnostic |
| Politique entrante par défaut | **Laisser tomber** | | | | Bloquer tout le reste |

### Sortant

| Étiquette | Actions | Remarques |
|-------|--------|-------|
| Politique sortante par défaut | **Accepter** | Autoriser tous les appels sortants (Docker pulls, certbot, GoDaddy API, etc.) |

### Ports NON nécessaires en externe

Ces ports sont liés à « 127.0.0.1 » uniquement et ne sont jamais accessibles depuis l'extérieur du serveur :

| Port | Services | Raison |
|------|---------|--------|
| 8080 | Conteneur d'applications | Nginx le proxy en interne |
| 8090 | Conteneur de clés | Nginx le proxy en interne |
| 3306 | MySQL | Réseau Docker interne uniquement |

---

## Dépannage

### Vérifiez le journal d'installation

```bash
tail -200 /var/log/stackscript.log
```

### Vérifiez le journal SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Afficher l'état du conteneur

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
