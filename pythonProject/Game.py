import pygame as pg
#import tensorflow as tf
import numpy as np
pg.init()
WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))

r = pg.Rect(50, 50, 100, 200)
pg.draw.rect(screen, (255, 0, 0), r, 0)
doing = True
while doing:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False

pg.quit()