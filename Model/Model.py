import keras
from keras.models import Sequential
from keras.layers import *
from keras import *
import pandas as pd
from keras.activations import *
from keras.initializers import *


class Model:
    def __init__(self):
        self.Gk_model = Sequential()
        self.def_model = Sequential()
        self.mid_model = Sequential()
        self.ak_model = Sequential()

    def load_data(self):
        dataset_gk = pd.read_csv("Resourses/GK.csv", delimiter=';')
        dataset_def = pd.read_csv('Resourses/DEF.csv', delimiter=';')
        dataset_mid = pd.read_csv('Resourses/MID.csv', delimiter=';')
        dataset_ak = pd.read_csv('Resourses/ATT.csv', delimiter=';')
        self.X_gk = dataset_gk.loc[:, :'Penalty'].to_numpy()
        self.X_gk = self.X_gk * 100
        self.y_gk = dataset_gk.loc[:, 'predict'].to_numpy()
        self.X_def = dataset_def.loc[:, :'Tackle'].to_numpy()
        self.X_def = self.X_def * 100
        self.y_def = dataset_def.loc[:, 'Result'].to_numpy()
        self.X_mid = dataset_mid.loc[:, :'Tackle'].to_numpy()
        self.y_mid = dataset_mid.loc[:, 'Result'].to_numpy()
        self.X_ak = dataset_ak.loc[:, :'Tackle'].to_numpy()
        self.y_ak = dataset_ak.loc[:, 'Result'].to_numpy()

    # def fit(self):
    #     self.Gk_model.add(Dense(3, input_shape=(4,), activation=keras.activations.relu, kernel_initializer=lecun_normal()))
    #     self.Gk_model.add(Dense(3, activation=softmax, kernel_initializer=lecun_normal()))
    #     self.mid_model.add(Dense(4, input_shape=(13,), activation=softmax, kernel_initializer=lecun_normal()))
    #     self.def_model.add(Dense(5, input_shape=(13,), activation=softmax, kernel_initializer=lecun_normal()))
    #     self.ak_model.add(Dense(5, input_shape=(13,), activation=softmax, kernel_initializer=lecun_normal()))
    #     self.Gk_model.compile(loss=losses.SparseCategoricalCrossentropy(), optimizer=optimizers.SGD(),
    #                           metrics=['accuracy'])
    #     self.info_gk = self.Gk_model.fit(self.X_gk, self.y_gk, epochs=10, validation_split=0.1)
    #     self.mid_model.compile(loss=losses.SparseCategoricalCrossentropy(), optimizer=optimizers.SGD(),
    #                            metrics=['accuracy'])
    #     self.info_mid = self.mid_model.fit(self.X_mid, self.y_mid, epochs=10, validation_split=0.1)
    #     self.def_model.compile(loss=losses.SparseCategoricalCrossentropy(), optimizer=optimizers.SGD(),
    #                            metrics=['accuracy'])
    #     self.info_def = self.def_model.fit(self.X_def, self.y_def, epochs=10, validation_split=0.1)
    #     self.ak_model.compile(loss=losses.SparseCategoricalCrossentropy(), optimizer=optimizers.SGD(),
    #                           metrics=['accuracy'])
    #     self.info_ak = self.ak_model.fit(self.X_ak, self.y_ak, epochs=10, validation_split=0.1)
    #     print(self.info_gk.history['accuracy'])
    #     print(self.info_mid.history['accuracy'])
    #     print(self.info_def.history['accuracy'])
    #     print(self.info_ak.history['accuracy'])
    #     self.Gk_model.save("Resourses/GK_model.h5")
    #     self.mid_model.save("Resourses/MID_model.h5")
    #     self.def_model.save("Resourses/Def_model.h5")
    #     self.ak_model.save("Resourses/ATT_model.h5")

    def load_model(self):
        self.Gk_model = keras.models.load_model("Resourses/GK_model.h5")
        print(self.X_gk[25])
        print(self.Gk_model.predict(self.X_gk))
