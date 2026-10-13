# SSG 영입 의사결정 분석 | 성능과 실행 가능성을 함께 비교하기

**형태:** SDA 2기 공동 분석 프로젝트<br>
**상태:** 2026년 6월 발표·최종 보고서 완료 / 아래 후보·시장 정보는 당시 기준<br>
**바로 보기:** [원본 저장소](https://github.com/jameshui0228/kbo-foreign-player-recruitment) · [최종 보고서 PDF](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/reports/ssg_overleaf_report_final.pdf) · [발표 PDF](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/reports/presentation/SSG_final_presentation_2026-06-24.pdf)

## 문제

성적이 높은 선수를 찾는 것만으로는 영입 의사결정을 내리기 어렵습니다. 팀의 약점에 맞는지, 다른 리그의 성적이 얼마나 이전될지, 계약과 시장 접근성이 확보되는지를 함께 비교해야 했습니다.

SSG의 보강 필요를 정의한 뒤, 여러 리그의 성적·로스터·거래 정보를 연결해 **분석상 매력적인 후보와 실제 접촉할 후보를 구분하는 과정**을 설계했습니다.

## 핵심 결과

- 구조화된 후보 시장: 타자 **736명**, 투수 **1,009명**. 이는 최종 성공·실패 모델의 학습 표본 수와 다릅니다.
- 팀 적합성, 리그 간 성적 이전, 계약·시장 접근성, 위험 신호를 검토해 타자·투수 각 3명의 접촉 우선 후보를 정리했습니다.
- 최종 제안은 타자 Will Brennan, 선발투수 Josh Fleming을 각각 접촉 1순위로 두었습니다. 구단의 실제 영입·채택 성과를 주장하는 프로젝트는 아닙니다.
- **23쪽 최종 보고서**, 발표 자료, 코드, 결과 표, 출처·검증 기록을 남겼습니다.

![공개 발표 자료의 후보 선정 과정](https://raw.githubusercontent.com/jameshui0228/kbo-foreign-player-recruitment/3d13bc4b91aaefd83dd15da6083abd6d9a932270/outputs/ppt_tables_png/04_candidate_funnel.png)

## 내 역할과 기여 근거

공동 프로젝트이며, 아래는 제 계정의 변경 기록으로 확인할 수 있는 기여 영역입니다. 커밋은 작업 이력의 근거이지 개인 기여율이나 독립 작성 능력의 수치가 아닙니다.

| 기여 영역 | 구체적인 작업 | 변경 기록 |
|---|---|---|
| 데이터 확장 | MiLB 이력 보강, NPB 공식 기록 수집, 팀원용 데이터 목록 정리 | [MiLB 보강](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/ff66dd4), [NPB 수집](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/60e6936) |
| 모델 검증 | 피처 집합별 비교 실험, 검증 결과와 사용 조건 정리 | [비교 실험](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/41fa0ac) |
| 실행 가능성 | 시장 접근성과 실패 위험을 후보 평가에 연결 | [시장 조건](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/7b612e0), [리스크 기록](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/ad81bbc) |
| 결과물 통합 | 최종 검증 기록, 보고서·발표 자료, 팀원용 인수인계 문서 정리 | [최종 산출물 정리](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/3d13bc4) |

AI 보조 도구를 활용한 분석·문서화 작업을 포함합니다. 도구의 생성 결과를 성과로 삼기보다, 공개된 코드·결과 표·검증 기록을 기준으로 작업을 설명합니다.

## 중요한 판단: 높은 점수를 그대로 믿지 않기

타자 성공·실패 모델은 22행, 고유 선수 17명으로 학습 표본이 작았습니다. 학습 데이터 적합도와 선수 단위 외부 검증을 구분하면 다음 차이가 나타났습니다.

| 평가 대상 | 학습 데이터 AUC | 선수 단위 제외 검증 AUC |
|---|---:|---:|
| 성공 분류 | 1.000 | 0.650 |
| 실패 분류 | 0.991 | 0.500 |

학습 데이터의 높은 수치를 일반화 성능으로 해석하지 않았습니다. 최종 보고서에서는 모델 출력의 ‘성공확률’ 표현을 제거하고, 후보 간 비교를 보조하는 신호로 한정했습니다. 계약·비용·시장 접근성은 별도로 확인하도록 정리했습니다.

근거: [모델 검증 원표](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/outputs/tables/model_probability_calibration_audit_v1.csv) · [최종 검증 기록](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/docs/final_report_last_validation_v1.md)

## 산출물과 재현 범위

- [최종 결론·산출물 위치](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/docs/final_project_handoff_2026_06_25.md)
- [최종 후보 표](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/outputs/tables/final_candidate_board_execution_v4.csv)
- [피처 집합 비교 코드](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/src/modeling/run_kbo_feature_family_ablation_v0_3.py)
- [원자료 없이 실행하는 결과 확인 예제](https://github.com/jameshui0228/kbo-foreign-player-recruitment/tree/main/docs/portfolio)

전체 모델 재학습에는 별도 원자료와 접근 권한이 필요합니다. 공개 예제는 저장된 결과 표를 검산하는 경로이며 모델 재학습이나 최신 후보 추천이 아닙니다.

## 다른 업무에 적용할 수 있는 점

서로 다른 출처를 공통 기준으로 정리하고, 매력도와 실행 제약을 나눠 비교하며, 판단의 근거와 한계를 문서화하는 경험입니다. 기업 조사·비교 분석으로 확장할 수 있는 작업 방식이지만, 기업가치 평가나 실제 투자 집행 경험과 동일시하지 않습니다.

**기술:** Python, Pandas, scikit-learn, 데이터 수집·검증, 피처 비교, 보고서 작성

[전체 포트폴리오로 돌아가기](../README.md)
