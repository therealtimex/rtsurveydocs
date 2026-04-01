---
weight: 2
title: "部署"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "使用 Docker 部署和管理您自己的 rtCloud 實例。完全掌控您的資料、基礎架構和設定。"
---

使用 Docker Compose 在您自己的基礎架構上執行 rtCloud。自行託管讓您完全擁有資料、網路和部署環境——非常適合有資料主權要求、隔離網路或自訂基礎架構需求的組織。

## 什麼是 rtCloud 自行託管？

rtCloud 自行託管是一個官方 Docker 映像，將整個 rtCloud 平台打包成可在任何 Linux 伺服器上執行的可攜式容器堆疊。該堆疊包括：

| 服務 | 說明 |
|---------|-------------|
| **rtCloud 應用程式** | Apache 2.4 + PHP 7.4 網頁應用程式，內建背景佇列（Beanstalkd）、分析伺服器（Shiny）和排程任務 |
| **MySQL 8.0** | 用於所有應用程式和問卷調查資料的關聯式資料庫 |
| **Keycloak** *(選用)* | 用於企業身份管理的嵌入式單一登入伺服器 |

## 何時選擇自行託管

當您有以下需求時，自行託管是正確的選擇：

- 需要**資料主權**——所有資料都保存在您自己的基礎架構內
- 在**隔離或受限網路**中操作，無法存取外部雲端
- 有**合規要求**（GDPR、HIPAA、政府資料政策）要求本地儲存
- 需要與**內部身份提供者**（Active Directory、LDAP、SAML）整合
- 想要**自訂資源**——按自己的條件分配 CPU、RAM 和儲存空間

## 本節內容

| 頁面 | 說明 |
|------|-------------|
| [快速入門](quick-start) | 在 10 分鐘內在伺服器上啟動 rtCloud |
| [設定參考](configuration) | 所有環境變數及其預設值的完整清單 |
| [雲端部署](cloud-deployment) | DigitalOcean、AWS、GCP 和 Linode 的一鍵自動化腳本 |
| [SSO 驗證](sso-authentication) | 設定 Keycloak、外部 OIDC 或 Azure AD |
| [維護](maintenance) | 升級、備份、還原和疑難排解您的實例 |

## 架構概覽

部署作為一組連接在內部網路上的 Docker 容器執行：

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4 application                   │
│  Beanstalkd queue (internal)           │
│  Shiny Server (port 3838)              │
│  Cron scheduler                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal only)  │
└────────────────────────────────────────┘
```

啟用 SSO 時，第三個容器會並行執行：

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

所有容器透過隔離的 Docker 橋接網路進行通訊。只有網頁應用程式連接埠和（可選的）Shiny 分析連接埠會暴露給主機。
