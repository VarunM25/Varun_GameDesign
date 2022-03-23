#Varun Mukund
#3/23/22

#main menu for the game, creating functions for menu
import pygame, time

pygame.init()

#Variable
WIDTH = 900
HEIGHT = 900
wb=30
hb=30

#lists for messages
Menulist=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Level 3', "Score Board", 'Exit']

#Get color
colors={'white':[255,255,255],'red':[255,0,0], 'orange' : [255,85,0], 'mag':[255,0,255], 'purple': [48,25,52], 'navy': [5,31,64], 'pink': [200,3,75], 'aqua' : [51,153,255], 'black': [0,0,0], 'mystery': [100,49,169], "mystery2" : [185, 23, 96]}
background = colors.get('white')
circlecolor=colors.get('orange')
hb_color = colors.get ('orange')
randColor = ''
sq_color = colors.get ('black')
#screen
wind =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Main Menu')


#Creating different types of fonts

TITLE_FNT=pygame.font.SysFont('Impact', 70)
MENU_FNT = pygame.font.SysFont('times new roman', 40)
INSTRUCTIONS_FNT = pygame.font.SysFont('comicsans', 25)

#Create Title
text= TITLE_FNT.render('MENU', 1, (255,0,0))
wind.fill((255,255,255))
#get width of text
#x value = WIDTH/2-wText/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(xt,50))

#Create first button


#create square for menu
xs = 50
ys = 250
square=pygame.Rect(xs,ys,wb,hb)
txty=243
for i in range(7):
    message = Menulist[i]
    text=MENU_FNT.render(message,1,(0,0,0))
    wind.blit(text,(90,txty))
    pygame.draw.rect(wind,sq_color,square)
    square.y+=50
    txty+=50
pygame.display.update()
pygame.time.delay(10000)


# text= MENU_FNT.render('-Instructions:', 1, (0,255,0))
# wind.blit(text,(20,100))
# text= INSTRUCTIONS_FNT.render('--> This is a two player game', 1, (0,0,0))
# wind.blit(text,(50,150))
# text= INSTRUCTIONS_FNT.render('--> One person is the circle, the other is the square', 1, (0,0,0))
# wind.blit(text,(50,200))
# text= INSTRUCTIONS_FNT.render('--> Use the arrow keys to operate the circle', 1, (0,0,0))
# wind.blit(text,(50,250))
# text= INSTRUCTIONS_FNT.render('--> Use the keys W (up) A (left) S (down) D (right) to operate the square', 1, (0,0,0))
# wind.blit(text,(50,300))
# text= INSTRUCTIONS_FNT.render('--> The circle is trying to "eat" the square while the square runs away', 1, (0,0,0))
# wind.blit(text,(50,350))
# text= TITLE_FNT.render('Return to Main Menu', 1, (0,0,0))
# wind.blit(text,(150,400))

