---
weight: 4
title: "SSL 설정"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "rtSurvey 서버에 대해 HTTPS를 구성하십시오. 로그인하기 전에 필요합니다."
---

로그인하기 전에 SSL을 구성해야 합니다. 앱을 처음 열면 자동으로 SSL 설정 화면으로 리디렉션됩니다.

---

## SSL 설정 옵션

![SSL 설정 옵션](/img/ssl-setup/ssl-setup-options.png)

세 가지 옵션 중 하나를 선택하십시오.

| 옵션 | 언제 사용하나요? |
|--------|-------------|
| **무료 rtsurvey.com 하위 도메인** *(추천)* | DNS 설정이 필요하지 않습니다. 우리는 당신을 위해 기록을 만듭니다. 2~5분 안에 준비됩니다. |
| **내 도메인** | 이미 도메인이 있고 해당 DNS가 이 서버를 가리킵니다. |
| **수동으로 인증서 설치** | 엔터프라이즈 또는 사용자 정의 CA. SSH 액세스가 필요합니다. |

---

## 옵션 1 - 무료 rtsurvey.com 하위 도메인(권장)

이것이 가장 빠른 옵션입니다. 도메인 등록이나 DNS 변경이 필요하지 않습니다.

1. 무료 rtsurvey.com 하위 도메인을 클릭하여 섹션을 확장하세요.
2. 입력 필드에 원하는 하위 도메인 이름을 입력하세요.

   > 소문자, 숫자, 하이픈을 사용하세요. 3~30자.
   > 예: `myproject` → `myproject.rtsurvey.com`

3. 만들기를 클릭하세요 **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. 인증서가 발급되는 동안 2~5분 정도 기다립니다.

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. 인증서가 준비되면 자동으로 새 HTTPS URL로 리디렉션됩니다.

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## 옵션 2 - 내 도메인

기존 도메인이 있고 해당 DNS A 레코드가 이미 이 서버의 IP를 가리키는 경우 이를 사용하십시오.

1. 내 도메인을 클릭하여 섹션을 확장하세요.
2. 전체 도메인 이름을 입력하세요. (e.g. `survey.myorganization.org`)
3. 인증서 생성을 클릭하세요.

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt가 도메인을 확인하고 인증서를 발급합니다. 이를 위해서는 DNS가 먼저 올바르게 지정되어야 합니다. 그렇지 않으면 요청이 실패합니다.

---

## 옵션 3 - 인증서를 수동으로 설치

사용자 정의 또는 내부 CA를 사용하는 엔터프라이즈 환경의 경우. SSH를 통해 서버에 인증서 파일을 배치한 다음 앱에 도메인을 입력합니다.

### 전제조건

- 서버에 대한 SSH 액세스
- 도메인에 대한 유효한 인증서 및 개인 키(PEM 형식)

### 1단계 - 서버에 SSH로 연결

```bash
ssh root@<server-ip>
```

### 2단계 - 인증서 파일 배치

디렉터리를 만들고 파일을 복사합니다.

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

파일을 다음과 같은 정확한 이름으로 해당 디렉터리에 복사하세요.

| 파일 | 설명 |
|------|-------------|
| `fullchain.pem` | 인증서 + 중간 CA 인증서(연결됨) |
| `privkey.pem` | 귀하의 개인 키 |

예:

```bash
# 로컬 컴퓨터에서 복사(서버가 아닌 로컬로 실행)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

올바른 권한을 설정하십시오.

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### 3단계 - 앱에 도메인을 입력하세요

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. SSL 설정 화면에서 수동으로 인증서 설치를 클릭하세요.
2. 도메인 이름을 입력하세요(인증서의 일반 이름 또는 SAN과 일치해야 함).
3. 적용을 클릭하세요

서버는 인증서로 Nginx를 구성하고 자동으로 다시 로드합니다.

---

## 다음 단계

SSL이 활성화되면 첫 번째 로그인으로 진행합니다 [first-login](first-login).
