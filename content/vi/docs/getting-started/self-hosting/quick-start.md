---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Bắt đầu nhanh"
icon: "play_circle"
toc: true
description: "Triển khai rtCloud trên máy chủ của bạn trong vài phút với script tự động."
---

Hướng dẫn này giúp bạn chạy rtCloud trên máy chủ của riêng mình. Các script tự động xử lý tất cả — Docker, SSL, cơ sở dữ liệu, tường lửa — chỉ trong một lần chạy.

## Yêu cầu

### Máy chủ

| Tài nguyên | Tối thiểu | Khuyến nghị |
|-----------|---------|-----------|
| RAM | 2 GB | 4 GB (bắt buộc khi dùng Keycloak SSO) |
| Ổ đĩa | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| HĐH | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Tên miền

Bạn cần tên miền với **bản ghi A trỏ đến IP máy chủ** trước khi chạy script. Let's Encrypt yêu cầu phân giải DNS để cấp chứng chỉ SSL.

---

## Chọn nhà cung cấp đám mây

Chọn nhà cung cấp bên dưới. Mỗi nhà cung cấp có script tự động chạy khi khởi động lần đầu và hoàn thành cài đặt trong **5–10 phút**.

| Nhà cung cấp | Hướng dẫn |
|------------|---------|
| Linode (Akamai) | [Triển khai trên Linode](../cloud-deployment/linode) — dễ nhất, thiết lập qua biểu mẫu với StackScript |
| DigitalOcean | [Triển khai trên DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Triển khai trên AWS](../cloud-deployment/aws) |
| Google Cloud | [Triển khai trên GCP](../cloud-deployment/gcp) |

> **Khuyến nghị cho hầu hết người dùng:** Bắt đầu với Linode — StackScript cung cấp giao diện dựa trên biểu mẫu nên không cần chỉnh sửa thủ công.
