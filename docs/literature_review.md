# Focused Literature Review — Working Notes

## Scope

This review supports the proposed research direction: **robust human-movement prediction from environmental IoT sensors under temporal and device distribution shift**.

It is intentionally a working review rather than a claim of a complete systematic literature review.

## 1. Sensor-based human activity recognition is affected by heterogeneity

A recent review of sensor-based human activity recognition identifies streaming-data heterogeneity as an important issue. It discusses temporal distribution changes, concept drift, concept evolution and other forms of changing activity data. This supports treating time-dependent evaluation as a research concern rather than assuming that randomly mixed samples represent deployment conditions.

Reference:
- *Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity* (2024 review)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11679906/

## 2. Distribution shift across devices and contexts remains an active problem

Recent work in the IEEE Internet of Things Journal has explicitly studied human activity recognition under distribution shifts, including changes associated with users and sensor positions. The reported experiments show that distribution-shift-aware representation learning can change generalisation performance.

Reference:
- Chen, Luke; Odema, Mohanad; Al Faruque, Mohammad. *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*. IEEE Internet of Things Journal, 2025.
- DOI: 10.1109/JIOT.2025.3551263
- https://its.uci.edu/research_products/published-journal-article-discovhar-contrastive-attention-for-human-activity-recognition-under-distribution-shifts/

## 3. Domain generalisation is becoming a specific research direction

A 2026 preprint by Adaimi and Thomaz systematically examines distribution shifts in sensor-based human activity recognition, including device type, sensor placement, sampling rate and user behaviour. The work is especially relevant to the proposed emphasis on evaluating models beyond a randomly mixed test set.

Reference:
- Adaimi, Rebecca; Thomaz, Edison. *Assessing Distribution Shift in Human Activity Recognition for Domain Generalization*. 2026.
- DOI: 10.48550/arXiv.2606.24781
- https://arxiv.org/abs/2606.24781

Important status note: this is a 2026 preprint, so it should be described as such unless a later peer-reviewed version is verified.

## 4. Concept drift is relevant to IoT streams

A 2025 IEEE Access review discusses concept drift in IoT systems and the practical constraints involved in detecting and adapting to changing data distributions.

Reference:
- Øren, Ask Espensønn et al. *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*. IEEE Access, 2025.
- DOI: 10.1109/ACCESS.2025.3622973
- https://doi.org/10.1109/ACCESS.2025.3622973

## 5. Rare events create an evaluation problem

The current project contains only 482 positive movement events among 405,184 observations. This makes headline accuracy difficult to interpret because a model can obtain high accuracy while providing poor information about the rare positive class.

The current repository therefore emphasises average precision, precision, recall and F1-score, together with threshold analysis.

The research argument should remain methodological: the purpose is to expose the behaviour of the positive-event detector under imbalance, not to claim that one metric is universally sufficient.

## 6. Working research gap

The literature already contains substantial work on:
- sensor-based human activity recognition;
- device and context distribution shift;
- domain generalisation;
- concept drift;
- continual or online adaptation.

The proposed project should therefore **not** claim that distribution shift in HAR is itself a new problem.

A narrower and more defensible research direction is:

> Evaluate how an interpretable environmental-IoT human-movement classifier behaves when rare-event imbalance, temporal separation and device separation are considered together, and develop a reproducible evaluation framework that makes these reliability changes visible.

This is the gap to test and refine through a fuller literature review.

## 7. Literature-review questions for the next stage

1. Which evaluation protocols are most commonly used for environmental-IoT movement/HAR data?
2. How do published studies define temporal and device-level distribution shift?
3. Which metrics are reported for rare-event sensor classification?
4. How are calibration and uncertainty handled in sensor-based classification?
5. What methods exist for drift detection and adaptation under resource constraints?
6. What evidence is required before a model can be described as robust across devices or time?
7. Which public datasets provide an appropriate external validation setting?

## 8. Implication for the proposed study

The literature supports moving beyond a single random train/test split. It also suggests that device and temporal variation should be treated explicitly when evaluating sensor-based machine-learning systems.

The next research task is therefore not simply to add a more complex model. It is to strengthen the experimental design, test the stability of the findings, and determine whether the observed behaviour survives under alternative datasets or evaluation settings.
