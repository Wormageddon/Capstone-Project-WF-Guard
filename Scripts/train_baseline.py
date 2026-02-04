#!/usr/bin/env python3
"""
train_baseline.py

Purpose:
    Train classical ML models (Random Forest, SVM) on aggregate features.

Usage:
    python train_baseline.py --data data/processed
"""

import argparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    args = parser.parse_args()

    X = np.load(f"{args.data}/X_agg.npy")
    y = np.load(f"{args.data}/y.npy")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y
    )

    clf = RandomForestClassifier(n_estimators=200)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"[RESULT] Baseline accuracy: {acc:.3f}")

if __name__ == "__main__":
    main()