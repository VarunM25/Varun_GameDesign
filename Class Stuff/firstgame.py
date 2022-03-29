import os,time
import pygame as p

#initialize pygame
p.init()
#define colors
white = [255,255,255]
red = [255,0,0]
mag = [255,0,255]
aqua = [51,153,255]
mystery = [47,192,229]
#create your window/screen
WIDTH = 600
HEIGHT = 700
screen = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('My Window')
# screen.fill(mystery)
# p.display.update()
# time.sleep(1)
# p.display.update()
# screen.fill(red)
# p.display.update()
# time.sleep(1)
# screen.fill(white)
# p.display.update()
# time.sleep(1)
# screen.fill(aqua)
# p.display.update()
# time.sleep(1)
# screen.fill
# screen.fill(mag)
# time.sleep(1)
# p.display.update()
# p.time.delay(5000)

#define a rectangle
#position
x=20
y=30
#width and height of rectangle
wbox = 50
hbox = 50
square = p.Rect(x,y,wbox,hbox)
square2 = p.Rect(x+200, y+200, wbox, hbox)
run = True
while run:
    screen.fill(mag)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    square.x +=5
    square.y+=5
    p.draw.rect(screen,(white), square)
    p.draw.rect(screen,(red), square2)
    p.display.update()
    p.time.delay (100)