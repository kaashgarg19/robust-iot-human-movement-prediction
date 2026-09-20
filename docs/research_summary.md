# Research Summary — Aman Gupta

## Working title
**Robust Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

## 1. Where the research started

This research started from my MSc dissertation at Birmingham City University:

**Intelligent System to Predict Human Movement near IoT Devices**

The original MSc project asked whether environmental sensor measurements collected by IoT devices could be used to predict whether human movement is present near the device. I prepared the data, explored the dataset, compared classification models and evaluated their performance.

The original implementation is preserved separately in the [original MSc repository](https://github.com/kaashgarg19/iot-human-movement-prediction-msc). The original Aman.py file has not been rewritten as part of the later research extension.

## 2. Why I continued the work

While revisiting the MSc project, I became interested in a different question: whether model performance is reliable when the data changes.

A random evaluation does not necessarily tell us how a model behaves when future observations look different from the training data, or when observations come from another sensing device.

The dataset also contains a very rare positive movement event: **482 positive observations among 405,184 observations**, approximately **0.119% positive prevalence**.

This motivated a move beyond a single accuracy value toward evaluation under more realistic conditions.

## 3. Research question

> **How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?**

Supporting questions cover random versus chronological evaluation, unseen-device transfer, sensor-feature contribution, decision thresholds, and interpretation under extreme class imbalance.

## 4. What changed from the MSc work

| MSc foundation | Research extension |
|---|---|
| Balanced modelling subset | Full rare-event distribution is retained |
| Mainly accuracy-based comparison | Precision-recall and rare-event metrics are emphasised |
| Random modelling split | Random and chronological evaluation |
| Historical model comparison | Reproducible baseline model pipeline |
| Original workflow | Additional device-level evaluation |
| Original feature set | Feature-ablation analysis |
| Fixed classification decision | Threshold-sensitivity analysis |
| Dissertation-level analysis | Experiment records and reproducibility documentation |

## 5. Dataset

- 405,184 observations
- 9 columns
- 3 IoT devices
- 482 positive movement events
- approximately 0.119% positive prevalence
- approximately 8 days of observations

The raw third-party CSV is not redistributed in GitHub. Dataset provenance, structure and access information are documented separately.

## 6. What I have done so far

1. Dataset validation and quality checks
2. Historical reconstruction of the MSc workflow
3. Baseline Logistic Regression, Random Forest and HistGradientBoosting models
4. Stratified random evaluation
5. Chronological hold-out evaluation
6. Preliminary unseen-device evaluation
7. Feature-ablation analysis
8. Decision-threshold sensitivity analysis
9. Precision-recall diagnostics
10. Uncertainty analysis where supported by the audited results
11. Reproducibility documentation
12. Research proposal working draft

The notebooks follow: 01_data_validation → 02_msc_original_analysis → 03_baseline_models → 04_temporal_evaluation → 05_robustness_analysis.

## 7. What the current evidence means

The current results are **dataset-specific pilot evidence**. The dataset covers only a short period and three devices. I therefore do not present the results as proof of deployment readiness or universal generalisation.

The purpose of the extension is to make limitations visible and test whether apparently strong performance changes under more realistic evaluation.

## 8. Next stage

- Measure distribution change across time and devices.
- Strengthen temporal evaluation with multiple hold-out configurations.
- Examine probability calibration under distribution change.
- Seek suitable external validation data.
- Run sensitivity analyses across reasonable model configurations.
- Build a paper-style manuscript and strengthen the literature review.

## 9. Intended contribution

The intended contribution is methodological rather than a claim that one classifier is universally better. The project aims to show how environmental-IoT movement prediction can be evaluated more carefully when the target event is extremely rare, observations change over time, devices differ, thresholds matter, and reproducibility is important.

## 10. Current limitations

The current evidence is constrained by approximately eight days of observations, three devices, very few positive events relative to the total dataset, and one primary dataset so far.

## 11. Research status

**Completed:** MSc reconstruction, dataset documentation, baseline evaluation, temporal evaluation, device-level evaluation record, feature ablation, threshold analysis and reproducibility structure.

**Next:** strengthen distribution-shift measurement, calibration, external validation where feasible, literature review and a paper-style manuscript.

## Research links

- [Current research repository](https://github.com/kaashgarg19/robust-iot-human-movement-prediction)
- [Original MSc repository](https://github.com/kaashgarg19/iot-human-movement-prediction-msc)
- [Research proposal](research_proposal.md)
- [Research questions](research_questions.md)
- [Reproducibility guide](reproducibility.md)
- [Portfolio](https://kaashgarg19.github.io/kaashgarg19/)
- [ORCID](https://orcid.org/0009-0007-4112-9993)