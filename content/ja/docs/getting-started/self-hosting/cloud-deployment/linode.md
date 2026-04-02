---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "StackScript を使用して Linode に rtCloud をデプロイします。構成は必要ありません。サーバーを作成し、展開後の手順に従うだけです。"
---

## ステップ 1 — StackScript を起動する

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

これにより、Linode Cloud Manager で StackScript ページが開きます。 [**新しい Linode のデプロイ**] をクリックします。

---

## ステップ 2 — Linode のフォームに記入する

Linode の標準サーバー作成フォームに記入します。

|フィールド |推奨値 |
|------|------|
| **画像** | Ubuntu 22.04 LTS |
| **地域** |ユーザーに最も近い |
| **計画** |共有CPU 4GB以上 |
| **ルートパスワード** |強力なパスワードを設定する |
| **タイムゾーン** *(唯一のフィールド)* |サーバーのタイムゾーン (デフォルト: `Asia/Ho_Chi_Minh`) |

完了したら、[**Linode の作成**] をクリックします。

---

## ステップ 3 — セットアップが完了するまで待ちます

スクリプトは最初の起動時に自動的に実行されます。 Docker をインストールし、rtSurvey イメージを取得し、データベースを初期化し、すべてのサービスを開始します。これには **5 ～ 10 分**かかります。

**Linode Cloud Manager** で進行状況を直接確認できます。SSH は必要ありません。

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. 新しく作成した Linode をクリックします。
3. **LISH コンソールの起動** (Linode の詳細ページの右上) をクリックします。

ブラウザ ターミナルが開き、ライブ ブート ログが表示されます。[**Weblish**] タブはブラウザで直接動作し、SSH クライアントは必要ありません。

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

次の内容が表示されるまで待ちます。

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

ログにはサーバー IP も表示されます。これは次のステップで必要になります。

---

## ステップ 4 — SSL をセットアップする

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

**[SSL セットアップ ガイド →](../ssl-setup)** に従って HTTPS を設定します。無料の **rsurvey.com サブドメイン** が最も速いオプションであり、DNS セットアップは必要ありません。

---

## ステップ 5 — 最初のログイン

SSL が有効になったら、**[初回ログイン ガイド →](../first-login)** に従って管理者アカウントにアクセスします。

---

## ステップ 6 — デフォルトのパスワードを変更する

すべてのパスワードのデフォルトは「admin」です。最初のログイン後すぐに変更します。

- **アプリ管理者パスワード** — アプリ内のアカウント設定
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## ファイアウォール ルール (Linode クラウド ファイアウォール)

Linode Cloud ファイアウォールをこのサーバーに接続する場合は、次のルールを使用します。

### インバウンド

|ラベル |アクション |プロトコル |ポート |情報源 |メモ |
|----------|----------|----------|------|-----------|----------|
| `accept-inbound-ssh` |同意する | TCP | 22 |すべての IPv4、すべての IPv6 | SSHアクセス |
| `accept-inbound-http` |同意する | TCP | 80 |すべての IPv4、すべての IPv6 | Nginx (HTTP + ACME チャレンジ) |
| `accept-inbound-https` |同意する | TCP | 443 |すべての IPv4、すべての IPv6 | Nginx (SSL セットアップ後の HTTPS) |
| `accept-inbound-shiny` |同意する | TCP | 3838 |すべての IPv4、すべての IPv6 |シャイニーサーバー (R アナリティクス) |
| `accept-inbound-icmp` |同意する | ICMP | — |すべての IPv4、すべての IPv6 | Ping / 診断 |
|デフォルトの受信ポリシー | **ドロップ** | | | |それ以外はすべてブロック |

### アウトバウンド

|ラベル |アクション |メモ |
|------|--------|------|
|デフォルトの送信ポリシー | **同意します** |すべてのアウトバウンドを許可する (Docker プル、certbot、GoDaddy API など) |

### ポートは外部には必要ありません

これらのポートは「127.0.0.1」のみにバインドされており、サーバーの外部からは決して到達できません。

|ポート |サービス |理由 |
|------|--------|----------|
| 8080 |アプリコンテナ | Nginx は内部的にプロキシします。
| 8090 | Keycloakコンテナ | Nginx は内部的にプロキシします。
| 3306 | MySQL |内部 Docker ネットワークのみ |

---

## トラブルシューティング

### セットアップログを確認してください

```bash
tail -200 /var/log/stackscript.log
```

### SSL ログを確認する

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### コンテナのステータスを表示する

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
