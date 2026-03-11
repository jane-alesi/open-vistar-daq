# Research: Open Vistar DAQ

## Unknowns & Risks

1. **InfluxDB-FastAPI Integration**: Optimal way to handle high-frequency MQTT ingest while FastAPI provides an API for historical queries.
2. **ECharts Real-time performance**: Handling 100Hz updates in React without memory leaks or UI jank.
3. **CERN Open Data Alignment**: Specific JSON models for LHC Page 1 visualization.

## Findings

### 1. High-Frequency Ingest (InfluxDB)
- **Recommendation**: Use InfluxDB 2.x `WriteApi` with batching enabled. FastAPI should run in a separate process or use `asyncio` to avoid blocking during ingestion.
- **Reference**: [InfluxDB Python Client Documentation](https://github.com/influxdata/influxdb-client-python)

### 2. Real-time Visualization (ECharts)
- **Recommendation**: Use `setOption` with `notMerge: false` and `lazyUpdate: true` for incremental updates. Buffer updates to 10-20Hz instead of 100Hz if UI starts to lag.
- **Reference**: [Apache ECharts Real-time Data Tutorial](https://echarts.apache.org/en/tutorial.html#Dynamic%20Data)

### 3. LHC Page 1 UI
- **Replication**: Colors (Black background, Yellow/Cyan/White text), Layout (Grid of charts and status panels), Font (Monospace for metrics).
- **Reference**: [CERN Vistar Public Displays](https://op-vistar-plan.web.cern.ch/vistar/vistar.php?vistar=LHC1)

## Decisions

- **MQTT Broker**: Eclipse Mosquitto (Standard, Lightweight).
- **Backend**: FastAPI with `paho-mqtt` running in a background task.
- **Frontend**: React + Vite for performance.
- **Visualization**: Apache ECharts over Canvas for the complex LHC-style charts.
- **Simulation**: A separate Python script (`mock_arduino.py`) will simulate the Poisson process for cosmic ray events.
