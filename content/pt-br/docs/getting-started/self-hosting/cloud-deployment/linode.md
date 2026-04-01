---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implante o rtCloud no Linode usando StackScripts com uma interface de configuração baseada em formulário."
---

O Linode usa **StackScripts** — scripts com uma interface de usuário baseada em formulário onde você preenche os campos de configuração diretamente no Linode Manager sem editar nenhum código.

> Os StackScripts do Linode são o método de implantação mais fácil. Os campos aparecem como um formulário ao criar um Linode — não é necessário editar scripts.

---

## Keycloak integrado (recomendado)

### Etapa 1 — Encontre o StackScript

O StackScript está disponível publicamente na comunidade do Linode — não é necessária configuração manual:

1. Vá para **Linodes** → **Criar Linode**
2. Em **Escolher uma distribuição**, selecione **StackScripts** → **StackScripts da comunidade**
3. Pesquise **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Selecione-o e preencha o formulário de configuração:

> Como alternativa, [baixe o script](/scripts/linode-stackscript-keycloak-embed.sh) e crie seu próprio StackScript em **StackScripts** → **Criar StackScript**.

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| ID do projeto | Não | Identificador único (padrão: `rtsurvey`). Usado como nome do banco de dados e ID do cliente Keycloak. |
| Senha do admin do Keycloak | Não | Senha para o console admin do Keycloak e login admin do aplicativo. O padrão é `admin` — **altere após o primeiro login**. |
| Domínio | Sim | Seu nome de domínio. O registro A de DNS deve apontar para o IP deste Linode. Necessário para HTTPS e Keycloak. |
| E-mail do Let's Encrypt | Sim | E-mail para notificações de certificado do Let's Encrypt. |
| Tag da imagem Docker | Não | Imagem a ser implantada (padrão: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Segurança:** Todas as senhas têm `admin` como padrão. Altere-as imediatamente após o primeiro login.

5. Escolha **Ubuntu 22.04 LTS** como imagem
6. Escolha o plano **Shared CPU 4 GB** ou maior
7. Clique em **Criar Linode**

### Etapa 2 — Adicione o registro DNS

Enquanto o Linode inicializa, adicione um **registro A** no seu provedor de DNS:

```
Tipo  : A
Nome  : meuapp          (ou @ para domínio raiz)
Valor : <ip-do-linode>
TTL   : 300
```

### Etapa 3 — Monitore o progresso

```bash
ssh root@<ip-do-linode>
tail -f /var/log/stackscript.log
```

O script exibe o IP do servidor no início — adicione o registro DNS assim que você o ver.

### Etapa 4 — Acesse o aplicativo

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

Entre com o nome de usuário `admin` e a senha `admin`, depois altere sua senha imediatamente.

---

## Após a implantação

### Alterar uma senha

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos os contêineres

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Verificar o log

```bash
tail -200 /var/log/stackscript.log
```
