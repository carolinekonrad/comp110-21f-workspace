"""Examples of optional parameters and Union types."""

def hello(name: str = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, " + name
    return greeting

from typing import Union

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result 

print(add(110.0, "100.0"))