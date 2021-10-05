"""Unit tests for list utility functions."""

__author__ = "730369129"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_odds() -> None:
    """Unit test for only_evens on list of only odds."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_use() -> None:
    """Unit test for only_evens on standard list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_use_2() -> None:
    """Unit test for only_evens on standard list."""
    xs: list[int] = [44, 46, 45, 78, 76]
    assert only_evens(xs) == [44, 46, 78, 76]


def test_sub_empty() -> None:
    """Unit test for sub on empty list."""
    xs: list[int] = []
    assert sub(xs, -1, 5) == []


def test_sub_use() -> None:
    """Unit test for sub on normal list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, 2, 5) == [3, 4, 5]


def test_sub_use_2() -> None:
    """Unit test for sub on normal list with large second index."""
    xs: list[int] = [2, 4, 5, 7, 9]
    assert sub(xs, 3, 7) == [7, 9]


def test_concat_empty() -> None:
    """Unit test for concat on empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_use() -> None:
    """Unit test for concat on two lists."""
    xs: list[int] = [1, 2]
    ys: list[int] = [3, 4, 5]
    assert concat(xs, ys) == [1, 2, 3, 4, 5]


def test_concat_use_2() -> None:
    """Unit test for concat on two lists."""
    xs: list[int] = [41, 39, 7, 11]
    ys: list[int] = [23, 14]
    assert concat(xs, ys) == [41, 39, 7, 11, 23, 14]   