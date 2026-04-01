---
weight: 4
title: "SSO 驗證"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "使用嵌入式 Keycloak、外部 OIDC 提供者或 Azure Active Directory 為自行託管的 rtCloud 設定單一登入。"
---

rtCloud 支援三種單一登入（SSO）方式：

| 選項 | 最適合 |
|--------|----------|
| [嵌入式 Keycloak](#embedded-keycloak) | 希望完全自包含的 SSO 伺服器與 rtCloud 捆綁的組織 |
| [外部 OIDC 提供者](#external-oidc-provider) | 已有身份提供者（Auth0、Authentik、Okta、Supabase 等）的組織 |
| [Azure Active Directory](#azure-active-directory) | 使用 Microsoft 365 或 Azure AD 的組織 |

未設定 SSO 時，使用者使用透過管理面板管理的本地 rtCloud 帳號登入。

---

## 嵌入式 Keycloak

部署包含一個可選的 Keycloak 容器，與 rtCloud 並行執行。Keycloak 預先設定了一個 rtSurvey realm，隨時可以使用。

### 需求

- 帶有 HTTPS 的域名（Keycloak 在生產環境中需要 HTTPS）
- 伺服器至少 4 GB RAM（Keycloak 增加約 512 MB 記憶體使用量）

### 設定

**1. 在 `.env` 中設定環境變數：**

```dotenv
# Enable the embedded Keycloak container
EMBED_KEYCLOAK=true

# Keycloak URLs — use your actual domain
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm and client settings (match the imported realm JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak admin credentials
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak database (created automatically)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port Keycloak listens on (host-side, proxied by Nginx)
KEYCLOAK_PORT=8091
```

**2. 使用嵌入式 Keycloak 設定檔啟動：**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. 驗證 Keycloak 是否健康：**

```bash
docker compose -f docker-compose.production.yml ps
```

`rtcloud-keycloak` 容器應在 2–3 分鐘後顯示 `Up (healthy)`。

**4. 存取 Keycloak 管理控制台：**

```
https://rtcloud.example.com/auth/admin
```

使用 `KEYCLOAK_ADMIN_USER` 和 `KEYCLOAK_ADMIN_PASSWORD` 登入。

### 預先設定的內容

嵌入式 Keycloak 以預先匯入的 `rtsurvey` realm 啟動，包括：

- 網頁應用程式的客戶端設定
- 預設使用者角色（`admin`、`project_manager`、`enumerator`、`analyst`）
- 為 rtSurvey 最佳化的會話和令牌設定

您可以直接在 Keycloak 管理控制台中新增使用者，或將 Keycloak 連接至上游身份提供者（LDAP、SAML）。

### Nginx 路由

使用雲端部署腳本時，Nginx 被設定為代理兩個服務：

| 路徑 | 後端 |
|------|---------|
| `/` | rtCloud 應用程式，位於 `127.0.0.1:8080` |
| `/auth/` | Keycloak，位於 `127.0.0.1:8090` |

---

## 外部 OIDC 提供者

將 rtCloud 連接至任何 OpenID Connect 相容的身份提供者。此方法不需要 Keycloak 容器。

### 支援的提供者

任何符合 OIDC 規範的提供者都可以使用，包括：
- Authentik
- Auth0
- Okta
- Keycloak（外部實例）
- Supabase
- Google（適用於 Google Workspace 組織）
- GitHub（透過帶有 OIDC 擴展的 OAuth 應用程式）

### 設定

**1. 在您的身份提供者中將 rtCloud 註冊為 OIDC 客戶端。**

您需要：
- 一個**客戶端 ID** 和**客戶端密鑰**
- 註冊**重定向 URI**：`https://rtcloud.example.com/auth/callback`
- 對於行動應用程式支援，還需要註冊：`vn.rta.rtsurvey.auth://callback`

**2. 在 `.env` 中設定環境變數：**

```dotenv
# OIDC discovery URL (provider-specific — check your IdP documentation)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Client credentials from your identity provider
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Scopes to request (openid, profile, and email are typically sufficient)
OIDC_SCOPE=openid profile email

# Redirect URI registered in your identity provider
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Optional: separate mobile app client
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Set to true to auto-create rtCloud accounts for new OIDC users
OPEN_REGISTRATION=false
```

**3. 重啟應用程式容器以套用更改：**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### 自動佈建使用者

當 `OPEN_REGISTRATION=true` 時，rtCloud 在使用者首次透過 OIDC 登入時自動建立本地帳號。帳號使用 ID 令牌中的使用者姓名和電子郵件填充。

當 `OPEN_REGISTRATION=false`（預設）時，rtCloud 管理員必須先建立使用者帳號，OIDC 身份在首次登入時連結。

### 自訂端點

如果您的提供者不支援 OIDC 探索（`.well-known/openid-configuration`），您可以手動設定端點：

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

將 rtCloud 與您組織的 Microsoft Azure AD 租戶整合。

### 設定

**1. 在 [Azure Portal](https://portal.azure.com) 中註冊新應用程式：**

   - 前往 **Azure Active Directory** → **應用程式註冊** → **新增註冊**
   - 名稱：`rtCloud`
   - 重定向 URI：`https://rtcloud.example.com/auth/callback`（Web 類型）
   - 建立後，記下**應用程式（客戶端）ID** 和**目錄（租戶）ID**
   - 在**憑證和密鑰**下，建立新的客戶端密鑰

**2. 在 `.env` 中設定環境變數：**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. 重啟應用程式容器：**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

您的 Azure AD 租戶中的使用者現在可以使用他們的 Microsoft 憑證登入 rtCloud。

---

## 停用 SSO

若要恢復本地驗證，請從 `.env` 中刪除或註解掉所有 SSO 相關變數，然後重啟應用程式容器：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

如果您使用的是嵌入式 Keycloak，請在不帶 `--profile embed-keycloak` 標記的情況下執行 `docker compose down`，然後在不帶設定檔的情況下執行 `up -d` 來停止它。
