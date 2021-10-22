from MultiPlayer import HumanPlayer, colors, interactions
import random
import os

word = ["halloween", "christmas", "easter"]
clue = ["Holiday on October 30th", "Santa Claus", "Rabbits!"]

winner = False

letterIDK = ""
ENDLETTERS = ""

chosenWord = random.choice(word)
chosenClue = clue[word.index(chosenWord)]

lettersGuessed = ""
numberOfGuesses = 0
playerSpot = 0

print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")

NumPlayers = interactions.getCorrectInput(
    "How many players are playing?", 1, 10)

playerNumber = NumPlayers

NamePlayers = [HumanPlayer(input("Enter the names of the player #{}".format(i+1)))
               for i in range(NumPlayers)]

print(chosenClue)

guessingWord = []
for i in chosenWord:
    guessingWord.append("_ ")

for i in guessingWord:
    letterIDK += i
print(letterIDK)

while(True):
    player = NamePlayers[playerSpot]

    # wheelPrize = interactions.spinWheel()

    # if wheelPrize["type"] == "bankrupt":
    #     player.Bankrupt()
    # elif wheelPrize["type"] == "loseturn":
    #     pass
    # elif wheelPrize["type"] == "cash":
    #     pass
    
    print(player)

    if(ENDLETTERS == chosenWord):
        print(colors.Gold + "Winner" + colors.White)
        break
    numberOfGuesses += 1

    # can't guess a letter twice

    guess = input("Guess a letter: ")
    letter = guess.upper()
    lettersGuessed += letter
    print(lettersGuessed)

    ENDLETTERS = ""
    for i in range(len(chosenWord)):
        if chosenWord[i] == letter:
            guessingWord[i] = letter

    for i in guessingWord:
        ENDLETTERS += i

    # Move on to the next player if everything else above passes or fails not sure where to place this at tbh
    #playerSpot = (playerSpot + 1) % len(NamePlayers)

    print(ENDLETTERS)

print(colors.White)
