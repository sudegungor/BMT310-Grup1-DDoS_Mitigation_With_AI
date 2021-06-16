from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Window(QWidget): # Window class  QWidget
#class'ından inheritance(miras almak) ediyor(window  QWidgetclass'ında bulunan tüm methotları kullanabiliyor)    
    def __init__(self): # yapıcı metot
        super().__init__() # miras almak için gerekli kod satırı
        self.setGeometry(50,50,1000,450)
        self.setWindowTitle("DDoS Mitigation with AI")
        self.buttonAc()
        self.buttonKapat()
        self.buttonKullanici()
        self.buttonYardım()
        self.buttonRapor()
        self.buttonTicket()
        self.label()
        self.labelMetin()
        self.show()
        
    def buttonKullanici(self):
        button=QPushButton("Kullanıcı Bilgileri", self)
        button.resize(130,30) # boyut ayarla
        button.move(0,65) # konum (px)
        button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
        button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
    
    def buttonAc(self):
         button=QPushButton("Aç", self)
         button.setToolTip("DDoS Savunma Programını Etkinleştir.") # açıklama
         button.resize(130,30) # boyut ayarla
         button.move(0,105) # konum (px)
         button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
         button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
    def buttonKapat(self):
         button=QPushButton("Kapat", self)
         button.setToolTip("DDoS Savunma Programını Kapat.") # açıklama
         button.resize(130,30) # boyut ayarla
         button.move(0,145) # konum (px)
         button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
         button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
    def buttonRapor(self):
         button=QPushButton("Rapor", self)
         button.setToolTip("DDoS Savunma Programıyla ilgili Mecut Raporlarınızı Görmek İçin Tıklayınız") # açıklama
         button.resize(130,30) # boyut ayarla
         button.move(0,185) # konum (px)
         button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
         button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
         
    def buttonTicket(self):
         button=QPushButton("Ticket Oluştur", self)
         button.resize(130,30) # boyut ayarla
         button.move(0,225) # konum (px)
         button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
         button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
    def buttonYardım(self):
         button=QPushButton("Yardım", self)
         button.setToolTip("Yardım menüsü") # açıklama
         button.resize(130,30) # boyut ayarla
         button.move(0,265) # konum (px)
         button.clicked.connect(self.buttonFunciton) #butona tıklandığında yapılacak işlemin çağrılması
         button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
    def label(self):
        self.text1=QLabel("DDoS Savunma Sistemi",self)
        self.text1.move(0, 0) # konum belirle
        self.text1.setFont(QFont("Arial",13))
        self.text1.resize(3000,30) # boyut ayarla
        self.text1.setStyleSheet("background-color: white")
        
    def labelMetin(self):
        self.text1=QLabel("Hoş Geldiniz",self)
        self.text1.move(400, 180) # konum belirle
        self.text1.setFont(QFont("Arial",30))
        
      
        
        
         
    def buttonFunciton(self):#butonun yapacağı işlemin tannımlanması
         print("hello world")
        
        
        
        
        
        
window=Window() #obje 