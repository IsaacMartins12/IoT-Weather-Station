import network
import time
import dht
import ujson
from umqtt.simple import MQTTClient
import time
import ntptime
import machine

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "wokwi-weather"

sensor = dht.DHT22(machine.Pin(15))

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Connected!")

prev_weather = ""

while True:
    try:
        print("Measuring weather conditions... ", end="")
        sensor.measure()
        message = ujson.dumps({
            "temp": sensor.temperature(),
            "humidity": sensor.humidity(),
        })
        if message != prev_weather:
         print("Updated!")
         print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
         client.publish(MQTT_TOPIC, message)
         prev_weather = message
        else:
            print("No change")
        time.sleep(0.5)
    except OSError as e:
        print("Error: ", e)
        print("Reconnecting to MQTT server...")
        client.connect()
        print("Reconnected!")
    except Exception as e:
        print("Unexpected error: ", e)
        time.sleep(5)
