from datetime import datetime
from src.models.events import CoincidenceEvent, VistarState

def test_coincidence_event_creation():
    now = datetime.utcnow()
    event = CoincidenceEvent(
        timestamp=now,
        device_id="test-device",
        ch1_mv=100.5,
        ch2_mv=200.5,
        energy_gev=3500.0
    )
    assert event.timestamp == now
    assert event.device_id == "test-device"
    assert event.ch1_mv == 100.5
    assert event.energy_gev == 3500.0

def test_vistar_state_defaults():
    state = VistarState()
    assert state.status == "NO BEAM"
    assert state.intensity == 0.0
    assert state.last_update is None
