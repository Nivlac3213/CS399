"""
Module 1: Object Oriented Programming
Date: 2/2/2023
Author: Calvin Henggeler
"""

# ***** Class vs Objects *****
# CLASS: collection of instance variables. A blueprint or template for objects
# OBJECTS: an Instance of a class

# Python objects have Contructors __new__ and initilizers __init__

# Method/ operator overloading does not work in Python (ex .add() )
# how ever a child class can override a mathod of a parent class


class ExampleClass:
    """ An example class for generic objects"""

    def __int__(self):
        """
        __init__ is an initilizer to initilze an object
        :return: None, Python 3.11 -> Self
        """
        pass

    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def print_name(self) -> None:
        print(self.name)


class ChildClass(ExampleClass):
    """Child Class inheriting from parent ExampleClass"""

    def __init__(self):
        pass


if __name__ == '__main__':
    exampleObj = ExampleClass('Big Cheese')
