#!/usr/bin/env python3
"""
train_cnn.py

Purpose:
    Train a simple 1D CNN on packet‑sequence features.

Usage:
    python train_cnn.py --data data/processed
"""

import argparse
import numpy as np
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

def build_cnn(input_length, num_classes):
    model = models.Sequential([
        layers.Conv1D(32, 5, activation="relu", input_shape=(input_length, 1)),
        layers.MaxPooling1D(2),
        layers.Conv1D(64, 5, activation="relu"),
        layers.GlobalMaxPooling1D(),
        layers.Dense(128, activation="relu"),
        layers.Dense(num_classes, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed")
    args = parser.parse_args()

    X = np.load(f"{args.data}/X_seq.npy")
    y = np.load(f"{args.data}/y.npy")

    X = X[..., None]  # add channel dimension
    num_classes = len(set(y))
    input_length = X.shape[1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y
    )

    model = build_cnn(input_length, num_classes)
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

    loss, acc = model.evaluate(X_test, y_test)
    print(f"[RESULT] CNN accuracy: {acc:.3f}")

if __name__ == "__main__":
    main()