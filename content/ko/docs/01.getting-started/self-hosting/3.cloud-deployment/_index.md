---
weight: 3
title: "클라우드 배포"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "DigitalOcean, AWS EC2, Google Cloud, Linode를 위한 자동화 스크립트로 주요 클라우드 공급자에 rtCloud를 배포합니다."
---

배포 리포지토리에는 주요 클라우드 공급자를 위한 자동화된 프로비저닝 스크립트가 포함되어 있습니다. 각 스크립트는 새로운 **Ubuntu 22.04 LTS** 서버의 첫 번째 부팅 시 실행되어 완전 무인 설정을 수행합니다:

- Docker 및 Docker Compose 설치
- 모든 내부 서비스에 대한 안전한 무작위 비밀번호 생성
- `docker-compose.production.yml` 및 `.env` 작성
- Nginx를 역방향 프록시로 구성
- Let's Encrypt에서 무료 TLS 인증서 획득 (DNS가 확인될 때까지 자동 재시도)
- UFW 방화벽 구성
- 선택적으로 내장 Keycloak SSO 서버 배포
- 모든 자격 증명이 포함된 전체 배포 요약 출력

표준 인스턴스에서 설정은 **5~10분** 내에 완료됩니다.

---

## 스크립트 선택

클라우드 공급자 및 SSO 설정에 따라 여러 스크립트 변형이 있습니다:

| 스크립트 | 공급자 | SSO 모드 | 최적 사용 사례 |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | 내장 Keycloak | 단순하고 자립형 SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak 또는 외부 OIDC | 완전한 제어 |
| `linode-stackscript-keycloak-embed.sh` | Linode | 내장 Keycloak | 양식 기반 설정, 가장 단순 |
| `linode-stackscript-oidc.sh` | Linode | 외부 OIDC만 | 기존 ID 공급자 |
| `linode-stackscript.sh` | Linode | Keycloak 또는 외부 OIDC | 완전한 제어 |
| `aws-ec2.sh` | AWS EC2 | Keycloak 또는 외부 OIDC | AWS 배포 |
| `gcp-compute.sh` | Google Cloud | Keycloak 또는 외부 OIDC | GCP 배포 |

> **대부분의 사용자에게 권장:** `keycloak-embed` 변형을 사용하세요. 내장 Keycloak ID 서버가 포함되어 있어 가장 적은 구성 필드가 필요합니다.

---

## 서버 크기 가이드

| 사용 사례 | RAM | 디스크 | 예시 |
|----------|-----|------|---------|
| 평가 / 개발 | 2 GB | 25 GB | DO Basic $18/월, t3.small, e2-small |
| 소규모 팀 (< 50명) | 4 GB | 40 GB | DO Basic $24/월, t3.medium, e2-medium |
| 프로덕션 (> 50명) | 8 GB | 80 GB | DO General $48/월, t3.large, n2-standard-2 |

> 내장 Keycloak에는 최소 **4 GB RAM**이 필요합니다. Keycloak 없이 평가용으로만 2 GB를 사용하세요.

---

## DNS 설정

모든 스크립트는 Let's Encrypt가 인증서를 발급하기 전에 **서버 IP를 가리키는 A 레코드**가 있는 도메인이 필요합니다.

스크립트는 설정 프로세스 초반에 서버 IP를 출력합니다:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

스크립트는 최대 1시간 동안 60초마다 Let's Encrypt를 **자동으로 재시도**합니다. DNS 레코드를 추가하고 기다리기만 하면 됩니다 — 재시작 필요 없습니다.

> **속도 제한:** Let's Encrypt는 도메인당 7일당 최대 **5개의 인증서**를 허용합니다. 동일한 도메인으로 서버를 반복적으로 배포하고 삭제하는 것을 피하세요. 제한에 도달하면 스크립트에 `retry after` 타임스탬프가 표시되고 즉시 중지됩니다.

---

## 배포 후 체크리스트

- [ ] 앱이 `https://your-domain.com`에서 열림
- [ ] `admin` 및 구성한 비밀번호로 로그인
- [ ] 모든 컨테이너가 정상: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt 갱신 작동: `certbot renew --dry-run`
- [ ] MySQL 포트 3306이 **노출되지 않음**: `ufw status`
- [ ] 일일 데이터베이스 백업 설정 ([유지 관리](../maintenance) 참조)

---

## 문제 해결

### 전체 설정 로그 확인

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt 속도 제한

로그에 `too many certificates`가 표시되면 5개 인증서/7일 제한에 도달한 것입니다. 로그에 정확한 재시도 시간이 표시됩니다:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

해당 시간까지 기다린 후 재배포하세요.

### Keycloak이 비정상 상태 유지

서버에 최소 4 GB RAM이 있는지 확인한 후 로그를 확인하세요:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### certbot 후 SSL 구성이 적용되지 않음

인증서는 발급되었지만 Nginx가 여전히 HTTP만 표시하는 경우 로그에서 오류 행을 확인하고 수동으로 Nginx를 다시 로드하세요:

```bash
nginx -t && systemctl reload nginx
```
