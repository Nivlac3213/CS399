"""
Sorted Unique Square List

Jaxson Mitchell
CS 399
"""


class SUSList(list):  # Inherits from the list class.
    """
    Datatype based on List, contains only sorted unique squares.
    I.e. the base-class' mutators that change the element order or add new elements, need to be overridden or disabled.
    """

    def __init__(self, *elements):
        """
        Initializes a new List (optionally with the given elements)
        :type elements: *int
        """
        super().__init__([*elements])
        self.sort()  # Sorts incase the user enters a not so ideal value.

    def add(self, element: int):
        """
        Inserts the given element into the list, still keeping elements sorted and unique.
        If the element is not a square, it will be converted to its closest square: round(abs(element)**0.5)**2
        Only if the element is not already in the list, will be inserted.
        :type element: object
        """
        self[:] += [element]
        self.sort()
        return self  # For some reason I needed to return self on the method itself.

    def extend(self, lst: list[int]):
        """
        Adds each element of the given list to this list, still keeping elements sorted and unique
        :type lst: list of integers
        """
        self[:] += lst  # Appends the entire list in this method
        self.sort()
        return self

    def append(self, element) -> None:
        raise NotImplementedError

    def insert(self, index: int, element) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self, key=None, reverse=False):
        """
        Sorts the list so that the list actually is SUS.
        :param key: I do not know what the key does yet
        :param reverse: Nor the reverse
        """

        # Rounds the values within the list.
        for num, itm in enumerate(self):
            self[num] = round(abs(itm) ** 0.5) ** 2  # Makes it the closest square.

        # Takes out redundant values.
        SUS_list = list(set(self))
        self[:] = SUS_list  # Overrides the SUSlist without being wonky with the overriding the initialization

        # Sorts list
        self[:] = sorted(self, key=key, reverse=reverse)

        return None
