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

from random import randint
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Sensor:
    """ Sensor Class for generic Sensor """
    frequency = 10  # (Hz) can call the sensor every 10 time per second

    def __init__(self, location: str):
        """
        Initialize the new ob ject of type Sensor
        :param location: str -> where the sensor is located
        :return: none
        """
        self.location = location
        self.req_counter = 0

    def __str__(self):
        return self.__class__.__name__

    def value(self) -> bool:
        """
        Models the frequency parameter for higher performing sensors respond
        more often
        :return: Bool
        """
        self.req_counter += 1
        return self.req_counter % self.frequency == 0


class TempSensor(Sensor):

    def __init__(self, location: str, unit: str):
        self.unit = unit
        super().__init__(location)

    def print_temp(self) -> None:
        print(f"Humidity in the {self.location} is {randint(0,102)} {self.unit} ")
        return None

    def value(self) -> str:
        if super().value():
            return f"Temperature in the {self.location} is {randint(42, 105)} {self.unit}"


class HumiditySensor(Sensor):
    frequency = 20  # (Hz)

    def value(self) -> str:
        if super().value():
            return f"Humidity in the {self.location} is {randint(10, 90)}"

    def print_humidity(self) -> None:
        print(f"Humidity in the {self.location} is {randint(10, 90)}")
        return None


@dataclass
class ClassForData:
    """
    This is an Example of a Data Class
    """
    # this class does not beed a __init__ to be called as if it had one
    data1: int
    data2: str

"""
Using abstract methods
"""
class Shape:
    """
    This Class cannot be instantiated because it has an abstract method
    """
    @abstractmethod
    def Area(self) -> float:
        """
        :return:
            float: surface Area of sharpe
        """

class square(Shape):
    side = 2

    def Area(self) -> float:
        return self.side**2

if __name__ == "__main__":
    kitchen_ts = TempSensor("kitchen", "F")
    kitchen_hs = HumiditySensor("kitchen")

    sl = [kitchen_ts, kitchen_hs]
    for i in range(30):
        for s in sl:
            reading = s.value()
            if reading:
                print(f"{s.req_counter} .. {s} : {reading}")


