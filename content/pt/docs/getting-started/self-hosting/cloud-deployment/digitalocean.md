---
weight: 1
title: "Oceano Digital"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implante rtCloud em um Droplet DigitalOcean usando scripts automatizados de dados do usuário."
---

A DigitalOcean usa scripts **User Data** que são executados automaticamente na primeira inicialização. Você preenche as variáveis ​​de configuração na parte superior do script e, em seguida, cola o script inteiro ao criar um Droplet.

> Ao contrário do Linode StackScripts, o DigitalOcean não possui interface de usuário de formulário - você deve editar o script diretamente antes de colar.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak incorporado (recomendado)

Use `digitalocean-droplet-keycloak-embed.sh` para a configuração mais simples com SSO integrado.

### Passo 1 — Preencha a configuração

Abra o script e edite o bloco `CONFIGURATION` na parte superior:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Obrigatório | Descrição |
|-------|----------|------------|
| `PROJETO_ID` | Sim | Usado como nome do banco de dados e ID do cliente Keycloak. Minúsculas, sem espaços. |
| `ADMIN_PASSWORD` | Não | Senha para login de administrador do aplicativo e console de administração Keycloak. O padrão é `admin` — **alterar após o primeiro login**. |
| `DOMÍNIO` | Sim | Seu nome de domínio. O registro DNS A deve apontar para o IP do Droplet. |
| `LETSENCRYPT_EMAIL` | Sim | Endereço de e-mail para notificações de certificado Let's Encrypt. |
| `PROJETO_URL` | Não | Substitua o URL público. Deixe em branco para usar `DOMAIN`. Útil por trás do Cloudflare. |

> **Segurança:** Todas as senhas são padronizadas como `admin`. Altere-os imediatamente após seu primeiro login.

### Passo 2 — Crie uma gota

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Clique em **Criar** → **Gotas**
2. Escolha **Ubuntu 22.04 LTS** como imagem
3. Selecione **Básico, 4 GB de RAM/2 vCPUs** ou maior
4. Vá até **Opções avançadas** → marque **Adicionar scripts de inicialização**
5. Cole o conteúdo completo do script na área de texto
6. Clique em **Criar gota**

### Etapa 3 — Adicione o registro DNS

Enquanto o Droplet inicializa, adicione um registro **A** em seu provedor de DNS:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Etapa 4 — Monitore o progresso

SSH no Droplet e observe o log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

O script imprime o IP do seu servidor próximo ao início – adicione o registro DNS assim que você o vir.

### Passo 5 — Acesse o aplicativo

Quando a configuração for concluída, o log mostrará um resumo:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Altere sua senha** imediatamente após o login em **Configurações** no menu superior direito.

---

## Após a implantação

### Alterar uma senha

SSH no Droplet, edite `.env` e reinicie o contêiner afetado:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Atualize o domínio

Se você atribuir um domínio diferente após a implantação, atualize `PROJECT_URL` em `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos os contêineres

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
