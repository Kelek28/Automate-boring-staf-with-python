# Chapter 4
# Project: Coin Flip Streaks

import random
numberOfStreaks = 0
streaks = 0
lastFlip = None
ListOfValues = []
    # Code that creates a list of 100 'heads' or 'tails' values.
for experimentNumber in range(10000):
    Flip = random.randint(0, 1)
    if(Flip == 0):
        ListOfValues.append("T")
    else:
        ListOfValues.append("H")
# Code that checks if there is a streak of 6 heads or tails in a row.
for value in ListOfValues:
    if(value == lastFlip):
        streaks += 1
        if(streaks == 6):
            numberOfStreaks += 1
            streaks = 0
    else:
        streaks = 0
    lastFlip = value

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
