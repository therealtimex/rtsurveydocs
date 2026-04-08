---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurvey의 `appearance` 열은 설문의 질문에 대한 시각적 표현과 동작을 사용자 정의할 수 있습니다. 이 기능은 사용자 경험을 향상시키고 데이터 수집 효율을 크게 향상시킬 수 있습니다. rtSurvey는 표준 XLSForm appearance 속성을 지원하고 추가 옵션으로 확장합니다.

## 표준 XLSForm Appearance 속성

rtSurvey는 다음 표준 XLSForm appearance 속성을 지원합니다:

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| multiline | text | 여러 줄 텍스트 상자 생성 (웹 클라이언트에 최적) |
| minimal | select_one, select_multiple | 선택지를 드롭다운 메뉴로 표시 |
| quick | select_one | 선택 후 다음 질문으로 자동 이동 (모바일 전용) |
| no-calendar | date | 달력 표시 억제 (모바일 전용) |
| month-year | date | 월 및 연도만 선택 허용 |
| year | date | 연도만 선택 허용 |
| horizontal-compact | select_one, select_multiple | 선택지를 수평으로 표시 (웹 전용) |
| horizontal | select_one, select_multiple | 선택지를 열 형태로 수평 표시 (웹 전용) |
| likert | select_one | 선택지를 Likert 척도로 표시 |
| compact | select_one, select_multiple | 최소 패딩으로 선택지를 나란히 표시 |
| quickcompact | select_one | 컴팩트 표시와 자동 이동 결합 (모바일 전용) |
| field-list | groups | 한 화면에 전체 그룹 표시 (모바일 전용) |
| label | select_one, select_multiple | 입력 없이 선택지 레이블만 표시 |
| list-nolabel | select_one, select_multiple | 레이블 없이 입력만 표시 (`label`과 함께 사용) |
| table-list | groups | 표 형식으로 질문 표시 |
| signature | image | 서명 캡처 활성화 (모바일 전용) |
| draw | image | 자유형 그리기 허용 (모바일 전용) |
| map, quick map | select_one, select_one_from_file | 지도 기능에서 선택 활성화 |

## Appearance 사용 모범 사례

1. **일관성**: 통일된 모양을 위해 설문 전체에 걸쳐 appearance 속성을 일관되게 사용합니다.
2. **모바일 대 웹**: 다양한 기기와 플랫폼에서 appearance가 어떻게 렌더링될지 고려합니다.
3. **성능**: 양식 로딩 속도를 늦출 수 있는 appearance 속성에 주의합니다 (예: 대형 그룹의 `table-list`).
4. **사용자 경험**: 응답자에게 데이터 입력을 더 쉽고 직관적으로 만드는 appearance를 선택합니다.
5. **테스트**: 항상 대상 기기에서 양식을 테스트하여 appearance가 예상대로 작동하는지 확인합니다.

## 고급 기술

### Appearance 결합

일부 appearance 속성은 더 복잡한 레이아웃을 위해 결합할 수 있습니다:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | 하나를 선택하세요: | minimal compact |
```

### 동적 Appearance

rtSurvey는 양식 논리에 따라 동적 appearance 변경을 허용합니다:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | 시간 입력: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## 모바일 앱 고려 사항

- 일부 appearance (예: `quick`, `signature`)는 모바일 기기에만 해당됩니다.
- 일관된 동작을 보장하기 위해 Android와 iOS 모두에서 철저히 테스트합니다.

## rtSurvey 확장 Appearance 속성

표준 XLSForm appearance 외에 rtSurvey는 다음 플랫폼별 옵션을 지원합니다:

### 데이터 및 표시 제어

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `invisible` | any | 값을 수집하거나 계산하면서 필드를 보이지 않게 합니다. `hidden` 유형과 다릅니다 — 필드는 여전히 논리에 참여합니다. |
| `displaytitle` | any | 그렇지 않으면 억제될 경우에도 필드의 레이블/제목 표시를 강제합니다. |
| `autopull` | select_one, select_multiple | 양식이 로드되거나 트리거 필드가 변경될 때 선택지를 채우기 위해 자동으로 외부 데이터를 가져옵니다. |
| `floating_hint` | text, integer, decimal | 힌트 텍스트를 입력 필드 아래가 아닌 위에 떠있는 레이블로 표시합니다. |
| `calculate-button` | calculate | 자동으로 계산하는 대신 필드의 재계산을 온디맨드로 트리거하는 버튼을 추가합니다. |

### 레이아웃

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `1screen` | group | 그룹 크기에 관계없이 전체 그룹을 단일 화면에 강제로 표시합니다. |
| `columns(n)` | select_one, select_multiple | `n` 열로 선택지를 표시합니다. 예시: `columns(3)`은 세 열의 라디오 버튼을 표시합니다. |
| `gridformat<row=R col=C colspan=S align=center>` | any | 행 `R`, 열 `C`, `S` 열에 걸쳐 CSS 그리드 레이아웃에서 필드를 배치합니다. `advanced-extension/grid-layout`에서 사용됩니다. |
| `ignore-simplify` | any | 양식 렌더러가 이 필드의 레이아웃 자동 단순화 또는 압축을 건너뛰도록 지시합니다. |
| `required-but-simplify` | any | 필드는 필수이지만 레이아웃은 여전히 단순화됨 |
| `embed` | any | 필드를 내장/인라인 표시 모드로 렌더링 |
| `popup` | select_one, select_multiple | 선택지 목록을 팝업/모달 오버레이로 렌더링 |
| `auto-hide-empty` | boxtag, select | 선택지 목록이 비어 있을 때 위젯 숨기기 |
| `text-nolabel` | select_one, select_multiple | 각 선택지의 텍스트 레이블 숨기기 |

### 위젯

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `likert` | select_one | 선택지를 Likert 척도 행으로 표시합니다 (이미 표준 표에 있음; 지원 확인됨). |
| `distress` | select_one | 선택지를 감정 아이콘이 있는 Kessler 심리적 고통 척도 (K10) 시각적 위젯으로 렌더링합니다. |

### 선택 시각적 위젯

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | 선택지를 클릭 가능한 태그 칩으로 표시 |
| `boxtag` | select_one, select_multiple | 선택지를 스타일화된 직사각형 박스로 표시 |
| `boxtag -search` | select_one, select_multiple | 박스 위에 검색/필터 입력이 있는 Boxtag 레이아웃 |
| `duolingo-style1` | select_one, select_multiple | 대형 카드 레이아웃 — 짧은 선택지 목록에 최적 |
| `rating_box` | select_one, select_multiple | 그리드 기반 평점 박스 |
| `star_rating` | select_one | 별점 위젯 — 선택지가 1–N 개의 별로 렌더링됨 |
| `choices-noshow` | select_one, select_multiple | 처음에 처음 10개의 선택지만 표시; 나머지는 요청 시 |
| `noshow` | select_one, select_multiple | 선택지 목록을 완전히 숨김; 값은 프로그래밍 방식으로 설정 |
| `checkall` | select_multiple | 목록 상단에 "모두 선택" 옵션 추가 |
| `max-items(N)` | select_one, select_multiple | 보이는 선택지 수를 N으로 제한 |

### 텍스트 시각적 위젯

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `richtext` | text | 서식 있는 텍스트 편집기 — 굵게, 기울임, 목록 및 링크가 있는 도구 모음 |
| `typingtest` | text | 타이핑 테스트 인터페이스 — 텍스트를 제시하고 타이핑 속도와 정확도를 측정 |

### 미디어 확장

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | 캡처된 사진에 텍스트 워터마크를 오버레이; 표현식은 캡처 시 평가됨 |
| `editable` | image | 응답자가 사진 촬영 후 이미지에 주석을 달고 그림을 그릴 수 있게 함 |

### 인라인 표시 구성

`display{}` 매개변수는 인라인 표시 동작을 구성합니다:

| 매개변수 | 설명 |
|---------|------|
| `display{title="레이블"}` | 인라인 표시를 위한 사용자 지정 제목 설정 |
| `display{icon="icon_name"}` | 인라인 표시를 위한 아이콘 설정 |
| `display{color="RRGGBB"}` | 인라인 표시를 위한 사용자 지정 색상 설정 |

`results{}` 매개변수는 결과 표시를 구성합니다:

| 매개변수 | 설명 |
|---------|------|
| `results{format="pattern"}` | 결과 표시를 위한 형식 패턴 설정 |
| `results{show=true}` | 결과를 인라인으로 표시 |

### API 통합

| Appearance 속성 | 질문 유형 | 설명 |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | 이 필드에 대한 API 호출 통합을 활성화합니다. calculation 열에는 `callapi()` 표현식이 포함되어야 합니다. [API 호출](advanced-extension/call-api)을 참조하세요. |
| `callapi-verify(params)` | text, integer, decimal | 정적 매개변수를 사용하여 API 검증 호출을 트리거합니다. API가 값을 확인할 때까지 양식이 진행을 차단합니다. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | `callapi-verify`와 동일하지만 런타임에 다른 필드 값에서 파생된 매개변수를 사용합니다. |

### 인라인 날짜/시간 형식

`date`, `time` 및 `datetime` 필드의 경우 appearance에 형식 문자열을 추가하여 사용자 정의 표시 형식을 지정할 수 있습니다:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

형식 토큰은 `format-date()` 및 `format-date-time()`과 동일합니다. [함수 — 날짜 및 시간 함수](operators-and-functions/functions#date-and-time-functions)를 참조하세요.

예시:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | 이벤트 날짜 및 시간 | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | 생년월일 | inline-[%d/%m/%Y] |

## 알려진 제한 사항

- 복잡한 appearance는 모든 플랫폼에서 동일하게 렌더링되지 않을 수 있습니다.
- 일부 고급 rtSurvey appearance는 오프라인 모드에서 지원되지 않을 수 있습니다.

## Appearance 문제 해결

1. **Appearance가 적용되지 않음**: appearance 열에 오타가 없는지 확인합니다.
2. **일관되지 않은 렌더링**: 질문 유형 및 플랫폼과의 호환성을 확인합니다.
3. **성능 문제**: 복잡한 appearance를 단순화하는 것을 고려합니다, 특히 대형 설문의 경우.
