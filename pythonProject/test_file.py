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
model.add(Dense(1, activation='linear', input_dim=1))
model.add(Dense(1, activation='linear'))
#model.compile(optimizer='AdaGrad', loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', # указывается параметр, по которому осуществляется ранняя остановка. Обычно это функция потреть на валидационном наборе (val_loss)
    patience=2, # количество эпох по истечении которых закончится обучение, если показатели не улучшатся
    mode='min', # указывает, в какую сторону должна быть улучшена ошибка
    restore_best_weights=True # если параметр установлен в true, то по окончании обучения модель будет инициализирована весами с самым низким показателем параметра "monitor"
)
model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss='binary_crossentropy', metrics=['accuracy'])
Datax = []
Datay = []
def function(a):
    return(a*10 + 5)

def give_data(count):
    global Datax, Datay
    Datax = []
    Datay = []
    for i in range(count):
        a = random.randint(0,100)
        Datax.append(a/2000)
        Datay.append(function(a)/2000)
def train_model():
    give_data(10000)
    X_and = tf.constant(Datax, dtype=tf.float16)
    Y_and = tf.constant(Datay, dtype=tf.float16)
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
        inputTens = tf.constant([a/2000], dtype=tf.float16)
        f = model.predict(inputTens)[0][0] * 2000
        print(a, 'results:', f, function(a), ':', abs(f - function(a)))

        timer = 0
    else:
        timer += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            doing = False
    clock.tick(10)
