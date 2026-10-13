# K League Match-Record Classification

[Portfolio](../README.md) · [한국어](k-league-prediction.ko.md)

**Category:** Early data-mining learning project<br>
**Public scope:** Data and classifier-comparison summary<br>
**Interpretation:** Not presented as verified pre-match forecasting until feature timing is rechecked.

## What I Studied

Compared win, draw, and loss classifiers using **1,368 match records and 24 variables** from the K League Data Center. I examined missing values, outliers, correlations, and the effects of scaling and classifier choice.

- **Preprocessing:** Missingness and distribution checks; robust scaling.
- **Models:** Decision tree, naive Bayes, KNN, logistic regression, MLP, SVM, bagging, and XGBoost.
- **Metrics:** Accuracy, precision, recall, and F1.
- **Interpretation:** Tree-based importance and mutual information.

## The Feature-Timing Question

Earlier documentation listed goals, shots on target, corners, clearances, and cards as inputs, but did not establish whether these were **lagged statistics from previous matches or records from the target match itself**.

Post-match information from the target match would not support a pre-match prediction claim. Until that distinction is verified, I classify this as a model-comparison learning record.

Extending it into a forecasting project requires checking:

1. When each variable becomes observable and whether historical aggregation and lags are applied.
2. Chronological training and validation splits.
3. Duplicate matches or teams, and possible leakage in preprocessing.
4. Performance against majority-class and home-team baselines.

## Preserved Results

The earlier record reports bagging accuracy of **63.44%** and F1 of **58.67%**. These remain historical learning results, not established out-of-sample forecasting performance. The available description also does not prove that leakage actually occurred.

## What I Learned

Define what is knowable at prediction time before choosing a model or reporting a score. That question informs how I now document data timing and validation units.

**Tools:** Python, Pandas, scikit-learn, exploratory analysis, classifier comparison.
