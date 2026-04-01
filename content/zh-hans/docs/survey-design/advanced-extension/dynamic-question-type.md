---
title: "动态题目类型"
description: "动态题目类型允许字段的题目类型和控件在运行时根据 API 响应或计算值来确定。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

**动态题目类型**功能允许字段的输入控件和验证行为在**运行时**而非表单设计时确定。这是一个高级 rtSurvey 扩展，用于当要收集的数据类型取决于服务器端配置、API 响应或前面的字段值时。

一个常见用例是可配置的检查清单，其中服务器定义哪些字段是必填的、它们是什么类型（文本、整数、选择等）以及可用的选项——无需为每种配置重建表单。

---

## 工作原理

标记为动态题目类型的字段使用 `callapi()` 从 API 获取其配置。API 响应定义：

- 要渲染的输入类型（text、integer、select_one 等）
- 可用的选项（对于选择类型）
- 验证规则

该字段在内部被标记为 `specialFeature: isDynamicQuestionType`，这告诉表单引擎使用 API 响应构建控件，而不是静态的表单定义。

---

## 设置

### 第一步：获取字段配置

使用带 `callapi()` 的 `calculate` 字段来检索动态配置：

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### 第二步：在动态字段中引用配置

动态字段在其 `appearance` 或 `constraint` 中使用 `callapi-verify()` 链接到获取的配置：

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | 检查结果 | `callapi-verify(dynamicParams)` |

表单引擎读取 `field_config` 并动态确定是否将 `inspection_result` 渲染为 `text`、`integer` 或 `select_one` 字段。

---

## API 响应格式

API 应返回描述字段配置的 JSON 对象。典型响应：

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "通过"},
      {"value": "fail", "label": "失败"},
      {"value": "na", "label": "不适用"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## 示例：可配置检查表单

根据检查类别从服务器获取清单项目及其答案类型的检查表单：

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | 检查类型 | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | 项目 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | 项目 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | 项目 3 | `callapi-verify(dynamicParams)` | |

服务器根据 `insp_type` 返回每个项目的正确控件类型、标签、选项和验证规则。

---

## 最佳实践

1. 仅在字段结构在运行时真正变化时使用动态题目类型——对于静态表单，使用标准题目类型。
2. 确保配置 API 响应迅速（2 秒以内），并且在现场网络上可用。
3. 始终在表单中为 API 不可达的情况定义合理的回退——带注释的纯 `text` 字段比损坏的控件好。
4. 对 API 响应架构进行版本控制——响应格式的更改将影响使用该端点的所有活跃表单。
5. 在部署之前测试 API 可能返回的每种字段类型组合。

## 限制

- 动态题目类型需要网络连接来获取配置。
- 动态可用的控件类型的完整范围取决于 rtSurvey 客户端版本——测试您的目标版本。
- 这是一个高级 rtSurvey 扩展，在标准 XLSForm 规范中没有等效项。
- 由于字段定义部分存在于表单中，部分存在于 API 响应中，调试错误更难追踪。
