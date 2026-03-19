---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implante o rtCloud em um Droplet da DigitalOcean usando scripts de dados do usuário automatizados."
---

A DigitalOcean usa scripts de **User Data** que são executados automaticamente na primeira inicialização. Você preenche as variáveis de configuração no início do script e cola o script completo ao criar um Droplet.

> Diferentemente dos StackScripts do Linode, a DigitalOcean não tem interface de formulário — você deve editar o script diretamente antes de colar.

**Baixar script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak integrado (recomendado)

Use `digitalocean-droplet-keycloak-embed.sh` para a configuração mais simples com SSO integrado.

### Etapa 1 — Preencha a configuração

Abra o script e edite o bloco `CONFIGURATION` no início:

```bash
# --- Obrigatório ---
PROJECT_ID="rtsurvey"                  # Identificador único do seu projeto (sem espaços)
ADMIN_PASSWORD="admin"                 # Senha para admin do aplicativo e do Keycloak — altere após o primeiro login

# --- Domínio + SSL ---
DOMAIN="meuapp.exemplo.com.br"        # Seu domínio — o registro A de DNS deve apontar aqui
PROJECT_URL=""                         # Deixe em branco a menos que esteja atrás do Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@exemplo.com.br" # E-mail para notificações do Let's Encrypt

# --- Opcional ---
STATA_ENABLED="false"
TZ="America/Sao_Paulo"
```

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `PROJECT_ID` | Sim | Usado como nome do banco de dados e ID do cliente Keycloak. Letras minúsculas, sem espaços. |
| `ADMIN_PASSWORD` | Não | Senha para login admin do aplicativo e console admin do Keycloak. O padrão é `admin` — **altere após o primeiro login**. |
| `DOMAIN` | Sim | Seu nome de domínio. O registro A de DNS deve apontar para o IP do Droplet. |
| `LETSENCRYPT_EMAIL` | Sim | Endereço de e-mail para notificações de certificado do Let's Encrypt. |
| `PROJECT_URL` | Não | Substituir a URL pública. Deixe em branco para usar `DOMAIN`. Útil atrás do Cloudflare. |

> **Segurança:** Todas as senhas têm `admin` como padrão. Altere-as imediatamente após o primeiro login.

### Etapa 2 — Crie um Droplet

No [painel de controle da DigitalOcean](https://cloud.digitalocean.com):

1. Clique em **Criar** → **Droplets**
2. Escolha **Ubuntu 22.04 LTS** como imagem
3. Selecione **Basic, 4 GB RAM / 2 vCPUs** ou maior
4. Role até **Opções avançadas** → marque **Adicionar scripts de inicialização**
5. Cole o conteúdo completo do script na área de texto
6. Clique em **Criar Droplet**

### Etapa 3 — Adicione o registro DNS

Enquanto o Droplet inicializa, adicione um **registro A** no seu provedor de DNS:

```
Tipo  : A
Nome  : meuapp          (ou @ para domínio raiz)
Valor : <ip-do-droplet>
TTL   : 300
```

### Etapa 4 — Monitore o progresso

Conecte-se via SSH ao Droplet e acompanhe o log:

```bash
ssh root@<ip-do-droplet>
tail -f /var/log/rtcloud-setup.log
```

O script exibe o IP do servidor no início — adicione o registro DNS assim que você o ver.

### Etapa 5 — Acesse o aplicativo

Quando a configuração estiver concluída, o log exibe um resumo:

```
============================================================
 Implantação do rtCloud concluída! (Keycloak integrado)
============================================================
 URL do aplicativo : https://meuapp.exemplo.com.br
 Admin             : admin / admin
 Keycloak          : https://meuapp.exemplo.com.br/auth/admin

 !! SEGURANÇA: Todas as senhas têm 'admin' como padrão.
    Altere-as imediatamente após o primeiro login.
============================================================
```

Abra `https://meuapp.exemplo.com.br` no seu navegador e entre com o nome de usuário `admin` e a senha `admin`.

> **Altere sua senha** imediatamente após o login em **Configurações** no menu superior direito.

---

## Após a implantação

### Alterar uma senha

Conecte-se via SSH ao Droplet, edite o `.env` e reinicie o contêiner afetado:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Atualizar o domínio

Se você atribuir um domínio diferente após a implantação, atualize `PROJECT_URL` no `.env`:

```bash
nano /opt/rtcloud/.env   # atualize PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos os contêineres

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
