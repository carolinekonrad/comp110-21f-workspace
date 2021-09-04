"""Repeating a beat in a loop."""

__author__ = "730369129"

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
counter: int = 0
long_beat: str = ""

while counter < repeat: 
    long_beat = long_beat + beat 
    if counter < repeat - 1: 
        long_beat = long_beat + " "
    counter = counter + 1

if repeat <= 0:
    print("No beat...")
else: 
    print(long_beat)