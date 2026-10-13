# Statiz KBO Win Prediction

[Portfolio](../README.md) · [한국어](statiz-kbo-prediction.ko.md)

**Focus:** Managing information availability and prediction operations alongside model performance<br>
**Public scope:** Case study only. Source code, raw data, and submission records are maintained privately.

## Overview

A competition project predicting the probability that the home team wins a KBO game. The work covered rule compliance, leakage control, daily reproducibility, and model versioning, not just offline scores.

We constructed a pre-game dataset, compared classifiers, and tracked prediction files and submissions. Operational checks identified home-team bias and overconfident probabilities, leading to input audits and calibration-related changes.

## Problem & Constraints

- **Target:** Home-team win outcome and probability.
- **Data:** 2023-2025 regular seasons and a subset of completed 2026 games.
- **Information boundary:** Features must be available before the target game starts.
- **Competition constraint:** Statiz-provided data only; no external sources.

## Work Completed

- Reviewed collection coverage across schedule, roster, lineup, playerDay, teamRecord, playerSeason, playerSituation, and boxscore APIs.
- Converted raw JSONL and CSV records into game-level datasets.
- Redesigned the training pipeline to exclude same-day leakage and post-game information.
- Compared CatBoost, XGBoost, LightGBM, Random Forest, Extra Trees, logistic regression, SVM, MLP, HistGradientBoosting, and AdaBoost.
- Maintained versioned prediction files, submission logs, data manifests, and a daily prediction index.

## Results & Evaluation Context

| Evaluation | Accuracy | AUC |
|---|---:|---:|
| Model V1, 2025 holdout | 0.59596 | 0.61316 |

CatBoost became the core operational model. During 2026 prediction runs, we identified home-team bias, overconfidence in the 60-70% probability range, and unreliable live-data updates. V5 introduced starting-pitcher prior and recent metrics, probability shrinkage, and caps and floors.

The table reports **V1 only**. It does not establish a like-for-like V5 improvement or a final competition ranking. Calibration-related changes are described as operational changes unless evaluated separately for generalization.

## What I Learned

A model's usefulness depends on input timing, leakage controls, probability calibration, distribution changes, and traceable prediction logs. A high score is not a reason to skip data-quality and risk checks.

## Contribution & Limits

This summary describes analysis and operational work within a project I participated in. It does not establish individual task allocation or enable external reproduction of the full pipeline. For inspectable code and personal change history, see the [public SSG case study](kbo-foreign-player-recruitment.md).

**Tools:** Python, Pandas, scikit-learn, CatBoost, XGBoost, LightGBM, GitHub, Markdown reporting.
