from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence, Tuple

import numpy as np
import matplotlib.pyplot as plt


def _ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def savefig(fig: plt.Figure, path: str | Path, dpi: int = 150) -> None:
    path = Path(path)
    _ensure_dir(path.parent)
    fig.tight_layout()
    fig.savefig(path, dpi=dpi)
    plt.close(fig)


def residual_plot(
    y_true: Sequence,
    y_pred: Sequence,
    title: str = "Residuals vs Predicted",
) -> plt.Figure:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    resid = y_true - y_pred

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(y_pred, resid)
    ax.axhline(0.0)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Residual (y - y_hat)")
    ax.set_title(title)
    return fig


def qq_plot(
    residuals: Sequence,
    title: str = "Q-Q Plot (Residuals)",
) -> plt.Figure:
    r = np.asarray(residuals, dtype=float)
    r = r[~np.isnan(r)]
    r = np.sort(r)
    n = len(r)

    # Normal theoretical quantiles (approx) without scipy:
    # use inverse error function approximation via numpy (if available) fallback
    # For safety: try scipy if installed; else approximate with numpy's percentile-based mapping.
    try:
        from scipy.stats import norm  # type: ignore

        theo = norm.ppf((np.arange(1, n + 1) - 0.5) / n)
    except Exception:
        # percentile-based rough approximation
        theo = np.linspace(-2.5, 2.5, n)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(theo, r)
    # reference line
    if n > 1:
        slope = (r[-1] - r[0]) / (theo[-1] - theo[0] + 1e-12)
        intercept = r[0] - slope * theo[0]
        ax.plot(theo, slope * theo + intercept)
    ax.set_xlabel("Theoretical Quantiles (Normal)")
    ax.set_ylabel("Sample Quantiles (Residuals)")
    ax.set_title(title)
    return fig


def calibration_plot(
    bin_centers: Sequence,
    frac_positives: Sequence,
    mean_predicted: Optional[Sequence] = None,
    title: str = "Calibration Curve",
) -> plt.Figure:
    x = np.asarray(bin_centers, dtype=float)
    y = np.asarray(frac_positives, dtype=float)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([0, 1], [0, 1])
    ax.scatter(x, y)

    if mean_predicted is not None:
        mp = np.asarray(mean_predicted, dtype=float)
        ax.scatter(mp, y)

    ax.set_xlabel("Predicted probability")
    ax.set_ylabel("Fraction of positives")
    ax.set_title(title)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return fig
