import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Util import Util
from Raporlama.Rapor import Rapor
from UI.design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loglar = Util.rapor.logkayitlari
        self.loadItems()

        self.raporGorunuyorMu = True
        self.ui.btn_rapor.clicked.connect(self.raporGoster)

    def raporGoster(self):
        self.raporGorunuyorMu = not(self.raporGorunuyorMu)
        self.ui.tbl_rapor.setVisible(self.raporGorunuyorMu)

    def loadItems(self):
        self.ui.tbl_rapor.setRowCount(len(self.loglar) -1 )
        self.ui.tbl_rapor.setColumnCount(3)
        self.ui.tbl_rapor.setHorizontalHeaderLabels(['saldırı', 'tarih', 'zaman'])

        row = 0
        for log in self.loglar[1:]:

            self.ui.tbl_rapor.setItem(row, 0, QTableWidgetItem(
                log[0]
            ))

            self.ui.tbl_rapor.setItem(row, 1, QTableWidgetItem(
                str(log[1])
            ))

            self.ui.tbl_rapor.setItem(row, 2, QTableWidgetItem(
                str(log[2])
            ))
            row += 1

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.setWindowTitle('Tablo uygulaması')
    win.show()
    sys.exit(app.exec_())

# App()