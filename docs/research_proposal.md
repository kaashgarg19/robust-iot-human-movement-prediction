# Research Proposal — Working Draft

## Working title

**Robust Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

## Background

My MSc dissertation at Birmingham City University investigated whether environmental sensor measurements from IoT devices could be used to predict human movement near the devices.

The current project starts from that work but asks a narrower research question: **how reliable is a machine-learning prediction when the data distribution changes over time or across sensing devices?**

This matters because sensor-based machine learning is often evaluated under an assumption that training and test data are similarly distributed. Recent human-activity-recognition research continues to identify device, sensor and contextual variation as important sources of distribution shift. Reviews also describe temporal heterogeneity and concept drift as recurring issues in streaming sensor data.

## Problem statement

The current IoT dataset is strongly imbalanced, with 482 positive movement events among 405,184 observations. The original MSc work addressed the imbalance by constructing a balanced modelling subset and primarily reporting accuracy.

The research extension keeps the rare-event structure intact and evaluates models under random and chronological splits, device-level hold-out, feature ablation and threshold sensitivity. This allows the project to examine reliability rather than relying on a single accuracy value.

## Working research gap

The literature establishes that sensor-based human-activity models can be affected by temporal and device-related distribution shifts. Recent work has moved toward domain generalisation, distribution-shift benchmarks and continual adaptation.

The specific gap this project will investigate is narrower:

> **Can a small, interpretable environmental-IoT movement-prediction workflow be evaluated in a way that makes temporal and device-related reliability visible, particularly when the positive event is extremely rare?**

This is a **working research gap**, not a claim that no previous study has addressed the problem.

## Aim

To develop and evaluate a reproducible framework for assessing the reliability and generalisation of machine-learning models for human-movement prediction from environmental IoT sensor data under rare-event and distribution-shift conditions.

## Objectives

1. Establish a reproducible baseline using the documented environmental IoT dataset.
2. Preserve and document the original MSc methodology as a historical baseline.
3. Compare conventional random evaluation with chronological evaluation.
4. Examine generalisation to devices that are not represented in model training.
5. Quantify how sensor-feature removal affects predictive performance.
6. Examine how decision thresholds affect precision, recall and F1-score.
7. Quantify uncertainty around important temporal results.
8. Investigate whether measurable changes in the sensor distribution are associated with changes in predictive performance.
9. Where suitable external data are available, test whether the evaluation framework transfers beyond the original dataset.
10. Produce a reproducible research record that clearly separates historical MSc evidence from new experimental findings.

## Research questions

### Primary question

How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?

### Secondary questions

- How does chronological evaluation differ from randomly mixed evaluation?
- How well do models generalise to unseen devices?
- Which sensor variables contribute most to predictive performance?
- How sensitive are precision and recall to decision-threshold selection?
- How does extreme class imbalance affect the interpretation of model performance?
- Can distribution-shift indicators help explain changes in predictive performance?

## Methodology

### Dataset

The current research record uses the Environmental Sensor Telemetry Data dataset published by Gary A. Stafford. The documented working dataset contains 405,184 observations, 9 columns, 3 devices and 482 positive movement events over approximately eight days.

### Baseline models

The current canonical comparison contains:

- Logistic Regression
- Random Forest
- Histogram Gradient Boosting

The original MSc models are preserved separately for historical comparison.

### Evaluation

The current protocol includes:

- stratified random 60/20/20 train/validation/test evaluation
- chronological 60/20/20 evaluation
- device-level hold-out where supported by the three-device structure
- feature ablation
- threshold sensitivity
- precision-recall analysis
- uncertainty analysis

Average precision, precision, recall and F1 are emphasised because the positive event is extremely rare.

### Proposed next-stage experiments

The next research stage should focus on:

1. **Distribution-shift measurement** — quantify changes in sensor distributions across time and devices.
2. **Time-aware validation** — test whether conclusions remain stable under different temporal gaps.
3. **Calibration analysis** — examine whether predicted probabilities remain reliable under temporal change.
4. **External validation** — use a second appropriate dataset if its target and sensor context are sufficiently comparable.
5. **Sensitivity analysis** — assess whether conclusions depend strongly on model configuration or threshold rule.
6. **Reproducible reporting** — attach dataset hash, code version, split, model configuration and metric definitions to each canonical result.

## Expected contribution

The intended contribution is methodological rather than a claim of a universally superior classifier.

The project aims to provide:

- a transparent bridge from an MSc IoT prediction study to a more rigorous research evaluation;
- an evaluation workflow that exposes the effect of temporal and device distribution shift;
- rare-event-aware reporting that avoids relying on accuracy alone;
- reproducible experiment records that make limitations visible;
- evidence about when a model's apparent performance may not transfer across time or devices.

## Limitations

The current dataset is small in domain coverage: approximately eight days and three devices. The positive event is also very rare.

The research therefore should not claim deployment readiness or broad generalisation from the current dataset alone. External validation and additional datasets would materially strengthen the evidence.

## Research ethics and data handling

The current project uses a public third-party dataset rather than newly collected personal data. No personal identifiers are intentionally redistributed in the repository. The raw third-party dataset is not stored in the GitHub repository.

## Current status

Completed foundation:

- MSc research reconstruction
- dataset documentation and codebook
- baseline models
- random evaluation
- chronological evaluation
- device-level evaluation record
- feature ablation record
- threshold analysis record
- reproducibility documentation
- public research repository and portfolio website

Next research stage:

- focused literature review
- formalise the research gap
- strengthen distribution-shift analysis
- validate findings externally where feasible
- prepare a paper-style research manuscript
- prepare supervisor-specific proposal versions

## Key literature to build from

- Chen, Odema & Al Faruque (2025), *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*, IEEE Internet of Things Journal.
- Adaimi & Thomaz (2026), *Assessing Distribution Shift in Human Activity Recognition for Domain Generalization*.
- Øren et al. (2025), *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*, IEEE Access.
- Review: *Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity*.
