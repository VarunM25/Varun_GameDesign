#Varun Mukund 3/8/22
#Learning how to draw cirlces and rectangles
#use keys to move objects
#use dictionaries

#Objective of game is basically pac-man

import os, time, random, pygame
pygame.init() 

#declare constants, variables, list, dictionaries, any object

#screen size
WIDTH = 700
HEIGHT = 700
check =True
move =5
#square variable
xs=20
ys=20
wbox=30
hbox=30

#circle variables
rad=15
xc=random.randint(rad,WIDTH-rad)
yc=random.randint(rad,HEIGHT-rad)

#creating the rectangle
square =pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle Eats Square')

#define colors
colors={'white':[255,255,255],'red':[255,0,0], 'orange' : [255,85,0], 'mag':[255,0,255], 'purple': [48,25,52], 'navy': [5,31,64], 'pink': [200,3,75], 'aqua' : [51,153,255], 'black': [0,0,0], 'mystery': [100,49,169]}

#Get colors
background = colors.get('pink')
sqcolor=colors.get('navy')
circlecolor=colors.get('white')
while check:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            check = False

    keys = pygame.key.get_pressed() #this returns a list
    if keys [pygame.K_a] and square.x >= move:
        square.x-= move
    if keys [pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move 
    if keys [pygame.K_w]:
        square.y -= move
    if keys [pygame.K_s]:
        square.y += move        
    pygame.draw.rect(screen, sqcolor, square)
    pygame.draw.circle(screen,circlecolor,(xc,yc),rad)

    pygame.display.update()
    pygame.time.delay(10)






