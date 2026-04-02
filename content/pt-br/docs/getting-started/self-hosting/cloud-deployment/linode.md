---
weight: 2
title: "Linode (Nuvem Akamai)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implante rtCloud em Linode usando um StackScript. Nenhuma configuração é necessária — basta criar o servidor e seguir as etapas pós-implantação."
---

## Etapa 1 — Inicie o StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Isto abre a página StackScript no Linode Cloud Manager. Clique em **Implementar Novo Linode**.

---

## Passo 2 — Preencha o formulário do Linode

Preencha o formulário de criação de servidor padrão do Linode:

| Campo | Valor recomendado |
|-------|------------------|
| **Imagem** | Ubuntu 22.04LTS |
| **Região** | Mais próximo dos seus usuários |
| **Plano** | CPU compartilhada de 4 GB ou maior |
| **Senha raiz** | Defina uma senha forte |
| **Fuso horário** *(nosso único campo)* | O fuso horário do seu servidor (padrão: `Asia/Ho_Chi_Minh`) |

Clique em **Criar Linode** quando terminar.

---

## Etapa 3 — Aguarde a conclusão da configuração

O script é executado automaticamente na primeira inicialização. Ele instala o Docker, extrai a imagem rtSurvey, inicializa o banco de dados e inicia todos os serviços. Isso leva de **5 a 10 minutos**.

Você pode observar o progresso diretamente no **Linode Cloud Manager** — sem necessidade de SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Clique no seu Linode recém-criado
3. Clique em **Launch LISH Console** (canto superior direito da página de detalhes do Linode)

Um terminal do navegador é aberto mostrando o log de inicialização ao vivo — a guia **Weblish** funciona diretamente no seu navegador, sem necessidade de cliente SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Espere até ver:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

O log também mostra o IP do seu servidor – você precisará dele para a próxima etapa.

---

## Etapa 4 — Configurar SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Siga o **[Guia de configuração de SSL →](../ssl-setup)** para configurar HTTPS. O subdomínio gratuito **rtsurvey.com** é a opção mais rápida – não é necessária configuração de DNS.

---

## Passo 5 — Primeiro login

Assim que o SSL estiver ativo, siga o **[Guia do primeiro login →](../first-login)** para acessar a conta de administrador.

---

## Passo 6 — Altere a senha padrão

Todas as senhas são padronizadas como `admin`. Altere-os imediatamente após seu primeiro login:

- **Senha de administrador do aplicativo** — configurações da conta dentro do aplicativo
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Regras de firewall (Linode Cloud Firewall)

Se anexar um Linode Cloud Firewall a este servidor, utilize as seguintes regras:

### Entrada

| Etiqueta | Ação | Protocolo | Porto | Fontes | Notas |
|---|--------|----------|------|---------|-------|
| `aceitar-entrada-ssh` | Aceitar | TCP | 22 | Tudo IPv4, Tudo IPv6 | Acesso SSH |
| `aceitar-entrada-http` | Aceitar | TCP | 80 | Todos IPv4, Todos IPv6 | Nginx (desafio HTTP + ACME) |
| `aceitar-entrada-https` | Aceitar | TCP | 443 | Todos IPv4, Todos IPv6 | Nginx (HTTPS após configuração SSL) |
| `aceitar-inbound-shiny` | Aceitar | TCP | 3838 | Todos IPv4, Todos IPv6 | Servidor brilhante (análise R) |
| `aceitar-inbound-icmp` | Aceitar | ICMP | — | Tudo IPv4, Tudo IPv6 | Ping/diagnóstico |
| Política de entrada padrão | **Descartar** | | | | Bloqueie todo o resto |

### Saída

| Etiqueta | Ação | Notas |
|-------|--------|-------|
| Política de saída padrão | **Aceitar** | Permitir todas as saídas (pulls do Docker, certbot, API GoDaddy, etc.) |

### Portas NÃO necessárias externamente

Essas portas estão vinculadas apenas a `127.0.0.1` e nunca podem ser acessadas de fora do servidor:

| Porto | Serviço | Razão |
|------|---------|--------|
| 8080 | Contêiner de aplicativo | Nginx faz proxy para ele internamente |
| 8090 | Recipiente Keycloak | Nginx faz proxy para ele internamente |
| 3306 | MySQL | Somente rede Docker interna |

---

## Solução de problemas

### Verifique o log de configuração

```bash
tail -200 /var/log/stackscript.log
```

### Verifique o registro SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Ver o status do contêiner

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
