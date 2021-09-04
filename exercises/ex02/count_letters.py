"""Counting letters in a string."""

__author__ = "730369129"

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word: ")

count: int = 0
times: int = 0

while times < len(word):
    if word[times] == letter:
        count = count + 1
    times = times + 1

print("Count: " + str(count))