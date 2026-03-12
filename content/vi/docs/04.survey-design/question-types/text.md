---
title: "Văn bản (Text)"
description: "Loại câu hỏi trả lời bằng văn bản tự do trong rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

## Tổng quan

Loại câu hỏi `text` (văn bản) trong rtSurvey cho phép trả lời bằng văn bản tự do, mang lại sự linh hoạt để thu thập các loại dữ liệu văn bản khác nhau. Nó dựa trên đặc tả XLSForm tiêu chuẩn nhưng bao gồm các phần mở rộng dành riêng cho rtSurvey để nâng cao chức năng.

## Đặc tả XLSForm

Trong XLSForm, loại câu hỏi văn bản được chỉ định là:

```
type: text
```

Để biết thêm chi tiết về cú pháp XLSForm tiêu chuẩn, hãy tham khảo [tài liệu XLSForm chính thức](https://xlsform.org/en/#question-types).

## Các phần mở rộng dành riêng cho rtSurvey

rtSurvey mở rộng chức năng của loại câu hỏi văn bản thông qua các tùy chọn hiển thị (`appearance`) khác nhau, đặc biệt là đối với việc nhập thời gian:

### Các phần mở rộng nhập Thời gian (Time Input)

- `appearance:` - Hiển thị đồng hồ để chọn giờ và phút
- `appearance: inline` - Hiển thị đồng hồ dưới dạng một biểu tượng
- `appearance: inline colors("0099FF")` - Hiển thị đồng hồ dưới dạng biểu tượng với màu sắc có thể tùy chỉnh
- `appearance: inline-1line` - Hiển thị đồng hồ để chọn theo định dạng hàng đơn
- `appearance: inline-1line-0000FF` - Định dạng hàng đơn với màu sắc tùy chỉnh
- `appearance: inline-1line colors("0000FF","FFFF00")` - Định dạng hàng đơn với nhiều tùy chọn màu sắc
- `appearance: inline-onlyresult` - Hiển thị đồng hồ dưới dạng biểu tượng ở cuối dòng, biến mất sau khi chọn
- `appearance: inline-onlyresult colors("0099FF")` - Giống như trên, với màu sắc biểu tượng tùy chọn

### Các phần mở rộng Định dạng Thời gian (Time Format)

- `appearance: inline-[%3]` - Hiển thị mili giây
- `appearance: inline-[%S]` - Hiển thị giây
- `appearance: inline-[%M]` - Hiển thị phút
- `appearance: inline-[%h]` - Hiển thị giờ (định dạng 12 giờ)
- `appearance: inline-[%H]` - Hiển thị giờ (định dạng 24 giờ)
- `appearance: inline-[%H-%M-%S]` - Hiển thị thời gian theo định dạng HH-MM-SS
- `appearance: inline-[%H:%M:%3]` - Hiển thị thời gian theo định dạng HH:MM:mili giây
- `appearance: inline-[%h:%M:%S]` - Hiển thị thời gian định dạng 12 giờ kèm theo giây
- `appearance: inline-[%H:%M]` - Hiển thị thời gian định dạng 24 giờ
- `appearance: inline-[%h:%M]` - Hiển thị thời gian định dạng 12 giờ
- `appearance: inline-[%M:%S]` - Hiển thị phút và giây
- `appearance: inline-[%M:%3]` - Hiển thị phút và mili giây

## Định dạng dữ liệu

Dữ liệu văn bản được lưu trữ và xuất dưới dạng văn bản. Đối với dữ liệu nhập dựa trên thời gian, dữ liệu được lưu trữ dưới định dạng datetime dạng văn bản.

## Lưu ý cho Ứng dụng di động

Loại câu hỏi văn bản, bao gồm tất cả các biến tể và hiển thị của nó, được hỗ trợ đầy đủ trên các nền tảng iOS, Android và Web.

## Các loại câu hỏi liên quan

- Số nguyên (Integers)
- Datetime

## Các phương pháp hay nhất

- Sử dụng nhãn rõ ràng và súc tích cho các câu hỏi văn bản để hướng dẫn người trả lời.
- Cân nhắc sử dụng các ràng buộc (`constraints`) hoặc quy tắc xác thực để đảm bảo chất lượng dữ liệu.
- Đối với nhập liệu thời gian, hãy chọn tùy chọn hiển thị phù hợp dựa trên mức độ chính xác yêu cầu cho bản khảo sát của bạn.

## Các hạn chế đã biết

Hiện tại, không có hạn chế nào được ghi nhận đối với loại câu hỏi văn bản trong rtSurvey.

## Ảnh chụp màn hình

[Lưu ý: Thêm các ảnh chụp màn hình liên quan để minh họa cho các hiển thị và biến thể khác nhau của loại câu hỏi văn bản.]
