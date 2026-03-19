---
title: "Text"
description: "rtSurvey 中的自由文本回答题目类型"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

`text` 题目类型收集自由文本回答——任意字符串。它是最灵活的输入类型，用于姓名、地址、描述、代码以及任何不适合更特定类型的内容。

rtSurvey 还通过**时间输入控件**扩展了 `text`，允许使用时钟选择器进行精确时间输入。

## 基本 XLSForm 规范

| type | name | label |
|------|------|-------|
| text | respondent_name | 受访者全名 |
| text | address | 家庭住址 |

有关标准 XLSForm text 类型的更多详情，请参阅 [XLSForm 规范](https://xlsform.org/en/#question-types)。

## 用途

文本题目用于：

1. 姓名、地址、自由描述
2. 开放式评论或反馈
3. 不适合 integer/decimal 的代码、ID 或参考编号
4. 使用 rtSurvey 时间输入扩展收集时间值
5. 自动完成文本字段（通过 `search-autocomplete-noedit-v2()`）

## 标准外观选项

| 外观 | 描述 |
|------------|-------------|
| *（无）* | 单行文本输入 |
| `multiline` | 多行文本区域——最适合网页上较长的自由文本 |

## rtSurvey 时间输入扩展

rtSurvey 通过**时钟选择器控件**扩展了 `text`，用于收集时间值。这些外观选项显示一个时钟图标，枚举员可以点击它来选择小时、分钟、秒或毫秒。

### 外观变体

| 外观 | 描述 |
|------------|-------------|
| `inline` | 字段旁边显示时钟图标 |
| `inline colors("RRGGBB")` | 带自定义十六进制颜色的时钟图标 |
| `inline-1line` | 以紧凑的单行格式显示时钟 |
| `inline-1line-RRGGBB` | 带自定义图标颜色的单行格式（十六进制，不带 `#`） |
| `inline-1line colors("RRGGBB","RRGGBB")` | 带两种颜色的单行格式 |
| `inline-onlyresult` | 选择后时钟图标消失；只显示值 |
| `inline-onlyresult colors("RRGGBB")` | 相同，带自定义图标颜色 |

### 时间格式标记

在括号中附加格式字符串以控制显示哪些时间组件：

| 格式字符串 | 显示内容 |
|---------------|----------|
| `inline-[%H:%M]` | 小时和分钟（24 小时制） |
| `inline-[%h:%M]` | 小时和分钟（12 小时制） |
| `inline-[%H:%M:%S]` | 小时、分钟、秒（24 小时制） |
| `inline-[%h:%M:%S]` | 小时、分钟、秒（12 小时制） |
| `inline-[%H:%M:%3]` | 小时、分钟、毫秒 |
| `inline-[%M:%S]` | 仅分钟和秒 |
| `inline-[%M:%3]` | 仅分钟和毫秒 |
| `inline-[%S]` | 仅秒 |
| `inline-[%3]` | 仅毫秒 |
| `inline-[%H]` | 仅小时（24 小时制） |
| `inline-[%h]` | 仅小时（12 小时制） |

### 示例：以分钟和秒记录任务持续时间

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | 完成任务所用时间 | `inline-[%M:%S]` |

### 示例：以自定义颜色的 24 小时格式记录事件时间

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | 事件时间 | `inline-1line colors("0099FF")` |

## 数据格式

文本数据存储并导出为纯字符串。对于使用 inline 时钟控件的基于时间的输入，值以与所选格式字符串匹配的格式存储（例如，`%H:%M` 对应 `14:32`）。

## 约束和验证

应用约束以强制执行格式、长度或模式：

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | 全名 | `string-length(.) >= 2` | 姓名至少需要 2 个字符 |
| text | code | 参考代码 | `regex(., '^[A-Z]{2}[0-9]{4}$')` | 请输入 2 个大写字母后跟 4 个数字 |
| text | phone | 电话号码 | `regex(., '^[0-9]{9,15}$')` | 请输入有效的电话号码 |

## 最佳实践

1. 只要数据具有已知结构，就使用更具体的类型（`integer`、`decimal`、`date`）——这可以防止无效输入并简化分析。
2. 使用 `constraint` 配合 `string-length()` 或 `regex()` 来验证代码或 ID。
3. 对于受访者可能写多句话的开放式问题，使用 `multiline` 外观。
4. 对于时间收集，选择与分析所需精度匹配的时间格式标记——当只需要分钟时收集毫秒会浪费枚举员的精力。

## 平台支持

text 题目类型和所有时间输入外观均支持 iOS、Android 和网页平台。

## 限制

- 文本回答是自由形式的——除正则表达式模式外，没有内置的拼写检查或词汇约束。
- inline 时间控件是 rtSurvey 扩展，不是标准 XLSForm 规范的一部分。
