import pygame as pg
import numpy as np
import pygame.time
import Proga as Pr
import random
import json

pg.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
Mode = 1
SPEEDs = [0.1, 0.2, 0.5, 1, 2]
speed =4

clock = pygame.time.Clock()
Screen = pg.display.set_mode((WIDTH, HEIGHT))
screen = pg.Surface((WIDTH, HEIGHT))
screen.fill((0, 0, 0))

Alldata1 = [[], []]
Alldata2 = [[], []]
n = 0

str_tex = ''
base_color = (100, 100, 100)


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

    b1 = Button(100, 300, 150, 50, change_mode, False, 1, 'K VS K')
    b2 = Button(100, 400, 150, 50, change_mode, False, 2, 'K VS P')
    b3 = Button(100, 500, 150, 50, change_mode, False, 3, 'P VS K')
    b4 = Button(100, 600, 150, 50, change_mode, False, 4, 'P VS P')
    b5 = Button(900, 20, 100, 50, change_speed, False, 1, '<->')
    b6 = Button(900, 220, 300, 50, train, False, 1, 'Train Russia')
    b7 = Button(900, 420, 300, 50, train, False, 2, 'Train Empire')
    buttons.append(b1)
    buttons.append(b2)
    buttons.append(b3)
    buttons.append(b4)
    buttons.append(b5)
    buttons.append(b6)
    buttons.append(b7)

    text1 = font.render(str(SPEEDs[speed]) + 'x', True, base_color)
    text2 = font.render('Memory1: ' + str(len(Pr.model1.memory.memory)), True, base_color)
    text3 = font.render('Memory2: ' + str(len(Pr.model2.memory.memory)), True, base_color)
    text4 = font.render('Mean accuracy: ' + str(Pr.mean_ac), True, base_color)
    text5 = font.render(str_tex , True, base_color)
    screen.blit(text1, [800, 20])
    screen.blit(text2, [0, 20])
    screen.blit(text3, [400, 20])
    screen.blit(text4, [650, 720])
    screen.blit(text5, [250, 720])
    return buttons


class Button():
    def __init__(self, x, y, width, height, onclickFunction=None, onePress=False, index=0, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = True
        self.index = index
        self.font = pg.font.SysFont('Arial', 40)
        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, (255, 0, 0), self.buttonRect, 1)
        self.text = text
        self.buttonSurf = self.font.render(text, True, base_color)
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
            if self.onclickFunction != validate:
                can_press = True
            if pg.mouse.get_pressed(num_buttons=3)[0] and can_press:
                if self.onePress:
                    self.onclickFunction(self.index)
                elif not self.alreadyPressed:
                    self.onclickFunction(self.index)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False


def krestik(n, i):
    a = [[325, 125], [525, 125], [725, 125], [325, 325],
         [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
    b = [[475, 275], [675, 275], [875, 275], [475, 475],
         [675, 475], [875, 475], [475, 675], [675, 675], [875, 675]]
    c = [[325, 275], [525, 275], [725, 275], [325, 475],
         [525, 475], [725, 475], [325, 675], [525, 675], [725, 675]]
    d = [[475, 125], [675, 125], [875, 125], [475, 325],
         [675, 325], [875, 325], [475, 525], [675, 525], [875, 525]]
    if n % 2 == 0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-7, a[i][1]), (b[i][0]-7, b[i][1]), 7)
        pg.draw.line(screen, (0, 0, 255), (a[i][0], a[i][1]), (b[i][0], b[i][1]), 7)
        pg.draw.line(screen, (255, 0, 0), (a[i][0]+7, a[i][1]), (b[i][0]+7, b[i][1]), 7)
    else:
        pg.draw.line(screen, (0, 0, 0), (c[i][0] - 7, c[i][1]), (d[i][0] - 7, d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 0), (c[i][0], c[i][1]), (d[i][0], d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 255), (c[i][0] + 7, c[i][1]), (d[i][0] + 7, d[i][1]), 7)


def train(number):
    global str_tex
    if number == 1:
        loss = Pr.dqn_training(Pr.model1)
    elif number == 2:
        loss = Pr.dqn_training(Pr.model2)
    if loss != None:
        str_tex = str(round(float(loss), 4))
    else:
        str_tex = 'Not enough'
    text = font.render(str_tex, True, base_color)
    pg.draw.rect(screen, (0, 0, 0), (250, 720, 200, 50))
    screen.blit(text, [250, 720])
def change_mode(i):
    global Alldata1, Alldata2
    global Mode, can_play

    if Mode == i:
        return False
    Mode = i
    clear(1)
    Alldata1 = [[], []]
    Alldata2 = [[], []]


def change_speed(i):
    global speed
    speed = (1 + speed) % len(SPEEDs)
    pg.draw.rect(screen, (0, 0, 0), (800, 20, 100, 50))
    text = font.render(str(SPEEDs[speed]) + 'x', True, base_color)
    screen.blit(text, [800, 20])


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
                replay = Button(10, 90, 130, 60, clear, False, 10, 'replay?')
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


def victory():
    all_conc = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
    for i in all_conc:
        if Data[i[0]] + Data[i[1]] + Data[i[2]] == 9:
            if Mode < 4:
                result(True)
            return True

    return False


k = 0
dt = 0
timer = 0

def salut():
    global k, dt
    ar = [[300, 300], [350, 350], [400, 300], [300, 400],
          [500, 290], [500, 500], [450, 300], [300, 300],
          [320, 400], [400, 400], [350, 370], [380, 434],
          [340, 400], [300, 430], [400, 400], [350, 430]]
    img = pg.image.load(str(k//3+1)+'.png')
    Screen.blit(img, ar[dt % 16])
    if k == 42:
        k = 0
        dt += 1
    else:
        k += 1


tim = 0
def result(how):
    Pr.analyse(moves, how)


def restart_game(how):
    clear(int(how))
    if Mode == 1:
        validate(random.randint(0, 8))


def real_move():
    global tim
    tim += 1
    if tim >= FPS / 20 / SPEEDs[speed]:
        tim = 0
        mov = Pr.make_move(Data, last, n)
        if not validate(mov):
            moves.append(mov)
            #
            # move = 0
            # for i in range(9):
            #    if Data[i] == 0:
            #        move = i
            #        break
            if Mode < 4:
                result(False)
            restart_game(False)
            tim = -FPS/20 - 2/SPEEDs[speed]


def load_data(name):
    with open(name) as json_file:
        data = json.load(json_file)
        return data['Data1', 'Data2']




def clear_data(name):
    with open(name, 'w') as outfile:
        json.dump({'Data1':[[], []], 'Data2':[[], []]}, outfile)


salutt = True
doing = True
buttons = []

Data = [0]*9
last = -1
moves = []
can_play = False

font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('Russia winner'), True, (128, 0, 255))
text1 = font.render(str('Russian Empire winner'), True, (128, 0, 255))

clear(0)
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
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
    clock.tick(FPS)
Pr.save_model('model')
Pr.save_data('data')
pg.quit()
