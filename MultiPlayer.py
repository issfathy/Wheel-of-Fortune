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

    def addMoney( self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)

class HumanPlayer(PlayerBasics):

    def __init(self,name):
        PlayerBasics.__ini__(self,name)

    def getMove(self,category, obscuredPhrase, guessed):
        print("{} has (${})".format(self.name,self.prizeMoney))

        print("Category:",category)
        print("Phrase:",obscuredPhrase)
        print("Guessed:",guessed)

        theChoose = str(input("Guess a letter, phrase, or type 'Leave' or 'Pass': "))
        return theChoose

class interactions:
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
    
    def winner():
        print("        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              " ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n" +
              "¶¶¶¶      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶¶¶¶\n" +
              '¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        ¶¶¶\n' +
              '¶¶        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        ¶¶¶\n' +
              '¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      ¶¶¶\n' +
              '¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶\n' +
              ' ¶¶¶   ¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶    ¶¶¶\n' +
              ' ¶¶¶¶   ¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶  ¶¶¶¶\n' +
              '   ¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶\n' +
              '    ¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶\n' +
              '     ¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶\n' +
              '               ¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '                 ¶¶¶¶¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '                   ¶¶¶¶\n' +
              '               ¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶            ¶¶¶\n' +
              '            ¶¶¶            ¶¶¶\n' +
              '            ¶¶¶            ¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '            ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              '         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' +
              "                You win!")
    

