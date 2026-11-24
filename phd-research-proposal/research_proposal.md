# PhD Research Proposal

## Working title

**Reliable Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

**Researcher:** Aman Gupta  
**Document status:** PhD proposal draft for supervisor discussion and university applications

## 1. Research background

My MSc dissertation at Birmingham City University investigated whether environmental sensor readings from Internet of Things (IoT) devices could be used to predict human movement near those devices. The project provided a practical starting point in sensor-data preparation, exploratory analysis and machine-learning classification.

When I revisited the work, I became interested in a broader reliability question: what happens when a model is used in conditions that differ from the data on which it was trained? In an IoT setting, this may happen when the system receives observations from a later period, when a sensing device is replaced or relocated, or when environmental conditions change.

A model may produce encouraging results when training and test observations are randomly mixed, yet behave differently when it is evaluated on later observations or a device not represented during training. This proposal develops that question from my MSc research and sets out a doctoral investigation into reliable evaluation under temporal and device-related distribution change.

The proposal does not assume that a new classifier is necessarily required. It aims to establish when existing models can be trusted, how their limitations can be identified, and which evaluation or adaptation approaches are appropriate.

## 2. Research problem

The documented primary dataset contains 405,184 sensor observations, nine columns, three devices and 482 positive movement events (approximately 0.119% of observations). The positive class is therefore very rare. This makes evaluation difficult: a model can achieve apparently strong overall accuracy while failing to identify the movement events that matter.

There are also limits to what can be learned from a random split. Random evaluation is useful as a baseline, but it may not represent deployment conditions in which a model is asked to predict later observations or data from a different device.

The doctoral research will investigate three connected issues:

- **Temporal change:** whether predictive performance changes when a model is tested on observations collected later than its training data.
- **Device change:** whether a model transfers to a sensing device that was not represented during training.
- **Rare-event reliability:** how class imbalance, decision thresholds, uncertainty and probability calibration affect the interpretation of predictions.

The research will also examine whether measurable changes in sensor-data distributions help explain changes in model performance.

## 3. Aim

To develop and evaluate a reproducible approach for assessing and improving the reliability of machine-learning models that predict human movement from environmental IoT sensor data under temporal change, device variation and severe class imbalance.

## 4. Research objectives

1. Establish a clear and reproducible baseline using the documented environmental-IoT dataset.
2. Preserve the MSc study as the historical foundation and distinguish it from new doctoral work.
3. Compare random evaluation with time-ordered evaluation and examine the effect of different temporal separation periods.
4. Investigate model performance when one sensing device is held out from training.
5. Measure changes in sensor distributions across time and devices and assess how those changes relate to predictive performance.
6. Examine the contribution of individual sensor variables and groups of variables.
7. Evaluate threshold selection, precision-recall trade-offs and false-positive burden under severe class imbalance.
8. Assess uncertainty and probability calibration under temporal and device-related changes.
9. Investigate suitable approaches for monitoring or adapting to changing data, where supported by the evidence.
10. Test the evaluation approach on an additional comparable dataset if one with sufficiently compatible sensors and target definitions can be identified.
11. Produce a transparent, reproducible research record and communicate findings with clear limitations.

## 5. Research questions

### Primary research question

**How can the reliability of machine-learning models for human-movement prediction from environmental IoT sensors be evaluated and improved when data distributions change over time and across sensing devices?**

### Supporting questions

1. How do results from random evaluation differ from results obtained using chronological evaluation?
2. How does the length of the temporal gap between training and testing data affect predictive reliability?
3. To what extent can models generalise to a device that was not represented during training?
4. Which sensor variables or groups of variables contribute to prediction, and do their contributions change across evaluation conditions?
5. How do decision thresholds affect recall, precision and false-positive rates when movement events are rare?
6. Which measures of distribution change are most informative about changes in predictive performance?
7. Does probability calibration remain reliable under temporal and device-related distribution change?
8. Under what conditions, if any, can monitoring or adaptation improve reliability without creating unacceptable false alarms?

## 6. Rationale and proposed research gap

Research in human activity recognition, sensor-based machine learning and domain adaptation already addresses heterogeneous data and changing distributions. The proposed work will not claim that distribution shift itself is an unexplored problem.

The focused opportunity is to investigate how temporal separation, device separation and rare-event imbalance interact in environmental-IoT human-movement prediction, and how these factors should be reflected in a transparent evaluation process. The study will connect measurable changes in sensor data with changes in model behaviour, rather than reporting model scores in isolation.

This is a working research gap. It will be refined through a systematic literature review and discussion with the prospective supervisory team.

## 7. Research design and methodology

The project will use an empirical, quantitative research design based on documented sensor datasets and reproducible machine-learning experiments.

### 7.1 Data and initial study

The initial study will use the Environmental Sensor Telemetry Data dataset published by Gary A. Stafford. The documented working version contains 405,184 observations, nine columns, three devices and 482 positive movement events over approximately eight days.

The raw third-party CSV is not redistributed in the repository. Dataset provenance, structure and access information are documented separately. The short observation period and limited number of devices will be treated as important constraints. The study will not claim that three devices are sufficient to establish broad device generalisation.

### 7.2 Existing research foundation

The current repository documents dataset validation, reconstruction of the historical MSc workflow, baseline Logistic Regression, Random Forest and Histogram Gradient Boosting models, random evaluation, chronological hold-out evaluation and reproducibility procedures.

The currently recorded average-precision values are:

| Evaluation | Logistic Regression | HistGradientBoosting | Random Forest |
|---|---:|---:|---:|
| Random split | 0.003968 | 0.009588 | 0.009638 |
| Chronological split | 0.004150 | 0.004028 | 0.002801 |

These are pilot results from one small dataset. They motivate further investigation but do not establish general performance, deployment readiness or the superiority of a particular classifier. The chronological test partition contains 92 positive events.

### 7.3 Planned doctoral experiments

The following work is proposed for the PhD and has not been presented as completed research. Experiment identifiers E08–E24 are reserved for this doctoral stage. The detailed order and final protocols will be agreed with supervisors after the literature review and assessment of data availability.

The planned work is expected to cover:

- **Temporal robustness:** evaluate different chronological windows and temporal gaps.
- **Unseen-device evaluation:** hold out devices from model training and test transfer to those devices.
- **Feature contribution:** remove or group sensor variables to understand how their contribution changes across conditions.
- **Threshold analysis:** assess the effect of decision thresholds on recall, precision and false-positive burden.
- **Uncertainty estimation:** quantify uncertainty in key metrics, particularly where positive events are few.
- **Precision-recall analysis:** examine model behaviour across operating thresholds.
- **Calibration:** compare predicted probabilities with observed event frequencies.
- **Distribution monitoring:** measure changes in sensor features and investigate their relationship with changes in predictive performance.
- **Adaptation and mitigation:** assess suitable monitoring or adaptation methods if the evidence shows that they are necessary and feasible.
- **External validation:** evaluate transfer to another dataset only if sensor variables, event definitions and collection conditions are sufficiently comparable.
- **Sensitivity and reproducibility:** test whether conclusions depend on split choices, model settings, preprocessing or threshold rules.

The experiment plan will be refined rather than treating every item as mandatory regardless of feasibility. Any change to the plan will be documented.

### 7.4 Models and comparison

The initial comparison will retain interpretable baseline methods: Logistic Regression, Random Forest and Histogram Gradient Boosting. Additional models or adaptation methods may be considered where justified by the literature and research findings.

The aim is not to increase model complexity without reason. Comparisons should help identify whether observed differences arise from the evaluation condition, data characteristics, model behaviour or adaptation method.

### 7.5 Evaluation measures

Given the rarity of positive movement events, the main evaluation will consider:

- average precision and precision-recall curves;
- precision, recall and F1-score;
- false-positive counts or rates;
- balanced accuracy where appropriate;
- confidence intervals or other uncertainty estimates;
- probability calibration and Brier score where suitable;
- distribution-change measures selected and justified through the literature.

Accuracy will not be used as the sole or primary indicator of success. Thresholds will be selected using training/validation data only, not by optimising against the final test set.

### 7.6 Reproducibility and validation

Each experiment will record the dataset version and hash where possible, software environment, code version, split strategy, preprocessing, model configuration, threshold-selection procedure, metrics and limitations. Test data will remain separate from model and threshold selection.

Where an external dataset is not sufficiently comparable, the study will report that limitation rather than forcing a misleading comparison.

## 8. Expected contribution

The intended contribution is a better-supported understanding of when environmental-IoT human-movement predictions remain reliable and when they become less trustworthy as time, devices or data distributions change.

Potential outputs include:

- a reproducible evaluation framework for temporal and device-related change;
- empirical evidence about the interaction between rare-event imbalance and distribution change;
- practical guidance on threshold selection, uncertainty and calibration;
- an assessment of monitoring or adaptation methods where justified;
- documented experiments and, subject to results, research publications.

The final contribution will be determined by the evidence. The proposal does not promise a new algorithm or claim that an adaptation method will necessarily improve performance.

## 9. Scope and limitations

The initial dataset is limited to approximately eight days of observations, three devices and 482 positive events. It represents one primary data source and does not include a deployment study. Device-level results from this dataset will therefore be treated as preliminary.

The doctoral project will seek additional data or comparable datasets where possible. If suitable data cannot be obtained, the scope and claims will be adjusted transparently. Generalisation to other environments will not be claimed without appropriate validation.

## 10. Ethics and data management

The initial study uses a publicly available third-party dataset. The raw dataset is not redistributed in the repository. Any future collection or use of personal or human-subject data will be subject to the host institution's ethics review, consent requirements, data-protection rules and approved data-management procedures before the work begins.

## 11. Indicative doctoral work plan

| Period | Main activities |
|---|---|
| Year 1 | Systematic literature review; refine research questions; confirm data access and ethics requirements; establish reproducible baselines; finalise evaluation protocols. |
| Year 2 | Conduct temporal and device experiments; investigate rare-event evaluation, uncertainty and calibration; assess distribution monitoring; present interim findings. |
| Year 3 | Evaluate suitable mitigation or adaptation methods; conduct external validation if feasible; consolidate findings; write and submit the thesis and research outputs. |

The exact schedule will be adapted to the university's doctoral structure, data access and supervisory advice.

## 12. Researcher preparation

The project builds on my MSc in Advanced Computer Science (Distinction) from Birmingham City University and my dissertation on predicting human movement near IoT devices. I have continued to document and extend the research through a public repository containing the research background, dataset documentation, methodology, baseline evaluation and reproducibility material.

The repository provides supporting evidence of the work completed to date. The doctoral experiments described in this proposal remain planned work.

## 13. Selected references

1. *Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity* (2024 review). https://pmc.ncbi.nlm.nih.gov/articles/PMC11679906/
2. Chen, L., Odema, M., & Al Faruque, M. (2025). *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*. IEEE Internet of Things Journal. DOI: 10.1109/JIOT.2025.3551263.
3. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432. DOI: 10.1371/journal.pone.0118432.
4. Øren, A. E. et al. (2025). *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*. IEEE Access. DOI: 10.1109/ACCESS.2025.3622973.

The literature review will be expanded and updated during proposal development. References and bibliographic details should be checked against the final university submission requirements.

## 14. Proposal status and adaptation

This document is a general PhD research proposal for discussion with prospective supervisors and for adapting to relevant doctoral opportunities. It is not tied to one country or university.

Before each application, the proposal should be tailored to the supervisor's research, available datasets and facilities, the advertised project's requirements, and the university's requested length and format. The research question and core research direction should remain consistent, while the specific methods and scope may be refined with supervisor input.
