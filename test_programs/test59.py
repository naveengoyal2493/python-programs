import string
import random

class VehicleInfo:
    vehicle_name: str
    catalogue_price: int
    electric: bool

    def __init__(self, vehicle_name, catalogue_price, electric):
        self.vehicle_name = vehicle_name
        self.catalogue_price = catalogue_price
        self.electric = electric

    def calculate_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.vehicle_name}")
        print(f"Payable tax: {self.calculate_tax()}")



class Vehicle:
    vehicle_id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, vehicle_id, license_plate, info: VehicleInfo):
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.vehicle_id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 60000)
        self.add_vehicle_info("BMW 5", True, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)


    def add_vehicle_info(self, vehicle_name, catalogue_price, electric):
        self.vehicle_info[vehicle_name] = VehicleInfo(vehicle_name, catalogue_price, electric)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        vehicle = registry.create_vehicle(brand)

        vehicle.print()

# app = Application()
# vehicle = app.register_vehicle("BMW 5")

##################################################################################################
from abc import ABC, abstractmethod

class Switch:

    @abstractmethod
    def turn_on():
        pass

    def turn_off():
        pass

class LightBulb(Switch):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switch):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:

    def __init__(self, s: Switch):
        self.switch = s
        self.on = False

    def press(self):
        if self.on:
            self.switch.turn_off()
            self.on = False
        else:
            self.switch.turn_on()
            self.on = True


# l = Fan()
# switch = ElectricPowerSwitch(l)
# switch.press()
# switch.press()


######################################################################################

import string
import random

class Ticket:
    
    def __init__(self, issue, customer_name):
        self.ticket_id = self.generate_id()
        self.issue = issue
        self.customer_name = customer_name

    def generate_id(self, length=8):
        # helper function for generating an id
        return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketStrategy:
    @abstractmethod
    def process_tickets(ticket_strategy):
        pass

class FIFOTicketStrategy(TicketStrategy):
    def process_tickets(self, tickets):
        return tickets.copy()
        

class FILOTicketStrategy(TicketStrategy):
    def process_tickets(self, tickets):
        for ticket in reversed(tickets):
            super().print_ticket(ticket)


class RandomTicketStrategy(TicketStrategy):
    def process_tickets(self, tickets):
        list_copy = tickets.copy()
        random.shuffle(list_copy)
        for ticket in list_copy:
            super().print_ticket(ticket)


class CustomerSupport:

    def __init__(self, processing_strategy: str = "fifo"):
        self.tickets = []
        self.processing_strategy = processing_strategy

        self.strategies = {
            "fifo": FIFOTicketStrategy,
            "filo": FILOTicketStrategy,
            "random": RandomTicketStrategy,
        }

    def create_ticket(self, issue, customer):
        ticket = Ticket(issue, customer)
        self.tickets.append(ticket)

    def process_tickets(self):
        strategy = self.strategies[self.processing_strategy]
        strategy(self.tickets).process_tickets()


# create the application
app = CustomerSupport("random")

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()





