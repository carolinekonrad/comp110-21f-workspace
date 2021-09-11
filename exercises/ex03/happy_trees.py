"""Drawing forests in a loop."""

__author__ = "730369129"

TREE: str = '\U0001F332'
integer_depth: int = int(input("Depth: "))
long_string: str = ""
counter: int = 0

if integer_depth >= 0:
    while counter < integer_depth:
        long_string = long_string + TREE
        print(long_string)
        counter = counter + 1