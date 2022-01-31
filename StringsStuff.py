#Varun Mukund
#1/31/22
#Strings are arrays of characters
#Has Many Functions
import os
os.system ('cls')
myName = "Varun Mukund"
myStatement = """My name is very nice because
whatever yay yay happy 

idk what im typing"""
#^^^ IF I USE TRIPLE QUOTATION MARKS - IT PRINTS EXACTLY HOW I TYPE (WITH THE SPACES AND EVERYTHING)
print (myName[6])
#^^ It takes the 6th letter and prints it
print (myStatement)
if 'yay' in myStatement:
    print ('true')
#Checks if the word is there then will give a output
print ('expert' not in myStatement)
#not in or in will make it check the statemtn and will print true or false depending on ur code
