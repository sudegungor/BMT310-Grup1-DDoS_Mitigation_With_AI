import sys
import os
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget,QTableWidget,QTableWidgetItem
class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.btn_kullaniciBilgi=QtWidgets.QPushButton(self)
        self.btn_kullaniciBilgi.setText("Kullanıcı Adı")
        self.btn_kullaniciBilgi.move(0,130)
        self.btn_kullaniciBilgi.resize(200,32)
        self.btn_rapor.clicked.connect(self.raporGoster)

        self.btn_ac=QtWidgets.QPushButton(self)
        self.btn_ac.setText("Aç")
        self.btn_ac.move(0,160)
        self.btn_ac.resize(200,32)

        self.btn_kapat=QtWidgets.QPushButton(self)
        self.btn_kapat.setText("Kapat")
        self.btn_kapat.move(0,190)
        self.btn_kapat.resize(200,32)
        

        self.btn_ticket=QtWidgets.QPushButton(self)
        self.btn_ticket.setText("Ticket Oluştur")
        self.btn_ticket.move(0,220)
        self.btn_ticket.resize(200,32)

        self.btn_rapor=QtWidgets.QPushButton(self)
        self.btn_rapor.setText("Rapor")
        self.btn_rapor.move(0,250)
        self.btn_rapor.resize(200,32)

        self.btn_yardim=QtWidgets.QPushButton(self)
        self.btn_yardim.setText("Yardım")
        self.btn_yardim.move(0,280)
        self.btn_yardim.resize(200,32)
    def raporGoster(self):
        sys.path=QFileDialog.getOpenFileName(self,'Open CVS',os.getenv('HOME'),'CVS(*.cvs)')
        if sys.path[0] !='':
            with open(sys.path[0],newline='')as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                ddos_sirket_bilgi=csv.reader(csv_file,delimiter=',',quotecher='|')
                for row_data in ddos_sirket_bilgi:
                    row=self.rowCount()
                    self.insertRow(row)
                    if len(row_data)>10:
                        self.setColumnCount(len(row_data))
                    for column,stuff in enumerate(row_data):
                        item=QTableWidgetItem(stuff)
                        self.setItem(row,column,item)


        



def app():
    app=QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec_())
app()