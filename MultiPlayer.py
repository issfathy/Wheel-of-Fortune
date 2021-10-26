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
        self.prizeMoney = 250
        self.prizes = []

    def addMoney(self, bank):
        self.prizeMoney += bank

    def vowelCost(self):
        self.prizeMoney -= VOWEL_COST

    def Bankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)

class PlayerMove(PlayerBasics):

    def __init(self,name):
        PlayerBasics.__ini__(self,name)
    #Will be used later, taking inputs and displaying different Category, Phrase, and Guessed
    def playerMove(self,category, phrase, guessed):
        print("{} has (${})".format(self.name,self.prizeMoney))

        print("Category:",category + "\n")
        print("Phrase:",phrase + "\n")
        print("Guessed:",guessed + "\n")

        return "okay"

class interactions:
    #Tested and Works
    def AmountPlaying(uinput, min, max):
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

    #Tested and will be used for later purposes
    def hidePhrase(phrase, guessed):
        input = ""
        for i in phrase:
            if(i in LETTERS) and (i not in guessed):
                input += "_"
            else:
                input = input+i
        return input

    #Tested and Works
    def WheelSpin():
        with open("Wheel.json", 'r') as f1:

            wheel = json.loads(f1.read())
            return random.choice(wheel)

    #Tested and Works
    def CategoryAndPhrase():
        with open("Phrases.json", 'r') as f1:
            phrases = json.loads(f1.read())

            category = random.choice(list(phrases.keys()))
            phrase   = random.choice(phrases[category])
            return (category, phrase.upper())

    #Tested and Works
    def winner():
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
    
