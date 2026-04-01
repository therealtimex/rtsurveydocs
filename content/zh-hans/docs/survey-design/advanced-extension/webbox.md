---
title: "Webbox"
description: "Webbox 将外部网页以模态 iframe 的形式嵌入调查中，允许枚举员查看参考资料或与外部工具交互，而无需离开表单。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** 将外部网页以**模态弹出窗口**（iframe）的形式嵌入调查中。枚举员点击标签或注释文本中的按钮，页面在表单内的全屏覆盖层中打开，关闭后他们回到原来的位置。这让您可以显示参考材料、地图、仪表板或自定义工具，而无需打开单独的浏览器标签。

---

## 语法

直接在 `label` 或 `note` 标签列中插入 `<webbox>` HTML 标签：

```html
<webbox src='https://example.com/reference' title='参考指南'>打开参考指南</webbox>
```

| 属性 | 描述 |
|-----------|-------------|
| `src` | 在 iframe 中加载的 URL。支持单引号和双引号。 |
| `title` | 在模态标题栏中显示的文本。支持纯文本。 |
| *（内容）* | 在调查字段中显示的可点击按钮标签 |

---

## 基本示例

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='现场指南'>📖 打开现场指南</webbox>` |

这渲染一个标有"📖 打开现场指南"的按钮。点击后，模态窗口打开显示现场指南网站。

---

## 嵌入地图

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='调查区域地图'>🗺 查看地图</webbox>` |

---

## 将表单值传递到嵌入页面

使用 `calculation` 列中的 `concat()` 将表单字段值附加到 URL，并在标签中引用结果：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='家庭仪表板'>打开仪表板</webbox>` |

{{% alert icon=" " context="warning" %}}
当标签从 `calculate` 字段计算时，`<webbox>` 标签中的 `src` 属性支持 `${fieldname}` 引用。在 `calculate` 字段中构建完整 URL 并引用它。
{{% /alert %}}

---

## 重复交互：删除按钮

Webbox 还支持在标签内管理重复组的特殊操作标签：

```html
<delete-repeat-current>删除此行</delete-repeat-current>
<delete-repeat-last>删除最后一行</delete-repeat-last>
```

这些渲染为按钮，点击时删除重复实例。将它们放在重复组内（或紧跟其后）的 `note` 字段中：

| type | name | label |
|------|------|-------|
| begin_repeat | items | 项目 |
| text | item_name | 项目名称 |
| note | delete_btn | `<delete-repeat-current>✕ 删除此项目</delete-repeat-current>` |
| end_repeat | | |

---

## 与嵌入页面的通信（postMessage）

webbox iframe 和父表单可以使用浏览器的 `postMessage` API 进行通信。父级在打开时向 iframe 发送 `init` 消息。嵌入的页面可以响应：

- `delete-repeat-current` — 触发删除当前重复实例
- `delete-repeat-last` — 触发删除最后一个重复实例

这使自定义网络工具（例如，绘图工具、交互式地图）能够在用户确认 iframe 内的操作时触发表单操作。

---

## 最佳实践

1. 将 webbox 用于**参考材料**（指南、查找表、地图）——而不是用于收集应在表单本身中的数据。
2. 确保嵌入的 URL 可从设备的网络访问——webbox 需要连接。
3. 保持嵌入页面适合移动端——模态最宽 800px，视口高度的 80%。
4. 使用描述性的按钮文字（例如，"查看村庄地图"）而不是通用标签（"点击这里"）。
5. 告知枚举员关闭模态后返回调查——某些用户可能不知道如何关闭 iframe 覆盖层。

## 限制

- Webbox 需要网络连接来加载嵌入的 URL。
- 某些外部站点通过 `X-Frame-Options` 或 `Content-Security-Policy` 标头阻止在 iframe 中嵌入——这些站点无法与 webbox 一起使用。
- 当枚举员离开当前题目时，模态关闭——iframe 中未保存的状态会丢失。
- Webbox 是 rtSurvey 网页表单扩展，在其他 ODK 兼容客户端中可能不起作用。
