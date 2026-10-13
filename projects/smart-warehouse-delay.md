# Warehouse Dispatch Delay Prediction

[Portfolio](../README.md) · [한국어](smart-warehouse-delay.ko.md)

**Focus:** How validation design changes the meaning of model performance<br>
**Public scope:** Problem, methods, and experiment review. Source code and competition data remain private.

## Overview

A machine-learning competition project predicting average dispatch delay over the next 30 minutes. The challenge was to distinguish performance on repeated scenarios from generalization to previously unseen warehouse layouts.

Rather than replacing a stable baseline with an entirely new model, we explored small residual corrections and documented cases where better internal validation did not translate to better leaderboard performance.

## Data

| Component | Size or Definition |
|---|---|
| Training data | 250,000 rows, 94 columns |
| Test data | 50,000 rows, 93 columns |
| Layout metadata | 300 warehouse layouts |
| Target | `avg_delay_minutes_next_30m` |
| Main internal metric | Mean absolute error (MAE) |

## Validation Design

- GroupKFold by `scenario_id` to separate scenarios.
- GroupKFold by `layout_id` to assess transfer across layouts.
- Scenario sequences treated as 25-row groups when constructing order, lag, rolling, and cumulative features.
- Candidate predictions compared with the strongest public-score reference using correlation, mean absolute difference, and distribution drift.

## Features & Models

Features represented scenario progress, active/idle/charging robot ratios, queues, congestion, dock waits, storage pressure, layout-normalized activity, cyclical time, and missing-value counts.

Modeling experiments included LightGBM, CatBoost, and XGBoost baselines; stacked residual models; routing for seen versus unseen layouts; and layout-, time-, and cluster-based routing. A deep residual sequence model was used as a small correction signal rather than a full replacement predictor.

## Results & Experiment Review

The internal `deep_full_context_residual_pipeline` record reported:

| Internal Validation | MAE |
|---|---:|
| Scenario-based | 8.600033 |
| Layout-based | 8.601428 |

These are distinct validation settings, not official final scores or rankings. The public summary is not sufficient to reproduce them independently.

Some candidates improved internal validation but degraded leaderboard performance, suggesting overfitting or a mismatch in evaluation conditions. Subsequent experiments introduced conservative controls around the public-score reference, drift checks, and per-row correction caps.

## Contribution & Limits

My project experience included feature construction, validation comparisons, residual-model experiments, and analysis of unsuccessful changes. Public evidence of individual task allocation is not included. No reduction in real warehouse delays or operating costs was measured.

**Tools:** Python, Pandas, LightGBM, CatBoost, XGBoost, GroupKFold, residual modeling, drift checks.
