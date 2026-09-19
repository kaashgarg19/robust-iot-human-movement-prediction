# Original MSc Implementation — Verified Reconstruction

## Purpose

This document connects the GitHub research project to the MSc dissertation implementation. The source evidence was checked against the original MSc dissertation material and the recovered implementation. This page is written to explain the work in plain language while keeping the historical method separate from the current research extension.

The original MSc project was different from the later robustness study. The original work established the human-movement prediction problem, performed exploratory IoT telemetry analysis, created a balanced modelling subset, and compared multiple classifiers.

## 1. Original research aim

The MSc research asked a practical question: could readings from environmental IoT sensors be used to identify and predict human movement near the devices? The stated objectives included assessing environmental sensor telemetry, preprocessing sensor data from different devices/locations, applying data-mining methods, visualising telemetry, and evaluating data models.

## 2. Original dataset handling

The dissertation code loaded `iotdata.csv` with pandas and identified three IoT devices. The recorded dataset contained 405,184 observations and nine columns: `ts`, `device`, `co`, `humidity`, `light`, `lpg`, `motion`, `smoke`, and `temp`. The code reported no null values.

The original code also converted the Unix timestamp into hour, minute, second and microsecond fields, factorised the device identifier, and label-encoded the Boolean `light` and `motion` variables.

## 3. Original class-balancing strategy

The original dataset contained 482 positive `motion=True` observations and 404,702 negative observations. The dissertation therefore constructed a balanced modelling subset by sampling 482 negative observations, then splitting both classes 75/25 into training and test partitions. This produced 722 training observations and 242 test observations, with 361 positives in each partition.

This is preserved here as **historical MSc methodology**, not as the preferred evaluation approach for the research extension.

## 4. Original modelling workflow

The dissertation imported and evaluated:

- Logistic Regression
- K-Nearest Neighbours
- Random Forest
- Decision Tree
- XGBoost
- Gaussian Naive Bayes
- Support Vector Classifier
- Gradient Boosting

It also used cross-validation and GridSearchCV for model tuning.

The original Random Forest implementation reported approximately 81.40% test accuracy before the later tuning stage. The tuned model-comparison table reported Random Forest at approximately 81.82% accuracy, followed by XGBoost at approximately 80.17% and Logistic Regression, Decision Tree and Gradient Boosting at approximately 78.93%.

## 5. Methodological distinction

The original MSc implementation used a small balanced subset because the movement event was extremely rare. It also applied standardisation during the historical model evaluation. These choices are retained for historical traceability and are not treated as the final research protocol.

The research extension uses the full dataset and evaluates rare-event prediction under controlled random, chronological and device-level conditions. It prioritises precision-recall behaviour, average precision, recall and F1 rather than presenting accuracy as the main result.

## 6. MSc to research extension

```text
MSc 2021
Environmental IoT telemetry
        ↓
Exploratory analysis
        ↓
Human-movement classification
        ↓
Multiple ML classifiers
        ↓
Random Forest / tuned model comparison
        ↓
Research extension
        ↓
Full rare-event dataset
        ↓
Random evaluation
        ↓
Chronological evaluation
        ↓
Unseen-device evaluation
        ↓
Feature ablation + threshold analysis
        ↓
Reliability-focused evaluation
```

## 7. Research continuity

**Original MSc work:** environmental-IoT human-movement prediction.

**Current extension:** examining whether predictive performance remains reliable under extreme class imbalance, temporal change, device variation and different decision thresholds.
