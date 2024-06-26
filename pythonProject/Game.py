import pygame as pg
import numpy as np
import pygame.time
import Proga as Pr
import random

pg.init()
WIDTH = 1200
HEIGHT = 800
Mode = 1

clock = pygame.time.Clock()
Screen = pg.display.set_mode((WIDTH, HEIGHT))
screen = pg.Surface((WIDTH, HEIGHT))
screen.fill((0, 0, 0))

Alldata11 = []
Alldata12 = []
Alldata21 = []
Alldata22 = []
n = 0


def draw():
    buttons = []
    screen.fill((0, 0, 0))
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
    b1 = Button(100, 300, 150, 50, change_mode, False, 11, 'K VS K')
    b2 = Button(100, 400, 150, 50, change_mode, False, 12, 'K VS P')
    b3 = Button(100, 500, 150, 50, change_mode, False, 13, 'P VS K')
    b4 = Button(100, 600, 150, 50, change_mode, False, 14, 'P VS P')
    buttons.append(b1)
    buttons.append(b2)
    buttons.append(b3)
    buttons.append(b4)
    return buttons


class Button():
    def __init__(self, x, y, width, height, onclickFunction=None, onePress=False, index=0, text=''):
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
        mouse_pos = pg.mouse.get_pos()
        if self.buttonRect.collidepoint(mouse_pos):
            can_press = can_play
            if self.index >= 10:
                can_press = True
            if pg.mouse.get_pressed(num_buttons=3)[0] and can_press:
                if self.onePress:
                    self.onclickFunction(self.index)
                elif not self.alreadyPressed:
                    self.onclickFunction(self.index)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False


a = [[325, 125], [525, 125], [725, 125], [325, 325], [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
b = [[475, 275], [675, 275], [875, 275], [475, 475], [675, 475], [875, 475], [475, 675], [675, 675], [875, 675]]
c = [[325, 275], [525, 275], [725, 275], [325, 475], [525, 475], [725, 475], [325, 675], [525, 675], [725, 675]]
d = [[475, 125], [675, 125], [875, 125], [475, 325], [675, 325], [875, 325], [475, 525], [675, 525], [875, 525]]


def change_mode(i):
    i -= 10
    global Mode, can_play
    if Mode == i:
        return False
    Mode = i
    clear(1)


def krestik(n, i):
    if n % 2 == 0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-7, a[i][1]), (b[i][0]-7, b[i][1]), 7)
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
moves = []
can_play = False


def validate(ind):
    global n, last, can_play

    if Data[ind] == 3 or (Data[ind] != 0 and (Data[ind]-n) % 2 != 0) or ind == last:
        return False
    else:
        krestik(n, ind)
        n += 1
        last = ind
        Data[ind] += (2 - n % 2)
        moves.append(ind)
        if victory():
            can_play = False
            if Mode != 1:
                replay = Button(10, 50, 130, 60, clear, False, 10, 'replay?')
                buttons.append(replay)
            if sum(Data) == 0:
                return True
            if n % 2 == 0:
                screen.blit(text1, (350, 250))
            if n % 2 == 1:
                screen.blit(text, (450, 250))
        return True


def clear(i):
    global Data, buttons, last, can_play, moves, n
    buttons = draw()
    Data = [0]*9
    last = -1
    if Mode != 1:
        can_play = True
    moves = []
    if i == 1 and Mode == 1:
        if n % 2 == 0:
            screen.blit(text1, (350, 250))
        if n % 2 == 1:
            screen.blit(text, (450, 250))
    n = 0
    for i in range(9):
        but = Button(300 + i % 3 * 200, 100 + i // 3 * 200, 200, 200, validate, False, i)
        buttons.append(but)


clear(0)


def victory():
    all_conc = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
    for i in all_conc:
        if Data[i[0]] + Data[i[1]] + Data[i[2]] == 9:
            if Mode == 1:
                restart_game(True)
            return True

    return False


salutt = True
k = 0
dt = 0
timer = 0
ar = [[300, 300], [350, 350], [400, 300], [300, 400], [500, 290], [500, 500], [450, 300], [300, 300],
      [320, 400], [400, 400], [350, 370], [380, 434], [340, 400], [300, 430], [400, 400], [350, 430]]
def salut():
    global k, dt
    img = pg.image.load(str(k//3+1)+'.png')
    Screen.blit(img, ar[dt % 16])
    if k == 42:
        k = 0
        dt += 1
    else:
        k += 1


tim = 0


def restart_game(how):
    global Alldata11, Alldata12, Alldata21, Alldata22
    datax1, datay1, datax2, datay2 = Pr.make_data(moves, how)
    clear(int(how))
    if len(Alldata11) >= 2:
        Pr.train_model(Alldata11, Alldata12, Alldata21, Alldata22)
        Alldata11 = []
        Alldata12 = []
        Alldata21 = []
        Alldata22 = []
    else:
        for j in range(10):
            for i in range(len(datax1)):
                Alldata11.append(datax1[i])
                Alldata12.append(datay1[i])
            for i in range(len(datax2)):
                Alldata21.append(datax2[i])
                Alldata22.append(datay2[i])
    # validate(random.randint(0, 8))


def real_move():
    global tim
    tim += 1
    if tim == 2:
        tim = 0
        mov = Pr.make_move(Data, last, n)
        print(mov)
        if not validate(mov):
            moves.append(mov)
            #
            # move = 0
            # for i in range(9):
            #    if Data[i] == 0:
            #        move = i
            #        break
            restart_game(False)
            tim = -8


font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('Russia winner'), True, (128, 0, 255))
text1 = font.render(str('Russian Empire winner'), True, (128, 0, 255))

while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Pr.save_model('now_model')
            doing = False
    for bu in buttons:
        bu.process()

    Screen.blit(screen, (0, 0))
    if Mode == 1:
        real_move()
    elif Mode == 2:
        if n % 2 == 0 and can_play:
            real_move()
    elif Mode == 3:
        if n % 2 == 1 and can_play:
            real_move()
    else:
        if not can_play:
            salut()
    clock.tick(30)
pg.quit()
