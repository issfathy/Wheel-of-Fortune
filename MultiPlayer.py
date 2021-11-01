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
    