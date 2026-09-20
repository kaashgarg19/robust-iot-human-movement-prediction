<div align="center">

<img src="figures/project-banner.svg" alt="Robust IoT Human Movement Prediction" width="100%" />

# Robust IoT Human Movement Prediction

**Environmental IoT · Machine Learning · Human Movement · Reproducible Evaluation**

[Research CV](https://github.com/kaashgarg19/kaashgarg19/blob/main/Aman_Gupta_CV.pdf) · [Research summary](docs/research_summary.md) · [Research questions](docs/research_questions.md) · [Research proposal](docs/research_proposal.md) · [Literature review](docs/literature_review.md) · [Original MSc repository](https://github.com/kaashgarg19/iot-human-movement-prediction-msc) · [MSc foundation](docs/msc_foundation.md) · [Dataset](docs/dataset_documentation.md) · [Methodology](docs/methodology.md) · [Experiments](docs/experimental_protocol.md) · [Reproducibility](docs/reproducibility.md)

</div>

## Overview

This repository is the research extension I am building from my MSc dissertation, *Intelligent System to Predict Human Movement near IoT Devices*.

My original MSc work asked whether environmental sensor measurements from IoT devices could help predict human movement. I am using that same starting point now, but looking more closely at what happens when movement events are rare and when the data changes over time or between devices.

I have kept the **original MSc work separate from this research extension**. That makes the progression easier to follow: what I did in 2021, what I reconstructed for transparency, and what belongs to the current research direction.

## Current research question

> How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?

### Questions I am exploring

1. How do baseline models perform on the available environmental IoT data?
2. How different are results when observations are split randomly versus chronologically?
3. How well do models transfer to a device that was not represented in training?
4. How much do individual sensor variables affect predictive performance?
5. How does the decision threshold change the precision/recall trade-off for the movement class?
6. How should model performance be interpreted when positive movement events are extremely rare?

The working hypothesis is that a randomly mixed evaluation may give a more optimistic view of performance than an evaluation that separates later observations or unseen devices. This is something I am testing, not assuming in advance.

## MSc foundation

**MSc Advanced Computer Science — Distinction**  
Birmingham City University, UK · 2020–2021

**Dissertation:** *Intelligent System to Predict Human Movement near IoT Devices*

The original project included environmental sensor-data preparation, exploratory analysis, machine-learning classification, model comparison and discussion of limitations and future work.

I keep the historical implementation and reported results as a separate record. They are not mixed into the current research-extension experiments.

## Dataset

The project uses the **Environmental Sensor Telemetry Data** dataset published on Kaggle by **Gary A. Stafford**.

- **405,184 observations**
- **9 columns**
- **3 IoT devices**
- **482 positive movement events**
- Approximately **0.119% positive prevalence**
- Approximately **8 days** of observations
- Timestamp stored as Unix seconds

The raw CSV is not redistributed in this repository. The source, structure and licence are documented in [Dataset documentation](docs/dataset_documentation.md).

[Original dataset source](https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k)

## What I have done so far

The current research record includes:

- dataset validation and data-quality checks
- reconstruction of the historical MSc workflow
- baseline Logistic Regression, Random Forest and HistGradientBoosting models
- stratified random evaluation
- chronological hold-out evaluation
- preliminary unseen-device evaluation
- feature-ablation analysis
- decision-threshold sensitivity analysis
- recall uncertainty and precision-recall diagnostics where supported by the audited record
- reproducibility documentation and experiment rules

The research notebook sequence makes the workflow easy to follow:

`01_data_validation.ipynb` → `02_msc_original_analysis.ipynb` → `03_baseline_models.ipynb` → `04_temporal_evaluation.ipynb` → `05_robustness_analysis.ipynb`

## Current evidence

The audited research record currently preserves average-precision values for the baseline and chronological evaluations in [results/canonical_research_metrics.csv](results/canonical_research_metrics.csv).

These are **dataset-specific pilot results**. The current dataset covers a short period and only three devices, so I am not presenting them as universal performance claims, deployment evidence or proof that one classifier is generally superior.

## Repository structure

```text
iot-human-movement-prediction/
├── data/       # data access notes
├── docs/       # research documentation
├── figures/    # research figures and diagrams
├── notebooks/  # analysis workflow
├── results/    # verified result artifacts
├── src/        # reusable Python code
└── requirements.txt
```

## Original MSc work

The original dissertation material is kept separately from the current research extension.

- [MSc foundation](docs/msc_foundation.md)
- [Historical implementation](docs/msc_original_implementation.md)
- [Historical results](docs/msc_results.md)
- [Dissertation record](docs/dissertation.md)

That separation matters: the later temporal, device-shift, imbalance and threshold analyses were **not part of the original 2021 dissertation**.

## Reproducibility

I have documented the intended environment, dataset checks, split rules, model configurations, threshold-selection rule and experiment metadata so that future reruns can be traced back to a specific setup.

For future canonical reruns, I record:

- dataset source/version and SHA-256 hash
- Python and package versions
- experiment ID
- Git commit
- split strategy
- preprocessing
- model configuration
- evaluation metrics
- interpretation and limitations

See the [Reproducibility Guide](docs/reproducibility.md).

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff).

## Author

**Aman Gupta**  
Computer Science · Data Analytics · Machine Learning · IoT

[Portfolio website](https://kaashgarg19.github.io/kaashgarg19/) · [ORCID](https://orcid.org/0009-0007-4112-9993) · [LinkedIn](https://www.linkedin.com/in/amangupta1911/)
