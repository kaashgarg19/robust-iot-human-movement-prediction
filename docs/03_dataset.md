# Dataset

## Source

The project uses the **Environmental Sensor Telemetry Data** dataset published on Kaggle by **Gary A. Stafford**.

**Source:** https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k

**Licence:** CC0: Public Domain

The source, dataset structure and licence were checked on **15 September 2026**.

## Dataset structure

The working dataset contains:

- **405,184 rows**
- **9 columns**
- **3 IoT devices**
- Environmental sensor measurements
- A timestamp field
- A device field
- A `motion` field used as the target

The observations cover approximately eight days, from **12 July 2020 to 19 July 2020 UTC**.

## Columns

The main fields are:

- `ts` — timestamp
- `device` — IoT device identifier
- `co` — carbon monoxide reading
- `humidity` — humidity reading
- `light` — light reading
- `motion` — movement indicator
- `lpg` — LPG-related sensor reading
- `smoke` — smoke-related sensor reading
- `temp` — temperature reading

## Data availability

The raw CSV is not committed to this repository. Download the dataset directly from the original Kaggle source when reproducing the project.

The repository documents the source, structure and licence so the origin of the data is clear.