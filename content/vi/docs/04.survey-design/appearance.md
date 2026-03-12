---
title: "Hiển thị (Appearance)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Cột `appearance` trong rtSurvey cho phép bạn tùy chỉnh cách trình bày trực quan và hành vi của các câu hỏi trong khảo sát. Tính năng này nâng cao trải nghiệm người dùng và có thể cải thiện đáng kể hiệu quả thu thập dữ liệu. rtSurvey hỗ trợ các thuộc tính appearance tiêu chuẩn của XLSForm và mở rộng chúng với các tùy chọn bổ sung.

## Thuộc tính Appearance tiêu chuẩn của XLSForm

rtSurvey hỗ trợ các thuộc tính appearance tiêu chuẩn sau của XLSForm:

| Thuộc tính Appearance | Loại câu hỏi | Mô tả |
|----------------------|----------------|-------------|
| multiline | text | Tạo một hộp văn bản nhiều dòng (tốt nhất cho web) |
| minimal | select_one, select_multiple | Hiển thị các lựa chọn trong một menu thả xuống (dropdown) |
| quick | select_one | Tự động chuyển sang câu hỏi tiếp theo sau khi chọn (chỉ dành cho di động) |
| no-calendar | date | Không hiển thị lịch (chỉ dành cho di động) |
| month-year | date | Chỉ cho phép chọn tháng và năm |
| year | date | Chỉ cho phép chọn năm |
| horizontal-compact | select_one, select_multiple | Hiển thị các lựa chọn theo chiều ngang (chỉ dành cho web) |
| horizontal | select_one, select_multiple | Hiển thị các lựa chọn theo chiều ngang trong các cột (chỉ dành cho web) |
| likert | select_one | Trình bày các lựa chọn dưới dạng thang đo Likert |
| compact | select_one, select_multiple | Hiển thị các lựa chọn cạnh nhau với khoảng cách tối thiểu |
| quickcompact | select_one | Kết hợp hiển thị nhỏ gọn với tự động chuyển câu hỏi (chỉ dành cho di động) |
| field-list | groups | Hiển thị toàn bộ nhóm trên một màn hình (chỉ dành cho di động) |
| label | select_one, select_multiple | Hiển thị nhãn lựa chọn mà không có nút chọn |
| list-nolabel | select_one, select_multiple | Hiển thị nút chọn mà không có nhãn (sử dụng kết hợp với `label`) |
| table-list | groups | Hiển thị các câu hỏi theo định dạng bảng |
| signature | image | Cho phép lấy chữ ký (chỉ dành cho di động) |
| draw | image | Cho phép vẽ tay (chỉ dành cho di động) |
| map, quick map | select_one, select_one_from_file | Cho phép chọn từ các đặc điểm trên bản đồ |

## Các phương pháp hay nhất khi sử dụng Appearance

1. **Sự nhất quán**: Sử dụng các thuộc tính appearance nhất quán trong suốt bản khảo sát để có giao diện đồng bộ.
2. **Di động và Web**: Xem xét cách các thuộc tính appearance sẽ hiển thị trên các thiết bị và nền tảng khác nhau.
3. **Hiệu suất**: Thận trọng với các thuộc tính appearance có thể làm chậm quá trình tải biểu mẫu (ví dụ: `table-list` cho các nhóm lớn).
4. **Trải nghiệm người dùng**: Chọn các kiểu hiển thị giúp việc nhập liệu dễ dàng và trực quan hơn cho người trả lời.
5. **Kiểm thử**: Luôn kiểm tra biểu mẫu của bạn trên các thiết bị mục tiêu để đảm bảo phần hiển thị hoạt động như mong đợi.

## Kỹ thuật nâng cao

### Kết hợp các Appearance

Một số thuộc tính appearance có thể được kết hợp để có bố cục phức tạp hơn:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Chọn một: | minimal compact |
```

### Appearance động

rtSurvey cho phép thay đổi appearance động dựa trên logic của biểu mẫu:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Nhập thời gian: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Lưu ý cho Ứng dụng di động

- Một số kiểu hiển thị (ví dụ: `quick`, `signature`) chỉ dành riêng cho thiết bị di động.
- Kiểm tra kỹ lưỡng trên cả Android và iOS để đảm bảo hành vi nhất quán.

## Các hạn chế đã biết

- Các kiểu hiển thị phức tạp có thể không hiển thị giống hệt nhau trên tất cả các nền tảng.
- Một số kiểu hiển thị nâng cao của rtSurvey có thể không được hỗ trợ ở chế độ ngoại tuyến (`offline mode`).

## Khắc phục sự cố hiển thị

1. **Appearance không được áp dụng**: Kiểm tra lỗi chính tả trong cột appearance.
2. **Hiển thị không nhất quán**: Xác minh tính tương thích với loại câu hỏi và nền tảng.
3. **Vấn đề hiệu suất**: Cân nhắc đơn giản hóa các kiểu hiển thị phức tạp, đặc biệt đối với các bản khảo sát lớn.
