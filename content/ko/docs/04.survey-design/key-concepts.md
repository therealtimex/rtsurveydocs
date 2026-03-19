---
title: "핵심 개념"
description: "양식 설계 개요"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## XLSForm이란?
rtSurvey는 정교한 설문을 만들기 위한 강력한 기능을 제공하는 [XLSForm](https://xlsform.org/) 표준의 확장 버전을 사용합니다. 이 가이드에서는 기본 XLSForm 구조부터 rtSurvey 특유의 고급 기능까지 rtSurvey에서 양식을 설계하는 핵심 개념을 소개합니다.

XLSForm을 사용하면 익숙한 Excel 도구를 이용하여 사람이 읽을 수 있는 형식으로 양식을 작성할 수 있어 누구나 쉽게 접근할 수 있습니다. 이 표준은 양식 제작 시 쉬운 공유와 협업을 가능하게 합니다.

XLSForm은 초보자에게도 친화적이지만, 숙련된 사용자가 복잡한 양식을 만드는 것도 허용합니다.

rtSurvey는 다양한 웹 및 모바일 데이터 수집 플랫폼에서 양식에 고급 기능(예: 건너뛰기 논리)을 일관되게 통합하는 방법을 제공합니다.

## XLSForm 구조
XLSForm은 일반적으로 두 개의 주요 워크시트로 구성됩니다:

1. **survey**: 양식의 구조와 내용을 정의합니다.
2. **choices**: 다중 선택 질문의 답변 선택지를 지정합니다.

선택적인 **settings** 워크시트로 추가 양식 사양을 제공할 수 있습니다.

survey와 choices 워크시트의 필수 열은 양식이 올바르게 작동하기 위해 반드시 있어야 합니다. 두 워크시트의 선택적 열은 각 항목의 동작을 추가로 제어하지만 필수는 아닙니다.

Excel 통합 문서의 열은 어떤 순서로도 나타날 수 있으며, 선택적 열은 비워둘 수 있습니다. 그러나 양식이 올바르게 작동하려면 XLSForm 문서에 지정된 정확한 구문과 명명 규칙을 사용하는 것이 중요합니다.

### survey 워크시트
**survey 워크시트**는 양식의 구조를 정의하고 내용을 제공하는 곳입니다. survey 워크시트의 각 행은 양식의 질문이나 요소를 나타냅니다. survey 워크시트에는 다음 열이 필수입니다:

- `type`: 질문에 대해 기대하는 입력 유형을 지정합니다.
- `name`: 해당 항목의 고유 변수 이름을 지정합니다. 이름은 문자나 밑줄로 시작해야 하며 문자, 숫자, 하이픈, 밑줄, 마침표만 포함할 수 있습니다. 이름은 대소문자를 구분합니다.
- `label`: 양식에서 질문에 대해 표시되는 실제 텍스트를 포함합니다.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | 응답자 성별?         |
| integer             | age      | 응답자 나이?         |

### choices 워크시트
**`choices`** 워크시트는 다중 선택 질문의 답변 선택지를 지정하는 데 사용됩니다. 각 행은 하나의 답변 선택지를 나타냅니다. choices 워크시트에는 다음 열이 필수입니다:

- **`list_name`**: 관련 답변 선택지 집합을 그룹화합니다.
- **`name`**: 해당 답변 선택지의 고유 변수 이름을 지정합니다.
- **`label`**: 양식에 표시할 답변 선택지를 정확하게 보여줍니다.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | 트랜스젠더           |
| gender              | female      | 여성                 |
| gender              | male        | 남성                 |
| gender              | other       | 기타                 |

Excel 통합 문서에 추가하는 열은 필수이든 선택이든 어떤 순서로도 나타날 수 있습니다. 선택적 열은 완전히 생략할 수 있습니다. 가독성을 높이기 위해 행이나 열을 비워둘 수 있지만, 한 시트에서 20개의 연속된 빈 열이나 행 이후의 데이터는 처리되지 않습니다. 모든 .xlsx 파일 서식은 무시되므로 양식을 더 읽기 쉽게 만들기 위해 구분선, 음영, 기타 글꼴 서식을 사용할 수 있습니다.

Excel에서 양식을 작성할 때 한 가지 유의할 점은 사용하는 구문이 정확해야 한다는 것입니다. 예를 들어 **choices** 대신 **Choices** 또는 **choice**라고 입력하면 양식이 작동하지 않습니다.

### settings 워크시트

settings 워크시트는 선택 사항이지만 양식 수준의 메타데이터와 동작을 지정할 수 있습니다. settings 워크시트의 일반적인 열은 다음과 같습니다:

| 열 | 설명 |
|--------|-------------|
| form_title | 사용자에게 표시되는 양식의 제목 |
| form_id | 데이터 관리 및 API 호출에 사용되는 양식의 고유 식별자 |
| default_language | 다국어 양식의 기본 언어 코드 (예: 영어의 경우 'en') |
| version | 변경 사항 추적에 유용한 양식의 버전 번호 |
| instance_name | 각 양식 제출에 대한 고유 이름을 생성하는 표현식 |
| generation | 양식의 세대를 표시하는 정수. 구조 변경 시 증가 |
| family | 구조 변경에 걸쳐 관련 양식을 그룹화하는 식별자 |

rtSurvey의 settings 워크시트에는 rtSurvey의 확장 기능에 특화된 추가 구성도 포함될 수 있습니다. 지원되는 설정의 전체 목록은 rtSurvey 문서를 참조하세요.

## Survey 워크시트의 핵심 구성 요소

survey 워크시트는 양식 설계의 핵심입니다. 주요 구성 요소 개요는 다음과 같습니다:

| 구성 요소 | 설명 |
|-----------|-------------|
| [type](#question-types) | 질문 유형 지정 (예: text, integer, select_one) |
| [name](#naming-conventions) | 질문의 고유 식별자 |
| [label](#labels-and-translations) | 응답자에게 표시되는 텍스트 |
| [hint](#hints-and-help-text) | 응답자를 위한 추가 안내 |
| [appearance](#appearance-options) | 질문 표시 방식 수정 |
| [relevant](#relevance-and-skip-logic) | 질문을 표시할 시점 결정 (건너뛰기 논리) |
| [constraint](#constraints-and-validation) | 응답 유효성 검사 |
| [calculation](#calculations) | 다른 응답을 기반으로 값 계산 |
| [required](#required-fields) | 질문 필수 여부 지정 |

이러한 각 구성 요소는 효과적이고 효율적인 설문을 만드는 데 중요한 역할을 합니다.

### 질문 유형
XLSForm은 다양한 질문 유형을 지원합니다. 다음은 XLSForm의 **`survey`** 워크시트의 **`type`** 열에 입력할 수 있는 몇 가지 옵션입니다:

| 질문 유형                 | 답변 입력                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| integer                   | 정수 (즉, 소수점 없는 숫자) 입력.                                                          |
| decimal                   | 소수 입력.                                                                               |
| range                     | [범위](#range) 입력 (평점 포함)                                                     |
| text                      | 자유 텍스트 응답.                                                                          |
| select_one [options]      | [다중 선택](#multiple-choice) 질문; 하나의 답변만 선택 가능.               |
| select_multiple [options] | [다중 선택](#multiple-choice) 질문; 여러 답변 선택 가능.              |
| select_one_from_file [file]| [파일에서 다중 선택](#multiple-choice-from-file); 하나의 답변만 선택 가능.      |
| select_multiple_from_file [file]| [파일에서 다중 선택](#multiple-choice-from-file); 여러 답변 선택 가능.|
| rank [options]            | [순위](#rank) 질문; 목록 순서 지정.                                                        |
| note                      | 화면에 메모를 표시하며, 입력을 받지 않습니다. readonly=true인 type=text의 약어입니다.    |
| geopoint                  | [단일 GPS 좌표](#gps) 수집.                                                     |
| geotrace                  | [두 개 이상의 GPS 좌표로 구성된 선](#gps) 기록.                                                |
| geoshape                  | [여러 GPS 좌표로 구성된 다각형](#gps) 기록; 마지막 점은 첫 번째 점과 동일합니다. |
| date                      | 날짜 입력.                                                                                  |
| time                      | 시간 입력.                                                                                  |
| dateTime                  | 날짜와 시간 입력을 모두 받습니다.                                                             |
| image                     | 사진 촬영 또는 [이미지 파일](#image) 업로드.                                            |
| audio                     | 오디오 녹음 또는 오디오 파일 업로드.                                                         |
| background-audio          | 양식 작성 중 배경에서 오디오가 녹음됩니다.                                                  |
| video                     | 비디오 녹화 또는 비디오 파일 업로드.                                                         |
| file                      | 일반 파일 입력 (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                   | 바코드 스캔, 바코드 스캐너 앱이 설치되어 있어야 합니다.                            |
| calculate                 | 계산 수행; 아래의 [계산](#calculation) 섹션을 참조하세요.                    |
| acknowledge               | "OK"가 선택되면 값을 "OK"로 설정하는 확인 프롬프트.                                      |
| hidden                    | UI 요소 없이 상수를 저장하는 데 사용할 수 있는 필드                  |
| xml-external              | [외부 XML 데이터](#external-xml-data) 파일에 대한 참조 추가                         |

### 레이블

레이블은 각 질문에 대해 응답자에게 표시되는 텍스트입니다. 설문에서 명확한 의사소통을 위해 매우 중요합니다.

- **기본 사용법**: `label` 열에 질문 텍스트를 입력합니다.
- **다국어**: 다국어 설문을 위해 `label::English` 및 `label::French`와 같은 추가 열을 사용합니다.
- **서식**: rtSurvey는 강조나 구조를 위해 레이블에서 기본 HTML 서식을 지원합니다.

예시:
```
| type | name | label | label::French |
|------|------|-------|---------------|
| text | name | 이름이 무엇입니까? | Quel est votre nom? |
```

### 힌트

힌트는 주요 질문 텍스트를 복잡하게 만들지 않으면서 응답자에게 추가 안내를 제공합니다.

- **사용법**: `hint` 열에 힌트를 추가합니다.
- **가시성**: 힌트는 일반적으로 주요 질문 텍스트 아래에 표시됩니다.
- **다국어**: 레이블처럼 힌트도 `hint::Language` 열을 사용하여 여러 언어로 지정할 수 있습니다.

예시:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | 나이가 몇 살입니까? | 연 단위로 나이를 입력해 주세요 |
```

### Appearance

rtSurvey의 `appearance` 열은 질문이 표시되는 방식을 사용자 정의할 수 있습니다.

- **표준 옵션**: 텍스트의 경우 'multiline', 선택 질문의 경우 'horizontal' 등이 포함됩니다.
- **rtSurvey 확장**: 
  - 시간 입력: 다양한 시계 표시 옵션 (예: `inline`, `inline-1line`)
  - 색상 사용자 정의: `colors()` 함수를 사용하여 아이콘 색상 변경

예시:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | 시간 입력 | inline-[%H:%M] |
```

### Relevant

`relevant` 열은 건너뛰기 논리를 구현하여 질문이 표시되어야 할 시점을 결정합니다.

- **구문**: XPath 표현식을 사용하여 조건을 정의합니다.
- **변수**: `${question_name}`을 사용하여 다른 질문 이름을 참조합니다.

예시:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | 알레르기 목록 | ${has_allergies} = 'yes' |
```

### Required

`required` 열은 질문에 반드시 답해야 하는지를 지정합니다.

- **기본 사용법**: 질문을 필수로 만들려면 'yes' 또는 'true'를 사용합니다.
- **고급**: 조건부 필수를 위한 표현식을 사용할 수 있습니다.

예시:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | 이메일 주소 | yes |
```

### 반복

반복은 질문 그룹이 여러 번 답변될 수 있도록 합니다.

- **사용법**: `begin repeat` 및 `end repeat` 행을 사용하여 반복 그룹을 정의합니다.
- **명명**: 각 반복 그룹에 고유한 이름을 부여합니다.

예시:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | 가구원 |
| text | member_name | 이름 |
| integer | member_age | 나이 |
| end repeat | | |
```

### 미디어

rtSurvey는 이미지, 오디오, 비디오 등 다양한 미디어 유형을 지원합니다.

- **질문 유형**: type 열에 'image', 'audio', 또는 'video'를 사용합니다.
- **레이블의 미디어**: HTML 태그를 사용하여 레이블에서 미디어 파일을 참조합니다.

예시:
```
| type | name | label |
|------|------|-------|
| image | house_photo | 집 사진 찍기 |
| note | | <img src="logo.jpg" /> 설문에 오신 것을 환영합니다 |
```

### 읽기 전용

읽기 전용 질문은 사용자 입력 없이 정보를 표시합니다.

- **사용법**: `appearance` 열에 'readonly'를 추가합니다.
- **계산**: 계산된 값을 표시하기 위해 calculate 유형과 함께 자주 사용됩니다.

예시:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | BMI | readonly | ${weight} / (${height} * ${height}) |
```

## rtSurvey 확장

rtSurvey는 `그리드 레이아웃`, `HTML 서식`, 다양한 새로운 `위젯` 등 추가 기능을 지원하여 XLSForm 표준을 확장합니다.

### 그리드 레이아웃
rtSurvey를 사용하면 여러 질문을 한 행에 압축하여 전통적인 종이 설문과 유사한 모양의 양식을 만들 수 있습니다.

### 양식 설정

### 데이터 설정

### Typeform 스타일

### pulldata() 확장

### Appearance 기반 확장

### Webbox 확장
