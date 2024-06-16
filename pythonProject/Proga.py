import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
import numpy as np
import random
def make_data(moves, how_played, move):
    pos = [0]*9
    Datatens1 = []
    Data_y1=[]
    Datatens2 = []
    Data_y2 = []
    win = (len(moves)+int(not how_played))%2
    s = len(moves)
    if not how_played:
        s-=1
    for i in range(len(moves)):
        if i != s:
            pos[moves[i]] += (2 - i % 2)
        new_data = [0]*10
        for j in range(len(pos)):
            new_data[j] = pos[j]/4
        new_data[-1] = moves[i]/8
        if i % 2 == 0:
            Datatens1.append(new_data)
        else:
            Datatens2.append(new_data)
        how_to_move =[0]*9
        if how_played:
            if (win-i) % 2 == 0:
                how_to_move[moves[i]] = 1
            else:
                how_to_move[moves[i]] = 1
        else:
            if i == len(moves)-1:
                how_to_move[move] = 1
            else:
                how_to_move[moves[i]] = 1
        if i % 2 == 0:
            Data_y1.append(how_to_move)
        else:
            Data_y2.append(how_to_move)
    #print(moves, how_played)
    return((Datatens1, Data_y1, Datatens2, Data_y2))
def save_model(name):
    # Saving the model to disk
    model1.save(name+'1.h5')
    model2.save(name + '2.h5')
def load_model(name):
    #Loading the model from disk
    model1 = tf.keras.models.load_model(name + '1.h5')
    model2 = tf.keras.models.load_model(name + '2.h5')
    return (model1, model2)
def new_model():

    # Создание новой последовательной модели
    if True:
        model1, model2 = load_model('now_model')
        model1.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])
        model2.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])
    else:
        inputs = keras.Input(shape=(10,), name="digits")
        x = layers.Dense(64, activation="linear", name="dense_1")(inputs)
        x = layers.Dense(16, activation="linear", name="dense_2")(x)
        outputs = layers.Dense(9, activation="sigmoid", name="predictions")(x)
        model1 = keras.Model(inputs=inputs, outputs=outputs)
        model1.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])
        inputs = keras.Input(shape=(10,), name="digits")
        x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
        x = layers.Dense(32, activation="linear", name="dense_2")(x)
        outputs = layers.Dense(9, activation="sigmoid", name="predictions")(x)
        model2 = keras.Model(inputs=inputs, outputs=outputs)
        model2.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

    return (model1, model2)
def train_model(Datax1, Datay1, Datax2, Datay2):
    X_and = tf.constant(Datax1, dtype=tf.float16)
    Y_and = tf.constant(Datay1, dtype=tf.float16)
    model1.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=30,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )
    X_and = tf.constant(Datax2, dtype=tf.float16)
    Y_and = tf.constant(Datay2, dtype=tf.float16)
    model2.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=30,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )


def make_move(Data, last, number):
    data = np.array([0.0]*10)
    for i in range(len(Data)):
        data[i] = Data[i]/3
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
