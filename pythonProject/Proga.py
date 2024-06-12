import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
def make_data(moves):
    pos = [0]*9
    Datatens = []
    Data_y=[]
    win = len(moves)%2
    for i in range(moves):
        pos[moves[i]] += (2 - i%2)
        new_data = [0]*11
        for j in range(pos):
            new_data[j] = pos[j]/4
        new_data[-2] = moves[i]/8
        new_data[-1] = i%2
        Datatens.append(new_data)
        Data_y.append(int((win -i)%2))
    return((Datatens, Data_y))
def save_model(model, name):
    # Saving the model to disk
    model.save(name)
def load_model(name):
    #Loading the model from disk
    new_model = tf.keras.models.load_model(name)
def new_model():

    # Создание новой последовательной модели
    model = keras.Sequential()

    model.add(layers.Dense(
        11,  # Количество нейронов
        input_dim=128,  # Задаем размер входа, подается два бита
        activation='relu'  # Используем функцию активации ReLU, так как все входы положительные
    ))

    model.add(layers.Dense(
        1,  # Количество нейронов. Мы хотим один выход
        activation='sigmoid'  # Используем сигмоид, потому что мы хотим бинарную классификацию
    ))

    # Компиляция слоев в модель

    model.compile(
        loss='mean_squared_error',  # Функция потерь, которую мы минимизируем
        optimizer='adam',  # Наша функция оптимизации
        metrics=['binary_accuracy']  # Метрики - различные значения, которые вы хотите отслеживать во время обучения
    )
    return model
def train_model(model, Datax, Datay):
    X_and = tf.constant(Datax, dtype=tf.float16)
    Y_and = tf.constant(Datay, dtype=tf.float16)
    model.fit(
        X_and,  # Входные данные для обучения
        Y_and,  # Выходные данные для обучения
        epochs=2000,  # Количество итераций, на которое мы хотим обучить модель
        verbose=1  # Уровень детализации при выводе в терминале во время обучения
    )


def make_move(Data, last, number, model):
    data = np.array(Data)/4
    data.append(last/8)
    data.append(number%2)
    inputTens = tf.constant(data, dtype=tf.float16)
    return round(model.predict(inputTens)[0][0])*8
def start():
    model = new_model()
