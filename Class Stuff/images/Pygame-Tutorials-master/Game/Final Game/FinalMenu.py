#Varun Mukund
#Version 1 of Final Game
import os, pygame, random, datetime

WIDTH = 700
HEIGHT = 700 

os.system('cls')
pygame.init()
name = input('What is your name: ')
win=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Final Game')
#Menu Booleans:
MAIN=True

GAME=False

INST=False

SETT=False

LEV_I=False

LEV_II=False

LEV_III=False

SCOREBOARD=False

EXIT=False

PROJECTILE = False

BKGD = False

BKGDIMG = False

MVMT = False

check = True

#Menu variables

wb_btn=30

hb_btn=30

xs_btn=50

ys_btn=250

MenuList=['Instruction','Setting','Level 1','Level 2','Level 3','Scoreboard','Exit']

SettingList=['Projectile Image','Background Color','Sound','Background Image', 'Movement Speed'] 

Projimage = ['Fireball', 'Meme', 'Explosion']

Mvmtspeed = ['Normal', 'Fast', 'Hyperspeed']

Bkgd = ['Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Black', 'White']

Bkgdimage = ['Forest', 'Desert', 'Space', 'Mars', 'Farm']
 

#define colors

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],

'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],

'black':[0,0,0],'white':[255,255,255]}

randColor=random.choice(list(colors))

 

#Get colors

background=colors.get('black')

cr_color=colors.get('white')

hb_color=colors.get('white')

sq_btn_color=colors.get('orange')

#Giving the square a random color


def ChangeColor():

    global randColor

    ColorCheck=True

    while ColorCheck:

        randColor=random.choice(list(colors))

        if colors.get(randColor)==background or colors.get(randColor)==cr_color:

            randColor=random.choice(list(colors))

        else:

            ColorCheck=False

ChangeColor()

sq_color=colors.get(randColor)

#Fonts

TITLE_FNT=pygame.font.SysFont('times new roman',80)

MENU_FNT=pygame.font.SysFont('courier',40)

INST_FNT=pygame.font.SysFont('calibri',25)

 

#Menu Screen Variables

def TitleMenu(Message):

    text=TITLE_FNT.render(Message,1,'green')

    win.fill(background)

    xt=WIDTH/2-text.get_width()/2

    win.blit(text,(xt,50))

square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)

 

def MainMenu(Mlist):

    ty=250

    square_button.y=250

    for i in range(len(Mlist)):

        message=Mlist[i]

        text=INST_FNT.render(message,1,'white')

        win.blit(text,(90,ty))

        pygame.draw.rect(win,sq_btn_color,square_button)

        square_button.y+=50

        ty+=50

    pygame.display.update()

    pygame.time.delay(1)

 

#instructions win variables

title=TITLE_FNT.render('Instructions',1,'green')

xt=WIDTH/2-title.get_width()/2

Instructions=MENU_FNT.render('Instructions:',1,'white')

inst1=INST_FNT.render('1) Shoot projectiles at your enemy to defeat them.',1,'white')

inst2=INST_FNT.render('2) Move forward by pressing "D".',1,'white')

inst3=INST_FNT.render('3) Jump with the Space Bar to dodge the enemy missiles.',1,'white')

inst4=INST_FNT.render('4) Press "F" to shoot a projectile.',1,'white')

inst5=INST_FNT.render('5) Kill the enemy robot.',1,'white')

 

#displaying instructions win

def instScreen():

    instr_Check=True

    while instr_Check:

        win.fill(background)

        for i in pygame.event.get():

            if i.type==pygame.QUIT:

                instr_Check=False

        keys=pygame.key.get_pressed() #this returns a list

        if keys[pygame.K_ESCAPE]:

            instr_Check=False

        else:

            win.blit(title,(xt,50))

            win.blit(Instructions,(200,200))

            win.blit(inst1,(10,300))

            win.blit(inst2,(10,350))

            win.blit(inst3,(10,400))

            win.blit(inst4,(10,450))

            win.blit(inst5,(10,500))

        pygame.display.update()

        pygame.time.delay(1)

def keepScore(score):

    date=datetime.datetime.now()

    scoreLine=str(score)+'\t'+name+'\t'+date.strftime('%m/%d/%Y'+'\n')

    #open a file and write

    #when you write it erases the previous text

    myFile=open('Class Stuff\Circle Eats Square\\final.txt','a')

    myFile.write(scoreLine)

    myFile.close()
while check:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False 

        if event.type==pygame.MOUSEBUTTONDOWN:

            mouse_pos=pygame.mouse.get_pos()

            print(mouse_pos)

            xm = mouse_pos[0]

            ym = mouse_pos[1]
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        pygame.display.set_caption('Menu')
        win.fill(background)
        TitleMenu("Circle eats Square")
        MainMenu(MenuList)

    if INST:

        pygame.display.set_caption('Instructions')

        TitleMenu("INSTRUCTIONS")

        instScreen()

        if keys[pygame.K_ESCAPE]:
            INST = False
            MAIN = True


    if SETT:

        pygame.display.set_caption('Settings')

        TitleMenu("SETTINGS")

        MainMenu(SettingList)
        if keys[pygame.K_ESCAPE]:
            SETT = False
            MAIN = True

    if LEV_I:

        pygame.display.set_caption('Level 1')

        # Game()
        if keys[pygame.K_ESCAPE]:
            LEV_I = False
            MAIN = True

    if LEV_II:

        pygame.display.set_caption('Level 2')

        bombvel = 20
        
        # Game()

        if keys[pygame.K_ESCAPE]:
            LEV_II = False
            MAIN = True

    if LEV_III:

        pygame.display.set_caption('Level 3')

        bombvel = 30
        
        # Game()

        if keys[pygame.K_ESCAPE]:
            LEV_III = False
            MAIN = True

    if SCOREBOARD:

        pygame.display.set_caption('Scoreboard')

        TitleMenu("SCOREBOARD")

        myFile=open('Class Stuff\Circle Eats Square\\final.txt','r')

        scoreboardlines = myFile.readlines()

        texty = 250

        for i in range (len(scoreboardlines)):

            newscoreline = MENU_FNT.render(scoreboardlines[i],1, 'white')

            win.blit(newscoreline,(90, texty))

            texty +=50

        pygame.display.update() 

        if keys[pygame.K_ESCAPE]:
            SCOREBOARD = False
            MAIN = True

    if PROJECTILE:

        pygame.display.set_caption('Projectile Image')

        TitleMenu("Projectile")

        MainMenu(Projimage)

        if keys[pygame.K_ESCAPE]:
            PROJECTILE = False
            SETT = True

    if BKGD:

        pygame.display.set_caption('Background Colors')

        TitleMenu("Background")

        MainMenu(Bkgd)

        if keys[pygame.K_ESCAPE]:
            BKGD = False
            SETT = True
        


    if MVMT:

        pygame.display.set_caption('Movement Speed')

        TitleMenu("Speed")

        MainMenu(Mvmtspeed)

        if keys[pygame.K_ESCAPE]:
            MVMT = False
            SETT = True
    
    if BKGDIMG:
        pygame.display.set_caption('Background Image')

        TitleMenu('Bkgd Image')

        MainMenu(Bkgdimage)

        if keys[pygame.K_ESCAPE]:
            BKGDIMG = False
            SETT = True


    if EXIT:

        TitleMenu("Game Over")


        keepScore(Gamescore)

        check = False





    if MAIN and ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:

        MAIN=False

        INST=True

    if MAIN and ((xm >20 and xm <80) and (ym >300 and ym <340))and MAIN :

        MAIN=False

        SETT=True

    if MAIN and ((xm >20 and xm <80) and (ym >350 and ym <390))and MAIN :

        MAIN=False

        LEV_I=True

    if MAIN and ((xm >20 and xm <80) and (ym >400 and ym <440))and MAIN :

        MAIN=False

        LEV_II=True

    if MAIN and ((xm >20 and xm <80) and (ym >450 and ym <490))and MAIN :

        MAIN=False

        LEV_III=True

    if MAIN and ((xm >20 and xm <80) and (ym >500 and ym <540))and MAIN :

        MAIN=False

        SCOREBOARD=True

    if MAIN and ((xm >20 and xm <80) and (ym >550 and ym <590))and MAIN :

        MAIN=False

        EXIT=True


    if SETT and ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT:

        SETT=False

        PROJECTILE=True

    if PROJECTILE and ((xm >20 and xm <80) and (ym >250 and ym <290)) and PROJECTILE:
        
        fireball = pygame.image.load('Class Stuff\images\Fireball\\fireball_02.png')

    if PROJECTILE and ((xm >20 and xm <80) and (ym >300 and ym <340))and PROJECTILE :

        fireball = pygame.image.load('Class Stuff\images\Fireball\meme.png')            

    if PROJECTILE and ((xm >20 and xm <80) and (ym >350 and ym <390))and PROJECTILE :

        fireball = pygame.image.load('Class Stuff\images\Fireball\hit-effectnew.png')
    
    if SETT and ((xm >20 and xm <80) and (ym >300 and ym <340))and SETT :

        SETT=False

        BKGD=True

    if BKGD and ((xm >20 and xm <80) and (ym >250 and ym <290)) and BKGD:

        background=colors.get('red')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >300 and ym <340))and BKGD :

        background=colors.get('green')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >350 and ym <390))and BKGD:

        background=colors.get('blue')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >400 and ym <440))and BKGD:

        background=colors.get('cyan')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >450 and ym <490))and BKGD:

        background=colors.get('magenta')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >500 and ym <540))and BKGD:

        background=colors.get('black')

        pygame.display.update()

    if BKGD and ((xm >20 and xm <80) and (ym >550 and ym <590))and BKGD:

        background=colors.get('white')

        pygame.display.update()

    if SETT and ((xm >20 and xm <80) and (ym >400 and ym <440))and SETT :

        SETT=False

        BKGDIMG=True

    if BKGDIMG and ((xm >20 and xm <80) and (ym >250 and ym <290)) and BKGDIMG:

        bg = bg

    if BKGDIMG and ((xm >20 and xm <80) and (ym >300 and ym <340)) and BKGDIMG:

        bg = bg2

    if BKGDIMG and ((xm >20 and xm <80) and (ym >350 and ym <390)) and BKGDIMG:

        bg = bg3

    if BKGDIMG and ((xm >20 and xm <80) and (ym >400 and ym <440)) and BKGDIMG:

        bg = bg4

    if BKGDIMG and ((xm >20 and xm <80) and (ym >450 and ym <490)) and BKGDIMG:

        bg = bg5


    if SETT and ((xm >20 and xm <80) and (ym >450 and ym <490))and SETT :

        SETT=False

        MVMT=True

    if MVMT and ((xm >20 and xm <80) and (ym >250 and ym <290)) and MVMT:
        
        vel = 6

    if MVMT and ((xm >20 and xm <80) and (ym >300 and ym <340))and MVMT :

        vel = 8

    if MVMT and ((xm >20 and xm <80) and (ym >350 and ym <390))and MVMT :

        vel = 10


        

    if keys[pygame.K_LSHIFT]:

        BKGD = False

        SETT = True
    if keys[pygame.K_ESCAPE]:

            GAME=False

            INST=False

            SETT=False

            LEV_I=False

            LEV_II=False

            LEV_III=False

            SCOREBOARD=False

            EXIT=False

            PROJECTILE = False

            BKGD = False

            BKGDIMG = False

            MVMT = False

            MAIN=True


    pygame.display.update()

    pygame.time.delay(1)

