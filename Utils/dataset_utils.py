"""
dataset_utils.py

Purpose:
    Helper functions for dataset management:
    - Train/val/test splits
    - Shuffling
    - Label mapping

Notes:
    These utilities keep scripts clean and modular.
"""

import numpy as np
from sklearn.model_selection import train_test_split

def split_dataset(X, y, test_size=0.2, val_size=0.1):
    """
    Split dataset into train/val/test sets.

    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test
    """
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=test_size + val_size, stratify=y
    )

    relative_val_size = val_size / (test_size + val_size)

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=relative_val_size, stratify=y_temp
    )

    return X_train, X_val, X_test, y_train, y_val, y_test