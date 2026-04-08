---
title: "질문 유형"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey는 모든 표준 XLSForm 질문 유형과 여러 확장 기능을 지원합니다. 각 질문 유형은 수집되는 데이터의 종류와 기기에서 입력 위젯이 렌더링되는 방식을 제어합니다.

질문 유형을 설정하려면 XLSForm의 **survey** 워크시트의 `type` 열에 유형 이름을 입력합니다.

## 텍스트 입력

| 유형 | 설명 |
|------|-------------|
| [text](text) | 자유 텍스트 응답 — 모든 문자 허용 |
| [integer](integer) | 정수 (소수점 없음) |
| [decimal](decimal) | 소수점이 있는 숫자 |
| [range](range) | 정의된 최소/최대 범위 내의 슬라이더로 선택된 숫자 |

## 선택

| 유형 | 설명 |
|------|-------------|
| [select_one listname](select-one) | 목록에서 정확히 하나의 옵션 선택 |
| [select_multiple listname](select-multiple) | 목록에서 하나 이상의 옵션 선택 |
| [rank listname](rank) | 선호도나 우선순위에 따라 선택지 순서 지정 |

## 날짜 및 시간

| 유형 | 설명 |
|------|-------------|
| [date](date) | 달력 날짜 (연, 월, 일) |
| [time](time) | 하루 중 시간 (시, 분) |
| [datetime](datetime-date-time) | 날짜와 시간 결합 |

## 위치

| 유형 | 설명 |
|------|-------------|
| [geopoint](geopoint) | 단일 GPS 좌표 (위도, 경도, 고도, 정확도) |
| [geotrace](geotrace) | 경로 — 선을 형성하는 일련의 GPS 점 |
| [geoshape](geoshape) | 구역 — GPS 점의 폐쇄 다각형 |

## 미디어

| 유형 | 설명 |
|------|-------------|
| [image](image) | 사진 캡처 또는 이미지 업로드 |
| [audio](audio) | 오디오 녹음 |
| [video](video) | 비디오 녹화 |
| [file](file) | 일반 파일 업로드 (PDF, 문서 등) |

## 기타

| 유형 | 설명 |
|------|-------------|
| [barcode](barcode) | 바코드 또는 QR 코드 스캔 |
| [note](note) | 읽기 전용 표시 텍스트 — 지침 또는 계산된 요약 표시 |
| [calculate](calculate) | 계산된 값을 저장하는 숨겨진 필드 |
| [hidden](hidden) | 정적 또는 미리 채워진 값을 저장하는 숨겨진 필드 |
| [trigger / acknowledge](trigger) | 조사원이 진술을 읽었음을 확인하기 위해 반드시 체크해야 하는 체크박스 |
| [meta](meta) | 자동 메타데이터: 타임스탬프, 기기 ID, 조사원 정보 |

## rtSurvey 확장

이 유형들은 rtSurvey 전용이며 표준 XLSForm 사양의 일부가 아닙니다.

| 유형 | 설명 |
|------|------|
| [search-autocomplete](search-autocomplete) | 실시간 API 기반 자동 완성 제안이 있는 텍스트 입력 |
| [mentions](mentions) | 엔티티를 인라인으로 태그하기 위한 `@` 멘션 자동 완성이 있는 텍스트 필드 |
| [texttags](texttags) | 태그 입력 — 각 항목이 제거 가능한 칩이 됨; 공백으로 구분된 문자열로 저장 |

반복 그룹에 대해서는 [Repeats](../advanced-extension/repeats) 참조

## 유형과 appearance의 작동 방식

`type`은 **수집되는 데이터**를 결정합니다. `appearance` 열은 **위젯의 모양**을 제어합니다. 많은 유형이 여러 appearance를 지원합니다 — 예를 들어 `select_one`은 라디오 버튼, 드롭다운, Likert 척도 또는 컴팩트 그리드로 나타날 수 있습니다.

전체 옵션 목록은 [Appearance](../appearance)를 참조하세요.
