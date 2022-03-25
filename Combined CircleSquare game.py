#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square,
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               Jump
#initialize pygame
import os, random, time, pygame
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
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

#List for messages
MenuList=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Level 3', 'Scoreboard', 'Exit']
#Get colors
background= colors.get('blreen')

cr_color=colors.get('red')
randColor=''
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            sq_color= colors.get(randColor)
           
        else:
            colorCheck=False

changeColor()
sq_color= colors.get(randColor)
   






#Menu / Instructions



#create different type of fonts

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('arial.ttf', 40)
INST_FNT=pygame.font.SysFont('arial.ttf', 40)

text=TITLE_FNT.render('Menu', 1, (125,45,30))
screen.fill((255,255,255))

xt=WIDTH/2-text.get_width()/2
screen.blit(text,(xt,50))
#get the width of the text


#Create First Button


#Create square for menu
xs=50
ys=250
wb=50
hb=50

menu_sq=colors.get('black')

square=pygame.Rect(xs,ys,wbox,hbox)
txty=250
for i in range (7):
    message=MenuList[i]
    text=INST_FNT.render(message,1,(0,0,0))
    screen.blit(text,(90,txty))
    pygame.draw.rect(screen, menu_sq, square )
    square.y +=50
    txty+=50




pygame.display.update()

pygame.time.delay(1000)












# text=INST_FNT.render("---- W to Move Up ----")
# screen.blit(text,(50,250))
# text=INST_FNT.render("---- S to Move Down ----")
# screen.blit(text,(50,150))
# text=INST_FNT.render("---- A to Move Left ----")
# screen.blit(text,(50,100))
# text=INST_FNT.render("---- D to Move Right ----")







#jumping square
jump_move = 10
jumping = False
#Get colors
background = colors.get('pink')
circlecolor=colors.get('white')
hb_color = colors.get ('white')
randColor = ''
def changecolor():
    global randColor
    checkcolor = True
    while checkcolor:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            randColor=random.choice(list(colors))
        else:
            checkcolor = False
changecolor()
sqcolor=colors.get(randColor)
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
        changecolor()
        sqcolor=colors.get(randColor)
        square = pygame.Rect(xs,ys,wbox,hbox)
        rad+=10
        c_wbox+=13.5
        c_hbox+=13.5
        xh=xc-(rad/1.5)
        yh=yc-(rad/1.5)
        hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)
#jumping
    if jumping==False and keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        square.y-=jump_move
        jump_move-=1
        if jump_move< -10:
            jumping=False
            jump_move=10
    pygame.draw.rect(screen, sqcolor, square)
    pygame.draw.circle(screen,circlecolor,(xc,yc),rad)
    pygame.draw.rect(screen, hb_color, hitbox)
    pygame.display.update()
    pygame.time.delay(3)
