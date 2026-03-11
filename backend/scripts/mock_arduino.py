import os
import json
import time
import random
import paho.mqtt.client as mqtt
from datetime import datetime

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = 1883
TOPIC = "daq/events"

client = mqtt.Client()

def simulate_events():
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    print(f"Starting mock_arduino.py on {MQTT_HOST}:{MQTT_PORT}")
    
    while True:
        # Simulate Poisson process (avg 1 event per sec)
        time.sleep(random.expovariate(1.0))
        
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "device_id": "detector-01",
            "ch1_mv": random.uniform(50, 500),
            "ch2_mv": random.uniform(50, 500),
            "energy_gev": random.uniform(1.0, 7000.0)
        }
        
        payload = json.dumps(event)
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")

if __name__ == "__main__":
    try:
        simulate_events()
    except KeyboardInterrupt:
        print("Stopping simulation")
