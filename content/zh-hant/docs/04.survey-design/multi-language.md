---
title: "多語言支援"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey 提供強大的多語言支援，讓您可以建立多種語言的問卷調查。此功能對於在不同語言人群中進行研究或在多語言環境中進行調查至關重要。

## 設定多語言問卷調查

要在 rtSurvey 中建立多語言問卷調查，您需要在 XLSForm 中添加特定語言的欄位。方法如下：

1. **標籤翻譯**：使用 `label::Language (code)` 格式為每種語言添加欄位。
2. **提示翻譯**：使用 `hint::Language (code)` 翻譯提示。
3. **媒體文件翻譯**：對於特定語言的媒體，使用 `media::Language (code)`。

範例：

```
| type    | name | label::English (en) | label::Español (es) | hint::English (en) | hint::Español (es) |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | How old are you?    | ¿Cuántos años tienes?| Enter your age      | Ingrese su edad     |
```

## 語言代碼

建議在語言名稱後使用官方 2 字符語言代碼（子標籤）。這有助於將表單語言與使用者介面語言匹配。您可以在[此處](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)找到官方代碼。

## 設定預設語言

要設定資料收集的預設語言，請在 XLSForm 的 `settings` 工作表中使用：

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | French (fr)       |
```

## rtSurvey 特定功能

### 動態語言切換

rtSurvey 允許使用者在資料收集期間動態切換語言：

- 在網頁介面中，使用頂部導航欄中的語言下拉選單。
- 在行動應用程式中，透過設定選單存取語言選項。

### 特定語言的驗證訊息

rtSurvey 將多語言支援擴展至驗證訊息：

```
| type    | name | constraint | constraint_message::English (en) | constraint_message::Español (es) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Age must be 150 or less          | La edad debe ser 150 o menos     |
```

### RTL 語言支援

對於從右到左（RTL）的語言，如阿拉伯語或希伯來語，rtSurvey 會自動調整佈局：

```
| type | name | label::English (en) | label::Arabic (ar) |
|------|------|---------------------|---------------------|
| text | name | Your name           | اسمك                |
```

### 特定語言的外觀

rtSurvey 允許您為不同語言指定不同的外觀：

```
| type | name | label::English (en) | label::Chinese (zh) | appearance::English (en) | appearance::Chinese (zh) |
|------|------|---------------------|---------------------|--------------------------|---------------------------|
| text | address | Address          | 地址                 | multiline                | textarea                  |
```

## 多語言問卷調查的最佳實踐

1. **一致的命名**：在整個表單中使用一致的語言代碼。
2. **專業翻譯**：聘請熟悉問卷調查背景的專業翻譯人員。
3. **背景備注**：為翻譯人員提供背景備注，確保準確翻譯。
4. **測試**：在部署前以所有語言測試您的表單。
5. **Unicode 支援**：確保您的資料收集裝置支援非拉丁文字的 Unicode。
6. **特定語言的媒體**：為每種語言使用文化上適當的圖像或音頻。
7. **避免圖像中的文字**：如果使用帶有文字的圖像，請為每種語言建立單獨的圖像。

## 處理特殊情況

### 混合語言回應

rtSurvey 允許受訪者以任何文字輸入文字，無論選取的表單語言如何。這對於以原始文字捕獲姓名或地址很有用。

### 特定語言的問題類型

某些問題類型可能更適合特定語言。rtSurvey 允許您為不同語言使用不同的問題類型：

```
| type::English (en) | type::Japanese (ja) | name | label::English (en) | label::Japanese (ja) |
|--------------------|---------------------|------|---------------------|----------------------|
| text               | select_one kanji    | name | Enter your name     | 名前を選んでください    |
```

## 匯出多語言資料

從 rtSurvey 匯出資料時：

- 選擇以特定語言匯出或包含所有語言版本。
- 語言元資料包含在匯出中，指示每個回應使用了哪種語言。

## 行動應用程式注意事項

- rtSurvey 行動應用程式支援離線語言切換。
- 確保在離線前已下載所有所需的語言文件。

## 已知限制

- 某些進階功能可能無法在所有語言中使用。
- 極長的翻譯可能會影響較小螢幕上的佈局。

透過利用 rtSurvey 的多語言功能，您可以建立包容性、可存取性的問卷調查，覆蓋多元人群，並提供高品質、語言準確的資料。
