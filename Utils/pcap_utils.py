"""
pcap_utils.py

Purpose:
    Provide helper functions for reading and parsing packet capture (pcap)
    files in a controlled, ethical, self-traffic-only environment.

Notes:
    - These functions DO NOT capture traffic.
    - They only parse pcaps already collected by collect_traces.py.
    - Real parsing logic can be added later using pyshark or scapy.
"""

from typing import List, Dict

def parse_pcap(pcap_path: str) -> List[Dict]:
    """
    Parse a pcap file and extract packet metadata.

    Returns:
        A list of dictionaries, each representing a packet:
        {
            "direction": +1 or -1,
            "size": int,
            "timestamp": float
        }

    Current behavior:
        Placeholder implementation returning mock data.
        Replace with real parsing logic later.
    """
    # Placeholder: return a tiny synthetic sequence
    return [
        {"direction": 1, "size": 512, "timestamp": 0.01},
        {"direction": -1, "size": 1024, "timestamp": 0.05},
        {"direction": 1, "size": 256, "timestamp": 0.09},
    ]


def live_capture_buffer(num_packets: int = 3000) -> List[int]:
    """
    Placeholder for real-time packet buffering.

    Returns:
        A synthetic sequence of packet sizes for testing the pipeline.

    Notes:
        - This does NOT capture real traffic.
        - It allows realtime_demo.py to run safely during development.
    """
    return [100] * num_packets