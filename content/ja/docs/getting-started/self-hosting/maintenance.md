---
weight: 5
title: "メンテナンス"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "セルフホストrtCloudインスタンスの日常メンテナンス：アップグレード、バックアップ、復元、一般的な問題のトラブルシューティング。"
---

## 共通コマンド

rtCloudコンテナを管理するためにこれらのコマンドを定期的に使用してください。`docker-compose.production.yml`を含むディレクトリから実行します。

```bash
# すべてのコンテナのステータスと正常性を確認する
docker compose -f docker-compose.production.yml ps

# ライブログを表示する（すべてのサービス）
docker compose -f docker-compose.production.yml logs -f

# アプリのみのログを表示する
docker compose -f docker-compose.production.yml logs -f rtcloud

# 単一コンテナを再起動する
docker compose -f docker-compose.production.yml restart rtcloud

# すべてのサービスを停止する
docker compose -f docker-compose.production.yml down

# すべてのサービスを起動する
docker compose -f docker-compose.production.yml up -d

# アプリコンテナ内のシェルを開く
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## アップグレード

rtCloudのアップデートは新しいDockerイメージタグとして配布されます。アップグレードにより最新のイメージがプルされてアプリコンテナが再作成されます。データベースマイグレーションは起動時に自動的に実行されます。

**1. 最新のイメージをプルする：**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. アプリコンテナを再作成する：**

```bash
docker compose -f docker-compose.production.yml up -d
```

Dockerはイメージが変更されたコンテナのみを置き換えます。MySQLコンテナとすべての名前付きボリュームは影響を受けません。

### バージョンの固定

`latest`ではなく特定のバージョンにアップグレードするには、`.env`の`RTCLOUD_IMAGE`を更新する：

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

その後、上記のように`docker compose pull`と`up -d`を実行します。

### ダウングレード

データベースマイグレーションは元に戻せないため、ダウングレードは一般的に推奨されません。ダウングレードが必要な場合は、アップグレード前に取得したデータベースバックアップから復元してください。

---

## バックアップと復元

### データベースのバックアップ

このコマンドを実行してアプリケーションデータベースをSQLファイルにエクスポートします：

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

バックアップファイルはホストの現在のディレクトリに書き込まれます。

### データベースの復元

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### アップロードファイルのバックアップ

調査の送信には、名前付きDockerボリュームに保存されたアップロードファイル（写真、音声、ドキュメント）が含まれることが多いです。データベースとは別にバックアップしてください：

```bash
# アップロードのバックアップ
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# 音声録音のバックアップ
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

デフォルトを変更した場合は、`rtcloud_uploads`と`rtcloud_audios`を実際のボリューム名（`COMPOSE_PROJECT_NAME`でプレフィックス）に置き換えてください。

### アップロードファイルの復元

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### 自動日次バックアップ

ホストにcronジョブを追加してバックアップを自動的に実行します。`crontab -e`でrootのcrontabを編集する：

```cron
# 毎日午前2時にデータベースをバックアップし、30日分の履歴を保持する
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## トラブルシューティング

### アプリコンテナが起動しない

エラーメッセージのコンテナログを確認する：

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

一般的な原因：
- `.env`の環境変数が欠落しているか無効
- MySQLがまだ準備できていない（60秒待ってから再確認）
- ポートの競合 — 別のプロセスが既に`APP_PORT`を使用している

### MySQLが正常でない

```bash
docker compose -f docker-compose.production.yml logs mysql
```

一般的な原因：
- `.env`に`MYSQL_ROOT_PASSWORD`が設定されていない
- データボリュームの破損（まれ — `df -h`でディスクスペースを確認）

MySQLは初回起動時の初期化に30〜60秒かかる場合があります。失敗と判断する前に待って再確認してください。

### ポートが既に使用中

`.env`の`APP_PORT`または`SHINY_PORT`を空きポートに変更してからコンテナを再作成する：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

ホストでポートを使用しているものを見つけるには：

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

このエラーは、リクエストのオリジンが期待されるホストと一致しないローカルまたはリバースプロキシ環境で表示されます。ローカル開発のみCSRF検証を無効にする：

```dotenv
CSRF_VALIDATION_ENABLED=false
```

その後アプリを再起動する：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> 本番環境ではCSRF検証を無効にしないでください。本番環境でこのエラーが発生した場合は、リバースプロキシが正しい`Host`と`X-Forwarded-For`ヘッダーを転送していることを確認してください。

### 管理者パスワードを忘れた

データベースで直接管理者パスワードをリセットします。MySQLコンテナに接続してパスワードハッシュを更新する：

**ステップ1** — 新しいパスワードハッシュを生成する。`newpassword`を希望のパスワードに置き換える：

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**ステップ2** — データベースのハッシュを更新する：

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### コンテナが再起動し続ける

ヘルスチェックが失敗しているか確認する：

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

アプリのヘルスチェックは`/health`エンドポイントを呼び出します。繰り返し失敗する場合は、アプリケーションログで起動エラーを確認してください。

### ディスクスペースが満杯

スペースを消費しているものを特定する：

```bash
# ホストのディスク使用量を確認する
df -h

# Dockerのディスク使用量を確認する（イメージ、コンテナ、ボリューム）
docker system df

# 未使用のイメージと停止したコンテナを削除する（安全に実行可能）
docker system prune
```

`docker system prune --volumes`は使用しないでください — アプリケーションデータが削除されます。

---

## ヘルスチェック

各サービスには自動ヘルスチェックがあります。コンテナのステータスは結果を反映します：

| コンテナ | チェック方法 | 開始期間 | 間隔 |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90秒 | 30秒 |
| `rtcloud-mysql` | `mysqladmin ping` | 30秒 | 10秒 |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120秒 | 30秒 |

ヘルスチェックが失敗したコンテナは`RESTART_POLICY`設定（デフォルト：`unless-stopped`）に従って自動的に再起動されます。
