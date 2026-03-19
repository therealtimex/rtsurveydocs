---
weight: 2
title: "Referência de configuração"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Referência completa de todas as variáveis de ambiente usadas para configurar uma implantação do rtCloud com hospedagem própria."
---

Toda a configuração é feita por meio de variáveis de ambiente no arquivo `.env` na raiz do seu diretório de implantação. O Docker Compose lê este arquivo automaticamente — não é necessário o sinalizador `--env-file`.

Variáveis marcadas como **obrigatórias** devem ser definidas antes de iniciar os contêineres. Todas as outras têm padrões e são opcionais.

---

## Projeto

Essas variáveis definem a identidade e o ponto de acesso da sua instância do rtCloud.

| Variável | Padrão | Obrigatória | Descrição |
|----------|--------|-------------|-----------|
| `PROJECT_ID` | — | **Sim** | Identificador único para esta implantação. Sem espaços ou caracteres especiais. Usado como prefixo para nomenclatura interna. |
| `PROJECT_URL` | — | **Sim** | Nome de domínio ou endereço IP onde os usuários acessam o aplicativo (por exemplo, `rtcloud.exemplo.com.br` ou `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Não | Variante da plataforma a ativar. Opções: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Não | Porta em que o aplicativo escuta dentro do contêiner. Não altere a menos que saiba o que está fazendo. |
| `HTTP_PROTOCOL` | `https` | Não | Protocolo usado para construir URLs internas. Defina como `http` se não estiver usando SSL. |

---

## Banco de dados

Credenciais de conexão do MySQL. O banco de dados é gerenciado automaticamente pelo contêiner MySQL — você só precisa definir senhas fortes.

| Variável | Padrão | Obrigatória | Descrição |
|----------|--------|-------------|-----------|
| `MYSQL_DATABASE` | `smartsurvey` | Não | Nome do banco de dados do aplicativo. |
| `MYSQL_USER` | `smartsurvey` | Não | Usuário MySQL para o aplicativo. |
| `MYSQL_PASSWORD` | — | **Sim** | Senha para `MYSQL_USER`. Use um valor forte e único. |
| `MYSQL_ROOT_PASSWORD` | — | **Sim** | Senha root do MySQL. Necessária para inicialização e operações administrativas do banco de dados. |
| `MYSQL_HOST` | `mysql` | Não | Nome do host MySQL. Use o padrão a menos que esteja conectando a um banco de dados externo. |
| `MYSQL_PORT` | `3306` | Não | Porta do MySQL. |

---

## Conta de administrador

A conta de administrador é criada automaticamente na primeira inicialização de um banco de dados novo.

| Variável | Padrão | Obrigatória | Descrição |
|----------|--------|-------------|-----------|
| `ADMIN_PASSWORD` | `admin` | **Sim** | Senha para o usuário `admin` integrado. Defina antes da primeira inicialização. Não tem efeito se o banco de dados já existir. |

> Após o primeiro login, altere a senha do administrador na página **Configurações da conta** na interface web.

---

## Portas

Controle quais portas do host o aplicativo vincula.

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `APP_PORT` | `8080` | Porta do host para a interface web principal. Altere se a porta 8080 já estiver em uso no seu servidor. |
| `SHINY_PORT` | `3838` | Porta do host para o servidor de análise Shiny. |

---

## Tempo de execução

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `RUN_ENV` | `prod` | Ambiente de execução. Use `prod` para implantações de produção, `dev` para desenvolvimento local. |
| `RUN_MODE` | `admin` | Função do contêiner. `admin` executa a pilha completa (web + fila + cron). `worker` executa apenas o processamento em segundo plano (para escalonamento horizontal). |
| `TZ` | `Asia/Ho_Chi_Minh` | Fuso horário do servidor. Afeta registros de data/hora dos logs, agendamentos cron e exibição de datas. Use um [nome de fuso horário do banco de dados TZ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, `UTC`, `America/Sao_Paulo`, `Europe/Lisbon`). |
| `LOG_LEVEL` | `info` | Verbosidade do log do aplicativo. Opções: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefixo aplicado a todos os nomes de contêineres e volumes Docker. Altere ao executar várias instâncias do rtCloud no mesmo host. |
| `RESTART_POLICY` | `unless-stopped` | Comportamento de reinicialização do contêiner Docker. Opções: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Imagem Docker a ser usada. Altere a tag para fixar uma versão específica. |
| `REQUIRE_LICENSE` | `false` | Habilitar validação de chave de licença na inicialização. Entre em contato com a RTA para informações sobre licença. |

---

## Segurança

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `CSRF_VALIDATION_ENABLED` | `true` | Habilitar validação de token CSRF. Mantenha como `true` em produção. Defina como `false` apenas em desenvolvimento local se encontrar erros `400 CSRF token could not be verified`. |
| `GII_ENABLED` | `false` | Habilitar a ferramenta geradora de código do framework Yii. **Nunca habilite em produção.** |

---

## SSO — Keycloak integrado

Habilite o contêiner Keycloak integrado para SSO empresarial completo. Requer um domínio com HTTPS.

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `EMBED_KEYCLOAK` | `false` | Defina como `true` para iniciar o contêiner Keycloak integrado. Ativa o perfil `embed-keycloak` do Docker Compose. |
| `KEYCLOAK_URL` | — | URL completa do servidor Keycloak (por exemplo, `https://rtcloud.exemplo.com.br/auth`). |
| `KEYCLOAK_REALM` | — | Nome do realm do Keycloak (por exemplo, `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | ID do cliente Keycloak para o aplicativo rtCloud. |
| `KEYCLOAK_CLIENT_SECRET` | — | Segredo do cliente Keycloak. Gere-o no console de administração do Keycloak. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Nome de usuário do administrador do Keycloak. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Senha do administrador do Keycloak. |
| `KEYCLOAK_DB` | `keycloak` | Nome do banco de dados para o Keycloak. Criado automaticamente na primeira inicialização. |
| `KEYCLOAK_DB_USER` | `keycloak` | Usuário do banco de dados para o Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Senha do banco de dados para o usuário Keycloak. |
| `KC_HOSTNAME` | — | URL de frontend do Keycloak (por exemplo, `https://rtcloud.exemplo.com.br/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Aplicar correspondência estrita de nome de host. Defina como `true` em produção com um domínio fixo. |

Consulte [Autenticação SSO](sso-authentication#embedded-keycloak) para o guia completo de configuração.

---

## SSO — Provedor OIDC externo

Conecte-se a um provedor de identidade compatível com OIDC existente (Supabase, Auth0, Authentik, Okta, etc.).

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `OIDC_ISSUER_URL` | — | URL de descoberta do emissor OIDC (por exemplo, `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | ID do cliente registrado no seu provedor de identidade. |
| `OIDC_CLIENT_SECRET` | — | Segredo do cliente do seu provedor de identidade. |
| `OIDC_SCOPE` | `openid profile email` | Lista de escopos OIDC separados por espaço para solicitar. |
| `OIDC_REDIRECT_URI` | — | URL de retorno de chamada para o aplicativo web (por exemplo, `https://rtcloud.exemplo.com.br/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | ID de cliente separado para o aplicativo móvel rtSurvey. |
| `OIDC_MOBILE_REDIRECT_URI` | — | URI de retorno de chamada do aplicativo móvel (por exemplo, `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Criar automaticamente contas rtCloud para usuários que se autenticam via OIDC pela primeira vez. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Substituir a URL do endpoint de autorização (deixe em branco para usar a descoberta). |
| `OIDC_TOKEN_ENDPOINT` | — | Substituir a URL do endpoint de token (deixe em branco para usar a descoberta). |
| `OIDC_USERINFO_ENDPOINT` | — | Substituir a URL do endpoint de informações do usuário (deixe em branco para usar a descoberta). |

---

## SSO — Azure Active Directory

| Variável | Descrição |
|----------|-----------|
| `AZURE_CLIENT_ID` | ID do aplicativo (cliente) do Azure AD. |
| `AZURE_TENANT_ID` | ID do diretório (tenant) do Azure AD. |

---

## Integrações opcionais

### Stata

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `STATA_ENABLED` | `false` | Habilitar integração com o software estatístico Stata para análise de dados. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Caminho absoluto para o binário do Stata dentro do contêiner. |

### Elasticsearch

| Variável | Descrição |
|----------|-----------|
| `ES_HOST` | Host do Elasticsearch (por exemplo, `http://elasticsearch:9200`). |
| `ES_PORT` | Porta do Elasticsearch. |

### Matomo Analytics

| Variável | Descrição |
|----------|-----------|
| `PIWIK_URL` | URL do servidor Matomo (Piwik). |
| `PIWIK_ID` | ID do site do Matomo. |
| `PIWIK_SECRET` | Token de autenticação do Matomo. |

### OpenCPU (Computação R)

| Variável | Descrição |
|----------|-----------|
| `OCPU_HOST` | URL do servidor OpenCPU para computação estatística baseada em R. |

### Integração RtBox

| Variável | Descrição |
|----------|-----------|
| `RTBOX_HOST` | URL do host do serviço RtBox. |
| `RTBOX_USER_API` | Chave API do usuário RtBox. |
| `RTBOX_BASIC_AUTH` | Credenciais de autenticação básica para o RtBox. |

### Mensagens Matrix

| Variável | Descrição |
|----------|-----------|
| `MATRIX_HOMESERVER_HOST` | Host do servidor Matrix. |
| `MATRIX_HOMESERVER_PORT` | Porta do servidor Matrix. |

---

## Volumes de dados

Todos os dados do aplicativo são armazenados em volumes Docker nomeados. Os volumes são criados automaticamente na primeira inicialização e persistem entre reinicializações e atualizações de contêineres.

| Volume | Ponto de montagem | Conteúdo |
|--------|-------------------|---------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | Arquivos do banco de dados MySQL |
| `rtcloud_uploads` | `…/uploads` | Arquivos enviados por respondentes da pesquisa |
| `rtcloud_audios` | `…/audios` | Gravações de áudio |
| `rtcloud_downloads` | `…/downloads` | Arquivos de exportação gerados |
| `rtcloud_gallery` | `…/gallery` | Imagens da galeria |
| `rtcloud_voicemail` | `…/voicemail` | Gravações de correio de voz |
| `rtcloud_analytics` | `…/analytics` | Dados de análise |
| `rtcloud_aggregate` | `…/aggregate` | Resultados agregados da pesquisa |
| `rtcloud_converter` | `…/converter` | Saídas de conversão de dados |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Scripts R do servidor Shiny |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Logs do servidor Shiny |
| `rtcloud_assets` | `…/assets` | Ativos web (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Cache de tempo de execução do aplicativo |
| `rtcloud_cache` | `…/cache` | Cache do aplicativo |
| `rtcloud_tmp` | `…/tmp` | Arquivos temporários |

Os nomes dos volumes são prefixados pelo valor de `COMPOSE_PROJECT_NAME` (padrão: `rtcloud`).

Liste todos os volumes da sua implantação:

```bash
docker volume ls | grep rtcloud
```
