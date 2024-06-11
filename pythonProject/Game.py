import pygame as pg
#import tensorflow as tf
import numpy as np
pg.init()
WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))

r = pg.Rect((WIDTH - 600)//2, (HEIGHT - 600)//2, 600, 600)
pg.draw.rect(screen, (200, 130, 90), r, 0)
doing = True
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False

pg.quit()