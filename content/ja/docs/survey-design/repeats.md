---
title: "質問の繰り返し"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

繰り返しはrtSurveyの強力な機能で、1回の調査内で同じ情報セットを複数回収集できます。これは、複数の世帯員のデータを収集する必要がある世帯調査などのシナリオに特に有用です。

## 基本的な繰り返し構造

rtSurveyで繰り返しを作成するには、`begin repeat`と`end repeat`の構造を使用します：

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | 子供の名前         |
| decimal      | birthweight  | 子供の出生体重  |
| select_one male_female | sex | 子供の性別         |
| end repeat   |              |                      |
```

この例では、ユーザーはフォームに新しい繰り返しを追加することで複数の子供に関する情報を収集できます。

## 繰り返しのラベル付け

`begin repeat`の`label`列はオプションですが、ラベルを追加することでナビゲーションが改善されます：

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | 子供の情報    |
| text         | name         | 子供の名前         |
| decimal      | birthweight  | 子供の出生体重  |
| select_one male_female | sex | 子供の性別         |
| end repeat   |              |                      |
```

rtSurveyは各繰り返しインスタンスのタイトルとして「子供の情報」を表示します。

## 固定繰り返し回数

固定の繰り返し回数を指定するには、`repeat_count`列を使用します：

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | 子供の情報    | 3            |
| text         | name         | 子供の名前         |              |
| decimal      | birthweight  | 子供の出生体重  |              |
| end repeat   |              |                      |              |
```

これにより正確に3つの子供繰り返しが作成されます。

## 動的繰り返し回数

rtSurveyは以前の回答に基づく動的繰り返し回数をサポートします：

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | 世帯人数は？   |                    |
| begin repeat | hh_member  | 世帯員               | ${num_hh_members}  |
| text     | name           | 名前                           |                    |
| integer  | age            | 年齢                            |                    |
| end repeat |              |                                |                    |
```

## 条件付き繰り返し

`relevant`列を使って繰り返しを条件付きで表示することができます：

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | 子供はここに住んでいますか？|                     |
| begin repeat      | child_repeat| 子供の情報         | ${has_child} = 'yes'|
| text              | name        | 子供の名前              |                     |
| decimal           | birthweight | 子供の出生体重       |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey固有の機能

### 繰り返しサマリー

rtSurveyは繰り返しのサマリービューを提供します。サマリーをカスタマイズするには、繰り返し内にグループを使用します：

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | 名                               |
| text         | last_name    | 姓                                |
| integer      | age          | 年齢                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### 繰り返しの外観オプション

rtSurveyは繰り返しの追加外観オプションを提供します：

- `appearance: field-list` - 繰り返しのすべての質問を1画面に表示する
- `appearance: table-list` - 繰り返しを表形式で表示する

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | 子供の情報 | table-list  |
| text         | name         | 名前              |             |
| integer      | age          | 年齢               |             |
| end repeat   |              |                   |             |
```

### ネストされた繰り返し

rtSurveyは複雑なデータ構造のためのネストされた繰り返しをサポートします：

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | 世帯            |
| text         | hh_name        | 世帯名       |
| begin repeat | hh_member      | 世帯員     |
| text         | member_name    | メンバー名          |
| integer      | member_age     | メンバーの年齢           |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## rtSurveyでの繰り返し使用のベストプラクティス

1. データ分析を向上させるために繰り返しに意味のある名前とラベルを使用する。
2. データ入力エラーを減らすために動的繰り返し回数の使用を検討する。
3. 複雑なネストされた繰り返しを使用する場合は特に、フォームを徹底的にテストする。
4. 調査員が長い繰り返しリストをナビゲートするのを助けるためにサマリー機能を使用する。
5. フォームのパフォーマンスに影響する可能性があるため、大量の繰り返しには注意する。

## ゼロ繰り返しの処理

rtSurveyでゼロ繰り返しを表現するには：

1. 必要でない場合は最初の繰り返しを削除するよう調査員をトレーニングする。
2. 正確な数がわかっている場合は動的繰り返し回数を使用する。
3. 繰り返しを条件付きで表示するために`relevant`を使用する。

## データエクスポートの考慮事項

rtSurveyからデータをエクスポートする場合、繰り返しデータは通常フラット化されます。各繰り返しインスタンスはエクスポートされたデータの別の行になり、親フォームのデータが各インスタンスに対して繰り返されます。

## モバイルアプリの考慮事項

- rtSurveyモバイルアプリの繰り返しはオフラインデータ収集をサポートする。
- 大量の繰り返しは低スペックのデバイスでアプリのパフォーマンスに影響する場合がある。

rtSurveyで繰り返しを効果的に使用することで、ユーザーフレンドリーなインターフェースを維持しながら複雑な階層的データ構造を取得できる、柔軟で強力な調査を作成できます。
