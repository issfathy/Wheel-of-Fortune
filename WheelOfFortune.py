import random 

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
while(numberOfGuesses <= 10): #stop loop if guessingWord = word
    if(ENDLETTERS == chosenWord):
        print("You win!")
        break
    numberOfGuesses += 1
    letter = input("Guess a letter: ")
    lettersGuessed += letter
    print(lettersGuessed)

    ENDLETTERS = ""
    for i in range(len(chosenWord)):
        if chosenWord[i] == letter:
            guessingWord[i] = letter
    for i in guessingWord:
        ENDLETTERS += i
    print(ENDLETTERS)


#IS THIS UPDATED???
