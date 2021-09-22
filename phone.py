from peewee import *
from PyQt5 import QtWidgets
from mainForm import Ui_Form  # импорт нашего сгенерированного файла
import sys


class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(891, 444)


app = QtWidgets.QApplication([])
application = Main_window()
application.show()

sys.exit(app.exec())
