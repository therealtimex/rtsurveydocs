---
weight: 1
title: "クイックスタート"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Docker Composeを使って10分以内に独自サーバーでrtCloudを起動する。"
---

このガイドでは、LinuxサーバーにゼロからセルフホストのrtCloudインスタンスをデプロイする手順を説明します。完了すると、ブラウザからアクセス可能なrtCloudが稼働します。

## 前提条件

開始前に、サーバーが以下の要件を満たしていることを確認してください：

### ハードウェア

| リソース | 最小 | 推奨 |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| ディスク | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### ソフトウェア

| ソフトウェア | バージョン |
|----------|---------|
| OS | Ubuntu 20.04 LTS以降（またはDockerサポートのある任意のLinux） |
| Docker | 20.10以降 |
| Docker Compose | v2.x（`docker compose`）またはv1.x（`docker-compose`） |

**UbuntuへのDockerインストール：**

```bash
curl -fsSL https://get.docker.com | sh
```

インストールの確認：

```bash
docker --version
docker compose version
```

---

## ステップ1 — ファイルを入手する

サーバーにデプロイリポジトリをクローンする：

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## ステップ2 — 環境を設定する

サンプル設定ファイルをコピーする：

```bash
cp .env.production.sample .env
```

テキストエディターで`.env`を開き、必要な値を入力する：

```dotenv
# このデプロイの一意の識別子（スペースや特殊文字なし）
PROJECT_ID=myproject

# ユーザーがアプリにアクセスするドメインまたはIPアドレス
# 例: rtcloud.example.com または 192.168.1.100
PROJECT_URL=rtcloud.example.com

# プロトコル: SSL付きドメインがある場合は"https"、それ以外は"http"
HTTP_PROTOCOL=https

# 強力で一意のパスワード — 起動前にすべて変更すること
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **重要：** Docker Composeが自動的に読み込むのは`.env`のみです。`.env.production`という名前のファイルを作成しないでください。混乱の原因になります。`ADMIN_PASSWORD`は新しいデータベースの**初回起動時**にのみ適用されます。

---

## ステップ3 — コンテナを起動する

バックグラウンドですべてのサービスを起動する：

```bash
docker compose -f docker-compose.production.yml up -d
```

初回起動には**3〜5分**かかります：

1. rtCloudアプリケーションイメージをプル（約1 GBのダウンロード）
2. MySQLデータベースの初期化
3. ベーススキーマのロード
4. 保留中のすべてのデータベースマイグレーションの実行

リアルタイムで起動の進捗を監視する：

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

アプリケーションの準備完了を示す出力が表示されるまで待ちます。コンテナのヘルスステータスも確認できます：

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## ステップ4 — アプリケーションにアクセスする

両方のコンテナが`Up (healthy)`と表示されたら、ブラウザを開きます：

```
http://<PROJECT_URL>:8080
```

管理者アカウントでログインする：

| フィールド | 値 |
|-------|-------|
| ユーザー名 | `admin` |
| パスワード | `.env`の`ADMIN_PASSWORD`に設定した値 |

> 初回ログイン後すぐに、アカウント設定ページから管理者パスワードを変更してください。

---

## ステップ5 — すべてのサービスを確認する

すべてのコンテナが稼働して正常であることを確認する：

```bash
docker compose -f docker-compose.production.yml ps
```

期待される出力：

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

コンテナが`Up (starting)`または`Up (unhealthy)`と表示されている場合は、30〜60秒待ってから再確認してください。MySQLは初回起動時に完全に初期化するのに最大1分かかることがあります。

---

## ポートリファレンス

| ポート | サービス | 説明 |
|------|---------|-------------|
| `8080` | rtCloudアプリ | メインWeb UI（`APP_PORT`で設定可能） |
| `3838` | Shinyサーバー | 分析とRベースの可視化（`SHINY_PORT`で設定可能） |

MySQL（ポート3306）およびオプションサービス（Keycloak）はデフォルトでは内部専用であり、ホストには公開されません。

---

## 次のステップ

rtCloudインスタンスが稼働中になりました。以下のフォローアップタスクを検討してください：

- **HTTPSを有効にする** — ドメインをサーバーに向けてLet's EncryptでSSLを設定する。自動HTTPSセットアップについては[クラウドデプロイ](cloud-deployment)を参照してください。
- **すべての設定を確認する** — [設定リファレンス](configuration)を参照して本番環境向けにデプロイを調整する。
- **SSOを設定する** — 一元化されたユーザー認証のためにIDプロバイダーを接続する。[SSO認証](sso-authentication)を参照してください。
- **バックアップを計画する** — バックアップとアップグレード手順については[メンテナンス](maintenance)ページを参照してください。
