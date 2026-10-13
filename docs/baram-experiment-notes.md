# DACON BARAM 2026 풍력발전량 예측

> 보존한 실험 메모입니다. 아래 후보 번호와 점수는 당시 Public 기록입니다. 검증 해석과 한계를 포함한 [현재 사례 요약](../projects/baram-2026-wind-power-forecast.md)을 먼저 읽어 주세요.

## 개요

DACON 제3회 풍력발전량 예측 AI 경진대회(BARAM 2026)에 참여해, 세 개의 KPX 그룹에 대한 시간별 풍력 발전량을 예측한 프로젝트입니다. 공개 리더보드 점수만 쫓는 대신 시간 순서를 지키는 검증, 예측 시점에 이용 가능한 데이터만 사용하는 누수 방지, FiCR까지 포함한 공식 평가 지표 재현을 중심으로 실험을 운영했습니다.

대회 데이터와 제출 원본은 공개 공유 제한 및 private 제출 로그를 포함하므로 이 저장소에는 포함하지 않고, 문제 정의·검증 설계·실험 결과·회고만 공개합니다.

## 평가 지표

공식 총점은 다음 두 항의 평균으로 관리했습니다.

```text
total = 0.5 × (1 - nMAE) + 0.5 × FiCR
```

따라서 평균 오차뿐 아니라 정산 성공 구간, 경계 근처 예측, 그룹별 균형과 대형 오차를 함께 관리해야 했습니다.

## 접근 방법

- 공식 train/test/sample schema와 forecast time·issue time·lead time 정렬을 먼저 점검
- 2022→2023, 2023→2024의 time-forward OOF를 사용하고 Group 3의 연도 외삽 성능을 별도로 확인
- LightGBM, CatBoost, XGBoost, TabM-style neural tabular, transformer/TCN, physics/NWP feature 계열을 독립적인 direct foundation으로 비교
- synoptic dynamics, farm-flow, weather consensus, power-curve·regime feature를 forecast-only contract로 구성
- Public best를 anchor로 고정한 뒤 그룹·월·상반기/하반기 단위의 작은 residual sidecar만 직렬 측정
- 모든 후보에 대해 OOF/Test residual 방향, 절대 변화량 비율, key/order/shape, finite/non-negative/capacity 범위를 확인

## Public 결과

아래는 프로젝트 로그와 화면으로 확인한 주요 Public 결과입니다. 점수는 `총점 / 1-nMAE / FiCR` 순서입니다.

| 후보 | 총점 | 1-nMAE | FiCR | 판단 |
|---|---:|---:|---:|---|
| R722 synoptic dynamics direct | 0.6563022737 | 0.8747360462 | 0.4378685013 | 기준 anchor |
| R861 month-stable route | 0.6563424717 | 0.8748093368 | 0.4378756066 | 세 지표 개선 |
| R893 R861 + R670 G1 July sidecar | **0.6563667041** | **0.8748389571** | **0.4378944510** | 확인된 최고 Public |

R893은 R861 대비 총점 `+0.0000242324`, 1-nMAE `+0.0000296203`, FiCR `+0.0000188444`를 기록했습니다. R722 대비로는 세 지표가 각각 `+0.0000644304 / +0.0001029109 / +0.0000259497` 상승했습니다.

R894, R895, R896은 다음 직렬 측정을 위해 생성·계약 검증까지 완료했지만, 이 요약을 작성하는 시점에 별도의 Public 점수로 승격하지 않았습니다. 따라서 최종 검증된 최고 기록은 R893으로 보수적으로 기록합니다.

## 주요 회고

1. OOF 점수가 높아도 2025 Test/Public으로 그대로 전이되지 않았습니다. 특히 broad residual correction과 여러 계열을 한 번에 쌓은 후보는 Public FiCR이 크게 무너질 수 있었습니다.
2. 모델 다양성보다 오류 상관과 시간 전이가 더 중요했습니다. 독립 base model을 만들었지만 전체 대체 모델로는 현재 anchor보다 낮은 경우가 많았습니다.
3. Public 결과는 하나의 aggregate oracle이므로, 후보를 동시에 올리지 않고 한 번에 한 가설만 측정해야 원인과 효과를 구분할 수 있었습니다.
4. R886 계열처럼 OOF 개선만으로 확장한 경로는 즉시 동결했고, 검증된 R861로 되돌린 뒤 작은 direct-anchor sidecar부터 다시 시작했습니다.
5. 작은 수정에서 세 Public 지표가 함께 개선된 기록이 있습니다. 이는 변경 단위를 작게 유지할 실무적 동기가 되었지만, 반복 제출의 선택 편향을 배제하거나 일반화 개선을 입증하지는 않습니다.

## 재현성과 공개 범위

원본 작업 디렉터리에는 연구 자료, feature/model artifacts, 실행 코드, 실험 로그, 제출 CSV가 보존되어 있습니다. 이 공개 포트폴리오 저장소에는 대회 원자료, 외부 데이터 dump, private 제출 이력, 인증 정보와 대용량 모델 산출물을 복사하지 않았습니다. 공개 요약은 결과를 과장하지 않고, 확인된 Public 점수와 실패한 검증 가설까지 함께 기록하는 것을 원칙으로 합니다.

## 사용 기술

Python, Pandas, NumPy, LightGBM, CatBoost, XGBoost, PyTorch, Parquet, time-forward OOF, FiCR audit, residual transfer, covariate-shift check, GitHub
