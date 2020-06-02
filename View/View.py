from View.MainWindow import *


class View(QtWidgets.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.ui = Ui_MainWindow(self)

    def set_on_start_button_listener(self, action):
        self.ui.start_button.clicked.connect(action)

    def set_on_clear_button_listener(self, action):
        self.ui.clear_button.clicked.connect(action)

    def set_on_add_button_listener(self, action):
        self.ui.add_window.ok_button.clicked.connect(action)

    def get_training_data(self):
        return self.ui.add_window.get_fields()

    def vizualize_indicators(self, name, indicators):
        self.ui.create_indicator_table(name=name, data=indicators)

    def get_player_type(self):
        print(self.ui.get_player_type())
        return self.ui.get_player_type()

