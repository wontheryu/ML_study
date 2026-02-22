from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, Optional, Sequence, Tuple

import numpy as np


def train_test_split_iid(
    n: int,
    test_size: float = 0.2,
    seed: int = 42,
    shuffle: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    IID hold-out split by indices [0..n-1].
    Returns: (train_idx, test_idx)
    """
    if not (0.0 < test_size < 1.0):
        raise ValueError("test_size must be between 0 and 1")

    idx = np.arange(n)
    if shuffle:
        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

    n_test = int(round(n * test_size))
    test_idx = idx[:n_test]
    train_idx = idx[n_test:]
    return train_idx, test_idx


def train_test_split_stratified(
    y: Sequence,
    test_size: float = 0.2,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simple stratified hold-out split by class labels y.
    Returns: (train_idx, test_idx)
    """
    y = np.asarray(y)
    n = len(y)
    if not (0.0 < test_size < 1.0):
        raise ValueError("test_size must be between 0 and 1")

    rng = np.random.default_rng(seed)
    test_idx_list = []
    train_idx_list = []

    for cls in np.unique(y):
        cls_idx = np.where(y == cls)[0]
        rng.shuffle(cls_idx)
        n_test = int(round(len(cls_idx) * test_size))
        test_idx_list.append(cls_idx[:n_test])
        train_idx_list.append(cls_idx[n_test:])

    test_idx = np.concatenate(test_idx_list) if test_idx_list else np.array([], dtype=int)
    train_idx = np.concatenate(train_idx_list) if train_idx_list else np.array([], dtype=int)

    rng.shuffle(test_idx)
    rng.shuffle(train_idx)
    return train_idx, test_idx


def timeseries_split(
    n: int,
    n_splits: int = 5,
    test_size: Optional[int] = None,
    gap: int = 0,
) -> Iterator[Tuple[np.ndarray, np.ndarray]]:
    """
    Walk-forward split for time series.
    - No shuffling.
    - Each split uses earlier indices as train and later contiguous block as test.

    If test_size is None, it uses roughly n/(n_splits+1).
    gap: number of samples to drop between train end and test start (leakage buffer).
    """
    if n_splits < 1:
        raise ValueError("n_splits must be >= 1")
    if test_size is None:
        test_size = n // (n_splits + 1)
    if test_size <= 0:
        raise ValueError("test_size must be positive")

    for k in range(1, n_splits + 1):
        test_end = k * test_size
        test_start = test_end - test_size
        train_end = max(0, test_start - gap)

        train_idx = np.arange(0, train_end)
        test_idx = np.arange(test_start, test_end)

        if len(train_idx) == 0 or len(test_idx) == 0:
            continue
        yield train_idx, test_idx
