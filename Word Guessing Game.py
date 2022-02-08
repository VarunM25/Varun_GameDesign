#Varun Mukund
#2/2/22
from modulefinder import IMPORT_NAME
import os,random, time
word = ""
guess = ""
def selectWord():
    global word
    os.system('cls')
    fruits =["bananas", 'grapes', 'watermelon', 'blueberries', 'apples', 'papaya', 'oranges', 'tomatoes', 'mangoes','kiwis', 'strawberries']
    # size = len(fruits)
    # Random = random.randint (0,size)
    # print (Random)
    # word = fruits[Random]
    # print (word)
    word = random.choice (fruits)
    
def guessFunction():
    global guess
    check = True
    while check:
        try:
            guess = input("\nenter a letter to guess the word: ")
            if guess.isalpha() and len(guess) ==1:
                check = False
            else:
                print ('Only one letter please')
        except ValueError:
            print ('only one letter please')
GameOn = True
tries = 0
letterGuessed = ""
selectWord()
while GameOn:
    guessFunction()
    letterGuessed += guess #same as letterguessed = letterguessed + guess
    if guess not in word:
        tries +=1
        print (tries) #for testing purposes
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print (letter, end=" ")
            countLetter +=1
        else:
            print ('_', end= " ")
    if tries >6:
        print ('\nSorry, you ran out of attempts! Come back soon')
        #playGame() #ask user if they want to play again
    if countLetter == len(word):
        print ('\nYOU WON')
        #Calculate Score
        #playGame() to see if they want to play again


print ("""▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒        
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒    
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒  OWOOOOOOOOOOOO! You have entered the chamber of doom, where frustration in word games...
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒  In this game, you will guess a word, that I CHOOSE, with NO HELP whatsoever
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒  Before you start, pick a level! (Type the number near the level)
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒            1 - Basketball Players
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒            2 - Vegetables
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒            3 - Computer Parts
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████

(scroll up if you are down here)""")



