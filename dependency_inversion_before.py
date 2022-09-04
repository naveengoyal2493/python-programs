from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on():
        pass
    
    @abstractmethod
    def turn_off():
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:

    def __init__(self, c):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = Fan()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()