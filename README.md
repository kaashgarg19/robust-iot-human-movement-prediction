# Robust IoT Human Movement Prediction

A research portfolio built from my MSc dissertation on predicting human movement near IoT devices using environmental sensor data and machine-learning methods.

## Where this project started

My MSc dissertation at Birmingham City University explored whether environmental measurements from IoT devices could be used to predict human movement.

**Original dissertation:** *Intelligent System to Predict Human Movement near IoT Devices*

This repository keeps the original work separate from the later re-analysis. That makes it easier to see what came from the MSc project and what I have done afterwards.

## Current project

I am using the original work as a starting point for a more careful analysis of rare movement events.

The current work looks at practical questions around:
- uneven class distribution
- chronological evaluation
- differences between devices
- feature sensitivity
- threshold choice
- reproducibility

I am treating this as ongoing analysis rather than presenting it as a finished published study.

## Workflow

**Original MSc work → data checks → reproducible analysis → controlled evaluation → additional checks**

## Dataset

The analysis uses environmental sensor telemetry data. The raw dataset is not redistributed here.

See [Dataset](docs/03_dataset.md) for the dataset description, source information and handling notes.

## Repository structure

- [Project overview](docs/01_project_overview.md)
- [MSc background](docs/02_msc_background.md)
- [Dataset](docs/03_dataset.md)
- [Methodology](docs/04_methodology.md)
- [Codebook](docs/05_codebook.md)
- [Reproducibility](docs/06_reproducibility.md)
- [Original MSc work](original_msc/README.md)
- Research documentation

## Original MSc work

The original Python work and dissertation are kept under original_msc/.

That separation matters: the dissertation is the academic starting point, while the later files record the re-analysis and extensions.

## Tools

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Jupyter

## Status

This repository is a work in progress. I am documenting the data, code and decisions as I go rather than presenting unfinished work as a final publication.

## Data and licensing

The repository does not claim ownership of third-party datasets. Dataset rights and source conditions remain with the original providers. Original code and documentation written for this repository are kept separate from third-party material.