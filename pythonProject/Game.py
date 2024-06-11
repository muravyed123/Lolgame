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
n=0
a=[[325, 125], [525, 125], [725, 125], [325, 325], [525, 325], [725, 325], [325, 525], [525, 525], [725, 525]]
b=[[475, 275],[675, 275], [875, 275], [475, 475],[675, 475], [875, 475], [475, 675],[675, 675], [875, 675]]
c=[[325, 275], [525, 275], [725, 275], [325, 475], [525, 475], [725, 475], [325, 675], [525, 675], [725, 675]]
d=[[475, 125],[675, 125], [875, 125], [475, 325],[675, 325], [875, 325], [475, 525],[675, 525], [875, 525]]
def krestik(n, i):
    if n%2==0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-7, a[i][1]), (b[i][0]-7, b[i][1]),7)
        pg.draw.line(screen, (0, 0, 255), (a[i][0], a[i][1]), (b[i][0], b[i][1]), 7)
        pg.draw.line(screen, (255, 0, 0), (a[i][0]+7, a[i][1]), (b[i][0]+7, b[i][1]), 7)
    if n%2==1:
        pg.draw.line(screen, (0, 0, 0), (c[i][0] - 7, c[i][1]), (d[i][0] - 7, d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 0), (c[i][0], c[i][1]), (d[i][0], d[i][1]), 7)
        pg.draw.line(screen, (255, 255, 255), (c[i][0] + 7, c[i][1]), (d[i][0] + 7, d[i][1]), 7)
for i in range (9):
    krestik(0, i)
    krestik(1, i)


doing = True
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False

pg.quit()

