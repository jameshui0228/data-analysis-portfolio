# K리그 승부 예측 데이터마이닝 프로젝트

## 개요

K리그 경기별 팀 기록 데이터를 기반으로 승/무/패를 예측하는 데이터마이닝 프로젝트입니다.

## 데이터

- 출처: K League 데이터센터
- 데이터 수: 1,368개
- Feature 수: 24개
- Target: win, draw, loss

## 주요 feature

- 득점, 유효 슈팅, 코너킥, 오프사이드, 클리어링, 파울, 경고/퇴장
- 프리킥 크로스 성공률, 드리블 성공률, 크로스 성공률, 태클 성공률
- 홈/원정 구분

## 수행 내용

- 결측치, 이상치, 상관관계, 분포 확인
- Robust scaling 적용
- Decision Tree, Naive Bayes, KNN, Multinomial Logistic Regression, MLP, SVM, Bagging, XGBoost 비교
- Accuracy, Precision, Recall, F1-score로 모델 평가
- Decision Tree, RandomForest, Mutual Information 기반 변수 중요도 검토

## 주요 결과

- Bagging 모델 Accuracy 63.44%, F1-score 58.67%
- 단일 모델 중 MLP가 상대적으로 우수한 성능을 보임
- 득점, 유효 슈팅, 클리어링, 레드카드 등이 주요 변수로 확인
- 무승부 예측은 상대적으로 어려웠으며, 외부 환경 변수와 선수 개별 특성 미반영이 한계로 정리됨

## 사용 기술

Python, Pandas, Scikit-learn, EDA, classification, feature importance
