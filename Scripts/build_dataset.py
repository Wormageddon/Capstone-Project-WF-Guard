#!/usr/bin/env python3
"""
build_dataset.py

Purpose:
    Converts processed JSON traces into ML‑ready NumPy arrays:
    - sequence features
    - aggregate features
    - labels

Usage:
    python build_dataset.py --input data/processed --output data/processed
"""

import argparse
import json
import numpy as np
from pathlib import Path
from utils.feature_utils import (
    build_sequence_feature,
    build_aggregate_feature
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed")
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args()

    input_dir = Path(args.input)
    seq_features = []
    agg_features = []
    labels = []

    for file in input_dir.glob("*.json"):
        with open(file) as f:
            packets = json.load(f)

        seq = build_sequence_feature(packets)
        agg = build_aggregate_feature(packets)

        label = int(file.stem.split("_")[0])

        seq_features.append(seq)
        agg_features.append(agg)
        labels.append(label)

    np.save(input_dir / "X_seq.npy", np.array(seq_features))
    np.save(input_dir / "X_agg.npy", np.array(agg_features))
    np.save(input_dir / "y.npy", np.array(labels))

    print("[INFO] Dataset built successfully.")

if __name__ == "__main__":
    main()