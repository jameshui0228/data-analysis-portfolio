# BARAM 2026 | Wind Power Forecasting

[Portfolio](../README.md) · [한국어](baram-2026-wind-power-forecast.ko.md)

**Project type:** Participation in the third DACON Wind Power Forecasting AI Competition<br>
**Public scope:** Analysis and experiment review. Raw data, model files, and submission records remain private.

## The Problem

Forecast hourly wind generation for three KPX groups using only weather information available at prediction time. The task required managing both normalized error and an incentive-related success metric.

## Recorded Results

The highest public composite score in the project records was **0.6563667041**. This is not a final private score or ranking. The emphasis of this case study is temporal validation, information availability, and experiment traceability.

| Metric | Best Recorded Public Candidate |
|---|---:|
| Composite score | 0.6563667041 |
| 1 - nMAE | 0.8748389571 |
| FiCR | 0.4378944510 |

The recorded scoring formula was `0.5 * (1 - nMAE) + 0.5 * FiCR`. More complex models did not automatically improve results; some broad residual corrections degraded public performance.

## Work Completed

1. Aligned weather forecast issue times, target times, and forecast intervals, and checked input schemas.
2. Used forward-in-time validation from 2022 to 2023 and from 2023 to 2024.
3. Compared boosting, neural-network, and physics- and weather-feature approaches.
4. Changed one hypothesis at a time from a reference prediction and logged errors by group and period.
5. Checked row order, keys, missing values, negative predictions, and capacity limits before submission.

## What I Learned

An internal improvement did not always transfer to the following year. Error overlap and temporal distribution changes mattered alongside model complexity.

Repeatedly inspecting small public-score differences also creates leaderboard adaptation risk. A small gain is not automatically evidence of generalization or a causal explanation of why a change worked. Final evaluation and real-world operating impact were not established in this summary.

This page describes experiments and validation work in a project I participated in; it does not quantify individual versus team contributions.

## Further Reading

Detailed candidate scores, changes, and unsuccessful hypotheses remain in the [original experiment notes (Korean)](../docs/baram-experiment-notes.md). Interpret those records with the evaluation context and limitations above.

**Tools:** Python, Pandas, NumPy, LightGBM, CatBoost, XGBoost, PyTorch, temporal validation, experiment tracking.
