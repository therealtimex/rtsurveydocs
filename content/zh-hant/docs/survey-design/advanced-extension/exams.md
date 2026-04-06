---
title: "考試"
description: "考試功能為問卷調查添加計時測驗模式，並可選擇為正確和錯誤答案提供音頻回饋。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

**考試**功能將問卷調查變成計時測驗。向受訪者顯示倒計時計時器，問卷調查記錄他們完成時剩餘的時間。可選擇為正確和錯誤答案播放音頻。

這對知識評估、識字測試、現場工作人員能力檢查以及任何任務時間是有意義資料的問卷調查都很有用。

---

## `check-exam()` 函數

使用 `check-exam()` 在表單開頭的 `calculate` 字段的 **`calculation`** 欄中配置考試：

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### 參數

| # | 參數 | 說明 |
|---|-----------|-------------|
| 1 | `examTime` | 總考試持續時間（秒） |
| 2 | `questionToStoreRemainingTime` | 考試結束時儲存剩餘時間的 `calculate` 或 `integer` 字段的 `name` |
| 3 | `rightSound` | *(可選)* 給出正確答案時播放的音頻文件名（作為媒體文件附加到表單） |
| 4 | `wrongSound` | *(可選)* 給出錯誤答案時播放的音頻文件名 |
| 5 | `excludeQuestion` | *(可選)* 要從考試計時器中排除的字段名稱的逗號分隔列表（例如 `'intro_note,consent'`） |

---

## 基本設定

### 步驟 1：添加考試字段

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` 觸發 600 秒（10 分鐘）計時器。`remaining_time` 在受訪者完成時自動填充。

### 步驟 2：添加您的問題

考試計時器涵蓋表單中除 `excludeQuestion` 中列出的所有問題。

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | 肯亞的首都是奈洛比。對還是錯？ |
| select_one choices | q2 | 哪個器官在體內泵送血液？ |
| select_one choices | q3 | 水在海平面上 100°C 時沸騰。對還是錯？ |

### 步驟 3：儲存剩餘時間

參數 2 中命名的字段（`remaining_time`）在受訪者提交時自動設定為剩餘秒數。`0` 表示時間用完；高值表示他們完成得很快。

---

## 帶音頻回饋

將聲音文件附加到表單（作為媒體附件），然後引用它們：

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` 在受訪者選擇正確答案時播放
- `wrong.mp3` 在受訪者選擇錯誤答案時播放

{{% alert icon=" " context="warning" %}}
聲音文件必須作為媒體文件附加到表單，文件名（包括副檔名）必須完全匹配（區分大小寫）。
{{% /alert %}}

---

## 從計時器中排除問題

傳遞以逗號分隔的字段名稱列表，從考試中排除（例如介紹性備注或同意問題）：

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

如果您不需要音頻但需要排除，請將 `rightSound` 和 `wrongSound` 設為空字串 `''`。

---

## 完整範例

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | 歡迎參加健康知識評估。您有 5 分鐘時間回答所有問題。 | |
| trigger | start_ack | 準備好開始時請點擊確定。 | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | 洗手可以防止疾病傳播。 | |
| select_one yesno | q2 | 您每天應該喝至少 2 升水。 | |
| select_one yesno | q3 | 瘧疾是由病毒引起的。 | |

---

## 最佳實踐

1. 在開始前始終告知受訪者時間限制——在 `check-exam()` 字段前使用 `note` 或 `trigger`。
2. 使用 `excludeQuestion` 參數從計時器中排除介紹備注和同意問題。
3. 在後續計算中使用 `remaining_time` 來檢測超時：`if(${remaining_time} = 0, '超時', '已完成')`。
4. 保持問題數量與允許時間成比例——對於大多數知識評估，每個問題 2–3 分鐘是合理的基準。
5. 在部署前在實際裝置上使用音頻文件進行測試——音頻播放在不同 Android 版本和瀏覽器上有所不同。

## 限制

- 計時器僅用於顯示——時間用完時表單不會自動提交；受訪者仍必須手動提交。
- 音頻回饋需要裝置音量打開且未靜音。
- 考試功能是 rtSurvey 擴展，不是標準 XLSForm 規格的一部分。
