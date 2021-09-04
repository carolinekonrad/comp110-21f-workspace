"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730369129"
from random import randint

fortune_1: str = "You will be kissed by a puppy!"
fortune_2: str = "The python gods will shine down on you today!"
fortune_3: str = "May your dreams be happy, not scary!"
fortune_4: str = "Your toes will thank you today!"

print("Your fortune cookie says...")

fortune_number: int = randint(1, 4)
if fortune_number == 1:
    print(fortune_1)
else: 
    if fortune_number == 2:
        print(fortune_2)
    else: 
        if fortune_number == 3:
            print(fortune_3)
        else: 
            print(fortune_4)

print("Now, go spread positive vibes!")