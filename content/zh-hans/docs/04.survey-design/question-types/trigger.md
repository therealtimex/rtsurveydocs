---
title: "Trigger / Acknowledge"
description: "Trigger 题目显示枚举员在继续之前必须明确确认的陈述。"
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

`trigger`（也称为 `acknowledge`）题目类型显示一个**带复选框的陈述**。枚举员必须勾选复选框以确认他们已阅读并理解该陈述，然后表单才允许继续。不存储数据值——只记录复选框是否被勾选。

## 基本 XLSForm 规范

| type | name | label |
|------|------|-------|
| trigger | consent_ack | 受访者已提供口头知情同意。 |

或使用 `acknowledge` 别名：

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | 受访者已提供口头知情同意。 |

`trigger` 和 `acknowledge` 等效——使用您平台文档中记载的任一种。

## 用途

Trigger/acknowledge 题目通常用于：

1. **知情同意**——确认枚举员在记录敏感数据之前获得了同意
2. **软警告**——对异常值发出警告，并要求在继续前明确确认
3. **清单项目**——确认已完成物理观察（例如，"我已直接观察了水源"）
4. **说明**——强制枚举员在继续之前确认章节级说明
5. **质量检查**——标记异常值并要求枚举员验证它们

## 使用示例

### 同意确认

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | 受访者已口头同意参与本次调查。 | yes |

### 异常值的软警告

与 `relevant` 表达式一起使用，仅在输入可疑值时显示 trigger：

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | 子女数量 | | |
| trigger | children_confirm | 您输入了 ${children} 个子女。请与受访者核实并点击确定。 | `${children} > 10` | `${children} > 10` |

### 章节开始时的说明确认

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | B 部分：农业土地利用。本部分所有问题只询问户主。 |

## 使 trigger 成为必填项

添加 `required: yes` 以防止在勾选复选框之前继续：

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | 所有安全设备均存在且正常工作。 | yes | 您必须确认才能继续。 |

## 条件显示

仅在满足条件时显示 trigger：

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | 家庭有水井吗？ | |
| trigger | well_observation | 确认您已直接观察水井状况。 | `${has_well} = 'yes'` |

## 与 `note` 的区别

| | `note` | `trigger` |
|--|--------|-----------|
| 显示文本 | 是 | 是 |
| 需要交互 | 否 | 是（必须勾选） |
| 存储数据 | 否 | 否（仅确定/已勾选） |
| 可以阻止进度 | 否 | 是（配合 `required`） |

## 最佳实践

1. 保持 trigger 标签简洁且可操作——枚举员应能在几秒钟内阅读并确认。
2. 当确认是强制性的时，始终添加 `required: yes`。
3. 在需要审计记录（证明枚举员已确认）的同意和安全检查中使用 trigger。
4. 与 `relevant` 结合，用于条件软警告，这样 trigger 只在值需要验证时才出现。

## 限制

- Trigger 字段不存储有意义的数据值——它们只记录复选框已被勾选。
- 在大多数客户端上，trigger 控件显示为简单的复选框/按钮；它不是完整的电子签名。
