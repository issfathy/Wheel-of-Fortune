# Wheel of Fortune Python Project
from MultiPlayer import PlayerBasics, PlayerMove, colors, interactions
from partsOfGame import game, ads, bonus
import os
import time
import random

# Setting variables for basic Tasks
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Start the entire game with a nice introduction
print(" ")
print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")


# Get the amount of players that are going to play
NumPlayers = interactions.AmountPlaying(
    "How many players are playing? ", 2, 3)

# Get the names of the players plus saving them into playermove
# Having a loop so it keeps popping up until Number of players is exceeded
NamePlayers = [PlayerMove(input("Enter the names of the player # {} ".format(i+1)))
               for i in range(NumPlayers)]

# bonus(NamePlayers)
# userChoices

# ads

# game

# bonus

for i in range(5):
    if i == 0:
        print("Now playing toss up")
    elif i == 1 or i == 2 or i == 3:
        print("Starting round ", i)
        game(NumPlayers,NamePlayers)
    else:
        bonus(NamePlayers)

# #bonus(NamePlayers)

# print(colors.White)

'''
THINGS TO FIX:
- when you win, it still says that you lost.
- validation for the consonants and vowels
- time limit (for just the overall round/game or for choices as well?)
'''
