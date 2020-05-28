import sys

from PyQt5.QtWidgets import QApplication
from Controller.Controller import Controller
from View.View import View
from Model.Model import Model


def main():
    app = QApplication(sys.argv)
    # Инициализация контроллера с заданием модели и представления
    Controller(model=Model(), view=View())
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
