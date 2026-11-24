# Experimental Protocol

## Objective

Evaluate human-movement prediction models under conventional and distribution-shift-aware evaluation settings while preserving the extreme rare-event structure of the dataset.

## Experiment sequence

| ID | Experiment | Status | Purpose |
|---|---|---|---|
| E01 | Dataset validation | Complete | Confirm structure, target, missingness, timestamp and data quality |
| E02 | Class distribution | Complete | Quantify movement-event imbalance |
| E03 | Historical MSc baseline reconstruction | Complete | Establish the documented starting point from the MSc work |
| E04 | Random Logistic Regression | Complete | Interpretable baseline classifier |
| E05 | Random Forest | Complete | Non-linear ensemble baseline |
| E06 | Histogram Gradient Boosting | Complete | Additional non-linear model |
| E07 | Chronological evaluation | Complete | Test performance on later observations |
| E08 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E09 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E10 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E11 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E12 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E13 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E14 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E15 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E16 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E17 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E18 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E19 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E20 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E21 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E22 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E23 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |
| E24 | PhD-stage experiment (to be defined) | Planned for PhD | To be designed and carried out during the PhD with supervisor guidance |

Experiments E08–E24 are reserved for the PhD stage. They have not been carried out as part of the current research record. Their exact questions, methods and order will be agreed during the PhD after the literature review and discussion with the supervisor.

## Canonical model configurations

The current research-extension model factories are defined in `src/models.py` and use random seed 42 where supported:

- Logistic Regression: balanced class weights, median imputation, standard scaling, `max_iter=2000`.
- Random Forest: 30 trees, maximum depth 12, minimum leaf size 20, square-root feature sampling, balanced class weights, 50% row subsampling and `n_jobs=-1`.
- Histogram Gradient Boosting: 50 iterations, learning rate 0.08, 15 maximum leaf nodes, minimum leaf size 50 and early stopping disabled.

These configurations define the current canonical pipeline. They should not be mixed with later conflicting reruns.

## Split and threshold rules

### Random evaluation

Use a stratified 60/20/20 train/validation/test split with random seed 42.

### Temporal evaluation

Sort by verified Unix-second timestamp and split chronologically into 60% train, 20% validation and 20% test.

### Threshold selection

Select the decision threshold using validation-set F1 only. Do not use test labels to choose the threshold.

## Required reporting for each experiment

- Dataset version/source
- Dataset hash
- Number of observations
- Features used
- Target definition
- Train/validation/test strategy
- Preprocessing
- Model and parameters
- Random seed, where applicable
- Threshold-selection rule
- Evaluation metrics
- Main result
- Interpretation
- Limitations
- Code version/commit

## Current canonical reference metrics

The audited research record currently reports average precision (AP):

| Evaluation | Logistic Regression | HistGradientBoosting | Random Forest |
|---|---:|---:|---:|
| Random split | 0.003968 | 0.009588 | 0.009638 |
| Chronological split | 0.004150 | 0.004028 | 0.002801 |

The chronological test set contains 92 positive events.

## Canonical-result rule

Only results generated under the documented protocol should be treated as canonical. A later rerun with a changed Random Forest configuration is not allowed to silently replace an audited result.

The research record specifically excludes `FINAL_TEMPORAL_AUDIT_RESULTS.csv` from the canonical record because it used a different Random Forest configuration.

## Reproducibility rule

No final research claim should be made from a result that cannot be traced to a documented dataset, preprocessing pipeline, split strategy, model configuration and environment. The exact dataset provenance, hash, environment versions and committed extension artifacts remain required for full reproducibility.
