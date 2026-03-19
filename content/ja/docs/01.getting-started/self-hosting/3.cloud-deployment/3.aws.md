---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "aws-ec2.shユーザーデータスクリプトを使ってAWS EC2インスタンスにrtCloudをデプロイする。"
---

EC2インスタンスを起動する際に`aws-ec2.sh`を**ユーザーデータ**スクリプトとして使用します。スクリプトは初回起動時に自動的に実行されます。

**スクリプトのダウンロード：** [aws-ec2.sh](/scripts/aws-ec2.sh)

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

## ステップ2 — EC2インスタンスを起動する

[AWS EC2コンソール](https://console.aws.amazon.com/ec2)で：

1. **インスタンスを起動**をクリックする
2. **AMI：** Ubuntu Server 22.04 LTS（64-bit x86）
3. **インスタンスタイプ：** `t3.medium`（4 GB RAM）以上
4. **キーペア：** SSHアクセス用のものを選択または作成する
5. **ネットワーク設定：** セキュリティグループを作成または選択する（下記参照）
6. **詳細** → **ユーザーデータ** → スクリプト全体の内容を貼り付ける
7. **インスタンスを起動**をクリックする

---

## ステップ3 — セキュリティグループを設定する

インスタンスのセキュリティグループで以下のポートを開く：

| ポート | プロトコル | 送信元 | 目的 |
|------|----------|--------|---------|
| 22 | TCP | 自分のIP | SSHアクセス |
| 80 | TCP | 0.0.0.0/0 | HTTP（NginxによりHTTPSにリダイレクト） |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Shiny直接アクセス |

> ポート3306（MySQL）は**開かないでください** — 公開アクセスは絶対に禁止です。

---

## ステップ4 — DNSレコードを追加する

インスタンスが起動している間に、DNSプロバイダーに**Aレコード**を追加する：

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## ステップ5 — 進捗を監視する

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## ステップ6 — アプリにアクセスする

セットアップが完了すると、ログにアプリのURLと認証情報のサマリーが表示されます。ユーザー名`admin`、パスワード`admin`でログインし、すぐにパスワードを変更してください。

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

### Elastic IPを割り当てる（オプション）

インスタンスを停止・起動すると、パブリックIPが変わります。安定したIPを保持するには、EC2コンソールで**Elastic IP**を割り当ててインスタンスに関連付けてください。
