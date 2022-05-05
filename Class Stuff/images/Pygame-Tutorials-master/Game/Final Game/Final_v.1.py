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
bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd1.jpg'), (700,600))
bg2 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd2.png'), (700,600))
bg3 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd3.png'), (700,600))
bg4 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd4.png'), (700,600))
bg5 = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd5.jpg'), (700,600))

# Character movements
char = pygame.transform.scale(pygame.image.load('Class Stuff\images\Idle-stance_04.png'), (64,64))
attacking = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Attacking\\attack_07.png'), (64,64))]
running = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_03.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_04.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_05.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_06.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_07.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_08.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\\new-run_09.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Running\Run2_03.png'), (64,64))]
jumping = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Jumping\Jumping_03.png'), (64,64))]
crouching = [pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_01.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_02.png'), (64,64)), pygame.transform.scale(pygame.image.load('Class Stuff\images\Crouching\crouching_03.png'), (64,64))]
thwomp = [pygame.image.load('Class Stuff\images\Bad dudes\\thwomp.png')]
fireball = [pygame.image.load('Class Stuff\images\Fireball\\fireball_02.png')]

#robots/bad guys
badrobot1 = [pygame.image.load('Class Stuff\images\Bad dudes\smallbaddude1.png')]
badrobot2 = [pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude3.png')]
badrobot3 = [pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude1.png')]
badrobot4 = [pygame.image.load('Class Stuff\images\Bad dudes\\bigbaddude2.png')]
bossrobot = [pygame.image.load('Class Stuff\images\Bad dudes\Reallybaddude.png')]
golem = [pygame.image.load('Class Stuff\images\Bad dudes\Golem1.png')]
thwomp = [pygame.image.load('Class Stuff\images\Bad dudes\\thwomp.png')]

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
char_hitbox = pygame.Rect(xc,yc,char_wb,char_hb)
vel=5


def gamewindow(KEY):
    global walkCount, Area1, Area2, Area3, Area4, Area5, bg, right, xc, keyddddddd
   
    if Area2:
       
        bg = bg2
        if KEY :  
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                print (yc)
                xc=0
                Area2=False
                Area3=True
    if Area3:
        bg =bg3
        if KEY and Area3:  
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                xc=0
                Area3=False
                Area4=True
    if Area4:
       
        bg = bg4
        if KEY and Area4:  
            if xc < WIDTH - vel - 64:
                xc += vel
                right = True
            else:
                xc=0
                Area4=False
                Area5=True
    if Area5:
       
        bg =bg5
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
    key = False
run = True
key = False
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
        elif Area1:
            xc=0
            Area1=False
            Area2=True
        elif Area2:
            xc=0
            Area2=False
            Area3=True    
        elif Area3:
            xc=0
            Area3=False
            Area4=True 
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
    gamewindow(key)
# def gamewindow(KEY):
#     global walkCount, Area1, Area2, Area3, Area4, Area5, bg, right, xc, key
#     if Area2:
        
#         bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\Backgrounds\\finalgamebkgd2.png'), (700,600))
#         if KEY :  
#             if xc < WIDTH - vel - 64:
#                 xc += vel
#                 right = True
#             else:
#                 print (yc)
#                 xc=0
#                 Area2=False
#                 Area3=True
#     if Area3:
#         bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd3.png'), (700,600))
#         if KEY and Area3:  
#             if xc < WIDTH - vel - 64:
#                 xc += vel
#                 right = True
#             else:
#                 xc=0
#                 Area3=False
#                 Area4=True
#     if Area4:
#         bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd4.png'), (700,600))
#         if KEY and Area4:  
#             if xc < WIDTH - vel - 64:
#                 xc += vel
#                 right = True
#             else:
#                 xc=0
#                 Area4=False
#                 Area5=True
#     if Area5:
#         bg = pygame.transform.scale(pygame.image.load('Class Stuff\images\\finalgamebkgd5.jpg'), (700,600))
#     win.blit(bg,(0,0))
#     if walkCount+1>=27:
#         walkCount=0           
#     elif right:
#         win.blit(running[walkCount//3],(xc,yc))
#         walkCount+=1
#     else:
#         win.blit(char,(xc, yc))
#         walkCount=0
#     pygame.display.update()
#     key = False
# run = True
# key = False
# while run: 
#     clock.tick(27)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_d]: 
#         key = True 
#         if xc < WIDTH - vel - 64:
#             xc += vel
#             right = True
#         else:
#             xc=0
#             Area1=False
#             Area2=True
#     else:
#         right = False
#         walkCount = 0
#     if not(isJump):
#         if keys[pygame.K_SPACE]:
#             isJump = True
#             walkCount = 0
#     else:
#         if jumpCount >= -10:
#             yc -= (jumpCount * abs(jumpCount)) * 0.5
#             jumpCount -= 1
#         else:
#             jumpCount = 10
#             isJump = False
#     gamewindow(key)

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
    
