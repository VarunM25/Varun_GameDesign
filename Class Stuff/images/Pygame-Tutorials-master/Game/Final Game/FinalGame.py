#Varun Mukund
#Version 1 of Final Game
import os, pygame, random, datetime

WIDTH = 700
HEIGHT = 700 

os.system('cls')
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
Game()