"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730369129"


class Simpy:
    values: list[float]
    
    def __init__(self, x: list[float]) -> None:
        """Initializing the object."""
        self.values = x

    def __str__(self) -> str:
        """Printing the str object."""
        return f"Simpy({str(self.values)})"
    
    def fill(self, numbers: float, how_many: int) -> None:
        """Create a list with a number how_many number of times."""
        i: int = 0
        self.values = []
        while i < how_many:
            self.values.append(numbers)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Assign object a list of values for a specific range and space between them."""
        assert step != 0.0
        self.values = []
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Sum the values of the object."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add two Simpy's together to create a new object."""
        new_list: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                new_list.append(self.values[i] + rhs)
                i += 1
        else:
            while i < len(self.values):
                new_list.append(self.values[i] + rhs.values[i])
                i += 1
        return Simpy(new_list)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Create a new object by raising one Simpy to the power of the other."""
        new_list: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                new_list.append(self.values[i] ** rhs)
                i += 1
        else:
            while i < len(self.values):
                new_list.append(self.values[i] ** rhs.values[i])
                i += 1
        return Simpy(new_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """CHeck if self's values are equal to rhs's."""
        list_bools: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                list_bools.append(self.values[i] == rhs)
                i += 1
        else:
            while i < len(self.values):
                list_bools.append(self.values[i] == rhs.values[i])
                i += 1
        return list_bools

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if self is greater than rhs."""
        list_bools: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                list_bools.append(self.values[i] > rhs)
                i += 1
        else:
            while i < len(self.values):
                list_bools.append(self.values[i] > rhs.values[i])
                i += 1
        return list_bools
    
    def __getitem__(self, rhs: int) -> float:
        """Printing value of self at index rhs."""
        return self.values[rhs]