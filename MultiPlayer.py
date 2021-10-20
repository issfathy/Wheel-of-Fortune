import json
import random
import time
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class colors:
    Green = '\033[92m'
    Red = '\033[91m'
    White = '\033[97m'
    Gold = '\033[33m'
    
class PlayerBasics:
    def __init__(self , name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, bank):
        self.prizeMoney += bank

    def Bankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)

class HumanPlayer(PlayerBasics):

    def __init(self,name):
        PlayerBasics.__ini__(self,name)

    def getMove(self,category, phrase, guessed):
        print("{} has (${})".format(self.name,self.prizeMoney))

        print("Category:",category)
        print("Phrase:",phrase)
        print("Guessed:",guessed)

        theChoose = str(input("Guess a letter, phrase, or type ('Leave' or 'Pass'): "))
        return theChoose

class interactions:
    #Tested and Works
    def getCorrectInput(uinput, min, max):
        userinput = input(uinput)

        while True:
            try:
                x = int(userinput)
                if x < min:
                    errmessage = 'Must be at least {}'.format(min)
                elif x > max:
                    errmessage = 'Must be at most {}'.format(max)
                else:
                    return x
            except ValueError:
                errmessage = '{} is not a number.'.format(userinput)

            userinput = input('{}\n{}'.format(errmessage, uinput))

    def requestMove(player, category, guessed):
        #Need to included Bibin phrase guessing
        while True:
            playerMove = player.getMove(category, guessed)
            playerMove = playerMove.lower()

            if playerMove == 'exit' or playerMove == 'pass':
                return playerMove
            elif len(playerMove) == 1:
                if playerMove not in LETTERS:
                    print("Your Guess should be a letter. Please try again")
                    continue
                elif playerMove in guessed:
                    print("{} is already guessed bud. Try again.".format(playerMove))
                    continue
                elif playerMove in VOWELS and player.prizeMoney < VOWEL_COST: # if it's a vowel, we need to be sure the player has enough
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
                else:
                    return playerMove
            else:
                return playerMove

    #Tested and Works
    def spinWheel():
        with open("wheel.json", 'r') as f1:
            wheel = json.loads(f1.read())
            return random.choice(wheel)

    #Tested and Works
    def winner(self):
        prize = (colors.Gold + "        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              " ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "¶¶¶¶      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶¶¶¶\n" +
              '¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        ¶¶¶\n' +
              '¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        ¶¶¶\n' +
              '¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      ¶¶¶\n' +
              '¶¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶\n' +
              '¶¶¶    ¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶    ¶¶¶\n' +
              ' ¶¶¶¶   ¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶  ¶¶¶¶\n' +
              '   ¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶\n' +
              '    ¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶\n' +
              '     ¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶\n' +
              '               ¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '                 ¶¶¶¶¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '               ¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶  GOOD JOB  ¶¶¶\n' +
              '            ¶¶¶    IM SO   ¶¶¶\n' +
              '            ¶¶¶    PROUD   ¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
                                colors.White)
        return prize
    
    #Also get category and phrase from there as well,

