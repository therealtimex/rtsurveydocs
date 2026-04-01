---
title: "고급 반복"
description: "반복 그룹을 위한 고급 패턴: 동적 횟수, 중첩 반복, 반복 데이터 요약 및 반복 전체에서 값 참조."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

이 페이지는 rtSurvey에서 반복 그룹을 사용하기 위한 고급 패턴을 다룹니다. 반복 그룹 설정의 기본 사항은 [그룹화 및 반복](../repeats)을 참조하세요.

---

## 동적 반복 횟수

기본적으로 조사원이 반복 횟수를 결정합니다. `repeat_count`를 사용하여 반복 횟수를 고정할 수 있습니다:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | 가구원 | `${num_members}` |
| text | member_name | 이름 | |
| integer | member_age | 나이 | |
| end_repeat | | | |

반복은 정확히 `${num_members}` 번 실행됩니다. 여기서 `num_members`는 양식의 앞 부분에서 수집되었습니다. 조사원은 인스턴스를 추가하거나 제거할 수 없습니다.

---

## 인덱스 액세스: `indexed-repeat()`

반복 그룹 **외부**에서 `indexed-repeat(repeatedField, repeatGroup, index)`를 사용하여 특정 반복 인스턴스의 필드 값에 액세스합니다:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

이는 반복 후 요약 필드를 작성하거나 "기본" 구성원의 데이터를 참조하는 데 유용합니다.

---

## 현재 인스턴스 위치: `index()`

반복 그룹 내에서 `index()`는 현재 인스턴스의 1기반 위치를 반환합니다. 각 반복에 레이블을 지정하거나 고유 식별자를 만드는 데 사용합니다:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | 필지 |
| note | plot_label | 필지 번호 ${index()} |
| text | plot_id | 필지 ID |
| end_repeat | | |

---

## 같은 인스턴스의 필드 참조

반복 내에서 `${fieldname}`을 사용하여 **같은 반복 인스턴스**의 다른 필드를 참조합니다. 같은 루프 내에서는 `indexed-repeat()`가 필요하지 않습니다:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | 구성원 | |
| text | member_name | 이름 | |
| integer | member_age | 나이 | |
| text | school_name | 학교 이름 | `${member_age} < 18` |
| end_repeat | | | |

---

## 반복 내부에서 상위 필드 참조

반복 그룹 외부 (위)의 필드는 `${fieldname}`으로 정상적으로 참조할 수 있습니다:

| type | name | label |
|------|------|-------|
| text | village | 마을 이름 |
| begin_repeat | plots | 농지 |
| note | plot_context | ${village}의 필지 |
| end_repeat | | |

---

## 반복 데이터 요약

반복 그룹 **외부**에서 반복 집계 함수를 사용하여 요약합니다:

| 함수 | 예시 | 설명 |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | 인스턴스 수 |
| `sum(field)` | `sum(${loan_amount})` | 숫자 필드의 합계 |
| `min(field)` | `min(${member_age})` | 최솟값 |
| `max(field)` | `max(${member_age})` | 최댓값 |
| `join(sep, field)` | `join(', ', ${member_name})` | 쉼표로 구분된 목록 |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | 조건부 카운트 |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | 조건부 합계 |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | 조건부 조인 |

### 예시: 가구 요약

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | 가구원 수는? | |
| begin_repeat | members | 구성원 | `${num_members}` |
| text | member_name | 이름 | |
| integer | member_age | 나이 | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members}명; 18세 미만 ${children_count}명. 성인: ${adult_names} | |

---

## 중첩 반복

반복 그룹은 다른 반복 그룹을 포함할 수 있습니다. 중첩 반복은 복잡성을 추가하고 조사원에게 혼란스러울 수 있으므로 신중하게 사용합니다.

| type | name | label |
|------|------|-------|
| begin_repeat | households | 가구 |
| text | hh_id | 가구 ID |
| begin_repeat | hh_members | 구성원 |
| text | member_name | 구성원 이름 |
| end_repeat | | |
| end_repeat | | |

내부 반복에서 외부 반복의 필드를 참조하려면 `${fieldname}`을 사용합니다 — 가장 가까운 일치하는 조상으로 해석됩니다:

`hh_members` 반복 내에서 `${hh_id}`는 모든 가구가 아닌 **현재** 가구의 ID를 반환합니다.

---

## 반복 그룹에서 순위: `rank-index()`

반복 내에 `rank` 필드가 있는 경우, 외부에서 특정 인스턴스의 서수 순위를 가져오기 위해 `rank-index(instanceNumber, repeatedField)`를 사용합니다:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})`는 가장 높은 점수의 인스턴스 인덱스를 반환합니다.

---

## 모범 사례

1. 반복 횟수가 미리 알려진 경우 항상 `repeat_count`를 사용합니다 — 조사원이 실수로 인스턴스를 추가하거나 제거하는 것을 방지합니다.
2. 반복 그룹을 집중적으로 유지합니다 — 인스턴스당 20개 이상의 질문이 있는 반복은 탐색하기 어렵습니다.
3. 반복 그룹에 명확한 이름을 사용합니다 (예: `household_members`가 아닌 `repeat1`) — 이름은 함수 호출 및 내보낸 데이터에 나타납니다.
4. 성능을 확인하기 위해 예상 최대 인스턴스 수로 테스트합니다.
5. 모바일에서 인스턴스당 모든 필드를 한 화면에 표시하려면 반복 그룹에 `field-list` appearance를 사용합니다.

---

## 제한 사항

- `indexed-repeat()`는 유효한 인덱스 (1에서 인스턴스 수까지)가 필요합니다 — 범위를 벗어난 인덱스는 빈 값을 반환합니다.
- 2수준을 초과하는 중첩 반복은 권장되지 않으며 일부 클라이언트에서 표시 문제가 발생할 수 있습니다.
- 집계 함수 (`sum`, `count` 등)는 전체 반복 그룹에서 작동합니다 — `*-if` 변형 없이는 인스턴스의 하위 집합을 집계할 수 없습니다.
