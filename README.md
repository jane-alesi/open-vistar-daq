# Open Vistar DAQ

**Democratizing High-Energy Physics Visualization**

Open Vistar DAQ is an open-source project that allows students and educators to build their own cosmic ray detectors and visualize coincidence events in a professional-grade interface (LHC Page 1 style).

[![Quality Checks](https://github.com/jane-alesi/open-vistar-daq/actions/workflows/quality.yml/badge.svg)](https://github.com/jane-alesi/open-vistar-daq/actions/workflows/quality.yml)
[![CodeQL](https://github.com/jane-alesi/open-vistar-daq/actions/workflows/security.yml/badge.svg)](https://github.com/jane-alesi/open-vistar-daq/actions/workflows/security.yml)

## Architecture
- **Hardware**: Arduino-based DAQ shield with SiPM sensors (CERN-OHL-W-2.0).
- **Backend**: FastAPI with MQTT ingestion and InfluxDB persistence (MIT).
- **Frontend**: React and Apache ECharts (MIT).

## Quickstart

1. Clone the repository: `git clone https://github.com/jane-alesi/open-vistar-daq.git`
2. Start infrastructure: `docker-compose up -d`
3. Run simulation: `python backend/scripts/mock_arduino.py`
4. View UI: `http://localhost:3000`

## Development

We follow **GitHub Flow** (main + feature branches) and the **Spec-Driven Development** (SDD) workflow. All changes must pass CI/CD quality gates before merging.

## Licenses
- Software: [MIT](LICENSE.software)
- Hardware: [CERN-OHL-W-2.0](LICENSE.hardware)
