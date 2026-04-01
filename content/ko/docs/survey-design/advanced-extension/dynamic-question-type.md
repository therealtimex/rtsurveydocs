---
title: "동적 질문 유형"
description: "동적 질문 유형은 API 응답 또는 계산된 값에 따라 런타임에 필드의 질문 유형과 위젯이 결정될 수 있도록 합니다."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

**동적 질문 유형** 기능은 양식 설계 시점이 아닌 **런타임**에 필드의 입력 위젯과 유효성 검사 동작이 결정될 수 있도록 합니다. 이는 수집할 데이터 유형이 서버 측 구성, API 응답 또는 이전 필드 값에 따라 달라지는 경우에 사용되는 고급 rtSurvey 확장입니다.

일반적인 사용 사례는 서버가 어떤 필드가 필요한지, 유형(text, integer, select 등)이 무엇인지, 사용 가능한 옵션이 무엇인지를 정의하는 구성 가능한 검사 체크리스트입니다 — 모든 구성에 대해 양식을 다시 구축하지 않고도 가능합니다.

---

## 작동 방식

동적 질문 유형으로 표시된 필드는 `callapi()`를 사용하여 API에서 구성을 가져옵니다. API 응답은 다음을 정의합니다:

- 렌더링할 입력 유형 (text, integer, select_one 등)
- 사용 가능한 선택지 (선택 유형의 경우)
- 유효성 검사 규칙

필드는 내부적으로 `specialFeature: isDynamicQuestionType`으로 표시되어, 정적 양식 정의 대신 API 응답을 사용하여 위젯을 구성하도록 양식 엔진에 알립니다.

---

## 설정

### 1단계: 필드 구성 가져오기

`callapi()`와 함께 `calculate` 필드를 사용하여 동적 구성을 검색합니다:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### 2단계: 동적 필드에서 구성 참조

동적 필드는 appearance 또는 constraint에서 `callapi-verify()`를 사용하여 가져온 구성에 연결합니다:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | 검사 결과 | `callapi-verify(dynamicParams)` |

양식 엔진은 `field_config`를 읽고 `inspection_result`를 `text`, `integer`, 또는 `select_one` 필드로 렌더링할지를 동적으로 결정합니다.

---

## API 응답 형식

API는 필드 구성을 설명하는 JSON 객체를 반환해야 합니다. 일반적인 응답:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "합격"},
      {"value": "fail", "label": "불합격"},
      {"value": "na", "label": "해당 없음"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## 예시: 구성 가능한 검사 양식

검사 유형에 따라 서버에서 항목 목록과 답변 유형을 가져오는 검사 양식:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | 검사 유형 | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | 항목 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | 항목 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | 항목 3 | `callapi-verify(dynamicParams)` | |

서버는 `insp_type`에 따라 각 항목에 대한 올바른 위젯 유형, 레이블, 선택지 및 유효성 검사를 반환합니다.

---

## 모범 사례

1. 필드 구조가 런타임에 실제로 달라지는 경우에만 동적 질문 유형을 사용합니다 — 정적 양식의 경우 표준 질문 유형을 사용합니다.
2. 구성 API가 빠르게 응답하는지(2초 미만) 확인하고 현장 네트워크에서 사용 가능한지 확인합니다.
3. API에 연결할 수 없는 경우를 위해 양식에 합리적인 폴백을 항상 정의합니다 — 메모가 있는 일반 `text` 필드가 깨진 위젯보다 낫습니다.
4. API 응답 스키마를 버전 관리합니다 — 응답 형식 변경은 해당 엔드포인트를 사용하는 모든 활성 양식에 영향을 미칩니다.
5. 배포 전에 API가 반환할 수 있는 모든 필드 유형 조합을 테스트합니다.

## 제한 사항

- 동적 질문 유형은 구성을 가져오기 위해 네트워크 연결이 필요합니다.
- 동적으로 사용 가능한 위젯 유형의 전체 범위는 rtSurvey 클라이언트 버전에 따라 다릅니다 — 대상 버전에서 테스트합니다.
- 이는 표준 XLSForm 사양에 해당하는 기능이 없는 고급 rtSurvey 확장입니다.
- 필드 정의가 양식과 API 응답에 분산되어 있어 디버그 오류를 추적하기가 더 어렵습니다.
