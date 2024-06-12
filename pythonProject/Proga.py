import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
import numpy as np
import random
def make_data(moves, how_played, move):
    pos = [0]*9
    Datatens = []
    Data_y=[]
    win = (len(moves)+int(not how_played))%2
    for i in range(len(moves)):
        pos[moves[i]] += (2 - i % 2)
        new_data = [0]*11
        for j in range(len(pos)):
            new_data[j] = pos[j]/4
        new_data[-2] = moves[i]/8
        new_data[-1] = i % 2
        Datatens.append(new_data)
        if how_played:
            Data_y.append(int((win - i) % 2))
        else:
            if i == len(moves)-1:

                Data_y.append(move/8)
            else:
                Data_y.append(moves[i]/8)
    print(Data_y)
    return((Datatens, Data_y))
def save_model(name):
    # Saving the model to disk
    model.save(name+'.h5')
def load_model(name):
    #Loading the model from disk
    model = tf.keras.models.load_model(name+'.h5')
    return model
def new_model():

    # Создание новой последовательной модели
    if False:
        model = load_model('now_model')
        model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    else:
        model = tf.keras.Sequential()
        model.add(Dense(128, activation='relu', input_dim=11))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return model
def train_model(Datax, Datay):
    X_and = tf.constant(Datax, dtype=tf.float16)
    Y_and = tf.constant(Datay, dtype=tf.float16)
    model.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=10,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )


def make_move(Data, last, number):
    data = np.array([0]*11)
    for i in range(len(Data)):
        data[i] = Data[i]/3
    data[-2] = last/8
    data[-1] = number % 2
    inputTens = tf.constant([data], dtype=tf.float32)
    return round(model.predict(inputTens)[0][0]*8)
model = new_model()
