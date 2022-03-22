#Varun Mukund
import pygame, time

pygame.init()
wind =pygame.display.set_mode((900,900))
pygame.display.set_caption('Font Testing')


#Creating different types of fonts

TITLE_FNT=pygame.font.SysFont('Impact', 70)
MENU_FNT = pygame.font.SysFont('times new roman', 50)
INSTRUCTIONS_FNT = pygame.font.SysFont('comicsans', 25)
text= TITLE_FNT.render('Circle Eats Square Game', 1, (255,0,0))
wind.fill((255,255,255))
wind.blit(text,(0,20))
text= MENU_FNT.render('-Instructions:', 1, (0,255,0))
wind.blit(text,(20,100))
text= INSTRUCTIONS_FNT.render('--> This is a two player game', 1, (0,0,0))
wind.blit(text,(50,150))
text= INSTRUCTIONS_FNT.render('--> One person is the circle, the other is the square', 1, (0,0,0))
wind.blit(text,(50,200))
text= INSTRUCTIONS_FNT.render('--> Use the arrow keys to operate the circle', 1, (0,0,0))
wind.blit(text,(50,250))
text= INSTRUCTIONS_FNT.render('--> Use the keys W (up) A (left) S (down) D (right) to operate the square', 1, (0,0,0))
wind.blit(text,(50,300))
text= INSTRUCTIONS_FNT.render('--> The circle is trying to "eat" the square while the square runs away', 1, (0,0,0))
wind.blit(text,(50,350))
text= TITLE_FNT.render('HAVE FUN!!!', 1, (0,0,0))
wind.blit(text,(250,400))
pygame.display.update()
pygame.time.delay(10000)
