---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Triển khai rtCloud trên Linode bằng StackScript. Không cần cấu hình — chỉ cần tạo máy chủ và làm theo các bước sau khi triển khai."
---

## Bước 1 - Khởi chạy StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Thao tác này sẽ mở trang StackScript trong Linode Cloud Manager. Nhấp vào **Triển khai Linode mới**.

---

## Bước 2 - Điền vào biểu mẫu của Linode

Điền vào form tạo server chuẩn của Linode:

| Lĩnh vực | Giá trị đề xuất |
|-------|-------------------|
| **Hình ảnh** | Ubuntu 22.04 LTS |
| **Vùng** | Gần gũi nhất với người dùng của bạn |
| **Kế hoạch** | CPU dùng chung 4 GB trở lên |
| **Mật khẩu gốc** | Đặt mật khẩu mạnh |
| **Múi giờ** *(trường duy nhất của chúng tôi)* | Múi giờ máy chủ của bạn (mặc định: `Châu Á/Ho_Chi_Minh`) |

Nhấp vào **Tạo Linode** khi hoàn tất.

---

## Bước 3 - Đợi quá trình thiết lập hoàn tất

Tập lệnh chạy tự động trong lần khởi động đầu tiên. Nó cài đặt Docker, lấy hình ảnh rtSurvey, khởi tạo cơ sở dữ liệu và khởi động tất cả các dịch vụ. Quá trình này mất **5–10 phút**.

Bạn có thể xem tiến trình trực tiếp trong **Linode Cloud Manager** — không cần SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Nhấp vào Linode mới tạo của bạn
3. Nhấp vào **Khởi chạy LISH Console** (trên cùng bên phải của trang chi tiết Linode)

Một thiết bị đầu cuối của trình duyệt mở ra hiển thị nhật ký khởi động trực tiếp — tab **Weblish** hoạt động trực tiếp trong trình duyệt của bạn, không cần ứng dụng khách SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Đợi cho đến khi bạn thấy:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Nhật ký cũng hiển thị IP máy chủ của bạn — bạn sẽ cần nó cho bước tiếp theo.

---

## Bước 4 - Thiết lập SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Làm theo **[Hướng dẫn thiết lập SSL →](../ssl-setup)** để định cấu hình HTTPS. **Tên miền phụ rtsurvey.com** miễn phí là tùy chọn nhanh nhất — không cần thiết lập DNS.

---

## Bước 5 - Đăng nhập lần đầu

Khi SSL được kích hoạt, hãy làm theo **[Hướng dẫn đăng nhập lần đầu →](../first-login)** để truy cập tài khoản quản trị viên.

---

## Bước 6 - Thay đổi mật khẩu mặc định

Tất cả mật khẩu mặc định là `admin`. Thay đổi chúng ngay sau lần đăng nhập đầu tiên của bạn:

- **Mật khẩu quản trị viên ứng dụng** — cài đặt tài khoản bên trong ứng dụng
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Quy tắc tường lửa (Tường lửa đám mây Linode)

Nếu bạn đính kèm Tường lửa đám mây Linode vào máy chủ này, hãy sử dụng các quy tắc sau:

### Nhập về

| Nhãn | Hành động | Giao thức | Cảng | Nguồn | Ghi chú |
|-------|--------|----------|------|----------|-------|
| `chấp nhận-vào-ssh` | Chấp nhận | TCP | 22 | Tất cả IPv4, Tất cả IPv6 | Truy cập SSH |
| `chấp nhận-vào-http` | Chấp nhận | TCP | 80 | Tất cả IPv4, Tất cả IPv6 | Nginx (Thử thách HTTP + ACME) |
| `chấp nhận-vào-https` | Chấp nhận | TCP | 443 | Tất cả IPv4, Tất cả IPv6 | Nginx (HTTPS sau khi thiết lập SSL) |
| `chấp nhận-vào-sáng bóng` | Chấp nhận | TCP | 3838 | Tất cả IPv4, Tất cả IPv6 | Máy chủ sáng bóng (phân tích R) |
| `chấp nhận-inbound-icmp` | Chấp nhận | ICMP | — | Tất cả IPv4, Tất cả IPv6 | Ping / chẩn đoán |
| Chính sách gửi đến mặc định | **Thả** | | | | Chặn mọi thứ khác |

### Đi

| Nhãn | Hành động | Ghi chú |
|-------|--------|-------|
| Chính sách gửi đi mặc định | **Chấp nhận** | Cho phép tất cả các dữ liệu gửi đi (Docker pull, certbot, GoDaddy API, v.v.) |

### Cổng KHÔNG cần thiết bên ngoài

Các cổng này chỉ được liên kết với `127.0.0.1` và không bao giờ có thể truy cập được từ bên ngoài máy chủ:

| Cảng | Dịch vụ | Lý do |
|------|----------|--------|
| 8080 | Vùng chứa ứng dụng | Proxy Nginx cho nó trong nội bộ |
| 8090 | Hộp đựng chìa khóa | Proxy Nginx cho nó trong nội bộ |
| 3306 | MySQL | Chỉ mạng Docker nội bộ |

---

## Khắc phục sự cố

### Kiểm tra nhật ký thiết lập

```bash
tail -200 /var/log/stackscript.log
```

### Kiểm tra nhật ký SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Xem trạng thái vùng chứa

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
