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
Gamelevel = int(input('Pick a level for the game: \n for level 1 (1-10) type 1 \n for level 2 (1-50) type 2 \n for level 3 (1-100) type 3\n'))
if Gamelevel == 1:
    myNumber = random.randint(1,10)
elif Gamelevel == 2:
    myNumber = random.randint(1,50)
else:
    myNumber = random.randint (1,100)
# print(myNumber)

GameOn=True
while(GameOn):
    userGuess= input ('Guess the number: ')
    if str.isnumeric (userGuess):
        if myNumber == int(userGuess):
            print ('THAT IS RIGHT!')
            GameOn = False
        else:
            print ('Thats wrong... If you want to quit, type \"quit\"')
            if int(userGuess) < myNumber:
                print ('Almost there, just a little higher!')
            elif int (userGuess) > myNumber:
                print ('Just a tad bit high there, arent ya mate?')
    elif str(userGuess) == 'quit':
        print ('Come back soon!')
        GameOn = False
    
print ('The number was: ', myNumber)
print ('Credit to Toxicwarp3658 for the quit function')

#for if else statements, you have to use a colon at the end and also have a space in the line underneath
#Always have else on the same vertical line as the if.

