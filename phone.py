import re
from models import List
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from mainForm import Ui_Form
import sys


class Main_window(QtWidgets.QMainWindow):
    def __init__(self, query):
        super(Main_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(891, 443)
        self.query = query
        self.ui.inp.setPlaceholderText('Введите текст для поиска...')

        self.ui.btnSearch.clicked.connect(self.search_name)

    def get_all_value(self):
        self.ui.table.setRowCount(0)
        self.ui.table.horizontalHeader().setSectionResizeMode(0, 1)
        # self.ui.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ui.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        # query = List.select()
        for i, data in enumerate(self.query):
            try:
                mobil = re.findall(r'8-\d\d\d-\d\d\d-\d\d-\d\d', data.Fio)
                fio = ' '.join(data.Fio.split()[:3])

                self.ui.table.setRowCount(i + 1)
                self.ui.table.setItem(i, 0, QTableWidgetItem(data.Name.title()))

                self.ui.table.setItem(i, 1, QTableWidgetItem(fio.title()))
                self.ui.table.setItem(i, 2, QTableWidgetItem(' '.join(mobil)))
                self.ui.table.setItem(i, 3, QTableWidgetItem(data.Vts))
                self.ui.table.setItem(i, 4, QTableWidgetItem(data.City))

            except ValueError:
                continue
        self.ui.lcd.display(self.ui.table.rowCount())

    def search_name(self):
        self.query = List.select().where(
            List.Fio ** f'%{self.ui.inp.text().upper()}%' |
            List.Name ** f'%{self.ui.inp.text().upper()}%' |
            List.Vts ** f'%{self.ui.inp.text().upper()}%')
        self.get_all_value()


app = QtWidgets.QApplication([])
application = Main_window(List.select())
application.get_all_value()
application.show()

sys.exit(app.exec())
