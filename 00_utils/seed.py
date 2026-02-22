from __future__ import annotations

import os
import random
from typing import Optional

import numpy as np


def set_seed(seed: int = 42, deterministic: bool = True) -> None:
    """
    Set random seeds for reproducibility.
    - numpy
    - python random
    - (optional) torch if installed

    deterministic=True will try to enable deterministic algorithms in torch.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch  # type: ignore

        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if deterministic:
            torch.backends.cudnn.deterministic = True  # type: ignore
            torch.backends.cudnn.benchmark = False  # type: ignore
            try:
                torch.use_deterministic_algorithms(True)  # type: ignore
            except Exception:
                pass
    except Exception:
        # torch not installed or not available — silently ignore
        pass
