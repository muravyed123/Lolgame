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
a=[[325, 325]]
b=[[475, 475]]
def krestik(n, i):
    if n%2==0:
        pg.draw.line(screen, (255, 255, 255), (a[i][0]-5, a[i][1]), (b[i][0]-5, b[i][1]),5)
        pg.draw.line(screen, (0, 0, 255), (a[i][0], a[i][1]), (b[i][0], b[i][1]), 5)
        pg.draw.line(screen, (255, 0, 0), (a[i][0]+5, a[i][1]), (b[i][0]+5, b[i][1]), 5)
krestik(0, 0)
doing = True
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False

pg.quit()