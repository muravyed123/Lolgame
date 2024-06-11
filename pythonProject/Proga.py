import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
def make_data():
    pass
def save_model(model, name):
    # Saving the model to disk
    model.save(name)
def load_model(name):
    #Loading the model from disk
    new_model = tf.keras.models.load_model(name)
X_and = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float16)
Y_and = tf.constant([[0], [0], [0], [1]], dtype=tf.float16)  # Логика операции AND

# Создание новой последовательной модели
model = keras.Sequential()

model.add(layers.Dense(
    4,  # Количество нейронов
    input_dim=11,  # Задаем размер входа, подается два бита
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

def make_move(Data, last, number):
    data = np.array(Data)
    data.append(last)
    data.append(number)
    inputTens = tf.constant(data / 8, dtype=tf.float16)
    return round(model.predict(inputTens)[0][0])*8
