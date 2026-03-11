# GitHub Copilot Instructions - Open Vistar DAQ

You are an expert developer working on the **Open Vistar DAQ** project, a real-time cosmic ray visualization dashboard mimicking the CERN Vistar LHC Page 1 layout.

## Project Architecture
- **Backend**: FastAPI (Python 3.13) using `uv` for dependency management. MQTT subscriber for data ingestion, InfluxDB for time-series storage.
- **Frontend**: React (TypeScript) with Tailwind CSS and Apache ECharts. Vite as the build tool, Vitest for testing.
- **Hardware**: Open hardware (CERN-OHL-W-2.0) based on Arduino Nano and SiPM sensors.
- **Infrastructure**: Docker Compose for local orchestration (Mosquitto, InfluxDB, Backend, Frontend).

## Code Style & Principles
- **Library-First**: Core logic should be modular and testable.
- **Test-First**: Write tests before implementation (PyTest for Backend, Vitest for Frontend).
- **Simplicity**: Avoid over-engineering. YAGNI.
- **Anti-Abstraction**: Use framework features directly without thin wrappers.
- **GitHub-First**: Follow GitHub Flow (main + feature branches).

## Contextual Guidance
- When writing backend code, prioritize Pydantic models for data validation.
- When writing frontend code, use Tailwind for styling and ensure ECharts configurations match the classic CERN Vistar look (green text on black background, step-line charts).
- Always include appropriate license headers: MIT for software, CERN-OHL-W-2.0 for hardware.
