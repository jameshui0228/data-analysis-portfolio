# DACON 모기 비행 궤적 예측 AI 경진대회

## 개요

모기의 짧은 3D 비행 궤적을 보고 마지막 관측 시점 기준 +80ms 위치를 예측하는 DACON AI 경진대회 프로젝트입니다.

## 문제 정의

- 입력: -400ms부터 0ms까지 40ms 간격의 3D 좌표 11개
- 출력: +80ms 시점의 x, y, z 좌표
- 평가 지표: R-Hit@1cm
- hit 조건: 예측점과 정답점의 3D Euclidean distance가 0.01m 이하

## 접근 방식

- 공식 스타일 constant velocity baseline 재현
- physics anchor 기반 residual learning
- 최근 속도, 가속도, jerk, turn angle, path efficiency 등 trajectory feature engineering
- hit probability routing 및 candidate selector
- 모기 비행 논문 기반 motion prior 실험
- KNN memory selector와 trajectory similarity 기반 conservative selector 적용

## 주요 결과

- 공식 baseline 재현 점수: 0.6006
- 최고 Public LB: 0.6974
- 최종 순위: 56위
- 생성 submission 후보 수: 1,084개
- 최종 best family: KNN memory selector / Gaussian KNN selector / KNN consensus

## 배운 점

이 대회에서는 평균 오차를 낮추는 것보다 1cm boundary 근처의 샘플을 안정적으로 안쪽으로 넣는 전략이 중요했습니다. 따라서 broad replacement보다 strong physics anchor 주변의 작은 보정, conservative gate, memory-based candidate selection이 효과적이었습니다.

## 사용 기술

Python, NumPy, Pandas, Scikit-learn, trajectory feature engineering, KNN, residual learning, experiment logging
