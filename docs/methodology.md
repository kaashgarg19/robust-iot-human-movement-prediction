# Methodology

## 1. Data understanding

The study first establishes the dataset structure, target variable, environmental sensor variables, timestamp information and device identifiers.

## 2. Data validation

The audited dataset contains 405,184 observations, 9 columns, 3 devices and 482 positive movement events. Validation covers:

- Missing values
- Duplicate observations/timestamps
- Data types
- Class distribution
- Timestamp coverage
- Device coverage
- Invalid or implausible values where identifiable
- Potential target leakage

The timestamp is treated as Unix seconds. Duplicate timestamp values are retained because simultaneous observations from different devices are plausible.

## 3. Preprocessing

The research-extension workflow keeps the original sensor variables and applies preprocessing through reproducible Python pipelines. Any transformation learned from data is fitted on the training portion only to reduce information leakage.

## 4. Historical MSc baseline

The repository preserves a separate reconstruction of the original MSc workflow. The MSc deliberately sampled negative observations to create a balanced modelling subset and primarily reported accuracy. That historical procedure is retained for provenance and comparison, not as the preferred evaluation protocol for the current research question.

## 5. Current model comparison

The canonical research-extension models are:

- Logistic Regression
- Random Forest
- Histogram Gradient Boosting

The current evaluation prioritises average precision, precision, recall and F1 because movement events are extremely rare. Accuracy is retained only as historical context.

## 6. Robust evaluation

### Random evaluation

A stratified 60/20/20 train/validation/test split provides a conventional reference point. Decision thresholds are selected using validation data only, and the test set remains untouched until final evaluation.

### Temporal generalisation

A chronological 60/20/20 split estimates performance on later observations rather than randomly mixed observations. This is the primary generalisation test for the current research question.

### Device-level generalisation

Where the device identifiers support it, selected devices are held out from training to assess cross-device generalisation. With only three devices, these results are treated as preliminary.

### Feature ablation

Features or feature groups are removed systematically to examine how predictive performance changes. Ablation and feature importance are interpreted as model evidence, not causal evidence.

### Threshold sensitivity

Performance is examined across decision thresholds to expose precision/recall trade-offs rather than assuming 0.5 is optimal.

### Uncertainty and diagnostics

The research record also includes temporal recall uncertainty and precision-recall/calibration diagnostics where the corresponding artifacts are available. These diagnostics are used to qualify conclusions, not to imply statistical certainty beyond the available data.

## 7. Current evidence boundary

The audited pilot evidence is based on one dataset covering approximately eight days and three devices, with 482 positive events. It therefore supports a research hypothesis and methodological demonstration, not a claim of deployment readiness or universal model superiority.

## 8. Reporting standard

Every canonical result should identify the dataset version/hash, split, preprocessing, model configuration, threshold rule, metrics, code version and limitations. Results from the MSc and current extension must remain clearly separated.
