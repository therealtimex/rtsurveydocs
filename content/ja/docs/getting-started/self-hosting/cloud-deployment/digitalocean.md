---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "自動化されたユーザーデータスクリプトを使ってDigitalOcean Dropletにrtクラウドをデプロイする。"
---

DigitalOceanは初回起動時に自動的に実行される**ユーザーデータ**スクリプトを使用します。スクリプトの先頭にある設定変数を入力してから、Dropletを作成する際にスクリプト全体を貼り付けます。

> Linode StackScriptsとは異なり、DigitalOceanにはフォームUIがありません — 貼り付ける前にスクリプトを直接編集する必要があります。

**スクリプトのダウンロード：** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## 組み込みKeycloak（推奨）

組み込みSSOで最もシンプルなセットアップには`digitalocean-droplet-keycloak-embed.sh`を使用します。

### ステップ1 — 設定を入力する

スクリプトを開き、先頭の`CONFIGURATION`ブロックを編集する：

```bash
# --- 必須 ---
PROJECT_ID="rtsurvey"                  # プロジェクトの一意識別子（スペースなし）
ADMIN_PASSWORD="admin"                 # アプリ管理者とKeycloakのパスワード — 初回ログイン後変更すること

# --- ドメイン + SSL ---
DOMAIN="myapp.example.com"            # ドメイン — DNSのAレコードがここを指している必要がある
PROJECT_URL=""                         # Cloudflare/プロキシの後ろでない限り空白のまま
LETSENCRYPT_EMAIL="admin@example.com" # Let's Encrypt通知用メール

# --- オプション ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| フィールド | 必須 | 説明 |
|-------|----------|-------------|
| `PROJECT_ID` | はい | データベース名とKeycloakクライアントIDとして使用される。小文字、スペースなし。 |
| `ADMIN_PASSWORD` | いいえ | アプリ管理者ログインとKeycloak管理コンソールのパスワード。デフォルトは`admin` — **初回ログイン後すぐに変更すること**。 |
| `DOMAIN` | はい | ドメイン名。DNSのAレコードがDroplet IPを指している必要がある。 |
| `LETSENCRYPT_EMAIL` | はい | Let's Encrypt証明書通知用メールアドレス。 |
| `PROJECT_URL` | いいえ | 公開URLを上書きする。`DOMAIN`を使用する場合は空白のまま。Cloudflareの後ろで有用。 |

> **セキュリティ：** すべてのパスワードはデフォルトで`admin`です。初回ログイン後すぐに変更してください。

### ステップ2 — Dropletを作成する

[DigitalOceanコントロールパネル](https://cloud.digitalocean.com)で：

1. **作成** → **Droplets**をクリックする
2. イメージとして**Ubuntu 22.04 LTS**を選択する
3. **Basic、4 GB RAM / 2 vCPU**以上を選択する
4. **詳細オプション**にスクロールして**初期化スクリプトの追加**にチェックを入れる
5. テキストエリアにスクリプト全体の内容を貼り付ける
6. **Dropletを作成**をクリックする

### ステップ3 — DNSレコードを追加する

Dropletが起動している間に、DNSプロバイダーに**Aレコード**を追加する：

```
Type  : A
Name  : myapp          (またはルートドメインには@)
Value : <droplet-ip>
TTL   : 300
```

### ステップ4 — 進捗を監視する

DropletにSSH接続してログを確認する：

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

スクリプトは最初の方でサーバーIPを出力します — それが表示されたらすぐにDNSレコードを追加してください。

### ステップ5 — アプリにアクセスする

セットアップが完了すると、ログにサマリーが表示されます：

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

ブラウザで`https://myapp.example.com`を開き、ユーザー名`admin`、パスワード`admin`でログインします。

> 右上メニューの**設定**から、ログイン後すぐに**パスワードを変更**してください。

---

## デプロイ後

### パスワードを変更する

DropletにSSH接続し、`.env`を編集して影響を受けるコンテナを再起動する：

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### ドメインを更新する

デプロイ後に異なるドメインを割り当てる場合は、`.env`の`PROJECT_URL`を更新する：

```bash
nano /opt/rtcloud/.env   # PROJECT_URL= を更新する
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### すべてのコンテナを確認する

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
