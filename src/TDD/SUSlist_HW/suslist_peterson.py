"""
    Sorted Unique Square List
    Author: Autumn Peterson
    Date: 27 March 2023
"""


class SUSList(list):
    """ Datatype based on List, contains only sorted unique squares.
    I.e. the base-class mutators that change the element order or add new elements, need to be overridden or disabled.
    """

    def __init__(self):
        """ Initializes a new List
        """
        super().__init__()

    @classmethod
    def _closest_square(cls, element: int) -> int:  # returns the closest square of the given element as method of class
        return round(abs(element) ** 0.5) ** 2

    def add(self, element: int) -> None:  # adds the closest square of the given element to the list
        """
        Inserts the given element into the list, still keeping elements sorted and unique.
        If the element is not a square, it will be converted to its closest square: round(abs(element)**0.5)**2
        Only if the element is not already in the list, will be inserted.
        :type element: object
        """
        proper = self.__class__._closest_square(element)
        if proper not in self:  # find the index of the smallest item bigger than proper.
            for i in range(len(self)):
                if self[i] > proper:
                    super().insert(i, proper)  # override the base-class insert method to insert the proper element
                    break
            else:
                super().append(proper)  # if proper is the biggest element, append it to the end of the list

    def extend(self, lst: list[int]) -> None:
        """
        Adds each element of the given list to this list, still keeping elements sorted and unique
        :type lst: list of integers
        """
        for i in lst:
            self.add(i)
        return None

    def append(self, element) -> None:
        raise NotImplementedError

    def insert(self, index: int, element) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self, key=None, reverse=False) -> None:
        return None
