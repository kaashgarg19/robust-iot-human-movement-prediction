# Dataset Codebook

This page gives a simple description of the fields in the environmental IoT dataset used in the project.

| Field | Description | Role |
|---|---|---|
| `ts` | Unix timestamp for the observation | Time |
| `device` | Identifier for the IoT device that recorded the observation | Device |
| `co` | Carbon monoxide sensor reading | Input |
| `humidity` | Humidity reading | Input |
| `light` | Light sensor reading | Input |
| `motion` | Indicates whether movement was recorded | Target |
| `lpg` | LPG-related sensor reading | Input |
| `smoke` | Smoke-related sensor reading | Input |
| `temp` | Temperature reading | Input |

## Dataset summary

- Rows: **405,184**
- Columns: **9**
- IoT devices: **3**
- Missing values in the working dataset: **none**
- Target field: `motion`
- Recorded positive movement events: **482**

## Notes

The timestamp is stored as Unix time in the source data.

The `motion` field is the outcome being predicted. It is highly imbalanced in the full dataset, so the class distribution should be considered when interpreting model results.

This codebook describes the working dataset only. It does not add fields or interpretations that are not present in the source data.
