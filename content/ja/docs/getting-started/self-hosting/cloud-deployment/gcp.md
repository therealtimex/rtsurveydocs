---
weight: 4
title: "Google Cloud（GCP）"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "gcp-compute.shスタートアップスクリプトを使ってGoogle Cloud Compute EngineにrtCloudをデプロイする。"
---

Compute Engine VMインスタンスを作成する際に`gcp-compute.sh`を**スタートアップスクリプト**として使用します。スクリプトは初回起動時に自動的に実行されます。

**スクリプトのダウンロード：** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## ステップ1 — 設定を入力する

スクリプトを開き、先頭の`CONFIGURATION`ブロックを編集する：

```bash
# --- 必須 ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # 初回ログイン後変更すること

# --- ドメイン + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- 組み込みKeycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ADMIN_PASSWORDにデフォルト設定
```

| フィールド | 必須 | 説明 |
|-------|----------|-------------|
| `PROJECT_ID` | はい | データベース名とKeycloakクライアントIDとして使用される。小文字、スペースなし。 |
| `ADMIN_PASSWORD` | いいえ | アプリ管理者パスワードとKeycloak管理者パスワード。デフォルトは`admin` — **初回ログイン後すぐに変更すること**。 |
| `DOMAIN` | いいえ | HTTPS用のドメイン。HTTPのみのモードには空白のまま。 |
| `LETSENCRYPT_EMAIL` | はい（DOMAINが設定されている場合） | Let's Encrypt通知用メール。 |
| `EMBED_KEYCLOAK` | いいえ | 組み込みKeycloakをデプロイするには`true`（4 GB RAMが必要）。 |

> **セキュリティ：** すべてのパスワードはデフォルトで`admin`です。初回ログイン後すぐに変更してください。

---

## ステップ2 — VMインスタンスを作成する

[Google Cloudコンソール](https://console.cloud.google.com/compute)で：

1. **インスタンスを作成**をクリックする
2. **マシン設定：**
   - シリーズ：`E2`
   - マシンタイプ：`e2-medium`（4 GB RAM）以上
3. **ブートディスク：**
   - オペレーティングシステム：Ubuntu
   - バージョン：Ubuntu 22.04 LTS
   - サイズ：40 GB以上
4. **ファイアウォール：** **HTTPトラフィックを許可**と**HTTPSトラフィックを許可**にチェックを入れる
5. **詳細オプション** → **管理** → **自動化** → **スタートアップスクリプト** → スクリプト全体の内容を貼り付ける
6. **作成**をクリックする

---

## ステップ3 — DNSレコードを追加する

VMが起動している間に、DNSプロバイダーに**Aレコード**を追加する：

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

コンソールのVMインスタンスリストで外部IPを確認できます。

---

## ステップ4 — 進捗を監視する

`gcloud` CLIを使用する：

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

または直接SSHする：

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## ステップ5 — アプリにアクセスする

セットアップが完了すると、ログにアプリのURLと認証情報のサマリーが表示されます。ユーザー名`admin`、パスワード`admin`でログインし、すぐにパスワードを変更してください。

---

## ファイアウォールルール

GCPの**HTTP/HTTPSを許可**チェックボックスでポート80と443が開きます。ポート3838でShinyへの直接アクセスも許可するには、ファイアウォールルールを追加する：

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

またはコンソールから追加する：**VPCネットワーク** → **ファイアウォール** → **ルールを作成**。

> ポート3306（MySQL）は**開かないでください** — 公開アクセスは絶対に禁止です。

---

## 静的IP（オプション）

デフォルトでは、GCPはVM再起動時に変わるエフェメラル外部IPを割り当てます。安定したIPを保持するには：

1. **VPCネットワーク** → **IPアドレス**に移動する
2. **外部静的アドレスを予約**をクリックする
3. VMインスタンスに割り当てる

---

## デプロイ後

### パスワードを変更する

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### すべてのコンテナを確認する

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
