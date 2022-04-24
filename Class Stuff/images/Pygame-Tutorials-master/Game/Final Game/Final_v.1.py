#Varun Mukund
#Version 1 of Final Game
import os, pygame

os.system('cls')
pygame.init()
win=pygame.display.set_mode((700,600))
pygame.display.set_caption('Final Game')

#background variables
bg1 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd1.jpg'), (700,600))
bg2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd2.jpg'), (700,600))
bg3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd3.jpg'), (700,600))
bg4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd4.jpg'), (700,600))
bg5 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd5.jpg'), (700,600))

#Characters

char = pygame.image.load('Class Stuff\images\Idle-stance_04.png')
attacking = [pygame.image.load('Class Stuff\images\Attacking_01.png'), pygame.image.load('Class Stuff\images\Attacking_02.png'), pygame.image.load('Class Stuff\images\Attacking_03.png'), pygame.image.load('Class Stuff\images\Attacking_04.png'), pygame.image.load('Class Stuff\images\Attacking_05.png'), pygame.image.load('Class Stuff\images\Attacking_06.png'), pygame.image.load('Class Stuff\images\Attacking_07.png')]
running = [pygame.image.load('Class Stuff\images\Running_01.png'), pygame.image.load('Class Stuff\images\Running_02.png'), pygame.image.load('Class Stuff\images\Running_03.png'), pygame.image.load('Class Stuff\images\Running_04.png'), pygame.image.load('Class Stuff\images\Running_05.png'), pygame.image.load('Class Stuff\images\Running_06.png'), pygame.image.load('Class Stuff\images\Running_07.png'), pygame.image.load('Class Stuff\images\Running_08.png'), pygame.image.load('Class Stuff\images\Running_09.png'), pygame.image.load('Class Stuff\images\Running2_01.png'), pygame.image.load('Class Stuff\images\Running2_02.png'), pygame.image.load('Class Stuff\images\Running2_03.png')]
jumping = [pygame.image.load('Class Stuff\images\Jumping_01.png'), pygame.image.load('Class Stuff\images\Jumping_02.png'), pygame.image.load('Class Stuff\images\Jumping_03.png')]
crouching = [pygame.image.load('Class Stuff\images\crouching_01.png'), pygame.image.load('Class Stuff\images\crouching_02.png'), pygame.image.load('Class Stuff\images\crouching_03.png')]
thwomp = [pygame.image.load('Class Stuff\images\\thwomp.png')]
fireball = [pygame.image.load('Class Stuff\images\\fireball_02.png')]


Area1 = True
Area2 = False
Area3 = False
Area4 = False
Area5 = False