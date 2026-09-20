# Research Summary — Aman Gupta

## Working title

**Robust Human-Movement Prediction from Environmental IoT Sensors Under Temporal and Device Distribution Shift**

## How this research started

This work grew out of my MSc dissertation at Birmingham City University, **Intelligent System to Predict Human Movement near IoT Devices**.

In the MSc project, I worked with environmental sensor data from IoT devices and looked at whether those measurements could be used to predict human movement. I prepared and explored the data, compared several machine-learning models, tuned models and evaluated their results.

The original work is kept separately in the [MSc repository](https://github.com/kaashgarg19/iot-human-movement-prediction-msc). The original `Aman.py` file is preserved there rather than being rewritten as part of this later work.

## Why I decided to continue it

When I came back to the project, I started looking at the data and the original approach again rather than simply treating the old result as the end of the project.

One thing stood out: movement is a very rare event in this dataset. There are **482 positive movement observations out of 405,184 observations**, about **0.119%**.

That made me question how much confidence we should place in a result from a randomly mixed evaluation, especially if the real situation is that we train on earlier data and later receive data from a different period or device.

That became the starting point for the research extension.

## The question I am now asking

> **How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?**

I am looking at this through a few practical questions:

- What happens when the data is split randomly compared with chronologically?
- How well does a model transfer to a device that was not used for training?
- Which sensor variables matter most to the model's predictions?
- How much does the decision threshold change precision and recall?
- What does model performance actually mean when the positive event is extremely rare?

## What is different from my MSc work?

The MSc work and the current research are deliberately kept separate.

| Original MSc work | Current research extension |
|---|---|
| Worked with a balanced modelling subset | Keeps the original rare-event distribution |
| Accuracy was an important reported measure | Gives more attention to precision-recall behaviour |
| Random modelling workflow | Random and chronological evaluation |
| Historical model comparison | Reproducible baseline pipeline |
| Original feature set | Feature-ablation experiments |
| Standard classification decision | Threshold-sensitivity analysis |
| Dissertation-level evaluation | Additional device and temporal reliability checks |

The point is not to say that the MSc approach was wrong. I am asking a different question now, so I need a different evaluation setup.

## What I have done so far

The current research repository contains:

1. Dataset validation and data-quality checks
2. A documented reconstruction of the historical MSc workflow
3. Baseline Logistic Regression, Random Forest and HistGradientBoosting models
4. Stratified random evaluation
5. Chronological hold-out evaluation
6. Preliminary unseen-device evaluation
7. Feature-ablation analysis
8. Decision-threshold sensitivity analysis
9. Precision-recall diagnostics
10. Uncertainty analysis where supported by the audited record
11. Reproducibility documentation
12. A working research proposal

The notebooks follow the research story:

`01_data_validation` → `02_msc_original_analysis` → `03_baseline_models` → `04_temporal_evaluation` → `05_robustness_analysis`

## Dataset

The working dataset contains:

- **405,184 observations**
- **9 columns**
- **3 IoT devices**
- **482 positive movement events**
- approximately **0.119% positive prevalence**
- approximately **8 days of observations**

The original third-party dataset is not redistributed in GitHub. Its source, structure and access information are documented in the repository.

## What the current results mean

I am treating the current results as **pilot evidence from this dataset**, not as proof that a model is ready for deployment or that the findings will automatically generalise to other datasets.

The short observation period and three-device setup are important limitations. They are also part of why I want to continue the research.

The aim is to understand what changes when the evaluation becomes more realistic, rather than simply finding a model that produces the highest number on one test split.

## What I want to investigate next

The next stage is focused on understanding the shift itself.

- Measure how the sensor distributions change across time and devices.
- Test several temporal hold-out configurations.
- Look at probability calibration under changing data.
- Strengthen the device-level evaluation if more data become available.
- Look for a suitable external dataset for validation.
- Test how sensitive the conclusions are to reasonable changes in the model setup.
- Develop the literature review into a stronger research foundation.
- Turn the work into a paper-style research manuscript.

## Intended contribution

At this stage, I am not claiming to have invented a new machine-learning algorithm.

The contribution I am working toward is a clearer and more reproducible way of studying **reliability of environmental-IoT movement prediction under rare events and changing data conditions**.

The important part for me is being able to show:

**what I originally did → what I noticed when I revisited it → why I changed the evaluation → what I tested → what the evidence currently says → what still needs to be tested.**

## Current limitations

The main limitations at this stage are:

- approximately eight days of observations;
- only three devices;
- very few positive movement events relative to the total dataset;
- one primary dataset so far.

These limitations mean the current work should be treated as a research starting point rather than a completed generalisation study.

## Current status

**Completed:** MSc reconstruction, dataset documentation, baseline evaluation, temporal evaluation, device-level evaluation record, feature ablation, threshold analysis and reproducibility structure.

**Next:** stronger distribution-shift analysis, calibration, external validation where feasible, literature review and a paper-style manuscript.

## Research links

- [Current research repository](https://github.com/kaashgarg19/robust-iot-human-movement-prediction)
- [Original MSc repository](https://github.com/kaashgarg19/iot-human-movement-prediction-msc)
- [Research proposal](research_proposal.md)
- [Research questions](research_questions.md)
- [Reproducibility guide](reproducibility.md)
- [Portfolio](https://kaashgarg19.github.io/kaashgarg19/)
- [ORCID](https://orcid.org/0009-0007-4112-9993)
