from __future__ import annotations

from typing import Dict, Optional, Sequence, Tuple

import numpy as np


def regression_metrics(y_true: Sequence, y_pred: Sequence) -> Dict[str, float]:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    err = y_true - y_pred
    mse = float(np.mean(err**2))
    rmse = float(np.sqrt(mse))
    mae = float(np.mean(np.abs(err)))

    # R^2
    ss_res = float(np.sum(err**2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else float("nan")

    return {"mse": mse, "rmse": rmse, "mae": mae, "r2": r2}


def binary_classification_metrics(
    y_true: Sequence,
    y_proba: Sequence,
    threshold: float = 0.5,
) -> Dict[str, float]:
    """
    Requires y_proba in [0,1]. No sklearn dependency.
    Returns: acc, precision, recall, f1, logloss, brier
    """
    y_true = np.asarray(y_true).astype(int)
    y_proba = np.asarray(y_proba, dtype=float)

    eps = 1e-15
    p = np.clip(y_proba, eps, 1 - eps)
    y_pred = (p >= threshold).astype(int)

    tp = int(np.sum((y_pred == 1) & (y_true == 1)))
    tn = int(np.sum((y_pred == 0) & (y_true == 0)))
    fp = int(np.sum((y_pred == 1) & (y_true == 0)))
    fn = int(np.sum((y_pred == 0) & (y_true == 1)))

    acc = float((tp + tn) / max(1, len(y_true)))
    precision = float(tp / max(1, tp + fp))
    recall = float(tp / max(1, tp + fn))
    f1 = float(2 * precision * recall / max(eps, precision + recall))

    logloss = float(-np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))
    brier = float(np.mean((p - y_true) ** 2))

    return {
        "acc": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "logloss": logloss,
        "brier": brier,
    }


def calibration_curve(
    y_true: Sequence,
    y_proba: Sequence,
    n_bins: int = 10,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (bin_centers, frac_positives, mean_predicted)
    """
    y_true = np.asarray(y_true).astype(int)
    y_proba = np.asarray(y_proba, dtype=float)

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    bin_ids = np.digitize(y_proba, bins) - 1
    bin_ids = np.clip(bin_ids, 0, n_bins - 1)

    frac_pos = np.zeros(n_bins, dtype=float)
    mean_pred = np.zeros(n_bins, dtype=float)
    counts = np.zeros(n_bins, dtype=int)

    for b in range(n_bins):
        mask = bin_ids == b
        counts[b] = int(np.sum(mask))
        if counts[b] > 0:
            frac_pos[b] = float(np.mean(y_true[mask]))
            mean_pred[b] = float(np.mean(y_proba[mask]))
        else:
            frac_pos[b] = np.nan
            mean_pred[b] = np.nan

    bin_centers = (bins[:-1] + bins[1:]) / 2.0
    return bin_centers, frac_pos, mean_pred
