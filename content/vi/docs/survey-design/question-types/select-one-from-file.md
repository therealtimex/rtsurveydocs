---
title: "Select from file"
description: "select_one_from_file và select_multiple_from_file tải lựa chọn động từ tệp CSV hoặc XML bên ngoài được đính kèm với biểu mẫu."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` và `select_multiple_from_file` hoạt động giống như `select_one` và `select_multiple`, nhưng thay vì định nghĩa lựa chọn trong **bảng tính choices**, các lựa chọn được tải từ **tệp CSV hoặc XML bên ngoài** được đính kèm với biểu mẫu. Điều này hữu ích khi danh sách lựa chọn của bạn rất dài, thay đổi thường xuyên, hoặc cần được cập nhật mà không cần xây dựng lại toàn bộ biểu mẫu.

## Cấu hình XLSForm cơ bản

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Chọn cơ sở y tế |
| select_multiple_from_file crops.csv | crops | Hộ gia đình trồng loại cây nào? |

Tên tệp sau tên loại phải khớp với tên tệp bạn đính kèm khi tải biểu mẫu lên.

## Định dạng tệp CSV

Tệp CSV của bạn phải có ít nhất hai cột: `name` (giá trị được lưu) và `label` (văn bản hiển thị). Bạn có thể thêm bất kỳ số cột bổ sung nào để lọc.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Lọc lựa chọn

Dùng cột `choice_filter` để chỉ hiển thị các lựa chọn phù hợp với ngữ cảnh hiện tại. Tham chiếu các cột CSV bằng tên cột trực tiếp (không dùng `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Chọn quận/huyện | |
| select_one_from_file health_facilities.csv | facility | Chọn cơ sở | district = ${district} |

Trong ví dụ này, chỉ các cơ sở trong quận/huyện đã chọn được hiển thị. `district` trong `choice_filter` tham chiếu đến cột `district` trong tệp CSV; `${district}` tham chiếu đến trường biểu mẫu có tên `district`.

## Ứng dụng

Câu hỏi chọn từ tệp thường được dùng cho:

1. **Danh sách lựa chọn dài** — cơ sở y tế, trường học, làng, danh sách loài (hàng trăm hoặc hàng nghìn mục)
2. **Danh sách thường xuyên cập nhật** — khi danh sách chính thay đổi giữa các đợt khảo sát, chỉ cần cập nhật CSV mà không cần xây dựng lại biểu mẫu
3. **Dữ liệu tham chiếu chia sẻ** — một tệp CSV được dùng cho nhiều biểu mẫu
4. **Lựa chọn phân tầng có lọc** — tải tất cả vùng/quận/làng trong một tệp, sau đó lọc theo lựa chọn cha

## Đính kèm tệp

Khi bạn tải biểu mẫu lên rtSurvey, đính kèm tệp CSV dưới dạng **tệp đính kèm media**. Tên tệp trong định nghĩa biểu mẫu phải khớp chính xác với tên tệp của tệp đính kèm.

{{% alert icon=" " context="warning" %}}
Tên tệp phân biệt chữ hoa chữ thường. `Health_Facilities.csv` và `health_facilities.csv` được coi là các tệp khác nhau.
{{% /alert %}}

## Dùng `choice-label()` với from-file

Để hiển thị nhãn của lựa chọn đã chọn trong một trường note hoặc calculate:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Chọn cơ sở | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Cơ sở đã chọn: ${facility_label} | |

## Thực hành tốt

1. Giữ tệp CSV dưới 5.000 hàng để đảm bảo hiệu suất tốt trên thiết bị di động.
2. Luôn bao gồm cột `name` và `label` — các cột bổ sung là tùy chọn.
3. Với lựa chọn phân tầng, dùng một CSV với cột cha và lọc bằng `choice_filter`.
4. Đặt tên phiên bản cho tên tệp CSV (ví dụ: `facilities_v3.csv`) khi thực hiện thay đổi cấu trúc cột.
5. Kiểm tra cẩn thận các biểu thức lọc — lỗi đánh máy trong `choice_filter` sẽ im lặng hiển thị không có lựa chọn nào.

## Giới hạn

- Tệp CSV rất lớn (10.000+ hàng) có thể làm chậm tải biểu mẫu, đặc biệt trên thiết bị cấu hình thấp.
- Tệp CSV phải được tải lên cùng với biểu mẫu — chúng không thể được tải từ URL lúc chạy (dùng `search()` hoặc `pulldata()` để tra cứu động).
- `select_multiple_from_file` ít được hỗ trợ hơn trên các client khác nhau — hãy xác minh tính tương thích trước khi sử dụng.

## So sánh với `search()`

| | `select_one_from_file` | Appearance `search()` |
|--|----------------------|----------------------|
| Nguồn lựa chọn | Tệp CSV/XML đính kèm | Truy vấn cơ sở dữ liệu phía server |
| Hoạt động ngoại tuyến | Có (tệp được đóng gói) | Cần kết nối mạng |
| Số lượng lựa chọn | Giới hạn bởi bộ nhớ thiết bị | Không giới hạn (phân trang) |
| Dữ liệu thời gian thực | Không | Có |

Với tập dữ liệu lớn, thường xuyên thay đổi, hoặc phía server, xem [Dynamic search](../advanced-extension/dynamic-search).
