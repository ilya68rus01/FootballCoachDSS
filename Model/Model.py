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

    def predict_train_schedudle(self, player_stats, player_type):
        predict = self.ann_model.predict(player_stats)[0]
        program = None
        for i in range(int(np.size(predict))):
            if predict[i] == max(predict):
                program = i + 1
        text_program = self.__get_program_text__(type=player_type, index=program)
        return [program, text_program]

    def __get_program_text__(self, type, index):
        file = str(type) + "_program_" + str(index) + ".txt"
        f = open('Resourses/Training program/'+str(file), 'r', encoding='utf-8')
        text = str(f.read())
        return text

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
        info = self.db_worker.get_player_history(name, ptype)
        data = list()
        indicators_all = list()
        name = None
        for element in info:
            name = str(element[0])
            indicators = list()
            for val in element[1]:
                indicators.append(val)
            indicators_all.append(indicators)
        progress = np.array(indicators_all[int(np.shape(indicators_all)[0])-1]) - np.array(indicators_all[int(np.shape(indicators_all)[0])-2])
        indicators_all.append(progress)
        data.append(name)
        data.append(indicators_all)
        return data
