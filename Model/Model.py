import keras
from keras.models import Sequential
from keras.layers import *
from keras import *
import pandas as pd
from keras.activations import *
from keras.initializers import *
from Model.DataConverter import DataConverter
from Model.Player import Player
from Model.DbWorker import DbWorker


class Model:
    def __init__(self):
        self.converter = DataConverter()
        self.player = Player
        self.ann_model = Sequential()
        self.db_worker = DbWorker()
        self.player_type = {
            "attacker": "Resourses/ATT_model.h5",
            "midfielder": "Resourses/MID_model.h5",
            "defender": "Resourses/DEF_model.h5",
            "goalkeeper": "Resourses/GK_model.h5",
            '': None
        }

    def __load_data__(self):
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

    def load_models(self, player_type):
        self.ann_model = keras.models.load_model(self.player_type[player_type])

    def predict_train_schedudle(self, player_stats):
        predict = self.ann_model.predict(player_stats)[0]
        for i in range(int(np.size(predict))):
            if predict[i] == max(predict):
                program = i + 1
        return program

    def save_player_in_db(self):
        self.db_worker.save_player(self.player)

    def set_data_player(self, player_type, name, params, train_program):
        self.player = Player(
            type = player_type,
            full_name = name,
            indicators = params,
            last_train = train_program
        )

    def convert_training_data(self, data):
        return self.converter.convert(data)

    def get_player_from_db(self, name, ptype):
        self.db_worker.get_player_history(name, ptype)
