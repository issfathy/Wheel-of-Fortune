#                                      The Best Wheel of Fortune Project Ever
### This wheel includes a tossup and bonus round, everything that others don't have
## Multiplayer.py file has different classes:


- Colors - with green, red, white, gold, adsgolden, and adsgreen 
- PlayerBasics - where there is prizeMoney, roundBank and prizes are stores with different functions like addMoney, addRoundMoney and others
- PlayerMove - gets the name of the players and stores them.
- Interactions - are the every interactions that has to do with the game like the amount of players playing, wheelSpins, category and phrase, ads, and more.

## PartsOfGame.py file has all the main functions:

- Tossup - works like in real life letters start displaying and who ever wants can do so as well. The prize money is $2000
- Ads - displays the ads using functions from multiplayer
- Game - is everything combined to run and play the entirety of the game 
- UserChoices - is the choice of 3 consonant and 1 vowel for the bonus round
- Bonus - is used for the bonus for the overall winner

## WheelOfFortune.oy file is the entire game being played

- Start with a nice welcome to wheel of fortune 
- NumPlayer - number of players playing 
- NamePlayers - the name of the players playing
- FinalWinner - determines the final winner for the bonus round
- Lastly there is a loop going over everything discussed above 

## Json files

- Wheel - is the main wheel being spun every time a player goes to guess a letter
- Phrases - is where the category and phrase are chosen from, we decided to norrow it down so it looks cleaner  
- bonusRound - is the wheel used for the bonus round
- ads - is used to display different ads before each round

## Issues Encountered:
- We have tried to implement a wheel but could not find a successful way to do so but we did come close. 
- We also encountered a difficulty with creating a timer that did not care about a user input but instead kept counting until the time ran out 

# This project was completed by Fathy Elhadidy, Shreya Sanjiv, and Bibin Benny from La Salle Univeristy. 
