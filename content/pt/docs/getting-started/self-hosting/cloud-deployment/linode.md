---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implante o rtCloud no Linode usando StackScripts com uma UI de configuração baseada em formulário."
---

O Linode usa **StackScripts** — scripts com uma UI baseada em formulário onde preenche os campos de configuração diretamente no Gestor Linode sem editar código algum.

> Os StackScripts Linode são o método de implantação mais fácil. Os campos aparecem como um formulário quando cria um Linode — não é necessária edição de scripts.

---

## Keycloak Incorporado (Recomendado)

### Passo 1 — Encontrar o StackScript

O StackScript está disponível publicamente na comunidade Linode — não é necessária configuração manual:

1. Vá a **Linodes** → **Criar Linode**
2. Em **Escolher uma Distribuição**, selecione **StackScripts** → **StackScripts da Comunidade**
3. Pesquise por **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Selecione-o e preencha o formulário de configuração:

> Em alternativa, [descarregue o script](/scripts/linode-stackscript-keycloak-embed.sh) e crie o seu próprio StackScript em **StackScripts** → **Criar StackScript**.

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| ID do Projeto | Não | Identificador único (predefinição: `rtsurvey`). Usado como nome de base de dados e ID de cliente Keycloak. |
| Palavra-passe Admin Keycloak | Não | Palavra-passe para a consola de admin Keycloak e início de sessão de admin da aplicação. Predefinição `admin` — **altere após o primeiro início de sessão**. |
| Domínio | Sim | O seu nome de domínio. O registo DNS A deve apontar para o IP deste Linode. Necessário para HTTPS e Keycloak. |
| Email da Let's Encrypt | Sim | Email para notificações de certificado da Let's Encrypt. |
| Tag de Imagem Docker | Não | Imagem a implantar (predefinição: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Segurança:** Todas as palavras-passe têm como predefinição `admin`. Altere-as imediatamente após o seu primeiro início de sessão.

5. Escolha **Ubuntu 22.04 LTS** como imagem
6. Escolha o plano **Shared CPU 4 GB** ou maior
7. Clique em **Criar Linode**

### Passo 2 — Adicionar o registo DNS

Enquanto o Linode inicia, adicione um **registo A** no seu fornecedor DNS:

```
Tipo  : A
Nome  : myapp          (ou @ para domínio raiz)
Valor : <linode-ip>
TTL   : 300
```

### Passo 3 — Monitorizar o progresso

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

O script imprime o IP do seu servidor perto do início — adicione o registo DNS assim que o vir.

### Passo 4 — Aceder à aplicação

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

Inicie sessão com o nome de utilizador `admin` e a palavra-passe `admin`, depois altere a sua palavra-passe imediatamente.

---

## Após a Implantação

### Alterar uma palavra-passe

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos os contentores

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Verificar o log

```bash
tail -200 /var/log/stackscript.log
```
