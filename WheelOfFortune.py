import random 


class colors:
    correctGreen = '\033[92m'
    wrongRed = '\033[91m'
    whiteBasic = '\033[97m'

class player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.prizes = []

    def addMoney(self, bank):
        self.prizeMoney += bank

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)
    
    #subtract function - for buy a vowel

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


NumPlayers = getCorrectInput("How many players are playing?", 1, 10)

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
while(numberOfGuesses <= 10):  # stop loop if guessingWord = word
    if(ENDLETTERS == chosenWord):
        print(colors.correctGreen + "You win!" + colors.whiteBasic)
        break
    numberOfGuesses += 1
    #can't guess a letter twice
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

print(colors.whiteBasic)
