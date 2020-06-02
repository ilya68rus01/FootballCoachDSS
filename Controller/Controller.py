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
        self.normalize_data = list()
        #self.model.load_models()

    def on_start_button_click(self):
        #self.model.load_data()
        self.model.load_models(self.view.get_player_type())
        print(self.model.predict_train_schedudle(np.array([0.79, 0.58, 0.77, 0.47])))
        #self.model.load_models()

    def on_add_button_click(self):
        training_data = self.view.get_training_data()
        self.view.ui.add_window.close()
        self.normalize_data = self.model.convert_training_data(data=training_data)
        print(self.normalize_data)
        self.view.vizualize_indicators(name=self.normalize_data[0], indicators=self.normalize_data[1])

    def on_clear_button_click(self):
        self.__init__(model=Model(), view=View())
