# Dataset Codebook

## 1. Dataset identity

**Project:** Human Movement Prediction using IoT Data

**Original MSc foundation:** Intelligent System to Predict Human Movement near IoT Devices

**Source:** Environmental Sensor Telemetry Data, published on Kaggle by **Gary A. Stafford**.

**Licence:** CC0: Public Domain

**Source checked:** 15 September 2026

**Audited shape:** 405,184 rows × 9 columns.

**Observation period:** 12 July 2020 to 19 July 2020 UTC (approximately 8 days).

**Target:** `motion`.

**Positive events:** 482.

**Positive prevalence:** approximately 0.11896% (~0.119%).

**Devices:** 3.

## 2. Column-level codebook

| Column | Role | Expected type | Description | Research use | Notes |
|---|---|---|---|---|---|
| `ts` | Identifier/time | integer-like | Unix timestamp in seconds | Chronological ordering and temporal splits | Treat as seconds. |
| `device` | Group identifier | categorical/integer-like | IoT device identifier | Device-level evaluation | Kept separate from sensor features. |
| `co` | Sensor feature | numeric | Carbon monoxide reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `humidity` | Sensor feature | numeric | Relative humidity reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `light` | Sensor feature | numeric | Light-level reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `lpg` | Sensor feature | numeric | Liquefied petroleum gas (LPG) reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `smoke` | Sensor feature | numeric | Smoke reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `temp` | Sensor feature | numeric | Temperature reading | Predictive feature | Environmental telemetry; not treated as causal. |
| `motion` | Binary target | binary | Indicator of movement/activity near the sensing environment | Classification target | Positive class is rare; accuracy is not used as the main metric. |

## 3. Data-quality decisions

- The dataset contains 405,184 observations and 9 columns.
- There are 13 duplicated timestamp values. They are retained because simultaneous readings from different devices are plausible.
- The timestamp is interpreted as Unix seconds.
- The target is extremely imbalanced: 482 positives out of 405,184 observations.
- Accuracy is therefore not an appropriate headline metric.
- The main evaluation measures are average precision, precision, recall and F1-score.
- Missing-value handling, where required, is fitted on training data only.
- Random and chronological evaluations are kept separate.

## 4. Feature interpretation

Sensor measurements are treated as predictive inputs. Feature importance and ablation results describe model behaviour and **must not be interpreted as evidence that a sensor variable causes human movement**.

## 5. Data access

The raw Kaggle CSV is not included in this repository. The source and licence information are documented above, and the original dataset should be obtained directly from Kaggle when reproducing the project.
