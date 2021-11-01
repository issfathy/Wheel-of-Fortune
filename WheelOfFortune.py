# Wheel of Fortune Python Project 
from MultiPlayer import PlayerMove, colors, interactions
import os
import time

# Setting variables for basic Tasks
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXZYZ'
VOWELS = 'AEIOU'
VOWELS_COST = 250
ENDLETTERS = ""
playerSpot = 0
guessingWord = []
lettersdash = ""
letterguessed = []
guessedSoFar = ""

# Setting category and phrase from the json files
category, phrase = interactions.CategoryAndPhrase()

# Hiding the phrase
for i in phrase:
    if LETTERS.__contains__(i):
        guessingWord.append('_')
    else:
        guessingWord.append(i)
        
for i in guessingWord:
    lettersdash += i

# Start the entire game with a nice introduction
print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")

# Get the amount of players that are going to play
NumPlayers = interactions.AmountPlaying(
    "How many players are playing? ", 1, 5)

# Get the names of the players plus saving them into playermove
# Having a loop so it keeps popping up until Number of players is exceeded
NamePlayers = [PlayerMove(input("Enter the names of the player # {} ".format(i+1)))
               for i in range(NumPlayers)]

# When the game winner is found it would turn this into True
Gamewinner = False

# For Testing purposes
print("\n" + "This is the word to be guessed", phrase)

# Displaying the ads
ads = interactions.displayAds()
# ads()

while(True):

    if(ENDLETTERS == ""):
        print("WORDS SO FAR: " + lettersdash)
    else:
        print("WORDS SO FAR: " + ENDLETTERS)

    player = NamePlayers[playerSpot]

    wheel = interactions.WheelSpin()

    if wheel["type"] == "bankrupt":
        player.Bankrupt()
        time.sleep(1)
        print("Player spun bankrupt")

    elif wheel["type"] == "loseturn":
        print("Player spun lose a turn")
        time.sleep(1)
        pass
    elif wheel["type"] == "cash":
        print("Player spun cash prize ${}".format(wheel["value"]))
        print(player)
        print("\n")
        time.sleep(1)

        guess = input("Guess a letter, phrase, or ('Quit'-To quit match or 'Pass'-Move to the next player): ")
        guess = guess.upper()

        if(guess == 'QUIT'):
            print("I'll see you next time")
            break
        elif(guess == 'PASS'):
            print("{} decided to skip to the next player".format(player.name))
            pass
        elif(len(guess) == 1):
            if letterguessed.__contains__(guess):
                print("{} has already been guessed, let's try this again".format(guess))
                playerSpot = (playerSpot + 1) % len(NamePlayers)
                continue
            pass     

            letterguessed.append(guess)
            guessedSoFar = ""

            if(VOWELS.__contains__(guess) and player.prizeMoney < VOWELS_COST):
                print("Need ${} to guess a vowel, let's try again".format(VOWELS_COST))
                continue
            elif(VOWELS.__contains__(guess) and player.prizeMoney > VOWELS_COST):
                player.vowelCost()

            for i in letterguessed:
                guessedSoFar += i

            print("LETTERS GUESSED SO FAR: ", guessedSoFar)

            for i in range(len(phrase)):
                if phrase[i] == guess:
                    guessingWord[i] = guess
                else:
                    pass

            ENDLETTERS = ""
            for i in guessingWord:
                ENDLETTERS += i

            count = phrase.count(guess)
            if(count > 0):
                if(count == 1):
                    print("There is one {}. Great Job".format(guess))
                else:
                    print("There are {} {}'s. Nice one".format(count, guess))

                # Give them the money and the prizes
                player.addMoney(count * wheel['value'])
                if wheel['prize']:
                    player.addPrize(wheel['prize'])

                # all of the letters have been guessed
                if ENDLETTERS == phrase:
                    winner = player
                    break

                continue  # this player gets to go again

            elif count == 0:
                print("There are no {} in this phrase".format(guess))

        if len(guess) > 1:
            if(guess == phrase):
                Gamewinner = player

                count = phrase.count(guess)
                player.addMoney(wheel['value'] * count)
                if wheel['prize']:
                    player.addPrize(wheel['prize'])
                break
            else:
                print("PHRASE IS WRONG")
                pass

    playerSpot = (playerSpot + 1) % len(NamePlayers)
    print("//////////////// End of Turn ////////////////")

if Gamewinner:
    time.sleep(1)
    print(interactions.winner())

    print('{} wins! The phrase was {}'.format(Gamewinner.name, phrase))
    print('Their prize money won is ${}'.format(Gamewinner.prizeMoney))

    if Gamewinner.prizes:
        print('{} also won:'.format(Gamewinner.name))
        for prize in Gamewinner.prizes:
            print('    - {}'.format(prize))
else:
    print('Noone has won. The phrase was {}'.format(phrase))
    print('Better luck next time bozo')

print(colors.White)
