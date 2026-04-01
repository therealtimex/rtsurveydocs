---
title: "進階重複"
description: "重複群組的進階模式：動態計數、嵌套重複、匯總重複資料和跨重複引用值。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

此頁面涵蓋在 rtSurvey 中使用重複群組的進階模式。有關設定重複群組的基礎知識，請參閱[群組和重複](../repeats)。

---

## 動態重複計數

預設情況下，調查員決定重複多少次。您可以使用 `repeat_count` 固定重複次數：

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | 家庭成員 | `${num_members}` |
| text | member_name | 成員姓名 | |
| integer | member_age | 年齡 | |
| end_repeat | | | |

重複恰好運行 `${num_members}` 次，其中 `num_members` 在表單的較早位置收集。調查員無法添加或刪除實例。

---

## 索引存取：`indexed-repeat()`

使用 `indexed-repeat(repeatedField, repeatGroup, index)` 從重複群組**外部**存取特定重複實例的字段值：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

這對於在重複後構建摘要字段或引用「主要」成員資料非常有用。

---

## 當前實例位置：`index()`

在重複群組內，`index()` 返回當前實例的從 1 開始的位置。用它來標記每個重複或創建唯一識別碼：

| type | name | label |
|------|------|-------|
| begin_repeat | plots | 地塊 |
| note | plot_label | 地塊編號 ${index()} |
| text | plot_id | 地塊 ID |
| end_repeat | | |

---

## 引用同一實例中的字段

在重複內，使用 `${fieldname}` 引用**同一重複實例**中的另一個字段。在同一循環內不需要 `indexed-repeat()`：

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | 成員 | |
| text | member_name | 姓名 | |
| integer | member_age | 年齡 | |
| text | school_name | 學校名稱 | `${member_age} < 18` |
| end_repeat | | | |

---

## 從重複內部引用父字段

重複群組外部（上方）的字段可以用 `${fieldname}` 正常引用：

| type | name | label |
|------|------|-------|
| text | village | 村莊名稱 |
| begin_repeat | plots | 農業地塊 |
| note | plot_context | ${village} 中的地塊 |
| end_repeat | | |

---

## 匯總重複資料

在重複群組**外部**使用重複聚合函數進行匯總：

| 函數 | 範例 | 說明 |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | 實例數量 |
| `sum(field)` | `sum(${loan_amount})` | 數字字段的總和 |
| `min(field)` | `min(${member_age})` | 最小值 |
| `max(field)` | `max(${member_age})` | 最大值 |
| `join(sep, field)` | `join(', ', ${member_name})` | 逗號分隔列表 |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | 條件計數 |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | 條件求和 |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | 條件連接 |

### 範例：家庭摘要

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | 有多少成員？ | |
| begin_repeat | members | 成員 | `${num_members}` |
| text | member_name | 姓名 | |
| integer | member_age | 年齡 | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} 名成員；${children_count} 名 18 歲以下。成年人：${adult_names} | |

---

## 嵌套重複

重複群組可以包含另一個重複群組。謹慎使用——嵌套重複增加了複雜性，可能使調查員感到困惑。

| type | name | label |
|------|------|-------|
| begin_repeat | households | 家庭 |
| text | hh_id | 家庭 ID |
| begin_repeat | hh_members | 成員 |
| text | member_name | 成員姓名 |
| end_repeat | | |
| end_repeat | | |

要從內部重複引用外部重複中的字段，使用 `${fieldname}`——它解析為最近的匹配祖先：

在 `hh_members` 重複內，`${hh_id}` 返回**當前**家庭的 ID，而非所有家庭。

---

## 重複群組中的排序：`rank-index()`

當 `rank` 字段存在於重複內時，使用 `rank-index(instanceNumber, repeatedField)` 從外部獲取特定實例的序數排名：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` 返回最高分的實例索引。

---

## 最佳實踐

1. 當重複次數事先知曉時，始終使用 `repeat_count`——它可以防止調查員意外添加或刪除實例。
2. 保持重複群組專注——每個實例有 20 個以上問題的重複難以導航。
3. 清晰命名重複群組（例如 `household_members`，而非 `repeat1`）——名稱出現在函數呼叫和匯出資料中。
4. 使用預期最大實例數進行測試以驗證效能。
5. 在重複群組上使用 `field-list` 外觀，在行動裝置上每個實例顯示所有字段在一個螢幕上。

---

## 限制

- `indexed-repeat()` 需要有效索引（1 到實例數）——超出範圍的索引返回空。
- 不建議超過 2 層的嵌套重複，在某些客戶端上可能導致顯示問題。
- 聚合函數（`sum`、`count` 等）對整個重複群組操作——您不能在不使用 `*-if` 變體的情況下聚合實例子集。
