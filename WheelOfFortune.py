from MultiPlayer import PlayerMove, colors, interactions
import random
import os

#Setting variables for basics 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWELS_COST = 250
ENDLETTERS = ""

playerSpot = 0
guessingWord = []
lettersdash = ""

#Setting category and phrase from the json files
category, phrase = interactions.CategoryAndPhrase()

#Start the entire game with a nice introduction
print(".\ / \ / \ / \ /.".center(os.get_terminal_size().columns))
print("Welcome to Wheel of Fortune".center(os.get_terminal_size().columns))
print("./ \ / \ / \ / \.".center(os.get_terminal_size().columns))
print(" ")

#Get the amount of players that are going to play
NumPlayers = interactions.AmountPlaying(
    "How many players are playing?", 1, 5)

#Get the names of the players plus saving them into playermove to be able to use getMove()
#Having a loop so it keeps popping up until Number of players is exceeded
NamePlayers = [PlayerMove(input("Enter the names of the player #{}".format(i+1)))
               for i in range(NumPlayers)]

#For testing purposes

print(phrase)

def requestMove(player, category, guessed):
    while True:
        playerMove = player.getMove(category, interactions.hidePhrase(phrase, guessed), guessed)
        playerMove = playerMove.upper()

        if playerMove == 'QUIT' or playerMove == 'PASS':
            return playerMove
        elif len(playerMove) == 1:
            if playerMove not in LETTERS:
                print("Your Guess should be a letter. Please try again")
                continue
            elif playerMove in guessed:
                print("{} is already guessed bud. Try again.".format(playerMove))
                continue
            # if it's a vowel, we need to be sure the player has enough to be able to buy
            elif playerMove in VOWELS and player.prizeMoney < VOWELS_COST:
                print('Need ${} to guess a vowel. Try again.'.format(VOWELS_COST))
            #if the letter guessed is within that chosen word, replace the dash with letter.    
                continue
            else:
                return playerMove
        else:
            return playerMove

letterguessed = []

while(True):
    player = NamePlayers[playerSpot]

    guess = input("Guess a letter: ")

    wheel = interactions.WheelSpin()

    if wheel["type"] == "bankrupt":
        player.Bankrupt()
    elif wheel["type"] == "loseturn":
        pass
    elif wheel["type"] == "cash":
        playerMove = requestMove(player, category)
        if(playerMove == 'QUIT'):
            print("I'll see you next time")
            break
        elif(playerMove == 'PASS'):
            print("{} decided to skip to the next player".format(player.name))
            pass
        elif len(playerMove) == 1:
            letterguessed.append(playerMove)

            if(playerMove.__contains__(VOWELS)):
                player.vowelCost()
            pass

            count = phrase.count(playerMove)
            player.addMoney(wheel['value'] * count)
            if(player.prizes is not False):
                player.addPrize(wheel['prize'])

    playerSpot = (playerSpot + 1) % len(NamePlayers)        
    print(player)

    # if(ENDLETTERS == phrase):
    #     print(colors.Gold + "Winner" + colors.White)
    #     break

    # # can't guess a letter twice

    # if lettersGuessed.__contains__(guess):
    #     print("That letter has been guessed. Try again!")
    #     pass
    # elif VOWELS.__contains__(guess):
    #     # subtract money from bank if possible

    #     # print("Sorry, you don't have enough funds for a vowel.")
    #     pass
    # else:
    #     letter = guess.upper()
    #     lettersGuessed += letter + ' '
    #     print("These letters have been guessed:", lettersGuessed)

    #     ENDLETTERS = ""
    #     for i in range(len(phrase)):
    #         if phrase[i] == letter:
    #             guessingWord[i] = letter
    #     for i in guessingWord:
    #         ENDLETTERS += i
    #     print(ENDLETTERS)  # prints out dashes including correct letters

    # ENDLETTERS = ""
    # for i in range(len(phrase)):
    #     if phrase[i] == letter:
    #         guessingWord[i] = letter

    # for i in guessingWord:
    #     ENDLETTERS += i

    # # Move on to the next player if everything else above passes or fails not sure where to place this at tbh
    # #playerSpot = (playerSpot + 1) % len(NamePlayers)

    # print(ENDLETTERS)

print(colors.White)
