---
weight: 1
title: "빠른 시작"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Docker Compose를 사용하여 10분 이내에 자체 서버에서 rtCloud를 실행합니다."
---

이 가이드는 처음부터 Linux 서버에서 셀프 호스팅 rtCloud 인스턴스를 배포하는 과정을 안내합니다. 완료하면 브라우저에서 접근할 수 있는 rtCloud가 실행됩니다.

## 사전 요구 사항

시작하기 전에 서버가 다음 요구 사항을 충족하는지 확인하세요:

### 하드웨어

| 리소스 | 최소 | 권장 |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| 디스크 | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |

### 소프트웨어

| 소프트웨어 | 버전 |
|----------|---------|
| OS | Ubuntu 20.04 LTS 이상 (또는 Docker를 지원하는 모든 Linux) |
| Docker | 20.10 이상 |
| Docker Compose | v2.x (`docker compose`) 또는 v1.x (`docker-compose`) |

**Ubuntu에 Docker 설치:**

```bash
curl -fsSL https://get.docker.com | sh
```

설치 확인:

```bash
docker --version
docker compose version
```

---

## 1단계 — 파일 가져오기

배포 리포지토리를 서버에 복제합니다:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## 2단계 — 환경 구성

샘플 구성 파일을 복사합니다:

```bash
cp .env.production.sample .env
```

텍스트 편집기에서 `.env`를 열고 필수 값을 입력합니다:

```dotenv
# 이 배포의 고유 식별자 (공백 없음, 특수 문자 없음)
PROJECT_ID=myproject

# 사용자가 앱에 접근할 도메인 또는 IP 주소
# 예: rtcloud.example.com  또는  192.168.1.100
PROJECT_URL=rtcloud.example.com

# 프로토콜: SSL이 있는 도메인이면 "https", 그렇지 않으면 "http"
HTTP_PROTOCOL=https

# 강력하고 고유한 비밀번호 — 시작 전에 세 가지 모두 변경
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **중요:** Docker Compose는 `.env`만 자동으로 읽습니다. `.env.production`이라는 파일을 생성하지 마세요. 혼란을 야기할 수 있습니다. `ADMIN_PASSWORD`는 새 데이터베이스의 **첫 번째 부팅** 시에만 적용됩니다.

---

## 3단계 — 컨테이너 시작

백그라운드에서 모든 서비스를 실행합니다:

```bash
docker compose -f docker-compose.production.yml up -d
```

첫 번째 시작 시 Docker가 다음을 수행하는 동안 **3~5분** 소요됩니다:

1. rtCloud 애플리케이션 이미지 가져오기 (~1 GB 다운로드)
2. MySQL 데이터베이스 초기화
3. 기본 스키마 로드
4. 보류 중인 모든 데이터베이스 마이그레이션 실행

실시간으로 시작 진행 상황 모니터링:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

애플리케이션이 준비되었음을 나타내는 출력이 나타날 때까지 기다립니다. 컨테이너 상태도 확인할 수 있습니다:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## 4단계 — 애플리케이션 접속

두 컨테이너 모두 `Up (healthy)` 상태를 표시하면 브라우저를 엽니다:

```
http://<PROJECT_URL>:8080
```

관리자 계정으로 로그인합니다:

| 필드 | 값 |
|-------|-------|
| 사용자명 | `admin` |
| 비밀번호 | `.env`에서 `ADMIN_PASSWORD`에 설정한 값 |

> 첫 번째 로그인 후 즉시 계정 설정 페이지에서 관리자 비밀번호를 변경하세요.

---

## 5단계 — 모든 서비스 확인

모든 컨테이너가 실행 중이고 정상인지 확인합니다:

```bash
docker compose -f docker-compose.production.yml ps
```

예상 출력:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

컨테이너가 `Up (starting)` 또는 `Up (unhealthy)` 상태를 표시하면 30~60초 더 기다린 후 다시 확인하세요. MySQL은 첫 번째 부팅 시 완전히 초기화하는 데 최대 1분 걸릴 수 있습니다.

---

## 포트 참조

| 포트 | 서비스 | 설명 |
|------|---------|-------------|
| `8080` | rtCloud 앱 | 메인 웹 UI (`APP_PORT`를 통해 구성 가능) |
| `3838` | Shiny 서버 | 분석 및 R 기반 시각화 (`SHINY_PORT`를 통해 구성 가능) |

MySQL(포트 3306) 및 선택적 서비스(Keycloak)는 내부 전용이며 기본적으로 호스트에 노출되지 않습니다.

---

## 다음 단계

rtCloud 인스턴스가 이제 실행 중입니다. 다음 후속 작업을 고려하세요:

- **HTTPS 활성화** — 서버에 도메인을 연결하고 Let's Encrypt로 SSL을 구성합니다. 자동화된 HTTPS 설정은 [클라우드 배포](cloud-deployment)를 참조하세요.
- **모든 설정 검토** — [구성 참조](configuration)를 탐색하여 프로덕션 배포를 조정하세요.
- **SSO 설정** — 중앙 집중식 사용자 인증을 위해 ID 공급자를 연결합니다. [SSO 인증](sso-authentication)을 참조하세요.
- **백업 계획** — 백업 및 업그레이드 절차는 [유지 관리](maintenance) 페이지를 검토하세요.
