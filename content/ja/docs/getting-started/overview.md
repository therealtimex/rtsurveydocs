---
weight: 1
date: "2024-07-01T12:00:00+01:00"
draft: false
author: "RealTimeX"
title: "概要"
icon: "rocket_launch"
toc: true
description: "rtSurveyで調査を実施するためのクイックスタートガイド"
publishdate: "2024-07-01T12:00:00+01:00"
tags: ["Beginners"]
---

rtSurveyはデータを効率的に収集するためのフォームとワークフローを構築する強力なプラットフォームです。rtSurveyでできることは以下の通りです：

1. 写真、GPS位置情報、スキップロジック、計算、外部データセット、複数言語などを組み込んだ高度なフォームを作成する。
2. モバイルアプリまたはWebインターフェースを使用してデータを収集し、インターネット接続が利用可能になると自動的に同期する。
3. CSVやStataへのエクスポート、またはrtSurveyをExcel、Power BI、Python、Rに接続してダイナミックなリアルタイム更新ダッシュボードを作成することで、データを簡単に分析できる。

研究者、フィールドチーム、さまざまな業界の専門家がrtSurveyを重要なデータ収集ニーズに活用しています。始め方は以下の通りです：

## 1. rtSurvey Cloudにアクセスする {#getting-started-get-rtCloud}

最も速く始める方法は、公式マネージドホスティングサービスである[rtSurvey Cloud](https://rtsurvey.com/#rtsurvey-cloud)を使用することです。rtSurveyのウェブサイトからアクセスでき、堅牢で安全なインフラ上に構築されています。または、ご希望であれば独自インフラでrtSurveyをホストすることもできます。

## 2. 調査フォームを作成する {#getting-started-create-form}

1. `XLSForm`を使ってフォームを設計するか、[All Widgetsフォーム](https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0)テンプレートを試してみてください。
2. XLSFormをrtSurvey Cloudにアップロードして公開するか、フォームビルダー（Beta）でビジュアルデザインを体験する。

## 3. rtSurveyアプリをインストールする {#getting-started-get-collect}

モバイルデバイスにrtSurveyアプリをダウンロードする：

### Androidデバイスの場合：
1. [Google Playストア](https://play.google.com/store/apps/details?id=vn.rta.rtsurvey)にアクセスする。
2. 「rtSurvey」を検索してrtSurveyのロゴが付いたアプリをタップする。
3. 「インストール」をクリックしてアプリをダウンロードしてセットアップする。

### iOSデバイスの場合：
1. デバイスで[App Store](https://apps.apple.com/vn/app/rtsurvey/id1178851547)を開く。
2. 「rtSurvey」を検索してrtSurveyのロゴが付いたアプリを探す。
3. 「入手」をタップしてアプリをダウンロードしてインストールする。

## 4. rtSurveyアプリをrtSurvey Cloudに接続する {#getting-started-connect}

1. アカウントを作成する：
   - rtSurvey CloudのAdminが調査員用のアカウントを作成できる。
   - または、Adminが調査員が自分でアカウントを作成するためのURLを生成することもできる。
2. rtSurveyアプリを開き、アカウントの認証情報でログインする。

## 5. 調査を実施する {#getting-started-fill-form}

1. アプリで「空白フォームに入力」を選択して新しい調査を開始する。
2. 回答者のデータを入力してフォームを完成させる。
3. 完了すると、インターネット接続が利用可能になったときに、フォームデータが自動的にrtSurvey Cloudと同期する。

## 6. rtSurvey Cloudでデータを分析する {#getting-started-use-data}

1. rtSurvey Cloudにログインして収集したデータにアクセスする。
2. データをCSVやStataなど様々な形式でダウンロードしてさらなる分析を行う。
3. 組み込みの分析ツールを活用するか、お好みのデータ分析ソフトウェアと連携する。
