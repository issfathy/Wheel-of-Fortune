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
    "How many players are playing? ", 1, 5)

# if(NumPlayers == 1):
#     print("Can't play by yourself")
#     raise Exception('Program Error --- Not enough players')


#Get the names of the players plus saving them into playermove to be able to use getMove()
#Having a loop so it keeps popping up until Number of players is exceeded
NamePlayers = [PlayerMove(input("Enter the names of the player # {}".format(i+1)))
               for i in range(NumPlayers)]

#For testing purposes

print("\n" + "This is the word to be guessed",phrase)

letterguessed = []

def requestMove(player, category, letterguessed):
    
    while True:
        themove = player.getMove(category, interactions.hidePhrase(phrase,letterguessed), letterguessed)
        themove = themove.upper()
        if themove == 'QUIT' or themove == 'PASS':
            return themove
        elif len(themove) == 1:
            if themove not in LETTERS:
                print("Your Guess should be a letter. Please try again")
                continue
            elif themove in letterguessed:
                print("{} is already guessed bud. Try again.".format(themove))
                continue
            # if it's a vowel, we need to be sure the player has enough to be able to buy
            elif themove in VOWELS and player.prizeMoney < VOWELS_COST:
                print('Need ${} to guess a vowel. Try again.'.format(VOWELS_COST))
                continue
            else:
                return themove
        else:
            return themove

winner = False

while(True):
    player = NamePlayers[playerSpot]

    wheel = interactions.WheelSpin()

    if wheel["type"] == "bankrupt":
        player.Bankrupt()
        print("Player spun bankrupt")
    elif wheel["type"] == "loseturn":
        print("Player spun lose a turn")
        pass
    elif wheel["type"] == "cash":
        print("\n" + "Player spun cash prize YAY")
        print(wheel['value'])
        playerMove = requestMove(player, category, letterguessed)
        if(playerMove == 'QUIT'):
            print("I'll see you next time")
            break
        elif(playerMove == 'PASS'):
            print("{} decided to skip to the next player".format(player.name))
            pass
        elif len(playerMove) == 1:
            letterguessed.append(playerMove)

            if(VOWELS.__contains__(playerMove)):
                player.vowelCost()
        
            # for i in range(len(guessingWord)):
            #     if phrase[i] == playerMove:
            #         guessingWord[i] = playerMove
            #         print("this letter is correct")
            #     else:
            #         print("your guess is wrong")
            
            # for i in guessingWord:
            #     ENDLETTERS += i

            #print("WORD SO FAR: ", ENDLETTERS) #prints out dashes including correct letters

            count = phrase.count(playerMove)
            player.addMoney(wheel['value'] * count)
            if(player.prizes is not False):
                player.addPrize(wheel['prize'])

                if interactions.hidePhrase(phrase, letterguessed) == phrase:
                    winner = player
                    break

                continue # this player gets to go again

            elif count == 0:
                print("There is no {}".format(playerMove))
        else: # they guessed the whole phrase
            if playerMove == phrase: # they guessed the full phrase correctly
                winner = player

                # Give them the money and the prizes
                player.addMoney(wheel['value'])
                if wheel['prize']:
                    player.addPrize(wheel['prize'])

                break
            else:
                print('{} was not the phrase'.format(playerMove))

    playerSpot = (playerSpot + 1) % len(NamePlayers)     

if winner:
    # In your head, you should hear this as being announced by a game show host
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))
print(colors.White)
