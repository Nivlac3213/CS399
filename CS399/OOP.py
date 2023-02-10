"""
Module 1: Object Oriented Programming
Date: 2/2/2023
Author: Calvin Henggeler
"""

# ***** Class vs Objects *****
# CLASS: collection of instance variables. A blueprint or template for objects.
# OBJECTS: an Instance of a class

# Python objects have constructors __new__ and inits __init__

# Method/ operator overloading does not work in Python (ex .add() )
# however a child class can override a method of a parent class

import random


class Sensor:
    """ Sensor Class for generic Sensor """
    frequency = 10  # (Hz) can call the sensor every 10 time per second

    def __int__(self, location: str):
        """
        Initialize the new ob ject of type Sensor
        :param location: str -> where the sensor is located
        :return: none
        """
        self.location = location
        self.req_counter = 0

    def __str__(self):
        return self.__class__.__name__


class HumiditySensor(Sensor):
    """
    HumiditySensor class models a humidity sensor
    Inherits from Sensor Class
    """
    frequency = 50  # (Hz)

    def read_humidity(self) -> str:
        return f"Humidity in the {self.location} is {random.randint(0,90)}"


class TempSensor(Sensor):

    def __init__(self, location: str, unit: str):
        self.unit = unit
        super().__init__(location)

    def read_temp(self) -> str:
        self.req_counter += 1
        if self.req_counter % self.frequency == 0:
            return f"Humidity in the {self.location} is {random.randint(0,102)} {self.unit} "


kitchen_ts = TempSensor("kitchen", "F")
# kitchen_hs = Sensor("kitchen")
print(kitchen_ts.read_temp())
