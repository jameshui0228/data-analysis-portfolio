# MLB DEC 군집화 및 이정후 타순 전략 분석

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

## 이정후 타순 전략

보고서에서는 현재 기준 6번 타순 운용을 합리적 출발점으로 두고, 출루율과 wOBA 기준이 6~8주 유지될 경우 2번 타순 테스트를 검토하는 방식으로 결론을 정리했습니다.

## 사용 기술

Python, Pandas, NumPy, Scikit-learn, PyTorch, clustering diagnostics, data visualization
