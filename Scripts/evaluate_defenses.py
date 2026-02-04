#!/usr/bin/env python3
"""
evaluate_defenses.py

Purpose:
    Apply padding, timing jitter, or morphing defenses to traces
    and measure how classifier accuracy changes.

Usage:
    python evaluate_defenses.py --data data/processed
"""

import argparse
import numpy as np
from utils.feature_utils import apply_padding, apply_timing_jitter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    args = parser.parse_args()

    X = np.load(f"{args.data}/X_seq.npy")
    y = np.load(f"{args.data}/y.npy")

    padded = apply_padding(X)
    jittered = apply_timing_jitter(X)

    print("[INFO] Defended datasets generated.")
    # You will later plug these into your trained models.

if __name__ == "__main__":
    main()