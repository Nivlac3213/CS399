"""
Instance inherits fom a class

Class inherits from a Metaclass

lazy: only perfrom action when asked for it
ex: fethcing weather data when asked instead of before anyone cares about the weather


dir(obj): results in all the methods from metaclass

*** Type ***

type(onj OR type(name (1) ,basses (2), dict (3))
2nd type use is how to dynamically create an object

    DynamicFoo = type("DynamicFoo", (object,), {"__init__": init, "product": product})
                      |    (1)    |    (2)   |              (3)                     |
    (1)
"""

"""
##########################################
Creating custom metaclass:

__new__ : sets up memory but does not initilize

"""
class MyMeta(type):
        def __init__(cls, name, bases, attrs):
            super().__init__(name, bases, attrs)
            for name, value in attrs.items():
            print(f"{name} : {value}")

class SomeClass(metaclass=MyMeta):
    instance_counter = 0

    def __init__(self, x: int, y: int):
        self.__class__.instance_counter += 1
        self.x = x #__setattr__('x',x) is called here
        self.y = y

"""
##########################################
__dict__
    important: returns a dictionary
        type: "mappingproxy" this dictionary cannot be modified (no __setattr__ method)
    tells all methods of an object
    tells file to be located
    tells any instance variables if instantiated

__getattribte__(self,item)
gets called by built-in funtion getattr()


__setattr__(self,hey,value)
gets called by built-in setattr()

__geattr__(self,item)
called if item cannot be found int instance
used to add attributes at runtime (dynamically/lazily)
"""


"""
Why use a metaclass:

enforcing programming rules/ style
creating API.s in libraries and frameworks
"""

"""
##### Built-Ins #####



"""


