---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Implante o rtCloud em uma instância EC2 da AWS usando o script de dados do usuário aws-ec2.sh."
---

Use `aws-ec2.sh` como script de **User Data** ao iniciar uma instância EC2. O script é executado automaticamente na primeira inicialização.

**Baixar script:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Etapa 1 — Preencha a configuração

Abra o script e edite o bloco `CONFIGURATION` no início:

```bash
# --- Obrigatório ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Altere após o primeiro login

# --- Domínio + SSL ---
DOMAIN="meuapp.exemplo.com.br"
LETSENCRYPT_EMAIL="admin@exemplo.com.br"

# --- Keycloak integrado ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Padrão para ADMIN_PASSWORD
```

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `PROJECT_ID` | Sim | Usado como nome do banco de dados e ID do cliente Keycloak. Letras minúsculas, sem espaços. |
| `ADMIN_PASSWORD` | Não | Senha do admin do aplicativo e do Keycloak. O padrão é `admin` — **altere após o primeiro login**. |
| `DOMAIN` | Não | Seu domínio para HTTPS. Deixe em branco para modo somente HTTP. |
| `LETSENCRYPT_EMAIL` | Sim (se DOMAIN definido) | E-mail para notificações do Let's Encrypt. |
| `EMBED_KEYCLOAK` | Não | `true` para implantar o Keycloak integrado (requer 4 GB de RAM). |

> **Segurança:** Todas as senhas têm `admin` como padrão. Altere-as imediatamente após o primeiro login.

---

## Etapa 2 — Inicie uma instância EC2

No [console EC2 da AWS](https://console.aws.amazon.com/ec2):

1. Clique em **Iniciar instância**
2. **AMI:** Ubuntu Server 22.04 LTS (64 bits x86)
3. **Tipo de instância:** `t3.medium` (4 GB de RAM) ou maior
4. **Par de chaves:** Selecione ou crie um para acesso SSH
5. **Configurações de rede:** Crie ou selecione um Grupo de segurança (veja abaixo)
6. **Detalhes avançados** → **Dados do usuário** → cole o conteúdo completo do script
7. Clique em **Iniciar instância**

---

## Etapa 3 — Configure o Grupo de segurança

Abra estas portas no Grupo de segurança da instância:

| Porta | Protocolo | Origem | Finalidade |
|-------|-----------|--------|------------|
| 22 | TCP | Seu IP | Acesso SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (redirecionado para HTTPS pelo Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Acesso direto ao Shiny |

> **Não** abra a porta 3306 (MySQL) — ela nunca deve ser acessível publicamente.

---

## Etapa 4 — Adicione o registro DNS

Enquanto a instância inicializa, adicione um **registro A** no seu provedor de DNS:

```
Tipo  : A
Nome  : meuapp
Valor : <ip-público-da-instância>
TTL   : 300
```

---

## Etapa 5 — Monitore o progresso

```bash
ssh ubuntu@<ip-da-instância>
tail -f /var/log/rtcloud-setup.log
```

---

## Etapa 6 — Acesse o aplicativo

Quando a configuração estiver concluída, o log exibe um resumo com a URL do seu aplicativo e as credenciais. Entre com o nome de usuário `admin` e a senha `admin`, depois altere sua senha imediatamente.

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

### Atribuir um IP elástico (opcional)

Se você parar e iniciar a instância, o IP público muda. Para manter um IP estável, aloque um **IP elástico** e associe-o à instância no console EC2.
