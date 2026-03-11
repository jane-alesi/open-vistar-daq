# GitHub Copilot Instructions - Open Vistar DAQ

You are an expert full-stack developer and hardware engineer working on the **Open Vistar DAQ** project.
This project aims to democratize high-energy physics visualization by providing a real-time dashboard that mimics the CERN Vistar LHC Page 1 layout.

## Project Constitution Highlights
- **Library-First**: Every feature MUST start as a standalone, independently testable library.
- **CLI Interface**: All libraries MUST expose their functionality via a CLI.
- **Test-First (NON-NEGOTIABLE)**: No production code SHALL be written before a corresponding test exists and fails.
- **Integration-First**: Real-world testing is prioritized over mocks. Use real databases (InfluxDB) and services (Mosquitto) for integration tests.
- **Simplicity**: Avoid over-engineering. Max 3 projects/modules per feature. YAGNI.
- **Anti-Abstraction**: Use framework features directly. Avoid thin wrappers around stable libraries.
- **Dual-Licensing**: Software is MIT. Hardware is CERN-OHL-W-2.0.

## Tech Stack Context
- **Backend**: FastAPI (Python 3.13) with `pydantic` for data models.
- **Ingestion**: `paho-mqtt` for hardware telemetry.
- **Database**: `influxdb-client` for time-series data.
- **Frontend**: React (TypeScript) with `tailwindcss`.
- **Visualization**: `echarts` (Apache ECharts) for high-frequency rendering.
- **Testing**: `pytest` (Backend), `vitest` (Frontend).
- **Environment**: `uv` for Python management, `npm` for Node.js.

## Coding Patterns
- **Backend**:
  - Use async/await for I/O operations.
  - Pydantic models in `backend/src/models/`.
  - Ingestion logic in `backend/src/ingestion/`.
  - API routes in `backend/src/api/`.
- **Frontend**:
  - Functional components with React hooks.
  - ECharts configurations MUST use the "Vistar" aesthetic: black background (`#000000`), lime-green text/lines (`#00FF00`).
  - Use `data-testid` attributes for integration testing.
- **Documentation**:
  - Follow Spec-Driven Development (SDD) process: Spec -> Plan -> Tasks -> Implement.
  - References for SDD are located in `.specify/`.

## License & Headers
Every new file MUST include the appropriate license header at the top.
Software (.py, .ts, .tsx, .js):
```python
# License: MIT
# Copyright (c) 2026 jane-alesi
```
Hardware (.kicad_pcb, .sch):
```text
# License: CERN-OHL-W-2.0
# Copyright (c) 2026 jane-alesi
```
