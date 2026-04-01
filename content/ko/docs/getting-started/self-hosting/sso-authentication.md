---
weight: 4
title: "SSO 인증"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "내장 Keycloak, 외부 OIDC 공급자 또는 Azure Active Directory를 사용하여 셀프 호스팅 rtCloud에 싱글 사인온을 구성합니다."
---

rtCloud는 싱글 사인온(SSO)을 위한 세 가지 방법을 지원합니다:

| 옵션 | 최적 사용 사례 |
|--------|----------|
| [내장 Keycloak](#embedded-keycloak) | rtCloud와 함께 번들된 완전 자립형 SSO 서버를 원하는 조직 |
| [외부 OIDC 공급자](#external-oidc-provider) | 이미 ID 공급자를 운영 중인 조직 (Auth0, Authentik, Okta, Supabase 등) |
| [Azure Active Directory](#azure-active-directory) | Microsoft 365 또는 Azure AD를 사용하는 조직 |

SSO가 구성되지 않으면 사용자는 관리 패널을 통해 관리되는 로컬 rtCloud 계정으로 로그인합니다.

---

## 내장 Keycloak {#embedded-keycloak}

배포에는 rtCloud와 함께 실행되는 선택적 Keycloak 컨테이너가 포함됩니다. Keycloak은 rtSurvey 렐름으로 사전 구성되어 즉시 사용할 수 있습니다.

### 요구 사항

- HTTPS가 있는 도메인 이름 (Keycloak은 프로덕션에서 HTTPS가 필요합니다)
- 서버에 최소 4 GB RAM (Keycloak은 약 512 MB 메모리를 추가로 사용합니다)

### 설정

**1. `.env`에서 환경 변수 구성:**

```dotenv
# 내장 Keycloak 컨테이너 활성화
EMBED_KEYCLOAK=true

# Keycloak URL — 실제 도메인 사용
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# 렐름 및 클라이언트 설정 (가져온 렐름 JSON과 일치)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak 관리자 자격 증명
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak 데이터베이스 (자동으로 생성됨)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Keycloak이 수신 대기하는 포트 (호스트 측, Nginx로 프록시)
KEYCLOAK_PORT=8091
```

**2. 내장 Keycloak 프로파일로 시작:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Keycloak이 정상인지 확인:**

```bash
docker compose -f docker-compose.production.yml ps
```

2~3분 후 `rtcloud-keycloak` 컨테이너에 `Up (healthy)`가 표시되어야 합니다.

**4. Keycloak 관리 콘솔 접속:**

```
https://rtcloud.example.com/auth/admin
```

`KEYCLOAK_ADMIN_USER` 및 `KEYCLOAK_ADMIN_PASSWORD`로 로그인합니다.

### 사전 구성된 내용

내장 Keycloak은 다음을 포함하는 사전 가져온 `rtsurvey` 렐름으로 시작합니다:

- 웹 애플리케이션에 대한 클라이언트 구성
- 기본 사용자 역할 (`admin`, `project_manager`, `enumerator`, `analyst`)
- rtSurvey에 최적화된 세션 및 토큰 설정

Keycloak 관리 콘솔에서 직접 사용자를 추가하거나 Keycloak을 업스트림 ID 공급자(LDAP, SAML)에 연결할 수 있습니다.

### Nginx 라우팅

클라우드 배포 스크립트를 사용할 때 Nginx는 두 서비스를 모두 프록시하도록 구성됩니다:

| 경로 | 백엔드 |
|------|---------|
| `/` | `127.0.0.1:8080`의 rtCloud 앱 |
| `/auth/` | `127.0.0.1:8090`의 Keycloak |

---

## 외부 OIDC 공급자 {#external-oidc-provider}

rtCloud를 OpenID Connect 호환 ID 공급자에 연결합니다. 이 방법은 Keycloak 컨테이너가 필요 없습니다.

### 지원 공급자

다음을 포함한 모든 OIDC 호환 공급자가 작동합니다:
- Authentik
- Auth0
- Okta
- Keycloak (외부 인스턴스)
- Supabase
- Google (Google Workspace 조직)
- GitHub (OIDC 확장이 있는 OAuth 앱)

### 설정

**1. ID 공급자에서 rtCloud를 OIDC 클라이언트로 등록합니다.**

다음이 필요합니다:
- **클라이언트 ID** 및 **클라이언트 시크릿**
- **리디렉션 URI** 등록: `https://rtcloud.example.com/auth/callback`
- 모바일 앱 지원을 위해 추가 등록: `vn.rta.rtsurvey.auth://callback`

**2. `.env`에서 환경 변수 구성:**

```dotenv
# OIDC 검색 URL (공급자별 — IdP 문서 확인)
OIDC_ISSUER_URL=https://your-identity-provider.com

# ID 공급자의 클라이언트 자격 증명
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# 요청할 스코프 (openid, profile, email이 일반적으로 충분)
OIDC_SCOPE=openid profile email

# ID 공급자에 등록된 리디렉션 URI
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# 선택 사항: 별도 모바일 앱 클라이언트
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# 새 OIDC 사용자를 위해 rtCloud 계정을 자동으로 생성하려면 true로 설정
OPEN_REGISTRATION=false
```

**3. 변경 사항을 적용하기 위해 앱 컨테이너를 재시작합니다:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### 사용자 자동 프로비저닝

`OPEN_REGISTRATION=true`이면 rtCloud는 사용자가 OIDC를 통해 처음 로그인할 때 자동으로 로컬 계정을 만듭니다. 계정은 ID 토큰의 사용자 이름 및 이메일로 채워집니다.

`OPEN_REGISTRATION=false` (기본값)이면 rtCloud 관리자가 먼저 사용자 계정을 만들어야 하며, OIDC ID는 첫 번째 로그인 시 연결됩니다.

### 사용자 지정 엔드포인트

공급자가 OIDC 검색(`.well-known/openid-configuration`)을 지원하지 않는 경우 엔드포인트를 수동으로 설정할 수 있습니다:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

조직의 Microsoft Azure AD 테넌트와 rtCloud를 통합합니다.

### 설정

**1. [Azure Portal](https://portal.azure.com)에서 새 앱을 등록합니다:**

   - **Azure Active Directory** → **앱 등록** → **새 등록** 이동
   - 이름: `rtCloud`
   - 리디렉션 URI: `https://rtcloud.example.com/auth/callback` (웹 유형)
   - 생성 후 **애플리케이션 (클라이언트) ID** 및 **디렉토리 (테넌트) ID**를 기록합니다
   - **인증서 및 비밀**에서 새 클라이언트 비밀을 만듭니다

**2. `.env`에서 환경 변수 구성:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. 앱 컨테이너를 재시작합니다:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

이제 Azure AD 테넌트의 사용자가 Microsoft 자격 증명을 사용하여 rtCloud에 로그인할 수 있습니다.

---

## SSO 비활성화

로컬 인증으로 되돌리려면 `.env`에서 모든 SSO 관련 변수를 제거하거나 주석 처리한 후 앱 컨테이너를 재시작합니다:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

내장 Keycloak을 사용하고 있었다면 `--profile embed-keycloak` 플래그를 생략하고 `docker compose down`을 실행한 후 프로파일 없이 `up -d`를 실행하여 중지합니다.
