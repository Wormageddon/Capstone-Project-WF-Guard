#!/usr/bin/env python3
"""
collect_traces.py

Purpose:
    Automates controlled, self‑traffic data collection through Tor.
    Visits a list of monitored sites, captures packet traces, and
    stores pcaps + metadata for later preprocessing.

Ethical Constraints:
    - Only collects traffic from the local machine.
    - Only visits sites defined in config/sites.csv.
    - Never captures third‑party traffic.

Usage:
    python collect_traces.py --output data/raw --trials 20
"""

import argparse
import time
import subprocess
from pathlib import Path
import pandas as pd

def load_sites(csv_path: str):
    """Load monitored site list from sites.csv."""
    return pd.read_csv(csv_path)

def start_capture(output_file: Path, interface: str):
    """Start tcpdump capture as a subprocess."""
    cmd = [
        "tcpdump",
        "-i", interface,
        "-w", str(output_file),
        "tcp port 9001 or tcp port 443"
    ]
    return subprocess.Popen(cmd)

def stop_capture(proc):
    """Stop tcpdump capture."""
    proc.terminate()
    proc.wait()

def visit_site(url: str):
    """Open the URL through Tor using a browser or curl."""
    # Placeholder: you will implement Selenium or curl here.
    print(f"[INFO] Visiting {url}")
    time.sleep(10)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sites", default="config/sites.csv")
    parser.add_argument("--output", default="data/raw")
    parser.add_argument("--interface", default="any")
    parser.add_argument("--trials", type=int, default=5)
    args = parser.parse_args()

    sites = load_sites(args.sites)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    for _, row in sites.iterrows():
        site_id = row["id"]
        url = row["url"]

        site_dir = output_dir / f"site_{site_id:02d}"
        site_dir.mkdir(exist_ok=True)

        for trial in range(args.trials):
            pcap_path = site_dir / f"{site_id}_trial_{trial}.pcap"
            print(f"[INFO] Collecting trace: {pcap_path}")

            proc = start_capture(pcap_path, args.interface)
            visit_site(url)
            stop_capture(proc)

            time.sleep(3)

if __name__ == "__main__":
    main()