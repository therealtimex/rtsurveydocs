---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "자동화된 user-data 스크립트를 사용하여 DigitalOcean Droplet에 rtCloud를 배포합니다."
---

DigitalOcean은 첫 번째 부팅 시 자동으로 실행되는 **User Data** 스크립트를 사용합니다. 스크립트 상단의 구성 변수를 입력한 후 Droplet 생성 시 전체 스크립트를 붙여넣습니다.

> Linode StackScript와 달리 DigitalOcean에는 양식 UI가 없습니다 — 붙여넣기 전에 스크립트를 직접 편집해야 합니다.

**스크립트 다운로드:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## 내장 Keycloak (권장)

내장 SSO를 통한 가장 단순한 설정을 위해 `digitalocean-droplet-keycloak-embed.sh`를 사용하세요.

### 1단계 — 구성 입력

스크립트를 열고 상단의 `CONFIGURATION` 블록을 편집합니다:

```bash
# --- 필수 ---
PROJECT_ID="rtsurvey"                  # 프로젝트의 고유 식별자 (공백 없음)
ADMIN_PASSWORD="admin"                 # 앱 관리자 및 Keycloak 비밀번호 — 첫 로그인 후 변경

# --- 도메인 + SSL ---
DOMAIN="myapp.example.com"            # 도메인 — DNS A 레코드가 여기를 가리켜야 함
PROJECT_URL=""                         # Cloudflare/프록시 뒤에 있지 않으면 공백으로 두세요
LETSENCRYPT_EMAIL="admin@example.com" # Let's Encrypt 알림용 이메일

# --- 선택 사항 ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| 필드 | 필수 | 설명 |
|-------|----------|-------------|
| `PROJECT_ID` | 예 | 데이터베이스 이름 및 Keycloak 클라이언트 ID로 사용됩니다. 소문자, 공백 없음. |
| `ADMIN_PASSWORD` | 아니오 | 앱 관리자 로그인 및 Keycloak 관리 콘솔 비밀번호. 기본값은 `admin` — **첫 로그인 후 변경**. |
| `DOMAIN` | 예 | 도메인 이름. DNS A 레코드가 Droplet IP를 가리켜야 합니다. |
| `LETSENCRYPT_EMAIL` | 예 | Let's Encrypt 인증서 알림용 이메일 주소. |
| `PROJECT_URL` | 아니오 | 공개 URL 재정의. `DOMAIN`을 사용하려면 공백으로 두세요. Cloudflare 뒤에서 유용합니다. |

> **보안:** 모든 비밀번호는 기본적으로 `admin`입니다. 첫 번째 로그인 후 즉시 변경하세요.

### 2단계 — Droplet 생성

[DigitalOcean 제어 패널](https://cloud.digitalocean.com)에서:

1. **만들기** → **Droplets** 클릭
2. 이미지로 **Ubuntu 22.04 LTS** 선택
3. **Basic, 4 GB RAM / 2 vCPUs** 이상 선택
4. **고급 옵션** 스크롤 → **초기화 스크립트 추가** 체크
5. 텍스트 영역에 전체 스크립트 내용 붙여넣기
6. **Droplet 만들기** 클릭

### 3단계 — DNS 레코드 추가

Droplet이 부팅되는 동안 DNS 공급자에 **A 레코드**를 추가합니다:

```
Type  : A
Name  : myapp          (또는 루트 도메인의 경우 @)
Value : <droplet-ip>
TTL   : 300
```

### 4단계 — 진행 상황 모니터링

Droplet에 SSH로 접속하여 로그를 봅니다:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

스크립트는 시작 부분에 서버 IP를 출력합니다 — 표시되자마자 DNS 레코드를 추가하세요.

### 5단계 — 앱 접속

설정이 완료되면 로그에 요약이 표시됩니다:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

브라우저에서 `https://myapp.example.com`을 열고 사용자명 `admin`, 비밀번호 `admin`으로 로그인합니다.

> 로그인 후 즉시 오른쪽 상단 메뉴의 **설정**을 통해 **비밀번호를 변경**하세요.

---

## 배포 후

### 비밀번호 변경

Droplet에 SSH로 접속하여 `.env`를 편집하고 영향받는 컨테이너를 재시작합니다:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 도메인 업데이트

배포 후 다른 도메인을 할당하는 경우 `.env`의 `PROJECT_URL`을 업데이트합니다:

```bash
nano /opt/rtcloud/.env   # PROJECT_URL= 업데이트
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 모든 컨테이너 보기

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
