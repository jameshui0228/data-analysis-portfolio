# 스마트 창고 출고 지연 예측 AI 경진대회

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

내부 검증에서 개선된 후보가 리더보드에서 과적합으로 드러난 사례를 기록했습니다. 이후 public-anchor guardrail, drift check, row-level cap 등 보수적 운영 방식을 도입했습니다. 이 경험은 모델 성능뿐 아니라 검증 구조와 리스크 통제가 중요하다는 점을 보여줍니다.

## 사용 기술

Python, Pandas, LightGBM, CatBoost, XGBoost, GroupKFold, residual modeling, drift check
