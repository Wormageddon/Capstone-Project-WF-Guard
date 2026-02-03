# Capstone-Project-WF-Guard
This is the Capstone Project for Julian, Connor, Hunter, Josiah. Website Fingerprinting on Tor — Research Sandbox This repository contains a controlled, lab‑only exploration of website‑fingerprinting attacks and defenses on the Tor anonymity network. The project demonstrates technical proficiency in data collection, traffic preprocessing, machine‑learning classification, and privacy‑preserving countermeasures. All experiments are performed exclusively on self‑generated traffic in a closed‑world environment. No third‑party traffic is ever captured or analyzed. This project is intended for educational and research purposes only. Project Overview This work implements:

    A reproducible offline data‑collection pipeline using Tor
    Feature extraction from packet‑level traffic
    Classical and deep‑learning classifiers for closed‑world website identification
    A controlled “real‑time” demonstration on the team’s own Tor client
    Defensive techniques such as padding, timing jitter, and traffic morphing
    Evaluation of how these defenses degrade classifier performance The goal is to understand both the feasibility and the limitations of website fingerprinting, and to explore practical defenses that improve user privacy.

Ethical Use This repository operates under a strict ethical framework. Please read ETHICS.md before using any code in this project.