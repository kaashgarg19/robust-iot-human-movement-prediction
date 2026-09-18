# Robust IoT Human Movement Prediction

![Project banner](figures/project-banner.svg)

A research repository extending my MSc dissertation on predicting human movement near IoT devices using environmental sensor data and machine-learning methods.

## Research direction

**Robust Rare-Event Human Movement Prediction from Environmental IoT Sensors under Temporal and Device Distribution Shift**

The current work examines how reliably environmental IoT sensor data can predict rare human-movement events when evaluation includes severe class imbalance, chronological variation and previously unseen devices.

### Main research question

> How reliably can environmental IoT sensor data predict rare human-movement events under class imbalance, temporal variation and device-level distribution shift?

## MSc foundation

My MSc dissertation at Birmingham City University investigated human movement near IoT devices using environmental sensor telemetry and machine-learning/data-mining methods.

- **Degree:** MSc Advanced Computer Science
- **University:** Birmingham City University, UK
- **Result:** Distinction
- **Original dissertation:** *Intelligent System to Predict Human Movement near IoT Devices*

The original MSc work and the later research extension are kept clearly separated in this repository.

## Research workflow

**IoT sensor data → Dataset audit → Preprocessing → Baseline modelling → Controlled evaluation → Temporal evaluation → Robustness analysis → Reproducible research record**

## Dataset

The project uses the **Environmental Sensor Telemetry Data** dataset published on Kaggle by **Gary A. Stafford**.

The raw dataset is not stored in this repository. See [Dataset](docs/03_dataset.md) for source, structure, licensing and data-handling information.

## Current analysis

The repository documents experiments covering:

- Controlled random 60/20/20 evaluation
- Chronological 60/20/20 evaluation
- Rare-event class imbalance
- Threshold selection using validation data
- Unseen-device evaluation
- Feature ablation
- Threshold sensitivity
- Temporal-gap sensitivity
- Recall uncertainty analysis
- Reproducibility and experiment tracking

The repository reports experimental evidence rather than treating a single model score as the conclusion.

## Repository map

- [Project overview](docs/01_project_overview.md)
- [MSc background](docs/02_msc_background.md)
- [Dataset](docs/03_dataset.md)
- [Methodology](docs/04_methodology.md)
- [Codebook](docs/05_codebook.md)
- [Reproducibility](docs/06_reproducibility.md)

### Original MSc work

- [Original MSc README](original_msc/README.md)
- [Original Python code](original_msc/Aman.py)
- [MSc dissertation](original_msc/dissertation/AmanGuptaDissertation_20101021.docx)
- [MSc dissertation record](original_msc/dissertation_record.md)

## Tools

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Jupyter

## Research status

This is an ongoing research portfolio project. The current repository distinguishes the original 2021 MSc work from subsequent analysis and documents the experimental setup and results used for future research development.

## Citation and reproducibility

Research documentation, codebooks, experimental logs and reproducibility materials are maintained alongside the analysis so that the workflow can be inspected and rerun.
