# Statiz KBO 승부예측 프로젝트

**읽을 포인트:** 모델 성능뿐 아니라 데이터 반영 시점과 예측 운영을 함께 관리한 사례<br>
**공개 범위:** 분석·운영 요약. 원본 코드·원자료·제출 이력은 비공개 저장소에서 관리합니다.

## 핵심 결과

경기 전 정보만 사용하는 데이터셋을 구성하고, 여러 분류 모델을 비교한 뒤 예측 파일·모델 버전·제출 기록을 함께 관리했습니다. 운영 중에는 홈팀 편향과 확률 과신을 발견해, 높은 확률을 그대로 사용하는 대신 보정과 입력 데이터 점검을 진행했습니다.

## 개요

스탯티즈 KBO 승부예측 공모전용 실전 운영 프로젝트입니다. 목표는 KBO 경기의 홈팀 승률을 예측하는 것이며, 단순 모델 성능뿐 아니라 규정 준수, 데이터 누수 방지, 일별 예측 재현성, 모델 버전 관리까지 포함해 운영했습니다.

## 문제 정의

- Target: 홈팀 승리 여부 및 홈팀 승률
- 데이터 범위: 2023~2025 정규시즌, 2026 완료 경기 일부
- 기본 원칙: 경기 시작 전 알 수 있는 정보만 feature로 사용
- 제한 조건: Statiz 제공 데이터만 사용, 외부 데이터 사용 금지

## 수행 내용

- schedule, roster, lineup, playerDay, teamRecord, playerSeason, playerSituation, boxscore 등 API 데이터 수집 범위 점검
- raw JSONL/CSV를 경기 단위 clean dataset으로 재구성
- same-day leakage와 postgame 정보를 제거한 학습 파이프라인 재설계
- CatBoost, XGBoost, LightGBM, RandomForest, ExtraTrees, LogisticRegression, SVM, MLP, HistGradientBoosting, AdaBoost 비교
- 모델 버전별 예측 파일, 제출 로그, 데이터 manifest, daily prediction index 관리

## 주요 결과

- Model V1 기준 2025 holdout Accuracy 0.59596, AUC 0.61316 확인
- CatBoost 중심의 운영 모델을 선정
- 2026 실전 운영 중 홈팀 편향, 60~70% 구간 과신, live data 반영 불안정 문제를 발견
- V5에서는 선발투수 prior/recent metric 반영, 확률 shrink, favorite cap/floor 등 운영 안정성 개선

위 수치는 **V1의 2025 holdout 평가**입니다. V5의 동일 조건 개선율이나 최종 대회 순위는 이 문서에서 확인되지 않으므로 주장하지 않습니다. 확률 보정도 일반화 성능 개선을 별도 평가하기 전에는 운영상 변경으로 구분합니다.

## 배운 점

예측 모델은 오프라인 점수만으로 평가하기 어렵고, 실제 운영에서는 데이터 반영 시점, 누수 통제, 확률 캘리브레이션, 분포 변화, 제출 로그가 함께 관리되어야 한다는 점을 학습했습니다. 이는 금융/투자 의사결정에서도 모델 신호를 그대로 믿기보다 데이터 품질과 리스크를 함께 점검해야 한다는 관점과 연결됩니다.

## 사용 기술

Python, Pandas, Scikit-learn, CatBoost, XGBoost, LightGBM, GitHub, Markdown report

## 역할과 확인 범위

이 요약은 참여한 프로젝트의 분석·운영 경험을 설명합니다. 현재 공개 자료는 개인·팀별 작업 분담이나 전체 파이프라인의 외부 재현까지 증명하지 않습니다. 검토 가능한 코드와 개인 변경 이력이 필요한 경우에는 [공개 SSG 사례](kbo-foreign-player-recruitment.md)를 함께 제시합니다.

[전체 포트폴리오로 돌아가기](../README.md)
