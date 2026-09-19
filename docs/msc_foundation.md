# MSc Foundation and Research Continuity

## Original MSc project

**Degree:** MSc Advanced Computer Science, Birmingham City University, UK  
**Dissertation:** *Intelligent System to Predict Human Movement near IoT Devices*  
**Research area:** IoT analytics, environmental sensor data and machine learning

The original dissertation investigated whether environmental telemetry from IoT devices could be used to predict human movement. It covered the research background, literature review, methodology, data analysis, machine-learning implementation and discussion of limitations and future work.

## What is carried forward

The current repository keeps the same central problem and examines it using a more controlled evaluation approach:

| MSc foundation | Current research extension |
|---|---|
| Human movement prediction | Rare-event human-movement prediction |
| Environmental IoT telemetry | Environmental IoT sensing across time and devices |
| Machine-learning models | Controlled model comparison |
| Prediction performance | Precision-recall and threshold-aware evaluation |
| Conventional evaluation | Random vs chronological evaluation |
| IoT devices | Unseen-device evaluation |
| Sensor variables | Feature-ablation analysis |

## Dataset

The research dataset contains **405,184 observations**, six environmental sensor features (`co`, `humidity`, `light`, `lpg`, `smoke`, `temp`) and a `motion` target. It contains **482 positive movement events (~0.119%)**, three devices and approximately eight days of observations. The raw timestamp field is treated as Unix seconds.

## Important distinction

This repository contains a research extension of the MSc work. The later experiments were not part of the original MSc dissertation. Results from the MSc and results from the current extension are kept clearly separated.

## Original dissertation material

The full MSc dissertation is retained as supporting academic evidence and is not included in this public repository. Original code is documented separately where it can be described accurately.

## Research continuity

The central continuity is:

**MSc question:** Can environmental IoT telemetry help predict human movement?  
**Research extension:** How reliable is that prediction when movement events are extremely rare and sensor distributions change across time and devices?
