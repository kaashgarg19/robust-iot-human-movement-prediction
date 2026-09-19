"""Canonical model factories for the research experiments."""
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42


def logistic_regression():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            solver="lbfgs",
            random_state=RANDOM_STATE,
        )),
    ])


def random_forest():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", RandomForestClassifier(
            n_estimators=30,
            max_depth=12,
            min_samples_leaf=20,
            max_features="sqrt",
            class_weight="balanced",
            max_samples=0.5,
            n_jobs=-1,
            random_state=RANDOM_STATE,
        )),
    ])


def hist_gradient_boosting():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", HistGradientBoostingClassifier(
            max_iter=50,
            learning_rate=0.08,
            max_leaf_nodes=15,
            min_samples_leaf=50,
            early_stopping=False,
            random_state=RANDOM_STATE,
        )),
    ])


def canonical_models():
    return {
        "Logistic Regression": logistic_regression(),
        "Random Forest": random_forest(),
        "HistGradientBoosting": hist_gradient_boosting(),
    }
