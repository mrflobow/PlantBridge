import json
import paho.mqtt.client as mqtt
from plants.flowersensor import FlowerSensor

class Shovel:

    def __init__(self):
        with open('config.json') as configFile:
            self.config = json.load(configFile)

    
    def run(self):
        plants = []
        for plant in self.config.sensors:
            sensor = FlowerSensor(plant.name,plant.mac)
            sensor.poll()
            plants.append(sensor)
            
        mqttc = mqtt.Client("miflora")
        mqttc.username_pw_set(self.config.mqtt.user,self.config.mqtt.password)
        mqttc.connect(self.config.mqtt.host, 1883)
        
        for plant in plants:
            mqttc.publish("/plant/{}".format(plant.name),json.dumps(plant))
        mqttc.loop(2)
    