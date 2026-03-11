# Tasks: Open Vistar DAQ

**Input**: Design documents from `specs/001-open-vistar-daq/`
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `quickstart.md`

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create project structure (backend, frontend, hardware, docker) per `plan.md`
- [X] T002 [P] Initialize Python backend project with FastAPI and Paho-MQTT
- [X] T003 [P] Initialize React frontend project with Vite and Tailwind CSS
- [ ] T004 Create `docker-compose.yml` with Mosquitto, InfluxDB, Backend, and Frontend services

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T005 [P] Setup InfluxDB initialization script (buckets: `daq_events`, `daq_metrics`)
- [X] T006 Implement base Pydantic models in `backend/src/models/events.py`
- [X] T007 Setup MQTT client wrapper in `backend/src/ingestion/mqtt_client.py`
- [ ] T008 Setup InfluxDB client wrapper in `backend/src/ingestion/influx_client.py`
- [X] T025 Setup Frontend Integration testing environment (Vitest + RTL) in `frontend/src/tests/`

**Checkpoint**: Foundation ready - user story implementation can now begin.

## Phase 3: User Story 1 - Real-time Cosmic Ray Visualization (Priority: P1) 🎯 MVP

**Goal**: Real-time visualization of coincidence events in LHC Page 1 style.

### Tests for User Story 1
- [X] T009 [P] [US1] Create `backend/scripts/mock_arduino.py` to simulate Poisson-distributed events
- [X] T010 [US1] Integration test for MQTT-to-InfluxDB flow in `backend/tests/integration/test_ingestion.py`
- [X] T026 [US1] Integration test for frontend dashboard presence in `frontend/src/tests/integration/App.test.tsx`

### Implementation for User Story 1
- [ ] T011 [US1] Implement MQTT subscriber in `backend/src/ingestion/subscriber.py`
- [ ] T012 [US1] Implement InfluxDB writer in `backend/src/ingestion/writer.py`
- [ ] T013 [P] [US1] Create ECharts component wrapper in `frontend/src/components/VistarChart.tsx`
- [ ] T014 [US1] Implement "LHC Page 1" layout in `frontend/src/App.tsx`
- [ ] T015 [US1] Connect frontend to real-time data source (Polling or WebSocket)

**Checkpoint**: MVP Ready - Simulated events visualized in real-time.

## Phase 4: User Story 2 - Data Acquisition & Storage (Priority: P2)

**Goal**: Persistence and retrieval of historical cosmic ray data.

### Implementation for User Story 2
- [ ] T016 [US1] Implement FastAPI endpoint `GET /events` for historical data in `backend/src/api/events.py`
- [ ] T017 [US2] Implement FastAPI endpoint `GET /metrics/summary` in `backend/src/api/metrics.py`
- [ ] T018 [US2] Add historical data view/toggle to the frontend

**Checkpoint**: User Story 2 complete - Historical data can be queried and viewed.

## Phase 5: User Story 3 - DIY Hardware Integration (Priority: P3)

**Goal**: Open-source hardware designs for the DAQ shield.

### Implementation for User Story 3
- [ ] T019 [US3] Create KiCad project structure in `hardware/kicad/`
- [ ] T020 [US3] Draft BOM (Bill of Materials) in `hardware/BOM.md`
- [ ] T021 [US3] Add Arduino Nano firmware for coincidence detection in `hardware/arduino/daq_firmware.ino`

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T022 [P] Add MIT and CERN-OHL-W-2.0 license headers to all files
- [ ] T023 [P] Update `README.md` with architecture and quickstart instructions
- [ ] T024 Final validation using `quickstart.md` scenarios

## Dependencies & Execution Order

1. **Setup (Phase 1)** -> **Foundational (Phase 2)** (Sequential)
2. **User Story 1 (Phase 3)** (Priority P1, MVP)
3. **User Story 2 (Phase 4)** (Depends on US1 data structures)
4. **User Story 3 (Phase 5)** (Hardware focus, can run in parallel with software tasks)
5. **Polish (Phase 6)** (Final gate)
