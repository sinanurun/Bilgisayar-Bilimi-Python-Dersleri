import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class Life2Coding(QDialog):
   def __init__(self):
       super(Life2Coding,self).__init__()
       loadUi('life2coding.ui',self)
       self.setWindowTitle('deneme ilk programım')
       self.pushButton.clicked.connect(self.on_pushButton_clicked)
   @pyqtSlot()
   def on_pushButton_clicked(self):
       import mesaj_kutusu
       uygulama = mesaj_kutusu.App()
       #uygulama.show()
       self.label1.setText("Hoş Geldiniz")
app=QApplication(sys.argv)
widget = Life2Coding()
widget.show()
sys.exit(app.exec_())