from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from View.TrainingDataWidget import *



class AddWidget(QWidget):
    def __init__(self, parent=None, i=0):
        _translate = QtCore.QCoreApplication.translate
        QWidget.__init__(self, parent=parent)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.groupBox = QtWidgets.QGroupBox()
        self.training_data_layout = QtWidgets.QVBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.name_layout = QtWidgets.QHBoxLayout()
        self.group_box_layout = QtWidgets.QHBoxLayout()
        self.match_counter = QtWidgets.QSpinBox()
        self.match_counter_layout = QtWidgets.QHBoxLayout()
        self.goalkeeper_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.defender_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.midfielder_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.attacker_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.full_name_label = QtWidgets.QLabel()
        self.full_name_line_edit = QtWidgets.QLineEdit()
        self.ok_button = QtWidgets.QPushButton()
        self.cancel_button = QtWidgets.QPushButton()
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.goalkeeper_radio_button.clicked.connect(self.create_training_data_field)
        self.defender_radio_button.clicked.connect(self.create_training_data_field)
        self.midfielder_radio_button.clicked.connect(self.create_training_data_field)
        self.attacker_radio_button.clicked.connect(self.create_training_data_field)
        self.initUi()

    def initUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddWindow", "Добавление игрока"))
        self.goalkeeper_radio_button.setText("Goalkeeper")
        self.defender_radio_button.setText("Defender")
        self.midfielder_radio_button.setText("Midlfielder")
        self.attacker_radio_button.setText("Attacker")
        self.full_name_label.setText("Full name")
        self.match_counter_layout.addWidget(self.match_counter)
        self.match_counter_layout.addWidget(self.groupBox)
        self.vertical_layout.addLayout(self.match_counter_layout)
        self.name_layout.addWidget(self.full_name_label)
        self.name_layout.addWidget(self.full_name_line_edit)
        self.vertical_layout.addLayout(self.name_layout)
        self.vertical_layout.addLayout(self.training_data_layout)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.groupBox.setLayout(self.group_box_layout)
        self.group_box_layout.addWidget(self.goalkeeper_radio_button)
        self.group_box_layout.addWidget(self.defender_radio_button)
        self.group_box_layout.addWidget(self.midfielder_radio_button)
        self.group_box_layout.addWidget(self.attacker_radio_button)
        self.horizontal_layout.addWidget(self.cancel_button)
        self.horizontal_layout.addItem(self.spacerItem)
        self.ok_button.setText("Поддтвердить")
        self.cancel_button.setText("Очистить")
        self.horizontal_layout.addWidget(self.ok_button)
        self.setLayout(self.vertical_layout)

    def create_training_data_field(self):
        current_type = self.get_player_type()
        self.layer_list = list()
        self.scroll_area.clearFocus()
        scroll_layout = QtWidgets.QVBoxLayout()
        wgt1 = QWidget()
        if current_type == "goalkeeper":
            for i in range(int(self.match_counter.text())):
                wgt = TrainingDataWidget(player_type=current_type)
                self.layer_list.append(wgt)
                scroll_layout.addWidget(self.layer_list[i])
        if current_type != "goalkeeper":
            for i in range(int(self.match_counter.text())):
                wgt = TrainingDataWidget(player_type=current_type)
                self.layer_list.append(wgt)
                scroll_layout.addWidget(self.layer_list[i])
        wgt1.setLayout(scroll_layout)
        self.scroll_area.setWidget(wgt1)
        self.training_data_layout.addWidget(self.scroll_area)

    def get_player_type(self):
        if (self.attacker_radio_button.isChecked()):
            return "attacker"
        if (self.defender_radio_button.isChecked()):
            return "defender"
        if (self.goalkeeper_radio_button.isChecked()):
            return "goalkeeper"
        if (self.midfielder_radio_button.isChecked()):
            return "midfielder"

    def get_fields(self):
        data = list()
        data.append(self.full_name_line_edit.text())
        if self.get_player_type() == "goalkeeper":
            for i in range(int(self.match_counter.text())):
                data.append(self.layer_list[i].get_data_gk())
        else:
            for i in range(int(self.match_counter.text())):
                data.append(self.layer_list[i].get_data())
        return data


