"""
Tests for the SUSList class.
By: Autumn Peterson
Date: 27 March 2023
"""

import pytest
from src.TDD.SUSlist_HW.suslist_peterson import SUSList


@pytest.fixture
def getsuslist():  # returns a new SUSList
    return SUSList()


def test_init():  # tests that SUSList is initialized as an empty list
    assert SUSList() == []


def test_add(getsuslist):  # tests that add() adds the closest square of the given element to the list
    getsuslist.add(25)
    getsuslist.add(24)
    getsuslist.add(37)
    getsuslist.add(63)
    getsuslist.add(79)
    getsuslist.add(81)
    getsuslist.add(101)
    assert getsuslist == [25, 36, 64, 81, 100]


def test_extend(getsuslist):  # tests that extend() adds closest square of each element in the given list to the suslist
    getsuslist.extend([105, 46, 15, 80, 23, 120, 3, 3])
    assert getsuslist == [4, 16, 25, 49, 81, 100, 121]
