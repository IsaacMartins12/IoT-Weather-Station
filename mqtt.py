import paho.mqtt.client as mqtt
import json
from database import Database

class Mqtt:

    def __init__(self, broker, port, topic):
        self.MQTT_BROKER = broker
        self.MQTT_PORT = int(port)
        self.MQTT_TOPIC = topic
        self.client = mqtt.Client()
        self.database = Database()

    def init_mqtt(self):
        # MQTT Client configuration
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect the MQTT Broker
    
        self.client.connect(self.MQTT_BROKER, self.MQTT_PORT, 60)

    # Callback when estabilized connection
    def on_connect(self, client, userdata, flags, rc):
        print(f"Conectado com código de resultado {rc}")
        # Subscrive in topic
        self.client.subscribe(self.MQTT_TOPIC)

    # Callback when a received mensage
    def on_message(self, client, userdata, msg):
        print(f"Received message in the topic '{msg.topic}': {msg.payload.decode()}")

        try:
            data = json.loads(msg.payload.decode())
            # Inserir os dados no banco de dados
            self.database.insert_data(data)
        except json.JSONDecodeError:
            print("Error decoding JSON")

    def start(self):
        
        try :
           self.client.loop_forever()
        except ValueError as e:
            print(f"Value Error: {e}")
        except Exception as e:
            print(f"Broker connection error: {e}")
