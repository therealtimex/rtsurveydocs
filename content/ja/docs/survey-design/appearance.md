---
title: "外観"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurveyの`appearance`列は調査の質問の視覚的な表示と動作をカスタマイズできます。この機能はユーザーエクスペリエンスを向上させ、データ収集効率を大幅に改善できます。rtSurveyは標準的なXLSForm外観属性をサポートし、追加オプションで拡張しています。

## 標準XLSForm外観属性

rtSurveyは以下の標準XLSForm外観属性をサポートしています：

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| multiline | text | 複数行のテキストボックスを作成する（Webクライアントに最適） |
| minimal | select_one、select_multiple | ドロップダウンメニューに選択肢を表示する |
| quick | select_one | 選択後に次の質問に自動進む（モバイルのみ） |
| no-calendar | date | カレンダー表示を非表示にする（モバイルのみ） |
| month-year | date | 月と年のみの選択を許可する |
| year | date | 年のみの選択を許可する |
| horizontal-compact | select_one、select_multiple | 選択肢を水平に表示する（Webのみ） |
| horizontal | select_one、select_multiple | 選択肢を列で水平に表示する（Webのみ） |
| likert | select_one | 選択肢をリッカートスケールとして表示する |
| compact | select_one、select_multiple | 最小パディングで選択肢を並べて表示する |
| quickcompact | select_one | コンパクト表示と自動進行を組み合わせる（モバイルのみ） |
| field-list | groups | グループ全体を1画面に表示する（モバイルのみ） |
| label | select_one、select_multiple | 入力なしで選択肢のラベルを表示する |
| list-nolabel | select_one、select_multiple | ラベルなしで入力を表示する（`label`と一緒に使用） |
| table-list | groups | 質問をテーブル形式で表示する |
| signature | image | 署名キャプチャを有効にする（モバイルのみ） |
| draw | image | フリーハンド描画を許可する（モバイルのみ） |
| map、quick map | select_one、select_one_from_file | 地図からの選択を有効にする |

## 外観使用のベストプラクティス

1. **一貫性**：調査全体で外観属性を一貫して使用する。
2. **モバイルとWeb**：異なるデバイスとプラットフォームでの表示を考慮する。
3. **パフォーマンス**：フォームの読み込みを遅くする可能性のある外観属性（例：大きなグループの`table-list`）に注意する。
4. **ユーザーエクスペリエンス**：回答者のデータ入力をより簡単で直感的にする外観を選択する。
5. **テスト**：外観が期待通りに機能することを確認するために、ターゲットデバイスで常にフォームをテストする。

## 高度なテクニック

### 外観の組み合わせ

一部の外観属性はより複雑なレイアウトのために組み合わせることができます：

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | 1つ選択してください： | minimal compact |
```

### 動的外観

rtSurveyはフォームロジックに基づいた動的な外観変更を許可します：

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | 時間を入力してください： | inline-[%H:%M] | ${show_time} = 'yes' |
```

## モバイルアプリの考慮事項

- 一部の外観（例：`quick`、`signature`）はモバイルデバイス固有です。
- 一貫した動作を確認するためにAndroidとiOSの両方で徹底的にテストする。

## rtSurvey拡張外観属性

標準のXLSForm外観に加えて、rtSurveyは以下のプラットフォーム固有のオプションをサポートしています：

### データと表示の制御

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `invisible` | any | フィールドを非表示にしながらも値の収集または計算を続ける。`hidden`タイプとは異なり、フィールドはロジックに参加し続ける。 |
| `displaytitle` | any | 通常は抑制される場合でもフィールドのラベル/タイトルを強制的に表示する。 |
| `autopull` | select_one、select_multiple | フォームが読み込まれるかトリガーフィールドが変わるときに外部データを自動取得して選択肢を入力する。 |
| `floating_hint` | text、integer、decimal | ヒントテキストを入力フィールドの下ではなく上のフローティングラベルとして表示する。 |
| `calculate-button` | calculate | 自動計算ではなく、オンデマンドでフィールドの再計算をトリガーする可視ボタンを追加する。 |

### レイアウト

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `1screen` | group | グループサイズに関わらずグループ全体を1画面に強制表示する。 |
| `columns(n)` | select_one、select_multiple | 選択肢を`n`列で表示する。例：`columns(3)`は3列のラジオボタンを表示する。 |
| `gridformat<row=R col=C colspan=S align=center>` | any | CSSグリッドレイアウトで行`R`、列`C`、`S`列スパンにフィールドを配置する。`advanced-extension/grid-layout`と一緒に使用する。 |
| `ignore-simplify` | any | フォームレンダラーにこのフィールドのレイアウトの自動簡略化や縮小をスキップするよう指示する。 |
| `required-but-simplify` | any | フィールドは必須だがレイアウトは簡略化されたまま |
| `embed` | any | フィールドを埋め込み/インライン表示モードでレンダリングする |
| `popup` | select_one, select_multiple | 選択肢リストをポップアップ/モーダルオーバーレイでレンダリングする |
| `auto-hide-empty` | boxtag, select | 選択肢リストが空のときウィジェットを非表示にする |
| `text-nolabel` | select_one, select_multiple | 各選択肢のテキストラベルを非表示にする |

### ウィジェット

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `likert` | select_one | 選択肢をリッカートスケール行として表示する。 |
| `distress` | select_one | 感情的なアイコンを持つKessler心理的苦痛スケール（K10）ビジュアルウィジェットとして選択肢をレンダリングする。 |

### 選択ビジュアルウィジェット

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `tagging` | select_one、select_multiple | 選択肢をクリック可能なタグチップとして表示する |
| `boxtag` | select_one、select_multiple | 選択肢をスタイル付きの長方形ボックスとして表示する |
| `boxtag -search` | select_one、select_multiple | ボックスの上に検索/フィルター入力があるBoxtag レイアウト |
| `duolingo-style1` | select_one、select_multiple | 大型カードレイアウト — 短い選択肢リストに最適 |
| `rating_box` | select_one、select_multiple | グリッドベースの評価ボックス |
| `star_rating` | select_one | 星評価ウィジェット — 選択肢が1〜N個の星としてレンダリングされる |
| `choices-noshow` | select_one、select_multiple | 最初に最初の10個の選択肢のみ表示；残りはオンデマンドで |
| `noshow` | select_one、select_multiple | 選択肢リストを完全に非表示にする；値はプログラムで設定される |
| `checkall` | select_multiple | リストの上部に「すべて選択」オプションを追加する |
| `max-items(N)` | select_one、select_multiple | 表示される選択肢の数をNに制限する |

### テキストビジュアルウィジェット

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `richtext` | text | リッチテキストエディター — 太字、斜体、リスト、リンク付きのツールバー |
| `typingtest` | text | タイピングテストインターフェース — 文章を提示し、タイピング速度と正確さを測定する |

### メディア拡張

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | 撮影した写真にテキストの透かしを重ねる；式は撮影時に評価される |
| `editable` | image | 回答者が写真撮影後に画像に注釈を付けたり描画できるようにする |

### インライン表示の設定

`display{}` パラメーターはインライン表示動作を設定します：

| パラメーター | 説明 |
|------------|------|
| `display{title="ラベル"}` | インライン表示のカスタムタイトルを設定する |
| `display{icon="icon_name"}` | インライン表示のアイコンを設定する |
| `display{color="RRGGBB"}` | インライン表示のカスタムカラーを設定する |

`results{}` パラメーターは結果表示を設定します：

| パラメーター | 説明 |
|------------|------|
| `results{format="pattern"}` | 結果表示のフォーマットパターンを設定する |
| `results{show=true}` | 結果をインラインで表示する |

### API統合

| 外観属性 | 質問タイプ | 説明 |
|----------------------|----------------|-------------|
| `callapi` | text、integer、decimal、select_one | このフィールドのAPI呼び出し統合を有効にする。calculationカラムには`callapi()`式を含める必要がある。[Call API](advanced-extension/call-api)を参照。 |
| `callapi-verify(params)` | text、integer、decimal | 静的パラメーターを使ってAPI検証呼び出しをトリガーする。APIが値を確認するまでフォームの進行をブロックする。 |
| `callapi-verify(dynamicParams)` | text、integer、decimal | `callapi-verify`と同じだが、パラメーターは実行時に他のフィールド値から導出される。 |

### インライン日付/時間フォーマット

`date`、`time`、`datetime`フィールドでは、外観に追加されたフォーマット文字列を使ってカスタム表示フォーマットを指定できます：

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

フォーマットトークンは`format-date()`および`format-date-time()`と同じです。[関数 — 日付と時間関数](operators-and-functions/functions#date-and-time-functions)を参照してください。

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | イベントの日時 | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | 生年月日 | inline-[%d/%m/%Y] |

## 既知の制限

- 複雑な外観はすべてのプラットフォームで同一にレンダリングされないことがある。
- 一部の高度なrtSurvey外観はオフラインモードではサポートされない場合がある。

## 外観問題のトラブルシューティング

1. **外観が適用されない**：外観列のタイポを確認する。
2. **一貫性のないレンダリング**：質問タイプとプラットフォームとの互換性を確認する。
3. **パフォーマンスの問題**：複雑な外観を簡略化することを検討する（特に大規模な調査の場合）。
