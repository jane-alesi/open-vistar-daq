# Data Model: Open Vistar DAQ

## InfluxDB Buckets

- **`daq_events`**: Raw coincidence events.
- **`daq_metrics`**: Aggregated metrics (Intensity, Avg Energy).

## Entities

### 1. Raw Event (`daq_events`)
- **Measurement**: `coincidence`
- **Tags**: 
    - `device_id`: ID of the detector.
- **Fields**: 
    - `ch1_mv`: Pulse amplitude channel 1 (float).
    - `ch2_mv`: Pulse amplitude channel 2 (float).
    - `energy_gev`: Calculated energy (float).
- **Precision**: Nanoseconds.

### 2. Aggregated Metric (`daq_metrics`)
- **Measurement**: `summary`
- **Tags**: 
    - `device_id`: ID of the detector.
- **Fields**: 
    - `intensity`: Counts per second (float).
    - `avg_energy_gev`: Average energy (float).
    - `luminosity`: Relative luminosity metric (float).

## API Models (FastAPI/Pydantic)

```python
class CoincidenceEvent(BaseModel):
    timestamp: datetime
    device_id: str
    ch1_mv: float
    ch2_mv: float
    energy_gev: float

class VistarState(BaseModel):
    status: str # e.g., "BEAM ON", "NO BEAM"
    intensity: float
    energy: float
    luminosity: float
    last_update: datetime
```
