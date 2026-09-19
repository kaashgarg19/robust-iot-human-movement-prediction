# Research Questions

## Primary research question

How reliably can machine-learning models predict human movement from environmental IoT sensor data when the data distribution changes across time and sensing devices?

## Secondary questions

1. What is the predictive performance of baseline and tree-based machine-learning models on the available IoT dataset?
2. How much does performance change under temporal hold-out evaluation compared with random train/test splitting?
3. How well do models generalise to devices not represented in the training set?
4. Which environmental sensor variables contribute most to prediction performance?
5. How does decision-threshold selection affect precision, recall and F1-score for the movement class?
6. How do class imbalance and rare-event characteristics affect the interpretation of model performance?

## Hypothesis direction

The working hypothesis is that randomly shuffled evaluation may provide more optimistic estimates than evaluation that explicitly separates later observations or unseen devices from training data.

This is a hypothesis to be tested experimentally, not a predetermined conclusion.

## Research contribution target

The intended contribution is a more robust evaluation framework for environmental-IoT human-movement prediction, with emphasis on realistic distribution shifts and transparent reporting rather than claiming a universally superior classifier.
