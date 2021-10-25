"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest 

__author__ = "730369129"


def test_invert_1() -> None:
    """Unit test for invert use case."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Unit test for 2nd invert use case."""
    xs: dict[str, str] = {'kris': 'kaki', 'michael': 'jordan', 'roy': 'williams'}
    assert invert(xs) == {'kaki': 'kris', 'jordan': 'michael', 'williams': 'roy'}


def test_invert_3() -> None:
    """Unit test for invert edge case."""
    with pytest.raises(KeyError):
        xs: dict[str, str] = {'a': 'z', 'b': 'z', 'c': 'y'}
        invert(xs)


def test_favorite_color_1() -> None:
    """Unit test for favorite_color use case."""
    xs: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(xs) == 'blue'


def test_favorite_color_2() -> None:
    """Unit test for favorite_color edge case."""
    xs: dict[str, str] = {'Lola': 'purple', 'Pippa': 'pink', 'Tess': 'purple', 'Geordi': 'blue', 'Lacey': 'pink'}
    assert favorite_color(xs) == 'purple'


def test_favorite_color_3() -> None:
    """Unit test for 2nd favorite_color use case."""
    xs: dict[str, str] = {'One ': 'red', 'Two': 'orange', 'Three': 'orange', 'Four': 'yellow'}
    assert favorite_color(xs) == 'orange'


def test_count_1() -> None:
    """Unit test for count use case."""
    xs: list[str] = ['orange', 'red', 'orange', 'red', 'orange']
    assert count(xs) == {'orange': 3, 'red': 2}


def test_count_2() -> None:
    """Unit test for 2nd count use case."""
    xs: list[str] = ['Lacey', 'Tess', 'Geordi', 'Pippa', 'Tess', 'Hazel', 'Zoey', 'Lola']
    assert count(xs) == {'Lacey': 1, 'Tess': 2, 'Geordi': 1, 'Pippa': 1, 'Hazel': 1, 'Zoey': 1, 'Lola': 1}


def test_count_3() -> None:
    """Unit test for count edge case."""
    xs: list[str] = []
    assert count(xs) == {}