project_name: Auren Recon
authorized_target:
  name: "Example authorized device"
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
