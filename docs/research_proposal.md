# Research Proposal

## Working title

**Robust Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

## 1. Where this research starts

My MSc dissertation at Birmingham City University looked at a fairly direct question: could environmental sensor readings from IoT devices be used to predict human movement?

That project gave me the starting point for the research I want to pursue now. While revisiting the work, I became more interested in a question that sits behind the prediction itself: **what happens to a model when the data it sees is no longer quite like the data it learned from?**

For an IoT system, that can happen naturally. A model may be trained on observations from one period and later receive data from another period. It may also be used with a different sensing device. If performance changes under those conditions, a conventional random train/test split may not make that change obvious.

This proposal develops that question from my MSc work. The aim is not to claim that distribution shift is a new problem. It is to investigate it carefully in this particular environmental-IoT human-movement setting and to build an evaluation process that makes the changes in reliability visible.

## 2. Problem I want to investigate

The working dataset contains **405,184 observations**, **3 devices** and **482 positive movement events**, so positive events make up only about **0.119%** of the observations.

That imbalance matters. A model can appear to perform well on a conventional metric while still missing much of the event of interest. It also matters how the data is divided. Randomly mixing observations can produce a useful baseline, but it does not necessarily represent the situation in which a model is asked to predict later observations or data from another device.

My research therefore focuses on three connected questions:

- How different is the picture produced by random evaluation compared with chronological evaluation?
- What happens when a device that was not used for training becomes the test condition?
- Can changes in the sensor data itself help explain changes in predictive performance?

I also want to understand how threshold choice and probability calibration affect the interpretation of rare movement events.

## 3. Why I think the question is worth pursuing

Human-activity-recognition and sensor-based machine-learning research already contains substantial work on heterogeneous data, domain variation, distribution shift and adaptation. Recent work continues to examine how recognition systems behave when the distribution changes.

My intention is therefore not to present “distribution shift in IoT” as an unexplored field. The more focused question is whether a transparent environmental-IoT movement-prediction workflow can show, in a reproducible way, **which evaluation conditions change the apparent reliability of the prediction and why**.

That distinction is important to me because the useful result may not be a new classifier. It may instead be a clearer understanding of when a model's reported performance can and cannot be trusted.

## 4. Working research gap

The gap is currently framed as:

> **How can an interpretable environmental-IoT human-movement prediction workflow be evaluated so that the effects of rare-event imbalance, temporal separation and device separation on predictive reliability are made visible and reproducible?**

This is a working gap rather than a final claim. I would refine it through a fuller literature review and through discussion with a prospective supervisor.

## 5. Aim

To develop and evaluate a reproducible approach for studying the reliability of machine-learning models that predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices.

## 6. Objectives

1. Establish a reproducible baseline using the documented environmental-IoT dataset.
2. Preserve the original MSc methodology as a historical reference rather than mixing it with new evidence.
3. Compare randomly mixed evaluation with chronological evaluation.
4. Examine how models perform when a device is not represented in training.
5. Investigate the effect of removing individual sensor variables or groups of variables.
6. Examine how decision thresholds change precision, recall and F1.
7. Quantify uncertainty around important temporal results.
8. Measure changes in sensor distributions across time and devices.
9. Examine whether probability calibration changes when the data distribution changes.
10. Where a genuinely comparable external dataset can be identified, test whether the evaluation approach transfers beyond the original dataset.
11. Keep a reproducible research record that clearly distinguishes completed MSc evidence, new experiments and proposed future work.

## 7. Research questions

### Primary question

**How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?**

### Secondary questions

1. How does chronological evaluation differ from randomly mixed evaluation?
2. How well do models generalise to devices that were not represented during training?
3. Which environmental sensor variables contribute most to predictive performance?
4. How sensitive are precision and recall to the decision threshold?
5. How does extreme class imbalance affect the interpretation of model performance?
6. Can measurable changes in the sensor distribution help explain changes in predictive performance?
7. Does probability calibration remain stable when the data distribution changes?

## 8. Methodology

### 8.1 Dataset

The primary dataset is the **Environmental Sensor Telemetry Data** dataset published by Gary A. Stafford. The documented working dataset contains 405,184 observations, 9 columns, 3 devices and 482 positive movement events over approximately eight days.

The raw third-party CSV is not redistributed in this repository. Dataset provenance, structure and access information are documented separately.

The small number of devices and short observation period are treated as limitations, not hidden from the research record.

### 8.2 What I have already done

The original MSc implementation is preserved in a separate repository.

The current research extension has so far included:

- dataset validation and data-quality checks;
- reconstruction of the historical MSc workflow;
- baseline Logistic Regression, Random Forest and HistGradientBoosting models;
- stratified random evaluation;
- chronological hold-out evaluation;
- preliminary device-level evaluation;
- feature-ablation analysis;
- decision-threshold sensitivity analysis;
- precision-recall and calibration-related diagnostics where supported by the audited record;
- reproducibility documentation.

Keeping these stages separate is deliberate. The later temporal, device-shift, imbalance and threshold analyses should not be presented as if they were part of the original 2021 dissertation.

### 8.3 Evaluation design

**Random evaluation**

A stratified 60/20/20 train/validation/test split provides a conventional reference point.

**Chronological evaluation**

Observations are ordered by timestamp and divided into earlier training, intermediate validation and later test periods. This gives a closer approximation to the question of how a model behaves on later observations.

**Device-level evaluation**

Where the three-device dataset allows it, selected devices are held out from training. Because only three devices are available, these experiments are preliminary and should not be treated as broad evidence of cross-device generalisation.

**Feature ablation**

Sensor variables or groups of variables are removed systematically to see whether the main conclusions depend heavily on a particular measurement.

**Threshold sensitivity**

Decision thresholds are varied to show how precision and recall move against one another rather than treating 0.5 as automatically meaningful.

**Uncertainty and diagnostics**

Temporal uncertainty, precision-recall behaviour and calibration will be examined where the experiment design supports reliable estimates.

### 8.4 Models

The current comparison uses:

- Logistic Regression;
- Random Forest;
- Histogram Gradient Boosting.

The purpose at this stage is not to search for the most complicated model. A smaller set of understandable baselines makes it easier to study how evaluation conditions affect the conclusions.

### 8.5 Metrics

Because positive movement events are extremely rare, the main reporting emphasis will be on:

- average precision;
- precision;
- recall;
- F1;
- balanced accuracy;
- false positives;
- threshold-dependent behaviour;
- probability calibration where appropriate.

Accuracy will remain available for historical comparison, but it will not be treated as the main evidence for the current research question.

## 9. Current pilot evidence

The audited research record currently preserves the following average-precision values:

| Evaluation | Logistic Regression | HistGradientBoosting | Random Forest |
|---|---:|---:|---:|
| Random split | 0.003968 | 0.009588 | 0.009638 |
| Chronological split | 0.004150 | 0.004028 | 0.002801 |

The chronological test partition contains 92 positive events.

These are **pilot results from one small dataset**. They are useful for motivating further investigation, but they are not being presented as universal model-performance claims, deployment evidence or proof that one classifier is generally better than another.

The contrast between the random and chronological results is one reason I want to continue the investigation.

## 10. Next experiments

### 10.1 Measure the distribution changes

I will examine how the sensor distributions differ between earlier and later observations and between devices. The specific statistical measures will be selected after reviewing established approaches to distribution-shift detection.

### 10.2 Test different temporal gaps

Rather than relying on one chronological split, I will vary the separation between training and test periods to see whether the conclusions remain similar.

### 10.3 Examine calibration

I will compare predicted probabilities with observed outcomes and investigate whether calibration changes when the model moves into a different temporal or device condition.

### 10.4 Investigate external validation

I will look for a second dataset with genuinely comparable sensors and target definitions. If the datasets are not comparable enough for a meaningful experiment, that limitation will be reported rather than forcing a comparison.

### 10.5 Sensitivity analysis

I will test whether the main conclusions remain reasonably stable when model configuration, threshold rules or feature handling are changed.

## 11. Expected contribution

At this stage, I am deliberately not promising a new algorithm.

The contribution I want to work toward is a clearer and reproducible way of evaluating environmental-IoT movement prediction under conditions that are closer to real changes in the data.

Depending on what the experiments show, this could include:

- a transparent bridge from the original MSc study to a more rigorous evaluation;
- evidence showing how temporal and device changes affect reported reliability;
- rare-event-aware reporting;
- reproducible experiment records;
- analysis connecting measurable changes in the sensor data with changes in model behaviour.

The final contribution should emerge from the experiments rather than being decided in advance.

## 12. Limitations

The current evidence has important limitations:

- approximately eight days of observations;
- only three devices;
- 482 positive movement events;
- one primary dataset so far;
- preliminary device-level evidence;
- no deployment study;
- no claim that the current results generalise to other IoT environments.

These constraints are part of the reason I see the current work as a research foundation and pilot investigation rather than a finished system.

## 13. Ethics and data handling

The current study uses a public third-party dataset rather than newly collected personal data. No personal identifiers are intentionally redistributed in the repository, and the raw third-party dataset is not stored in GitHub.

If future research introduces human-subject data or additional personal information, the appropriate ethics approval, consent and data-governance requirements would need to be considered before collection or analysis.

## 14. What I would do if selected

The work would begin from the evidence already established here rather than starting from a completely new problem.

First, I would reproduce and strengthen the baseline experiments and complete the literature review with the supervisor. I would then define the distribution-shift conditions more precisely and test them systematically across time and devices.

The next stage would be to investigate whether the observed performance changes can be explained by measurable changes in the sensor data, followed by calibration and sensitivity experiments. If a suitable external dataset is available, I would use it to test how far the evaluation approach transfers.

The exact modelling techniques should remain open at this stage. If the evidence suggests that a different method is more appropriate, I would adapt the research direction rather than forcing the project to follow a predetermined algorithm.

That is also how I would describe the project to a supervisor: **my MSc work gives me the starting point; the research question is about reliability under changing data; the experiments are how I intend to find out what actually happens.**

## 15. Current status

### Completed or documented

- original MSc work preserved separately;
- dataset documentation and codebook;
- historical MSc reconstruction;
- baseline models;
- random evaluation;
- chronological evaluation;
- device-level evaluation record;
- feature-ablation work;
- threshold analysis;
- reproducibility documentation;
- public research repository.

### Next

- strengthen distribution-shift measurement;
- run temporal-gap sensitivity experiments;
- complete calibration analysis;
- investigate external validation;
- strengthen the literature review;
- refine the research questions with supervisor input;
- develop the work into a paper-style research manuscript if the results support it.

## 16. References

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

## 17. Proposal status

This is a **supervisor-discussion draft**, not a final university submission.

The exact research gap, distribution-shift definition, external-validation plan and final contribution should be refined through the literature review and supervisor feedback.
