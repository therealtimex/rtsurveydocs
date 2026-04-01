---
weight: 1
title: "Início rápido"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Coloque o rtCloud em funcionamento no seu próprio servidor em menos de 10 minutos usando o Docker Compose."
---

Este guia orienta você na implantação de uma instância do rtCloud com hospedagem própria em um servidor Linux do zero. Ao final, você terá um rtCloud em execução acessível no seu navegador.

## Pré-requisitos

Certifique-se de que seu servidor atende aos seguintes requisitos antes de começar:

### Hardware

| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| RAM | 2 GB | 4 GB |
| Disco | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |

### Software

| Software | Versão |
|----------|--------|
| SO | Ubuntu 20.04 LTS ou mais recente (ou qualquer Linux com suporte ao Docker) |
| Docker | 20.10 ou mais recente |
| Docker Compose | v2.x (`docker compose`) ou v1.x (`docker-compose`) |

**Instalar o Docker no Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Verifique a instalação:

```bash
docker --version
docker compose version
```

---

## Etapa 1 — Obtenha os arquivos

Clone o repositório de implantação no seu servidor:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Etapa 2 — Configure o ambiente

Copie o arquivo de configuração de exemplo:

```bash
cp .env.production.sample .env
```

Abra o `.env` em um editor de texto e preencha os valores necessários:

```dotenv
# Identificador único para esta implantação (sem espaços, sem caracteres especiais)
PROJECT_ID=meuprojeto

# Domínio ou endereço IP onde os usuários acessarão o aplicativo
# Exemplo: rtcloud.exemplo.com.br  ou  192.168.1.100
PROJECT_URL=rtcloud.exemplo.com.br

# Protocolo: use "https" se tiver um domínio com SSL, "http" caso contrário
HTTP_PROTOCOL=https

# Senhas fortes e únicas — altere todas as três antes de iniciar
MYSQL_PASSWORD=minha_senha_forte
MYSQL_ROOT_PASSWORD=minha_senha_root
ADMIN_PASSWORD=minha_senha_admin
```

> **Importante:** Apenas o `.env` é lido automaticamente pelo Docker Compose. Não crie um arquivo chamado `.env.production`, pois isso causaria confusão. O `ADMIN_PASSWORD` é aplicado somente na **primeira inicialização** de um banco de dados novo.

---

## Etapa 3 — Inicie os contêineres

Inicie todos os serviços em segundo plano:

```bash
docker compose -f docker-compose.production.yml up -d
```

A primeira inicialização leva **3 a 5 minutos** enquanto o Docker:

1. Baixa a imagem do aplicativo rtCloud (download de ~1 GB)
2. Inicializa o banco de dados MySQL
3. Carrega o esquema base
4. Executa todas as migrações de banco de dados pendentes

Monitore o progresso da inicialização em tempo real:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Aguarde até ver a saída indicando que o aplicativo está pronto. Você também pode monitorar o status de integridade do contêiner:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Etapa 4 — Acesse o aplicativo

Assim que ambos os contêineres mostrarem `Up (healthy)`, abra seu navegador:

```
http://<PROJECT_URL>:8080
```

Entre com a conta de administrador:

| Campo | Valor |
|-------|-------|
| Nome de usuário | `admin` |
| Senha | O valor que você definiu para `ADMIN_PASSWORD` no `.env` |

> Altere a senha do administrador imediatamente após o primeiro login nas configurações da conta.

---

## Etapa 5 — Verifique todos os serviços

Verifique se todos os contêineres estão em execução e saudáveis:

```bash
docker compose -f docker-compose.production.yml ps
```

Saída esperada:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Se um contêiner mostrar `Up (starting)` ou `Up (unhealthy)`, aguarde mais 30 a 60 segundos e verifique novamente. O MySQL pode levar até um minuto para inicializar completamente na primeira inicialização.

---

## Referência de portas

| Porta | Serviço | Descrição |
|-------|---------|-----------|
| `8080` | rtCloud App | Interface web principal (configurável via `APP_PORT`) |
| `3838` | Shiny Server | Análises e visualizações baseadas em R (configurável via `SHINY_PORT`) |

O MySQL (porta 3306) e quaisquer serviços opcionais (Keycloak) são somente internos e não são expostos ao host por padrão.

---

## Próximas etapas

Sua instância do rtCloud está em execução. Considere estas tarefas de acompanhamento:

- **Habilitar HTTPS** — Aponte um domínio para o seu servidor e configure SSL com Let's Encrypt. Consulte [Implantação em nuvem](cloud-deployment) para configuração automatizada de HTTPS.
- **Revisar todas as configurações** — Consulte a [Referência de configuração](configuration) para ajustar sua implantação para produção.
- **Configurar SSO** — Conecte um provedor de identidade para autenticação centralizada de usuários. Consulte [Autenticação SSO](sso-authentication).
- **Planejar seus backups** — Revise a página de [Manutenção](maintenance) para procedimentos de backup e atualização.
