# 스마트 창고 출고 지연 예측 AI 경진대회

**한국어** | [English](smart-warehouse-delay.md)

**읽을 포인트:** 데이터가 나뉘는 방식에 따라 모델 성능의 의미가 달라진다는 것을 검토한 사례<br>
**공개 범위:** 문제·접근·실험 회고. 원본 코드와 대회 데이터는 비공개입니다.

## 핵심 결과

같은 시나리오가 학습·평가에 섞이는 문제와, 새로운 창고 배치에 일반화하는 문제를 나눠 검증했습니다. 복잡한 모델로 전부 교체하기보다 안정적인 기준 예측에 작은 보정을 더하는 방향을 실험했습니다. 내부 검증이 좋아져도 리더보드 성능이 나빠질 수 있다는 실패 사례를 기록했습니다.

## 개요

스마트 창고 운영 데이터에서 30분 후 평균 출고 지연 시간을 예측하는 머신러닝 경진대회 프로젝트입니다. 반복 시나리오와 unseen warehouse layout에 모두 robust한 예측을 만드는 것이 핵심 과제였습니다.

## 데이터

- Train: 250,000 rows, 94 columns
- Test: 50,000 rows, 93 columns
- Layout metadata: 300 warehouse layouts
- Target: avg_delay_minutes_next_30m
- 내부 주요 지표: MAE

## 검증 전략

- GroupKFold by scenario_id
- GroupKFold by layout_id
- scenario_id는 25개 row 단위로 보고 row order, time progress, lag, rolling, cumulative feature 구성
- 후보 제출 파일은 public-best backbone과의 correlation, mean absolute difference, distribution drift를 비교

## Feature Engineering

- scenario order: row_in_scenario, time_progress, time_remaining
- robot/load ratio: active/idle/charging ratios
- operational pressure: battery queue, congestion density, dock wait, storage pressure
- layout-normalized features: traffic per aisle width, robots per area, inflow per area
- cyclic time feature
- missing_count

## 모델링

- LightGBM, CatBoost, XGBoost baseline
- stacked/meta residual model
- seen/unseen routing
- route by layout type, time slot, layout cluster
- deep residual sequence model은 직접 예측보다 작은 correction signal로 활용

## 주요 회고

내부 실험 기록의 `deep_full_context_residual_pipeline`은 시나리오 기준 검증 MAE 8.600033, 배치 기준 검증 MAE 8.601428을 보고했습니다. 두 값은 서로 다른 검증 조건이며 공식 최종 점수나 순위가 아닙니다. 이 공개 요약만으로 외부 재현이 가능하다고 주장하지 않습니다.

내부 검증에서 개선된 후보가 리더보드에서 과적합으로 드러난 사례를 기록했습니다. 이후 public-anchor guardrail, drift check, row-level cap 등 보수적 운영 방식을 도입했습니다. 이 경험은 모델 성능뿐 아니라 검증 구조와 리스크 통제가 중요하다는 점을 보여줍니다.

## 사용 기술

Python, Pandas, LightGBM, CatBoost, XGBoost, GroupKFold, residual modeling, drift check

## 역할과 한계

참여 과정에서 다룬 주요 작업은 피처 구성, 검증 기준 비교, 잔차 모델 실험과 실패 회고입니다. 팀별·개인별 분담을 입증하는 공개 기록은 포함하지 않았습니다. 실제 물류 현장의 지연 감소나 비용 절감 효과를 측정한 프로젝트도 아닙니다.

[전체 포트폴리오로 돌아가기](../README.ko.md)
