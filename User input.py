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
myNumber=random.randint(1,10)
print('______________________________________________________________________________')
print('|                                                                            |')
print('|                                guess a number                              |')
print('|                                                                            |')
print('______________________________________________________________________________')
GameOn = True
#randint is random integer which is what we want
while(GameOn): #NEED COLON
    userGuess = int(input("Guess a number from 1-10 "))
    if myNumber == userGuess:
        print('You guessed it!')
        GameOn = False
    else: 
        print ('Good Luck next time!')
print ('The number to guess was ', myNumber)

#for if else statements, you have to use a colon at the end and also have a space in the line underneath
#Always have else on the same vertical line as the if.


