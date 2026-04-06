---
title: "질문 건너뛰기"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

건너뛰기 로직 (분기 또는 조건부 로직이라고도 함)은 응답자의 답변에 적응하는 동적 설문을 만들 수 있게 합니다. rtSurvey에서는 XLSForm의 `relevant` 열을 사용하여 건너뛰기 로직을 구현합니다.

## 기본 건너뛰기 로직

기본 건너뛰기 로직을 구현하려면 `relevant` 열을 사용하여 조건을 지정합니다:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | 피자를 좋아하십니까?          |                    |
| select_multiple pizza_toppings | favorite_topping | 좋아하는 토핑 | ${likes_pizza} = 'yes' |
```

이 예시에서 "좋아하는 토핑" 질문은 응답자가 피자를 좋아한다고 답했을 때만 표시됩니다.

## Relevant 표현식 구문

- 다른 질문 변수를 참조하려면 `${ }`를 사용합니다.
- `select_one` 질문의 경우 직접 비교합니다: `${question_name} = 'answer'`
- `select_multiple` 질문의 경우 `selected()` 함수를 사용합니다.

## 고급 건너뛰기 로직

### 다중 조건

`and`, `or`, 괄호를 사용하여 여러 조건을 결합할 수 있습니다:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | 나이가 어떻게 되십니까?       |                                           |
| text    | school| 어떤 학교에 다닙니까? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### select_multiple 질문 사용

`select_multiple` 질문의 경우 `selected()` 함수를 사용합니다:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | 좋아하는 토핑 |                                         |
| text           | cheese_type   | 좋아하는 치즈 종류     | selected(${favorite_topping}, 'cheese') |
```

### 객관식에서 "기타" 옵션

`relevant`을 사용하여 자유 텍스트 "기타" 옵션을 구현합니다:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | 좋아하는 피자 토핑은 무엇입니까? |                                       |
| text           | favorite_toppings_other | 다른 토핑이 있다면 무엇입니까?   | selected(${favorite_toppings}, 'other') |
```

choices 워크시트에 'other'를 옵션으로 포함하는 것을 잊지 마세요.

## rtSurvey 특정 기능

### 동적 관련성

rtSurvey는 계산된 필드를 기반으로 동적 관련성을 허용합니다:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| 총점        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | 피드백           | ${total_score} > 75             |
```

### 반복 내의 관련성

rtSurvey는 반복 그룹 내에서 관련성을 지원합니다:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | 아동 정보|                        |
| integer      | child_age    | 아동 나이      |                        |
| text         | school_name  | 학교 이름      | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### 계단식 관련성

rtSurvey는 계단식 관련성을 효율적으로 처리합니다. 한 질문의 관련성이 다른 질문에 의존하고, 그 질문이 세 번째 질문에 의존하는 경우:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | 자동차를 소유하고 있습니까?      |                        |
| select_one car_type | car_type | 자동차 종류는?    | ${has_car} = 'yes'     |
| text           | model       | 특정 모델         | ${car_type} = 'sedan'  |
```

## rtSurvey에서 건너뛰기 로직 모범 사례

1. **단순하게 유지**: 가능한 경우 지나치게 복잡한 관련성 조건을 피합니다.
2. **철저히 테스트**: rtSurvey의 미리 보기 기능을 사용하여 설문의 모든 가능한 경로를 테스트합니다.
3. **성능 고려**: 매우 복잡한 건너뛰기 로직은 설문 성능에 영향을 줄 수 있습니다, 특히 모바일 기기에서.
4. **명확한 변수 이름 사용**: 관련성 표현식을 읽고 유지 관리하기 쉽게 합니다.
5. **로직 문서화**: 팀 협업을 위해 복잡한 건너뛰기 패턴을 설명하는 노트를 추가합니다.
6. **데이터 분석 고려**: 건너뛴 질문은 누락된 데이터를 초래합니다. 분석을 그에 맞게 계획합니다.

## 건너뛰기 로직 문제 해결

- **구문 오류**: 모든 `${ }`가 올바르게 닫히고 철자가 맞는지 확인합니다.
- **순환 참조**: 질문이 서로에게 의존하는 루프를 만들지 않습니다.
- **대소문자 구분**: 관련성 표현식에서 답변 선택지는 대소문자를 구분합니다.
- **수치 비교**: 수치 비교에 적절한 연산자 (`<`, `>`, `=`)를 사용합니다.

## 결론

건너뛰기 로직을 효과적으로 사용하면 rtSurvey 프로젝트의 응답자 경험과 데이터 품질을 크게 향상시킬 수 있습니다. rtSurvey의 고급 기능을 활용하고 모범 사례를 따르면 각 응답자의 고유한 상황에 맞게 적응하는 동적이고 효율적인 설문을 만들 수 있습니다.
