"""Finding duplicate letters in a word."""

__author__ = "730369129"

word: str = input("Enter a word: ")
count: int = 0
spot: int = 1
indexing_spot: int = 0

while indexing_spot < len(word) - 1:
    while spot < len(word):
        if word[indexing_spot] == word[spot] and indexing_spot != spot:
            count = count + 1
            spot = spot + 1
        else: 
            spot = spot + 1
    indexing_spot = indexing_spot + 1
    spot = 0

if count > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")