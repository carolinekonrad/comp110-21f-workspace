"""Challenge Question #1"""

__author__ = "730369129"

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice > 75:
            print("C")
        else:
            print("D")