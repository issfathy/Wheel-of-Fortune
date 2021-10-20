from MultiPlayer import HumanPlayer, colors, interactions
import random
import os

print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")

NumPlayers = interactions.getCorrectInput(
    "How many players are playing?", 1, 10)

playerNumber = NumPlayers

NamePlayers = [HumanPlayer(input("Enter the names of the player #{}".format(i+1)))
               for i in range(NumPlayers)]

word = ["halloween", "christmas", "easter"]
clue = ["Holiday on October 30th", "Santa Claus", "Rabbits!"]
wheelPrize = []
winner = False
letterIDK = ""
ENDLETTERS = ""

chosenWord = random.choice(word)
chosenClue = clue[word.index(chosenWord)]

print(chosenClue)

guessingWord = []
for i in chosenWord:
    guessingWord.append("_ ")

for i in guessingWord:
    letterIDK += i
print(letterIDK)

lettersGuessed = ""
numberOfGuesses = 0
playerSpot = 0

while(True):  # stop loop if guessingWord = word

    """ 
    Sudoo code for bankrupt and stuff

    if the wheel spun bankrupt
        player.Bankrupt()
    elif the wheel spun is loseturn
        player pass I think idk
    elif the wheel spun cash
        than we can continue with the game
    """
    #The prize print place
    #prize = interactions.winner("")
    
    #The index but has an error needs to be fixed
    player = NamePlayers[playerSpot]

    print(player)
    if(ENDLETTERS == chosenWord):
        print(colors.Gold + "Winner"+ colors.White)
        break
    numberOfGuesses += 1

    # can't guess a letter twice

    guess = input("Guess a letter: ")
    letter = guess.lower()
    lettersGuessed += letter
    print(lettersGuessed)

    ENDLETTERS = ""
    for i in range(len(chosenWord)):
        if chosenWord[i] == letter:
            guessingWord[i] = letter

    for i in guessingWord:
        ENDLETTERS += i


    #Move on to the next player if everything else above passes or fails not sure where to place this at tbh 
    #playerSpot = (playerSpot + 1) % len(NamePlayers)

    print(ENDLETTERS)

print(colors.White)
