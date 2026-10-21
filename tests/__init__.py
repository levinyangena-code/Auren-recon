# Auren Recon

Auren Recon is a Python CLI for orchestrating Bluetooth security research tooling in a controlled, authorized workflow. It is designed to invoke external, separately-installed tools rather than embedding analysis or exploit logic in this repository.

This project orchestrates:
- BlueToolkit
- Crackle
- BLERP

It is intended for lawful, authorized security testing and defensive validation only.

## Legal notice

This project is for authorized testing only. You must own the target device or have written authorization from the owner before testing it.
Unauthorized Bluetooth testing is unlawful and unethical.
This repository does not include exploit payloads or attack code. It only calls existing external tools that must be installed separately.

## Purpose

Auren Recon provides a structured workflow for:
- verifying tool availability
- enforcing legal authorization before running against a target
- running Bluetooth reconnaissance and scanning against an authorized target
- capturing BLE traffic to a `.pcap`
- passing capture evidence into Crackle for TK/LTK analysis
- running BLERP re-pair workflows only when explicitly authorized
- aggregating results into a Markdown report

## Requirements

- Python 3.9+
- `pip` and a virtual environment
- external Bluetooth tooling installed separately
- a written authorization or ownership record for the target under test

## Installation

```bash
git clone https://github.com/levinyangena-code/Auren-recon.git
cd Auren-recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Install the required external tools separately and ensure each binary is available in your `PATH`.

## CLI usage

The project supports a small command set for validation, capture, and reporting:

```bash
python btrecon.py validate --config config.yaml
python btrecon.py capture --config config.yaml --demo
python btrecon.py report --config config.yaml --capture ./sessions/ble_capture.pcap
python btrecon.py workflow --config config.yaml --demo
```

### Commands

- `validate`: checks target authorization and required tools
- `capture`: executes the capture workflow
- `report`: writes a Markdown report for an existing capture
- `workflow`: runs validation, capture, and report generation in sequence

## Demo mode vs live mode

Demo mode exists for development and validation work. It generates placeholder capture and report output without depending on external Bluetooth hardware or tools.

Live mode should only be used when:
- the target is owned by you or explicitly authorized
- the required tools are installed and valid
- the workflow is being executed in a controlled environment
- the activity is consistent with policy and law

## Example workflow

1. Update `config.yaml` with a valid target and authorization file.
2. Validate the setup:
   ```bash
   python btrecon.py validate --config config.yaml
   ```
3. Test the workflow in demo mode:
   ```bash
   python btrecon.py workflow --config config.yaml --demo
   ```
4. Run the live workflow only in a properly authorized environment:
   ```bash
   python btrecon.py workflow --config config.yaml
   ```
5. Review the generated Markdown report in the configured output location.

## Example config

```yaml
project_name: Auren Recon
authorized_target:
  name: "Authorized test device"
  identifier: "AA:BB:CC:DD:EE:FF"
  owner: "Responsible operator or owner"
  authorization_file: ./sessions/authorization.txt
  authorized: true
capture:
  output_dir: ./sessions
  pcap_file: ./sessions/ble_capture.pcap
  duration_seconds: 30
  commands:
    - "echo 'simulated capture command'"
report:
  output_file: ./sessions/report.md
  title: "Auren Recon report"
tools:
  required:
    - btmon
    - hcidump
    - crackle
    - bluetoolkit
    - blerp
```

## Safety and ethics

This project should only be used when:
- the target belongs to you or you have written authorization from the owner
- the testing is consistent with local law, policy, and contractual obligations
- the workflow is occurring in a controlled research or defensive validation context

Do not use it on unauthorized devices. Do not use it for surveillance, evasion, or malicious activity.

## Repository structure

```text
auren-recon/
├── .gitignore
├── LICENSE
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
├── sessions/
│   ├── authorization.txt
│   └── .gitkeep
├── tests/
│   ├── test_cli.py
│   └── test_legal.py
└── .venv/
```

## Contributing

Contributions should preserve the safety-first workflow and improve validation. Proposed changes should include tests and documentation for new commands or configuration fields.

Included is some information about a GitHub repository and its language composition.
repo: levinyangena-code/Auren-recon
repo ID: 1428538109
The description for this repo is `BT-Recon — Bluetooth Security Testing Orchestrator`.
