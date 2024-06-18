import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
import numpy as np
import random


def make_data(moves, how_played):
    pos = [0]*9
    Datatens1 = []
    Data_y1=[]
    Datatens2 = []
    Data_y2 = []
    win = (len(moves)+int(not how_played)) % 2
    s = len(moves)
    if not how_played:
        s -= 1
    for i in range(len(moves)):
        new_data = [0]*10
        how_to_move = [0] * 9

        for j in range(len(pos)):
            new_data[j] = pos[j]/4
            if (2 - i % 2 == pos[j] or pos[j] == 0) and (i != 0 and j != moves[i-1]):
                how_to_move[j] = 0.2
        if i != 0:
            new_data[-1] = moves[i - 1]/8
        else:
            new_data[-1] = 1
        if i % 2 == 0:
            Datatens1.append(new_data)
        else:
            Datatens2.append(new_data)

        if not how_played:
            if i == len(moves)-1:
                how_to_move[moves[i]] = 0
            else:
                how_to_move[moves[i]] = 1
        else:
            s = len(moves)/20
            if len(moves) - i <= 2:
                s = (win - i) % 2
            how_to_move[moves[i]] = ((win - i) % 2 + s)/2
        if i % 2 == 0:
            Data_y1.append(how_to_move)
        else:
            Data_y2.append(how_to_move)
        print(pos, how_to_move)
        pos[moves[i]] += (1 + i % 2)
    return((Datatens1, Data_y1, Datatens2, Data_y2))


def save_model(name):
    # Saving the model to disk
    model1.save(name+'1.h5')
    model2.save(name + '2.h5')


def load_model(name):
    # Loading the model from disk
    model_load1 = tf.keras.models.load_model(name + '1.h5')
    model_load2 = tf.keras.models.load_model(name + '2.h5')
    return model_load1, model_load2


def new_model():
    # Создание новой последовательной модели
    opt = 'Adam'
    if True:
        model_1, model_2 = load_model('now_model')
        model_1.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
        model_2.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    else:
        inputs = keras.Input(shape=(10,), name="digits")
        x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
        x = layers.Dense(16, activation="linear", name="dense_2")(x)
        outputs = layers.Dense(9, activation="sigmoid", name="predictions")(x)
        model_1 = keras.Model(inputs=inputs, outputs=outputs)
        model_1.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
        inputs = keras.Input(shape=(10,), name="digits")
        x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
        x = layers.Dense(32, activation="linear", name="dense_2")(x)
        outputs = layers.Dense(9, activation="sigmoid", name="predictions")(x)
        model_2 = keras.Model(inputs=inputs, outputs=outputs)
        model_2.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])

    return model_1, model_2


def train_model(Datax1, Datay1, Datax2, Datay2):
    ep = 20
    X_and = tf.constant(Datax1, dtype=tf.float16)
    Y_and = tf.constant(Datay1, dtype=tf.float16)
    model1.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=ep,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )
    X_and = tf.constant(Datax2, dtype=tf.float16)
    Y_and = tf.constant(Datay2, dtype=tf.float16)
    model2.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=ep,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )


def make_move(Data, last, number):
    data = np.array([0.0]*10)
    for i in range(len(Data)):
        data[i] = Data[i]/3
    if last == -1:
        last = 8
    data[-1] = last/8
    inputTens = tf.constant([data], dtype=tf.float32)
    if number % 2 == 0:
        g = model1.predict(inputTens)[0]
    else:
        g = model2.predict(inputTens)[0]
    print(g)

    max, index_max = -1, 0
    for i in range(len(g)):
        if g[i] >= max:
            max = g[i]
            index_max = i
    return index_max


model1, model2 = new_model()
