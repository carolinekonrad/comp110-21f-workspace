"""An exercise in remainders and boolean logic."""

__author__ = "730369129"

integer: int = int(input("Enter an int: "))

if integer % 2 == 0 and integer % 7 == 0:
    print("TAR HEELS")
else: 
    if integer % 2 == 0:
        print("TAR")
    else: 
        if integer % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")