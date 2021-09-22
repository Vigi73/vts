import re
from models import List
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from mainForm import Ui_Form
import sys


class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(891, 444)

    def get_all_value(self):
        self.ui.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        # self.ui.table.setHorizontalHeaderItem(1, item)
        #self.ui.table.horizontalHeader().setDefaultSectionSize(220)
        self.ui.table.horizontalHeader().setSectionResizeMode(0, 1)
        self.ui.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        query = List.select()
        for i, data in enumerate(query):
            try:
                mobil = re.findall(r'8-\d\d\d-\d\d\d-\d\d-\d\d', data.Fio)
                fio = ' '.join(data.Fio.split()[:3])

                self.ui.table.setRowCount(i + 1)
                self.ui.table.setItem(i, 0, QTableWidgetItem(data.Name))

                self.ui.table.setItem(i, 1, QTableWidgetItem(fio))
                self.ui.table.setItem(i, 2, QTableWidgetItem(' '.join(mobil)))
                self.ui.table.setItem(i, 3, QTableWidgetItem(data.Vts))
                self.ui.table.setItem(i, 4, QTableWidgetItem(data.City))
            except ValueError:
                continue


app = QtWidgets.QApplication([])
application = Main_window()
application.get_all_value()
application.show()

sys.exit(app.exec())
