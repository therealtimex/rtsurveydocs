---
title: "Các phần mở rộng nâng cao (Advanced extensions)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Cột `appearance` (hiển thị) trong rtSurvey cho phép bạn tùy chỉnh trình bày trực quan và hành vi của các câu hỏi trong khảo sát. Tính năng này nâng cao trải nghiệm người dùng và có thể cải thiện đáng kể hiệu quả thu thập dữ liệu. rtSurvey hỗ trợ các thuộc tính hiển thị XLSForm tiêu chuẩn và mở rộng chúng với các tùy chọn bổ sung.

## Các phần mở rộng hiển thị riêng của rtSurvey (rtSurvey-Specific Appearance Extensions)

rtSurvey mở rộng các tùy chọn hiển thị tiêu chuẩn với các tùy chọn sau:

### Tùy chỉnh nhập liệu thời gian (Time Input Customization)

Đối với các câu hỏi kiểu `text` được sử dụng để nhập thời gian:

- `appearance:` - Hiển thị một chiếc đồng hồ để chọn giờ và phút.
- `appearance: inline` - Hiển thị đồng hồ dưới dạng một biểu tượng.
- `appearance: inline-1line` - Hiển thị đồng hồ ở định dạng một hàng duy nhất.
- `appearance: inline-onlyresult` - Hiển thị biểu tượng đồng hồ, biến mất sau khi chọn.
- `appearance: inline-[FORMAT]` - Tùy chỉnh hiển thị định dạng thời gian (ví dụ: `[%H:%M]`, `[%h:%M:%S]`).

### Tùy chỉnh màu sắc (Color Customization)

rtSurvey cho phép tùy chỉnh màu sắc cho các kiểu hiển thị khác nhau:

- `appearance: inline colors("0099FF")` - Tùy chỉnh màu sắc biểu tượng.
- `appearance: inline-1line colors("0000FF","FFFF00")` - Tùy chỉnh màu sắc trong định dạng một hàng.

### Bố cục lưới (Grid Layout)

rtSurvey giới thiệu bố cục lưới cho các hiển thị dạng bảng, nhỏ gọn:

- `appearance: grid` - Áp dụng cho các nhóm để tạo bố cục lưới.

### Các nhóm có thể thu gọn (Collapsible Groups)

- `appearance: collapsible` - Tạo các nhóm có thể mở rộng hoặc thu gọn.

## Các thực hành tốt nhất khi sử dụng Appearance (Best Practices)

1. **Tính nhất quán**: Sử dụng các thuộc tính hiển thị nhất quán trong suốt khảo sát để có giao diện đồng bộ.
2. **Di động vs Web**: Xem xét cách hiển thị sẽ trông như thế nào trên các thiết bị và nền tảng khác nhau.
3. **Hiệu suất**: Cẩn trọng với các thuộc tính hiển thị có thể làm chậm quá trình tải biểu mẫu (ví dụ: `table-list` cho các nhóm lớn).
4. **Trải nghiệm người dùng**: Chọn các kiểu hiển thị giúp việc nhập dữ liệu dễ dàng và trực quan hơn cho người trả lời.
5. **Kiểm tra**: Luôn kiểm tra biểu mẫu của bạn trên các thiết bị mục tiêu để đảm bảo hiển thị hoạt động như mong đợi.

## Các kỹ thuật nâng cao (Advanced Techniques)

### Kết hợp các kiểu hiển thị (Combining Appearances)

Một số thuộc tính hiển thị có thể được kết hợp cho các bố cục phức tạp hơn:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Chọn một: | minimal compact |
```

### Hiển thị động (Dynamic Appearances)

rtSurvey cho phép thay đổi hiển thị động dựa trên logic của biểu mẫu:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Nhập thời gian: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Lưu ý cho ứng dụng di động (Mobile App Considerations)

- Một số kiểu hiển thị (ví dụ: `quick`, `signature`) chỉ dành riêng cho thiết bị di động.
- Kiểm tra kỹ lưỡng trên cả Android và iOS để đảm bảo hành vi nhất quán.

## Các hạn chế đã biết (Known Limitations)

- Các kiểu hiển thị phức tạp có thể không hiển thị giống hệt nhau trên tất cả các nền tảng.
- Một số kiểu hiển thị rtSurvey nâng cao có thể không được hỗ trợ trong chế độ ngoại tuyến.

## Khắc phục sự cố hiển thị (Troubleshooting Appearance Issues)

1. **Hiển thị không được áp dụng**: Kiểm tra lỗi chính tả trong cột appearance.
2. **Hiển thị không nhất quán**: Xác minh tính tương thích với loại câu hỏi và nền tảng.
3. **Vấn đề hiệu suất**: Cân nhắc đơn giản hóa các kiểu hiển thị phức tạp, đặc biệt là đối với các khảo sát lớn.
