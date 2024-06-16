import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
import numpy as np
import pygame.time
import pygame as pg
import random
pg.init()
model = tf.keras.Sequential()
model.add(Dense(8, activation='linear', input_dim=2))
model.add(Dense(1, activation='linear'))
#model.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', # указывается параметр, по которому осуществляется ранняя остановка. Обычно это функция потреть на валидационном наборе (val_loss)
    patience=2, # количество эпох по истечении которых закончится обучение, если показатели не улучшатся
    mode='min', # указывает, в какую сторону должна быть улучшена ошибка
    restore_best_weights=True # если параметр установлен в true, то по окончании обучения модель будет инициализирована весами с самым низким показателем параметра "monitor"
)
model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss='binary_crossentropy', metrics=['accuracy'])
Datax = []
Datay = []
def function(a, b):
    return(a * 2 + b ** 0.5)

def give_data(count):
    global Datax, Datay
    Datax = []
    Datay = []
    for i in range(count):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        Datax.append([a/1000, b/1000])
        Datay.append(function(a, b)/1000)
def train_model():
    #give_data(100000)
    for i in range(0, 100):
        for j in range(0, 100):
            Datax.append([i/1000, j/1000])
            Datay.append(function(i, j)/1000)
    X_and = tf.constant(Datax, dtype=tf.float32)
    Y_and = tf.constant(Datay, dtype=tf.float32)
    model.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=10,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1,  # Уровень детализации при выводе в терминале во время обучения

    )
doing = True
clock = pygame.time.Clock()
timer = 0
train_model()
while doing:
    if timer == 5:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        inputTens = tf.constant([[a/1000, b/1000]], dtype=tf.float16)
        f = model.predict(inputTens)[0][0] * 1000
        print(a, b,  'results:', f, function(a, b), ':', abs(f - function(a, b)))

        timer = 0
    else:
        timer += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False
    clock.tick(10)
