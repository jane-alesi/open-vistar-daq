import os
import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MQTTClient:
    def __init__(self, host=None, port=1883):
        self.host = host or os.getenv("MQTT_HOST", "localhost")
        self.port = port
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
            client.subscribe("daq/events")
        else:
            logger.error(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        logger.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if self.callback:
            self.callback(msg.payload)

    def set_callback(self, callback):
        self.callback = callback

    def start(self):
        self.client.connect(self.host, self.port, 60)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
