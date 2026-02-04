Script_Use_README.md
Website Fingerprinting Research — Script Usage Guide
This document explains every script in the repository, why it exists, and exactly how to use it.
If you forget the entire project tomorrow, reading this file will restore your full workflow.

1. Overview: How the Pipeline Works
Your project follows a strict, linear pipeline:
- Collect Tor traffic → raw .pcap files
- Preprocess pcaps → structured packet sequences
- Build dataset → NumPy arrays for ML
- Train models → baseline + CNN
- Apply defenses → padding, jitter, morphing
- Run real‑time demo → controlled, self‑traffic only
Each script corresponds to one stage.

2. Script‑by‑Script Breakdown

collect_traces.py
Purpose
This script collects raw Tor traffic by visiting websites through Tor and capturing packets with tcpdump.
Why it matters
This is the foundation of your dataset.
Without pcaps, nothing else in the pipeline works.
What it does
- Reads config/sites.csv
- For each site:
- Opens the site through Tor
- Captures packets
- Saves .pcap files in data/raw/site_xx/
How to use it
python scripts/collect_traces.py --output data/raw --trials 20


Output
data/raw/
    site_01/
        01_trial_0.pcap
        01_trial_1.pcap
        ...



preprocess_pcap.py
Purpose
Converts raw .pcap files into structured packet sequences.
Why it matters
Machine learning models cannot use raw pcaps.
This script extracts:
- packet direction (+1 / −1)
- packet size
- timestamp
How to use it
python scripts/preprocess_pcap.py --input data/raw --output data/processed


Output
data/processed/
    01_trial_0.json
    01_trial_1.json


Each JSON contains a list of packet events.

build_dataset.py
Purpose
Turns preprocessed JSON files into NumPy arrays for ML training.
Why it matters
This is the bridge between “network data” and “machine learning data.”
What it produces
- X_seq.npy — sequence features for CNN
- X_agg.npy — aggregate features for classical ML
- y.npy — labels
How to use it
python scripts/build_dataset.py --input data/processed


Output
data/processed/X_seq.npy
data/processed/X_agg.npy
data/processed/y.npy



train_baseline.py
Purpose
Trains classical ML models (Random Forest, SVM) on aggregate features.
Why it matters
This gives you:
- A sanity check
- A baseline accuracy
- A way to confirm your dataset is valid
If this model performs near random chance, something upstream is broken.
How to use it
python scripts/train_baseline.py --data data/processed


Output
Terminal printout:
[RESULT] Baseline accuracy: 0.74



train_cnn.py
Purpose
Trains a 1D CNN on packet‑sequence features.
Why it matters
This is your main attack model.
Deep learning typically outperforms classical ML in website fingerprinting.
How to use it
python scripts/train_cnn.py --data data/processed


Output
- Model accuracy
- Saved model file (if you add saving logic)

evaluate_defenses.py
Purpose
Applies defensive transformations to your dataset:
- Padding
- Timing jitter
- Traffic morphing (optional)
Why it matters
This is where you break your own attack and demonstrate:
- How defenses reduce accuracy
- How privacy can be preserved
How to use it
python scripts/evaluate_defenses.py --data data/processed


Output
Defended datasets (in memory or saved if you extend the script).

realtime_demo.py
Purpose
Runs a controlled, ethical demonstration of the attack:
- Listens to your own Tor interface
- Buffers the first N packets
- Runs your trained CNN
- Prints predicted site label
Why it matters
This is your “wow factor” demo — but still safe and ethical.
How to use it
python scripts/realtime_demo.py --model models/saved/cnn.h5


Output
[PRED] Site ID: 3 (confidence 0.82)



3. Full Pipeline Summary (Print This Out)
If you forget everything, run these in order:
Step 1 — Collect data
python scripts/collect_traces.py


Step 2 — Preprocess pcaps
python scripts/preprocess_pcap.py


Step 3 — Build dataset
python scripts/build_dataset.py


Step 4 — Train baseline
python scripts/train_baseline.py


Step 5 — Train CNN
python scripts/train_cnn.py


Step 6 — Evaluate defenses
python scripts/evaluate_defenses.py


Step 7 — Run real‑time demo
python scripts/realtime_demo.py



4. Why This Pipeline Matters
This structure demonstrates:
- Understanding of Tor traffic
- Data engineering
- Feature extraction
- Classical ML
- Deep learning
- Privacy defenses
- Ethical research practices
- Real‑time inference
It’s a complete, end‑to‑end research project.