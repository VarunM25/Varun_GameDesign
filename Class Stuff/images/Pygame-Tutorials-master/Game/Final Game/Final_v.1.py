#Varun Mukund
#Version 1 of Final Game
import os, pygame

WIDTH = 700
HEIGHT = 600 

os.system('cls')
pygame.init()
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Final Game')

#background variables
bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd1.jpg'), (700,600))
bg2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd2.png'), (700,600))
bg3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd3.png'), (700,600))
bg4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd4.png'), (700,600))
bg5 = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd5.jpg'), (700,600))

# Character movements
char = pygame.transform.scale(pygame.image.load('Class Stuff\images\Idle-stance_04.png'), (64,64))
attacking = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking_07.png'))]
running = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_07.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_08.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running_09.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running2_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running2_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running2_03.png'), (64,64))]
jumping = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping_03.png'))]
crouching = [pygame.transform.scale(pygame.image.load('Class Stuff\images\crouching_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\crouching_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\crouching_03.png'))]
thwomp = [pygame.image.load('Class Stuff\images\\thwomp.png')]
fireball = [pygame.image.load('Class Stuff\images\\fireball_02.png')]

#robots/bad guys
badrobot1 = [pygame.image.load('Class Stuff\images\smallbaddude1.png')]
badrobot2 = [pygame.image.load('Class Stuff\images\\bigbaddude3.png')]
badrobot3 = [pygame.image.load('Class Stuff\images\\bigbaddude1.png')]
badrobot4 = [pygame.image.load('Class Stuff\images\\bigbaddude2.png')]
bossrobot = [pygame.image.load('Class Stuff\images\Reallybaddude.png')]
golem = [pygame.image.load('Class Stuff\images\Golem1.png')]

#Booleans:
Area1 = True
Area2 = False
Area3 = False
Area4 = False
Area5 = False
test = False

clock=pygame.time.Clock()
isJump=False
jumpCount=10
right=False
walkCount=0




char_hb = 40
char_wb = 40
xc = 15
yc = HEIGHT-64
# hitbox = pygame.Rect(xc,yc,char_wb,char_hb)
vel=5



def gamewindow(key):
    global walkCount, Area1, Area2, Area3, Area4, Area5, bg, right, xc, KEY
    if Area2:
        print (xc)
        bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd2.png'), (700,600))
        if key:  
            
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                
                xc=0
                Area2=False
                Area3=True
    if Area3:
        bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd3.png'), (700,600))
        if key:  
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                xc=0
                Area3=False
                Area4=True
    if Area4:
        bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd4.png'), (700,600))
        if key:  
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                xc=0
                Area4=False
                Area5=True
    if Area5:
        bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd5.jpg'), (700,600))
    win.blit(bg,(0,0))
    if walkCount+1>=27:
        walkCount=0           
    elif right:
        win.blit(running[walkCount//3],(xc,yc))
        walkCount+=1
    else:
        win.blit(char,(xc, yc))
        walkCount=0
    pygame.display.update()
    KEY = False
run = True
KEY = False
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]: 
        key = True 
        if xc < WIDTH - vel - 64:
            xc += vel
            right = True
        else:
            xc=0
            Area1=False
            Area2=True
    else:
        right = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            walkCount = 0
    else:
        if jumpCount >= -10:
            yc -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    gamewindow(KEY)
pygame.quit()








# while test:
#     win.blit(bg1, (0,0))
#     for case in pygame.event.get():
#         if case==pygame.QUIT:
#             test = False
#     mouse_pos=pygame.mouse.get_pos()
#     xm = mouse_pos [0]
#     ym = mouse_pos [1]
#     print (xm,ym)
#     os.system('cls')
#     pygame.display.update()
#     pygame. time.delay(1)
    
