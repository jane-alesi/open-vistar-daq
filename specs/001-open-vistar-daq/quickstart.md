# Quickstart: Open Vistar DAQ

## Development Setup

1. **Install Prerequisites**: `docker`, `docker-compose`, `python 3.12+`.
2. **Start Infrastructure**:
   ```bash
   docker-compose up -d
   ```
3. **Start Simulator**:
   ```bash
   python backend/scripts/mock_arduino.py
   ```
4. **Access UI**:
   - URL: `http://localhost:3000`
   - You should see the LHC Page 1 visualization updating in real-time.

## Verification Scenarios

### 1. Ingestion Verification
- **Action**: Check Mosquitto logs: `docker logs mosquitto`.
- **Expected**: Payload received on `daq/events` topic.

### 2. Storage Verification
- **Action**: Query InfluxDB: `docker exec influxdb influx query 'from(bucket:"daq_events") |> range(start:-1m)'`.
- **Expected**: Recent coincidence events returned.

### 3. UI Verification
- **Action**: Inspect React frontend.
- **Expected**: ECharts showing Intensity peaks and Energy distributions. Status should be "BEAM ON".
