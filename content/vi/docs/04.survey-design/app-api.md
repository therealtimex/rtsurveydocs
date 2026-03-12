---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

App API cho phép người dùng tải các siêu dữ liệu (`meta data`) hệ thống từ ứng dụng bằng các phương thức khác nhau trong `FormEngine` và `DMView`. Nó cung cấp quyền truy cập vào các khóa dữ liệu khác nhau để lấy thông tin cụ thể từ ứng dụng.

Trong XLSForm, bạn có thể sử dụng hàm `pulldata()` với cú pháp sau:

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Từ khóa này thông báo cho `FormEngine` tải dữ liệu từ App API.
- `'data-key'`: Đây là khóa của dữ liệu bạn muốn tải từ App API.
- Nếu khóa dữ liệu không hợp lệ hoặc không được hỗ trợ, phép tính sẽ trả về "n/a".

Dưới đây là các khóa dữ liệu được hỗ trợ mà bạn có thể sử dụng với App-API:

`osPlatform`: Trả về tên hệ điều hành hiện tại (Android hoặc iOS) và phiên bản hệ điều hành. Các nền tảng web sẽ trả về một giá trị trống.

`appPlatform`: Trả về tên nền tảng ứng dụng, đó là `rtSurvey`.

`appVersion`: Trả về tên phiên bản của ứng dụng.

`getDisplayWidth`: Trả về chiều rộng màn hình thiết bị tính bằng pixel.

`getDisplayHeight`: Trả về chiều cao màn hình thiết bị tính bằng pixel.

`getScreenSize`: Trả về kích thước màn hình thiết bị tính bằng inch.

`projectCode`: Trả về mã dự án hiện tại của trang web mà người dùng đang đăng nhập.

`projectURL`: Trả về URL dự án hiện tại của trang web mà người dùng đang đăng nhập. Giá trị mặc định/dự phòng là một chuỗi văn bản trống ("").

`startingPoint`: Trả về đường dẫn của điểm bắt đầu biểu mẫu. Tham khảo "Form starting point" để biết thêm chi tiết.

`serverTime`: Trả về ước tính tốt nhất có thể về ngày và giờ trên máy chủ.

`user.[attribute]`: Trả về các thuộc tính của người dùng hiện tại dựa trên khóa thuộc tính được chỉ định. Tham khảo bảng "Thuộc tính người dùng" cho các khóa thuộc tính có sẵn.

Kết hợp các khóa thuộc tính bên dưới với "user." trong các tham số `pulldata()` để lấy thông tin người dùng hiện tại. Ví dụ, sử dụng `user.username`, `user.email`, v.v.

| Khóa thuộc tính | Mô tả |
|----------------------|--------------------------------------|
| username | Tên đăng nhập của người dùng |
| name | Tên đầy đủ của người dùng |
| staffCode | Mã nhân viên của người dùng |
| phone | Số điện thoại của người dùng |
| email | Địa chỉ email của người dùng |
| description | Văn bản mô tả trong thông tin người dùng |
| organization_id | ID tổ chức mà người dùng thuộc về |
| organization_name | Tên tổ chức mà người dùng thuộc về |
| team_id | ID đội nhóm mà người dùng thuộc về |
| supervisor_id | ID của giám sát viên của người dùng |
| user_role | Vai trò người dùng |
| user_group | Nhóm người dùng |
| is_supervisor | 1 nếu người dùng là giám sát viên, 0 nếu không |
| auto_approve_edit_request | 1 nếu người dùng được phép tự động phê duyệt "yêu cầu chỉnh sửa", 0 nếu không |
| ipcall.user          | Tham số của tài khoản IP Call - username |
| ipcall.token         | Tham số của tài khoản IP Call - token    |
| ipcall.password      | Tham số của tài khoản IP Call - password |
| ipcall.url           | Tham số của tài khoản IP Call - URL |
| ipcall.auth          | Tham số của tài khoản IP Call - auth (tùy chọn) |
| ipcall.port          | Tham số của tài khoản IP Call - port (tùy chọn) |

`instancePath`: Trả về đường dẫn thư mục của bản ghi (`instance`) hiện tại.

`appLanguage`: Trả về ngôn ngữ hiện tại của ứng dụng được thiết lập trong phần cài đặt ứng dụng (ví dụ: vi, en).

`openArgs.[attribute]`: Trả về các đối số mở biểu mẫu (`open-form-argument`) được truyền từ các ActionButton (`act_fill_form`, `act_get_instance`). Giá trị mặc định/dự phòng là một chuỗi văn bản trống ("").

`primaryAppColor`: Lấy màu chính của ứng dụng.
