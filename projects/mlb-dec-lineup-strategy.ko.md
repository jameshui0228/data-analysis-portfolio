# MLB DEC 군집화 및 이정후 타순 전략 분석

**한국어** | [English](mlb-dec-lineup-strategy.md)

**형태:** SDA 공동 분석 프로젝트<br>
**읽을 포인트:** 비지도학습의 군집을 설명 가능한 상태와 전략 가설로 연결한 경험<br>
**관련 공개 기록:** [SDA 1기 프로젝트 아카이브](https://ku-sda.com/projects/11000000-0000-4000-8000-000000000001)

## 핵심 결과

팀·선수의 월별 지표와 변화량을 묶어 유사 상태를 찾고, 특정 선수의 활용 전략을 논의하는 근거로 정리했습니다. 최종 전략은 확정된 효과를 주장하기보다 지표가 일정 기간 유지되는지를 확인한 뒤 타순 변경을 검토하는 조건부 가설로 제시했습니다.

## 개요

MLB 팀과 선수의 월별 상태를 비지도학습으로 군집화하고, 군집별 성과와 전이 구조를 바탕으로 SF Giants와 이정후 선수의 타순 배치 전략을 분석한 프로젝트입니다.

## 데이터

- Team-month: 3,120 observations
- Player-month: 11,412 observations
- 기간: 2008~2025
- 월 단위 bucket: Mar/Apr, May, Jun, Jul, Aug, Sep/Oct

## 방법론

- Deep Embedded Clustering(DEC) 적용
- 팀 모델 k=8, 선수 모델 k=9 선정
- autoencoder latent dimension 16
- median imputation, Yeo-Johnson PowerTransformer, StandardScaler 적용
- wOBA, OBP, SLG, ISO, BABIP, K%, BB%, whiff rate, swing rate, delta/rolling feature 구성

## 주요 결과

- 팀 모델 latent 평가: Silhouette 0.7938, Davies-Bouldin 0.2865, Calinski-Harabasz 14164.55
- 선수 모델 latent 평가: Silhouette 0.791, Davies-Bouldin 0.270, Calinski-Harabasz 15363.44
- 팀 군집 중 C2가 평균 win_pct 0.5834로 가장 높은 성과를 보임
- 선수 군집 중 C2가 평균 wOBA 0.4121로 가장 높은 성과를 보임
- SF 2025 월별 상태와 유사 top team/player state를 비교해 타순 배치 전략으로 연결

위 군집 지표는 **학습된 잠재공간에서의 분리도**입니다. 높은 Silhouette 점수가 실제 경기 예측력이나 타순 변경의 인과적 효과를 입증하지는 않습니다. 원공간 비교, 시기별 안정성, 기준 군집 방법과의 비교를 함께 확인해야 합니다.

## 이정후 타순 전략

보고서에서는 현재 기준 6번 타순 운용을 합리적 출발점으로 두고, 출루율과 wOBA 기준이 6~8주 유지될 경우 2번 타순 테스트를 검토하는 방식으로 결론을 정리했습니다.

## 사용 기술

Python, Pandas, NumPy, Scikit-learn, PyTorch, clustering diagnostics, data visualization

## 역할과 한계

참여한 공동 프로젝트의 분석 접근과 결과를 정리한 사례입니다. 이 페이지에 개인별 변경 기록은 포함하지 않았으므로 전체 분석을 개인 단독 성과로 설명하지 않습니다. 공개 아카이브의 WAR·연봉 분석과 이 문서의 군집·타순 확장 분석은 다루는 범위가 다를 수 있습니다.

[전체 포트폴리오로 돌아가기](../README.ko.md)
