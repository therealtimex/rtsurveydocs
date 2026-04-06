---
title: "应用 API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI 允许用户使用 FormEngine 和 DMView 中的不同方法从应用加载系统元数据。它提供对各种数据键的访问，以从应用中检索特定信息。

在 xlsform 中，您可以使用 `pulldata()` 函数，语法如下：


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`：此关键字通知 FormEngine 从 App API 加载数据。
- `'data-key'`：这是您希望从 App API 加载的数据键。
- 如果数据键无效或不受支持，计算将返回"n/a"。

以下是可与 App-API 一起使用的支持数据键：

`osPlatform`：返回当前操作系统名称（Android 或 iOS）和操作系统版本。网页平台将返回空值。

`appPlatform`：返回应用平台名称，即 `rtSurvey`。

`appVersion`：返回应用的版本名称。

`getDisplayWidth`：返回设备屏幕宽度（像素）。

`getDisplayHeight`：返回设备屏幕高度（像素）。

`getScreenSize`：返回设备屏幕尺寸（英寸）。

`projectCode`：返回用户登录站点的当前项目代码。

`projectURL`：返回用户登录站点的当前项目 URL。默认/回退值为空文本（""）。

`startingPoint`：返回启动表单的点的路径。有关详细信息，请参阅"表单起始点"。

`serverTime`：返回服务器上日期和时间的最佳可用近似值。

`user.[attribute]`：根据指定的属性键返回当前用户属性。可用属性键请参阅"用户属性"表。

将以下属性键与 `pulldata()` 参数中的"user."组合，以检索当前用户信息。例如，使用 `user.username`、`user.email` 等。

| 属性键        | 描述                          |
|----------------------|--------------------------------------|
| username             | 用户的用户名                  |
| name                 | 用户的全名                 |
| staffCode            | 用户的员工代码                     |
| phone                | 用户的电话号码              |
| email                | 用户的邮箱地址             |
| description          | 用户信息中的描述文本  |
| organization_id      | 用户所属的组织 ID    |
| organization_name    | 用户所属的组织名称  |
| team_id              | 用户所属的团队 ID            |
| supervisor_id        | 用户主管的 ID            |
| is_supervisor        | 如果用户是主管则为 1，否则为 0|

`instancePath`：返回当前实例文件夹路径。

`appLanguage`：返回应用设置中设置的当前应用语言（例如 vi、en）。

`openArgs.[attribute]`：返回从 ActionButton（act_fill_form、act_get_instance）传递的打开表单参数。默认/回退值为空文本（""）。

`primaryAppColor`：检索应用的主要颜色。

---

## 使用示例

### 存储调查员的用户名和组织

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

在注释标签中使用这些字段进行审计：
```
note | interviewer_info | 访谈员：${enumerator_name}（${enumerator_org}）
```

### 设备和屏幕信息

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

用于故障排除：将 `device_platform` 和 `app_ver` 与您的数据一起导出，以识别每次提交使用了哪个设备版本。

### 使用服务器时间而非设备时间

设备时钟可能不准确。使用 `serverTime` 获得更可靠的时间戳：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### 基于用户角色的条件逻辑

仅向主管显示主管专用部分：

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | 主管审查 | `${is_supervisor} = '1'` |
| text | supervisor_notes | 主管备注 | |
| end_group | | | |

### 从操作按钮传递参数

当表单从带有自定义参数的 `act_fill_form` 操作按钮启动时：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

操作按钮必须传递具有匹配键（例如 `household_id`、`task_code`）的参数。

### 使用项目信息

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## 注意事项

- 所有 `pulldata('app-api', ...)` 调用在表单打开时评估，在会话期间不会动态重新评估（`serverTime` 和 `now()` 除外）。
- 如果键不受支持或数据不可用，函数返回 `'n/a'`（不是空字符串——使用 `!= 'n/a'` 而不是 `!= ''` 进行测试）。
- `openArgs` 值仅在表单从操作按钮启动时可用；否则返回空字符串。
