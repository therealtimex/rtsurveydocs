---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Cột `appearance` trong rtSurvey cho phép bạn tùy chỉnh cách trình bày trực quan và hành vi của các câu hỏi trong khảo sát. Tính năng này nâng cao trải nghiệm người dùng và có thể cải thiện đáng kể hiệu quả thu thập dữ liệu. rtSurvey hỗ trợ các thuộc tính appearance tiêu chuẩn của XLSForm và mở rộng chúng với các tùy chọn bổ sung.

## Các thuộc tính Appearance tiêu chuẩn của XLSForm

rtSurvey hỗ trợ các thuộc tính appearance tiêu chuẩn sau của XLSForm:

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|--------------|-------|
| multiline | text | Tạo hộp văn bản nhiều dòng (tốt nhất cho web) |
| minimal | select_one, select_multiple | Hiển thị các lựa chọn trong menu thả xuống |
| quick | select_one | Tự động chuyển sang câu hỏi tiếp theo sau khi chọn (chỉ mobile) |
| no-calendar | date | Không hiển thị lịch (chỉ mobile) |
| month-year | date | Chỉ cho phép chọn tháng và năm |
| year | date | Chỉ cho phép chọn năm |
| horizontal-compact | select_one, select_multiple | Hiển thị lựa chọn theo chiều ngang (chỉ web) |
| horizontal | select_one, select_multiple | Hiển thị lựa chọn theo chiều ngang trong các cột (chỉ web) |
| likert | select_one | Trình bày lựa chọn dưới dạng thang đo Likert |
| compact | select_one, select_multiple | Hiển thị lựa chọn cạnh nhau với khoảng cách tối thiểu |
| quickcompact | select_one | Kết hợp hiển thị thu gọn với tự động chuyển câu hỏi (chỉ mobile) |
| field-list | groups | Hiển thị toàn bộ nhóm trên một màn hình (chỉ mobile) |
| label | select_one, select_multiple | Hiển thị nhãn lựa chọn mà không có nút chọn |
| list-nolabel | select_one, select_multiple | Hiển thị nút chọn mà không có nhãn (dùng với `label`) |
| table-list | groups | Hiển thị câu hỏi theo định dạng bảng |
| signature | image | Bật chụp chữ ký (chỉ mobile) |
| draw | image | Cho phép vẽ tay (chỉ mobile) |
| map, quick map | select_one, select_one_from_file | Bật chọn từ các đặc điểm trên bản đồ |

## Thực hành tốt khi sử dụng Appearance

1. **Nhất quán**: Sử dụng các thuộc tính appearance nhất quán trong toàn bộ khảo sát để có giao diện đồng bộ.
2. **Mobile và Web**: Xem xét cách appearance hiển thị trên các thiết bị và nền tảng khác nhau.
3. **Hiệu suất**: Thận trọng với các appearance có thể làm chậm tải biểu mẫu (ví dụ: `table-list` cho các nhóm lớn).
4. **Trải nghiệm người dùng**: Chọn appearance giúp nhập liệu dễ dàng và trực quan hơn cho người trả lời.
5. **Kiểm thử**: Luôn kiểm tra biểu mẫu trên thiết bị đích để đảm bảo appearance hoạt động đúng mong đợi.

## Kỹ thuật nâng cao

### Kết hợp Appearance

Một số thuộc tính appearance có thể kết hợp để tạo bố cục phức tạp hơn:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Chọn một: | minimal compact |
```

### Appearance động

rtSurvey cho phép thay đổi appearance động dựa trên logic biểu mẫu:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Nhập thời gian: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Lưu ý cho Ứng dụng di động

- Một số appearance (ví dụ: `quick`, `signature`) chỉ dành riêng cho thiết bị di động.
- Kiểm tra kỹ trên cả Android và iOS để đảm bảo hành vi nhất quán.

## Các thuộc tính Appearance mở rộng của rtSurvey

Ngoài các appearance XLSForm tiêu chuẩn, rtSurvey hỗ trợ các tùy chọn riêng cho nền tảng sau:

### Kiểm soát hiển thị và dữ liệu

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|--------------|-------|
| `invisible` | bất kỳ | Ẩn trường khỏi hiển thị trong khi vẫn thu thập hoặc tính toán giá trị. Khác với loại `hidden` — trường vẫn tham gia vào logic. |
| `displaytitle` | bất kỳ | Buộc hiển thị nhãn/tiêu đề của trường ngay cả khi nó thường bị ẩn. |
| `autopull` | select_one, select_multiple | Tự động lấy dữ liệu bên ngoài để điền lựa chọn khi biểu mẫu tải hoặc trường kích hoạt thay đổi. |
| `floating_hint` | text, integer, decimal | Hiển thị gợi ý dưới dạng nhãn nổi phía trên trường nhập thay vì phía dưới. |
| `calculate-button` | calculate | Thêm nút hiển thị kích hoạt tính lại trường theo yêu cầu, thay vì tính tự động. |

### Bố cục

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|--------------|-------|
| `1screen` | group | Buộc hiển thị toàn bộ nhóm trên một màn hình bất kể kích thước nhóm. |
| `columns(n)` | select_one, select_multiple | Hiển thị lựa chọn theo `n` cột. Ví dụ: `columns(3)` hiển thị ba cột nút radio. |
| `gridformat<row=R col=C colspan=S align=center>` | bất kỳ | Định vị trường trong bố cục CSS grid tại hàng `R`, cột `C`, kéo dài `S` cột. Dùng với `advanced-extension/grid-layout`. |
| `ignore-simplify` | bất kỳ | Hướng dẫn renderer biểu mẫu bỏ qua đơn giản hóa hoặc thu gọn tự động bố cục trường này. |
| `required-but-simplify` | bất kỳ | Trường là bắt buộc nhưng bố cục vẫn được đơn giản hóa bởi renderer |
| `embed` | bất kỳ | Hiển thị trường trong chế độ nhúng/nội tuyến, loại bỏ vùng bọc ngoài và vùng chứa nhãn |
| `popup` | select_one, select_multiple | Hiển thị danh sách lựa chọn trong lớp phủ popup/modal thay vì nội tuyến |
| `auto-hide-empty` | boxtag, select | Ẩn toàn bộ widget câu hỏi khi danh sách lựa chọn trống |
| `text-nolabel` | select_one, select_multiple | Ẩn nhãn văn bản cho mỗi lựa chọn, chỉ hiển thị control nhập liệu |

### Widget

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|--------------|-------|
| `likert` | select_one | Trình bày lựa chọn dưới dạng hàng thang Likert (đã có trong bảng tiêu chuẩn ở trên; được xác nhận hỗ trợ). |
| `distress` | select_one | Hiển thị lựa chọn dưới dạng widget trực quan Thang đo tâm lý Kessler (K10) với biểu tượng cảm xúc. |

### Widget trực quan lựa chọn

Các appearance này thay đổi toàn bộ cách hiển thị danh sách lựa chọn.

| Appearance | Loại câu hỏi | Mô tả |
|------------|--------------|-------|
| `tagging` | select_one, select_multiple | Các lựa chọn hiển thị dưới dạng chip thẻ hình viên thuốc có thể nhấp. |
| `boxtag` | select_one, select_multiple | Các lựa chọn hiển thị dưới dạng hộp hình chữ nhật có kiểu dáng mà người dùng nhấn. |
| `boxtag -search` | select_one, select_multiple | Bố cục boxtag với ô tìm kiếm/lọc trực tiếp phía trên các hộp. |
| `duolingo-style1` | select_one, select_multiple | Bố cục thẻ lớn lấy cảm hứng từ Duolingo — phù hợp cho danh sách ngắn với biểu tượng. |
| `rating_box` | select_one, select_multiple | Lưới các hộp số có thể nhấn — phù hợp cho câu hỏi thang đo hoặc NPS. |
| `star_rating` | select_one | Các lựa chọn hiển thị dưới dạng ngôi sao; số ngôi sao bằng số lựa chọn. |
| `choices-noshow` | select_one, select_multiple | Ban đầu chỉ hiển thị 10 lựa chọn đầu tiên với điều khiển "Hiện thêm". |
| `noshow` | select_one, select_multiple | Ẩn hoàn toàn danh sách lựa chọn; giá trị được đặt theo chương trình qua calculate hoặc API. |
| `checkall` | select_multiple | Thêm phím tắt "Chọn tất cả" ở đầu danh sách lựa chọn. |
| `max-items(N)` | select_one, select_multiple | Giới hạn danh sách lựa chọn hiển thị thành N mục. Ví dụ: max-items(5). |

### Widget trực quan văn bản

| Appearance | Loại câu hỏi | Mô tả |
|------------|--------------|-------|
| `richtext` | text | Thay thế ô nhập văn bản thuần bằng trình soạn thảo văn bản phong phú (in đậm, in nghiêng, danh sách, liên kết). Lưu dưới dạng HTML. |
| `typingtest` | text | Widget kiểm tra gõ phím — nhãn là đoạn văn; widget ghi lại phản hồi đã gõ và thời gian. |

### Phần mở rộng phương tiện

| Appearance | Loại câu hỏi | Mô tả |
|------------|--------------|-------|
| `watermark("expression")` | image | Chèn hình mờ văn bản lên ảnh chụp. Tham số là biểu thức XPath được đánh giá tại thời điểm chụp. |
| `editable` | image | Cho phép chú thích/vẽ lên ảnh chụp trước khi lưu. |

### Cấu hình hiển thị nội tuyến

Các modifier `display{}` và `results{}` kiểm soát căn chỉnh biểu tượng và hiển thị kết quả cho các widget nội tuyến.

#### Tham số `display{}`

| Tham số | Giá trị | Mô tả |
|---------|---------|-------|
| Căn chỉnh | `left`, `right`, `top`, `bottom`, `center` | Vị trí của biểu tượng so với trường nhập liệu |
| Kích thước | `small`, `medium`, `large` | Kích thước biểu tượng |
| Chế độ | `inline-icon` | Hiển thị trigger dưới dạng biểu tượng |
| Chế độ | `inline-button` | Hiển thị trigger dưới dạng nút đầy đủ |

#### Tham số `results{}`

| Tham số | Giá trị | Mô tả |
|---------|---------|-------|
| Căn chỉnh | `left`, `right`, `top`, `bottom`, `center` | Vị trí của hiển thị giá trị kết quả |
| `hide(field)` | tên trường phụ bất kỳ | Ẩn một thành phần cụ thể của kết quả |

### Tích hợp API

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|--------------|-------|
| `callapi` | text, integer, decimal, select_one | Bật tích hợp gọi API cho trường này. Cột calculation phải chứa biểu thức `callapi()`. Xem [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Kích hoạt cuộc gọi API xác minh với tham số tĩnh. Biểu mẫu chặn tiến độ cho đến khi API xác nhận giá trị. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Giống `callapi-verify` nhưng với tham số lấy từ giá trị trường khác trong thời gian thực. |

### Định dạng ngày/giờ inline

Với các trường `date`, `time`, và `datetime`, bạn có thể chỉ định định dạng hiển thị tùy chỉnh bằng chuỗi định dạng gắn vào appearance:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Các mã định dạng giống với `format-date()` và `format-date-time()`. Xem [Hàm — Hàm ngày giờ](operators-and-functions/functions#date-and-time-functions).

Ví dụ:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Ngày và giờ sự kiện | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Ngày sinh | inline-[%d/%m/%Y] |

## Hạn chế đã biết

- Các appearance phức tạp có thể không hiển thị giống hệt nhau trên tất cả các nền tảng.
- Một số appearance nâng cao của rtSurvey có thể không được hỗ trợ ở chế độ ngoại tuyến.

## Khắc phục sự cố Appearance

1. **Appearance không được áp dụng**: Kiểm tra lỗi đánh máy trong cột appearance.
2. **Hiển thị không nhất quán**: Xác minh tính tương thích với loại câu hỏi và nền tảng.
3. **Vấn đề hiệu suất**: Cân nhắc đơn giản hóa các appearance phức tạp, đặc biệt với khảo sát lớn.
