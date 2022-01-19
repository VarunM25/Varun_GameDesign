#Varun Mukund
# 1/19/2022

# We are going to learn other operatiors +-*/   ** exponent   %modulus 
#                           format printing   escape character

# Program creating an equation, asking user input, and formatting the output

import os
os.system('cls')
#Declare variable:
var1= input('Enter value for the first variable:')
var2= input('Enter value for the second variable:')
var3= input('Enter value for the third variable:')
var4= input('Enter value for the fourth variable:')

#Calculate equation given
# print(2**4)
result= (3*float(var1) - 2*float(var2)**2/float(var3))/float(var4)
print('The first variable = %5.2f'% float(var1))
print('The second variable = %5.2f'% float(var2))
print('The third variable = %5.2f'% float(var3))
print('The fourth variable = %5.2f'% float(var4))
#The reason we put the percentage and the % 5d is to give 5 spaces to each digit so it all prints in a nice straight line
#all of the percentages are for formatting
print('Result = %6.2f'% result)
#"f" in %6.2f tells us it is the float point

#in order to print quotation marks put backslash quotation (\")
# In order to print tabs (\t)
# In order to print backslash (\\)