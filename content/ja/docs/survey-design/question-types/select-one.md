---
title: "Select_one"
description: "Select_one質問タイプは回答者が定義済みの選択肢リストから1つのオプションを選択できるようにします。"
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

`select_one`質問タイプは、回答者が定義済みのリストから**ちょうど1つのオプション**を選択するように促します。デフォルトではラジオボタンとして表示されますが、レイアウトと動作を変更するための豊富な外観オプションが利用できます。

## 基本XLSForm仕様

**surveyワークシート：**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | 回答者は同意しましたか？ |

**choicesワークシート：**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | はい |
| yesno | no | いいえ |

`select_one listname`の`listname`はchoicesワークシートの`list_name`列と一致しなければなりません。

詳細については[XLSForm仕様](https://xlsform.org/en/#question-types)を参照してください。

## 用途

Select_one質問は以下に使用されます：

1. はい/いいえの質問
2. 単一回答の選択肢（例：学歴、性別、婚姻状態）
3. カテゴリ評価（例：悪い / 普通 / 良い / 優秀）
4. 前の回答に基づいて選択肢がフィルタリングされるカスケード（リンク）選択
5. 国、地域、地区、その他の行政単位の選択

## 外観オプション

`appearance`列に値を指定して選択肢の表示方法を変更します：

{{< table >}}
| 外観 | 説明 |
|------------|-------------|
| *(なし)* | デフォルトのラジオボタン、1行に1つ |
| `minimal` | ラジオボタンの代わりに単一のドロップダウン/スピナー |
| `quick` | 選択後すぐに次の質問に自動進行（モバイルのみ） |
| `compact` | コンパクトな選択肢グリッド — 画面幅に応じて列数を調整 |
| `compact-N` | N列に強制されたコンパクトグリッド（例：`compact-3`） |
| `quickcompact` | `quick`と`compact`を組み合わせ |
| `quickcompact-N` | N列固定の`quick`と`compact`の組み合わせ |
| `horizontal` | 水平行に配置された選択肢（Web） |
| `horizontal-compact` | 水平、コンパクトスペーシング（Web） |
| `likert` | リッカートスケール行 — 上にラベル、下にラジオボタン |
| `label` | 入力なしで選択肢ラベルのみを表示（`list-nolabel`とペアで使用） |
| `list-nolabel` | ラベルなしで入力のみを表示（`label`とペアで使用） |
| `columns(N)` | N列で表示（rtSurvey拡張、例：`columns(3)`） |
| `distress` | Kessler心理的苦痛（K10）感情アイコンウィジェット |
| `search-api(...)` | ダイナミック検索 — 実行時にAPIから選択肢を読み込む |
| `tagging` | ラジオボタンの代わりにクリック可能なタグチップとして選択肢を表示する |
| `boxtag` | 選択肢をスタイル付きの長方形ボックスとして表示し、ユーザーがタップして選択する |
| `boxtag -search` | ボックスの上に検索/フィルター入力があるBoxtag レイアウト |
| `duolingo-style1` | Duolingo 風のカードレイアウト — アイコン付きの大きなタップ可能なカード |
| `rating_box` | グリッドベースの評価ボックス — 数値またはスケールの選択肢に最適 |
| `star_rating` | 星評価ウィジェット — 選択肢が1〜N個の星としてレンダリングされる |
| `choices-noshow` | 最初に最初の10個の選択肢のみ表示；残りはオンデマンドで表示 |
| `noshow` | 選択肢リストを完全に非表示にする；値はプログラムで設定される |
| `checkall` | リストの上部に「すべて選択」オプションを追加する |
| `max-items(N)` | 表示される選択肢の数をNに制限する（例：max-items(5)） |
{{< /table >}}

### 例：リッカートスケール

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | サービスにどれくらい満足していますか？ | likert |

### 例：コンパクト3列

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | 地域を選択してください | compact-3 |

## カスケード選択

カスケード（リンク）選択は、前の質問で選択された値に基づいて選択肢をフィルタリングします。`choice_filter`列にchoicesワークシートの列名を使用します。

**survey：**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | 県を選択してください | |
| select_one district | district | 地区を選択してください | province_name = ${province} |

**choices：**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

回答者が`nairobi`を選択すると、地区リストには`Westlands`と`Kasarani`のみが表示されます。

{{% alert icon=" " context="warning" %}}
`choice_filter`で使用される列名（例：`province_name`）はchoicesワークシートに存在しなければなりません。`${province}`は`province`という名前のsurveyフィールドを参照します。
{{% /alert %}}

## 式で選択された値を使用する

選択された**値**（ラベルではなく）を`${fieldname}`で参照します：

```
relevant: ${consent} = 'yes'
```

値の代わりに選択肢ラベルを取得するには、`choice-label()`を使用します：

```
calculate: choice-label(${education_level}, ${education_level})
```

## テキストフィールド付きの「その他」オプション

一般的なパターンは、テキストフィールドを表示する「その他」オプションを含めることです：

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | あなたの職業は何ですか？ | |
| text | job_other | 詳細を指定してください | `${job} = 'other'` |

**choices：**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | 農業 |
| occupation | trader | 商業 |
| occupation | student | 学生 |
| occupation | other | その他（詳細を指定してください） |

## ベストプラクティス

1. リストを短く相互に排他的に保ってください — 回答者が複数を選びたい場合は`select_multiple`を使用してください。
2. 最も一般的な回答を最初に置くか、長いリストではアルファベット順に並べてください。
3. 関連する場合は常に「わからない」または「回答しない」オプションを含めてください。
4. モバイルで画面スペースを節約するために、7〜8個以上の選択肢があるリストには`minimal`（ドロップダウン）を使用してください。
5. カスケード選択の場合は、フォームを構築する前にchoicesワークシートのすべてのフィルター列を追加してください。

## 制限事項

- 回答者は1つの選択肢しか選べません — 複数回答の質問には`select_multiple`を使用してください。
- `likert`外観は1行に収まる5〜7個の選択肢で最もよく機能します。
- `quick`自動進行はモバイルのみです；Webフォームには効果がありません。
