#Varun Mukund
#1/25/22
#This is notes on Ms. Suarez's Code

import random, os
os.system ('cls')
def menu():
    print('______________________________________________________________________________')
    print('|                                                                            |')
    print('|                                                                            |')
    print('|                                                                            |')
    print('|                            Guess a Number Menu                             |')
    print('|                              Level 1: 1-10                                 |')
    print('|                              Level 2: 1-50                                 |')
    print('|                              Level 3: 1-100                                |')
    print('|                                                                            |')
    print('______________________________________________________________________________')
#checkin for correct user input 

menu()     #calling the function menu
Menu = True
while(Menu):
    try:
        choice=int(input("Choice: "))
        Menu = False
    except ValueError:
        print ('Sorry, wrong choice, try again')

if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)
print(choice)
GameOn=True
while(GameOn):
    userGuess=int(input("give me a number "))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("good luck next time", myNumber)
print("The number to guess was " + str(myNumber))
os.system ('cls')
menu()