import threading
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
from database import Database
from graphic import Graphic
from mqtt import Mqtt

# Carrega as variáveis do arquivo .env
load_dotenv()

# Agora você pode acessar as variáveis de ambiente
DB_NAME = os.getenv('DB_NAME')
MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_TOPIC = os.getenv('MQTT_TOPIC')

if __name__ == "__main__":

    database_instance = Database()
    database_instance.initialize_db()

    mqtt_instance = Mqtt(MQTT_BROKER,MQTT_PORT,MQTT_TOPIC)
    mqtt_instance.init_mqtt()

    graphic_instance = Graphic()

    mqtt_thread = threading.Thread(target=mqtt_instance.start)
    graphic_thread = threading.Thread(target=graphic_instance.start)

    mqtt_thread.start()
    graphic_thread.start()

    mqtt_thread.join()
    graphic_thread.join()