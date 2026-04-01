---
weight: 2
title: "구성 참조"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "셀프 호스팅 rtCloud 배포를 구성하는 데 사용되는 모든 환경 변수에 대한 전체 참조."
---

모든 구성은 배포 디렉토리 루트의 `.env` 파일에 있는 환경 변수를 통해 수행됩니다. Docker Compose는 이 파일을 자동으로 읽으므로 `--env-file` 플래그가 필요 없습니다.

**필수**로 표시된 변수는 컨테이너를 시작하기 전에 설정해야 합니다. 나머지는 기본값이 있으며 선택 사항입니다.

---

## 프로젝트

이 변수들은 rtCloud 인스턴스의 ID와 접근 지점을 정의합니다.

| 변수 | 기본값 | 필수 | 설명 |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **예** | 이 배포의 고유 식별자. 공백 또는 특수 문자 없음. 내부 이름 지정의 접두사로 사용. |
| `PROJECT_URL` | — | **예** | 사용자가 앱에 접근하는 도메인 이름 또는 IP 주소 (예: `rtcloud.example.com` 또는 `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | 아니오 | 활성화할 플랫폼 변형. 옵션: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | 아니오 | 컨테이너 내부에서 애플리케이션이 수신 대기하는 포트. 내용을 알지 못하면 변경하지 마세요. |
| `HTTP_PROTOCOL` | `https` | 아니오 | 내부 URL을 구성하는 데 사용되는 프로토콜. SSL을 사용하지 않는 경우 `http`로 설정. |

---

## 데이터베이스

MySQL 연결 자격 증명. 데이터베이스는 MySQL 컨테이너에서 자동으로 관리됩니다 — 강력한 비밀번호만 설정하면 됩니다.

| 변수 | 기본값 | 필수 | 설명 |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | 아니오 | 애플리케이션 데이터베이스 이름. |
| `MYSQL_USER` | `smartsurvey` | 아니오 | 애플리케이션의 MySQL 사용자. |
| `MYSQL_PASSWORD` | — | **예** | `MYSQL_USER`의 비밀번호. 강력하고 고유한 값을 사용하세요. |
| `MYSQL_ROOT_PASSWORD` | — | **예** | MySQL 루트 비밀번호. 데이터베이스 초기화 및 관리 작업에 필요. |
| `MYSQL_HOST` | `mysql` | 아니오 | MySQL 호스트명. 외부 데이터베이스에 연결하지 않는 한 기본값을 사용하세요. |
| `MYSQL_PORT` | `3306` | 아니오 | MySQL 포트. |

---

## 관리자 계정

관리자 계정은 새 데이터베이스의 첫 번째 부팅 시 자동으로 생성됩니다.

| 변수 | 기본값 | 필수 | 설명 |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **예** | 내장 `admin` 사용자의 비밀번호. 첫 번째 부팅 전에 설정하세요. 데이터베이스가 이미 존재하는 경우 효과 없음. |

> 첫 번째 로그인 후 웹 UI의 **계정 설정** 페이지에서 관리자 비밀번호를 변경하세요.

---

## 포트

애플리케이션이 바인딩하는 호스트 포트를 제어합니다.

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `APP_PORT` | `8080` | 메인 웹 UI의 호스트 포트. 서버에서 포트 8080이 이미 사용 중인 경우 변경하세요. |
| `SHINY_PORT` | `3838` | Shiny 분석 서버의 호스트 포트. |

---

## 런타임

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | 런타임 환경. 프로덕션 배포에는 `prod`, 로컬 개발에는 `dev`를 사용하세요. |
| `RUN_MODE` | `admin` | 컨테이너 역할. `admin`은 전체 스택(웹 + 큐 + 크론)을 실행합니다. `worker`는 백그라운드 처리만 실행합니다(수평 확장용). |
| `TZ` | `Asia/Ho_Chi_Minh` | 서버 시간대. 로그 타임스탬프, 크론 스케줄 및 날짜 표시에 영향을 줍니다. [TZ 데이터베이스 이름](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)을 사용하세요(예: `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | 애플리케이션 로그 상세도. 옵션: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | 모든 Docker 컨테이너 및 볼륨 이름에 적용되는 접두사. 동일한 호스트에서 여러 rtCloud 인스턴스를 실행할 때 변경하세요. |
| `RESTART_POLICY` | `unless-stopped` | Docker 컨테이너 재시작 동작. 옵션: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | 사용할 Docker 이미지. 특정 버전을 고정하려면 태그를 변경하세요. |
| `REQUIRE_LICENSE` | `false` | 시작 시 라이선스 키 유효성 검사 활성화. 라이선스 정보는 RTA에 문의하세요. |

---

## 보안

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | CSRF 토큰 유효성 검사 활성화. 프로덕션에서는 `true`로 유지하세요. `400 CSRF token could not be verified` 오류가 발생하는 경우 로컬 개발에서만 `false`로 설정하세요. |
| `GII_ENABLED` | `false` | Yii 프레임워크 코드 생성기 도구 활성화. **프로덕션에서 절대 활성화하지 마세요.** |

---

## SSO — 내장 Keycloak

전체 기능의 엔터프라이즈 SSO를 위한 번들 Keycloak 컨테이너를 활성화합니다. HTTPS가 있는 도메인이 필요합니다.

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | 내장 Keycloak 컨테이너를 시작하려면 `true`로 설정. `embed-keycloak` Docker Compose 프로파일을 활성화합니다. |
| `KEYCLOAK_URL` | — | Keycloak 서버의 전체 URL (예: `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak 렐름 이름 (예: `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | rtCloud 애플리케이션의 Keycloak 클라이언트 ID. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak 클라이언트 시크릿. Keycloak 관리 콘솔에서 생성하세요. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak 관리자 사용자명. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak 관리자 비밀번호. |
| `KEYCLOAK_DB` | `keycloak` | Keycloak의 데이터베이스 이름. 첫 번째 부팅 시 자동으로 생성됩니다. |
| `KEYCLOAK_DB_USER` | `keycloak` | Keycloak의 데이터베이스 사용자. |
| `KEYCLOAK_DB_PASSWORD` | — | Keycloak 사용자의 데이터베이스 비밀번호. |
| `KC_HOSTNAME` | — | Keycloak 프론트엔드 URL (예: `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | 엄격한 호스트명 매칭 적용. 고정된 도메인이 있는 프로덕션에서는 `true`로 설정. |

전체 설정 가이드는 [SSO 인증](sso-authentication#embedded-keycloak)을 참조하세요.

---

## SSO — 외부 OIDC 공급자

기존 OIDC 호환 ID 공급자(Supabase, Auth0, Authentik, Okta 등)에 연결합니다.

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC 발급자 검색 URL (예: `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | ID 공급자에 등록된 클라이언트 ID. |
| `OIDC_CLIENT_SECRET` | — | ID 공급자의 클라이언트 시크릿. |
| `OIDC_SCOPE` | `openid profile email` | 요청할 OIDC 스코프의 공백으로 구분된 목록. |
| `OIDC_REDIRECT_URI` | — | 웹 앱의 콜백 URL (예: `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | rtSurvey 모바일 앱을 위한 별도 클라이언트 ID. |
| `OIDC_MOBILE_REDIRECT_URI` | — | 모바일 앱 콜백 URI (예: `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | OIDC를 통해 처음 인증하는 사용자를 위해 rtCloud 계정을 자동으로 생성. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | 인증 엔드포인트 URL 재정의 (검색 사용은 공백). |
| `OIDC_TOKEN_ENDPOINT` | — | 토큰 엔드포인트 URL 재정의 (검색 사용은 공백). |
| `OIDC_USERINFO_ENDPOINT` | — | 사용자 정보 엔드포인트 URL 재정의 (검색 사용은 공백). |

---

## SSO — Azure Active Directory

| 변수 | 설명 |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD 애플리케이션 (클라이언트) ID. |
| `AZURE_TENANT_ID` | Azure AD 디렉토리 (테넌트) ID. |

---

## 선택적 통합

### Stata

| 변수 | 기본값 | 설명 |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | 데이터 분석을 위한 Stata 통계 소프트웨어 통합 활성화. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | 컨테이너 내부 Stata 바이너리의 절대 경로. |

### Elasticsearch

| 변수 | 설명 |
|----------|-------------|
| `ES_HOST` | Elasticsearch 호스트 (예: `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch 포트. |

### Matomo 분석

| 변수 | 설명 |
|----------|-------------|
| `PIWIK_URL` | Matomo(Piwik) 서버 URL. |
| `PIWIK_ID` | Matomo 사이트 ID. |
| `PIWIK_SECRET` | Matomo 인증 토큰. |

### OpenCPU (R 계산)

| 변수 | 설명 |
|----------|-------------|
| `OCPU_HOST` | R 기반 통계 계산을 위한 OpenCPU 서버 URL. |

### RtBox 통합

| 변수 | 설명 |
|----------|-------------|
| `RTBOX_HOST` | RtBox 서비스 호스트 URL. |
| `RTBOX_USER_API` | RtBox 사용자 API 키. |
| `RTBOX_BASIC_AUTH` | RtBox의 기본 인증 자격 증명. |

### Matrix 메시징

| 변수 | 설명 |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix 홈서버 호스트. |
| `MATRIX_HOMESERVER_PORT` | Matrix 홈서버 포트. |

---

## 데이터 볼륨

모든 애플리케이션 데이터는 명명된 Docker 볼륨에 저장됩니다. 볼륨은 첫 번째 시작 시 자동으로 생성되며 컨테이너 재시작 및 업데이트에도 유지됩니다.

| 볼륨 | 마운트 지점 | 내용 |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL 데이터베이스 파일 |
| `rtcloud_uploads` | `…/uploads` | 설문 응답자가 업로드한 파일 |
| `rtcloud_audios` | `…/audios` | 오디오 녹음 |
| `rtcloud_downloads` | `…/downloads` | 생성된 내보내기 파일 |
| `rtcloud_gallery` | `…/gallery` | 갤러리 이미지 |
| `rtcloud_voicemail` | `…/voicemail` | 음성 메일 녹음 |
| `rtcloud_analytics` | `…/analytics` | 분석 데이터 |
| `rtcloud_aggregate` | `…/aggregate` | 집계된 설문 결과 |
| `rtcloud_converter` | `…/converter` | 데이터 변환 출력 |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny 서버 R 스크립트 |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny 서버 로그 |
| `rtcloud_assets` | `…/assets` | 웹 자산 (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | 애플리케이션 런타임 캐시 |
| `rtcloud_cache` | `…/cache` | 애플리케이션 캐시 |
| `rtcloud_tmp` | `…/tmp` | 임시 파일 |

볼륨 이름은 `COMPOSE_PROJECT_NAME` 값(기본값: `rtcloud`)으로 접두사가 붙습니다.

배포의 모든 볼륨 나열:

```bash
docker volume ls | grep rtcloud
```
