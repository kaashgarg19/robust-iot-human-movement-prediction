# Dataset

## Source

The dataset used for this project is **Environmental Sensor Telemetry Data**, published on Kaggle by **Gary A. Stafford**.

Source: https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k

The Kaggle dataset page describes the data as environmental sensor telemetry collected from three IoT sensor arrays connected to Raspberry Pi devices.

## Licence

The Kaggle dataset is listed as **CC0: Public Domain**.

The licence information was checked against the Kaggle dataset page on **15 September 2026**.

## Dataset size

The dataset used in the project contains:

- 405,184 rows
- 9 columns
- 3 IoT devices
- 6 environmental sensor measurements
- 1 timestamp field
- 1 device identifier
- 1 movement field used as the prediction target

These details match the dataset description published on Kaggle.

## Sensor information

The main environmental measurements are:

- Carbon monoxide (`co`)
- Humidity (`humidity`)
- Light (`light`)
- LPG (`lpg`)
- Smoke (`smoke`)
- Temperature (`temp`)

The other fields are:

- `ts` — timestamp
- `device` — IoT device identifier
- `motion` — movement recorded or not recorded

## Data period

Kaggle describes the dataset as covering **12 July 2020 to 19 July 2020 UTC**.

## Important note about this repository

The raw CSV is **not stored in this GitHub repository**. The repository documents the dataset and the work performed with it, while the original dataset remains available from its Kaggle source.

## Dataset check

The dataset source, structure, row count and licence have been checked against the original Kaggle dataset page. The working copy used for this project has the same 405,184-row, 9-column structure described by the source.
