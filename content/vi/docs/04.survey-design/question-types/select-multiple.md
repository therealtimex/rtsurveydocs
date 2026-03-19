---
title: "Select_multiple"
description: "Câu hỏi Select_multiple cho phép người trả lời chọn một hoặc nhiều tùy chọn từ danh sách đã định sẵn."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Loại câu hỏi `select_multiple` hiển thị danh sách cho phép người trả lời chọn **một hoặc nhiều tùy chọn**. Mặc định, các lựa chọn được hiển thị dưới dạng hộp kiểm. Giá trị được lưu là **danh sách các giá trị lựa chọn đã chọn, ngăn cách nhau bởi dấu cách**.

## Cấu hình XLSForm cơ bản

**Bảng tính survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Hộ gia đình trồng loại cây nào? |

**Bảng tính choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Ngô |
| crops | beans | Đậu |
| crops | rice | Lúa |
| crops | vegetables | Rau củ |
| crops | other | Khác |

Để biết thêm chi tiết, xem [thông số kỹ thuật XLSForm](https://xlsform.org/en/#question-types).

## Định dạng dữ liệu được lưu

Cột dữ liệu xuất chứa danh sách các giá trị đã chọn, ngăn cách nhau bởi dấu cách:

```
maize beans vegetables
```

Dùng hàm `selected()` — không phải `=` — khi kiểm tra giá trị select_multiple trong các biểu thức (xem bên dưới).

## Ứng dụng

Câu hỏi Select_multiple được dùng cho:

1. Thu thập nhiều câu trả lời đồng thời hợp lệ (ví dụ: nguồn thu nhập, cây trồng, triệu chứng)
2. Các mục kiểm tra dạng hộp kiểm (ví dụ: "Chọn tất cả phương án phù hợp")
3. Danh sách ngôn ngữ hoặc kỹ năng
4. Bất kỳ câu hỏi nào có nhiều câu trả lời đồng thời hợp lệ

## Tùy chọn hiển thị (appearance)

{{< table >}}
| Appearance | Mô tả |
|------------|-------|
| *(không có)* | Hộp kiểm mặc định, một hộp mỗi dòng |
| `minimal` | Widget chọn nhiều dạng thả xuống |
| `compact` | Lưới thu gọn, số cột tự điều chỉnh theo chiều rộng màn hình |
| `compact-N` | Lưới thu gọn cố định N cột |
| `horizontal` | Các lựa chọn xếp ngang theo hàng (web) |
| `horizontal-compact` | Ngang, khoảng cách thu gọn (web) |
| `label` | Chỉ hiển thị nhãn, không có hộp kiểm (dùng với `list-nolabel`) |
| `list-nolabel` | Chỉ hiển thị hộp kiểm, không có nhãn (dùng với `label`) |
| `columns(N)` | Hiển thị theo N cột (phần mở rộng rtSurvey) |
{{< /table >}}

### Ví dụ: Bố cục lưới 3 cột thu gọn

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Chọn tất cả triệu chứng quan sát được | compact-3 |

## Dùng `selected()` trong biểu thức

Vì giá trị được lưu là chuỗi ngăn cách bởi dấu cách, bạn **phải** dùng `selected()` để kiểm tra xem một lựa chọn cụ thể đã được chọn chưa. Dùng `=` sẽ không hoạt động đúng.

### Trong `relevant`

Hiển thị câu hỏi tiếp theo chỉ khi "khác" được chọn:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Cây nào được trồng? | |
| text | crops_other | Vui lòng ghi rõ loại cây khác | `selected(${crops_grown}, 'other')` |

### Trong `constraint`

Yêu cầu chọn ít nhất 2 lựa chọn:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Vui lòng chọn ít nhất 2 vấn đề |

Giới hạn tối đa 3 lựa chọn:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Chỉ được chọn tối đa 3 ưu tiên |

### Trong `calculate` — ghép nhãn đã chọn

Kết hợp `selected-at()`, `count-selected()`, và `choice-label()` để tạo tóm tắt có thể đọc được:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Tùy chọn "Không có mục nào" / lựa chọn loại trừ

Một mẫu phổ biến là làm cho một tùy chọn loại trừ tất cả các tùy chọn còn lại. Dùng `constraint` để thực thi:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Chọn tất cả vấn đề hiện có | `not(selected(., 'none') and count-selected(.) > 1)` | "Không có" không thể chọn cùng với các tùy chọn khác |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Thiếu nước |
| issues | roads | Đường sá kém |
| issues | health | Thiếu dịch vụ y tế |
| issues | none | Không có vấn đề nào |

## Đếm và tóm tắt các lựa chọn

| Hàm | Ví dụ | Kết quả |
|-----|-------|---------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Số lượng lựa chọn đã chọn |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Giá trị được chọn đầu tiên |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Nhãn của một giá trị |

## Thực hành tốt

1. Luôn dùng `selected()` trong `relevant`, `constraint`, và `calculate` — không bao giờ dùng `=` hoặc `!=`.
2. Thêm constraint để giới hạn số lượng lựa chọn tối đa nếu thiết kế câu hỏi yêu cầu.
3. Bao gồm tùy chọn "Không có" hoặc "Không áp dụng" khi không chọn gì cũng là câu trả lời hợp lệ.
4. Với danh sách dài (15+ lựa chọn), dùng `minimal` (danh sách thả xuống chọn nhiều) để tránh cuộn quá nhiều.
5. Xuất dữ liệu và dùng tách chuỗi trong công cụ phân tích — định dạng ngăn cách bởi dấu cách cần tách trước khi phân tích tổng hợp.

## Giới hạn

- Giá trị Select_multiple không thể so sánh trực tiếp bằng `=`. Luôn dùng `selected()`.
- Kiểu hiển thị compact có thể không hiển thị tốt với nhãn lựa chọn rất dài.
- Khi lọc lựa chọn bằng `choice_filter`, việc lọc áp dụng cho tất cả lựa chọn được hiển thị, giống như `select_one`.
