# Feature Specification: Open Vistar DAQ

**Feature Branch**: `001-open-vistar-daq`  
**Created**: 2026-03-11  
**Status**: Draft  
**Input**: User description: "AGENTIC EXECUTION PLAN: OPEN-VISTAR-DAQ"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Real-time Cosmic Ray Visualization (Priority: P1)

As a physics student or educator, I want to see real-time cosmic ray coincidence events visualized in a professional-grade interface (LHC Page 1 style), so that I can understand and observe particle physics phenomena locally.

**Why this priority**: This is the core value proposition of the project - democratizing high-energy physics visualization.

**Independent Test**: Can be tested using the `mock_arduino.py` emulator. The system should display Intensity, Energy, and Luminosity metrics based on simulated MQTT payloads.

**Acceptance Scenarios**:

1. **Given** the MQTT broker and backend are running, **When** the `mock_arduino.py` sends Poisson-distributed coincidence events, **Then** the React frontend should update the ECharts visualization with new data points within 500ms.
2. **Given** the frontend is open, **When** no MQTT data is received, **Then** the interface should show a "Waiting for Data" or "No Beam" status consistent with LHC Vistar styles.

---

### User Story 2 - Data Acquisition & Storage (Priority: P2)

As a researcher, I want my cosmic ray data to be stored in a time-series database, so that I can perform long-term analysis of coincidence rates and energy distributions.

**Why this priority**: Enables scientific utility beyond real-time observation.

**Independent Test**: Verify that data sent via MQTT is correctly ingested by the FastAPI backend and stored in InfluxDB.

**Acceptance Scenarios**:

1. **Given** a stream of simulated SiPM pulses, **When** data is ingested, **Then** it must be queryable from InfluxDB with accurate timestamps and amplitude values.

---

### User Story 3 - DIY Hardware Integration (Priority: P3)

As a maker, I want to build a DAQ shield using off-the-shelf components and open-source schematics, so that I can create a functional cosmic ray detector.

**Why this priority**: Lowers the barrier to entry for hardware experimentation.

**Independent Test**: Verify the existence and completeness of KiCad schematics and BOM in the repository. (Simulated in Phase 6).

**Acceptance Scenarios**:

1. **Given** the KiCad project, **When** inspected, **Then** it must contain the SiPM step-up converter and coincidence logic for Arduino Nano.

---

### Edge Cases

- What happens when the MQTT broker connection is lost?
- How does the system handle extremely high count rates (e.g., during testing or high-background environments)?
- How are invalid or malformed MQTT payloads handled by the ingestion script?

## Clarifications (Resolved)

1. **MQTT Payload Format**: `{"timestamp": <ISO8601>, "ch1_mv": <float>, "ch2_mv": <float>, "energy_gev": <float>}`. Matches CERN data patterns.
2. **Docker Hub Org**: `janealesi` (e.g., `janealesi/open-vistar-backend`).
3. **CERN API Alignment**: LHC Page 1 JSON model if available; standard ROOT-compatible time-series structures otherwise.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide an asynchronous FastAPI backend for MQTT data ingestion.
- **FR-002**: System MUST use Eclipse Mosquitto as the message broker for telemetry.
- **FR-003**: System MUST store metrics in InfluxDB for time-series analysis.
- **FR-004**: Frontend MUST replicate the LHC "Vistar" Page 1 UI layout.
- **FR-005**: Frontend MUST use Apache ECharts for high-frequency rendering of particle events.
- **FR-006**: System MUST include a Python-based serial emulator (`mock_arduino.py`) for testing.
- **FR-007**: Hardware designs MUST be provided in KiCad format and licensed under CERN-OHL-W-2.0.

### Key Entities

- **Event**: A single coincidence detection, characterized by timestamp, SiPM pulse amplitudes (mV), and calculated energy (GeV).
- **Metric**: Aggregated data such as Intensity (counts/sec), Energy (avg GeV), and Luminosity.
- **Device**: The DAQ shield/Arduino assembly providing the telemetry.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: End-to-end latency from hardware event (simulated) to UI update is less than 1 second.
- **SC-002**: System sustains a simulated count rate of 100 Hz without data loss in InfluxDB.
- **SC-003**: UI rendering remains fluid (at least 30 FPS) during high-frequency data bursts.
- **SC-004**: Project follows dual-licensing: MIT for code, CERN-OHL-W-2.0 for hardware.
