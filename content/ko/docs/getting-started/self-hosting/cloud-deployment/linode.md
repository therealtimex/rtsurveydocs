---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "StackScript를 사용하여 Linode에 rtCloud를 배포합니다. 구성이 필요하지 않습니다. 서버를 생성하고 배포 후 단계를 따르기만 하면 됩니다."
---

## 1단계 - StackScript 실행

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Linode Cloud Manager에서 StackScript 페이지가 열립니다. **새 Linode 배포**를 클릭합니다.

---

## 2단계 - Linode 양식 작성

Linode의 표준 서버 생성 양식을 작성하십시오.

| 필드 | 권장값 |
|-------|------|
| **이미지** | 우분투 22.04 LTS |
| **지역** | 사용자에게 가장 가까운 |
| **계획** | 공유 CPU 4GB 이상 |
| **루트 비밀번호** | 강력한 비밀번호 설정 |
| **시간대** *(유일한 필드)* | 서버 시간대(기본값: `Asia/Ho_Chi_Minh`) |

완료되면 **Linode 만들기**를 클릭하세요.

---

## 3단계 — 설정이 완료될 때까지 기다립니다.

스크립트는 처음 부팅할 때 자동으로 실행됩니다. Docker를 설치하고, rtSurvey 이미지를 가져오고, 데이터베이스를 초기화하고, 모든 서비스를 시작합니다. **5~10분** 정도 걸립니다.

**Linode Cloud Manager**에서 직접 진행 상황을 볼 수 있습니다. SSH가 필요하지 않습니다.

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. 새로 생성된 Linode를 클릭하세요.
3. **Launch LISH Console**을 클릭합니다(Linode 세부정보 페이지 오른쪽 상단).

라이브 부팅 로그를 보여주는 브라우저 터미널이 열립니다. **Weblish** 탭은 브라우저에서 직접 작동하며 SSH 클라이언트가 필요하지 않습니다.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

다음이 표시될 때까지 기다리세요.

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

로그에는 서버 IP도 표시됩니다. 이는 다음 단계에 필요합니다.

---

## 4단계 - SSL 설정

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

**[SSL 설정 가이드 →](../ssl-setup)**에 따라 HTTPS를 구성하세요. 무료 **rtsurvey.com 하위 도메인**은 가장 빠른 옵션입니다. DNS 설정이 필요하지 않습니다.

---

## 5단계 — 첫 번째 로그인

SSL이 활성화되면 **[첫 로그인 안내 →](../first-login)**에 따라 관리자 계정에 접근하세요.

---

## 6단계 — 기본 비밀번호 변경

모든 비밀번호는 기본적으로 'admin'입니다. 처음 로그인한 후 즉시 변경하십시오.

- **앱 관리자 비밀번호** — 앱 내부 계정 설정
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## 방화벽 규칙(Linode 클라우드 방화벽)

Linode Cloud Firewall을 이 서버에 연결하는 경우 다음 규칙을 사용하십시오.

### 인바운드

| 라벨 | 액션 | 프로토콜 | 포트 | 출처 | 메모 |
|-------|---------|----------|------|---------|-------|
| `수락-인바운드-ssh` | 동의 | TCP | 22 | 모든 IPv4, 모든 IPv6 | SSH 액세스 |
| `수락-인바운드-http` | 동의 | TCP | 80 | 모든 IPv4, 모든 IPv6 | Nginx(HTTP + ACME 챌린지) |
| `수락-인바운드-https` | 동의 | TCP | 443 | 모든 IPv4, 모든 IPv6 | Nginx(SSL 설정 후 HTTPS) |
| `수락-인바운드-빛나` | 동의 | TCP | 3838 | 모든 IPv4, 모든 IPv6 | 샤이니 서버(R 분석) |
| `수락-인바운드-icmp` | 동의 | ICMP | — | 모든 IPv4, 모든 IPv6 | 핑/진단 |
| 기본 인바운드 정책 | **드롭** | | | | 다른 모든 항목 차단 |

### 아웃바운드

| 라벨 | 액션 | 메모 |
|-------|---------|-------|
| 기본 아웃바운드 정책 | **수락** | 모든 아웃바운드 허용(Docker pull, certbot, GoDaddy API 등) |

### 외부에는 포트가 필요하지 않습니다.

이러한 포트는 '127.0.0.1'에만 바인딩되어 있으며 서버 외부에서는 연결할 수 없습니다.

| 포트 | 서비스 | 이유 |
|------|---------|---------|
| 8080 | 앱 컨테이너 | Nginx는 내부적으로 프록시를 사용합니다 |
| 8090 | 열쇠망토 컨테이너 | Nginx는 내부적으로 프록시를 사용합니다 |
| 3306 | MySQL | 내부 Docker 네트워크만 |

---

## 문제 해결

### 설정 로그를 확인하세요

```bash
tail -200 /var/log/stackscript.log
```

### SSL 로그를 확인하세요

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### 컨테이너 상태 보기

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
