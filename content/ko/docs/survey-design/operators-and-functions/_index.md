---
title: "연산자 및 함수"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

rtSurvey의 표현식은 JavaRosa/ODK 함수와 사용자 정의 rtSurvey 함수로 확장된 **XPath 1.0**의 하위 집합으로 작성됩니다. XLSForm의 `calculate`, `constraint`, `relevant`, `required`, `default` 열에서 표현식을 사용합니다.

## 필드 값 참조

다른 필드의 값을 참조하려면 `${fieldname}`을 사용합니다:

```
${age} > 18
```

**현재 필드의 값**을 참조하려면 `.` (점 하나)를 사용합니다 — `constraint` 표현식에서 흔히 사용됩니다:

```
. >= 0 and . <= 100
```

상위 그룹을 참조하려면 `..`를 사용합니다 (반복에서의 고급 사용).

## 표현식 구문

표현식은 표준 XPath 규칙을 따릅니다:

- **문자열**은 단따옴표로 묶어야 합니다: `'yes'`
- **숫자**는 있는 그대로 작성합니다: `42`, `3.14`
- **Boolean** 결과는 `relevant`, `required`, `constraint`에 사용됩니다 — 비어있지 않고 0이 아닌 값은 참입니다
- 연산자 주위의 공백은 무시됩니다

{{% alert icon=" " context="warning" %}}
항상 직선 따옴표 (`'` 또는 `"`)를 사용하세요 — 절대 "스마트 따옴표" (곡선 따옴표)를 사용하지 마세요. 리치 텍스트 편집기는 종종 따옴표를 자동으로 변환하여 표현식을 깨트립니다.
{{% /alert %}}

## 이 챕터의 섹션

- **[연산자](operators)** — 비교 연산자 (`=`, `!=`, `>`, `<`, `>=`, `<=`) 및 논리 연산자 (`and`, `or`, `not()`)
- **[함수](functions)** — 문자열, 선택, 숫자, 날짜/시간, boolean, 지리, 유틸리티 함수
- **[참조](references)** — 필드 및 컨텍스트 값을 참조하는 방법

## 빠른 예시

| 사용 사례 | 표현식 |
|----------|------------|
| 나이가 18세 이상인 경우 표시 | `${age} > 18` |
| "yes"가 선택된 경우에만 표시 | `${consent} = 'yes'` |
| 다른 필드가 비어있지 않은 경우 필수 | `${name} != ''` |
| 합계 계산 | `${adults} + ${children}` |
| 이름 연결 | `concat(${first_name}, ' ', ${last_name})` |
| 오늘 날짜 | `today()` |
| 옵션 선택 여부 확인 | `selected(${interests}, 'sports')` |
