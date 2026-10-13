# MLB Monthly State Clustering & Lineup Strategy

[Portfolio](../README.md) · [한국어](mlb-dec-lineup-strategy.ko.md)

**Project type:** Collaborative SDA analysis project<br>
**Focus:** Turning unsupervised clusters into interpretable states and conditional strategy hypotheses<br>
**Public record:** [SDA first-cohort project archive, Korean](https://ku-sda.com/projects/11000000-0000-4000-8000-000000000001)

## Overview

We grouped monthly MLB team and player statistics into comparable states and examined transitions between them. The analysis informed a discussion of the San Francisco Giants' lineup and Jung Hoo Lee's batting-order position.

The recommendation was conditional: monitor whether selected indicators persist before testing a lineup change, rather than claiming a proven performance effect.

## Data & Methods

| Component | Scope |
|---|---|
| Team-month observations | 3,120 |
| Player-month observations | 11,412 |
| Period | 2008-2025 |
| Monthly buckets | Mar/Apr, May, Jun, Jul, Aug, Sep/Oct |
| Clustering | Deep Embedded Clustering (DEC) |
| Selected clusters | 8 for teams; 9 for players |
| Autoencoder latent dimension | 16 |

Preprocessing used median imputation, a Yeo-Johnson power transform, and standard scaling. Features included wOBA, OBP, SLG, ISO, BABIP, strikeout and walk rates, whiff and swing rates, and changes and rolling measures.

## Recorded Results

| Latent-Space Metric | Team Model | Player Model |
|---|---:|---:|
| Silhouette | 0.7938 | 0.791 |
| Davies-Bouldin | 0.2865 | 0.270 |
| Calinski-Harabasz | 14,164.55 | 15,363.44 |

Team cluster C2 had the highest mean win percentage at 0.5834. Player cluster C2 had the highest mean wOBA at 0.4121. We compared the Giants' 2025 monthly states with similar team and player states to frame lineup hypotheses.

These metrics describe **separation in a learned latent space**. They do not establish game-prediction accuracy or the causal effect of a batting-order change. Original-feature-space comparisons, temporal stability, and baseline clustering methods remain important checks.

## Lineup Hypothesis

The report treated the sixth batting position as a reasonable starting point for Lee in its historical context. It proposed considering a trial in the second position if OBP and wOBA thresholds were sustained for six to eight weeks.

## Contribution & Limits

This is a summary of a collaborative project's analytical approach and findings. Individual change records are not provided here, so the full analysis is not presented as my sole work. The WAR and salary analysis in the public archive may cover a different scope from the clustering and lineup extension described on this page.

**Tools:** Python, Pandas, NumPy, scikit-learn, PyTorch, clustering diagnostics, visualization.
