import unittest
from unittest.mock import MagicMock, patch
from src.ingestion.mqtt_client import MQTTClient

class TestMQTTClient(unittest.TestCase):
    @patch('paho.mqtt.client.Client')
    def test_init(self, mock_paho_client):
        client = MQTTClient(host="mqtt.example.com", port=1883)
        self.assertEqual(client.host, "mqtt.example.com")
        self.assertEqual(client.port, 1883)
        mock_paho_client.assert_called_once()

    @patch('paho.mqtt.client.Client')
    def test_on_connect(self, mock_paho_client):
        client = MQTTClient()
        mock_client = MagicMock()
        client.on_connect(mock_client, None, None, 0)
        mock_client.subscribe.assert_called_with("daq/events")

    @patch('paho.mqtt.client.Client')
    def test_on_message(self, mock_paho_client):
        client = MQTTClient()
        callback = MagicMock()
        client.set_callback(callback)
        
        mock_msg = MagicMock()
        mock_msg.payload = b'{"test": "data"}'
        mock_msg.topic = "daq/events"
        
        client.on_message(None, None, mock_msg)
        callback.assert_called_with(b'{"test": "data"}')
