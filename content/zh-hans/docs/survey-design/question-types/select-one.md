---
title: "Select_one"
description: "Select_one 题目让受访者从预定义的选项列表中选择恰好一个选项。"
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

`select_one` 题目类型提示受访者从预定义列表中选择**恰好一个选项**。默认情况下，选项以单选按钮的形式渲染，但可以使用多种外观选项来更改布局和行为。

## 基本 XLSForm 规范

**survey 工作表：**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | 受访者是否给予同意？ |

**choices 工作表：**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | 是 |
| yesno | no | 否 |

`select_one listname` 中的 `listname` 必须与 choices 工作表中的 `list_name` 列匹配。

更多详情请参阅 [XLSForm 规范](https://xlsform.org/en/#question-types)。

## 用途

Select_one 题目用于：

1. 是/否题
2. 单答多选题（例如，教育程度、性别、婚姻状况）
3. 分类评级（例如，差 / 一般 / 好 / 优秀）
4. 级联（链接）选择，其中选项根据先前的回答进行过滤
5. 国家、地区、区县或其他行政单位的选择

## 外观选项

在 `appearance` 列中指定值以更改选项的显示方式：

{{< table >}}
| 外观 | 描述 |
|------------|-------------|
| *（无）* | 默认单选按钮，每行一个 |
| `minimal` | 单个下拉/旋转框而不是单选按钮 |
| `quick` | 选择后立即自动前进到下一个题目（仅限移动端） |
| `compact` | 紧凑的选项网格——列数根据屏幕宽度调整 |
| `compact-N` | 强制显示 N 列的紧凑网格（例如，`compact-3`） |
| `quickcompact` | 结合 `quick` 和 `compact` |
| `quickcompact-N` | 结合 `quick` 和 `compact`，强制显示 N 列 |
| `horizontal` | 选项水平排列成一行（网页） |
| `horizontal-compact` | 水平，紧凑间距（网页） |
| `likert` | 李克特量表行——标签在上，单选按钮在下 |
| `label` | 仅显示选项标签，无输入（与 `list-nolabel` 配对使用） |
| `list-nolabel` | 仅显示输入，无标签（与 `label` 配对使用） |
| `columns(N)` | 以 N 列显示（rtSurvey 扩展，例如，`columns(3)`） |
| `distress` | Kessler 心理困扰（K10）情感图标控件 |
| `search-api(...)` | 动态搜索——在运行时从 API 加载选项 |
| `tagging` | 将选项显示为可点击的标签片，而不是单选按钮 |
| `boxtag` | 将选项显示为样式化的矩形框，用户点击以选择 |
| `boxtag -search` | 带有搜索/过滤输入框的 Boxtag 布局 |
| `duolingo-style1` | Duolingo 风格的卡片布局——带图标的大型可点击卡片 |
| `rating_box` | 基于网格的评分框——最适合数字或量表选项 |
| `star_rating` | 星级评分控件——选项呈现为 1–N 颗星 |
| `choices-noshow` | 初始仅显示前 10 个选项；按需显示其余选项 |
| `noshow` | 完全隐藏选项列表；值通过程序设置 |
| `checkall` | 在列表顶部添加"全选"选项 |
| `max-items(N)` | 将可见选项数量限制为 N（例如，max-items(5)） |
{{< /table >}}

### 示例：李克特量表

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | 您对服务的满意度如何？ | likert |

### 示例：紧凑 3 列

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | 选择地区 | compact-3 |

## 级联选择

级联（链接）选择根据先前题目中选择的值过滤选项。使用 `choice_filter` 列配合 choices 工作表中的列名。

**survey：**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | 选择省份 | |
| select_one district | district | 选择区县 | province_name = ${province} |

**choices：**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | 内罗毕 | |
| province | mombasa | 蒙巴萨 | |
| district | westlands | 西部地区 | nairobi |
| district | kasarani | 卡萨拉尼 | nairobi |
| district | nyali | 尼亚利 | mombasa |
| district | likoni | 利科尼 | mombasa |

当受访者选择 `nairobi` 时，区县列表中只出现"西部地区"和"卡萨拉尼"。

{{% alert icon=" " context="warning" %}}
`choice_filter` 中使用的列名（例如，`province_name`）必须存在于 choices 工作表中。`${province}` 引用名为 `province` 的调查字段。
{{% /alert %}}

## 在表达式中使用所选值

使用 `${fieldname}` 引用所选**值**（而非标签）：

```
relevant: ${consent} = 'yes'
```

要获取选项标签而不是值，使用 `choice-label()`：

```
calculate: choice-label(${education_level}, ${education_level})
```

## 带自由文本的"其他"选项

一种常见模式是包含一个显示文本字段的"其他"选项：

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | 您的职业是什么？ | |
| text | job_other | 请说明 | `${job} = 'other'` |

**choices：**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | 农民 |
| occupation | trader | 商人 |
| occupation | student | 学生 |
| occupation | other | 其他（请说明） |

## 最佳实践

1. 保持列表简短且相互排斥——如果受访者可能需要多个答案，使用 `select_multiple`。
2. 将最常见的答案排在前面，或对长列表按字母顺序排列。
3. 在相关情况下，始终包含"不知道"或"不愿回答"的选项。
4. 对于移动端超过 7–8 个选项的列表，使用 `minimal`（下拉框）以节省屏幕空间。
5. 对于级联选择，在构建表单之前，在 choices 工作表中添加所有过滤列。

## 限制

- 受访者只能选择一个选项——对于多答案题，使用 `select_multiple`。
- `likert` 外观最适合 5–7 个适合一行的选项。
- `quick` 自动前进仅限移动端；在网页表单上无效。
