#Varun Mukund
#Version 1 of Final Game
import os, pygame, random, datetime, time

WIDTH = 700
HEIGHT = 700 

os.system('cls')
name=input('Enter your name: ')
pygame.init()
win=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Final Game')

#background variables
bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd1.jpg'), (700,700))
bg2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd2.png'), (700,700))
bg3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd3.png'), (700,700))
bg4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd4.png'), (700,700))
bg5 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd5.jpg'), (700,700))

# Character movements
char = pygame.transform.scale(pygame.image.load('Class Stuff\images\Idle-stance_04.png'), (64,64))
attacking = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_07.png'), (64,64))]
running = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_07.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_08.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_09.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_03.png'), (64,64))]
jumping = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_03.png'), (64,64))]
crouching = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_03.png'), (64,64))]
thwomp = pygame.image.load('Class Stuff\images\Bad dudes\\thwomp.png')
fireball = pygame.image.load('Class Stuff\images\Fireball\\fireball_02.png')

#robots/bad guys
badrobot = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\smallbaddude1.png'), (180,180))
badrobot2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude3.png'), (180,180))
badrobot3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude1.png'), (180,180))
badrobot4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude2.png'), (180,180))
bossrobot = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\Reallybaddude.png'), (180,180))
golem = pygame.image.load('Class Stuff\images\Bad dudes\Golem1.png')
thwomp = pygame.transform.scale(pygame.image.load('Class Stuff\images\Bad dudes\\thwomp.png'), (30,30))
bomb = pygame.transform.scale(pygame.image.load('Class Stuff\images\Fireball\\newbomb.png'), (50,50))
explosion = pygame.transform.scale(pygame.image.load('Class Stuff\images\Fireball\hit-effectnew.png'), (20,20))
meme = pygame.transform.scale(pygame.image.load('Class Stuff\images\Fireball\meme.png'), (20,20))
#Booleans:
Area1 = True
Area2 = False
Area3 = False
Area4 = False
Area5 = False
test = False
attack = False
idle = True
explode = False
bad = True
bombing = True
check = True
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

xm=0
ym=0
clock=pygame.time.Clock()
isJump=False
jumpCount=10
right=False
walkCount=0
attackCount=0




char_hb = 60
char_wb = 40
xc = 15
yc = HEIGHT-64
char_hitbox = pygame.Rect(xc,yc,char_wb,char_hb)
vel=7 
badxc = WIDTH-180
badyc = HEIGHT-160
bad_wb = 180
bad_hb = 180
barrier_wb = bad_wb
barrier_xc = badxc
barrier_yc = 0
barrier_hb = HEIGHT
bad_hitbox = pygame.Rect(badxc,badyc,bad_wb,bad_hb)
xf = char_hitbox.x 
yf = char_hitbox.y 
wf = 30
hf = 30
projhitbox = pygame.Rect(xf,yf,wf,hf)
projectile_vel = 7
barrier = pygame.Rect(barrier_xc,barrier_yc,barrier_wb, barrier_hb)
healthy = badyc-50
healthw = 100
healthh = 20
healthbar = pygame.Rect(badxc, healthy, healthw, healthh)
bombnumber = random.randint(1, 10)
# Just creates a color for the health bar
green=(18,230,3)
run = True
key = False
bombx = WIDTH-150
bomby = HEIGHT-80
bombw = 50
bombh = 50
bombhitbox = pygame.Rect(bombx,bomby,bombw,bombh)
bombvel = 10

def Game():
    global char_hb, char_wb, xc, yc, char_hitbox, vel, badxc, badyc, bad_wb, bad_hb, barrier_wb, barrier_xc, barrier_yc, barrier_hb, bad_hitbox, xf, yf, wf, hf, projhitbox, projectile_vel, barrier, healthy
    global healthw, healthh, healthbar, bombnumber, green, run, key, bombx, bomby, bombw, bombh, bombhitbox, bombvel, Area1, bad, bombing, walkCount, right, attack, isJump
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        if Area1:
            pygame.draw.rect(win, (0,0,0), barrier, 3)
            pygame.draw.rect(win,(255,255,255), char_hitbox, 3)
            pygame.draw.rect(win, (0,0,0), projhitbox, 3)
            win.blit(bg,(0,0))
            if bad:
                win.blit(badrobot, (badxc,badyc))
        
            if bombing:
                if healthw>0:
                    win.blit(bomb, (bombx, bomby))
                    bombx -= 10
                    bombhitbox.x -= 10
                    print (bombhitbox.x)
                    if bombhitbox.x <= 0:
                        bombx = WIDTH-150
                        bombhitbox.x = WIDTH-150
                        win.blit(bomb, (bombx, bomby))  
                        bombx -= bombvel
                        bombhitbox.x -= bombvel
                    if not bombhitbox.colliderect(char_hitbox):
                        run = True
                    else: 
                        run = False
                else:
                    bombing = False



            pygame.draw.rect (win,(0,255,0), healthbar, 100)
            if walkCount+1>=27:
                walkCount=0          
            elif right:
                win.blit(running[walkCount//3],(xc,yc))
                walkCount+=1
            else:
                if idle:
                    win.blit(char,(xc, yc))
                    walkCount=0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                attack=True
            # for i in range (len(attacking)):
            if attack:
                
                win.blit(fireball,(xf,yf))
                xf+= projectile_vel
                projhitbox.x+= projectile_vel
            if projhitbox.colliderect(barrier):
                healthw = healthw-20
                healthbar = pygame.Rect(badxc, healthy, healthw, healthh)
                attack = False
                xf = char_hitbox.x
                projhitbox.x = char_hitbox.x  
                yf = char_hitbox.y 
                projhitbox.y = char_hitbox.y
                if healthw <= 0:
                    bad = False
                    pygame.time.get_ticks
            if keys[pygame.K_d] :# and not barrier.colliderect(char_hitbox):
                key = True 
                if xc < WIDTH - vel - 64:
                    char_hitbox.x += vel
                    xc+=vel
                    right = True
                elif Area1: # will get executed only when the char is at the end fo the screen
                    xc=0
                    Area1=False
                    Area2=True
                    char_hitbox.x = 0
                # elif Area2:
                #     xc=0
                #     Area2=False
                #     Area3=True   
                #     char_hitbox.x = 0 
                # elif Area3:
                #     xc=0
                #     Area3=False
                #     Area4=True 
                #     char_hitbox.x = 0
                if healthw > 0:
                    if barrier.colliderect(char_hitbox):
                        vel = 0
                else:
                    vel = 7

            else:
                right = False
                walkCount = 0
            if not(isJump):
                if keys[pygame.K_SPACE]:
                    isJump = True
                    walkCount = 0
            else:
                if jumpCount >= -10:
                    char_hitbox.y -= (jumpCount * abs(jumpCount)) * 0.5
                    yc -= (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 1
                    char_hitbox.y=yc
                else:
                    jumpCount = 10
                    isJump = False

                        

            #print (Area1)
            pygame.display.update()
            key = False
            pygame.quit()
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

    if SETT:

        pygame.display.set_caption('Settings')

        TitleMenu("SETTINGS")

        MainMenu(SettingList)

    if LEV_I:

        pygame.display.set_caption('Level 1')

        Game()

    if LEV_II:

        pygame.display.set_caption('Level 2')

        bombvel = 20
        
        Game()

    if LEV_III:

        pygame.display.set_caption('Level 3')

        bombvel = 30
        
        Game()

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

    if PROJECTILE:

        pygame.display.set_caption('Projectile Image')

        TitleMenu("Projectile")

        MainMenu(Projimage)

    if BKGD:

        pygame.display.set_caption('Background Colors')

        TitleMenu("Background")

        MainMenu(Bkgd)


    if MVMT:

        pygame.display.set_caption('Movement Speed')

        TitleMenu("Speed")

        MainMenu(Mvmtspeed)
    
    if BKGDIMG:
        pygame.display.set_caption('Background Image')

        TitleMenu('Bkgd Image')

        MainMenu(Bkgdimage)


    if EXIT:

        TitleMenu("Game Over")
        if #level1>0 and level2score>0 and level3score>0
        # Create stopwatch for each level
            Gamescore = 

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



    