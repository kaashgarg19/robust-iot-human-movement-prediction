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

## Repository structure

```text
robust-iot-human-movement-prediction/
├── data/
├── docs/
├── figures/
├── notebooks/
├── results/
├── src/
└── requirements.txt
```

More detailed analysis and experiments will be kept separate from the basic project documentation so the original MSc work remains clear.