# Reproducibility Guide

## Purpose

This guide explains how to reproduce the research workflow without redistributing the third-party Kaggle dataset.

## 1. Obtain the dataset

Place the authorised copy of the dataset at:

```text
data/raw/iotdata.csv
```

The dataset source, publisher and licence are documented in `docs/dataset_documentation.md`.

For an exact rerun, the local dataset hash and software versions should also be recorded alongside the experiment results.

## 2. Create the environment

Use Python 3.10 or a compatible newer version supported by the dependency ranges in `requirements.txt`.

From this project directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Validate the dataset first

Run notebook `01_data_validation.ipynb` and confirm:

- 405,184 rows
- 9 columns
- 3 devices
- 482 positive movement events
- approximately 0.119% positive prevalence
- Unix-second timestamps
- 13 duplicated timestamp values

If these checks do not match, stop and review the dataset version before interpreting any result.

## 4. Historical MSc reconstruction

Run `02_msc_original_analysis.ipynb` to document the MSc foundation and compare the verified historical accuracy values.

`src/msc_original.py` contains a separated historical implementation. It is provided for provenance and should not be confused with the current research protocol.

## 5. Current research evaluation

The current research notebooks use the full rare-event dataset and the model configurations documented in `src/models.py`.

- `03_baseline_models.ipynb` — random stratified 60/20/20 evaluation.
- `04_temporal_evaluation.ipynb` — chronological 60/20/20 evaluation.
- `05_robustness_analysis.ipynb` — robustness analysis and result references.

Threshold selection uses validation data only. The final test set remains untouched until evaluation.

## 6. Research metrics

The documented research record currently preserves these average-precision values:

| Split | Logistic Regression | HistGradientBoosting | Random Forest |
|---|---:|---:|---:|
| Random | 0.003968 | 0.009588 | 0.009638 |
| Chronological | 0.004150 | 0.004028 | 0.002801 |

The chronological test partition contains 92 positive events.

These values are dataset-specific pilot evidence and are not universal performance claims.

## 7. Recording an experiment

For each reproducible result, record:

1. Dataset source and version
2. Dataset SHA-256 hash
3. Python version
4. Package versions
5. Experiment ID
6. Git commit
7. Split strategy
8. Model configuration
9. Evaluation metrics
10. Main result and limitations

## 8. Interpretation rules

Accuracy is not used as the main performance claim because the positive event rate is approximately 0.119%. Average precision, precision, recall and F1 are prioritised, together with threshold behaviour where relevant.

Feature importance and ablation describe predictive model behaviour; they do not establish causality.

Temporal and device-level findings are preliminary because the current dataset covers only about eight days and three devices.
