#Varun Mukund
#2/2/22
from modulefinder import IMPORT_NAME
import os,random, time
word = ""
guess = ""
os.system ('cls')
def menu():
    print ("""        
    ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
    ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
    ▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
    ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒  OWOOOOOOOOOOOO! You have entered the chamber of doom, where frustration meets word games...
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
    """)
    level = input('Pick a level from the three above...or else...(scroll up): ')
    if int(level) == 1:
        selectWord1()
        guessFunction()
    elif int(level) ==2:
        selectWord2()
        guessFunction()
    elif int(level) ==3:
        selectWord3()
        guessFunction()
    # print (word)
def selectWord1():
    global word
    os.system('cls')
    Bball =["westbrook", 'lebron', 'durant', 'harden', 'kyrie', 'doncic', 'giannis', 'ja', 'curry','kobe', 'jordan']
    word = random.choice (Bball)
def selectWord2():
    global word
    os.system('cls')
    Veggies =["cucumber", 'carrot', 'broccoli', 'potato', 'radishes', 'pumpkin', 'squash']
    word = random.choice (Veggies)
def selectWord3():
    global word
    os.system('cls')
    Comp =['motherboard', 'cpu', 'microprocessor', 'ram', 'firewall', 'monitor', 'keyboard', 'mouse', 'trackpad']
    word = random.choice (Comp)

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

menu()



GameOn = True
def restart():
    playagain = input('Do you want to LOSE- I mean play again? Yes(1) or No(2)\n p.s. if you type anything, and I mean ANYTHING, else I am sending you back into the death maze - I mean game...')
    if int(playagain) == 2:
        os.system('cls')
        print ('You had', points, 'points')
        print ('Come back soon... to meet your doom')
        GameOn = False
    else:
        os.system('cls')
        print ('restarting...')
        time.sleep (2)
        menu()
tries = 0
points = 0
letterGuessed = ""
while GameOn:
    guessFunction()
    letterGuessed += guess #same as letterguessed = letterguessed + guess
    if guess not in word:
        tries +=1
        print ('You have', 7-tries, 'attempts left... use them wisely...')
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print (letter, end=" ")
            countLetter +=1
        else:
            print ('_', end= " ")
    if countLetter ==len(word):
        os.system ('cls')
        print ('\nHOW?! HOW DID YOU WIN...I will have my revenge')
        if tries < 2:
            print ('You got 5 points...')
            points += 5
            print ('You now have', points, 'points')
        elif tries >2 and tries <5:
            print ('You got 2 points...')
            points += 2
            print ('You now have', points, 'points')
        restart()
    elif tries >6:
        os.system('cls')
        print ('\nHA HA HA, you ran out of tries. Now let me call my brothers... we will feast on your remains... AWOOOOOOOOOO\n AND YOU GET NO POINTS HAHAHHAAH')
        restart()





