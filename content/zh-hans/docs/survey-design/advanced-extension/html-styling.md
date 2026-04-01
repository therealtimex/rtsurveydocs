---
title: "HTML 样式"
description: "rtSurvey 在标签和提示中支持 HTML 标签，允许富文本格式、链接和动态颜色主题。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey 在网页表单上将 **label** 和 **hint** 文本渲染为 HTML。这意味着您可以使用标准 HTML 标签来格式化文本、添加换行、创建链接和应用颜色。这对于注释字段、章节说明和动态摘要特别有用。

{{% alert icon=" " context="warning" %}}
标签中的 HTML 在**网页表单**和 rtSurvey 移动应用上渲染。它可能不在所有 ODK 兼容客户端中渲染。始终在您的目标平台上测试。
{{% /alert %}}

---

## 支持的 HTML 标签

### 文本格式

| 标签 | 效果 |
|-----|--------|
| `<strong>text</strong>` 或 `<b>text</b>` | **粗体文本** |
| `<em>text</em>` 或 `<i>text</i>` | *斜体文本* |
| `<u>text</u>` | 下划线文本 |
| `<br>` | 换行 |
| `<span style="...">text</span>` | 内联样式 |

### 链接

```html
<a href="https://example.com" target="_blank">点击这里</a>
```

在新标签页中打开。用于枚举员应该查阅的参考文档、指南或外部资源。

### 颜色

使用带内联样式的 `<span>`：

```html
<span style="color: red;">警告：值超出范围</span>
<span style="color: #009688;">章节已完成</span>
```

---

## 颜色主题变量

rtSurvey 支持适应应用配置主题的**颜色主题标记**。使用 `__COLOR_THEME_NAME__` 语法：

```html
<span style="color: var(--color-theme-primary);">主色调文本</span>
```

或在标签文本中使用标记简写：

```
<font color="var(--COLOR_THEME_PRIMARY)">重要说明</font>
```

这在渲染时自动转换为带 CSS 变量的等效 `<span>`。

---

## 多语言标签

在语言标签中包装内容以在单个标签单元格中支持多种语言：

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey 提取与当前应用语言匹配的内容。如果未找到匹配的语言标签，则按原样显示完整字符串。

---

## 注释字段中的示例

### 带粗体和换行的章节说明

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>第 3 部分：土地利用</strong><br>本部分所有问题只询问户主。` |

### 带计算引用的动态摘要

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `家庭成员总数：<strong>${total}</strong><br><span style="color: gray;">成年人：${adults} · 儿童：${children}</span>` |

### 红色警告

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>警告：</strong>输入的年龄（${age}）异常偏高。请核实。</span>` | `${age} > 100` |

### 链接到参考文档

| type | name | label |
|------|------|-------|
| note | guidelines_link | `开始本部分之前，请参阅<a href="https://docs.example.com/guidelines" target="_blank">现场指南</a>。` |

---

## 特殊 rtSurvey HTML 标签

### `<webbox src='url' title='title'>...</webbox>`

嵌入一个在表单内模态框中打开 URL 的按钮。有关完整详情，请参阅 [Webbox](webbox)。

### `<delete-repeat-current>label</delete-repeat-current>`

在重复组内渲染一个按钮，点击时删除当前重复实例。

### `<delete-repeat-last>label</delete-repeat-last>`

渲染一个删除最后一个重复实例的按钮。

在重复组中的使用示例：

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>删除此成员</delete-repeat-current>` |

---

## 最佳实践

1. 谨慎使用 HTML——过度格式化的标签更难读，而不是更容易读。
2. 粗体首选 `<strong>`，斜体首选 `<em>`，而不是已弃用的 `<b>` 和 `<i>`。
3. 使颜色使用有意义——红色用于警告，不用于装饰。
4. 始终在移动应用和网页表单上测试 HTML 渲染，因为渲染可能略有不同。
5. 避免在标签中使用 `<table>` 标签——它们在移动屏幕上很少能很好地渲染。
6. 不要使用 JavaScript（`<script>`）——它将被剥离或导致错误。

## 限制

- 不支持复杂 HTML（表格、表单、脚本），可能会破坏渲染。
- 某些旧版移动客户端可能将 HTML 标签显示为文字文本——在所有目标设备上测试。
- `<a>` 链接在浏览器或 WebView 中打开——枚举员离开表单，这在移动端可能会造成干扰。
