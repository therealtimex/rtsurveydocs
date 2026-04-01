---
title: "Hidden"
description: "隐藏字段存储从不向受访者显示的值——用于传递上下文、预填数据或存储中间结果。"
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

`hidden` 字段存储**从不向受访者显示**的值。与 `calculate`（计算值）不同，`hidden` 用于携带**外部提供的值**——例如，从另一个系统传递的任务 ID、家庭 ID，或在表单启动时注入的枚举员代码。

## 基本 XLSForm 规范

| type | name | label |
|------|------|-------|
| hidden | household_id | |

由于屏幕上不渲染任何内容，隐藏字段不需要标签。

## 用途

隐藏字段通常用于：

1. 从调查管理系统传递预分配的 ID（例如，家庭 ID、案例编号、任务代码）
2. 存储表单版本或部署元数据
3. 在表单启动时注入枚举员特定的配置
4. 在链接工作流中将数据从父表单携带到子表单
5. 当表单通过 Web 链接打开时，存储从 URL 参数派生的值

## 设置默认值

最常见的模式是将 `hidden` 与 `default` 表达式一起使用，以便在表单打开时设置值：

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## 在计算中引用隐藏字段

隐藏值可以像任何其他字段一样使用 `${fieldname}` 引用：

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} 欢迎参加家庭调查 | |

## 将 hidden 与预填 / URL 参数一起使用

通过 URL 启动 Web 表单时，您可以传递参数来填充隐藏字段。这允许您预加载家庭 ID 或任务代码，而无需枚举员手动输入：

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

名为 `household_id` 的字段将自动填充为 `H00123`。

## 最佳实践

1. 当值是**从外部注入**且不应重新计算时，使用 `hidden`（而非 `calculate`）。
2. 当值是**从表单中的其他字段派生**时，使用 `calculate`。
3. 如果隐藏字段必须有值，始终设置 `default`——没有默认值的隐藏字段将为空。
4. 清晰地命名隐藏字段以区分它们（例如，以 `_hidden_` 为前缀或使用一致的命名约定）。

## 限制

- 隐藏字段像任何其他字段一样包含在导出数据中。
- 它们不能有条件地显示——它们始终存在（但不可见）。
- 如果需要动态计算的字段，请使用 `calculate`。
