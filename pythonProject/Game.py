import pygame as pg
#import tensorflow as tf
import numpy as np
pg.init()
WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
r = pg.Rect((WIDTH - 600)//2, (HEIGHT - 600)//2, 600, 600)
pg.draw.rect(screen, (200, 130, 90), r, 0)
r1 = pg.Rect((WIDTH - 600)//2+195, (HEIGHT - 600)//2, 10, 600)
pg.draw.rect(screen, (255, 255, 255), r1, 0)
r2 = pg.Rect((WIDTH - 600)//2+395, (HEIGHT - 600)//2, 10, 600)
pg.draw.rect(screen, (255, 255, 255), r2, 0)
r3 = pg.Rect((WIDTH - 600)//2, (HEIGHT - 600)//2+195, 600, 10)
pg.draw.rect(screen, (255, 255, 255), r3, 0)
r4 = pg.Rect((WIDTH - 600)//2, (HEIGHT - 600)//2+395, 600, 10)
pg.draw.rect(screen, (255, 255, 255), r4, 0)
<<<<<<< HEAD

class Button():
    def __init__(self, x, y, width, height, onclickFunction=None, onePress=False, index = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.index = index
        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, (255,0,0), self.buttonRect, 5)
    def process(self):
        mousePos = pg.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                if self.onePress:
                    self.onclickFunction(self.index)
                elif not self.alreadyPressed:
                    self.onclickFunction(self.index)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

n = 0
a = [[325, 125], [525, 125], [725, 125], [325, 325], [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
b = [[475, 275],[675, 275], [875, 275], [475, 475],[675, 475], [875, 475], [475, 675],[675, 675], [875, 675]]
=======
n=0
a=[[325, 125], [525, 125], [725, 125], [325, 325], [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
b=[[475, 275],[675, 275], [875, 275], [475, 475],[675, 475], [875, 475], [475, 675],[675, 675], [875, 675]]
c=[[325, 275], [525, 275], [725, 275], [325, 475], [525, 475], [725, 475], [325, 675], [525, 675], [725, 675]]
d=[[475, 125],[675, 125], [875, 125], [475, 325],[675, 325], [875, 325], [475, 525],[675, 525], [875, 525]]
>>>>>>> b829aa1c65340040d77123c40c0842da4a7246a7
def krestik(n, i):
    if n % 2 == 0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-7, a[i][1]), (b[i][0]-7, b[i][1]),7)
        pg.draw.line(screen, (0, 0, 255), (a[i][0], a[i][1]), (b[i][0], b[i][1]), 7)
        pg.draw.line(screen, (255, 0, 0), (a[i][0]+7, a[i][1]), (b[i][0]+7, b[i][1]), 7)
<<<<<<< HEAD
Data = [0]*9
n = 0
=======
    if n%2==1:
        pg.draw.line(screen, (0, 0, 0), (c[i][0] - 7, c[i][1]), (d[i][0] - 7, d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 0), (c[i][0], c[i][1]), (d[i][0], d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 255), (c[i][0] + 7, c[i][1]), (d[i][0] + 7, d[i][1]), 7)
for i in range (9):
    krestik(0, i)
    krestik(1, i)


>>>>>>> b829aa1c65340040d77123c40c0842da4a7246a7
doing = True
buttons = []
def validate(ind):
    global n
    if Data[ind] == 3 or (Data[ind] != 0 and (Data[ind]-n) % 2 == 0):
        return False
    else:
        krestik(n, ind)
        n += 1
        return True
for i in range(9):
    but = Button(300 + i%3*200, 100 + i//3 * 200, 200, 200, validate, False, i)
    buttons.append(but)
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False
    for bu in buttons:
        bu.process()

pg.quit()
