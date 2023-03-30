"""
    Sorted Unique Square List
    Author: Marcello Novak
    Date: 03/25/2023

    Disclaimer:
        The creation of this code was assisted by GitHub Copilot and ChatGPT-3.
        I assert that all the code given is of my own design, and that the aid
        used was for assistance, not for the creation of this assignment.

    Description: This program creates a new datatype SUSList based on list with the following functionalities:
        - Only unique integers (not already in the list) may be inserted
        - The list is always sorted
        - All elements in the list are squares of integers (e.g. 1, 4, 9, 16, 25, ...)
        - If an element is not a square, it is converted to the nearest square:
            like so: round(abs(element) ** 0.5) ** 2

    Side note: it is 1:05 in the morning and I can't stop giggling at "SUSList", send help.
    (Dr. Paulus, "Sus" is a popular online meme referring the game among us, short for suspicious.
    So this whole time I've been cackling to myself about how I'm coding a sussy list. I'm sorry.)

"""


class SUSList(list):

    """ Datatype based on List, contains only sorted unique squares.
    I.e. the base-class's mutators that change the element order or
    add new elements, need to be overridden or disabled.
    """

    def __init__(self, *elements):
        """ Initializes a new List (optionally with the given elements)
        :type elements: *int
        """
        super().__init__()
        for element in elements:
            self.add(element)

    def add(self, element: int) -> None:
        """ Adds the given element into the list, still keeping elements sorted and unique.
        Only unique elements will be added into the list
        :type element: object
        """

        # Check if the element is an integer
        if not isinstance(element, int):
            raise TypeError("SUSList can only contain integers")

        # Convert negative numbers to their absolute value
        if element < 0:
            element = abs(element)

        # Convert non-squares to the nearest square
        if int(element ** 0.5) ** 2 != element:
            element = int(round(abs(element) ** 0.5) ** 2)

        # If the element is not already in the list, add it
        if element not in self:
            # Call the base-class's append() method to add the element
            super().append(element)
            # Sort the list with the base-class's sort() method
            super().sort()

    def extend(self, lst: list[int]) -> None:
        """ Adds each element of the given list to this list, still keeping elements sorted and unique
        :type lst: list of integers
        """
        for element in lst:
            self.add(element)

    # Unimplemented/Redundant/Invalid methods
    def append(self, element) -> None:
        # Redundant, since add() already inserts the value in the correct position
        raise NotImplementedError("Append has been replaced with add()")

    def insert(self, index: int, element) -> None:
        # Redundant, since add() already inserts in the correct position
        raise NotImplementedError("Cannot insert into SUSList, use add() instead")

    def reverse(self) -> None:
        # Cannot reverse a sorted list
        raise NotImplementedError("Cannot reverse a SUSList, must always be sorted")

    def sort(self, key=None, reverse=False) -> None:
        # SUSLists are already sorted
        return None

