---
weight: 115
title: "셀프 호스팅"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Docker를 사용하여 자체 rtCloud 인스턴스를 배포하고 관리합니다. 데이터, 인프라 및 구성에 대한 완전한 제어권을 가집니다."
---

Docker Compose를 사용하여 자체 인프라에서 rtCloud를 실행하세요. 셀프 호스팅은 데이터, 네트워크 및 배포 환경에 대한 완전한 소유권을 제공하며, 데이터 거주 요구 사항, 에어갭 네트워크 또는 맞춤형 인프라 요구가 있는 조직에 이상적입니다.

## rtCloud 셀프 호스팅이란?

rtCloud 셀프 호스팅은 모든 Linux 서버에서 실행할 수 있는 이식 가능한 컨테이너 스택으로 전체 rtCloud 플랫폼을 패키징한 공식 Docker 이미지입니다. 스택에는 다음이 포함됩니다:

| 서비스 | 설명 |
|---------|-------------|
| **rtCloud 앱** | 내장 백그라운드 큐(Beanstalkd), 분석 서버(Shiny), 예약 작업이 있는 Apache 2.4 + PHP 7.4 웹 애플리케이션 |
| **MySQL 8.0** | 모든 애플리케이션 및 설문 데이터를 위한 관계형 데이터베이스 |
| **Keycloak** *(선택 사항)* | 엔터프라이즈 ID 관리를 위한 내장 싱글 사인온 서버 |

## 셀프 호스팅이 적합한 경우

다음과 같은 경우 셀프 호스팅이 적합합니다:

- **데이터 주권** 필요 — 모든 데이터가 자체 인프라 내에 유지됨
- 외부 클라우드 접근이 없는 **에어갭 또는 제한된 네트워크**에서 운영
- 온프레미스 저장소를 의무화하는 **규정 준수 요구 사항**(GDPR, HIPAA, 정부 데이터 정책)
- **내부 ID 공급자**(Active Directory, LDAP, SAML)와 통합 필요
- 자체 조건으로 CPU, RAM 및 스토리지 할당을 **리소스를 사용자 지정** 원함

## 이 섹션의 내용

| 페이지 | 설명 |
|------|-------------|
| [빠른 시작](quick-start) | 10분 이내에 서버에서 rtCloud 실행하기 |
| [구성 참조](configuration) | 모든 환경 변수 및 기본값의 전체 목록 |
| [클라우드 배포](cloud-deployment) | DigitalOcean, AWS, GCP, Linode를 위한 원클릭 자동화 스크립트 |
| [SSO 인증](sso-authentication) | Keycloak, 외부 OIDC 또는 Azure AD 구성 |
| [유지 관리](maintenance) | 인스턴스 업그레이드, 백업, 복원 및 문제 해결 |

## 아키텍처 개요

배포는 내부 네트워크에서 연결된 Docker 컨테이너 세트로 실행됩니다:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4 application                   │
│  Beanstalkd queue (internal)           │
│  Shiny Server (port 3838)              │
│  Cron scheduler                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal only)  │
└────────────────────────────────────────┘
```

SSO를 활성화하면 세 번째 컨테이너가 함께 실행됩니다:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

모든 컨테이너는 격리된 Docker 브리지 네트워크를 통해 통신합니다. 웹 애플리케이션 포트와 (선택적으로) Shiny 분석 포트만 호스트에 노출됩니다.
