# Robust IoT Human Movement Prediction

![Project banner](figures/project-banner.svg)

A machine-learning project based on my MSc dissertation, using environmental IoT sensor data to study and predict human movement.

## About the project

My MSc dissertation at Birmingham City University focused on predicting human movement near IoT devices using environmental sensor data and machine-learning methods.

This repository brings the original project into a clean, organised format and provides a place to document the work as it develops.

## Project flow

**IoT sensor data → Data preparation → Exploration → Machine learning → Results**

## Dataset

The project uses the **Environmental Sensor Telemetry Data** dataset published on Kaggle by **Gary A. Stafford**.

The Kaggle page lists the dataset licence as **CC0: Public Domain**. The source, structure and licence were checked on 15 September 2026.

The raw CSV is not stored in this repository. See [Dataset](docs/03_dataset.md) for details.

## MSc background

- **Degree:** MSc Advanced Computer Science
- **University:** Birmingham City University, UK
- **Result:** Distinction
- **Dissertation:** *Intelligent System to Predict Human Movement near IoT Devices*

## Tools

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Documentation

- [Project overview](docs/01_project_overview.md)
- [MSc background](docs/02_msc_background.md)
- [Dataset](docs/03_dataset.md)
- [Basic methodology](docs/04_methodology.md)

## Original MSc work

- [Original MSc work](original_msc/README.md)
- [Original Python code](original_msc/Aman.py)
- [MSc dissertation](original_msc/dissertation/AmanGuptaDissertation_20101021.docx)
- [MSc dissertation record](original_msc/dissertation_record.md)

## Repository structure

```text
robust-iot-human-movement-prediction/
├── README.md
├── docs/
│   ├── 01_project_overview.md
│   ├── 02_msc_background.md
│   ├── 03_dataset.md
│   └── 04_methodology.md
├── figures/
│   └── project-banner.svg
└── original_msc/
    ├── README.md
    ├── Aman.py
    ├── dissertation_record.md
    └── dissertation/
        ├── README.md
        └── AmanGuptaDissertation_20101021.docx
```

The repository is being built in stages. The original MSc work is kept separate from any later research extension.
