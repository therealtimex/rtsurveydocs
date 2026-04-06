---
title: "Meta"
description: "元数据题目类型自动捕获设备、枚举员和时间信息，无需受访者任何输入。"
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

元数据题目类型是**自动**填写的特殊字段——受访者永远不会看到它们。它们捕获关于提交的上下文：数据是何时收集的、使用了哪个设备以及谁收集的。像任何其他题目类型一样在 `survey` 工作表中添加它们；它们只是不会出现在屏幕上。

## 基本 XLSForm 规范

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

由于元数据字段从不显示，标签是可选的。

---

## 时间元数据字段

### `start`

记录**表单打开时的日期和时间**。以 ISO 8601 格式存储（`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`）。

```
type    | name  | label
start   | start |
```

### `end`

记录**表单提交时的日期和时间**。与 `start` 结合，您可以计算填写表单所花费的时间：

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

记录**当前日期**（无时间组件）。以 `YYYY-MM-DD` 格式存储。当您只需要日期而不需要完整时间戳时很有用。

```
type  | name  | label
today | today |
```

---

## 设备元数据字段

### `deviceid`

记录用于数据收集的**设备的唯一标识符**。在 Android 上，这通常是 IMEI 或 Android ID。用于跟踪哪台设备提交了每个表单以及检测同一设备的重复提交。

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

记录设备中 SIM 卡的**电话号码**（如果可用）。如果设备没有 SIM 卡或号码未存储在 SIM 卡上，可能为空。

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

记录 **SIM 卡的序列号**（ICCID）。用于识别使用了哪个 SIM/运营商。

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

记录 **IMSI（国际移动用户识别码）**——SIM 卡上的唯一用户标识符。

```
type         | name        | label
subscriberid | subscriberid |
```

---

## 枚举员元数据字段

### `username`

记录**已登录枚举员的用户名**（rtSurvey 应用中使用的账户）。这是跟踪谁收集了每次提交的最可靠方式。

```
type     | name     | label
username | username |
```

### `email`

记录**已登录枚举员的电子邮件地址**。

```
type  | name  | label
email | email |
```

### `phonenumber`

记录与枚举员账户关联的**电话号码**（如果已配置）。

```
type        | name       | label
phonenumber | phonenumber |
```

---

## 审计日志

### `audit`

`audit` 元数据字段启用**详细的审计日志记录**——它记录枚举员访问每个题目的时间戳日志、在每个题目上花费的时间，以及（可选）每一步的 GPS 位置。审计日志作为单独的 `audit.csv` 文件与每次提交一起保存。

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### 审计参数

| 参数 | 描述 |
|-----------|-------------|
| `location-priority` | GPS 精度级别：`no-gps`、`low-power`、`balanced`、`high-accuracy` |
| `location-min-interval` | 位置捕获之间的最小秒数 |
| `location-max-age` | 可接受的缓存位置的最大年龄（秒） |

审计日志捕获：
- 题目名称和事件类型（`question`、`form.start`、`form.exit`、`form.save`、`form.finalize`）
- 每个事件的开始和结束时间戳
- GPS 坐标（如果设置了 `location-priority`）

{{% alert icon=" " context="warning" %}}
`audit` 字段每次提交生成一个单独的文件。确保您的数据管道同时处理主表单数据和审计 CSV。
{{% /alert %}}

---

## 完整示例

典型的家庭调查可能包含所有时间和枚举员元数据字段：

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | 家庭 ID |
| ... | ... | ... |

---

## 最佳实践

1. 始终包含 `start` 和 `end`——它们是免费的、自动的，对于质量监控来说非常宝贵。
2. 始终包含 `username` 来跟踪枚举员。
3. 当您想检测重复提交或跟踪现场设备时，包含 `deviceid`。
4. 在高问责调查中使用 `audit`，您需要验证枚举员确实访问了每个题目。
5. SIM 相关字段（`simserial`、`subscriberid`、`devicephonenum`）只在有活跃 SIM 卡的 Android 设备上可靠——对于纯平板电脑部署可跳过它们。

---

## 限制

- 所有元数据字段都是**只读的**——它们不能被其他计算引用或修改。
- `username` 和 `email` 需要枚举员已登录；对于匿名提交，它们将为空。
- SIM/电话元数据字段在纯 Wi-Fi 平板电脑和某些 Android 版本上可能返回空值，因为权限限制。
