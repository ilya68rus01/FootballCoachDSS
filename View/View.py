from View.MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets


class View(QtWidgets.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.ui = Ui_MainWindow(self)
