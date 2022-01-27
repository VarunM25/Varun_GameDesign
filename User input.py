#Varun Mukund
# 1/21/22

# We are going to learn the input () function, random numbers
# Type casting, branching, looping

#Declare variable for user input
import os, random
os.system('cls')
# print('enter a number from 1-10: ', end = "")
# userInfo=int(input())
# print('The number is %.2f'%(userInfo/3))
# #input is a string, so it won't multiply an integer - must convert to integer - must type cast if we need integer
# #If you want just a digit, use %d, but for decimals you need %.2f (float)

# guess=int(input('Please give me a number'))

#guess a number
# myNumber = 9 instead of using fixed number, we will use a random
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

RunGame = True
while(RunGame): 
    menu()
    Menu = True
    while(Menu):
        try:
            Gamelevel=int(input("This is the guessing game where YOU try to guess the number in MY head! \n Pick a Level: \n For Level 1 - Type \"1\" \n For Level 2 - Type \"2\" \n For Level 3 - Type \"3\" \n"))
            Menu = False
        except ValueError:
            print ('Sorry, wrong choice, try again  ¯\_(ツ)_/¯')

    if Gamelevel == 1:
        myNumber = random.randint(1,10)
        attempts = 5
    elif Gamelevel == 2:
        myNumber = random.randint(1,50)
        attempts = 10
    else:
        myNumber = random.randint (1,100)
        attempts = 15
    # print(myNumber)

    GameOn=True
    while(GameOn):
        if attempts == 1:
            GameOn = False
        else:
            GameOn = True
        print ('You have', attempts, ' attempts left. Use them wisely young one!')
        userGuess= input ('Guess the number: ')
        if str.isnumeric (userGuess):
            if myNumber == int(userGuess):
                print (' ')
                print ('THAT IS RIGHT!  (⌐■_■)')
                GameOn = False
            else:
                print ('  ')
                print ('Thats wrong (T_T)')
                if int(userGuess) < myNumber:
                    print ('You are almost there, just a little higher! (☞ﾟヮﾟ)☞')
                    attempts = attempts - 1
                elif int (userGuess) > myNumber:
                    print ('You are just a tad bit high there, arent ya mate? ☜(ﾟヮﾟ☜)')
                    attempts = attempts - 1
                print (' ')
                print ('... If you want to quit, type \"quit\" ...\n')
        elif str(userGuess) == 'quit':
            print (' ')
            print ('---------------')
            print ('Come back soon!')
            GameOn = False
        else:
            print('Wrong! If you give up type \"quit\" to finish')
            attempts = attempts - 1
        
    print ('The number was: ', myNumber)
    print (' ')
    print ('Credit to Toxicwarp3658 for the quit function\n')

    Restart = input('----Would you like to play again? Type \"yes\" or \"no\"----\n')
    if Restart.lower() ==str('no'):
        RunGame = False
        os.system ('cls')
        print ('We hope you come back later!! Have a FANTASTIC day! :-D')
        print (' ')
        print (' ')
       
    elif  Restart.lower() == str('yes'):
        print ('Restarting now')
        os.system ('cls')
        menu()
        

#for if else statements, you have to use a colon at the end and also have a space in the line underneath
#Always have else on the same vertical line as the if.

