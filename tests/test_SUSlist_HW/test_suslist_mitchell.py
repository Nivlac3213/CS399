"""
Jaxson Mitchell

Test document

Tests that should be added
    - Initialization
        - If initialized, the list should test_SUSlist_HW for squares, sort, and remove redundant values.
    - Test the add method:
        - Adds a single normal square to a list
        - Sorts the list accordingly
        - Rounds the value inputted to make it a square
        - The rounded value must be unique to be entered.
    - Test the extend method.
        - The extend method should simply be multiple add methods, so if the add method works, in theory this should
        work. But a good test_SUSlist_HW is multiple of the same values, or non add values.
    - Edge Cases & Corner Cases
        - 0, -1, ...
        - Should negative values work?

Structure of the tests:
Basically my methodology for creating the tests is to create a singular test_SUSlist_HW for each of the cases where something
if not implemented properly should fail, for example each part of the sort, and then one or two cases having a
combination of each of those cases plus the edge cases to try to be comprehensive. This is due to the fact it
would be easier to find where errors within the code arise if one of the more specific cases fails. A good example
of this is within my initialization, where I have one separate for getting squares, sorting, and getting rid
of unique values.
The top tests are for the lower stuff while the bottom tests are built off of the methods the top tests test_SUSlist_HW.
"""
import pytest
from suslist import SUSList


@pytest.fixture
def ex_SUSlist():
    """
    Fixture used to get the first test_SUSlist_HW set of the SUSlist class.
    """
    return SUSList(2, 5, 9, 8, 109, 29, 29, 29, 109, -1)


@pytest.fixture
def empty_SUSlist():
    """
    Empty SUSList
    """
    return SUSList()


# Ensures SUSList is not empty if given inputs.
def test_SUSlist_elements():
    """
    tests if values even are able to be stored.
    """
    assert len(SUSList(1, 9, 20)) == 3


# Sort initialization tests.
def test_SUSlist_round():
    """
    Tests the initialization itself.

    First tests if the initialization works with rounding off the numbers
    """
    assert SUSList(2, 5, 29, 109) == SUSList(1, 4, 25, 100)


def test_SUSlist_redundant():
    """
    Tests if the SUSlist succeeds in getting out redundant values alone..
    """
    assert SUSList(1, 1, 1, 4, 4, 9) == SUSList(1, 4, 9)


def test_SUSlist_sorting():
    """
    Tests if the SUSList succeeds in sorting specifically.
    """
    assert SUSList(4, 9, 1) == SUSList(1, 4, 9)


def test_SUSlist_comprehensive(ex_SUSlist):
    """
    Tests if the SUSList succeeds in a combination of all three errors along with edge cases regarding negative numbers
    """
    assert ex_SUSlist == SUSList(1, 4, 9, 100, 25)  # Uses the fixture.


# Add tests
def test_add_appending():
    """
    Tests how the add method works in one case as well as the initialization of a SUSlist.
    In this example the goal is to get the 2 term to round down to 1 within the initialization
    :return:
    """
    Added_SUSlist = SUSList(2, 3, 4).add(9)
    assert Added_SUSlist == SUSList(1, 4, 9)


def test_add_redundancy():
    """
    Tests if redundant values are not added + edge case of negative values.
    """
    assert SUSList(1, 4, 9).add(-1) == SUSList(1, 4, 9)


def test_add_sorting():
    """
    Tests if an added values goes to the proper sorted part.
    """
    assert SUSList(1, 9, 16, 25, 36).add(4) == SUSList(1, 4, 9, 16, 25, 36)


def test_add_round():
    """
    Tests if an added value will become a square automatically
    """
    assert SUSList(1, 9, 16, 169).add(226) == SUSList(1, 9, 16, 169, 225)


def test_add_comprehensive(ex_SUSlist):
    """
    Tests all the cases in one huge part.
    """
    assert ex_SUSlist.add(16) == SUSList(1, 4, 9, 16, 25, 100)


# Extend
def test_extend_round():
    """
    Tests how values are rounded with the test_SUSlist_HW extend method.
    """
    assert SUSList(1, 4, 9, 16).extend([1009, 7923]) == SUSList(1, 4, 9, 16, 1000, 7921)


def test_extend_sorting():
    """
    Tests how the sorting works
    """
    assert SUSList(1, 7, 10, 29).extend([17, 203, 900]) == SUSList(1, 9, 16, 25, 900, 196)


def test_extend_redundancy(empty_SUSlist):
    """
    Tests if redundancy is dealt with properly
    """
    assert empty_SUSlist.extend([1, 1, 1, 1, 1, 1]) == SUSList(1)


def test_extend_comprehensive(ex_SUSlist):
    """
    Tests all the properties in junction
    SUSList(2, 5, 9, 8, 109, 29, 29, 29, 109, -1)
    """
    assert ex_SUSlist.extend([1, 4, 9, 169, 23, 42]) == SUSList(1, 4, 9, 25, 36, 100, 169)


# Weird input tests + Edge cases
def test_SUSlist_floats():
    """
    Tests how it reacts to floating points.
    """
    assert SUSList(1.0, 3.14159 ** 2) == SUSList(1, 9)


def test_SUSlist_edgecase():
    """
    Tests how it reacts to having negative values, floats, and zero by itself
    """
    assert SUSList(-10.0, 0, -1) == SUSList(0, 1, 9)


def test_SUSlist_noinput(empty_SUSlist):
    """
    Tests if the SUSList properly initializes with no input by checking its type as well as checks if the lists
    length is 0.
    """
    assert (type(empty_SUSlist) == SUSList) and (len(empty_SUSlist) == 0)

# We could also look at how other inputs are handled, but I decided to assume the user would simply give reasonable
# inputs.
