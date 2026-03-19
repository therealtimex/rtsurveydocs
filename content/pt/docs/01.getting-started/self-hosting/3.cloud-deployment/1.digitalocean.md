---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implante o rtCloud num Droplet DigitalOcean usando scripts de dados de utilizador automatizados."
---

O DigitalOcean usa scripts de **Dados de Utilizador** que são executados automaticamente na primeira inicialização. Preenche as variáveis de configuração no topo do script e depois cola o script completo ao criar um Droplet.

> Ao contrário dos StackScripts Linode, o DigitalOcean não tem UI de formulário — deve editar o script diretamente antes de colar.

**Descarregar script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak Incorporado (Recomendado)

Use `digitalocean-droplet-keycloak-embed.sh` para a configuração mais simples com SSO incorporado.

### Passo 1 — Preencher a configuração

Abra o script e edite o bloco `CONFIGURAÇÃO` no topo:

```bash
# --- Obrigatório ---
PROJECT_ID="rtsurvey"                  # Identificador único para o seu projeto (sem espaços)
ADMIN_PASSWORD="admin"                 # Palavra-passe para o admin da aplicação e Keycloak — altere após o primeiro início de sessão

# --- Domínio + SSL ---
DOMAIN="myapp.example.com"            # O seu domínio — o registo DNS A deve apontar aqui
PROJECT_URL=""                         # Deixe em branco a menos que esteja atrás do Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email para notificações da Let's Encrypt

# --- Opcional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `PROJECT_ID` | Sim | Usado como nome de base de dados e ID de cliente Keycloak. Minúsculas, sem espaços. |
| `ADMIN_PASSWORD` | Não | Palavra-passe para início de sessão de admin da aplicação e consola de admin Keycloak. Predefinição `admin` — **altere após o primeiro início de sessão**. |
| `DOMAIN` | Sim | O seu nome de domínio. O registo DNS A deve apontar para o IP do Droplet. |
| `LETSENCRYPT_EMAIL` | Sim | Endereço de email para notificações de certificado da Let's Encrypt. |
| `PROJECT_URL` | Não | Substituir o URL público. Deixe em branco para usar `DOMAIN`. Útil atrás do Cloudflare. |

> **Segurança:** Todas as palavras-passe têm como predefinição `admin`. Altere-as imediatamente após o seu primeiro início de sessão.

### Passo 2 — Criar um Droplet

No [painel de controlo DigitalOcean](https://cloud.digitalocean.com):

1. Clique em **Criar** → **Droplets**
2. Escolha **Ubuntu 22.04 LTS** como imagem
3. Selecione **Basic, 4 GB RAM / 2 vCPUs** ou maior
4. Role até **Opções Avançadas** → marque **Adicionar scripts de inicialização**
5. Cole o conteúdo completo do script na área de texto
6. Clique em **Criar Droplet**

### Passo 3 — Adicionar o registo DNS

Enquanto o Droplet inicia, adicione um **registo A** no seu fornecedor DNS:

```
Tipo  : A
Nome  : myapp          (ou @ para domínio raiz)
Valor : <droplet-ip>
TTL   : 300
```

### Passo 4 — Monitorizar o progresso

Aceda ao Droplet via SSH e observe o log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

O script imprime o IP do seu servidor perto do início — adicione o registo DNS assim que o vir.

### Passo 5 — Aceder à aplicação

Quando a configuração estiver concluída, o log mostra um resumo:

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

Abra `https://myapp.example.com` no seu navegador e inicie sessão com o nome de utilizador `admin` e a palavra-passe `admin`.

> **Altere a sua palavra-passe** imediatamente após o início de sessão em **Configurações** no menu superior direito.

---

## Após a Implantação

### Alterar uma palavra-passe

Aceda ao Droplet via SSH, edite `.env` e reinicie o contentor afetado:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Atualizar o domínio

Se atribuir um domínio diferente após a implantação, atualize `PROJECT_URL` em `.env`:

```bash
nano /opt/rtcloud/.env   # atualize PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos os contentores

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
