"""Evaluation utilities that keep rare-event metrics explicit."""
import numpy as np
from sklearn.metrics import average_precision_score, balanced_accuracy_score, f1_score, precision_score, recall_score


def classification_metrics(y_true, y_score, threshold=0.5):
    y_pred = (np.asarray(y_score) >= threshold).astype(int)
    return {
        "average_precision": float(average_precision_score(y_true, y_score)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "threshold": float(threshold),
        "false_positives": int(((y_pred == 1) & (np.asarray(y_true) == 0)).sum()),
    }


def select_threshold_by_validation_f1(y_true, y_score, thresholds=None):
    """Select the threshold using validation F1 only."""
    if thresholds is None:
        thresholds = np.linspace(0.01, 0.99, 99)
    best_threshold, best_f1 = 0.5, -1.0
    for threshold in thresholds:
        score = f1_score(y_true, np.asarray(y_score) >= threshold, zero_division=0)
        if score > best_f1:
            best_threshold, best_f1 = float(threshold), float(score)
    return best_threshold, best_f1
