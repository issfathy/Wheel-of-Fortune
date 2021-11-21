import json
import random
import time
import os
from tkinter import *
import webbrowser

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class colors:
    Green = '\033[92m'
    Red = '\033[91m'
    White = '\033[97m'
    Gold = '\033[33m'
    adsgolden = '#f5c842' # set your favourite rgb color
    adsgreen = '#009e2d'
    
class PlayerBasics:
    def __init__(self , name):
        self.name = name
        # Can 0 it out before submitting
        self.prizeMoney = 250
        self.RoundBank = 0
        self.prizes = []

    def addMoney(self, bank):
        self.prizeMoney += bank

    def addRoundMoney(self, secureBank):
        self.RoundBank += secureBank

    def vowelCost(self):
        self.prizeMoney -= VOWEL_COST

    def Bankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def listPlayer(self):
        return "Player: {}".format(self.name)

    def __str__(self):
        return "Player: {} | Prize Money:(${}) | OverAll Money:(${})".format(self.name,self.prizeMoney, self.RoundBank)

class PlayerMove(PlayerBasics):

    def __init(self,name):
        PlayerBasics.__ini__(self,name)

class interactions:
    # The validation of the number of players playing
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

    # Spins the wheel from a json file
    def WheelSpin():
        print("Spinning...")
        for i in range(10):
            with open("wheel.json", 'r') as f1:
                wheel = json.loads(f1.read())
            
            wheelRand = random.choice(wheel)

            time.sleep(0.2)    
            if wheelRand["type"] == "cash":
                print("${}".format(wheelRand["value"]))
            elif wheelRand["type"] == "bankrupt":
                print("Bankrupt")
            else:
                print("LoseTurn")
            
        print("You spun {}".format(wheelRand["text"]))
        return wheelRand

    def BonusSpin():
        print("Spinning...")
        for i in range(10):
            with open("bonusRound.json", 'r') as f1:
                wheel = json.loads(f1.read())
            
            wheelRand = random.choice(wheel)

            time.sleep(0.2)    
            if wheelRand["type"] == "cash":
                print("${}".format(wheelRand["value"]))
            
        print("You spun {}".format(wheelRand["text"]))
        return wheelRand

    # Gets the category and phrase from a json file
    def CategoryAndPhrase():
        with open("phrases.json", 'r') as f1:
            phrases = json.loads(f1.read())

            category = random.choice(list(phrases.keys()))
            phrase   = random.choice(phrases[category])
            return (category, phrase.upper())

    def ads():
        with open("ads.json", 'r') as f1:
            ads = json.loads(f1.read())

            return random.choice(ads)

    def displayAds():
        window = Tk()
        window.configure(bg=colors.adsgolden)
        window.title("A Quick Break")
        window.geometry("450x100")
        
        ads = interactions.ads()
        adsText = ads['text']
        url = ads['urlLink']
        adstype = ads['type']

        def onClick(x):
            webbrowser.open(x,new=1)

        label = Label(text = adsText, bg=colors.adsgolden, font=("Comic Sans MS", 16, "bold"))
        label.pack()
        labelOne = Label(text="A word from our sponsor", font=("Arial", 10), bg=colors.adsgolden)
        labelOne.pack()

        click = Button(window, bg=colors.adsgreen, text = adstype, command = lambda: onClick(url))
        click.pack()
        window.mainloop()
    # Prints the winner with a little throphy
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
    
