"""Historical reconstruction of the original MSc modelling workflow.

This script is intentionally kept separate from the research-extension
pipeline. It documents the modelling logic recovered from the MSc dissertation.
It should not be treated as the preferred modern evaluation protocol.
"""

from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score


FEATURES = ["co", "humidity", "light", "lpg", "smoke", "temp"]
TARGET = "motion"


def load_msc_data(path: str | Path) -> pd.DataFrame:
    """Load the original MSc dataset and reproduce its basic preparation."""
    df = pd.read_csv(path)

    # Historical dissertation preparation.
    df["hour"] = pd.to_datetime(df["ts"], unit="s").dt.hour
    df["minute"] = pd.to_datetime(df["ts"], unit="s").dt.minute
    df["second"] = pd.to_datetime(df["ts"], unit="s").dt.second
    df["microsecond"] = pd.to_datetime(df["ts"], unit="s").dt.microsecond
    df = df.drop("ts", axis=1)

    codes, _ = df["device"].factorize()
    df["deviceFactor"] = codes
    df = df.drop("device", axis=1)

    label = LabelEncoder()
    df["light"] = label.fit_transform(df["light"])
    df["motion"] = label.fit_transform(df["motion"])
    return df


def make_balanced_msc_split(df: pd.DataFrame, random_state: int = 42):
    """Reproduce the dissertation's 482-positive balanced subset strategy."""
    positives = df[df[TARGET] == 1]
    negatives = df[df[TARGET] == 0]

    true_train, true_test = train_test_split(
        positives, test_size=0.25, random_state=random_state
    )
    _, negative_subset = train_test_split(
        negatives, test_size=0.00119, random_state=random_state
    )
    false_train, false_test = train_test_split(
        negative_subset, test_size=0.25, random_state=random_state
    )

    result_train = pd.concat([true_train, false_train])
    result_test = pd.concat([true_test, false_test])
    return result_train, result_test


def run_original_models(result_train: pd.DataFrame, result_test: pd.DataFrame):
    """Run the main classifiers used in the MSc dissertation."""
    X_train = result_train.drop(TARGET, axis=1)
    y_train = result_train[TARGET]
    X_test = result_test.drop(TARGET, axis=1)
    y_test = result_test[TARGET]

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "Logistic Regression": LogisticRegression(),
        "KNN": KNeighborsClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "Gaussian NB": GaussianNB(),
        "SVC": SVC(),
        "Gradient Boosting": GradientBoostingClassifier(),
    }

    rows = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        rows.append(
            {
                "model": name,
                "accuracy": accuracy_score(y_test, prediction),
                "roc_auc_from_hard_predictions": roc_auc_score(y_test, prediction),
                "confusion_matrix": confusion_matrix(y_test, prediction).tolist(),
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    data_path = Path("../data/raw/iotdata.csv")
    df = load_msc_data(data_path)
    train, test = make_balanced_msc_split(df)
    results = run_original_models(train, test)
    print(results.to_string(index=False))
