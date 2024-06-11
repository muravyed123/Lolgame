import pygame as pg
import tensorflow as tf
import numpy as np
pg.init()
WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()