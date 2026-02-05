"""
feature_utils.py

Purpose:
    Convert parsed packet metadata into ML-ready features:
    - Sequence features for CNNs
    - Aggregate features for classical ML
    - Defensive transformations (padding, jitter)

Notes:
    These are placeholder implementations to allow the pipeline to run
    safely before real data is introduced.
"""

import numpy as np
from typing import List, Dict

def build_sequence_feature(packets: List[Dict], max_len: int = 3000) -> np.ndarray:
    """
    Convert packet metadata into a fixed-length sequence.

    Current behavior:
        - Uses direction * size as a simple placeholder.
        - Pads or truncates to max_len.
    """
    seq = [p["direction"] * p["size"] for p in packets]
    seq = seq[:max_len]
    seq += [0] * (max_len - len(seq))
    return np.array(seq, dtype=np.int32)


def build_aggregate_feature(packets: List[Dict]) -> np.ndarray:
    """
    Build simple aggregate features.

    Current behavior:
        - Total bytes sent
        - Total bytes received
        - Packet count
    """
    sent = sum(p["size"] for p in packets if p["direction"] == 1)
    recv = sum(p["size"] for p in packets if p["direction"] == -1)
    count = len(packets)
    return np.array([sent, recv, count], dtype=np.float32)


def apply_padding(X: np.ndarray) -> np.ndarray:
    """
    Apply a simple padding defense.

    Current behavior:
        - Adds a constant offset to all values.
        - Placeholder for real padding logic.
    """
    return X + 10


def apply_timing_jitter(X: np.ndarray, jitter: float = 0.01) -> np.ndarray:
    """
    Apply timing jitter defense.

    Current behavior:
        - Adds small random noise to each element.
        - Placeholder for real timing jitter.
    """
    noise = np.random.normal(0, jitter, X.shape)
    return X + noise