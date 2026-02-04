#!/usr/bin/env python3
"""
realtime_demo.py

Purpose:
    Controlled demonstration of a classifier running on the team's
    own Tor client. Buffers packets in real time and predicts the
    visited site.

Ethical Constraints:
    - Only monitors the local machine.
    - Only for demonstration, not deployment.

Usage:
    python realtime_demo.py --model models/saved/cnn.h5
"""

import argparse
import time
import numpy as np
from utils.pcap_utils import live_capture_buffer
from tensorflow.keras.models import load_model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    model = load_model(args.model)

    print("[INFO] Starting controlled real‑time demo...")

    while True:
        seq = live_capture_buffer(num_packets=3000)
        seq = np.array(seq)[None, :, None]

        preds = model.predict(seq)
        label = np.argmax(preds)

        print(f"[PRED] Site ID: {label}  (confidence {preds[0][label]:.2f})")
        time.sleep(1)

if __name__ == "__main__":
    main()