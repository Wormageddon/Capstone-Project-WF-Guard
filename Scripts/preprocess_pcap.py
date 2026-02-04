#!/usr/bin/env python3
"""
preprocess_pcap.py

Purpose:
    Converts raw pcaps into structured packet sequences:
    - direction (+1 / -1)
    - packet size
    - timestamp (relative)

Output:
    Saves JSON or NumPy arrays into data/processed/.

Usage:
    python preprocess_pcap.py --input data/raw --output data/processed
"""

import argparse
from pathlib import Path
import json
from utils.pcap_utils import parse_pcap

def process_pcap(pcap_path: Path):
    """Extract features from a single pcap."""
    packets = parse_pcap(pcap_path)
    return packets

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw")
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    for site_dir in input_dir.iterdir():
        if not site_dir.is_dir():
            continue

        for pcap in site_dir.glob("*.pcap"):
            features = process_pcap(pcap)
            out_file = output_dir / f"{pcap.stem}.json"

            with open(out_file, "w") as f:
                json.dump(features, f)

            print(f"[INFO] Processed {pcap} → {out_file}")

if __name__ == "__main__":
    main()