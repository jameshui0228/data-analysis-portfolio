# DACON Mosquito Trajectory Prediction

[Portfolio](../README.md) · [한국어](dacon-mosquito-trajectory.ko.md)

**Focus:** Physics baselines, residual correction, and retrieval of similar trajectories<br>
**Public scope:** Experiment summary. Competition data, submission files, and source code remain private.

## Overview

Predict a mosquito's 3D position 80 milliseconds after the last observation. The evaluation rewarded predictions within a 1 cm radius, making the shape of the error distribution important, not just average coordinate error.

We retained a physics-based reference prediction while exploring residual corrections and conservative selection among similar trajectories.

## Task

- **Input:** Eleven 3D positions at 40 ms intervals, from -400 ms to 0 ms.
- **Output:** The x, y, and z coordinates at +80 ms.
- **Metric:** R-Hit@1cm.
- **Hit condition:** 3D Euclidean distance between prediction and target of at most 0.01 m.

## Approach

- Reproduced a constant-velocity baseline aligned with the official approach.
- Explored residual learning around a physics-based reference.
- Engineered velocity, acceleration, jerk, turning angle, and path-efficiency features.
- Tested hit-probability routing and candidate selection.
- Explored motion priors informed by mosquito-flight literature.
- Used KNN memory and trajectory similarity for conservative candidate selection.

## Recorded Results

| Item | Project Record |
|---|---|
| Baseline reproduction score | 0.6006 |
| Best public leaderboard score | 0.6974 |
| Final rank recorded in the project review | 56 |
| Generated candidate submission files | 1,084 |
| Best recorded model family | KNN memory, Gaussian KNN, and KNN consensus selectors |

The 1,084 files are **generated candidates, not the number of leaderboard uploads**. The baseline and public scores are not converted into an improvement rate without evidence that they use the same evaluation split. The score and rank above come from project records; official leaderboard evidence is not attached to this page.

## What I Learned

Under a radius-based hit metric, getting predictions near the boundary just inside the accepted region can matter more than reducing mean error. The recorded experiments favored small corrections around a physics reference and conservative selection over broad replacement.

## Contribution & Limits

My project experience covered physics baselines, trajectory features, residual and selection models, and experiment logging. This summary does not quantify individual contribution or independent implementation.

Exploring many candidates creates a risk of adapting to the public leaderboard. The best public score alone does not establish performance on unseen data.

**Tools:** Python, NumPy, Pandas, scikit-learn, KNN, residual learning, trajectory features, experiment logging.
