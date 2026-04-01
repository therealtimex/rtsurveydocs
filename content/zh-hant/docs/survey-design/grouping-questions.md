---
title: "問題分組"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

XLSForm 中的群組允許您將相關問題組織在一起，改善問卷調查的結構並增強資料分析能力。rtSurvey 完全支援 XLSForm 群組，並使用附加功能擴展其功能。

## 基本群組結構

要建立問題群組，請使用 `begin_group` 和 `end_group` 語法：

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondent Information                   |
| text         | name       | Enter the respondent's name              |
| text         | position   | Enter the respondent's position          |
| end_group    |            |                                          |
```

主要要點：
- `begin_group` 行需要 `name` 和 `label`。
- `end_group` 行不需要名稱或標籤。
- `begin_group` 和 `end_group` 之間的問題屬於該群組。

## 群組外觀

rtSurvey 支援群組的各種外觀選項：

1. **field-list**：在同一螢幕上顯示多個問題。
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Respondent| field-list |
   | text         | name       | Name      |            |
   | text         | position   | Position  |            |
   | end_group    |            |           |            |
   ```

2. **grid**：為群組建立緊湊的、類似表格的佈局（rtSurvey 特定）。
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Household | grid       |
   | text         | member_name| Name      |            |
   | integer      | member_age | Age       |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**：建立可展開/可收合的群組（rtSurvey 特定）。
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Details   | collapsible |
   | text         | address    | Address   |             |
   | text         | phone      | Phone     |             |
   | end_group    |            |           |             |
   ```

## 巢狀群組

群組可以巢狀在其他群組中，以實現更複雜的結構：

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Hospital Information                     |
| text         | hosp_name  | What is the name of this hospital?       |
| begin_group  | medication | Medication Availability                  |
| select_one y_n| hiv_meds  | Does this hospital have HIV medication?  |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**注意**：始終先結束最近開始的群組，以保持適當的巢狀結構。

## 群組的跳題邏輯

使用 `relevant` 欄對整個群組實現跳題邏輯：

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | How old are you?                             |                 |
| begin_group  | child  | Child                                        | ${age} <= 5     |
| integer      | muac   | Record child's mid-upper arm circumference   |                 |
| select_one y_n| mrdt  | Is the child's rapid diagnostic test positive?|                |
| end_group    |        |                                              |                 |
```

在此範例中，`child` 群組只有在受訪者年齡為 5 歲或以下時才會出現。

## 使用群組的最佳實踐

1. 使用有意義的群組名稱以改善資料分析。
2. 讓群組專注於相關問題。
3. 謹慎使用巢狀群組以避免過於複雜的結構。
4. 在群組上使用 `relevant` 時徹底測試跳題邏輯。
5. 考慮對短群組使用 `field-list` 外觀以減少滾動。
6. 利用 rtSurvey 的網格佈局進行相關資訊的緊湊顯示。
7. 對長表單使用可收合群組以改善導航。

## rtSurvey 特定功能

1. **網格佈局**：使用 `grid` 外觀進行類似表格的顯示。
2. **可收合群組**：實現 `collapsible` 外觀以建立可展開的部分。
3. **自訂樣式**：對群組應用自訂 CSS 以實現獨特的視覺設計。
4. **動態群組行為**：在群組內實現複雜的跳題邏輯和計算。

## 多語言支援

rtSurvey 支援多語言群組。使用特定語言的標籤欄：

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Personal Info  | Infos Personnelles |
| text         | name       | Name           | Nom           |
| end_group    |            |                |               |
```

## 行動應用程式注意事項

- 帶有 `field-list` 外觀的群組在行動應用程式中顯示為單一螢幕。
- 可收合群組可以改善較小螢幕上的導航。
- 網格佈局可能會調整以在行動裝置上更好地顯示。

## 已知限制

- 群組的極深巢狀可能會影響某些裝置的效能。
- 某些進階樣式選項可能在行動應用程式中對群組不可用。

## 群組疑難排解

1. 確保每個 `begin_group` 都有對應的 `end_group`。
2. 檢查群組名稱在表單中是否唯一。
3. 驗證跳題邏輯是否參考了正確的問題名稱。
4. 在網頁和行動介面上徹底測試群組。

透過在 rtSurvey 的 XLSForms 中有效使用群組，您可以建立組織良好、高效的問卷調查，既改善資料收集體驗，又提高資料分析品質。
