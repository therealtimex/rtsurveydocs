---
title: "Các loại câu hỏi"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey hỗ trợ tất cả các loại câu hỏi XLSForm tiêu chuẩn, cùng với một số phần mở rộng. Mỗi loại câu hỏi xác định loại dữ liệu được thu thập và cách widget nhập liệu được hiển thị trên thiết bị.

Để đặt loại câu hỏi, nhập tên loại vào cột `type` trong bảng tính **survey** của XLSForm.

## Nhập văn bản

| Loại | Mô tả |
|------|-------|
| [text](text) | Câu trả lời văn bản tự do — cho phép bất kỳ ký tự nào |
| [integer](integer) | Số nguyên (không có phần thập phân) |
| [decimal](decimal) | Số có phần thập phân |
| [range](range) | Số được chọn từ thanh trượt trong phạm vi tối thiểu/tối đa đã xác định |

## Lựa chọn

| Loại | Mô tả |
|------|-------|
| [select_one listname](select-one) | Chọn đúng một tùy chọn từ danh sách |
| [select_multiple listname](select-multiple) | Chọn một hoặc nhiều tùy chọn từ danh sách |
| [rank listname](rank) | Sắp xếp các lựa chọn theo ưu tiên hoặc thứ tự quan trọng |

## Ngày và Giờ

| Loại | Mô tả |
|------|-------|
| [date](date) | Ngày theo lịch (năm, tháng, ngày) |
| [time](time) | Thời gian trong ngày (giờ, phút) |
| [datetime](datetime-date-time) | Kết hợp ngày và giờ |

## Vị trí

| Loại | Mô tả |
|------|-------|
| [geopoint](geopoint) | Tọa độ GPS đơn lẻ (vĩ độ, kinh độ, độ cao, độ chính xác) |
| [geotrace](geotrace) | Một tuyến đường — chuỗi các điểm GPS tạo thành đường |
| [geoshape](geoshape) | Một khu vực — đa giác khép kín gồm các điểm GPS |

## Đa phương tiện

| Loại | Mô tả |
|------|-------|
| [image](image) | Chụp ảnh hoặc tải ảnh lên |
| [audio](audio) | Ghi âm |
| [video](video) | Quay video |
| [file](file) | Tải lên tệp chung (PDF, tài liệu, v.v.) |

## Khác

| Loại | Mô tả |
|------|-------|
| [barcode](barcode) | Quét mã vạch hoặc mã QR |
| [note](note) | Văn bản chỉ đọc — hiển thị hướng dẫn hoặc tóm tắt được tính toán |
| [calculate](calculate) | Trường ẩn lưu trữ giá trị được tính toán |
| [hidden](hidden) | Trường ẩn lưu trữ giá trị tĩnh hoặc được điền sẵn |
| [trigger / acknowledge](trigger) | Hộp kiểm mà người điều tra phải đánh dấu để xác nhận đã đọc một phát biểu |
| [meta](meta) | Siêu dữ liệu tự động: dấu thời gian, ID thiết bị, thông tin người điều tra |

## Phần mở rộng rtSurvey

Các loại này là đặc trưng của rtSurvey và không thuộc thông số kỹ thuật XLSForm tiêu chuẩn.

| Loại | Mô tả |
|------|-------|
| [search-autocomplete](search-autocomplete) | Nhập văn bản với gợi ý tự động hoàn thành từ API theo thời gian thực |
| [mentions](mentions) | Trường văn bản với tính năng tự động hoàn thành `@` để gắn thẻ thực thể ngay trong dòng |
| [texttags](texttags) | Nhập thẻ — mỗi mục nhập trở thành chip có thể xóa; lưu dưới dạng chuỗi phân tách bằng khoảng trắng |

Xem thêm về nhóm lặp: [Repeats](../advanced-extension/repeats)

## Cách type và appearance hoạt động cùng nhau

Cột `type` xác định **loại dữ liệu được thu thập**. Cột `appearance` kiểm soát **giao diện của widget**. Nhiều loại hỗ trợ nhiều kiểu hiển thị khác nhau — ví dụ `select_one` có thể hiển thị dưới dạng nút radio, danh sách thả xuống, thang Likert, hoặc lưới thu gọn.

Xem [Appearance](../appearance) để biết danh sách đầy đủ các tùy chọn.
