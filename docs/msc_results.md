# Original MSc Results — Verified Historical Record

This document records the original MSc model-comparison results recovered from the dissertation. It is kept separate from the later robustness experiments.

## Historical model comparison

| Model | Original MSc test accuracy |
|---|---:|
| Random Forest | 81.82% |
| XGBoost | 80.17% |
| Logistic Regression | 78.93% |
| Decision Tree | 78.93% |
| Gradient Boosting | 78.93% |
| KNN | 78.51% |
| Gaussian NB | 78.51% |
| SVC | 71.90% |

The original Random Forest implementation also reported approximately **81.40%** test accuracy before the later tuned model-comparison stage.

## Historical data split

The original dissertation reported 482 positive movement observations and 404,702 negative observations. It sampled 482 negative observations to form a balanced modelling subset, then used a 75/25 train/test split. This produced 722 training observations and 242 test observations.

## How to interpret these results

These numbers are useful for documenting what the MSc actually did and for showing the starting point of the research trajectory. They are **not** the headline evidence for the current research question because the historical workflow deliberately balanced the classes and used accuracy as its principal metric.

The current extension preserves the full rare-event distribution and evaluates precision-recall behaviour, chronological generalisation, unseen-device generalisation, feature ablation, threshold sensitivity and uncertainty.

## Figure policy

Figures generated from the dataset using the notebook are labelled **reconstructed** rather than described as the original dissertation artwork. This avoids confusing a modern reproduction with the original 2021 figure.

See:

- `notebooks/02_msc_original_analysis.ipynb`
- `src/msc_original.py`
- `docs/msc_original_implementation.md`
- `results/msc_original_results.csv`
