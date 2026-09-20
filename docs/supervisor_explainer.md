# Supervisor Discussion Guide — Aman Gupta

## 1. The 60-second explanation

> My research started from my MSc dissertation, where I used environmental IoT sensor data to predict human movement near IoT devices. I have kept the original MSc implementation separate and unchanged, and then built a research extension around the same problem.
>
> When I revisited the work, I became interested in whether the model performance was reliable when the data changed. The dataset has only about 0.119% positive movement events, and it covers a relatively short period and three devices. So instead of treating one random split and accuracy as the whole story, I started testing random versus chronological evaluation, unseen-device evaluation, feature ablation and threshold sensitivity.
>
> My current research question is how reliably machine-learning models can predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices. I see the current work as a pilot and want to strengthen it through formal distribution-shift measurement, calibration and, if possible, external validation.

## 2. What I did in the MSc

The MSc dissertation was **Intelligent System to Predict Human Movement near IoT Devices**.

The work involved environmental IoT sensor data, data preparation, exploratory analysis and visualisation, class balancing for the movement target, several classification models, model comparison, hyperparameter tuning, and evaluation using accuracy, ROC-AUC and confusion matrices.

The original code is preserved as Aman.py in the separate MSc repository.

### Important distinction

The current research extension should not be described as if all of its experiments were part of the 2021 dissertation. The MSc work is the foundation. The temporal, device-shift, feature-ablation, threshold and reproducibility work belongs to the later extension.

## 3. Why the MSc approach was not enough for the new question

The original project was suitable for the MSc objective, but the research extension asks a different question.

The original modelling workflow created a balanced subset and relied heavily on accuracy. That is useful for documenting the historical experiment, but it does not preserve the original rare-event prevalence.

For the new question, the evaluation retains the rare-event structure and reports metrics that show how well the positive class is identified.

This is not a claim that the MSc work was wrong. It is a change in research question and evaluation objective.

## 4. Central research problem

The central issue is **reliability under distribution change**.

- **Temporal change:** future observations may differ from earlier observations.
- **Device change:** a model trained on some devices may not perform the same way on another device.
- **Feature change:** some environmental variables may be more useful in one setting than another.
- **Decision-threshold change:** the threshold changes the balance between finding positive events and producing false alarms.

## 5. Why class imbalance matters

There are 482 positive movement observations among 405,184 total observations.

A model can therefore have high-looking accuracy while still being poor at finding movement events.

The current research pays more attention to average precision, precision, recall, F1, balanced accuracy, false positives and threshold sensitivity.

## 6. Why compare random and chronological splits?

A random split mixes observations from the same overall time period into training and testing. A chronological split asks a more realistic question: if I train using earlier observations, how does the model perform on later observations?

The two evaluations answer different questions. The purpose is not to declare one split universally correct, but to understand how reported performance changes under different assumptions.

## 7. Why test an unseen device?

A model can learn patterns that are specific to a device or its local environment.

A device-level hold-out asks whether a model trained without a particular device can transfer to that device.

The current dataset has only three devices, so this is preliminary evidence rather than a definitive generalisation study.

## 8. Why feature ablation?

Feature ablation removes or changes selected sensor variables and measures how performance changes. The purpose is to understand whether the model depends strongly on particular inputs. This should be interpreted as predictive importance, not proof of causality.

## 9. Why threshold analysis?

A default classification threshold is not automatically the correct operating point. Changing the threshold can increase recall while reducing precision, or reduce false positives while missing more positive events.

For a rare event such as movement, that trade-off can be important.

## 10. Working research gap

I am deliberately describing this as a **working research gap**, rather than claiming that nobody has studied it.

The literature already shows that sensor-based activity recognition can be affected by device, sensor, temporal and contextual distribution changes.

My narrower question is whether a small and interpretable environmental-IoT movement-prediction workflow can be evaluated in a way that makes those reliability changes visible, especially when the positive event is extremely rare.

## 11. What is novel at this stage?

I would not present the current work as a confirmed novel algorithm.

The current contribution is better described as a **research evaluation framework and empirical investigation** built around the original MSc problem, rare-event evaluation, temporal hold-out, device-level hold-out, feature ablation, threshold analysis and reproducible experiment records.

Whether this becomes a stronger research contribution depends on the next-stage experiments and literature review.

## 12. What would make it stronger?

1. Formal distribution-shift measurements.
2. Multiple temporal hold-out configurations.
3. Probability calibration analysis.
4. Stronger device-level validation if more devices/data become available.
5. External validation on a comparable dataset.
6. More systematic literature review.
7. Sensitivity analysis across reasonable model configurations.
8. A paper-style manuscript with clearly separated historical and new evidence.

## 13. Questions to ask a supervisor

- Is the distribution-shift question sufficiently focused for an MPhil/PhD project?
- Which type of shift should become the primary research focus: temporal, device, sensor or a combination?
- Would external validation be necessary for the intended contribution?
- Which evaluation framework or literature should I build around?
- Would you recommend extending the current dataset or finding a second dataset?
- What would you consider a sufficiently strong methodological contribution?
- Which experiments should be prioritised before turning this into a formal proposal?

## 14. What to show in a meeting

1. README.md
2. docs/research_summary.md
3. docs/research_questions.md
4. docs/research_proposal.md
5. notebooks/02_msc_original_analysis.ipynb
6. notebooks/03_baseline_models.ipynb
7. notebooks/04_temporal_evaluation.ipynb
8. notebooks/05_robustness_analysis.ipynb
9. results/canonical_research_metrics.csv
10. Original MSc repository and Aman.py

The story is simple:

**What I originally did → what I noticed → why I changed the evaluation → what I tested → what I know → what I still need to investigate.**

## 15. Presentation rule

Be precise about what is original MSc evidence and what is later research.

Use:
> My MSc work gave me the foundation. I then reconstructed the workflow and built a separate research extension to investigate reliability under distribution shift.

Do not say:
> My MSc proved that the model generalises.

The current evidence does not support that broader claim.