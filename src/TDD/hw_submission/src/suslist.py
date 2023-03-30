"""
Author:     Calvin Henggeler
Date:       March 27, 2023
Course:     CS - 399 Intermediate Python

Description:
            Sorted Unique Square List
            This python file is made to complete Homework 4 on the topic of
            Test Driven Development and Fixtures
Disclaimers:
            Some GitHib Copilot was used
Sources:
            Given starting code from assignment
            Complementary file is test_suslist.py
"""


class SUSList(list):
    """ Datatype based on List, contains only sorted unique squares.
        I.e. the base-class' mutators that change the element order or add new
        elements, need to be overridden or disabled.
    """

    def __init__(self, *elements):
        """ Initializes a new List (optionally with the given elements)
        :type elements: *int
        """
        # take make new elements squares
        super().__init__(list(set(map(lambda x: round(x ** 0.5)**2, elements))))

        # initial sort
        super().sort()

    def add(self, element: int) -> None:
        """
        Inserts the given element into the list, still keeping elements sorted and unique.
        If the element is not a square, it will be converted to its closest square: round(abs(element)**0.5)**2
        Only if the element is not already in the list, will be inserted.
        :type element: object
        """

        # Force new element to the closest square
        sqr_elem = round(element ** 0.5)**2

        # case if SUSlist is empty
        if len(self) == 0:
            self.__init__(sqr_elem)
        elif sqr_elem not in self:

            # append the new element
            super().append(sqr_elem)
            # make the list unique
            super().__init__(list(set(self)))
            # re-sort
            super().sort()

        return None

    def extend(self, lst: list[int]) -> None:
        """
        Adds each element of the given list to this list, still keeping elements sorted and unique
        :type lst: list of integers
        """
        for _ in lst:
            self.add(_)

    def append(self, element) -> None:
        raise NotImplementedError

    def insert(self, index: int, element) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self, key=None, reverse=False) -> None:
        super().sort(key=key, reverse=reverse)
        return None
