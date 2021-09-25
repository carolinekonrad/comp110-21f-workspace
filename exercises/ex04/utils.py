"""List utility functions."""

__author__ = "730369129"


def all(my_list: list[int], my_int: int) -> bool:
    """Defining the function 'all'."""
    i: int = 0
    if len(my_list) == 0:
        return False
    while i < len(my_list):
        item: int = my_list[i]
        if item == my_int:
            i += 1
        else:
            return False
    return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Defining the function 'is_equal'."""
    if len(first_list) != len(second_list):
        return False
    i: int = 0
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            return False
        else:
            i += 1
    return True


def max(my_list: list[int]) -> int:
    """Defining the function 'max'."""
    if len(my_list) == 0:
        raise ValueError("max() arg is an empty list")
    incumbent_solution: int = my_list[0]
    i: int = 1
    while i < len(my_list):
        if my_list[i] > incumbent_solution:
            incumbent_solution = my_list[i]
        i += 1
    return incumbent_solution