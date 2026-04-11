# Vietnamese Localization Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create and update Vietnamese locale files in `_locales/vi/` to match all content added in the missing-features-docs plan (new pages + additions to existing pages).

**Architecture:** All Vietnamese files live under `_locales/vi/` and mirror the structure of `pages/`. Each file is a full MDX translation — same sections, same code blocks (untranslated), all prose in Vietnamese. Vietnamese translations keep technical terms in English (e.g., "rawquery", "appearance", "select_one") but translate all explanatory prose and table cells.

**Tech Stack:** Nextra MDX, `_locales/vi/` locale overlay, Nextra `Callout` component

---

## Translation conventions

- **Keep in English (do not translate):** field names, XLSForm column names (`type`, `name`, `label`, `appearance`, `calculation`, `relevant`, `constraint`), function names (`pulldata`, `search-autocomplete-noedit-v2`, `autopull`, etc.), appearance values (`rawquery`, `audio-start`, `SaveFinalizedExit`, etc.), code blocks, table header values that are column/parameter names, technical terms like "rawquery", "SQLite", "XLSForm", "MDX".
- **Translate:** prose paragraphs, callout text, table description cells, best-practices list items, limitations text.
- **Frontmatter `title` and `description`:** translate to Vietnamese.
- **Cross-links:** keep link targets identical (e.g., `[Local Database Search](local-database-search)` → `[Tìm kiếm cơ sở dữ liệu nội bộ](local-database-search)`).

---

## File Map

**Create:**
- `_locales/vi/survey-design/advanced-features/local-database-search.mdx` — Task 1
- `_locales/vi/survey-design/advanced-features/audio-recording.mdx` — Task 2
- `_locales/vi/survey-design/advanced-features/form-navigation.mdx` — Task 3
- `_locales/vi/survey-design/advanced-features/family-path.mdx` — Task 4
- `_locales/vi/survey-design/operators-and-functions/pulldata.mdx` — Task 5

**Modify:**
- `_locales/vi/survey-design/advanced-features/html-styling.mdx` — Task 6
- `_locales/vi/survey-design/appearance.mdx` — Task 7
- `_locales/vi/survey-design/advanced-features/dynamic-search.mdx` — Task 8
- `_locales/vi/survey-design/multi-language.mdx` — Task 9
- `_locales/vi/survey-design/operators-and-functions/functions.mdx` — Task 10
- `_locales/vi/survey-design/advanced-features/repeats.mdx` — Task 11
- `_locales/vi/survey-design/advanced-features/_meta.json` — Task 12

---

## Task 1: Create `local-database-search.mdx` in Vietnamese

**Files:**
- Create: `_locales/vi/survey-design/advanced-features/local-database-search.mdx`
- Reference (English source): `pages/survey-design/advanced-features/local-database-search.mdx`

- [ ] **Step 1: Write the full Vietnamese translation**

Create `_locales/vi/survey-design/advanced-features/local-database-search.mdx` with this exact content:

```mdx
---
title: "Tìm kiếm cơ sở dữ liệu nội bộ"
description: "Tìm kiếm cơ sở dữ liệu nội bộ truy vấn tệp SQLite .db được đóng gói bằng SQL thuần túy, cho phép tự động hoàn thành ngoại tuyến nhanh cho tập dữ liệu tĩnh lớn."
---

import { Callout } from 'nextra/components'

**Tìm kiếm cơ sở dữ liệu nội bộ** cho phép trường `select_one` hoặc `text` truy vấn tệp SQLite `.db` được đóng gói trong gói media của biểu mẫu — hoàn toàn ngoại tuyến, không cần kết nối mạng. Đây là cách tiếp cận đúng khi danh sách lựa chọn lớn và tĩnh (ví dụ: danh sách quốc gia các làng xã, cơ sở y tế, hay đơn vị hành chính) và không thể đảm bảo kết nối mạng.

| Cách tiếp cận | Nguồn dữ liệu | Yêu cầu kết nối mạng |
|---|---|---|
| Tìm kiếm cơ sở dữ liệu nội bộ (`rawquery`) | Tệp `.db` đóng gói (SQLite) | Không |
| `search-api()` | REST API từ xa | Có |
| `search()` | Tệp CSV đóng gói | Không |

---

## Các biến thể appearance

Trường tự động hoàn thành được cấu hình qua cột `appearance`. Có ba biến thể:

| Biến thể | Ghi chú |
|---|---|
| `search-autocomplete-noedit(...)` | Tự động hoàn thành tiêu chuẩn — người điều tra phải chọn từ danh sách; không lưu nếu nhập tự do |
| `search-autocomplete-noedit-v2(...)` | Biến thể được khuyến nghị — hành vi tương tự nhưng dùng engine hiển thị cập nhật với hiệu suất tốt hơn trên tập kết quả lớn |
| `search(...)` | Khớp đơn giản theo cột trong tệp CSV đóng gói; **không** hỗ trợ SQL thuần — liệt kê ở đây để so sánh |

<Callout type="info">
`search-autocomplete-noedit` là alias — khi phân tích cú pháp, ứng dụng thay thế bằng tên hàm nội bộ `searchAutocompleteNoedit`. Dùng cách viết nào cũng được trong XLSForm; cả hai đều hoạt động.
</Callout>

---

## Nguồn dữ liệu `rawquery`

Để chạy truy vấn SQL đối với tệp `.db`, truyền `'rawquery'` làm đối số đầu tiên của hàm appearance. Cú pháp đầy đủ:

```
search-autocomplete-noedit-v2(
  'rawquery',
  <db_path>,
  '[display_col]',
  'value_col',
  'SELECT ...',
  param1, param2, ...
)
```

### Tham số

| Vị trí | Tham số | Mô tả |
|---|---|---|
| 1 | `'rawquery'` | Chuỗi ký tự — báo cho ứng dụng thực thi SQL trực tiếp |
| 2 | `db_path` | Đường dẫn đến tệp SQLite, định dạng `<dir>/<file>.db::tableName`. Phần `::tableName` bị cắt khi mở tệp; tên bảng dùng bên trong SQL |
| 3 | `'[display_col]'` | Cột hiển thị trong danh sách thả xuống. Dấu `[ ]` bị cắt khi chạy |
| 4 | `'value_col'` | Cột có giá trị được lưu khi người điều tra chọn |
| 5 | `'SELECT ...'` | Câu lệnh SQLite SELECT bất kỳ. `SELECT DISTINCT` tự động được thêm nếu `DISTINCT` chưa có |
| 6+ | `param1, ...` | Tùy chọn. Giá trị gán cho placeholder `?` trong SQL, theo thứ tự. Nếu SQL có `?` nhưng không có tham số, trường trả về rỗng (bảo vệ khỏi thiếu đối số) |

### Quy ước `db_path`

Tệp cơ sở dữ liệu nằm bên trong thư mục media đóng gói của biểu mẫu. Khi chạy, `pulldata('app-api', 'family_path')` trả về đường dẫn thư mục đó. Xem [family_path](family-path) để biết cách thiết lập. Mẫu chuẩn:

```
concat(${family_path}, '/mydata.db::tableName')
```

Khi ứng dụng mở tệp, phần `::tableName` bị cắt và chỉ dùng đường dẫn tệp thuần. Tên bảng chỉ xuất hiện bên trong SQL.

---

## Ví dụ cơ bản — tra cứu tỉnh thành

Danh sách thả xuống tỉnh thành chỉ đọc, được hỗ trợ bởi tệp `vnxa3.db` đóng gói:

| type | name | label | appearance | calculation |
|---|---|---|---|---|
| calculate | family_path | | | `pulldata('app-api', 'family_path')` |
| select_one | province | Tỉnh/Thành phố | `search-autocomplete-noedit-v2('rawquery', concat(${family_path}, '/vnxa3.db::externalData'), '[provv]', 'provid', 'SELECT provv, provid FROM externalData WHERE rta_filter = "1"')` | |

Giá trị cột `appearance` (mở rộng để dễ đọc):

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[provv]', 'provid',
  'SELECT provv, provid FROM externalData WHERE rta_filter = "1"')
```

- Nhãn hiển thị lấy từ cột `provv`.
- Giá trị lưu lấy từ cột `provid`.
- Chỉ hiển thị các hàng có `rta_filter = "1"`.

---

## Truy vấn có tham số

Dùng placeholder `?` trong SQL và truyền các tham chiếu trường tương ứng làm đối số bổ sung (vị trí 6 trở đi). Đây là mẫu chuẩn cho select dạng cascade — ví dụ tải quận/huyện thuộc tỉnh đã chọn trước đó.

<Callout type="warning">
Nếu SQL có ít nhất một `?` nhưng không có đối số tham số, trường trả về tập kết quả rỗng. Điều này ngăn dữ liệu cũ hoặc không phân vùng hiển thị trước khi có lựa chọn cha.
</Callout>

### Ví dụ cascade quận/huyện

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[distv]', 'distid',
  'SELECT distv, distid FROM externalData
   WHERE provid = ? AND rta_filter = "1"',
  ${province})
```

Giá trị `${province}` gán cho `?` đầu tiên. Trường để trống cho đến khi người điều tra chọn tỉnh.

### Ví dụ hai tham số — cascade xã/phường

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[commv]', 'commid',
  'SELECT commv, commid FROM externalData
   WHERE provid = ? AND distid = ? AND rta_filter = "1"',
  ${province}, ${district})
```

Tham số gán theo vị trí: `${province}` → `?` đầu tiên, `${district}` → `?` thứ hai.

---

## UNION SELECT cho giá trị đặc biệt

Đưa các hàng tổng hợp — như "Không biết" hoặc "Từ chối trả lời" — trực tiếp vào SQL bằng `UNION SELECT`:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[provv]', 'provid',
  'SELECT provv, provid FROM externalData WHERE rta_filter = "1"
   UNION SELECT "<i>Không biết</i>", "888"')
```

Quy ước dùng trong các biểu mẫu RTSurvey:

| Mã | Ý nghĩa |
|---|---|
| `888` | Không biết |
| `999` | Từ chối trả lời |

Các thẻ HTML như `<i>` trong chuỗi hiển thị được ứng dụng render — bạn có thể dùng chúng để phân biệt trực quan các tùy chọn đặc biệt.

---

## Hiển thị đa ngôn ngữ

Lưu nhãn theo ngôn ngữ trong các cột riêng (ví dụ: `label_vi`, `label_en`) và chọn cột phù hợp dựa trên trường ngôn ngữ trong biểu mẫu:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  '[label_vi]', 'provid',
  'SELECT label_vi, label_en, provid FROM externalData
   WHERE rta_filter = "1"')
```

Để chuyển cột động dựa trên trường `${language}`, dùng biểu thức `if()` trên tham số cột hiển thị:

```
search-autocomplete-noedit-v2('rawquery',
  concat(${family_path}, '/vnxa3.db::externalData'),
  if(${language} = 'vi', '[label_vi]', '[label_en]'),
  'provid',
  'SELECT label_vi, label_en, provid FROM externalData
   WHERE rta_filter = "1"')
```

<Callout type="info">
Tham số cột hiển thị được tính toán trước khi truy vấn chạy. Chỉ tên cột (không có dấu ngoặc) được truyền cho SQL engine; dấu ngoặc chỉ là ký hiệu phân biệt bị cắt khi phân tích cú pháp.
</Callout>

---

## Xác thực lựa chọn thực sự

Khi trường cho phép các giá trị đặc biệt như 888 hoặc 999, kiểm tra `required = yes` thông thường là chưa đủ — nó được thỏa mãn ngay cả khi người điều tra chọn "Không biết". Dùng constraint `selected-at(., 0) != -997` để xác minh giá trị lưu là lựa chọn thực sự, không phải sentinel nội bộ `-997` (giá trị "chưa chọn gì"):

| cột | giá trị |
|---|---|
| constraint | `selected-at(., 0) != -997` |
| constraint_message | Vui lòng chọn một tùy chọn hợp lệ |

Giá trị `-997` là mã nội bộ RTSurvey lưu khi chưa có mục nào được chọn từ danh sách tự động hoàn thành. Lựa chọn 888 hoặc 999 vẫn là lựa chọn có chủ ý và vượt qua kiểm tra này.

Để yêu cầu thêm giá trị thực (không phải giá trị đặc biệt), mở rộng constraint:

```
selected-at(., 0) != -997 and selected-at(., 0) != '888' and selected-at(., 0) != '999'
```

---

## So sánh: cơ sở dữ liệu nội bộ so với các phương pháp tìm kiếm khác

| Tính năng | Tự động hoàn thành `rawquery` | `search-api()` | `search()` CSV | Lựa chọn CSV thông thường |
|---|---|---|---|---|
| Nguồn dữ liệu | `.db` đóng gói (SQLite) | REST API từ xa | CSV đóng gói | Bảng choices |
| Hoạt động ngoại tuyến | Có | Không | Có | Có |
| Hỗ trợ SQL thuần | Có | Không | Không | Không |
| Lọc cascade | Có — tham số `?` | Qua request body | Hạn chế | Không |
| Kích thước tập dữ liệu | Rất lớn (hàng triệu hàng) | Không giới hạn (phía server) | Trung bình (vài chục nghìn) | Nhỏ |
| Hàng đặc biệt được đưa vào | Có — `UNION SELECT` | Không | Không | Có (thủ công) |
| Độ phức tạp thiết lập | Trung bình — cần tệp `.db` đóng gói | Cao — cần server API | Thấp | Không có |

---

## Giới hạn

- Tệp `.db` phải được đóng gói trong gói media của biểu mẫu trước khi triển khai. Cập nhật động cơ sở dữ liệu yêu cầu triển khai biểu mẫu mới.
- SQL được thực thi nguyên văn trên thiết bị. Không có kiểm tra bảo mật phía server — tránh xây dựng SQL từ văn bản nhập tự do của người điều tra.
- Chỉ hỗ trợ câu lệnh `SELECT`. `INSERT`, `UPDATE` và `DELETE` không được phép.
- Truy vấn rất phức tạp (chuỗi `UNION` dài, nhiều join) có thể chậm trên thiết bị Android cấp thấp.
- Các biến thể `search-autocomplete-noedit` không cho phép người điều tra lưu giá trị không có trong tập kết quả. Nếu cần nhập tự do, dùng trường `text` riêng.
- `SELECT DISTINCT` chỉ tự động thêm khi `DISTINCT` chưa có trong truy vấn. Nếu bạn viết `SELECT DISTINCT` tường minh, nó sẽ không bị nhân đôi.
```

- [ ] **Step 2: Verify file was created**

Confirm `_locales/vi/survey-design/advanced-features/local-database-search.mdx` exists and has the expected frontmatter.

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/local-database-search.mdx
git commit -m "i18n(vi): add Vietnamese translation for local-database-search"
```

---

## Task 2: Create `audio-recording.mdx` in Vietnamese

**Files:**
- Create: `_locales/vi/survey-design/advanced-features/audio-recording.mdx`
- Reference (English source): `pages/survey-design/advanced-features/audio-recording.mdx`

- [ ] **Step 1: Write the full Vietnamese translation**

Create `_locales/vi/survey-design/advanced-features/audio-recording.mdx` with this exact content:

```mdx
---
title: "Ghi âm"
description: "Ghi âm môi trường hoặc phỏng vấn trong quá trình thu thập dữ liệu khảo sát bằng appearance audio-start và audio-end trên trường text."
---

Ghi âm cho phép biểu mẫu thu âm âm thanh một cách thầm lặng hoặc hiển thị trong một phần của khảo sát. Tính năng này hữu ích để ghi lại các cuộc phỏng vấn, âm thanh xung quanh trong quá trình quan sát thực địa, hoặc câu trả lời bằng lời nói bổ sung cho các câu trả lời có cấu trúc.

---

import { Callout } from 'nextra/components'

<Callout type="warning">
**Chỉ dành cho ứng dụng di động.** Ghi âm yêu cầu ứng dụng di động rtSurvey. Trên biểu mẫu web, appearance `audio-start` và `audio-end` bị bỏ qua âm thầm — không có ghi âm nào diễn ra và không có lỗi nào hiển thị. Luôn kiểm tra trực tiếp trên thiết bị khi cần ghi âm.
</Callout>

---

## Cách hoạt động

Ghi âm được điều khiển bởi hai trường `text` đóng vai trò là **điểm đánh dấu**:

- Trường có appearance `audio-start` bắt đầu ghi âm khi người điều tra đến trường đó.
- Trường có appearance `audio-end` dừng ghi âm và lưu tệp âm thanh vào bản nộp.

Cả hai trường đánh dấu đều có kiểu `text`. Chúng thường được ẩn khỏi người điều tra (dùng `relevant = false` hoặc đặt ở vị trí không tương tác), mặc dù có thể hiển thị. Âm thanh được ghi đính kèm vào bản nộp dưới dạng tệp liên kết với trường `audio-end`.

---

## Ví dụ cơ bản

| type | name | label | appearance |
|------|------|-------|------------|
| text | audio_s_a1 | | `audio-start` |
| text | q_name | Tên người trả lời | |
| text | q_occupation | Nghề nghiệp | |
| integer | q_age | Tuổi | |
| text | audio_e_a1 | | `audio-end` |

Ứng dụng bắt đầu ghi âm khi người điều tra đến `audio_s_a1` và dừng khi đến `audio_e_a1`. Tất cả câu hỏi giữa hai điểm đánh dấu đều được ghi âm.

---

## Ghi âm thầm lặng: `audio-start invisible`

Mặc định, ứng dụng di động hiển thị chỉ báo đang ghi âm khi thu âm. Thêm `invisible` vào appearance sẽ ẩn chỉ báo này, ghi âm diễn ra mà không có tín hiệu hiển thị nào cho người trả lời.

| type | name | label | appearance |
|------|------|-------|------------|
| text | audio_s_a1 | | `audio-start invisible` |
| text | q_consent | Bạn có đồng ý tham gia không? | |
| text | q_feedback | Phản hồi của bạn | |
| text | audio_e_a1 | | `audio-end` |

Chỉ dùng `invisible` khi các yêu cầu tiết lộ đã được đáp ứng qua phương tiện khác (ví dụ: trường chấp thuận bằng văn bản riêng trước phần ghi âm).

---

## Quy ước đặt tên

Các biểu mẫu sản xuất dùng mẫu đặt tên nhất quán cho các trường đánh dấu:

```
audio_s_{phần}{n}   — điểm đánh dấu bắt đầu
audio_e_{phần}{n}   — điểm đánh dấu kết thúc
```

Trong đó `{phần}` là nhãn ngắn cho phần biểu mẫu và `{n}` là số thứ tự trong phần đó.

| Tên trường | Vai trò | Ý nghĩa |
|------------|---------|---------|
| `audio_s_a1` | Bắt đầu | Ghi âm đầu tiên trong phần A |
| `audio_e_a1` | Kết thúc | Kết thúc ghi âm đầu tiên trong phần A |
| `audio_s_b1` | Bắt đầu | Ghi âm đầu tiên trong phần B |
| `audio_e_b1` | Kết thúc | Kết thúc ghi âm đầu tiên trong phần B |
| `audio_s_a2` | Bắt đầu | Ghi âm thứ hai trong phần A |
| `audio_e_a2` | Kết thúc | Kết thúc ghi âm thứ hai trong phần A |

Tuân theo quy ước này giúp dễ xác định ranh giới ghi âm khi xem lại định nghĩa biểu mẫu và dữ liệu bản nộp.

---

## Lưu trữ và truy xuất

Khi người điều tra đến trường `audio-end`, ứng dụng hoàn thiện tệp âm thanh và đính kèm vào bản nộp. Tệp sẽ:

- Được lưu dưới dạng tệp đính kèm âm thanh trong bản nộp, liên kết với tên trường `audio-end`.
- Có thể xem trong trình xem bản nộp backend rtSurvey cùng với các tệp đính kèm media khác.
- Có thể tải xuống qua xuất bản nộp chuẩn — tệp âm thanh xuất hiện trong cột media tương ứng với tên trường `audio-end`.

Định dạng tệp và tốc độ bit phụ thuộc vào thiết bị và phiên bản ứng dụng.

---

## Nhiều phần ghi âm

Một biểu mẫu có thể chứa nhiều phần ghi âm không chồng lấp nhau. Mỗi cặp điểm đánh dấu `audio-start` / `audio-end` phải được chứa hoàn toàn — các phần không được đan xen nhau.

| type | name | label | appearance |
|------|------|-------|------------|
| text | audio_s_a1 | | `audio-start` |
| text | q_intro | Giới thiệu | |
| text | audio_e_a1 | | `audio-end` |
| note | section_break | — | |
| text | audio_s_b1 | | `audio-start invisible` |
| text | q_detail | Chi tiết | |
| text | audio_e_b1 | | `audio-end` |

Mỗi phần tạo ra một tệp âm thanh riêng đính kèm vào trường `audio-end` tương ứng.

---

## Giới hạn

- **Chỉ dành cho ứng dụng di động.** Tính năng không được hỗ trợ trên biểu mẫu web. `audio-start` và `audio-end` bị bỏ qua âm thầm trên trình duyệt.
- **Không được lồng nhau.** Các phần ghi âm không được chồng lấp. Bắt đầu ghi âm mới trước khi đạt điểm đánh dấu `audio-end` trước đó không được hỗ trợ.
- **Kiểu trường phải là `text`.** Dùng `audio-start` hoặc `audio-end` trên kiểu câu hỏi khác không được hỗ trợ.
- **Kích thước tải lên.** Ghi âm dài tạo ra tệp lớn. Lưu ý giới hạn kích thước bản nộp và điều kiện mạng ngoài thực địa.
- **Không tạm dừng giữa chừng.** Ghi âm chạy liên tục từ điểm đánh dấu bắt đầu đến điểm kết thúc; không có cơ chế tạm dừng và tiếp tục trong một phần.
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/audio-recording.mdx
git commit -m "i18n(vi): add Vietnamese translation for audio-recording"
```

---

## Task 3: Create `form-navigation.mdx` in Vietnamese

**Files:**
- Create: `_locales/vi/survey-design/advanced-features/form-navigation.mdx`
- Reference (English source): `pages/survey-design/advanced-features/form-navigation.mdx`

- [ ] **Step 1: Write the full Vietnamese translation**

Create `_locales/vi/survey-design/advanced-features/form-navigation.mdx` with this exact content:

```mdx
---
title: "Điều hướng biểu mẫu"
description: "Dùng giá trị appearance SaveFinalizedExit và SaveIncompleteExit để hiển thị nút thoát có kiểu dáng, lưu và thoát biểu mẫu."
---

**Điều hướng biểu mẫu** là các giá trị appearance đặt trên trường `note` (hoặc `text`) hiển thị dưới dạng nút toàn chiều rộng có kiểu dáng ở cuối khảo sát. Chúng cho phép người điều tra lưu bản nộp và thoát biểu mẫu chỉ với một lần chạm — hoặc là bản ghi đã hoàn thành (finalized) hoặc là bản nháp (incomplete).

---

## `SaveFinalizedExit<#COLOR/>`

Hiển thị nút **lưu bản nộp dưới dạng finalized** và thoát biểu mẫu. Nhãn nút lấy từ cột `label` của trường.

| Cột XLSForm | Giá trị |
|----------------|-------|
| `type` | `note` |
| `name` | tên duy nhất bất kỳ (ví dụ: `btn_finish`) |
| `label` | văn bản hiển thị trên nút |
| `appearance` | `SaveFinalizedExit<#RRGGBB/> toc-hide` |

Bản nộp được đánh dấu là bản ghi cuối cùng, hoàn chỉnh. Tương đương với việc nhấn nút nộp tích hợp sẵn.

---

## `SaveIncompleteExit<#COLOR/>`

Hiển thị nút **lưu bản nộp dưới dạng incomplete (nháp)** và thoát biểu mẫu. Người điều tra có thể quay lại sau và tiếp tục điền.

| Cột XLSForm | Giá trị |
|----------------|-------|
| `type` | `note` |
| `name` | tên duy nhất bất kỳ (ví dụ: `btn_pause`) |
| `label` | văn bản hiển thị trên nút |
| `appearance` | `SaveIncompleteExit<#RRGGBB/> toc-hide` |

---

## Cú pháp màu sắc

Cả hai appearance đều chấp nhận màu nội tuyến theo định dạng `<#RRGGBB/>`:

- `#` theo sau bởi đúng **6 chữ số hex** (chữ hoa hoặc chữ thường)
- Dấu đóng `/>` là **bắt buộc** — bỏ qua sẽ gây lỗi phân tích
- Ví dụ: `<#04B404/>` (xanh lá), `<#EDC602/>` (vàng hổ phách), `<#D9534F/>` (đỏ)

Màu sắc điều khiển nền nút. Màu chữ được ứng dụng tự động xác định.

---

## Ví dụ

Hai trường sau đặt ở cuối biểu mẫu tạo ra nút **Nộp** màu xanh lá và nút **Lưu nháp** màu vàng hổ phách:

| type | name | label | appearance |
|------|------|-------|------------|
| note | btn_finish | Nộp | `SaveFinalizedExit<#04B404/> toc-hide` |
| note | btn_pause | Lưu nháp | `SaveIncompleteExit<#EDC602/> toc-hide` |

---

## `toc-hide` — loại trừ nút khỏi mục lục

Token appearance `toc-hide` báo cho rtSurvey loại trừ một trường khỏi **mục lục** (danh sách tổng quan câu hỏi) của biểu mẫu. Các nút điều hướng không phải câu hỏi, nên chúng không nên xuất hiện trong mục lục.

Luôn thêm `toc-hide` sau appearance thoát:

```
SaveFinalizedExit<#04B404/> toc-hide
SaveIncompleteExit<#EDC602/> toc-hide
```

Xem [Appearance — toc-hide](../appearance#group-and-navigation) để biết tài liệu tham khảo toc-hide.

---

## Quy ước đặt vị trí

Tuân theo các quy ước sau khi thêm điều hướng vào biểu mẫu:

- Đặt cả hai nút ở **cuối biểu mẫu**, sau tất cả câu hỏi và nhóm.
- Luôn bao gồm **cả hai** nút cùng nhau — một finalized và một incomplete — để người điều tra luôn có cách thoát bất kể trạng thái hoàn thành.
- Dùng cột `relevant` trên nút thoát finalized nếu chỉ được phép nộp khi đáp ứng điều kiện nhất định (ví dụ: một phần bắt buộc đã hoàn thành). Nút thoát incomplete thường nên **luôn hiển thị**.

---

## Thoát finalized có điều kiện

Dùng cột `relevant` để kiểm soát khi nào nút thoát finalized hiển thị. Nút thoát incomplete nên luôn hiển thị vô điều kiện để người điều tra luôn có thể tạm dừng và quay lại.

| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| note | btn_finish | Nộp | `SaveFinalizedExit<#04B404/> toc-hide` | `${consent} = 'yes' and ${section_a_complete} = '1'` |
| note | btn_pause | Lưu nháp | `SaveIncompleteExit<#EDC602/> toc-hide` | |

Trong ví dụ này, nút **Nộp** chỉ xuất hiện khi người điều tra đã đồng ý và đánh dấu phần A là hoàn thành. Nút **Lưu nháp** luôn có mặt.

---

## Giới hạn

- **Kiểu trường phải là `note` hoặc `text`.** Dùng các appearance này trên kiểu câu hỏi khác không được hỗ trợ.
- **Chỉ hex 6 chữ số.** Hex viết tắt (`<#FFF/>`) và màu được đặt tên không được hỗ trợ — luôn dùng định dạng 6 chữ số đầy đủ (ví dụ: `<#FFFFFF/>`).
- **Cột label là văn bản nút.** Cột `hint` bị bỏ qua với các trường này; chỉ `label` được hiển thị.
- **Nên có cả hai nút.** Bỏ nút thoát incomplete khiến người điều tra không có cách tạm dừng giữa chừng.
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/form-navigation.mdx
git commit -m "i18n(vi): add Vietnamese translation for form-navigation"
```

---

## Task 4: Create `family-path.mdx` in Vietnamese

**Files:**
- Create: `_locales/vi/survey-design/advanced-features/family-path.mdx`
- Reference (English source): `pages/survey-design/advanced-features/family-path.mdx`

- [ ] **Step 1: Write the full Vietnamese translation**

Create `_locales/vi/survey-design/advanced-features/family-path.mdx` with this exact content:

```mdx
---
title: "family_path"
description: "family_path là trường calculate theo quy ước, trả về đường dẫn thư mục media đóng gói của biểu mẫu khi chạy — bắt buộc với mọi biểu mẫu dùng tra cứu cơ sở dữ liệu nội bộ hoặc tìm kiếm dựa trên tệp."
---

import { Callout } from 'nextra/components'

`family_path` là trường calculate theo quy ước, lưu đường dẫn đến thư mục media đóng gói của biểu mẫu. Mọi biểu mẫu thực hiện tra cứu cơ sở dữ liệu nội bộ bằng `rawquery`, `pulldata`, hoặc `search()` đều phải có trường này — nếu không, các đường dẫn tệp không thể giải quyết được và tra cứu sẽ âm thầm trả về rỗng.

---

## Trường calculate

Thêm hàng này gần đầu bảng survey, sau các trường meta và trước câu hỏi đầu tiên dùng tệp cơ sở dữ liệu:

| type | name | label | calculation |
|---|---|---|---|
| calculate | `family_path` | | `pulldata('app-api', 'family_path')` |

Trường này không lưu giá trị hiển thị và không cần nhãn. Đây là điều kiện tiên quyết âm thầm cho tất cả việc xây dựng đường dẫn theo sau.

---

## Tại sao cần thiết

RTSurvey đóng gói media của biểu mẫu — cơ sở dữ liệu SQLite, hình ảnh, âm thanh — bên trong thư mục riêng theo biểu mẫu trên thiết bị. Đường dẫn chính xác khác nhau giữa các nền tảng (Android, iOS, web) và giữa các thiết bị.

Khi chạy, ứng dụng tự động điền `family_path`. Một giá trị đã giải quyết điển hình trông như:

```
resources/familyMedia/Phuong_Person_Test
```

Vì đường dẫn phụ thuộc vào nền tảng và được xác định khi khởi chạy, nó không thể được cứng hóa trong biểu mẫu. `pulldata('app-api', 'family_path')` là cách duy nhất đáng tin cậy để lấy nó.

---

## Cách dùng trong đường dẫn

Sau khi `family_path` được định nghĩa, xây dựng đường dẫn tệp đầy đủ với `concat()`:

```
concat(${family_path}, '/file.db::tableName')
```

Phần `::tableName` bị cắt khi ứng dụng mở tệp; tên bảng chỉ dùng bên trong truy vấn SQL.

---

## Nơi family_path được dùng

`family_path` là bắt buộc trong đối số đường dẫn bất cứ khi nào tham chiếu đến tệp đóng gói:

- **Tìm kiếm cơ sở dữ liệu nội bộ** — đối số `db_path` của `search-autocomplete-noedit-v2('rawquery', ...)` phải được xây dựng với `concat(${family_path}, ...)`. Xem [Tìm kiếm cơ sở dữ liệu nội bộ](local-database-search) để biết chi tiết sử dụng đầy đủ.
- **`pulldata` rawquery** — mọi lời gọi `pulldata('rawquery', ...)` đọc từ tệp `.db` dùng cùng mẫu `concat()`.
- **`search()` với tệp nội bộ** — appearance dynamic-search tải từ CSV hoặc DB đóng gói cũng dựa vào `family_path` cho tham chiếu tệp.

---

## Vị trí trong biểu mẫu

`family_path` phải xuất hiện **trước trường đầu tiên tham chiếu nó**. Vị trí được khuyến nghị là ngay sau nhóm meta:

| type | name | label | calculation |
|---|---|---|---|
| begin_group | meta | | |
| deviceid | deviceid | | |
| start | start | | |
| end | end | | |
| end_group | | | |
| calculate | `family_path` | | `pulldata('app-api', 'family_path')` |
| select_one | province | Tỉnh/Thành phố | *(appearance rawquery tham chiếu `${family_path}`)* |

<Callout type="warning">
Nếu `family_path` bị thiếu trong biểu mẫu, hoặc được đặt sau trường `rawquery` / `search()` đầu tiên tham chiếu nó, tất cả tra cứu đối với các tệp đóng gói sẽ âm thầm trả về rỗng. Không có thông báo lỗi — tự động hoàn thành đơn giản không hiển thị kết quả.
</Callout>

---

## Nhiều tệp cơ sở dữ liệu

Một biểu mẫu có thể dùng nhiều tệp `.db`. Mỗi đường dẫn được xây dựng độc lập với `concat()`:

```
concat(${family_path}, '/locations.db::externalData')
concat(${family_path}, '/health_facilities.db::facilities')
concat(${family_path}, '/household_list.db::households')
```

Định nghĩa `family_path` một lần; tham chiếu trong bao nhiêu trường tùy ý.

---

## Xác minh trong quá trình phát triển

Thêm trường `note` tạm thời bên dưới `family_path` để kiểm tra giá trị đã giải quyết trên thiết bị:

| type | name | label | calculation |
|---|---|---|---|
| calculate | `family_path` | | `pulldata('app-api', 'family_path')` |
| note | family_path_check | `Đường dẫn: ${family_path}` | |

Note sẽ hiển thị đường dẫn thực sự đã giải quyết trong quá trình kiểm thử. Xóa nó trước khi triển khai biểu mẫu cuối cùng.
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/family-path.mdx
git commit -m "i18n(vi): add Vietnamese translation for family-path"
```

---

## Task 5: Create `pulldata.mdx` in Vietnamese

**Files:**
- Create: `_locales/vi/survey-design/operators-and-functions/pulldata.mdx`
- Reference (English source): `pages/survey-design/operators-and-functions/pulldata.mdx`

Note: This file does **not** exist yet in the Vietnamese locale. Create it as a full translation of the English source.

- [ ] **Step 1: Write the full Vietnamese translation**

Create `_locales/vi/survey-design/operators-and-functions/pulldata.mdx` with this exact content — translate all prose, keep all code blocks, keep all column names, keep all parameter names unchanged:

```mdx
---
title: "pulldata()"
description: "Hàm pulldata() lấy giá trị từ tệp CSV bên ngoài đính kèm với biểu mẫu, khớp cột khóa với giá trị khóa và trả về cột kết quả tương ứng."
---

import { Callout } from 'nextra/components'

Hàm `pulldata()` lấy giá trị từ tệp CSV đính kèm với biểu mẫu. Cho một tên tệp, cột kết quả cần trả về, cột để khớp, và giá trị khóa, nó trả về ô tại giao điểm của hàng khớp và cột kết quả.

```
pulldata('filename.csv', 'result_column', 'key_column', ${key_field})
```

| Vị trí | Tham số | Mô tả |
|----------|-----------|-------------|
| 1 | Tên tệp | Tên tệp media CSV (cùng tên dùng trong `select_one_from_file`) |
| 2 | Cột kết quả | Cột có giá trị cần trả về |
| 3 | Cột khóa | Cột để khớp |
| 4 | Giá trị khóa | Giá trị cần khớp — thường là tham chiếu trường như `${field}` |

Hàm trả về chuỗi rỗng nếu không tìm thấy kết quả khớp.

---

## Điều kiện tiên quyết

Tệp CSV phải được đính kèm với biểu mẫu dưới dạng **tệp media**. Tệp được tham chiếu bởi `pulldata()` cũng có thể dùng làm danh sách lựa chọn cho `select_one_from_file`.

**Ví dụ CSV — `staff.csv`:**

```
name,id,department,phone
Alice,S001,Health,+1234567890
Bob,S002,Education,+0987654321
Carol,S003,Health,+1122334455
```

---

## Ví dụ cơ bản

Tra cứu phòng ban và số điện thoại của nhân viên từ ID của họ:

**survey:**

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file staff.csv | staff_id | Chọn nhân viên | |
| calculate | dept | | `pulldata('staff.csv', 'department', 'name', ${staff_id})` |
| calculate | phone | | `pulldata('staff.csv', 'phone', 'name', ${staff_id})` |
| note | dept_note | Phòng ban: `${dept}` — Điện thoại: `${phone}` | |

<Callout type="info">
Cột `name` trong CSV `select_one_from_file` là giá trị được lưu. Khi người điều tra chọn "Alice", `${staff_id}` có giá trị `"Alice"`, mà `pulldata()` dùng làm khóa để lấy phòng ban và điện thoại của cô ấy.
</Callout>

---

## Lấy nhãn của lựa chọn đã chọn

Trường `select_one_from_file` lưu giá trị `name`. Để hiển thị nhãn có thể đọc được, dùng `pulldata()` để tra cứu:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file villages.csv | village | Chọn làng/xã | |
| calculate | village_label | | `pulldata('villages.csv', 'label', 'name', ${village})` |
| note | confirm | Bạn đã chọn: `${village_label}` | |

---

## Nhiều tra cứu từ một lựa chọn

Bạn có thể gọi `pulldata()` nhiều lần trên cùng một tệp để lấy các cột khác nhau cho cùng hàng đã chọn:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file facilities.csv | facility | Chọn cơ sở | |
| calculate | fac_type | | `pulldata('facilities.csv', 'type', 'name', ${facility})` |
| calculate | fac_district | | `pulldata('facilities.csv', 'district', 'name', ${facility})` |
| calculate | fac_beds | | `pulldata('facilities.csv', 'beds', 'name', ${facility})` |

---

## Dùng pulldata trong relevant và constraint

`pulldata()` có thể dùng trong cột `relevant` và `constraint` để áp dụng logic dựa trên giá trị được tra cứu:

| type | name | label | relevant | constraint |
|------|------|-------|----------|------------|
| select_one_from_file facilities.csv | facility | Chọn cơ sở | | |
| integer | bed_count | Số giường đang sử dụng | | `. <= number(pulldata('facilities.csv', 'beds', 'name', ${facility}))` |

---

## Dùng pulldata với `once()`

Để tính `pulldata()` chỉ một lần khi tải (ngăn tính lại khi trường khóa thay đổi sau lần nhập đầu), bọc trong `once()`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | initial_dept | | `once(pulldata('staff.csv', 'department', 'name', ${staff_id}))` |

---

## Thực hành tốt

1. Cột khóa trong CSV phải khớp với cột `name` dùng trong `select_one_from_file` — chúng phải là cùng giá trị.
2. Tên cột trong CSV phân biệt chữ hoa/thường — `Department` và `department` là hai cột khác nhau.
3. Nếu giá trị khóa không tìm thấy, `pulldata()` trả về chuỗi rỗng — dùng `if(${field} != '', pulldata(...), '')` để bảo vệ khỏi lựa chọn rỗng.
4. Giữ tệp CSV nhỏ nếu có thể — tệp lớn làm tăng thời gian tải biểu mẫu trên kết nối băng thông thấp.
5. Với dữ liệu thay đổi giữa các vòng thu thập, cập nhật tệp media CSV bằng cách tải lên phiên bản biểu mẫu mới.

## Giới hạn

- `pulldata()` chỉ khớp **hàng đầu tiên** có cột khóa bằng giá trị khóa — giá trị khóa trùng lặp trong CSV không được hỗ trợ.
- Tệp CSV phải được đính kèm với biểu mẫu trước khi triển khai; không thể lấy từ URL khi chạy.
- Giá trị số được trả về bởi `pulldata()` là chuỗi — bọc trong `number()` khi dùng trong phép tính: `number(pulldata(...))`.

<Callout type="info">
rtSurvey cũng hỗ trợ các dạng mở rộng của `pulldata()` để đọc metadata thiết bị, trường JWT và dữ liệu JSON. Xem [App API](../app-api) để biết về `pulldata('app-api', ...)` và trang [Call API](../advanced-features/call-api) để biết về các mẫu tra cứu dựa trên JSON.
</Callout>

---

## Các biến thể pulldata() mở rộng

Ngoài tra cứu CSV, `pulldata()` hỗ trợ nhiều nguồn dữ liệu bổ sung bằng cách thay đổi đối số đầu tiên.

### `pulldata('app-api', key)`

Đọc metadata thiết bị, thuộc tính người dùng và ngữ cảnh ứng dụng. Xem tài liệu tham khảo đầy đủ trên trang [App API](../app-api).

```
pulldata('app-api', 'user.name')
pulldata('app-api', 'serverTime')
pulldata('app-api', 'projectCode')
```

### `pulldata('json', jsonString, jsonpath)`

Phân tích cú pháp chuỗi JSON nội tuyến và trích xuất giá trị bằng biểu thức JSONPath. Hữu ích khi có literal JSON nhúng trong biểu mẫu.

```
pulldata('json', '{"status":"active","code":42}', '$.code')
```

Trả về giá trị đã khớp dưới dạng chuỗi, hoặc chuỗi rỗng nếu không tìm thấy.

### `pulldata('jsonpath', fieldRef, jsonpath)`

Trích xuất giá trị từ chuỗi JSON lưu trong trường khác bằng biểu thức JSONPath. Tương đương với `substr-jsonpath(${field}, jsonpath)`.

```
pulldata('jsonpath', ${api_raw}, '$.data.id')
```

### `pulldata('jwt', tokenField, claimName)`

Giải mã token JWT lưu trong trường và trả về giá trị của một claim cụ thể từ payload.

```
pulldata('jwt', ${auth_token}, 'sub')
pulldata('jwt', ${auth_token}, 'exp')
```

Trả về chuỗi rỗng nếu token không hợp lệ hoặc claim không có.

### `pulldata('instanceid')`

Trả về ID instance duy nhất của bản nộp hiện tại. Tương đương với trường meta `instanceID`.

```
pulldata('instanceid')
```

### `pulldata('mapping', value, mappingName)`

Ánh xạ giá trị sang giá trị khác bằng bảng ánh xạ được đặt tên định nghĩa trong cấu hình biểu mẫu.

```
pulldata('mapping', ${district_code}, 'district_names')
```

Trả về giá trị được ánh xạ, hoặc chuỗi rỗng nếu không có ánh xạ nào khớp.

### `pulldata('options', optionName)`

Đọc tùy chọn cấu hình biểu mẫu theo tên.

```
pulldata('options', 'max_household_size')
```

### `pulldata('rawquery', path, sql, param1, ...)`

Thực thi `SELECT` SQL đối với tệp SQLite `.db` đóng gói và trả về giá trị từ cột đầu tiên của hàng đầu tiên khớp. Các tham số sau chuỗi SQL được thay thế theo thứ tự cho placeholder `?`.

| Vị trí | Tham số | Mô tả |
|----------|-----------|-------------|
| 1 | `'rawquery'` | Chuỗi ký tự xác định biến thể này |
| 2 | path | Đường dẫn tệp theo định dạng `concat(${family_path}, '/file.db::tableName')` |
| 3 | SQL | Câu lệnh `SELECT` dùng `?` làm placeholder vị trí |
| 4+ | params | Giá trị thay thế cho mỗi `?` theo thứ tự — thường là tham chiếu trường như `${field}` |

Trả về chuỗi rỗng nếu không có hàng nào khớp.

**Ví dụ — tra cứu tên tỉnh theo ID:**

```
pulldata('rawquery',
  concat(${family_path}, '/locations.db::provinces'),
  'SELECT name FROM provinces WHERE id = ?',
  ${province_id})
```

**Ví dụ — tra cứu tên phường/xã lọc theo cả mã tỉnh và quận/huyện:**

```
pulldata('rawquery',
  concat(${family_path}, '/locations.db::wards'),
  'SELECT name FROM wards WHERE province_code = ? AND district_code = ?',
  ${province_code},
  ${district_code})
```

Khác với `pulldata()` bốn đối số tiêu chuẩn khớp một cột khóa duy nhất trong tệp CSV, biến thể `rawquery` thực thi toàn bộ `SELECT` SQL đối với cơ sở dữ liệu SQLite, cho phép điều kiện `WHERE` nhiều cột và bất kỳ cột nào làm giá trị trả về.

<Callout type="info">
`rawquery` thường được dùng với trường tự động hoàn thành cho tra cứu địa điểm phân cấp. Xem [Tìm kiếm cơ sở dữ liệu nội bộ](../advanced-features/local-database-search) để biết chi tiết về xây dựng tệp `.db` và kết nối với `pulldata('rawquery', ...)`.
</Callout>
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/operators-and-functions/pulldata.mdx
git commit -m "i18n(vi): add Vietnamese translation for pulldata"
```

---

## Task 6: Add `autopull()` section to Vietnamese `html-styling.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/advanced-features/html-styling.mdx`
- Reference (English section added): `pages/survey-design/advanced-features/html-styling.mdx` — section "Dynamic HTML summaries with autopull()" which was inserted just before the "## Best Practices" heading

The Vietnamese file currently ends at the "## Thực hành tốt" heading. Insert the new section **immediately before** `## Thực hành tốt`.

- [ ] **Step 1: Read the current Vietnamese file to identify the insertion point**

Read `_locales/vi/survey-design/advanced-features/html-styling.mdx` and confirm the exact text of the line just before `## Thực hành tốt`.

- [ ] **Step 2: Insert the Vietnamese autopull section**

The old_string to replace is:
```
## Thực hành tốt
```

The new_string is:
```
## Tóm tắt HTML động với autopull()

`autopull()` là một appearance dùng trên trường `note` để hiển thị HTML được tạo ra và cập nhật trực tiếp trong biểu mẫu. Các tham chiếu trường bên trong `concat()` được thay thế bằng giá trị hiện tại và HTML được render lại mỗi khi có thay đổi. Dùng tính năng này cho màn hình tóm tắt cập nhật khi người điều tra điền dữ liệu.

### Cú pháp

```
autopull(concat('<html>...</html>'))
```

Các tham chiếu trường (`${field_name}`) bên trong `concat()` được thay thế bằng giá trị trực tiếp hiện tại và HTML được render lại mỗi khi có thay đổi.

### Giới hạn chiều cao với scroll-view()

Với tóm tắt dài hơn, kết hợp `autopull()` với `scroll-view(N%)` để giới hạn chiều cao panel và cho phép cuộn:

```
scroll-view(45%) autopull(concat('<html>...</html>'))
```

Giá trị `N%` là tương đối so với vùng biểu mẫu hiển thị. `45%` là giá trị mặc định thực tế cho panel tóm tắt ở giữa trang.

### Ví dụ đầy đủ — tóm tắt địa điểm hộ gia đình

Trường `note` sau render bảng hai cột hiển thị tỉnh, quận/huyện và xã/phường đã chọn. Tự động cập nhật bất cứ khi nào `${tinh_name}`, `${huyen_name}` hoặc `${xa_name}` thay đổi.

| type | name | label | appearance |
|------|------|-------|------------|
| note | location_summary | | `scroll-view(45%) autopull(concat('<html><table style="width:100%;border-collapse:collapse"><tr><td style="padding:4px;font-weight:bold">Tỉnh:</td><td style="padding:4px">', ${tinh_name}, '</td></tr><tr><td style="padding:4px;font-weight:bold">Quận/Huyện:</td><td style="padding:4px">', ${huyen_name}, '</td></tr><tr><td style="padding:4px;font-weight:bold">Xã/Phường:</td><td style="padding:4px">', ${xa_name}, '</td></tr></table></html>'))` |

Trong XLSForm, giá trị appearance được viết trong một ô:

```
scroll-view(45%) autopull(concat(
  '<html><table style="width:100%;border-collapse:collapse">
   <tr><td style="padding:4px;font-weight:bold">Tỉnh:</td>
       <td style="padding:4px">', ${tinh_name}, '</td></tr>
   <tr><td style="padding:4px;font-weight:bold">Quận/Huyện:</td>
       <td style="padding:4px">', ${huyen_name}, '</td></tr>
   <tr><td style="padding:4px;font-weight:bold">Xã/Phường:</td>
       <td style="padding:4px">', ${xa_name}, '</td></tr>
   </table></html>'))
```

### Inline styles

Thuộc tính `style="..."` nội tuyến trên bất kỳ phần tử HTML nào đều được hỗ trợ và là cách được khuyến nghị để áp dụng định dạng trực quan bên trong khối `autopull()`.

Các thứ sau **không** được hỗ trợ bên trong nội dung `autopull()`:

- Khối `<style>`
- Thẻ `<link>` stylesheet bên ngoài
- JavaScript (`<script>`)

### Khi nào dùng autopull()

| Trường hợp sử dụng | Ghi chú |
|----------|-------|
| Màn hình xem trước khi nộp | Hiển thị tất cả câu trả lời chính trên một panel trước khi người điều tra hoàn thành |
| Tổng chạy | Hiển thị tổng được tính cập nhật khi nhập số lượng |
| Panel tham chiếu hiển thị | Hiển thị giá trị tra cứu đã chọn (ví dụ: tên tỉnh) trong khi người điều tra điền các trường con |

---

## Thực hành tốt
```

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/html-styling.mdx
git commit -m "i18n(vi): add autopull() section to html-styling"
```

---

## Task 7: Add new appearance entries to Vietnamese `appearance.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/appearance.mdx`
- Reference (English additions): new entries in tables of `pages/survey-design/appearance.mdx` under sections "Group and navigation", "Input behaviour", "Layout", "Widgets", "Language switcher"

Read the current Vietnamese file first. Find the section "## rtSurvey Extended Appearance Attributes" (or its Vietnamese equivalent). The English file added new rows to these tables and added completely new table sections. Add the Vietnamese equivalents after the existing rtSurvey extended appearances content.

The English file has these new sections/rows added:
- Under "Group and navigation" table: `section`, `toc-hide`, `minilog`
- Under "Input behaviour" table: `proper`, `text-nolabel`, `inline-1line`, `popup`
- Under "Layout" table: `horizontal(N)`, `scroll-view(N%)`
- Under "Widgets" table: `rating_box-fill-{c1}-{c2}-{c3}-{c4}-{c5}`, `tagging-choices-noshow-v2-{c1}-{c2}-{c3}-{c4}-{c5}`
- New section "Language switcher": `change_language-{colors} default('lang')`

- [ ] **Step 1: Read the current Vietnamese appearance.mdx**

Read `_locales/vi/survey-design/appearance.mdx` fully to understand its current structure and identify the best insertion point.

- [ ] **Step 2: Add the new extended appearances section**

Find the appropriate place in the Vietnamese file to add the new rtSurvey-specific entries. The new content to append after the existing extended attributes section (before "## Known Limitations" or at the end of the extended attributes):

```markdown
### Nhóm và điều hướng

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| `section` | group | Hiển thị nhóm dưới dạng card phần có thể thu gọn. Lưu ý: chỉ dành cho ứng dụng di động. |
| `toc-hide` | bất kỳ | Loại trừ câu hỏi khỏi panel điều hướng mục lục (TOC). |
| `minilog` | begin_repeat | Hiển thị các mục lặp đã hoàn thành dưới dạng danh sách mini-log gọn thay vì mở rộng mỗi mục inline. |

### Hành vi nhập liệu

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| `proper` | text | Tự động viết hoa chữ cái đầu của mỗi từ khi người trả lời gõ (hành vi title-case). |
| `text-nolabel` | text, integer, decimal | Hiển thị trường nhập liệu không có nhãn hiển thị. |
| `inline-1line` | text | Buộc trường nhập văn bản hiển thị một dòng đơn ngay cả khi nhãn câu hỏi dài. |
| `popup` | bất kỳ | Hiển thị trường bên trong popup/modal overlay thay vì inline trên trang. |

### Bố cục

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| `horizontal(N)` | select_one, select_multiple | Đặt mỗi lựa chọn chiếm `N` phần trăm độ rộng hàng. Ví dụ: `horizontal(50)` đặt hai lựa chọn mỗi hàng. |
| `scroll-view(N%)` | group, repeat | Giới hạn container ở chiều cao tối đa `N%` viewport (hoặc parent), thêm thanh cuộn khi nội dung tràn. |

### Widget

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| `rating_box-fill-{c1}-{c2}-{c3}-{c4}-{c5}` | select_one | Hiển thị lựa chọn dưới dạng ô xếp hạng có kiểu với năm khe màu. `c1` = viền container ngoài, `c2` = viền chưa chọn, `c3` = viền và nền đã chọn, `c4` = màu chữ chưa chọn, `c5` = màu chữ đã chọn. Ví dụ: `rating_box-fill-grey-blue-green-black-white`. |
| `tagging-choices-noshow-v2-{c1}-{c2}-{c3}-{c4}-{c5}` | select_multiple | Hiển thị lựa chọn dưới dạng chip tag có màu. Năm khe màu theo cùng thứ tự như `rating_box-fill`. Lựa chọn đã chọn được làm nổi bật; lựa chọn chưa chọn bị ẩn khỏi tóm tắt. |

### Chuyển đổi ngôn ngữ

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| `change_language-{colors} default('lang')` | note, text | Hiển thị widget chuyển đổi ngôn ngữ được tạo kiểu với các mã màu đã cho. Token `default('lang')` đặt ngôn ngữ ban đầu (ví dụ: `default('vi')`); nó được nội bộ viết lại thành `rtDefault('lang')` khi phân tích. Ví dụ: `change_language-blue-white default('vi')`. |
```

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/appearance.mdx
git commit -m "i18n(vi): add extended appearance attributes to Vietnamese appearance page"
```

---

## Task 8: Add `search()` section to Vietnamese `dynamic-search.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/advanced-features/dynamic-search.mdx`
- Reference (English section added): `pages/survey-design/advanced-features/dynamic-search.mdx` — section "## Local file search with search()" added before "## Best Practices"

The Vietnamese file currently has "## Thực hành tốt" and "## Giới hạn" at the end. Insert the new section immediately before "## Thực hành tốt".

- [ ] **Step 1: Insert the Vietnamese search() section**

The old_string to replace is the `## Thực hành tốt` heading (first occurrence). The new_string:

```markdown
## Tìm kiếm tệp nội bộ với search()

`search()` thực hiện tra cứu bằng đẳng thức cột, ngoại tuyến đối với tệp SQLite `.db` đóng gói — không cần kết nối mạng và không cần truy vấn SQL. Dùng khi dữ liệu tham chiếu được đóng gói trong biểu mẫu và bạn cần tra cứu "tìm tất cả hàng có cột bằng giá trị" đơn giản.

### Cú pháp

```
search(path, 'matches', 'list_name', ${field})
```

### Tham số

| Tham số | Mô tả |
|---------|-------|
| `path` | Đường dẫn đến bảng SQLite: `concat(${family_path}, '/file.db::table')` |
| `'matches'` | Toán tử khớp — trả về hàng có cột bằng giá trị |
| `'list_name'` | Tên cột để khớp |
| `${field}` | Giá trị cần khớp; thường là tham chiếu trường |

### Ví dụ

Điền `select_one` từ cơ sở dữ liệu nội bộ bằng cách khớp giá trị của `${d307}` với cột `list_name` trong bảng `externalData` của `d307.db`:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Chọn cơ sở | `search(concat(${family_path}, '/d307.db::externalData'), 'matches', 'list_name', ${d307})` |

Khi `${d307}` bằng `"HF001"`, `search()` trả về mọi hàng trong `externalData` có `list_name = 'HF001'` — hoàn toàn từ tệp đóng gói, không cần kết nối mạng.

### search() so với tự động hoàn thành rawquery

| Tính năng | `search()` | Tự động hoàn thành `rawquery` |
|---------|-----------|------------------------|
| Truy vấn SQL | Không — chỉ đẳng thức cột | Có — toàn bộ `SELECT … FROM …` |
| Input có tham số | Khớp giá trị cột | Nhúng trong chuỗi SQL |
| Nhập tự do | Có — người điều tra có thể gõ tự do | Không — phải chọn từ danh sách |
| UNION / nhiều bảng | Không được hỗ trợ | Được hỗ trợ |

### Khi nào dùng mỗi loại

- Dùng **`search()`** khi cần khớp đẳng thức đơn giản đối với tệp `.db` đóng gói, biểu mẫu phải hoạt động ngoại tuyến, và muốn cho phép nhập tự do.
- Dùng **tự động hoàn thành `rawquery`** khi cần linh hoạt SQL (JOIN, UNION, cột tính toán) hoặc phải truy vấn nhiều bảng.

---

## Thực hành tốt
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/dynamic-search.mdx
git commit -m "i18n(vi): add search() section to dynamic-search"
```

---

## Task 9: Add new sections to Vietnamese `multi-language.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/multi-language.mdx`
- Reference (English additions): `pages/survey-design/multi-language.mdx` — sections "## HTML formatting in bilingual labels" and "## Language-aware calculations" added after the language-specific appearance section, before Best Practices.

The current Vietnamese file has a section "### Thông báo xác thực dành riêng cho ngôn ngữ" and "### Hỗ trợ Ngôn ngữ RTL". Add the two new sections after "### Hiển thị (Appearance) dành riêng cho ngôn ngữ" (the last subsection under "## Các tính năng dành riêng cho rtSurvey") and before "## Các phương pháp hay nhất khi khảo sát đa ngôn ngữ".

- [ ] **Step 1: Read the Vietnamese file to identify the exact insertion point**

Read `_locales/vi/survey-design/multi-language.mdx` lines 67–85 to find the text just before "## Các phương pháp hay nhất".

- [ ] **Step 2: Insert the new sections**

Find the text:
```
## Các phương pháp hay nhất khi khảo sát đa ngôn ngữ
```

Replace it with:

```markdown
## Định dạng HTML trong nhãn song ngữ

Bạn có thể kết hợp thẻ HTML với các thẻ ngôn ngữ trong một ô nhãn duy nhất. rtSurvey trích xuất khối ngôn ngữ đang hoạt động và render HTML còn lại.

Ví dụ dùng in đậm và màu font theo từng ngôn ngữ:

```
<en><big><b>Section 2: Household Income</b></big><br>Ask the household head only.</en><vi><big><b>Phần 2: Thu nhập hộ gia đình</b></big><br>Chỉ hỏi chủ hộ.</vi>
```

Các thẻ inline được hỗ trợ bên trong thẻ ngôn ngữ: `<b>`, `<i>`, `<u>`, `<big>`, `<small>`, `<font color="...">`, `<br>`, `<span style="...">`.

Ví dụ văn bản màu theo từng ngôn ngữ:

```
<en><font color="red">Required field</font></en><vi><font color="red">Trường bắt buộc</font></vi>
```

## Tính toán nhận biết ngôn ngữ

Khi biểu mẫu có trường `${language_use}` (được đặt bởi widget `change_language`), dùng `if()` để trả về giá trị theo ngôn ngữ đang hoạt động:

```
if(${language_use} = 'en', label_en, label_vi)
```

Ví dụ — hiển thị kết quả tra cứu theo ngôn ngữ đang hoạt động bằng `pulldata('rawquery', ...)`:

```
| type      | name        | calculation                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| calculate | district_label | if(${language_use} = 'en', pulldata('rawquery', concat(${family_path}, '/locations.db::externalData'), 'SELECT label_en FROM externalData WHERE code = ?', ${district}), pulldata('rawquery', concat(${family_path}, '/locations.db::externalData'), 'SELECT label_vi FROM externalData WHERE code = ?', ${district})) |
```

Lưu ý: Trường `language_use` thường được đặt bởi widget appearance `change_language`. Xem Appearance — change_language.

## Các phương pháp hay nhất khi khảo sát đa ngôn ngữ
```

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/multi-language.mdx
git commit -m "i18n(vi): add HTML bilingual labels and language-aware calculations to multi-language"
```

---

## Task 10: Add new functions to Vietnamese `functions.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/operators-and-functions/functions.mdx`
- Reference (English additions): `pages/survey-design/operators-and-functions/functions.mdx`

Two additions were made to the English functions page:
1. Under String functions: item 2 `string-length()` — **cascade dependency pattern** sub-note was added
2. Under Date functions: new item 8 `STRFTIME()` was added after item 7 `format-date-time()`

- [ ] **Step 1: Add cascade dependency pattern to string-length()**

In `_locales/vi/survey-design/operators-and-functions/functions.mdx`, find the `string-length` entry (item 2 under Hàm chuỗi):

```
2. `string-length(field)`: Trả về độ dài chuỗi của trường.
   - Ví dụ: `string-length(.) > 3 and string-length(.) < 10` có thể dùng để đảm bảo trường hiện tại có từ 3 đến 10 ký tự.
```

Replace with:

```
2. `string-length(field)`: Trả về độ dài chuỗi của trường.
   - Ví dụ: `string-length(.) > 3 and string-length(.) < 10` có thể dùng để đảm bảo trường hiện tại có từ 3 đến 10 ký tự.
   - **Mẫu cascade dependency**: `string-length(${province}) >= 0` luôn trả về `true` nhưng buộc rtSurvey tính lại biểu thức bất cứ khi nào `${province}` thay đổi. Dùng trong `relevant` để kích hoạt làm mới cascade khi trường cha cập nhật:
     | type | name | relevant |
     |------|------|----------|
     | select_one | district | `string-length(${province}) >= 0` |
     Điều này đảm bảo câu hỏi quận/huyện tính lại appearance `search()` hoặc `rawquery` bất cứ khi nào tỉnh thay đổi.
```

- [ ] **Step 2: Add STRFTIME to Date functions**

Find the existing item 7 `format-date-time` in the Vietnamese functions file under the Date functions section. Add item 8 immediately after it:

```
8. `STRFTIME(format, datetime)`: Định dạng ngày theo kiểu SQLite. Có sẵn bên trong chuỗi SQL truyền cho truy vấn `rawquery` — **không** có sẵn trong cột `calculation` hay `label` của XLSForm. Dùng token định dạng SQLite (`%Y`, `%m`, `%d`, `%H`, `%M`, `%S`).
   - Ví dụ bên trong chuỗi SQL rawquery: `'SELECT STRFTIME(''%Y-%m'', interview_date) AS month FROM data WHERE id = ?'`
   - Lưu ý: Dùng `format-date-time()` để định dạng ngày trong biểu thức XLSForm. `STRFTIME()` là hàm SQLite chỉ có sẵn trong SQL truyền cho `rawquery`.
```

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/operators-and-functions/functions.mdx
git commit -m "i18n(vi): add STRFTIME and cascade dependency pattern to functions"
```

---

## Task 11: Add repeat sections to Vietnamese `repeats.mdx`

**Files:**
- Modify: `_locales/vi/survey-design/advanced-features/repeats.mdx`
- Reference (English additions): `pages/survey-design/advanced-features/repeats.mdx` — three new sections added before "## Best Practices": `1screen`, `add_repeat`, delete buttons

The current Vietnamese file ends with the old Best Practices item 5: `Dùng appearance \`field-list\`...`. The new content must be inserted before `## Thực hành tốt`.

- [ ] **Step 1: Insert the three new sections before "## Thực hành tốt"**

Find the text:
```
## Thực hành tốt
```

Replace with:

```markdown
## Hiển thị một màn hình mỗi phiên bản: `1screen`

Đặt `appearance: 1screen` trên trường `begin_repeat` để hiển thị tất cả trường của một phiên bản trên cùng một màn hình — tương tự `field-list` cho nhóm thông thường.

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Thành viên | `1screen` |
| text | member_name | Tên thành viên | |
| integer | member_age | Tuổi | |
| end_repeat | | | |

Khi `1screen` được đặt và không có `repeat_count` và không có trường `add_repeat` bên trong nhóm, rtSurvey tự động hiển thị nút **+** tròn ở cuối màn hình để người điều tra có thể thêm phiên bản mới mà không cần cấu hình thêm.

| Appearance | Một màn hình mỗi phiên bản | Nút + mặc định được thêm |
|------------|-------------------------|------------------------|
| `1screen` | Có | Có (khi không có child `add_repeat`) |
| `field-list` | Có | Không |

Dùng `field-list` khi muốn bố cục theo nhóm mà không có nút thêm tự động. Dùng `1screen` khi muốn cả bố cục theo nhóm và cách tích hợp để thêm phiên bản.

---

## Nút thêm tùy chỉnh `add_repeat`

Trường `note` (hoặc `text`) đặt **bên trong** nhóm lặp với `appearance: add_repeat` hiển thị dưới dạng nút "Thêm" toàn chiều rộng. Nhãn nút lấy từ cột `label` của trường. Khi có trường `add_repeat`, nút + tròn mặc định (từ `1screen`) bị ẩn.

Đặt trường `add_repeat` là trường cuối cùng bên trong nhóm lặp:

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Thành viên | `1screen` |
| text | member_name | Tên thành viên | |
| integer | member_age | Tuổi | |
| note | btn_add | + Thêm thành viên | `add_repeat` |
| end_repeat | | | |

### Tùy chỉnh màu sắc

Truyền mã màu bên trong giá trị appearance để tạo kiểu cho nút:

| Giá trị Appearance | Kết quả |
|------------------|--------|
| `add_repeat <#04B404/>` | Nền xanh lá, màu chữ mặc định |
| `add_repeat 04B404-ffffff` | Nền xanh lá, chữ trắng |

Màu đầu tiên là màu nền và màu thứ hai (sau dấu gạch nối) là màu chữ. Bỏ qua `#` khi dùng dạng phân cách bằng gạch nối.

### Biến thể icon

Dùng `add_repeat icon` (có khoảng trắng) để hiển thị nút icon tròn gọn thay vì nút toàn chiều rộng:

| type | name | label | appearance |
|------|------|-------|------------|
| note | btn_add | + Thêm | `add_repeat icon` |

---

## Nút xóa: `delete-repeat-current` và `delete-repeat-last`

Trường `note` bên trong nhóm lặp với `appearance: delete-repeat-current` hoặc `appearance: delete-repeat-last` hiển thị dưới dạng nút xóa split.

| Appearance | Hành động |
|------------|--------|
| `delete-repeat-current` | Xóa phiên bản hiện tại (đang hoạt động) |
| `delete-repeat-last` | Xóa phiên bản cuối cùng trong vòng lặp |

Nút mặc định (không phải icon) là nút split: icon thùng rác bên trái và văn bản nhãn trường bên phải, chiếm toàn bộ chiều rộng màn hình.

### Biến thể icon

Thêm `-icon` để có nút icon thùng rác tròn gọn:

| Appearance | Kết quả |
|------------|--------|
| `delete-repeat-current-icon` | Icon thùng rác tròn, xóa phiên bản hiện tại |
| `delete-repeat-last-icon` | Icon thùng rác tròn, xóa phiên bản cuối cùng |

### Tùy chỉnh màu sắc

Định dạng màu giống với `add_repeat`: dùng `<#RRGGBB/>` hoặc `RRGGBB-RRGGBB` (nền-chữ).

### Ví dụ mẫu đầy đủ

Vòng lặp sau dùng `1screen`, nút xóa-phiên-bản-hiện-tại tròn ở trên cùng, và nút thêm toàn chiều rộng ở dưới cùng:

| type | name | label | appearance |
|------|------|-------|------------|
| begin_repeat | members | Thành viên | `1screen` |
| note | btn_del | Xóa | `delete-repeat-current-icon` |
| text | member_name | Tên thành viên | |
| integer | member_age | Tuổi | |
| note | btn_add | + Thêm thành viên | `add_repeat` |
| end_repeat | | | |

---

## Thực hành tốt
```

- [ ] **Step 2: Update best practices item 5**

Find:
```
5. Dùng appearance `field-list` trên nhóm lặp để hiển thị tất cả trường trên một màn hình mỗi phiên bản (mobile).
```

Replace with:
```
5. Dùng `1screen` trên `begin_repeat` để hiển thị tất cả câu hỏi trên một màn hình mỗi phiên bản, kết hợp với trường `note` có `add_repeat` bên trong nhóm để cung cấp cho người điều tra nút "Thêm" được gắn nhãn rõ ràng.
```

- [ ] **Step 3: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/repeats.mdx
git commit -m "i18n(vi): add 1screen, add_repeat, and delete button sections to repeats"
```

---

## Task 12: Update `_meta.json` with 4 new entries

**Files:**
- Modify: `_locales/vi/survey-design/advanced-features/_meta.json`

Current content:
```json
{
  "index": {
    "display": "hidden"
  },
  "call-api": "Call API",
  "dynamic-question-type": "Loại câu hỏi động",
  "dynamic-search": "Tìm kiếm động",
  "grid-layout": "Bố cục lưới",
  "html-styling": "HTML Styling",
  "images": "Hình ảnh",
  "repeats": "Lặp lại nâng cao"
}
```

- [ ] **Step 1: Add 4 new entries**

Replace the entire file with:

```json
{
  "index": {
    "display": "hidden"
  },
  "audio-recording": "Ghi âm",
  "call-api": "Call API",
  "dynamic-question-type": "Loại câu hỏi động",
  "dynamic-search": "Tìm kiếm động",
  "family-path": "family_path",
  "form-navigation": "Điều hướng biểu mẫu",
  "grid-layout": "Bố cục lưới",
  "html-styling": "HTML Styling",
  "images": "Hình ảnh",
  "local-database-search": "Tìm kiếm cơ sở dữ liệu nội bộ",
  "repeats": "Lặp lại nâng cao"
}
```

- [ ] **Step 2: Commit**

```bash
cd /Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com
git add _locales/vi/survey-design/advanced-features/_meta.json
git commit -m "i18n(vi): add 4 new pages to advanced-features _meta.json"
```

---

## Final step: Review

After all 12 tasks are complete, quickly verify:
- All 5 new files exist in `_locales/vi/`
- All 7 modified files have the new sections at the correct locations
- `_meta.json` has 11 entries (was 8, added 4 new, minus no removals — check against 8 + 4 = 12 total... actually 8 existing entries + 4 new = 12, but existing has 8 keys including `index`)
- Cross-links in the new Vietnamese files point to valid page slugs
