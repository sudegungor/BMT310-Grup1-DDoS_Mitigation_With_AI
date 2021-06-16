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

        self.products = [
            {'name': 'Lenovo', 'price': 4000},
            {'name': 'Asus', 'price': 5000},
            {'name': 'Dell', 'price': 3000},
            {'name': 'Monster', 'price': 3000},
            {'name': 'Dell', 'price': 7000},
            {'name': 'Hp', 'price': 8000}
        ]


        self.loadKullanici()

        self.raporGorunuyorMu = True
        self.ui.btn_rapor.clicked.connect(self.raporGoster)

        self.kullaniciBilgiGorunuyorMu = True
        self.ui.btn_kullaniciBilgi.clicked.connect(self.KullaniciBilgiGoster)

    def raporGoster(self):
        self.raporGorunuyorMu = not(self.raporGorunuyorMu)
        self.ui.tbl_rapor.setVisible(self.raporGorunuyorMu)

    def KullaniciBilgiGoster(self):
        self.kullaniciBilgiGorunuyorMu = not(self.kullaniciBilgiGorunuyorMu)
        self.ui.tbl_kullaniciBilgi.setVisible(self.kullaniciBilgiGorunuyorMu)
    

    def loadKullanici(self):

        self.ui.tbl_kullaniciBilgi.setRowCount(len(self.products))
        self.ui.tbl_kullaniciBilgi.setColumnCount(2)
        self.ui.tbl_kullaniciBilgi.setHorizontalHeaderLabels(['Name', 'Price'])

        row = 0
        for product in self.products:
            self.ui.tbl_kullaniciBilgi.setItem(row, 0, QTableWidgetItem(product['name']))
            self.ui.tbl_kullaniciBilgi.setItem(row, 1, QTableWidgetItem(str(product['price'])))
            row += 1
        '''
        self.ui.tbl_kullaniciBilgi.setRowCount(3)
        self.ui.tbl_kullaniciBilgi.setColumnCount(2)
        self.ui.tbl_kullaniciBilgi.setItem(0,0,QTableWidgetItem('Samsung s5'))
        self.ui.tbl_kullaniciBilgi.setItem(0,1,QTableWidgetItem('2000'))
        self.ui.tbl_kullaniciBilgi.setItem(1,0,QTableWidgetItem('Asus Zenfone'))
        self.ui.tbl_kullaniciBilgi.setItem(1,1,QTableWidgetItem('3500'))
        '''

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
    def kullaniciBilgi(self):
        pass

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.setWindowTitle('Tablo uygulaması')
    win.show()
    sys.exit(app.exec_())
    
App()