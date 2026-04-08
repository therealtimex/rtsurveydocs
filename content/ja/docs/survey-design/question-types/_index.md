---
title: "質問タイプ"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurveyはすべての標準XLSForm質問タイプに加え、独自の拡張機能をサポートしています。各質問タイプは収集するデータの種類とデバイス上での入力ウィジェットの表示方法を制御します。

質問タイプを設定するには、XLSFormの**survey**ワークシートの`type`列にタイプ名を入力します。

## テキスト入力

| タイプ | 説明 |
|------|-------------|
| [text](text) | 自由テキスト回答 — あらゆる文字を入力可能 |
| [integer](integer) | 整数（小数なし） |
| [decimal](decimal) | 小数点を含む数値 |
| [range](range) | 定義された最小値/最大値の範囲内でスライダーから選択した数値 |

## 選択

| タイプ | 説明 |
|------|-------------|
| [select_one listname](select-one) | リストから1つのオプションだけを選択 |
| [select_multiple listname](select-multiple) | リストから1つ以上のオプションを選択 |
| [rank listname](rank) | 好みや優先度に従って選択肢を並べ替え |

## 日付と時刻

| タイプ | 説明 |
|------|-------------|
| [date](date) | 暦日（年、月、日） |
| [time](time) | 時刻（時、分） |
| [datetime](datetime-date-time) | 日付と時刻の組み合わせ |

## 位置情報

| タイプ | 説明 |
|------|-------------|
| [geopoint](geopoint) | 単一GPS座標（緯度、経度、高度、精度） |
| [geotrace](geotrace) | パス — 線を形成するGPS点の系列 |
| [geoshape](geoshape) | エリア — GPS点の閉じたポリゴン |

## メディア

| タイプ | 説明 |
|------|-------------|
| [image](image) | 写真撮影または画像アップロード |
| [audio](audio) | 音声録音 |
| [video](video) | 動画録画 |
| [file](file) | 一般的なファイルアップロード（PDF、ドキュメントなど） |

## その他

| タイプ | 説明 |
|------|-------------|
| [barcode](barcode) | バーコードまたはQRコードをスキャン |
| [note](note) | 読み取り専用の表示テキスト — 指示や計算されたサマリーを表示 |
| [calculate](calculate) | 計算された値を格納する非表示フィールド |
| [hidden](hidden) | 静的または事前入力された値を格納する非表示フィールド |
| [trigger / acknowledge](trigger) | 調査員が声明を読んだことを確認するためにチェックしなければならないチェックボックス |
| [meta](meta) | 自動メタデータ：タイムスタンプ、デバイスID、調査員情報 |

## rtSurvey 拡張

これらのタイプは rtSurvey 固有のものであり、標準の XLSForm 仕様には含まれていません。

| タイプ | 説明 |
|--------|------|
| [search-autocomplete](search-autocomplete) | リアルタイム API による自動補完候補付きテキスト入力 |
| [mentions](mentions) | エンティティをインラインでタグ付けするための `@` メンション自動補完付きテキストフィールド |
| [texttags](texttags) | タグ入力 — 各エントリが削除可能なチップになる；スペース区切りの文字列として保存 |

繰り返しグループについては [Repeats](../advanced-extension/repeats) を参照

## タイプと外観の連携

`type`は**収集するデータ**を決定します。`appearance`列は**ウィジェットの外観**を制御します。多くのタイプが複数の外観をサポートしています。たとえば`select_one`はラジオボタン、ドロップダウン、リッカートスケール、コンパクトグリッドとして表示できます。

全オプションについては[外観](../appearance)を参照してください。
