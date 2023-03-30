import pytest
from suslist_novakm import SUSList


def test_init():
    # For none
    testlist = SUSList()
    assert testlist == []

    # For a basic list
    testlist = SUSList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert testlist == [1, 4, 9]

    # For a list involving negative numbers
    testlist = SUSList(-1234, -100, -4)
    assert testlist == [4, 100, 1225]

    # Extend previous list with extend()
    testlist.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert testlist == [1, 4, 9, 100, 1225]

    # Add a new element with add() to previous list
    testlist.add(225)
    assert testlist == [1, 4, 9, 100, 225, 1225]


