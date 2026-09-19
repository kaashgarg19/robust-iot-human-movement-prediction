"""Data loading and validation utilities for the IoT movement project."""
from pathlib import Path
import pandas as pd

FEATURES = ["co", "humidity", "light", "lpg", "smoke", "temp"]
TARGET = "motion"
TIME_COL = "ts"
DEVICE_COL = "device"
REQUIRED_COLUMNS = [TIME_COL, DEVICE_COL, *FEATURES, TARGET]


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the local raw CSV without changing values."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}. Place the licensed/source CSV at this path."
        )
    return pd.read_csv(path)


def validate_schema(df: pd.DataFrame) -> dict:
    """Return a compact schema/data-quality audit."""
    missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    numeric_columns = [TIME_COL, *FEATURES, TARGET]
    numeric_report = {
        c: {"dtype": str(df[c].dtype), "missing": int(df[c].isna().sum())}
        for c in numeric_columns
    }
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_columns": missing_columns,
        "duplicate_timestamps": int(df[TIME_COL].duplicated().sum()),
        "unique_devices": int(df[DEVICE_COL].nunique(dropna=True)),
        "positive_events": int((df[TARGET] == 1).sum()),
        "positive_prevalence": float((df[TARGET] == 1).mean()),
        "numeric_report": numeric_report,
    }


def prepare_time(df: pd.DataFrame) -> pd.DataFrame:
    """Add a UTC datetime view of the verified Unix-second timestamp."""
    out = df.copy()
    out["datetime_utc"] = pd.to_datetime(out[TIME_COL], unit="s", utc=True)
    return out
