"""List utility functions part 2."""

__author__ = "730369129"


def only_evens(xs: list[int]) -> list[int]:
    """Return a list containing even numbers."""
    evens_list: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens_list.append(xs[i])
        i += 1
    return evens_list


def sub(ys: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a list between the indeces."""
    i: int = 0
    new_list: list[int] = []
    while i < len(ys):
        if i >= start_index and i < end_index:
            new_list.append(ys[i])
        i += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatonate two lists together."""
    i: int = 0
    i_2: int = 0
    concat_list: list[int] = []
    while i < len(xs):
        concat_list.append(xs[i])
        i += 1
    while i_2 < len(ys):
        concat_list.append(ys[i_2])
        i_2 += 1
    return concat_list