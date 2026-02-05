# Threat Model

## Adversary
A passive local observer who can see Tor TLS packet metadata (size, direction, timing) but cannot decrypt traffic.

## Capabilities
- Observe packet headers
- Measure timing and direction
- Perform offline ML classification

## Limitations
- No payload access
- No active attacks
- No global visibility
- Only closed‑world classification

## Ethical Constraints
All traffic is self‑generated. No third‑party traffic is captured or analyzed.