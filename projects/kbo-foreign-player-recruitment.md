# SSG 외국인 선수 및 아시아쿼터 영입 분석

## 개요

고려대학교 SDA 2기 프로젝트입니다. 2023년 이후 KBO, MLB/MiLB, NPB, 기사/인터뷰, 구장/날씨 데이터를 결합해 SSG 랜더스의 전력 니즈를 진단하고, 외국인 선수 및 아시아쿼터 후보군을 데이터 기반으로 평가하는 프레임을 설계했습니다.

원본 공개 저장소:

- https://github.com/jameshui0228/kbo-foreign-player-recruitment

## 핵심 질문

단순히 성적이 좋은 선수를 찾는 것이 아니라, 다음 질문에 답하는 것을 목표로 합니다.

- SSG는 타자, 선발, 불펜 중 어디의 marginal value가 가장 큰가?
- KBO에서 성공한 외국인 선수는 입단 전 어떤 패턴을 가졌는가?
- MLB/MiLB/NPB에서는 결함으로 평가되지만 KBO와 SSG 환경에서는 감당 가능한 선수는 누구인가?
- SSG 홈구장, ABS, 로스터 구조, 기사/인터뷰 맥락과 후보의 장단점이 맞는가?

## 수행 내용

- STATIZ, KBO official, Baseball Savant, FanGraphs, NPB official, Naver News API 등 source log 작성
- 데이터 출처, 접근 방식, 한계, 프로젝트 활용 목적을 문서화
- Raw Skill, SSG Need Fit, KBO Translation, Availability, Risk Score 기반 0~100점 랭킹 프레임 설계
- historical transfer backtest를 위한 leakage rule 설계
- 후보명과 추천 순위는 데이터 검증 레이어 통과 전 공개하지 않는 정책 설정

## 현재 단계

현재는 선수 추천 전 사전 설계 및 데이터 검증 단계입니다. 후보의 이름이나 최종 순위는 확정하지 않고, 데이터 소스 감사, 스키마 설계, success metric, feature hypothesis, validation 방식을 먼저 고정하는 방향으로 진행했습니다.

## 사용 기술

Python, Pandas, data dictionary, source logging, ranking framework, leakage control
