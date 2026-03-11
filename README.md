# Open Vistar DAQ

**Democratizing High-Energy Physics Visualization**

Open Vistar DAQ is an open-source project that allows students and educators to build their own cosmic ray detectors and visualize coincidence events in a professional-grade interface (LHC Page 1 style).

## Architecture
- **Hardware**: Arduino-based DAQ shield with SiPM sensors (CERN-OHL-W-2.0).
- **Backend**: FastAPI with MQTT ingestion and InfluxDB persistence (MIT).
- **Frontend**: React and Apache ECharts (MIT).

## Quickstart

1. Start infrastructure: `docker-compose up -d`
2. Run simulation: `python backend/scripts/mock_arduino.py`
3. View UI: `http://localhost:3000`

## Licenses
- Software: [MIT](LICENSE.software)
- Hardware: [CERN-OHL-W-2.0](LICENSE.hardware)
