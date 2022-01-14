import os
# Varun P Mukund 
# Jan 14, 2022
# Declare variables, print variables, print types of data, learn some operators
# Hashtags are for comments --> computer will ignore 

# Program is the Average of 3 tests
# I want to clear my terminal
os.system('cls')
# Declare and Assign values
test1=89
test2=78.5
test3=86
Flag=False

# to display things on the screen, use function "print()"

# print(type(test1), type(test2), type(Flag))

#Declare Sum to add tests - symbol for addition is +
Sum = test1 + test2 + test3 
#Average - use division --> "/"
# print('The Sum is', Sum)
Average= Sum/3
print("Test 1 =", test1, end=" ")
print("Test 2 =", test2, end=" ")
# end=" " puts the display on the same line of text instead of going to a new line under
print("Test 3 =", test3)
print('The Sum is', Sum)
print('The average of your 3 tests is', Average)

#I want to print  "The average" - use quotation marks (shown above)
