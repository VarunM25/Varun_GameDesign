#Varun Mukund
#Learning Files:
#a)open/create a file
#b) write "w"
#c) append "a"
#d) read 'r'
#e) close()
import pygame, os, datetime
os.system ('cls')
date = datetime.datetime.now()
score = 123
name = 'Jesse'
print (date.strftime('%m/%d/%Y'))
newdate = date.strftime('%m/%d/%Y')
scoreline=str(score)+' '+name+' '+ newdate
print(scoreline)
#open a file and write in it
myFile=open('Class Stuff\Circle Eats Square\sce.txt', 'w')
myFile.write(scoreline)
myFile.close()
score = 345
name = 'Jay'
print(date.strftime('%m,%d,%Y'))
scoreline=str(score)+' '+name+' '+ newdate
print(scoreline)
#open a file and write in it
myFile=open('Class Stuff\Circle Eats Square\sce.txt', 'a')
myFile.write(scoreline)
myFile.close()
myFile=open('Class Stuff\Circle Eats Square\sce.txt', 'r')
lines = myFile.readline()
print (lines)
lines = myFile.readline()
print (lines)
myFile.close()
