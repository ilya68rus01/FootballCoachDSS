from View.MainWindow import *


class View(QtWidgets.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.ui = Ui_MainWindow(self)

