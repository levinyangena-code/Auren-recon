# Auren Recon

Auren Recon is a Python CLI for orchestrating Bluetooth security research tooling in a controlled, authorized workflow. It is designed to invoke external, separately-installed tools rather than bundling or reimplementing attack logic.

This project orchestrates:
- BlueToolkit
- Crackle
- BLERP

It is intended for lawful, authorized security testing and defensive validation only.

Important legal notice

This project is for authorized testing only. You must own the target device or have written authorization from the owner before testing it.
Unauthorized Bluetooth testing is unlawful and unethical.
This repository does not include exploit payloads or attack code. It only calls existing external tools that must be installed separately.

Project purpose

Auren Recon provides a structured workflow for:
- verifying tool availability
- enforcing legal authorization before running against a target
- running Bluetooth reconnaissance and scanning against an authorized target
- capturing BLE traffic to a `.pcap`
- passing capture evidence into Crackle for TK/LTK analysis
- running BLERP re-pairing workflows when explicitly authorized
- aggregating results into a Markdown report

Repository structure

```text
auren-recon/
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── README.md
├── requirements.txt
├── config.yaml
├── btrecon.py
├── modules/
│   ├── __init__.py
│   ├── bluetoolkit.py
│   ├── crackle.py
│   ├── blerp.py
│   ├── capture.py
│   └── report.py
├── utils/
│   ├── __init__.py
│   ├── deps.py
│   ├── legal.py
│   └── logging.py
├── tests/
│   ├── mock-tools/
│   │   ├── btmon
│   │   ├── hcidump
│   │   ├── crackle
│   │   ├── bluetoolkit
│   │   └── blerp
│   └── mock_data/
│       └── mock_ble_capture.pcap
└── sessions/
