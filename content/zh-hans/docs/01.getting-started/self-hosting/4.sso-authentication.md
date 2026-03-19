---
weight: 4
title: "SSO 认证"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "使用内嵌 Keycloak、外部 OIDC 提供商或 Azure Active Directory 为自托管 rtCloud 配置单点登录。"
---

rtCloud 支持三种单点登录（SSO）方式：

| 选项 | 最适合 |
|--------|----------|
| [内嵌 Keycloak](#embedded-keycloak) | 希望将完全自包含的 SSO 服务器与 rtCloud 捆绑的组织 |
| [外部 OIDC 提供商](#external-oidc-provider) | 已在运行身份提供商（Auth0、Authentik、Okta、Supabase 等）的组织 |
| [Azure Active Directory](#azure-active-directory) | 使用 Microsoft 365 或 Azure AD 的组织 |

未配置 SSO 时，用户通过管理面板管理的本地 rtCloud 账户登录。

---

## 内嵌 Keycloak {#embedded-keycloak}

部署包含一个与 rtCloud 并行运行的可选 Keycloak 容器。Keycloak 已预配置了 rtSurvey realm，可直接使用。

### 要求

- 具有 HTTPS 的域名（Keycloak 在生产环境中需要 HTTPS）
- 服务器上至少 4 GB RAM（Keycloak 额外消耗约 512 MB 内存）

### 设置

**1. 在 `.env` 中配置环境变量：**

```dotenv
# 启用内嵌 Keycloak 容器
EMBED_KEYCLOAK=true

# Keycloak URL——使用您的实际域名
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm 和客户端设置（与导入的 realm JSON 匹配）
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak 管理员凭据
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak 数据库（自动创建）
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Keycloak 监听的端口（主机侧，由 Nginx 代理）
KEYCLOAK_PORT=8091
```

**2. 使用内嵌 Keycloak 配置文件启动：**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. 验证 Keycloak 是否健康：**

```bash
docker compose -f docker-compose.production.yml ps
```

`rtcloud-keycloak` 容器应在 2–3 分钟后显示 `Up (healthy)`。

**4. 访问 Keycloak 管理控制台：**

```
https://rtcloud.example.com/auth/admin
```

使用 `KEYCLOAK_ADMIN_USER` 和 `KEYCLOAK_ADMIN_PASSWORD` 登录。

### 预配置内容

内嵌 Keycloak 启动时带有预导入的 `rtsurvey` realm，包含：

- 网页应用的客户端配置
- 默认用户角色（`admin`、`project_manager`、`enumerator`、`analyst`）
- 针对 rtSurvey 优化的会话和令牌设置

您可以直接在 Keycloak 管理控制台中添加用户，或将 Keycloak 连接到上游身份提供商（LDAP、SAML）。

### Nginx 路由

使用云端部署脚本时，Nginx 配置为代理两个服务：

| 路径 | 后端 |
|------|---------|
| `/` | `127.0.0.1:8080` 上的 rtCloud 应用 |
| `/auth/` | `127.0.0.1:8090` 上的 Keycloak |

---

## 外部 OIDC 提供商 {#external-oidc-provider}

将 rtCloud 连接到任何 OpenID Connect 兼容的身份提供商。此方式不需要 Keycloak 容器。

### 支持的提供商

任何符合 OIDC 标准的提供商均可工作，包括：
- Authentik
- Auth0
- Okta
- Keycloak（外部实例）
- Supabase
- Google（适用于 Google Workspace 组织）
- GitHub（通过带 OIDC 扩展的 OAuth 应用）

### 设置

**1. 在您的身份提供商中将 rtCloud 注册为 OIDC 客户端。**

您需要：
- **客户端 ID** 和**客户端密钥**
- 注册**重定向 URI**：`https://rtcloud.example.com/auth/callback`
- 如需移动应用支持，还需注册：`vn.rta.rtsurvey.auth://callback`

**2. 在 `.env` 中配置环境变量：**

```dotenv
# OIDC 发现 URL（特定于提供商——请查阅您的 IdP 文档）
OIDC_ISSUER_URL=https://your-identity-provider.com

# 来自您的身份提供商的客户端凭据
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# 要请求的范围（openid、profile 和 email 通常足够）
OIDC_SCOPE=openid profile email

# 在您的身份提供商中注册的重定向 URI
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# 可选：独立的移动应用客户端
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# 设置为 true 以自动为新 OIDC 用户创建 rtCloud 账户
OPEN_REGISTRATION=false
```

**3. 重启应用容器以应用更改：**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### 自动配置用户

当 `OPEN_REGISTRATION=true` 时，rtCloud 会在用户首次通过 OIDC 登录时自动创建本地账户。账户使用 ID 令牌中的用户姓名和邮箱填充。

当 `OPEN_REGISTRATION=false`（默认值）时，rtCloud 管理员必须先创建用户账户，OIDC 身份在首次登录时关联。

### 自定义端点

如果您的提供商不支持 OIDC 发现（`.well-known/openid-configuration`），您可以手动设置端点：

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

将 rtCloud 与您组织的 Microsoft Azure AD 租户集成。

### 设置

**1. 在 [Azure 门户](https://portal.azure.com)中注册新应用：**

   - 转到 **Azure Active Directory** → **应用注册** → **新注册**
   - 名称：`rtCloud`
   - 重定向 URI：`https://rtcloud.example.com/auth/callback`（Web 类型）
   - 创建后，记下**应用程序（客户端）ID** 和**目录（租户）ID**
   - 在**证书和密钥**下，创建新的客户端密钥

**2. 在 `.env` 中配置环境变量：**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. 重启应用容器：**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

您 Azure AD 租户中的用户现在可以使用其 Microsoft 凭据登录 rtCloud。

---

## 禁用 SSO

要恢复到本地身份验证，请从 `.env` 中删除或注释掉所有 SSO 相关变量，然后重启应用容器：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

如果您使用的是内嵌 Keycloak，请通过省略 `--profile embed-keycloak` 标志来停止它，先运行 `docker compose down`，然后在没有配置文件的情况下运行 `up -d`。
