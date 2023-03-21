""" OOP Demo """
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Engine:
    cylinder: int
    horsepower: int


@dataclass
class TruckEngine(Engine):
    torque: int


class Car(ABC):
    """ Composition: a car HAS an engine """
    instances = 0  # class variable

    def __init__(self, model: str, mpg: float, passengers: int, engine: Engine = Engine(4, 220)):
        """ init method also shows the use on an default argument """
        self.model = model
        self.mpg = mpg
        self.passengers = passengers
        self.engine = engine
        self.__class__.instances += 1  # counting number of cars initialized
        self.color = "red"  # hard-coding an instance variable

    @classmethod
    def cars_produced(cls) -> int:
        return cls.instances

    @abstractmethod
    def drive(self) -> str:
        """ all sub classes need to implement this method """
        pass

    def __str__(self):
        """ show a car's model value instead of the default (memory...)"""
        return self.model

    def __gt__(self, other):
        """ Let's use a car's mpg for comparing cars """
        if isinstance(other, Car):
            return self.mpg > other.mpg
        else:
            raise TypeError(f"Cannot compare {other.__class__.__name__} with {self.__class__.__name__}")


class Van(Car):
    """
    Inheritance, a Van IS a car.
    The Van class does not need its own init, since has has no need to change the way it's initialized
    """
    instances = 0  # class variable

    def drive(self) -> str:
        return "compfy at a slow pace"


class Truck(Car):
    """Inheritance, a Truck IS a car"""
    instances = 0  # class variable

    def __init__(self, model: str, mpg: float, type_: str, passengers: int, engine: TruckEngine):
        """ need to add a new instance variable, therefore init needs to be overridden"""
        super().__init__(model, mpg, passengers, engine)
        self.type_ = type_

    def drive(self) -> str:
        return f"loud, {'forceful' if self.engine.torque > 350 else 'strong'}"


lst = [Van("Kia Sedona", 24, 6),
       Van("Toyota Sienna", 36, 8, TruckEngine(4, 245, 147)),  # this works, a TruckEngine is an Engine
       Truck("Dodge RAM", 22, "Medium duty", 4, TruckEngine(6, 240, 450))]

for car in lst:
    print(car.model, car.drive())

# Best car .. highest miles per gallon
print("Best car: ", max(lst))

# no, no, no, .. best car is the car with most hp:
print("Best car: ", max(lst, key=lambda x: x.engine.horsepower))

print(f"So far we have built {Van.cars_produced()} van(s)")
print(f"So far we have built {Truck.cars_produced()} truck(s)")
