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
            Complementary file is HenggelerCalvin_TDD_HW.py
"""

# =========================================================================== #
#                               Module Imports                                #
# =========================================================================== #
import pytest

from src.TDD.HenggelerCalvin_TDD_HW import SUSList


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
    print(f" Type: {type(empty_list)} Elements: {empty_list}")


def test_init_with_values(sus_list):
    sus_list.__init__(10, 20, 69, 144, 144, 9, 9, 5, 48, 29)
    print(f" Type: {type(sus_list)} Elements: {sus_list}")


def test_add(empty_list):
    empty_list.add(121)  # Add a unique square
    print(f" Elements: {empty_list}")


def test_add_with_values(sus_list):
    sus_list.add()


def test_extend(empty_list, sus_list):
    pass


def test_extend_with_values(sus_list):
    pass


def test_append(sus_list):
    pass


def test_insert(sus_list):
    pass


def test_reverse(sus_list):
    pass


def test_sort(sus_list):
    pass