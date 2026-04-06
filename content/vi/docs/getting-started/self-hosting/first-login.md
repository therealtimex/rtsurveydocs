---
weight: 5
title: "Đăng nhập lần đầu"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Cách đăng nhập vào phiên bản rtSurvey của bạn lần đầu tiên sau khi triển khai."
---

> **SSL phải được cấu hình trước khi đăng nhập.** Nếu bạn truy cập ứng dụng qua HTTP, bạn sẽ thấy cảnh báo bảo mật và SSO sẽ bị chặn. Hãy hoàn thành [Cài đặt SSL](ssl-setup) trước.

Sau khi SSL hoạt động, mở trình duyệt tại URL HTTPS của bạn:

```
https://your-domain.com
```

---

## Màn hình đăng nhập

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

Trang đăng nhập hiển thị:

- Các trường **Tên người dùng** và **Mật khẩu**
- Nút **Đăng nhập**
- Nút **Đăng nhập bằng SSO** (bên dưới đường phân cách) — cho thành viên nhóm có tài khoản SSO

---

## Thông tin đăng nhập quản trị viên mặc định

Nhập thông tin đăng nhập mặc định và nhấp **Đăng nhập**:

| Trường | Giá trị |
|--------|---------|
| Tên người dùng | `admin` |
| Mật khẩu | `admin` |

> **Hãy đổi mật khẩu ngay sau lần đăng nhập đầu tiên.**

---

## Nếu bạn thấy cảnh báo bảo mật

Nếu bạn truy cập ứng dụng qua HTTP (trước khi SSL được cấu hình), bạn sẽ thấy:

- Biểu ngữ cảnh báo màu vàng ở đầu trang đăng nhập
- Hộp thoại khi nhấp **Đăng nhập**, cảnh báo rằng thông tin đăng nhập sẽ được gửi không mã hóa

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Nhấp **Cài đặt SSL** để cấu hình HTTPS, hoặc **Tiếp tục dù sao** để đăng nhập không có SSL (không khuyến nghị).

Đăng nhập SSO bị chặn hoàn toàn qua HTTP — nhấp **Đăng nhập bằng SSO** sẽ hiển thị thông báo thay vì chuyển hướng.

---

## Sau khi đăng nhập

Khi vào trong, bạn sẽ thấy bảng điều khiển. Từ đây:

1. **Đổi mật khẩu quản trị viên** — cài đặt tài khoản → đổi mật khẩu
2. **Tạo dự án đầu tiên** — Dự án → Dự án mới
3. **Tải lên hoặc xây dựng biểu mẫu** — Biểu mẫu → Tải lên XLSForm hoặc mở Form Builder
4. **Thêm người dùng** — Người dùng → Mời hoặc tạo tài khoản cho nhóm của bạn
