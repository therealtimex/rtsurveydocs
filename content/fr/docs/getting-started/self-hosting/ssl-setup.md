---
weight: 4
title: "Configuration SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configurez HTTPS pour votre serveur rtSurvey. Requis avant de vous connecter."
---

SSL doit être configuré avant de pouvoir vous connecter. Lorsque vous ouvrez l'application pour la première fois, vous serez automatiquement redirigé vers l'écran de configuration SSL.

---

## Options de configuration SSL

![Options de configuration SSL](/img/ssl-setup/ssl-setup-options.png)

Choisissez l'une des trois options :

| Option | Quand l'utiliser |
|--------|-----------------|
| **Sous-domaine rtsurvey.com gratuit** *(Recommandé)* | Aucune configuration DNS nécessaire. Nous créons l'enregistrement pour vous. Prêt en 2–5 minutes. |
| **Mon propre domaine** | Vous avez déjà un domaine et son DNS pointe vers ce serveur. |
| **Installer le certificat manuellement** | Entreprise ou CA personnalisé. Nécessite un accès SSH. |

---

## Option 1 — Sous-domaine rtsurvey.com gratuit *(Recommandé)*

C'est l'option la plus rapide. Aucun enregistrement de domaine ni modification DNS requis.

1. Cliquez sur **Sous-domaine rtsurvey.com gratuit** pour développer la section
2. Saisissez le nom de sous-domaine souhaité dans le champ de saisie

   > Utilisez des lettres minuscules, des chiffres et des tirets. 3–30 caractères.
   > Exemple : `myproject` → `myproject.rtsurvey.com`

3. Cliquez sur **Créer https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Attendez 2–5 minutes pendant l'émission du certificat

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Une fois le certificat prêt, vous serez automatiquement redirigé vers votre nouvelle URL HTTPS

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — Mon propre domaine

Utilisez ceci si vous avez un domaine existant et que son enregistrement DNS `A` pointe déjà vers l'IP de ce serveur.

1. Cliquez sur **Mon propre domaine** pour développer la section
2. Saisissez votre nom de domaine complet (ex. `survey.myorganization.org`)
3. Cliquez sur **Créer le certificat**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vérifiera votre domaine et émettra un certificat. Le DNS doit être correctement pointé au préalable — sinon la demande échouera.

---

## Option 3 — Installer le certificat manuellement

Pour les environnements d'entreprise utilisant une CA personnalisée ou interne. Vous placerez vos fichiers de certificat sur le serveur via SSH, puis saisirez votre domaine dans l'application.

### Prérequis

- Accès SSH au serveur
- Certificat valide et clé privée pour votre domaine (format PEM)

### Étape 1 — SSH sur le serveur

```bash
ssh root@<server-ip>
```

### Étape 2 — Placer vos fichiers de certificat

Créez le répertoire et copiez vos fichiers :

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copiez vos fichiers avec ces noms exacts :

| Fichier | Description |
|---------|-------------|
| `fullchain.pem` | Votre certificat + certificats CA intermédiaires (concaténés) |
| `privkey.pem` | Votre clé privée |

Exemple :

```bash
# Copier depuis votre machine locale (exécuter localement, pas sur le serveur)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Définir les permissions correctes :

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Étape 3 — Saisir votre domaine dans l'application

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Sur l'écran de configuration SSL, cliquez sur **Installer le certificat manuellement**
2. Saisissez votre nom de domaine (doit correspondre au Common Name ou SAN du certificat)
3. Cliquez sur **Appliquer**

Le serveur configurera Nginx avec votre certificat et rechargera automatiquement.

---

## Étape suivante

Une fois SSL actif, passez à la [Première connexion](first-login).
