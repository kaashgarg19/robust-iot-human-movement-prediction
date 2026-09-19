# Dataset Documentation

## Dataset role

The dataset is the empirical foundation for the MSc project and its current research extension. It was obtained from Kaggle and is documented as an external dataset rather than as data collected by the researcher.

## Source and licence

**Dataset:** Environmental Sensor Telemetry Data  
**Publisher:** Gary A. Stafford  
**Source:** https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k  
**Licence:** CC0: Public Domain

The source, dataset description and licence were checked against the Kaggle dataset page on **15 September 2026**.

## Dataset structure

| Item | Value |
|---|---|
| Observations | 405,184 |
| Columns | 9 |
| Target | `motion` |
| Sensor features | `co`, `humidity`, `light`, `lpg`, `smoke`, `temp` |
| Positive movement events | 482 |
| Positive prevalence | ~0.119% |
| Devices | 3 |
| Observation period | ~8 days |
| Timestamp | Unix seconds |
| Unique timestamps | 405,171 |
| Duplicate timestamp values | 13 |

## Interpretation

The target is highly imbalanced: only 482 of 405,184 observations are positive movement events. Consequently, headline accuracy can be misleading. The research therefore considers precision, recall, F1-score, average precision/PR-AUC and threshold-dependent behaviour.

## Timestamp note

The raw `ts` field is recorded as Unix time. The 13 duplicate timestamp values are retained because simultaneous readings across multiple devices can be plausible.

## Data-quality record

The working dataset used in this project was checked for its basic structure and quality. The documented record includes the row and column counts, data types, missing-value status, timestamp information, device identifiers, duplicate timestamps and target prevalence.

The dataset used for the documented experiments contains no missing values.

## Reproducibility

The raw dataset is not stored in this repository. Reproduction should use the original Kaggle source and the documented dataset structure.
