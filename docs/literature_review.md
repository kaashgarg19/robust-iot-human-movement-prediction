# Focused Literature Review

## Scope

This review supports the research direction:

**Robust human-movement prediction from environmental IoT sensors under temporal and device distribution shift.**

It is a focused working review, not yet a systematic review. Its purpose is to establish what is already known, identify the part of the problem that is still worth investigating, and guide the next experiments.

## 1. Sensor-based human activity recognition is affected by heterogeneous data

Sensor-based human activity recognition is not always performed under stable data conditions. A 2024 review discusses data heterogeneity in sensor-based HAR, including temporal distribution changes, concept drift and concept evolution in streaming data.

For this project, that supports treating time as part of the evaluation design rather than assuming that randomly mixed observations are always representative of future observations.

**Reference**

*Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity* (2024 review).

https://pmc.ncbi.nlm.nih.gov/articles/PMC11679906/

## 2. Distribution shift across users, sensors and contexts is an active HAR problem

Recent HAR research explicitly studies distribution shifts. Chen, Odema and Al Faruque's 2025 work, *DisCovHAR*, addresses HAR under distribution shifts and examines variation associated with users and sensor positions.

This is directly relevant to the current research direction because the proposed experiments ask what happens when the data source changes rather than only when observations are randomly divided.

**Reference**

Chen, L., Odema, M., & Al Faruque, M. (2025). *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*. IEEE Internet of Things Journal.

DOI: 10.1109/JIOT.2025.3551263

https://its.uci.edu/research_products/published-journal-article-discovhar-contrastive-attention-for-human-activity-recognition-under-distribution-shifts/

## 3. Domain generalisation is becoming an explicit research direction

Adaimi and Thomaz's 2026 preprint examines distribution shifts in sensor-based HAR, including device type, sensor placement, sampling rate and user behaviour.

This work is useful for defining the vocabulary and experimental dimensions of distribution shift in HAR. It also means that the current project should not claim that distribution shift itself is a new problem.

**Reference**

Adaimi, R., & Thomaz, E. (2026). *Assessing Distribution Shift in Human Activity Recognition for Domain Generalization*. arXiv preprint.

DOI: 10.48550/arXiv.2606.24781

https://arxiv.org/abs/2606.24781

**Status note:** This source is treated as a 2026 preprint unless a later peer-reviewed version is verified.

## 4. Concept drift matters for IoT streams

IoT systems can operate as data streams in which the underlying distribution changes. Øren et al. (2025) review concept drift strategies under IoT constraints.

This supports a second part of the proposed research: measuring changes in the sensor data rather than simply observing that model performance changed.

**Reference**

Øren, A. E. et al. (2025). *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*. IEEE Access.

DOI: 10.1109/ACCESS.2025.3622973

https://doi.org/10.1109/ACCESS.2025.3622973

## 5. Rare-event evaluation needs careful metric choice

The project's positive movement event is extremely rare: 482 positive observations among 405,184 total observations.

In imbalanced classification, accuracy can remain high even when the positive class is poorly identified. Saito and Rehmsmeier (2015) show why precision-recall analysis can provide a more informative view of classifier behaviour under strong class imbalance.

That supports the current decision to report average precision, precision, recall and F1 alongside threshold behaviour rather than using accuracy as the main evidence.

**Reference**

Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432.

DOI: 10.1371/journal.pone.0118432

https://doi.org/10.1371/journal.pone.0118432

## 6. Robustness and domain generalisation provide a useful methodological connection

The broader machine-learning literature contains established work on domain generalisation: learning from one or more source distributions and assessing behaviour on a different target distribution.

For example, University of Melbourne researchers have published work on robust domain generalisation that explicitly addresses distribution bias and unseen domains, including activity-recognition examples.

**Reference**

Erfani, S. M., Baktashmotlagh, M., Moshtaghi, M., Nguyen, V., Leckie, C., Bailey, J., & Ramamohanarao, K. (2016). *Robust Domain Generalisation by Enforcing Distribution Invariance*. IJCAI.

https://people.eng.unimelb.edu.au/baileyj/papers/ijcai16Tv2.pdf

This is useful background rather than a direct template for the current environmental-IoT study.

## 7. What the literature means for this project

The literature gives us four important points:

1. Sensor-based activity-recognition data can be heterogeneous.
2. Device, user, sensor and temporal differences can create distribution shift.
3. Concept drift is relevant when IoT data are treated as streams.
4. Severe class imbalance changes how model performance should be interpreted.

These points support the research direction, but they do not by themselves establish the project's specific contribution.

## 8. Working research gap

The literature already contains substantial work on:

- sensor-based human activity recognition;
- distribution shift;
- domain generalisation;
- concept drift;
- online and continual adaptation;
- imbalanced classification.

Therefore, the project should **not** claim that distribution shift in HAR is a new problem.

The narrower question is:

> **How can an interpretable environmental-IoT human-movement prediction workflow be evaluated so that the combined effects of rare-event imbalance, temporal separation and device separation on reliability are made visible and reproducible?**

This is a working gap that still needs to be tested against a broader literature review.

## 9. Questions the literature review should answer next

### Evaluation

- Which temporal split strategies are commonly used in sensor-based HAR?
- How long should a temporal gap be before it is considered meaningful?
- How are device-level hold-outs normally defined?

### Metrics

- Which metrics are preferred for extremely rare activity events?
- How is average precision interpreted when prevalence is extremely low?
- When should calibration be reported alongside discrimination?

### Distribution shift

- How is sensor distribution shift measured?
- Which statistical or divergence measures are appropriate for these sensor variables?
- How should drift be separated from normal temporal variability?

### Generalisation

- What evidence is required before a model can reasonably be described as robust across devices?
- How do published studies validate models on genuinely unseen users, devices or environments?

### External validation

- Which public datasets have sufficiently comparable sensor variables and movement targets?
- If no dataset is sufficiently comparable, what alternative validation design would be defensible?

## 10. Implications for the experiments

The literature suggests that the next step should not simply be adding more complex classifiers.

The stronger path is to improve the experimental design:

**Measure the shift → evaluate the model under the shift → examine calibration/uncertainty → test sensitivity → validate externally where possible.**

That gives the project a clearer progression from the MSc work to a research question that can be tested systematically.

## References

1. *Machine Learning Techniques for Sensor-Based Human Activity Recognition with Data Heterogeneity* (2024 review).  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC11679906/

2. Chen, L., Odema, M., & Al Faruque, M. (2025). *DisCovHAR: Contrastive Attention for Human Activity Recognition Under Distribution Shifts*. IEEE Internet of Things Journal.  
   DOI: 10.1109/JIOT.2025.3551263  
   https://its.uci.edu/research_products/published-journal-article-discovhar-contrastive-attention-for-human-activity-recognition-under-distribution-shifts/

3. Adaimi, R., & Thomaz, E. (2026). *Assessing Distribution Shift in Human Activity Recognition for Domain Generalization*. arXiv.  
   DOI: 10.48550/arXiv.2606.24781  
   https://arxiv.org/abs/2606.24781

4. Øren, A. E. et al. (2025). *Concept Drift Under Harsh Constraints: A Review of Potential Strategies for IoT Systems*. IEEE Access.  
   DOI: 10.1109/ACCESS.2025.3622973  
   https://doi.org/10.1109/ACCESS.2025.3622973

5. Saito, T., & Rehmsmeier, M. (2015). *The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets*. PLOS ONE, 10(3), e0118432.  
   DOI: 10.1371/journal.pone.0118432  
   https://doi.org/10.1371/journal.pone.0118432

6. Erfani, S. M., Baktashmotlagh, M., Moshtaghi, M., Nguyen, V., Leckie, C., Bailey, J., & Ramamohanarao, K. (2016). *Robust Domain Generalisation by Enforcing Distribution Invariance*. IJCAI.  
   https://people.eng.unimelb.edu.au/baileyj/papers/ijcai16Tv2.pdf
