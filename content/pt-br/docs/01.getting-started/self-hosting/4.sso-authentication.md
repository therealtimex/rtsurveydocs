---
weight: 4
title: "Autenticação SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configure o Single Sign-On para o rtCloud com hospedagem própria usando o Keycloak integrado, um provedor OIDC externo ou o Azure Active Directory."
---

O rtCloud suporta três abordagens para Single Sign-On (SSO):

| Opção | Melhor para |
|-------|-------------|
| [Keycloak integrado](#embedded-keycloak) | Organizações que desejam um servidor SSO totalmente autossuficiente integrado ao rtCloud |
| [Provedor OIDC externo](#external-oidc-provider) | Organizações que já executam um provedor de identidade (Auth0, Authentik, Okta, Supabase, etc.) |
| [Azure Active Directory](#azure-active-directory) | Organizações que usam o Microsoft 365 ou Azure AD |

Sem SSO configurado, os usuários entram com contas locais do rtCloud gerenciadas pelo painel de administração.

---

## Keycloak integrado {#embedded-keycloak}

A implantação inclui um contêiner Keycloak opcional que é executado junto com o rtCloud. O Keycloak é pré-configurado com um realm rtSurvey e está pronto para usar.

### Requisitos

- Um nome de domínio com HTTPS (o Keycloak requer HTTPS em produção)
- Pelo menos 4 GB de RAM no servidor (o Keycloak adiciona ~512 MB de uso de memória)

### Configuração

**1. Configure as variáveis de ambiente no `.env`:**

```dotenv
# Habilitar o contêiner Keycloak integrado
EMBED_KEYCLOAK=true

# URLs do Keycloak — use seu domínio real
KEYCLOAK_URL=https://rtcloud.exemplo.com.br/auth
KC_HOSTNAME=https://rtcloud.exemplo.com.br/auth
KC_HOSTNAME_STRICT=false

# Configurações de realm e cliente (correspondem ao JSON do realm importado)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=seu-segredo-do-cliente-aqui

# Credenciais do administrador do Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=minha_senha_admin_keycloak

# Banco de dados do Keycloak (criado automaticamente)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=minha_senha_keycloak_db

# Porta em que o Keycloak escuta (lado do host, proxy pelo Nginx)
KEYCLOAK_PORT=8091
```

**2. Inicie com o perfil do Keycloak integrado:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verifique se o Keycloak está saudável:**

```bash
docker compose -f docker-compose.production.yml ps
```

O contêiner `rtcloud-keycloak` deve mostrar `Up (healthy)` após 2 a 3 minutos.

**4. Acesse o console de administração do Keycloak:**

```
https://rtcloud.exemplo.com.br/auth/admin
```

Entre com `KEYCLOAK_ADMIN_USER` e `KEYCLOAK_ADMIN_PASSWORD`.

### O que está pré-configurado

O Keycloak integrado inicia com um realm `rtsurvey` pré-importado que inclui:

- Configuração de cliente para o aplicativo web
- Funções de usuário padrão (`admin`, `project_manager`, `enumerator`, `analyst`)
- Configurações de sessão e token otimizadas para o rtSurvey

Você pode adicionar usuários diretamente no console de administração do Keycloak ou conectar o Keycloak a um provedor de identidade upstream (LDAP, SAML).

### Roteamento do Nginx

Ao usar os scripts de implantação em nuvem, o Nginx é configurado para fazer proxy de ambos os serviços:

| Caminho | Backend |
|---------|---------|
| `/` | Aplicativo rtCloud em `127.0.0.1:8080` |
| `/auth/` | Keycloak em `127.0.0.1:8090` |

---

## Provedor OIDC externo {#external-oidc-provider}

Conecte o rtCloud a qualquer provedor de identidade compatível com OpenID Connect. Esta abordagem não requer o contêiner Keycloak.

### Provedores suportados

Qualquer provedor compatível com OIDC funciona, incluindo:
- Authentik
- Auth0
- Okta
- Keycloak (instância externa)
- Supabase
- Google (para organizações do Google Workspace)
- GitHub (por meio de aplicativos OAuth com extensão OIDC)

### Configuração

**1. Registre o rtCloud como cliente OIDC no seu provedor de identidade.**

Você precisará de:
- Um **ID de cliente** e um **segredo de cliente**
- Registrar o **URI de redirecionamento**: `https://rtcloud.exemplo.com.br/auth/callback`
- Para suporte ao aplicativo móvel, registre também: `vn.rta.rtsurvey.auth://callback`

**2. Configure as variáveis de ambiente no `.env`:**

```dotenv
# URL de descoberta OIDC (específica do provedor — consulte a documentação do seu IdP)
OIDC_ISSUER_URL=https://seu-provedor-de-identidade.com

# Credenciais do cliente do seu provedor de identidade
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=seu-segredo-do-cliente-aqui

# Escopos para solicitar (openid, profile e email geralmente são suficientes)
OIDC_SCOPE=openid profile email

# URI de redirecionamento registrado no seu provedor de identidade
OIDC_REDIRECT_URI=https://rtcloud.exemplo.com.br/auth/callback

# Opcional: cliente separado para o aplicativo móvel
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Defina como true para criar automaticamente contas rtCloud para novos usuários OIDC
OPEN_REGISTRATION=false
```

**3. Reinicie o contêiner do aplicativo para aplicar as alterações:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Provisionamento automático de usuários

Quando `OPEN_REGISTRATION=true`, o rtCloud cria automaticamente uma conta local na primeira vez que um usuário entra via OIDC. A conta é preenchida com o nome e e-mail do usuário a partir do token de ID.

Quando `OPEN_REGISTRATION=false` (padrão), um administrador do rtCloud deve criar a conta do usuário primeiro, e a identidade OIDC é vinculada no primeiro login.

### Endpoints personalizados

Se o seu provedor não suportar descoberta OIDC (`.well-known/openid-configuration`), você pode definir endpoints manualmente:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://seu-provedor.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://seu-provedor.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://seu-provedor.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Integre o rtCloud com o tenant do Microsoft Azure AD da sua organização.

### Configuração

**1. Registre um novo aplicativo no [Portal do Azure](https://portal.azure.com):**

   - Vá para **Azure Active Directory** → **Registros de aplicativos** → **Novo registro**
   - Nome: `rtCloud`
   - URI de redirecionamento: `https://rtcloud.exemplo.com.br/auth/callback` (tipo Web)
   - Após a criação, anote o **ID do aplicativo (cliente)** e o **ID do diretório (tenant)**
   - Em **Certificados e segredos**, crie um novo segredo de cliente

**2. Configure as variáveis de ambiente no `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Reinicie o contêiner do aplicativo:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Os usuários no seu tenant do Azure AD agora podem entrar no rtCloud usando suas credenciais Microsoft.

---

## Desabilitando o SSO

Para reverter para autenticação local, remova ou comente todas as variáveis relacionadas ao SSO no `.env`, depois reinicie o contêiner do aplicativo:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Se você estava usando o Keycloak integrado, pare-o omitindo o sinalizador `--profile embed-keycloak` e executando `docker compose down` seguido de `up -d` sem o perfil.
