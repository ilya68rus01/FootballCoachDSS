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
        self.group_box_layout = QtWidgets.QHBoxLayout()
        self.goalkeeper_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.defender_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.midfielder_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.attacker_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.ok_button = QtWidgets.QPushButton()
        self.cancel_button = QtWidgets.QPushButton()
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.vertical_layout.addWidget(self.groupBox)
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
        layer_list = list()
        self.scroll_area.clearFocus()
        scroll_layout = QtWidgets.QVBoxLayout()
        wgt1 = QWidget()
        if current_type == "goalkeeper":
            for i in range(2):
                wgt = TrainingDataWidget(player_type=current_type)
                layer_list.append(wgt)
                scroll_layout.addWidget(layer_list[i])
        if current_type != "goalkeeper":
            for i in range(6):
                wgt = TrainingDataWidget(player_type=current_type)
                layer_list.append(wgt)
                scroll_layout.addWidget(layer_list[i])
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
        pass
