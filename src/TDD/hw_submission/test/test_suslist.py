"""
Author:     Calvin Henggeler
Date:       March 27, 2023
Course:     CS-399 Intermediate Python

Description:
            Test module Sorted Unique Square/ linked List List
            This python file is made to complete Homework 4 on the topic of
            Test Driven Development and Fixtures
Disclaimers:
            None, No Artificial Intelligence tools used
Sources:
            Given starting code from assignment
            Complementary file is suslist.py
"""

# =========================================================================== #
#                               Module Imports                                #
# =========================================================================== #
import pytest

from src.HenggelerCalvin_TDD_HW import SUSList


# =========================================================================== #
#                                  Fixtures                                   #
# =========================================================================== #

# SUSlist instance with no elements
@pytest.fixture
def empty_list():
    empty_list = SUSList()
    return empty_list


# SUSlist instance with optional initial arguments
@pytest.fixture
def sus_list():
    # ---------------- |   SUS   | repeated sqrs | non-sqrs |
    sus_list = SUSList(10, 20, 69, 144, 144, 9, 9, 5, 48, 29)
    return sus_list


# =========================================================================== #
#                             Functionality Tests                             #
# =========================================================================== #
def test_init(empty_list):
    empty_list.__init__()
    print(f"\n\t Type: {type(empty_list)} Elements: {empty_list}")


def test_init_with_values(sus_list):
    sus_list.__init__(10, 20, 69, 144, 144, 9, 9, 5, 48, 29)
    print(f"\n\tType: {type(sus_list)} Elements: {sus_list}")


def test_add(empty_list):
    empty_list.add(121)  # Add a unique square
    print(f"\n\tType: {type(empty_list)} Elements: {empty_list}")


def test_add_with_values(sus_list):
    # add element that is already in the sus_list
    sus_list.add(144)
    # add new sqare element
    sus_list.add(36)
    # add new non-sqare element
    sus_list.add(99) # --> 10**2 = 100

    print(f"\n\tType: {type(sus_list)} Elements: {sus_list}")


def test_extend(empty_list, sus_list):
    print('\n\tExtending empty_list with sus_list...')
    print(f"\tsus_list: {sus_list}")
    print(f"\tOLD empty_list: {empty_list}")
    print('\n\tExtending empty_list with sus_list...')
    empty_list.extend(sus_list)
    print(f"\tNEW empty_list: {empty_list}")



def test_extend_with_values(sus_list):
    print(f"\n\tOLD sus_list: {sus_list}")
    print("\tExtending sus_list with new elements...")
    # ------------- |   SUS  |  repeated sqrs  |  non-sqrs  |
    sus_list.extend([100, 121, 144, 49, 144, 25, 32, 1000, 3])
    print(f"\tNEW sus_list: {sus_list}")


def test_append(sus_list):
    pass


def test_insert(sus_list):
    pass


def test_reverse(sus_list):
    pass


def test_sort(sus_list):
    pass