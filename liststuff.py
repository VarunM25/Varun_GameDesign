#Varun Mukund
#2/16/22
import os, random
os.system ('cls')
fruits =['bananas', 'grapes', 'watermelon', 'blueberries', 'papaya', 'mango', 'oranges', 'tomatoes', 'strawberries', 'bananas', 'kiwis', 'blackberries']
#length of array
size = len(fruits)
print (size)
fruits.append ('rambutan')
for i in range (size+1):
    print (fruits[i])
print (fruits[size-1])
print (fruits [-2])
print (fruits.count('bananas'))
list2=[3,6,8,9,10]
fruits.append(list2)
print ("append \n", fruits)
#adds the entire list
fruits.pop(-1)
#deletes last index
fruits.extend(list2)
print('extend \n', fruits)
#adds each element to the original list
fruits.insert (2,'dragonfruit')
#inserts element into the list at a certain position 
print (fruits)