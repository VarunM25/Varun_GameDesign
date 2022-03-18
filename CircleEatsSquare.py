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
move =1
#square variable
xs=20
ys=20
wbox=30
hbox=30

#circle variables
rad=15
xc=random.randint(rad,WIDTH-rad)
yc=random.randint(rad,HEIGHT-rad)

#circle hitbox
c_wbox = 20
c_hbox = 20
xh = xc-(rad/1.5)
yh = yc-(rad/1.5)
hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)

#creating the rectangle
square =pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle Eats Square')

#define colors
colors={'white':[255,255,255],'red':[255,0,0], 'orange' : [255,85,0], 'mag':[255,0,255], 'purple': [48,25,52], 'navy': [5,31,64], 'pink': [200,3,75], 'aqua' : [51,153,255], 'black': [0,0,0], 'mystery': [100,49,169]}

#Get colors
background = colors.get('pink')
sqcolor=colors.get('aqua')
circlecolor=colors.get('white')
hb_color = colors.get ('white')
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
    if keys [pygame.K_w] and square.y>=move:
        square.y -= move
    if keys [pygame.K_s] and square.y<= HEIGHT-(hbox+move):
        square.y += move
#Circle movement
    if keys [pygame. K_LEFT] and xc >=move:
        xc-=move
        hitbox.x-=move
    if keys [pygame. K_RIGHT] and xc <= WIDTH -move:  
        xc+=move
        hitbox.x+=move
    if keys [pygame. K_UP] and yc >=move:  
        yc-=move
        hitbox.y-=move
    if keys [pygame. K_DOWN] and yc <= HEIGHT -move:
        yc+=move
        hitbox.y+=move 
#collisions
    if square.colliderect(hitbox):
        xs=random.randint(0,WIDTH-wbox)
        ys=random.randint(0, HEIGHT-hbox)
        square = pygame.Rect(xs,ys,wbox,hbox)
        rad+=10
        c_wbox+=13.5
        c_hbox+=13.5
        xh=xc-(rad/1.5)
        yh=yc-(rad/1.5)
        hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)
    pygame.draw.rect(screen, sqcolor, square)
    pygame.draw.circle(screen,circlecolor,(xc,yc),rad)
    pygame.draw.rect(screen, hb_color, hitbox)
    pygame.display.update()
    pygame.time.delay(3)






