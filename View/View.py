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

    def set_on_report_button_listener(self, action):
        self.ui.report_window.accept_button.clicked.connect(action)

    def get_training_data(self):
        return self.ui.add_window.get_fields()

    def vizualize_indicators(self, name, indicators):
        self.ui.create_indicator_table(name=name, data=indicators)

    def vizualize_train_program(self, program):
        self.ui.write_train_program(data=program)

    def get_player_type(self):
        return self.ui.get_player_type()

    def get_current_player_for_report(self):
        return [self.ui.report_window.player_list_box.currentText(), self.ui.report_window.get_player_type()]

    def create_report(self, player_info):
        self.ui.draw_report(player_info)

