# Auren Recon

Auren Recon is a Python CLI for orchestrating Bluetooth security research tooling in a controlled, authorized workflow. It is designed to invoke external, separately-installed tools rather than bundling attack or exploitation code into this repository.

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

## What this project does

Auren Recon is best understood as a workflow orchestrator and safety gate. It is not a standalone Bluetooth scanner or complete security toolkit by itself. Instead, it coordinates external tools that are installed in your environment and keeps the process focused on authorized, auditable research workflows.

Typical workflow:
1. Validate required tools are installed and executable.
2. Confirm that authorization is present and that the target is explicitly approved.
3. Run a reconnaissance or capture workflow against the approved target.
4. Save captured traffic to a `.pcap` file.
5. Send evidence to Crackle for TK/LTK analysis when applicable.
6. Optionally run BLERP re-pairing flows only when explicitly authorized.
7. Generate a Markdown report summarizing the actions and findings.

## Requirements

- Python 3.9+ recommended
- `pip` / virtual environment support
- External Bluetooth tools installed separately:
  - BlueToolkit
  - Crackle
  - BLERP
- A legal authorization record for the target under test

## Installation

Clone the repository:

```bash
git clone https://github.com/levinyangena-code/Auren-recon.git
cd Auren-recon
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

If the project requires external tools to be already present on your machine, install them separately according to the vendor instructions for each tool and ensure they are available in your `PATH`.

## Quick start

After installing dependencies and external tools, create a local `config.yaml` file based on the example below and run the CLI.

```bash
python btrecon.py --help
python btrecon.py --config config.yaml
```

## Example configuration

A sample configuration might look like this:

```yaml
# Example config.yaml
project_name: Auren Recon
authorized_target:
  name: "My authorized test device"
  identifier: "AA:BB:CC:DD:EE:FF"
  owner: "authorized owner or responsible operator"
  authorization_file: ./authorization.txt
capture:
  output_dir: ./sessions
  pcap_file: ./sessions/ble_capture.pcap
  duration_seconds: 60
report:
  output_file: ./sessions/report.md
```

This file is an example only. Use the project’s actual configuration fields and update them to match your environment and legal authorization requirements.

## CLI usage

The CLI is intended to support a controlled workflow with explicit approvals and tool checks before any active testing begins.

Common usage patterns:

```bash
python btrecon.py --config config.yaml
python btrecon.py --config config.yaml --target "AA:BB:CC:DD:EE:FF"
python btrecon.py --help
```

The exact flags and command syntax may vary depending on the current implementation of the project. Use `--help` to inspect the available options in your local version.

## Workflow overview

Auren Recon is designed to help you:
- verify that required external tools are available
- validate that the target has been explicitly authorized
- run BLE reconnaissance or capture only against approved targets
- save evidence in `.pcap` format
- analyze captured data with Crackle where appropriate
- generate a human-readable Markdown report for auditability

## Repository structure

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
```

## External tool integration

Auren Recon is intentionally designed to integrate with external tooling rather than include that functionality in this repository.

The project expects these tools to be installed and available on the system:
- BlueToolkit
- Crackle
- BLERP

If a dependency is missing, Auren Recon should fail early and clearly instead of proceeding with unauthorized or unsupported actions.

## Safety and ethics

This project should be used only in the following contexts:
- you own the device or system under test
- you have written permission from the owner or authorized operator
- your work is aligned with applicable laws, policies, and testing agreements

Do not use this project on third-party devices without explicit authorization. Do not use it for unauthorized surveillance, evasion, or malicious activity.

## Reporting and evidence

One of Auren Recon's goals is to make testing easier to document and review. It helps produce structured output that can be reviewed later, including:
- capture files such as `.pcap`
- result summaries
- analysis output from Crackle
- report artifacts in Markdown

## Contributing

Contributions are welcome if they improve the safety, reliability, and clarity of the project. Please keep the workflow lawful and clearly documented, and prefer changes that strengthen validation and authorization checks.

Before submitting changes:
- run the relevant tests
- verify that changes do not weaken legal safeguards
- document any new configuration or CLI behavior

## License

This project is distributed under the terms of the repository license. See `LICENSE` for details.

Included is some information about a GitHub repository and its language composition.
repo: levinyangena-code/Auren-recon
repo ID: 1428538109
The description for this repo is `BT-Recon — Bluetooth Security Testing Orchestrator`.
