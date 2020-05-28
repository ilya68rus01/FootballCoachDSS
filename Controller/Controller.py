from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, pyqtSignal, QObject
from View.View import View
from Model.Model import Model


class Controller:
    struct = None
    flag = False
    counter = 0

    def __init__(self, model: Model, view: View):
        super().__init__()
        self.view = view
        self.model = model
        self.view.show()
        self.model.load_data()
        self.model.load_model()
        #self.model.fit()
