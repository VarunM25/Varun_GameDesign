#Varun Mukund
#Version 1 of Final Game
import os, pygame

os.system('cls')
pygame.init()
win=pygame.display.set_mode((500,480))
pygame.display.set_caption('Final Game')

#background variables
bg1 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd1.jpg'), (500,480))
bg2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd2.jpg'), (500,480))
bg3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd3.jpg'), (500,480))
bg4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd4.jpg'), (500,480))
bg5 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd5.jpg'), (500,480))