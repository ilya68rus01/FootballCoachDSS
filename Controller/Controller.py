from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, pyqtSignal, QObject
from View.View import View
from Model.Model import Model
import numpy as np
from Model.DataConverter import DataConverter


class Controller:
    struct = None
    flag = False
    counter = 0

    def __init__(self, model: Model, view: View):
        super().__init__()
        self.view = view
        self.model = model
        self.view.show()
        self.view.set_on_start_button_listener(lambda: self.on_start_button_click())
        self.view.set_on_clear_button_listener(lambda: self.on_clear_button_click())
        self.view.set_on_add_button_listener(lambda: self.on_add_button_click())
        self.view.set_on_report_button_listener(lambda: self.on_report_button_click())
        self.normalize_data = list()

    def on_report_button_click(self):
        name, player_type = self.view.get_current_player_for_report()
        player_info = self.model.get_player_from_db(name, player_type)
        self.view.ui.report_window.close()
        self.view.create_report(player_info)


    def on_start_button_click(self):
        player_type = self.view.get_player_type()
        self.model.load_models(player_type)
        player_stats = np.array([self.normalize_data[1]], dtype=np.float32)
        train_program_index, train_program_text = self.model.predict_train_schedudle(player_stats=player_stats,
                                                                                         player_type=player_type)
        self.view.vizualize_train_program(program=train_program_text)
        self.model.set_data_player(name=self.normalize_data[0],
                                   params=self.normalize_data[1],
                                   player_type=player_type,
                                   train_program=train_program_index)
        self.model.save_player_in_db()

    def on_add_button_click(self):
        training_data = self.view.get_training_data()
        self.view.ui.add_window.close()
        self.normalize_data = self.model.convert_training_data(data=training_data)
        self.view.vizualize_indicators(name=self.normalize_data[0], indicators=self.normalize_data[1])

    def on_clear_button_click(self):
        self.__init__(model=Model(), view=View())
