---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "gcp-compute.sh 시작 스크립트를 사용하여 Google Cloud Compute Engine에 rtCloud를 배포합니다."
---

Compute Engine VM 인스턴스를 만들 때 `gcp-compute.sh`를 **시작 스크립트**로 사용합니다. 스크립트는 첫 번째 부팅 시 자동으로 실행됩니다.

**스크립트 다운로드:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## 1단계 — 구성 입력

스크립트를 열고 상단의 `CONFIGURATION` 블록을 편집합니다:

```bash
# --- 필수 ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # 첫 로그인 후 변경

# --- 도메인 + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- 내장 Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # ADMIN_PASSWORD로 기본 설정
```

| 필드 | 필수 | 설명 |
|-------|----------|-------------|
| `PROJECT_ID` | 예 | 데이터베이스 이름 및 Keycloak 클라이언트 ID로 사용됩니다. 소문자, 공백 없음. |
| `ADMIN_PASSWORD` | 아니오 | 앱 관리자 비밀번호 및 Keycloak 관리자 비밀번호. 기본값은 `admin` — **첫 로그인 후 변경**. |
| `DOMAIN` | 아니오 | HTTPS용 도메인. HTTP 전용 모드는 공백으로 두세요. |
| `LETSENCRYPT_EMAIL` | 예 (DOMAIN 설정 시) | Let's Encrypt 알림용 이메일. |
| `EMBED_KEYCLOAK` | 아니오 | 내장 Keycloak 배포는 `true` (4 GB RAM 필요). |

> **보안:** 모든 비밀번호는 기본적으로 `admin`입니다. 첫 번째 로그인 후 즉시 변경하세요.

---

## 2단계 — VM 인스턴스 만들기

[Google Cloud Console](https://console.cloud.google.com/compute)에서:

1. **인스턴스 만들기** 클릭
2. **머신 구성:**
   - 시리즈: `E2`
   - 머신 유형: `e2-medium` (4 GB RAM) 이상
3. **부팅 디스크:**
   - 운영 체제: Ubuntu
   - 버전: Ubuntu 22.04 LTS
   - 크기: 40 GB 이상
4. **방화벽:** **HTTP 트래픽 허용** 및 **HTTPS 트래픽 허용** 체크
5. **고급 옵션** → **관리** → **자동화** → **시작 스크립트** → 전체 스크립트 내용 붙여넣기
6. **만들기** 클릭

---

## 3단계 — DNS 레코드 추가

VM이 부팅되는 동안 DNS 공급자에 **A 레코드**를 추가합니다:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

콘솔의 VM 인스턴스 목록에서 외부 IP를 확인하세요.

---

## 4단계 — 진행 상황 모니터링

`gcloud` CLI 사용:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

또는 직접 SSH:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## 5단계 — 앱 접속

설정이 완료되면 로그에 앱 URL 및 자격 증명이 포함된 요약이 표시됩니다. 사용자명 `admin`, 비밀번호 `admin`으로 로그인한 후 즉시 비밀번호를 변경하세요.

---

## 방화벽 규칙

GCP의 **HTTP/HTTPS 허용** 체크박스는 포트 80 및 443을 엽니다. 포트 3838에서 Shiny 직접 접근도 허용하려면 방화벽 규칙을 추가합니다:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

또는 콘솔을 통해 추가: **VPC 네트워크** → **방화벽** → **규칙 만들기**.

> 포트 3306 (MySQL)을 **열지 마세요** — 절대 공개적으로 접근 가능해서는 안 됩니다.

---

## 고정 IP (선택 사항)

GCP는 기본적으로 VM 재시작 시 변경되는 임시 외부 IP를 할당합니다. 안정적인 IP를 유지하려면:

1. **VPC 네트워크** → **IP 주소** 이동
2. **외부 고정 주소 예약** 클릭
3. VM 인스턴스에 할당

---

## 배포 후

### 비밀번호 변경

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 모든 컨테이너 보기

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
