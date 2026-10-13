# SSG Recruitment Decision Support

[Portfolio](../README.md) · [한국어](kbo-foreign-player-recruitment.ko.md)

**Project type:** Collaborative analysis project, SDA second cohort<br>
**Status:** Final report and presentation completed in June 2026; candidate and market information reflects that period<br>
**Explore:** [Repository](https://github.com/jameshui0228/kbo-foreign-player-recruitment) · [Final report, Korean](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/reports/ssg_overleaf_report_final.pdf) · [Presentation, Korean](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/reports/presentation/SSG_final_presentation_2026-06-24.pdf)

## The Question

Strong performance statistics alone do not make a player a realistic recruitment target. We also needed to assess team fit, how performance might transfer between leagues, and whether contract and market conditions made an approach feasible.

Starting from SSG's roster needs, we combined performance, roster, and transaction data to distinguish **analytically attractive candidates from actionable contact priorities**.

## Outcomes

- Structured a candidate universe of **736 hitters and 1,009 pitchers**. These counts are not the training sample size for the final success and failure models.
- Produced three contact priorities for each role after considering team fit, cross-league translation, availability, and risk.
- Recommended Will Brennan and Josh Fleming as the first contact priorities for hitter and starting pitcher, respectively. This was a project recommendation, not a claim of adoption or recruitment by the club.
- Delivered a **23-page report**, presentation materials, code, result tables, and source and validation records.

![Candidate selection funnel from the original Korean presentation](https://raw.githubusercontent.com/jameshui0228/kbo-foreign-player-recruitment/3d13bc4b91aaefd83dd15da6083abd6d9a932270/outputs/ppt_tables_png/04_candidate_funnel.png)

## My Contribution

The project was collaborative. The changes below provide evidence of work recorded under my account; they are not a measure of contribution percentage or unaided authorship.

| Area | Work | Change History |
|---|---|---|
| Data coverage | Expanded MiLB history, collected official NPB records, and organized data inventories for collaborators | [MiLB](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/ff66dd4), [NPB](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/60e6936) |
| Validation | Compared feature families and documented evaluation results and usage constraints | [Ablation experiments](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/41fa0ac) |
| Feasibility | Incorporated availability and failure-risk considerations into candidate assessment | [Market constraints](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/7b612e0), [risk records](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/ad81bbc) |
| Final deliverables | Consolidated validation records, reports, presentation files, and handover documentation | [Final handover](https://github.com/jameshui0228/kbo-foreign-player-recruitment/commit/3d13bc4) |

The work includes AI-assisted analysis and documentation. The public code, result tables, and review records provide the basis for discussing the contribution.

## A Key Decision: Do Not Treat Training Fit as Generalization

The hitter success and failure models used a small historical sample: **22 rows representing 17 unique players**. Separating in-sample fit from leave-one-player-group-out validation exposed a substantial gap.

| Model | Training AUC | Player-Held-Out AUC |
|---|---:|---:|
| Success classification | 1.000 | 0.650 |
| Failure classification | 0.991 | 0.500 |

We did not present the training scores as predictive performance on unseen players. The final report removed the interpretation of model outputs as absolute success probabilities and used them only as supporting signals for candidate comparison. Contract, cost, and availability checks remained separate.

[Audit table](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/outputs/tables/model_probability_calibration_audit_v1.csv) · [Final validation notes, Korean](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/docs/final_report_last_validation_v1.md)

## Deliverables & Reproducibility

- [Final conclusions and artifact map, Korean](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/docs/final_project_handoff_2026_06_25.md)
- [Final candidate table](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/outputs/tables/final_candidate_board_execution_v4.csv)
- [Feature-family comparison code](https://github.com/jameshui0228/kbo-foreign-player-recruitment/blob/main/src/modeling/run_kbo_feature_family_ablation_v0_3.py)
- [Offline result verification](https://github.com/jameshui0228/kbo-foreign-player-recruitment/tree/main/docs/portfolio)

Full model retraining requires separate source data and access permissions. The public demo checks stored result tables; it does not retrain models, recompute AUC from predictions, or generate current recruitment recommendations.

## Transferable Skills

This project required aligning heterogeneous sources, separating attractiveness from feasibility, and documenting the reasoning and limits behind a recommendation. Those practices are relevant to company research and comparative analysis, without equating this project with professional valuation or investment execution.

**Tools:** Python, Pandas, scikit-learn, data collection and validation, feature ablation, analytical reporting.
