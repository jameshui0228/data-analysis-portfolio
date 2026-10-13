# DACON 모기 비행 궤적 예측 AI 경진대회

**한국어** | [English](dacon-mosquito-trajectory.md)

**읽을 포인트:** 물리 기반 기준 모델에서 출발해 유사 궤적을 활용한 보정으로 확장한 사례<br>
**공개 범위:** 실험 요약. 대회 원자료·제출 파일과 원본 코드는 비공개입니다.

## 핵심 결과

단순히 평균 좌표 오차를 낮추는 대신, 예측점이 실제 위치에서 1cm 안에 들어오는지를 기준으로 접근을 바꿨습니다. 물리 모델을 유지하면서 잔차 보정과 유사 궤적 탐색을 실험했고, 프로젝트 회고에는 최고 Public 점수 0.6974와 최종 순위 56위가 기록되어 있습니다.

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

`1,084개`는 **생성한 제출 후보 파일 수**이며 실제 대회 업로드 횟수가 아닙니다. 기준 모델의 검증 점수와 Public 점수는 평가 분할이 같다는 근거 없이 직접 개선율로 환산하지 않습니다. 순위와 점수는 프로젝트 기록 기준이며 이 페이지에 공식 리더보드 증빙은 첨부하지 않았습니다.

## 배운 점

이 대회에서는 평균 오차를 낮추는 것보다 1cm boundary 근처의 샘플을 안정적으로 안쪽으로 넣는 전략이 중요했습니다. 따라서 broad replacement보다 strong physics anchor 주변의 작은 보정, conservative gate, memory-based candidate selection이 효과적이었습니다.

## 사용 기술

Python, NumPy, Pandas, Scikit-learn, trajectory feature engineering, KNN, residual learning, experiment logging

## 역할과 한계

참여 과정에서 물리 기준 모델, 궤적 피처, 잔차·선택 모델, 실험 기록을 다뤘습니다. 공개 요약은 팀 내 기여율이나 독립 구현량을 의미하지 않습니다. 많은 후보를 검토한 만큼 리더보드 적응 위험이 있으며, Public 최고점만으로 보지 못한 데이터에 대한 성능을 보장하지 않습니다.

[전체 포트폴리오로 돌아가기](../README.ko.md)
