---
title: "Đường địa lý (Geotrace)"
description: "Các câu hỏi kiểu Geotrace cho phép người trả lời ghi lại một chuỗi các điểm được kết nối trên bản đồ, tạo thành các đường hoặc lối đi như một phần của cuộc khảo sát."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Loại câu hỏi `geotrace` (đường địa lý) trong XLSForm và rtSurvey cho phép người trả lời thu thập một chuỗi các điểm được kết nối trên bản đồ, tạo thành các đường hoặc lối đi. Tính năng này đặc biệt hữu ích để lập bản đồ các tuyến đường, ranh giới hoặc các đối tượng dạng đường trong các khảo sát không gian.

## Đặc tả XLSForm cơ bản

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Vẽ lại lộ trình của dòng sông   |

Để biết thêm chi tiết về loại câu hỏi geotrace cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi đường địa lý thường được dùng cho:

1. Lập bản đồ các tuyến đường hoặc lối đi trong các cuộc khảo sát thực địa
2. Vẽ các đối tượng dạng đường như đường sá, sông ngòi hoặc ranh giới
3. Ghi lại phạm vi của cơ sở hạ tầng dạng đường (ví dụ: đường ống, đường dây điện)
4. Ghi lại lộ trình di chuyển trong các nghiên cứu giao thông
5. Xác định các tuyến cắt (transects) trong khảo sát sinh thái

## Các phương pháp hay nhất

1. Đảm bảo thiết bị đã bật dịch vụ vị trí và đã được cấp quyền truy cập.
2. Cung cấp hướng dẫn rõ ràng về cách vẽ đường và những đối tượng nào nên được bao gồm.
3. Cân nhắc sử dụng ảnh vệ tinh hoặc bản đồ nền để giúp người trả lời vẽ đường chính xác hơn.
4. Lưu ý đến độ phức tạp tiềm tàng của các đường vẽ và tác động của chúng đối với kích thước dữ liệu và quá trình xử lý.

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng câu hỏi geotrace trong một cuộc khảo sát:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Vẽ lại lối đi của đường mòn leo núi       | Bắt đầu tại đầu đường mòn và kết thúc tại đỉnh núi |

## Các phần mở rộng của rtSurvey

Mặc dù đặc tả XLSForm cơ bản cho câu hỏi đường địa lý khá đơn giản, rtSurvey có thể cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Tích hợp với bản đồ ngoại tuyến cho các khu vực vùng sâu vùng xa
2. Tùy chọn thiết lập số điểm tối thiểu và tối đa cho đường vẽ
3. Khả năng chỉnh sửa hoặc hoàn thiện các đường vẽ sau khi đã vẽ ban đầu
4. Hỗ trợ tự động vẽ theo các khoảng thời gian nhất định trong quá trình di chuyển

## Định dạng dữ liệu

Dữ liệu geotrace thường được lưu trữ dưới dạng một chuỗi các cặp tọa độ cách nhau bằng dấu cách, tương tự như geoshape nhưng không có điểm đóng:

```
vĩ độ1 kinh độ1; vĩ độ2 kinh độ2; vĩ độ3 kinh độ3; ... vĩ độN kinh độN
```

Ví dụ:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## Các lưu ý khi phân tích

Khi sử dụng câu hỏi đường địa lý, hãy cân nhắc:

1. Cách dữ liệu địa lý sẽ được hiển thị trực quan và phân tích (ví dụ: phần mềm GIS)
2. Nhu cầu tiềm năng về làm sạch dữ liệu hoặc đơn giản hóa các đường vẽ phức tạp
3. Các biện pháp bảo mật và bảo vệ dữ liệu khi xử lý dữ liệu không gian chi tiết
4. Tích hợp với các nguồn dữ liệu không gian khác để phân tích toàn hiện

## Hạn chế

- Việc vẽ các đường dẫn chính xác trên màn hình di động nhỏ có thể gặp khó khăn.
- Các đường vẽ phức tạp có thể yêu cầu khả năng lưu trữ và xử lý đáng kể.
- Việc sử dụng GPS liên tục để tự động vẽ đường có thể nhanh chóng làm cạn pin thiết bị.
- Có thể có các lo ngại về quyền riêng tư liên quan đến việc thu thập dữ liệu đường đi chi tiết.
