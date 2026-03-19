---
weight: 2
title: "Referência de Configuração"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Referência completa para todas as variáveis de ambiente usadas para configurar uma implantação auto-alojada do rtCloud."
---

Toda a configuração é feita através de variáveis de ambiente no ficheiro `.env` na raiz do seu diretório de implantação. O Docker Compose lê este ficheiro automaticamente — não é necessário o sinalizador `--env-file`.

As variáveis marcadas como **obrigatórias** devem ser definidas antes de iniciar os contentores. Todas as outras têm valores predefinidos e são opcionais.

---

## Projeto

Estas variáveis definem a identidade e o ponto de acesso da sua instância rtCloud.

| Variável | Predefinição | Obrigatória | Descrição |
|----------|-------------|-------------|-----------|
| `PROJECT_ID` | — | **Sim** | Identificador único para esta implantação. Sem espaços ou caracteres especiais. Usado como prefixo para nomenclatura interna. |
| `PROJECT_URL` | — | **Sim** | Nome de domínio ou endereço IP onde os utilizadores acedem à aplicação (por ex., `rtcloud.example.com` ou `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Não | Variante de plataforma a ativar. Opções: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Não | Porta em que a aplicação escuta dentro do contentor. Não altere a menos que saiba o que está a fazer. |
| `HTTP_PROTOCOL` | `https` | Não | Protocolo usado para construir URLs internos. Defina como `http` se não estiver a usar SSL. |

---

## Base de Dados

Credenciais de ligação MySQL. A base de dados é gerida automaticamente pelo contentor MySQL — só precisa de definir palavras-passe fortes.

| Variável | Predefinição | Obrigatória | Descrição |
|----------|-------------|-------------|-----------|
| `MYSQL_DATABASE` | `smartsurvey` | Não | Nome da base de dados da aplicação. |
| `MYSQL_USER` | `smartsurvey` | Não | Utilizador MySQL para a aplicação. |
| `MYSQL_PASSWORD` | — | **Sim** | Palavra-passe para `MYSQL_USER`. Use um valor forte e único. |
| `MYSQL_ROOT_PASSWORD` | — | **Sim** | Palavra-passe root do MySQL. Necessária para inicialização da base de dados e operações de administração. |
| `MYSQL_HOST` | `mysql` | Não | Nome do host MySQL. Use o valor predefinido a menos que esteja a ligar a uma base de dados externa. |
| `MYSQL_PORT` | `3306` | Não | Porta MySQL. |

---

## Conta de Administrador

A conta de administrador é criada automaticamente na primeira inicialização de uma base de dados nova.

| Variável | Predefinição | Obrigatória | Descrição |
|----------|-------------|-------------|-----------|
| `ADMIN_PASSWORD` | `admin` | **Sim** | Palavra-passe para o utilizador `admin` incorporado. Defina isto antes da primeira inicialização. Não tem efeito se a base de dados já existir. |

> Após o primeiro início de sessão, altere a palavra-passe do administrador na página **Configurações de Conta** na UI web.

---

## Portas

Controle quais portas do host a aplicação vincula.

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `APP_PORT` | `8080` | Porta do host para a UI web principal. Altere isto se a porta 8080 já estiver em uso no seu servidor. |
| `SHINY_PORT` | `3838` | Porta do host para o servidor de análise Shiny. |

---

## Runtime

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `RUN_ENV` | `prod` | Ambiente de runtime. Use `prod` para implantações de produção, `dev` para desenvolvimento local. |
| `RUN_MODE` | `admin` | Função do contentor. `admin` executa a pilha completa (web + fila + cron). `worker` executa apenas processamento em segundo plano (para escalamento horizontal). |
| `TZ` | `Asia/Ho_Chi_Minh` | Fuso horário do servidor. Afeta timestamps de log, agendamentos cron e exibição de datas. Use um [nome de fuso horário TZ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ex., `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Verbosidade do log da aplicação. Opções: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefixo aplicado a todos os nomes de contentores e volumes Docker. Altere isto ao executar múltiplas instâncias rtCloud no mesmo host. |
| `RESTART_POLICY` | `unless-stopped` | Comportamento de reinício do contentor Docker. Opções: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Imagem Docker a usar. Altere a tag para fixar uma versão específica. |
| `REQUIRE_LICENSE` | `false` | Ativar validação de chave de licença na inicialização. Contacte a RTA para informações de licença. |

---

## Segurança

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `CSRF_VALIDATION_ENABLED` | `true` | Ativar validação de token CSRF. Mantenha isto `true` em produção. Defina como `false` apenas em desenvolvimento local se encontrar erros `400 CSRF token could not be verified`. |
| `GII_ENABLED` | `false` | Ativar a ferramenta geradora de código do framework Yii. **Nunca ative em produção.** |

---

## SSO — Keycloak Incorporado

Ative o contentor Keycloak incorporado para SSO empresarial completo. Requer um domínio com HTTPS.

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `EMBED_KEYCLOAK` | `false` | Defina como `true` para iniciar o contentor Keycloak incorporado. Ativa o perfil Docker Compose `embed-keycloak`. |
| `KEYCLOAK_URL` | — | URL completo do servidor Keycloak (por ex., `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Nome do realm Keycloak (por ex., `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | ID de cliente Keycloak para a aplicação rtCloud. |
| `KEYCLOAK_CLIENT_SECRET` | — | Segredo de cliente Keycloak. Gere isto a partir da consola de administração Keycloak. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Nome de utilizador administrador do Keycloak. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Palavra-passe do administrador Keycloak. |
| `KEYCLOAK_DB` | `keycloak` | Nome da base de dados para o Keycloak. Criado automaticamente na primeira inicialização. |
| `KEYCLOAK_DB_USER` | `keycloak` | Utilizador da base de dados para o Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Palavra-passe da base de dados para o utilizador Keycloak. |
| `KC_HOSTNAME` | — | URL frontend do Keycloak (por ex., `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Impor correspondência estrita de nome de host. Defina como `true` em produção com um domínio fixo. |

Consulte [Autenticação SSO](sso-authentication#embedded-keycloak) para o guia de configuração completo.

---

## SSO — Fornecedor OIDC Externo

Ligue a um fornecedor de identidade compatível com OIDC existente (Supabase, Auth0, Authentik, Okta, etc.).

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `OIDC_ISSUER_URL` | — | URL de descoberta do emissor OIDC (por ex., `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | ID de cliente registado no seu fornecedor de identidade. |
| `OIDC_CLIENT_SECRET` | — | Segredo de cliente do seu fornecedor de identidade. |
| `OIDC_SCOPE` | `openid profile email` | Lista separada por espaços de scopes OIDC a solicitar. |
| `OIDC_REDIRECT_URI` | — | URL de callback para a aplicação web (por ex., `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | ID de cliente separado para a aplicação móvel rtSurvey. |
| `OIDC_MOBILE_REDIRECT_URI` | — | URI de callback para a aplicação móvel (por ex., `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Criar automaticamente contas rtCloud para utilizadores que se autentiquem via OIDC pela primeira vez. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Substituir o URL do endpoint de autorização (deixe em branco para usar descoberta). |
| `OIDC_TOKEN_ENDPOINT` | — | Substituir o URL do endpoint de token (deixe em branco para usar descoberta). |
| `OIDC_USERINFO_ENDPOINT` | — | Substituir o URL do endpoint de informação do utilizador (deixe em branco para usar descoberta). |

---

## SSO — Azure Active Directory

| Variável | Descrição |
|----------|-----------|
| `AZURE_CLIENT_ID` | ID da aplicação Azure AD (cliente). |
| `AZURE_TENANT_ID` | ID do diretório Azure AD (inquilino). |

---

## Integrações Opcionais

### Stata

| Variável | Predefinição | Descrição |
|----------|-------------|-----------|
| `STATA_ENABLED` | `false` | Ativar integração do software estatístico Stata para análise de dados. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Caminho absoluto para o binário Stata dentro do contentor. |

### Elasticsearch

| Variável | Descrição |
|----------|-----------|
| `ES_HOST` | Host Elasticsearch (por ex., `http://elasticsearch:9200`). |
| `ES_PORT` | Porta Elasticsearch. |

### Matomo Analytics

| Variável | Descrição |
|----------|-----------|
| `PIWIK_URL` | URL do servidor Matomo (Piwik). |
| `PIWIK_ID` | ID do site Matomo. |
| `PIWIK_SECRET` | Token de autenticação Matomo. |

### OpenCPU (Computação R)

| Variável | Descrição |
|----------|-----------|
| `OCPU_HOST` | URL do servidor OpenCPU para computação estatística baseada em R. |

### Integração RtBox

| Variável | Descrição |
|----------|-----------|
| `RTBOX_HOST` | URL do host do serviço RtBox. |
| `RTBOX_USER_API` | Chave API de utilizador RtBox. |
| `RTBOX_BASIC_AUTH` | Credenciais de autenticação básica para RtBox. |

### Mensagens Matrix

| Variável | Descrição |
|----------|-----------|
| `MATRIX_HOMESERVER_HOST` | Host do servidor Matrix. |
| `MATRIX_HOMESERVER_PORT` | Porta do servidor Matrix. |

---

## Volumes de Dados

Todos os dados da aplicação são armazenados em volumes Docker nomeados. Os volumes são criados automaticamente na primeira inicialização e persistem entre reinícios e atualizações de contentores.

| Volume | Ponto de Montagem | Conteúdo |
|--------|-------------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | Ficheiros da base de dados MySQL |
| `rtcloud_uploads` | `…/uploads` | Ficheiros carregados pelos respondentes do inquérito |
| `rtcloud_audios` | `…/audios` | Gravações de áudio |
| `rtcloud_downloads` | `…/downloads` | Ficheiros de exportação gerados |
| `rtcloud_gallery` | `…/gallery` | Imagens de galeria |
| `rtcloud_voicemail` | `…/voicemail` | Gravações de correio de voz |
| `rtcloud_analytics` | `…/analytics` | Dados de análise |
| `rtcloud_aggregate` | `…/aggregate` | Resultados agregados do inquérito |
| `rtcloud_converter` | `…/converter` | Saídas de conversão de dados |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Scripts R do servidor Shiny |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Logs do servidor Shiny |
| `rtcloud_assets` | `…/assets` | Ativos web (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Cache de runtime da aplicação |
| `rtcloud_cache` | `…/cache` | Cache da aplicação |
| `rtcloud_tmp` | `…/tmp` | Ficheiros temporários |

Os nomes dos volumes têm como prefixo o valor de `COMPOSE_PROJECT_NAME` (predefinição: `rtcloud`).

Liste todos os volumes para a sua implantação:

```bash
docker volume ls | grep rtcloud
```
