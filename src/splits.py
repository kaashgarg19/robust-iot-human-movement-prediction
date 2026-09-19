"""Random and chronological split helpers."""
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42


def random_60_20_20(df, target="motion"):
    """Return stratified train/validation/test partitions."""
    train, temp = train_test_split(
        df, test_size=0.4, stratify=df[target], random_state=RANDOM_STATE
    )
    validation, test = train_test_split(
        temp, test_size=0.5, stratify=temp[target], random_state=RANDOM_STATE
    )
    return train, validation, test


def chronological_60_20_20(df, time_col="ts"):
    """Return chronological 60/20/20 partitions after sorting by verified time."""
    ordered = df.sort_values(time_col).reset_index(drop=True)
    n = len(ordered)
    train_end = int(n * 0.6)
    validation_end = int(n * 0.8)
    return (
        ordered.iloc[:train_end].copy(),
        ordered.iloc[train_end:validation_end].copy(),
        ordered.iloc[validation_end:].copy(),
    )
