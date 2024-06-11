import pygame as pg
#import tensorflow as tf
import numpy as np
import pygame.time

pg.init()
WIDTH = 1200
HEIGHT = 800
clock = pygame.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
def draw():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    r = pg.Rect((WIDTH - 600) // 2, (HEIGHT - 600) // 2, 600, 600)
    pg.draw.rect(screen, (200, 100, 90), r, 0)
    r1 = pg.Rect((WIDTH - 600) // 2 + 195, (HEIGHT - 600) // 2, 10, 600)
    pg.draw.rect(screen, (255, 255, 255), r1, 0)
    r2 = pg.Rect((WIDTH - 600) // 2 + 395, (HEIGHT - 600) // 2, 10, 600)
    pg.draw.rect(screen, (255, 255, 255), r2, 0)
    r3 = pg.Rect((WIDTH - 600) // 2, (HEIGHT - 600) // 2 + 195, 600, 10)
    pg.draw.rect(screen, (255, 255, 255), r3, 0)
    r4 = pg.Rect((WIDTH - 600) // 2, (HEIGHT - 600) // 2 + 395, 600, 10)
    pg.draw.rect(screen, (255, 255, 255), r4, 0)
class Button():
    def __init__(self, x, y, width, height, onclickFunction=None, onePress=False, index = 0, text = ''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.index = index
        self.font = pg.font.SysFont('Arial', 40)
        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, (255, 0, 0), self.buttonRect, 1)
        self.text = text
        self.buttonSurf = self.font.render(text, True, (70, 70, 70))
        if self.text != '':
            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
            ])
            screen.blit(self.buttonSurface, self.buttonRect)
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
a=[[325, 125], [525, 125], [725, 125], [325, 325], [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
b=[[475, 275],[675, 275], [875, 275], [475, 475],[675, 475], [875, 475], [475, 675],[675, 675], [875, 675]]
c=[[325, 275], [525, 275], [725, 275], [325, 475], [525, 475], [725, 475], [325, 675], [525, 675], [725, 675]]
d=[[475, 125],[675, 125], [875, 125], [475, 325],[675, 325], [875, 325], [475, 525],[675, 525], [875, 525]]
def krestik(n, i):
    if n % 2 == 0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-7, a[i][1]), (b[i][0]-7, b[i][1]),7)
        pg.draw.line(screen, (0, 0, 255), (a[i][0], a[i][1]), (b[i][0], b[i][1]), 7)
        pg.draw.line(screen, (255, 0, 0), (a[i][0]+7, a[i][1]), (b[i][0]+7, b[i][1]), 7)
    else:
        pg.draw.line(screen, (0, 0, 0), (c[i][0] - 7, c[i][1]), (d[i][0] - 7, d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 0), (c[i][0], c[i][1]), (d[i][0], d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 255), (c[i][0] + 7, c[i][1]), (d[i][0] + 7, d[i][1]), 7)
doing = True
buttons = []
Data = [0]*9
last = -1
can_play = True
def validate(ind):
    global n, last, can_play
    if not can_play:
        return False
    if Data[ind] == 3 or (Data[ind] != 0 and (Data[ind]-n) % 2 != 0) or ind == last:
        return False
    else:
        krestik(n, ind)
        n += 1
        last = ind
        Data[ind] += (2 - n % 2)
        if victory():
            can_play = False
            replay = Button(10, 50, 130,60, clear, False, 0, 'replay?')
            buttons.append(replay)
        return True
def clear(i):
    global Data, buttons, last, can_play
    draw()
    Data = [0]*9
    buttons = []
    last = -1
    can_play = True
    for i in range(9):
        but = Button(300 + i % 3 * 200, 100 + i // 3 * 200, 200, 200, validate, False, i)
        buttons.append(but)
all_conc = np.array([[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]])
clear(0)
def victory():
    for i in all_conc:
        if Data[i[0]] + Data[i[1]] + Data[i[2]] == 9:
            return True
    return False
saluty = [pg.image.load("1.png"), pg.image.load("2.png"), pg.image.load("3.png"), pg.image.load("4.png"), pg.image.load("5.png"), pg.image.load("6.png"), pg.image.load("7.png"), pg.image.load("8.png"), pg.image.load("9.png"), pg.image.load("10.png"), pg.image.load("11.png"), pg.image.load("12.png"), pg.image.load("13.png"), pg.image.load("14.png"), pg.image.load("15.png")]
salutt = True
k = 0
a = [[300,300],[350,350],[400,300],[300,400],[500,290],[500,500],[450,300],[300,300],[320,400],[400,400],[350,370],[380,434],[340,400],[300,430],[400,400],[350,430]]
def salut():
    global k
    while salutt:
       screen.blit(saluty[k], a[k])
       if k==14:
           k=0
       else:
           k+=1
           pg.display.update()
       clock.tick(20)
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False
    for bu in buttons:
        bu.process()
    salut()
pg.quit()
