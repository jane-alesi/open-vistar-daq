import pytest
import json
from datetime import datetime
from src.models.events import CoincidenceEvent

def test_mock_ingestion_flow():
    # Simulate data received from MQTT
    mock_payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": "detector-01",
        "ch1_mv": 120.5,
        "ch2_mv": 98.2,
        "energy_gev": 500.0
    }
    
    # Validate it can be parsed by our model
    event = CoincidenceEvent(**mock_payload)
    
    assert event.device_id == "detector-01"
    assert event.ch1_mv == 120.5
    assert event.energy_gev == 500.0
