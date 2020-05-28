# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QVBoxLayout, QErrorMessage
from PyQt5.QtWidgets import QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Ui_MainWindow():

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.data_player = QtWidgets.QWidget()
        self.data_player.setObjectName("data_player")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.data_player)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.data_player)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.data_player, "")
        self.training_schedudle = QtWidgets.QWidget()
        self.training_schedudle.setObjectName("training_schedudle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.training_schedudle)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.training_schedudle)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.tabWidget.addTab(self.training_schedudle, "")
        self.progress_report = QtWidgets.QWidget()
        self.progress_report.setObjectName("progress_report")
        self.tabWidget.addTab(self.progress_report, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.goalkeeper_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.goalkeeper_radio_button.setObjectName("goalkeeper_radio_button")
        self.verticalLayout_2.addWidget(self.goalkeeper_radio_button)
        self.defender_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.defender_radio_button.setObjectName("defender_radio_button")
        self.verticalLayout_2.addWidget(self.defender_radio_button)
        self.midfielder_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.midfielder_radio_button.setObjectName("midfielder_radio_button")
        self.verticalLayout_2.addWidget(self.midfielder_radio_button)
        self.attacker_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.attacker_radio_button.setObjectName("attacker_radio_button")
        self.verticalLayout_2.addWidget(self.attacker_radio_button)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_player), _translate("MainWindow", "Данные игрока"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.training_schedudle), _translate("MainWindow", "График тренировок"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.progress_report), _translate("MainWindow", "Отчет о прогрессе"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.goalkeeper_radio_button.setText(_translate("MainWindow", "Вратарь"))
        self.defender_radio_button.setText(_translate("MainWindow", "Защитник"))
        self.midfielder_radio_button.setText(_translate("MainWindow", "Полузащитник"))
        self.attacker_radio_button.setText(_translate("MainWindow", "Нападающий"))
        self.clear_button.setText(_translate("MainWindow", "Очистить"))
        self.start_button.setText(_translate("MainWindow", "Спрогнозировать треннировку"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
