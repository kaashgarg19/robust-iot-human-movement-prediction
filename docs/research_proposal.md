# Research Proposal

## Working title

**Robust Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

## 1. Background

My MSc dissertation at Birmingham City University investigated whether environmental sensor measurements from IoT devices could be used to predict human movement near IoT devices.

I have kept that original work separate and unchanged. The current project starts from the MSc problem, but asks a more specific question about how reliable the prediction remains when the data changes.

This question is relevant to sensor-based human activity recognition (HAR), where differences in users, devices, sensor placement, sampling conditions and time can change the data seen by a model. A 2024 review of sensor-based HAR discusses data heterogeneity, temporal distribution changes and concept drift as recurring issues in streaming sensor data. Recent work has also explicitly studied HAR under distribution shifts and domain generalisation. These studies suggest that evaluation conditions matter, rather than assuming that randomly mixed observations always represent future use. [1–3]

## 2. Problem statement

The working dataset contains **405,184 observations**, **3 devices** and **482 positive movement events**, giving a positive prevalence of approximately **0.119%**.

The original MSc workflow addressed the imbalance by creating a balanced modelling subset and primarily reporting accuracy. That approach documents the historical MSc experiment, but it changes the original class distribution and does not directly answer the current question of how a model behaves on the rare event in the full dataset.

The research extension therefore keeps the rare-event distribution and compares random evaluation with chronological and device-level evaluation. It also examines feature ablation and decision thresholds.

For highly imbalanced classification, precision-recall analysis can reveal behaviour that accuracy or ROC-based summaries may obscure. Saito and Rehmsmeier's analysis is one established reference for this point. [4]

## 3. Research motivation

The motivation is practical and methodological.

If a model is trained on sensor data collected during one period or from a particular device, its performance may change when the data comes from a later period or another device. A useful research evaluation should make that change visible.

The aim is therefore not simply to find the model with the highest score on one split. It is to understand how stable the prediction is under different data conditions and how much confidence should be placed in the result.

## 4. Working research gap

There is already substantial research on:

- sensor-based human activity recognition;
- device and context variation;
- domain generalisation;
- distribution shift;
- concept drift;
- adaptation to changing sensor streams.

I therefore do **not** claim that distribution shift in HAR is a new problem.

The narrower gap I want to investigate is:

> **How can an interpretable environmental-IoT human-movement prediction workflow be evaluated so that the combined effects of rare-event imbalance, temporal separation and device separation on reliability are made visible and reproducible?**

This is a working research gap that should be refined through a fuller literature review and further experiments.

## 5. Aim

To develop and evaluate a reproducible framework for studying the reliability of machine-learning models for human-movement prediction from environmental IoT sensor data under rare-event and distribution-shift conditions.

## 6. Objectives

1. Establish a reproducible baseline using the documented environmental IoT dataset.
2. Preserve and document the original MSc methodology as a historical reference.
3. Compare conventional random evaluation with chronological evaluation.
4. Examine generalisation to devices not represented in training.
5. Measure how removing sensor variables changes predictive performance.
6. Examine how decision thresholds affect precision, recall and F1.
7. Quantify uncertainty around important temporal results.
8. Measure changes in sensor distributions across time and devices.
9. Examine whether calibration changes when the data distribution changes.
10. Where a sufficiently comparable external dataset is available, test whether the evaluation framework transfers beyond the original dataset.
11. Produce a reproducible record that clearly separates historical MSc evidence from new research evidence.

## 7. Research questions

### Primary question

**How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?**

### Secondary questions

1. How does chronological evaluation differ from randomly mixed evaluation?
2. How well do models generalise to devices not represented in training?
3. Which environmental sensor variables contribute most to predictive performance?
4. How sensitive are precision and recall to decision-threshold selection?
5. How does extreme class imbalance affect interpretation of model performance?
6. Can measurable changes in the sensor distribution help explain changes in predictive performance?
7. Does probability calibration remain stable when the data distribution changes?

## 8. Methodology

### 8.1 Dataset

The primary dataset is the Environmental Sensor Telemetry Data dataset published by Gary A. Stafford. The documented working dataset contains 405,184 observations, 9 columns, 3 devices and 482 positive movement events over approximately eight days.

The raw third-party CSV is not redistributed in the repository. Dataset provenance, structure and access information are documented separately.

### 8.2 Historical MSc reference

The original MSc implementation is preserved in a separate repository. The current research repository contains a documented historical reconstruction so that the research trajectory can be understood without modifying the original `Aman.py`.

The historical workflow is treated as a baseline for provenance, not as the preferred evaluation protocol for the new research question.

### 8.3 Current models

The canonical research comparison currently contains:

- Logistic Regression
- Random Forest
- Histogram Gradient Boosting

The models are implemented through reusable pipelines and use the documented preprocessing and random-state rules.

### 8.4 Evaluation design

The current protocol includes:

**Random evaluation**  
A stratified 60/20/20 train/validation/test split provides a conventional reference point.

**Chronological evaluation**  
Observations are ordered by timestamp and split into earlier training, intermediate validation and later test periods.

**Device-level evaluation**  
Where supported by the three-device dataset, selected devices are held out to examine cross-device transfer. Because only three devices are available, these results are preliminary.

**Feature ablation**  
Sensor variables or groups are removed systematically to examine changes in predictive performance.

**Threshold sensitivity**  
Decision thresholds are varied to show the precision/recall trade-off rather than assuming that 0.5 is automatically appropriate.

**Uncertainty and diagnostics**  
The project includes temporal recall uncertainty and precision-recall/calibration diagnostics where supported by the audited record.

### 8.5 Metrics

Because the positive event is extremely rare, the primary reporting emphasis is on:

- average precision;
- precision;
- recall;
- F1;
- balanced accuracy;
- false positives;
- threshold-dependent behaviour.

Accuracy is retained as historical context rather than treated as the main evidence for the current research question.

## 9. Current pilot evidence

The audited research record currently preserves average-precision values for the random and chronological evaluations.

| Evaluation | Logistic Regression | HistGradientBoosting | Random Forest |
|---|---:|---:|---:|
| Random split | 0.003968 | 0.009588 | 0.009638 |
| Chronological split | 0.004150 | 0.004028 | 0.002801 |

The chronological test partition contains 92 positive events.

These values are **dataset-specific pilot results**. They should not be interpreted as universal model rankings, deployment evidence or proof of generalisation.

## 10. Next-stage experiments

### 10.1 Distribution-shift measurement

Measure how sensor distributions differ between training and later periods and between devices. Candidate measures should be selected after reviewing established shift-detection approaches.

### 10.2 Temporal-gap sensitivity

Repeat the temporal evaluation with different separation windows to determine whether conclusions depend on one particular split.

### 10.3 Calibration

Compare predicted probabilities with observed outcomes and examine whether calibration changes across temporal or device conditions.

### 10.4 External validation

Identify a second dataset with sufficiently comparable sensor variables and target definition. If the datasets are not genuinely comparable, document that limitation rather than forcing a direct comparison.

### 10.5 Sensitivity analysis

Test whether the main conclusions remain stable under reasonable changes to model configuration, threshold rule and feature handling.

## 11. Expected contribution

The intended contribution is methodological and empirical rather than a claim of a new classifier.

The project aims to provide:

- a transparent bridge from an MSc IoT prediction study to a more rigorous research evaluation;
- an evaluation workflow that makes temporal and device-related reliability visible;
- rare-event-aware reporting;
- reproducible experiment records;
- evidence about the conditions under which apparent predictive performance changes.

The final contribution will depend on the results of the next-stage experiments and the completed literature review.

## 12. Limitations

The current evidence has several important limitations:

- approximately eight days of observations;
- only three devices;
- only 482 positive events;
- one primary dataset so far;
- preliminary device-level evidence;
- no claim of deployment readiness.

These limitations mean the current work should be presented as a research foundation and pilot investigation.

## 13. Ethics and data handling

The current study uses a public third-party dataset rather than newly collected personal data. No personal identifiers are intentionally redistributed in the repository. The raw third-party dataset is not stored in GitHub.

If future work introduces human-subject data or additional personal data, the appropriate ethics, consent and data-governance requirements would need to be considered separately.

## 14. Current status and proposed next stage

### Completed

- original MSc work preserved separately;
- dataset documentation and codebook;
- historical MSc reconstruction;
- baseline models;
- random evaluation;
- chronological evaluation;
- device-level evaluation record;
- feature ablation;
- threshold analysis;
- reproducibility documentation;
- public research repository.

### Next

- strengthen distribution-shift measurement;
- run temporal-gap sensitivity experiments;
- complete calibration analysis;
- investigate external validation;
- strengthen the literature review;
- write a paper-style research manuscript;
- refine the proposal with supervisor feedback.

## 15. References

**[1]** *Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity* (2024 review).  
https://pmc.ncbi.nlm.nih.gov/articles/PMC11679906/

**[2]** Chen, L., Odema, M., & Al Faruque, M. (2025). *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*. IEEE Internet of Things Journal. DOI: 10.1109/JIOT.2025.3551263.  
https://its.uci.edu/research_products/published-journal-article-discovhar-contrastive-attention-for-human-activity-recognition-under-distribution-shifts/

**[3]** Adaimi, R., & Thomaz, E. (2026). *Assessing Distribution Shift in Human Activity Recognition for Domain Generalization*. arXiv preprint. DOI: 10.48550/arXiv.2606.24781.  
https://arxiv.org/abs/2606.24781

**[4]** Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. DOI: 10.1371/journal.pone.0118432.  
https://doi.org/10.1371/journal.pone.0118432

**[5]** Øren, A. E. et al. (2025). *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*. IEEE Access. DOI: 10.1109/ACCESS.2025.3622973.  
https://doi.org/10.1109/ACCESS.2025.3622973

## 16. Proposal status

This document is now a **research proposal draft for supervisor discussion**. It should be refined further after supervisor feedback, particularly around the exact distribution-shift definition, external validation strategy and final contribution.