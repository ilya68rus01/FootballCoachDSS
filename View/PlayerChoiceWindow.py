from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from Model.DbWorker import DbWorker


class PlayerChoiceWindow(QWidget):
    def __init__(self, parent=None):
        _translate = QtCore.QCoreApplication.translate
        QWidget.__init__(self, parent=parent)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.horizontal_layout_for_box = QtWidgets.QHBoxLayout()
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.groupBox = QtWidgets.QGroupBox()
        self.group_box_layout = QtWidgets.QHBoxLayout()
        self.goalkeeper_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.defender_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.midfielder_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.attacker_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.player_label = QtWidgets.QLabel()
        self.player_list_box = QtWidgets.QComboBox()
        self.accept_button = QtWidgets.QPushButton()
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.goalkeeper_radio_button.clicked.connect(self.create_player_list)
        self.defender_radio_button.clicked.connect(self.create_player_list)
        self.midfielder_radio_button.clicked.connect(self.create_player_list)
        self.attacker_radio_button.clicked.connect(self.create_player_list)
        self.initUi()

    def initUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Player choice", "Выбор игрока"))
        self.goalkeeper_radio_button.setText("Goalkeeper")
        self.defender_radio_button.setText("Defender")
        self.midfielder_radio_button.setText("Midlfielder")
        self.attacker_radio_button.setText("Attacker")
        self.accept_button.setText("Создать отчет")
        self.player_label.setText("Имя игрока: ")
        self.vertical_layout.addWidget(self.groupBox)
        self.vertical_layout.addLayout(self.horizontal_layout_for_box)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.groupBox.setLayout(self.group_box_layout)
        self.group_box_layout.addWidget(self.goalkeeper_radio_button)
        self.group_box_layout.addWidget(self.defender_radio_button)
        self.group_box_layout.addWidget(self.midfielder_radio_button)
        self.group_box_layout.addWidget(self.attacker_radio_button)
        self.horizontal_layout_for_box.addWidget(self.player_label)
        self.horizontal_layout_for_box.addWidget(self.player_list_box)
        self.horizontal_layout.addItem(self.spacerItem)
        self.horizontal_layout.addWidget(self.accept_button)
        self.setLayout(self.vertical_layout)

    def create_player_list(self):
        current_type = self.get_player_type()
        db_worker = DbWorker()
        player_list = db_worker.get_player_list(current_type)
        self.player_list_box.clear()
        for i in player_list:
            self.player_list_box.addItem(i)

    def get_player_type(self):
        if (self.attacker_radio_button.isChecked()):
            return "attacker"
        if (self.defender_radio_button.isChecked()):
            return "defender"
        if (self.goalkeeper_radio_button.isChecked()):
            return "goalkeeper"
        if (self.midfielder_radio_button.isChecked()):
            return "midfielder"