
from MultiPlayer import HumanPlayer, colors, interactions
import random
import os


print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")

NumPlayers = interactions.getCorrectInput(
    "How many players are playing?", 1, 10)

NamePlayers = [HumanPlayer(input("Enter the names of the player #{}".format(i+1)))
               for i in range(NumPlayers)]

word = ["halloween", "christmas", "easter"]
clue = ["Holiday on October 30th", "Santa Claus", "Rabbits!"]
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


while(True):  # stop loop if guessingWord = word

    if(ENDLETTERS == chosenWord):
        print(colors.Gold + "Winner" + colors.White)
        break
    numberOfGuesses += 1

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
    print(ENDLETTERS)

print(colors.White)
