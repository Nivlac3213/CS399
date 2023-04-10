number = 13
print(type(number))


class City:
    def __init__(self, name: str):
        self.name = name

print(type(City))

my_city = City("Sedona")
print(type(my_city))
print(hasattr(City, "name"))