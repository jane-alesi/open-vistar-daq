# Implementation Plan: Open Vistar DAQ

**Branch**: `001-open-vistar-daq` | **Date**: 2026-03-11 | **Spec**: `specs/001-open-vistar-daq/spec.md`
**Input**: Feature specification from `specs/001-open-vistar-daq/spec.md`

## Summary
The Open Vistar DAQ project aims to democratize particle physics by providing a real-time, professional-grade visualization interface (LHC Page 1 style) for DIY cosmic ray detectors. The technical approach involves a distributed architecture:
- **Hardware/Emulator**: Arduino-based DAQ or Python emulator sending Poisson-distributed event data via MQTT.
- **Backend**: FastAPI (Python) subscriber that ingests MQTT data and persists it to InfluxDB.
- **Frontend**: React-based "Vistar" dashboard using Apache ECharts for high-frequency data rendering.
- **Infrastructure**: Dockerized environment for seamless deployment of all components (Mosquitto, InfluxDB, Backend, Frontend).

## Technical Context

**Language/Version**: Python 3.12 (Backend), TypeScript/React 18+ (Frontend)
**Primary Dependencies**: FastAPI, Paho-MQTT, InfluxDB-client-python, Apache ECharts, Tailwind CSS
**Storage**: InfluxDB (Time-series)
**Testing**: PyTest (Backend), Vitest (Frontend), Playwright (E2E)
**Target Platform**: Linux/Docker
**Project Type**: Full-stack Web Application + IoT Integration
**Performance Goals**: <500ms end-to-end latency, 100Hz event handling, 30+ FPS UI rendering
**Constraints**: MIT License for code, CERN-OHL-W-2.0 for hardware
**Scale/Scope**: Educational/Research tool for secondary/tertiary physics

## Constitution Check

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Library-First | PASS | Backend ingestion and UI components will be modular. |
| II. CLI Interface | PASS | Backend will include a CLI for manual data injection/testing. |
| III. Test-First | PASS | TDD will be applied to ingestion logic and UI state transitions. |
| IV. Integration-First| PASS | Docker Compose will be used for full-system integration testing. |
| V. Simplicity | PASS | Minimalist architecture: Ingest -> Store -> Visualize. |
| VI. Anti-Abstraction | PASS | Direct use of FastAPI, ECharts, and InfluxDB APIs. |
| VII. Dual-Licensing | PASS | License headers and repo structure will reflect dual-licensing. |

## Project Structure

```text
backend/
├── src/
│   ├── ingestion/       # MQTT subscriber & InfluxDB writer
│   ├── api/             # FastAPI endpoints for historical data
│   ├── models/          # Pydantic models for events
│   └── cli/             # Admin/Test CLI tools
├── tests/
│   ├── integration/
│   └── unit/
├── Dockerfile
└── requirements.txt

frontend/
├── src/
│   ├── components/      # ECharts wrappers, Vistar panels
│   ├── hooks/           # WebSocket/Polling for real-time data
│   ├── services/        # API client for backend
│   └── App.tsx
├── tests/
├── Dockerfile
└── package.json

hardware/
├── kicad/               # DAQ Shield schematics & PCB
├── arduino/             # DAQ firmware
└── LICENSE.hardware     # CERN-OHL-W-2.0

docker-compose.yml
README.md
LICENSE.software         # MIT
```

**Structure Decision**: Option 2 (Web application) with an additional `hardware/` directory for CERN-OHL components.

## Complexity Tracking
*No violations detected.*
