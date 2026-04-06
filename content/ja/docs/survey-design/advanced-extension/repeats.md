---
title: "Advanced Repeats"
description: "繰り返しグループの高度なパターン：動的なカウント、ネストされた繰り返し、繰り返しデータのサマリー、繰り返しをまたいだ値の参照。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

このページでは、rtSurveyで繰り返しグループを扱うための高度なパターンをカバーします。繰り返しグループのセットアップの基本については、[グループ化と繰り返し](../repeats)を参照してください。

---

## 動的な繰り返しカウント

デフォルトでは、調査員が繰り返し回数を決定します。`repeat_count`を使用して繰り返しの回数を固定できます：

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | 世帯員 | `${num_members}` |
| text | member_name | 氏名 | |
| integer | member_age | 年齢 | |
| end_repeat | | | |

繰り返しはちょうど`${num_members}`回実行されます。`num_members`はフォームの前の部分で収集されます。調査員はインスタンスを追加または削除できません。

---

## インデックスアクセス：`indexed-repeat()`

**繰り返しグループの外**から特定の繰り返しインスタンスのフィールド値にアクセスするには、`indexed-repeat(repeatedField, repeatGroup, index)`を使用します：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

これはサマリーフィールドを構築したり、繰り返しの後に「主要な」メンバーのデータを参照したりするのに便利です。

---

## 現在のインスタンス位置：`index()`

繰り返しグループ内で、`index()`は現在のインスタンスの1ベースの位置を返します。各繰り返しにラベルを付けたり、一意の識別子を作成したりするために使用します：

| type | name | label |
|------|------|-------|
| begin_repeat | plots | 農地 |
| note | plot_label | 農地番号 ${index()} |
| text | plot_id | 農地ID |
| end_repeat | | |

---

## 同じインスタンス内のフィールドの参照

繰り返し内では、`${fieldname}`を使用して**同じ繰り返しインスタンス**内の別のフィールドを参照します。同じループ内では`indexed-repeat()`は不要です：

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | メンバー | |
| text | member_name | 氏名 | |
| integer | member_age | 年齢 | |
| text | school_name | 学校名 | `${member_age} < 18` |
| end_repeat | | | |

---

## 繰り返し内から親フィールドの参照

繰り返しグループの外（上）にあるフィールドは、通常の`${fieldname}`で参照できます：

| type | name | label |
|------|------|-------|
| text | village | 村の名前 |
| begin_repeat | plots | 農地 |
| note | plot_context | ${village}の農地 |
| end_repeat | | |

---

## 繰り返しデータのサマリー

繰り返しグループの**外**で繰り返し集計関数を使用してサマリーを作成します：

| 関数 | 例 | 説明 |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | インスタンスの数 |
| `sum(field)` | `sum(${loan_amount})` | 数値フィールドの合計 |
| `min(field)` | `min(${member_age})` | 最小値 |
| `max(field)` | `max(${member_age})` | 最大値 |
| `join(sep, field)` | `join(', ', ${member_name})` | カンマ区切りリスト |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | 条件付きカウント |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | 条件付き合計 |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | 条件付き結合 |

### 例：世帯サマリー

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | 何人のメンバーがいますか？ | |
| begin_repeat | members | メンバー | `${num_members}` |
| text | member_name | 氏名 | |
| integer | member_age | 年齢 | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members}人のメンバー；${children_count}人が18歳未満。大人：${adult_names} | |

---

## ネストされた繰り返し

繰り返しグループには別の繰り返しグループを含めることができます。これは慎重に使用してください — ネストされた繰り返しは複雑さを増し、調査員を混乱させる可能性があります。

| type | name | label |
|------|------|-------|
| begin_repeat | households | 世帯 |
| text | hh_id | 世帯ID |
| begin_repeat | hh_members | メンバー |
| text | member_name | 氏名 |
| end_repeat | | |
| end_repeat | | |

内側の繰り返しから外側の繰り返しのフィールドを参照するには、`${fieldname}`を使用します — 最も近い一致する先祖に解決されます：

`hh_members`繰り返し内では、`${hh_id}`はすべての世帯ではなく**現在の**世帯のIDを返します。

---

## 繰り返しグループ内のランク：`rank-index()`

`rank`フィールドが繰り返し内に存在する場合、外部から特定のインスタンスの順位ランクを取得するために`rank-index(instanceNumber, repeatedField)`を使用します：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})`は最高スコアのインスタンスインデックスを返します。

---

## ベストプラクティス

1. 繰り返し回数が事前にわかっている場合は常に`repeat_count`を使用してください — これにより調査員が誤ってインスタンスを追加または削除するのを防げます。
2. 繰り返しグループに集中してください — インスタンスごとに20以上の質問がある繰り返しはナビゲートが困難です。
3. 繰り返しグループに明確な名前を付けてください（例：`household_members`、`repeat1`ではなく）— 名前は関数呼び出しとエクスポートされたデータに表示されます。
4. 予想される最大インスタンス数でパフォーマンスを確認するためにテストしてください。
5. インスタンスごとに1つの画面にすべてのフィールドを表示するために繰り返しグループに`field-list`外観を使用してください（モバイル）。

---

## 制限事項

- `indexed-repeat()`は有効なインデックス（1からインスタンスのカウント）が必要です — 範囲外のインデックスは空を返します。
- 2レベルを超えるネストされた繰り返しは推奨されず、一部のクライアントで表示の問題を引き起こす可能性があります。
- 集計関数（`sum`、`count`など）は繰り返しグループ全体に対して機能します — `*-if`バリアントなしではインスタンスのサブセットを集計できません。
