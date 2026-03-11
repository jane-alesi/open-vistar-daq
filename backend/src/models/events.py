from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CoincidenceEvent(BaseModel):
    timestamp: datetime
    device_id: str
    ch1_mv: float
    ch2_mv: float
    energy_gev: float

class VistarState(BaseModel):
    status: str = "NO BEAM"
    intensity: float = 0.0
    energy: float = 0.0
    luminosity: float = 0.0
    last_update: Optional[datetime] = None
