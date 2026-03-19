---
title: "File"
description: "文件题目允许受访者上传文档和其他文件作为调查回答的一部分。"
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

`file` 题目类型允许受访者从其设备**上传任何文件**——文档、电子表格、PDF 或其他文件类型。与启动特定捕获工具的 `image`、`audio` 和 `video` 不同，`file` 打开通用文件选择器。

## 基本 XLSForm 规范

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | 请上传您的文件  |

有关标准 file 题目类型的更多详情，请参阅 [XLSForm 规范](https://xlsform.org/en/#question-types)。

## 用途

文件题目通常用于：

1. 收集支持文件（收据、证书、合同、报告）
2. 上传已扫描的纸质表单
3. 收集来自其他系统的电子表格或数据导出
4. image/audio/video 不涵盖的任何数字文件类型

## 数据格式

上传的文件作为二进制附件存储：

- **格式：** 保留原始格式（PDF、XLSX、DOCX 等）
- **命名：** `{instanceID}-{fieldname}.{extension}`
- **存储：** 与提交一起上传到服务器媒体文件夹
- **访问：** 可从提交管理界面下载

## rtSurvey 扩展

### 接受的文件类型

使用 `parameters` 列限制可以选择的文件类型：

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | 上传检查报告 | `accept=.pdf` |
| file | spreadsheet | 上传数据文件 | `accept=.xlsx,.csv` |

`accept` 参数使用标准文件扩展名语法（逗号分隔）。

### 文件大小指南

rtSurvey 在题目级别不强制执行硬性文件大小限制，但服务器上传限制适用。使用 `hint` 向枚举员传达期望：

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | 上传付款收据 | 接受：PDF 或图片。最大文件大小：5 MB |

### 与设备文件系统和云存储集成

在 Android 和 iOS 上，`file` 题目打开设备的原生文件选择器，可能包括访问：
- 设备本地存储
- SD 卡（Android）
- iCloud Drive（iOS）
- Google Drive、Dropbox（如果已安装）

在网页上，它打开浏览器的标准文件上传对话框。

## 使用示例

### 必填 PDF 上传

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | 上传已签署的同意书 | 仅限 PDF，最大 2MB | yes | 需要同意书 |

### 条件文件上传

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | 家庭有土地证吗？ | |
| file | land_title_doc | 上传土地证的照片或扫描件 | `${has_land_title} = 'yes'` |

## 最佳实践

1. 使用 `accept` 限制文件类型——这可以防止枚举员意外上传错误的文件。
2. 始终在 `hint` 列中包含大小和格式指南。
3. 对于照片和图像，使用 `image` 类型——它提供更好的压缩和一致的格式处理。
4. 对于含文件附件的大型调查，相应规划数据存储和下载带宽。
5. 在目标设备类型（Android vs. iOS vs. 网页）上测试文件选择器，然后再部署——对云端存储的访问权限各不相同。

## 数据处理注意事项

- 文件以原始格式存储；rtSurvey 不会转换或压缩它们。
- 下载后分析文件——rtSurvey 不提取或索引文件内容。
- 大型文件附件会显著增加下载完整数据集所需的时间。

## 限制

- 文件题目不验证文件内容——只有通过 `accept` 的文件扩展名检查在 UI 层面执行。
- 在低连接环境中，非常大的文件（100 MB 以上）上传可能超时。
- 离线枚举员可以附加文件，但在恢复连接之前不会上传。
- 某些设备配置会限制对特定存储位置的访问（例如，企业 MDM 策略）。
