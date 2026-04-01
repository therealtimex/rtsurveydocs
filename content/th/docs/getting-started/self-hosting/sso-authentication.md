---
weight: 4
title: "การยืนยันตัวตน SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "กำหนดค่า Single Sign-On สำหรับ rtCloud แบบโฮสต์ด้วยตนเองโดยใช้ Keycloak แบบฝัง ผู้ให้บริการ OIDC ภายนอก หรือ Azure Active Directory"
---

rtCloud รองรับสามแนวทางสำหรับ Single Sign-On (SSO):

| ตัวเลือก | เหมาะสำหรับ |
|--------|----------|
| [Keycloak แบบฝัง](#embedded-keycloak) | องค์กรที่ต้องการเซิร์ฟเวอร์ SSO แบบครบในตัวเองที่รวมมากับ rtCloud |
| [ผู้ให้บริการ OIDC ภายนอก](#external-oidc-provider) | องค์กรที่ใช้งานผู้ให้บริการตัวตนอยู่แล้ว (Auth0, Authentik, Okta, Supabase ฯลฯ) |
| [Azure Active Directory](#azure-active-directory) | องค์กรที่ใช้ Microsoft 365 หรือ Azure AD |

หากไม่ได้กำหนดค่า SSO ผู้ใช้จะเข้าสู่ระบบด้วยบัญชี rtCloud ภายในที่จัดการผ่านแผงผู้ดูแลระบบ

---

## Keycloak แบบฝัง

การติดตั้งใช้งานมีคอนเทนเนอร์ Keycloak เสริมที่ทำงานควบคู่กับ rtCloud Keycloak ได้รับการกำหนดค่าล่วงหน้าด้วย realm rtSurvey และพร้อมใช้งาน

### ข้อกำหนด

- ชื่อโดเมนพร้อม HTTPS (Keycloak ต้องการ HTTPS ในการผลิต)
- RAM อย่างน้อย 4 GB บนเซิร์ฟเวอร์ (Keycloak เพิ่มการใช้หน่วยความจำ ~512 MB)

### การตั้งค่า

**1. กำหนดค่าตัวแปรสภาพแวดล้อมใน `.env`:**

```dotenv
# เปิดใช้งานคอนเทนเนอร์ Keycloak แบบฝัง
EMBED_KEYCLOAK=true

# URL Keycloak — ใช้โดเมนจริงของคุณ
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# การตั้งค่า realm และ client (ตรงกับ realm JSON ที่นำเข้า)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# ข้อมูลประจำตัวผู้ดูแลระบบ Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# ฐานข้อมูล Keycloak (สร้างโดยอัตโนมัติ)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# พอร์ตที่ Keycloak รับฟัง (ฝั่งโฮสต์ proxied โดย Nginx)
KEYCLOAK_PORT=8091
```

**2. เริ่มต้นด้วยโปรไฟล์ Keycloak แบบฝัง:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. ตรวจสอบว่า Keycloak มีสุขภาพดี:**

```bash
docker compose -f docker-compose.production.yml ps
```

คอนเทนเนอร์ `rtcloud-keycloak` ควรแสดง `Up (healthy)` หลังจาก 2–3 นาที

**4. เข้าถึงคอนโซลผู้ดูแลระบบ Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

เข้าสู่ระบบด้วย `KEYCLOAK_ADMIN_USER` และ `KEYCLOAK_ADMIN_PASSWORD`

### สิ่งที่กำหนดค่าไว้ล่วงหน้า

Keycloak แบบฝังเริ่มต้นด้วย realm `rtsurvey` ที่นำเข้าล่วงหน้าซึ่งรวมถึง:

- การกำหนดค่า client สำหรับเว็บแอปพลิเคชัน
- บทบาทผู้ใช้เริ่มต้น (`admin`, `project_manager`, `enumerator`, `analyst`)
- การตั้งค่า session และ token ที่ปรับให้เหมาะสำหรับ rtSurvey

คุณสามารถเพิ่มผู้ใช้โดยตรงในคอนโซลผู้ดูแลระบบ Keycloak หรือเชื่อมต่อ Keycloak กับผู้ให้บริการตัวตน upstream (LDAP, SAML)

### การกำหนดเส้นทาง Nginx

เมื่อใช้สคริปต์การติดตั้งบนคลาวด์ Nginx ถูกกำหนดค่าให้ proxy ทั้งสองบริการ:

| Path | Backend |
|------|---------|
| `/` | แอป rtCloud บน `127.0.0.1:8080` |
| `/auth/` | Keycloak บน `127.0.0.1:8090` |

---

## ผู้ให้บริการ OIDC ภายนอก

เชื่อมต่อ rtCloud กับผู้ให้บริการตัวตนที่รองรับ OpenID Connect ใดก็ได้ แนวทางนี้ไม่ต้องการคอนเทนเนอร์ Keycloak

### ผู้ให้บริการที่รองรับ

ผู้ให้บริการ OIDC ที่สอดคล้องใดก็ได้ทำงานได้ รวมถึง:
- Authentik
- Auth0
- Okta
- Keycloak (อินสแตนซ์ภายนอก)
- Supabase
- Google (สำหรับองค์กร Google Workspace)
- GitHub (ผ่านแอป OAuth พร้อมส่วนขยาย OIDC)

### การตั้งค่า

**1. ลงทะเบียน rtCloud เป็น OIDC client ในผู้ให้บริการตัวตนของคุณ**

คุณจะต้องการ:
- **client ID** และ **client secret**
- ลงทะเบียน **redirect URI**: `https://rtcloud.example.com/auth/callback`
- สำหรับการรองรับแอปมือถือ ให้ลงทะเบียนเพิ่มด้วย: `vn.rta.rtsurvey.auth://callback`

**2. กำหนดค่าตัวแปรสภาพแวดล้อมใน `.env`:**

```dotenv
# URL การค้นพบ OIDC (เฉพาะผู้ให้บริการ — ตรวจสอบเอกสาร IdP ของคุณ)
OIDC_ISSUER_URL=https://your-identity-provider.com

# ข้อมูลประจำตัว client จากผู้ให้บริการตัวตน
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Scopes ที่จะร้องขอ (openid, profile และ email มักเพียงพอ)
OIDC_SCOPE=openid profile email

# Redirect URI ที่ลงทะเบียนในผู้ให้บริการตัวตน
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# ไม่บังคับ: client แอปมือถือแยกต่างหาก
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# ตั้งเป็น true เพื่อสร้างบัญชี rtCloud โดยอัตโนมัติสำหรับผู้ใช้ OIDC ใหม่
OPEN_REGISTRATION=false
```

**3. รีสตาร์ทคอนเทนเนอร์แอปเพื่อใช้การเปลี่ยนแปลง:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### การจัดเตรียมผู้ใช้อัตโนมัติ

เมื่อ `OPEN_REGISTRATION=true` rtCloud จะสร้างบัญชีภายในโดยอัตโนมัติเมื่อผู้ใช้เข้าสู่ระบบผ่าน OIDC เป็นครั้งแรก บัญชีจะถูกกรอกด้วยชื่อและอีเมลของผู้ใช้จาก ID token

เมื่อ `OPEN_REGISTRATION=false` (ค่าเริ่มต้น) ผู้ดูแลระบบ rtCloud ต้องสร้างบัญชีผู้ใช้ก่อน และตัวตน OIDC จะถูกเชื่อมโยงเมื่อเข้าสู่ระบบครั้งแรก

### Endpoints ที่กำหนดเอง

หากผู้ให้บริการของคุณไม่รองรับการค้นพบ OIDC (`.well-known/openid-configuration`) คุณสามารถตั้ง endpoints ด้วยตนเอง:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

ผสานรวม rtCloud กับ Microsoft Azure AD tenant ขององค์กร

### การตั้งค่า

**1. ลงทะเบียนแอปใหม่ใน [Azure Portal](https://portal.azure.com):**

   - ไปที่ **Azure Active Directory** → **App registrations** → **New registration**
   - Name: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (ประเภท Web)
   - หลังจากสร้าง ให้จดบันทึก **Application (client) ID** และ **Directory (tenant) ID**
   - ใต้ **Certificates & secrets** ให้สร้าง client secret ใหม่

**2. กำหนดค่าตัวแปรสภาพแวดล้อมใน `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. รีสตาร์ทคอนเทนเนอร์แอป:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

ผู้ใช้ใน Azure AD tenant ของคุณสามารถเข้าสู่ระบบ rtCloud โดยใช้ข้อมูลประจำตัว Microsoft ได้แล้ว

---

## การปิดใช้งาน SSO

เพื่อกลับไปใช้การยืนยันตัวตนภายในเครื่อง ให้ลบหรือคอมเมนต์ตัวแปรที่เกี่ยวข้องกับ SSO ทั้งหมดจาก `.env` แล้วรีสตาร์ทคอนเทนเนอร์แอป:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

หากคุณใช้ Keycloak แบบฝัง ให้หยุดโดยละเว้นแฟล็ก `--profile embed-keycloak` และรัน `docker compose down` ตามด้วย `up -d` โดยไม่มีโปรไฟล์
