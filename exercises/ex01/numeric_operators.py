"""Ex01 Part 2 Homework."""

__author__: str = "730369129"

left_side: str = input("What number would you like on the left side? ")
right_side: str = input("What number would you like on the right side? ")

print("Left-hand side: " + left_side)
print("Right-hand side: " + right_side)
print(left_side + " ** " + right_side + " is " + str(int(left_side) ** int(right_side)))
print(left_side + " / " + right_side + " is " + str(float(int(left_side) / int(right_side))))
print(left_side + " // " + right_side + " is " + str(int(left_side) // int(right_side)))
print(left_side + " % " + right_side + " is " + str(int(left_side) % int(right_side)))