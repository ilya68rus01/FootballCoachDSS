from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget


class TrainingDataWidget(QWidget):
    def __init__(self, parent=None, player_type=None):
        _translate = QtCore.QCoreApplication.translate
        QWidget.__init__(self, parent=parent)
        self.grid_layout = QtWidgets.QGridLayout()

        self.speed_label_all = QtWidgets.QLabel("Max speed")
        self.completion_label_all = QtWidgets.QLabel("All completion")
        self.penalty_label_all = QtWidgets.QLabel("All penalty")
        self.long_shots_label_all = QtWidgets.QLabel("All long shots")
        self.penalty_acc_label_all = QtWidgets.QLabel("All penalty accuracy")
        self.awnings_label_all = QtWidgets.QLabel("All awnings")
        self.dribbling_label_all = QtWidgets.QLabel("All dribbling")
        self.long_pass_label_all = QtWidgets.QLabel("All long pass")
        self.short_pass_label_all = QtWidgets.QLabel("All short pass")
        self.intercepts_label_all = QtWidgets.QLabel("All intercepts")
        self.head_game_label_all = QtWidgets.QLabel("All head games")
        self.selection_label_all = QtWidgets.QLabel("All selection")
        self.tackle_label_all = QtWidgets.QLabel("All tackle")

        self.speed_label_successfully = QtWidgets.QLabel("Speed")
        self.completion_label_successfully = QtWidgets.QLabel("Completion")
        self.penalty_label_successfully = QtWidgets.QLabel("Penalty")
        self.long_shots_label_successfully = QtWidgets.QLabel("Long shots")
        self.penalty_acc_label_successfully = QtWidgets.QLabel("Penalty accuracy")
        self.awnings_label_successfully = QtWidgets.QLabel("Awnings")
        self.dribbling_label_successfully = QtWidgets.QLabel("Dribbling")
        self.long_pass_label_successfully = QtWidgets.QLabel("Long pass")
        self.short_pass_label_successfully = QtWidgets.QLabel("Short pass")
        self.intercepts_label_successfully = QtWidgets.QLabel("Intercepts")
        self.head_game_label_successfully = QtWidgets.QLabel("Head games")
        self.selection_label_successfully = QtWidgets.QLabel("Selection")
        self.tackle_label_successfully = QtWidgets.QLabel("Tackle")

        self.speed_successfully = QtWidgets.QLineEdit()
        self.completion_successfully = QtWidgets.QLineEdit()
        self.penalty_successfully = QtWidgets.QLineEdit()
        self.long_shots_successfully = QtWidgets.QLineEdit()
        self.penalty_acc_successfully = QtWidgets.QLineEdit()
        self.awnings_successfully = QtWidgets.QLineEdit()
        self.dribbling_successfully = QtWidgets.QLineEdit()
        self.long_pass_successfully = QtWidgets.QLineEdit()
        self.short_pass_successfully = QtWidgets.QLineEdit()
        self.intercepts_successfully = QtWidgets.QLineEdit()
        self.head_game_successfully = QtWidgets.QLineEdit()
        self.selection_successfully = QtWidgets.QLineEdit()
        self.tackle_successfully = QtWidgets.QLineEdit()

        self.speed_all = QtWidgets.QLineEdit()
        self.completion_all = QtWidgets.QLineEdit()
        self.penalty_all = QtWidgets.QLineEdit()
        self.long_shots_all = QtWidgets.QLineEdit()
        self.penalty_acc_all = QtWidgets.QLineEdit()
        self.awnings_all = QtWidgets.QLineEdit()
        self.dribbling_all = QtWidgets.QLineEdit()
        self.long_pass_all = QtWidgets.QLineEdit()
        self.short_pass_all = QtWidgets.QLineEdit()
        self.intercepts_all = QtWidgets.QLineEdit()
        self.head_game_all = QtWidgets.QLineEdit()
        self.selection_all = QtWidgets.QLineEdit()
        self.tackle_all = QtWidgets.QLineEdit()

        self.hand_play_label_All = QtWidgets.QLabel("All Hand play")
        self.kicking_play_label_All = QtWidgets.QLabel("All Kicking play")
        self.dives_label_All = QtWidgets.QLabel("All Dives")
        self.penalty_label_All = QtWidgets.QLabel("All Penalty")

        self.hand_play_label_successfully = QtWidgets.QLabel("Successfully Hand play")
        self.kicking_play_label_successfully = QtWidgets.QLabel("Successfully Kicking play")
        self.dives_label_successfully = QtWidgets.QLabel("Successfully Dives")
        self.penalty_label_successfully_gk = QtWidgets.QLabel("Successfully Penalty")

        self.hand_play_all = QtWidgets.QLineEdit()
        self.kicking_play_all = QtWidgets.QLineEdit()
        self.dives_all = QtWidgets.QLineEdit()
        self.penalty_all_gk = QtWidgets.QLineEdit()
        self.hand_play_successfully = QtWidgets.QLineEdit()
        self.kicking_play_successfully = QtWidgets.QLineEdit()
        self.dives_successfully = QtWidgets.QLineEdit()
        self.penalty_successfully_gk = QtWidgets.QLineEdit()
        self.type = player_type
        self.concrete_init()
        self.setLayout(self.grid_layout)

    def concrete_init(self):
        if self.type == "goalkeeper":
            self.init_goalkeeper_Ui()
        if self.type != "goalkeeper":
            self.initUi()

    def init_goalkeeper_Ui(self):
        self.grid_layout.addWidget(self.hand_play_label_All, 0, 0)
        self.grid_layout.addWidget(self.kicking_play_label_All, 0, 2)
        self.grid_layout.addWidget(self.dives_label_All, 0, 4)
        self.grid_layout.addWidget(self.penalty_label_All, 0, 6)
        self.grid_layout.addWidget(self.hand_play_label_successfully, 0, 1)
        self.grid_layout.addWidget(self.kicking_play_label_successfully, 0, 3)
        self.grid_layout.addWidget(self.dives_label_successfully, 0, 5)
        self.grid_layout.addWidget(self.penalty_label_successfully_gk, 0, 7)
        self.grid_layout.addWidget(self.hand_play_all, 1, 0)
        self.grid_layout.addWidget(self.hand_play_successfully, 1, 1)
        self.grid_layout.addWidget(self.kicking_play_all, 1, 2)
        self.grid_layout.addWidget(self.kicking_play_successfully, 1, 3)
        self.grid_layout.addWidget(self.dives_all, 1, 4)
        self.grid_layout.addWidget(self.dives_successfully, 1, 5)
        self.grid_layout.addWidget(self.penalty_all_gk, 1, 6)
        self.grid_layout.addWidget(self.penalty_successfully_gk, 1, 7)

    def initUi(self):
        self.grid_layout.addWidget(self.speed_label_all, 0, 0)
        self.grid_layout.addWidget(self.speed_label_successfully, 0, 1)
        self.grid_layout.addWidget(self.completion_label_all, 0, 2)
        self.grid_layout.addWidget(self.completion_label_successfully, 0, 3)
        self.grid_layout.addWidget(self.penalty_label_all, 0, 4)
        self.grid_layout.addWidget(self.penalty_label_successfully, 0, 5)
        self.grid_layout.addWidget(self.long_shots_label_all, 0, 6)
        self.grid_layout.addWidget(self.long_shots_label_successfully, 0, 7)
        self.grid_layout.addWidget(self.penalty_acc_label_all, 0, 8)
        self.grid_layout.addWidget(self.penalty_acc_label_successfully, 0, 9)
        self.grid_layout.addWidget(self.awnings_label_all, 0, 10)
        self.grid_layout.addWidget(self.awnings_label_successfully, 0, 11)
        self.grid_layout.addWidget(self.dribbling_label_all, 0, 12)
        self.grid_layout.addWidget(self.dribbling_label_successfully, 0, 13)
        self.grid_layout.addWidget(self.long_pass_label_all, 0, 14)
        self.grid_layout.addWidget(self.long_pass_label_successfully, 0, 15)
        self.grid_layout.addWidget(self.short_pass_label_all, 0, 16)
        self.grid_layout.addWidget(self.short_pass_label_successfully, 0, 17)
        self.grid_layout.addWidget(self.intercepts_label_all, 0, 18)
        self.grid_layout.addWidget(self.intercepts_label_successfully, 0, 19)
        self.grid_layout.addWidget(self.head_game_label_all, 0, 20)
        self.grid_layout.addWidget(self.head_game_label_successfully, 0, 21)
        self.grid_layout.addWidget(self.selection_label_all, 0, 22)
        self.grid_layout.addWidget(self.selection_label_successfully, 0, 23)
        self.grid_layout.addWidget(self.tackle_label_all, 0, 24)
        self.grid_layout.addWidget(self.tackle_label_successfully, 0, 25)
        self.grid_layout.addWidget(self.speed_all, 1,  0)
        self.grid_layout.addWidget(self.speed_successfully, 1, 1)
        self.grid_layout.addWidget(self.completion_all, 1,  2)
        self.grid_layout.addWidget(self.completion_successfully, 1, 3)
        self.grid_layout.addWidget(self.penalty_all, 1,  4)
        self.grid_layout.addWidget(self.penalty_successfully, 1, 5)
        self.grid_layout.addWidget(self.long_shots_all, 1,  6)
        self.grid_layout.addWidget(self.long_shots_successfully, 1, 7)
        self.grid_layout.addWidget(self.penalty_acc_all, 1,  8)
        self.grid_layout.addWidget(self.penalty_acc_successfully, 1, 9)
        self.grid_layout.addWidget(self.awnings_all, 1, 10)
        self.grid_layout.addWidget(self.awnings_successfully, 1, 11)
        self.grid_layout.addWidget(self.dribbling_all, 1, 12)
        self.grid_layout.addWidget(self.dribbling_successfully, 1, 13)
        self.grid_layout.addWidget(self.long_pass_all, 1, 14)
        self.grid_layout.addWidget(self.long_pass_successfully, 1, 15)
        self.grid_layout.addWidget(self.short_pass_all, 1, 16)
        self.grid_layout.addWidget(self.short_pass_successfully, 1, 17)
        self.grid_layout.addWidget(self.intercepts_all, 1, 18)
        self.grid_layout.addWidget(self.intercepts_successfully, 1, 19)
        self.grid_layout.addWidget(self.head_game_all, 1, 20)
        self.grid_layout.addWidget(self.head_game_successfully, 1, 21)
        self.grid_layout.addWidget(self.selection_all, 1, 22)
        self.grid_layout.addWidget(self.selection_successfully, 1, 23)
        self.grid_layout.addWidget(self.tackle_all, 1, 24)
        self.grid_layout.addWidget(self.tackle_successfully, 1, 25)

    def get_data_gk(self):
        fields = list()
        fields.append(["hand play", self.hand_play_successfully.text(), self.hand_play_all.text()])
        fields.append(["kicking play", self.kicking_play_successfully.text(), self.kicking_play_all.text()])
        fields.append(["dives", self.dives_successfully.text(), self.dives_all.text()])
        fields.append(["penalty gk", self.penalty_successfully_gk.text(), self.penalty_all_gk.text()])
        return fields

    def get_data(self):
        fields = list()
        fields.append(["speed", self.speed_successfully.text(), self.speed_all.text()])
        fields.append(["completion", self.completion_successfully.text(), self.completion_all.text()])
        fields.append(["penalty", self.penalty_successfully.text(), self.penalty_all.text()])
        fields.append(["long shots", self.long_shots_successfully.text(), self.long_shots_all.text()])
        fields.append(["penalty accuracy", self.penalty_acc_successfully.text(), self.penalty_acc_all.text()])
        fields.append(["awnings", self.awnings_successfully.text(), self.awnings_all .text()])
        fields.append(["dribbling", self.dribbling_successfully.text(), self.dribbling_all.text()])
        fields.append(["long pass", self.long_pass_successfully.text(), self.long_pass_all.text()])
        fields.append(["short pass", self.short_pass_successfully.text(), self.short_pass_all.text()])
        fields.append(["intercepts", self.intercepts_successfully.text(), self.intercepts_all.text()])
        fields.append(["head games", self.head_game_successfully.text(), self.head_game_all.text()])
        fields.append(["selection", self.selection_successfully.text(), self.selection_all.text()])
        fields.append(["tackle", self.tackle_successfully.text(), self.tackle_all.text()])
        return fields
