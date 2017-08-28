from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY


class FlowerSensor:
    
    def __init__(self,name,mac):
        self.name = name
        self.mac = mac
        self.temp = 0
        self.light = 0
        self.battery = 0
        self.conductivity = 0
        self.moisture = 0
        self.firmware_version = ""
        
    def poll(self):
        poller = MiFloraPoller(self.mac)
        self.firmware_version = poller.firmware_version()
        self.temp = poller.parameter_value(MI_TEMPERATURE)
        self.moisture = poller.parameter_value(MI_MOISTURE)
        self.light = poller.parameter_value(MI_LIGHT)
        self.conductivity = poller.parameter_value(MI_CONDUCTIVITY)
        self.battery = poller.parameter_value(MI_BATTERY)

        
    def to_json(self):
        return { "temp" : self.temp, "moisture": self.moisture , "light": self.light, "conductivity" : self.conductivity, "battery": self.battery }
        
