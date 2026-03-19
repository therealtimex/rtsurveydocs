---
title: "高级扩展"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

rtSurvey 中的 `appearance` 列允许您自定义调查中题目的视觉呈现和行为。此功能可增强用户体验，并能显著提高数据收集效率。rtSurvey 支持标准 XLSForm appearance 属性，并通过附加选项进行了扩展。

## rtSurvey 特有的 Appearance 扩展

rtSurvey 通过以下内容扩展了标准 appearance 选项：

### 时间输入自定义

对于用于时间输入的 `text` 类型题目：

- `appearance:` - 显示用于选择小时和分钟的时钟
- `appearance: inline` - 将时钟显示为图标
- `appearance: inline-1line` - 以单行格式显示时钟
- `appearance: inline-onlyresult` - 显示时钟图标，选择后消失
- `appearance: inline-[FORMAT]` - 自定义时间格式显示（例如，`[%H:%M]`、`[%h:%M:%S]`）

### 颜色自定义

rtSurvey 允许对各种 appearance 进行颜色自定义：

- `appearance: inline colors("0099FF")` - 自定义图标颜色
- `appearance: inline-1line colors("0000FF","FFFF00")` - 在单行格式中自定义颜色

### 网格布局

rtSurvey 引入了网格布局，用于紧凑的、类似表格的显示：

- `appearance: grid` - 应用于组以创建网格布局

### 可折叠组

- `appearance: collapsible` - 创建可展开/折叠的组

## 使用 Appearance 的最佳实践

1. **一致性**：在整个调查中一致使用 appearance 属性，以获得统一的外观。
2. **移动端与网页**：考虑 appearance 在不同设备和平台上的渲染效果。
3. **性能**：谨慎使用可能降低表单加载速度的 appearance 属性（例如，大型组的 `table-list`）。
4. **用户体验**：选择使数据录入对受访者更容易、更直观的 appearance。
5. **测试**：始终在目标设备上测试您的表单，确保 appearance 按预期工作。

## 高级技巧

### 组合 Appearance

某些 appearance 属性可以组合以创建更复杂的布局：

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | 选择一个： | minimal compact |
```

### 动态 Appearance

rtSurvey 允许根据表单逻辑进行动态 appearance 更改：

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | 输入时间： | inline-[%H:%M] | ${show_time} = 'yes' |
```

## 移动应用注意事项

- 某些 appearance（例如，`quick`、`signature`）是移动设备特有的。
- 在 Android 和 iOS 上彻底测试，确保行为一致。

## 已知限制

- 复杂的 appearance 在所有平台上的渲染可能不完全相同。
- 某些高级 rtSurvey appearance 在离线模式下可能不受支持。

## Appearance 问题排查

1. **Appearance 未应用**：检查 appearance 列中是否有拼写错误。
2. **渲染不一致**：验证与题目类型和平台的兼容性。
3. **性能问题**：考虑简化复杂的 appearance，尤其是对于大型调查。
