import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from PyQt5.uic import loadUi
from veritabani_06 import ekle
class kitaplar(QMainWindow):
   def __init__(self):
       super(kitaplar,self).__init__()
       loadUi('kitaplik.ui',self)
       self.setWindowTitle('deneme ilk programım')
       self.kaydet.clicked.connect(self.on_pushButton_clicked)
   @pyqtSlot()
   def on_pushButton_clicked(self):
       kadi=self.kitapAdi.text()
       kitapYazar=self.kitapYazar.text()
       okunma = self.okunma.text()
       begeni = self.begeni.text()
       bildirim = ekle(kadi,kitapYazar,okunma,begeni)
       self.bildiri.setText(bildirim)
app=QApplication(sys.argv)
widget = kitaplar()
widget.show()
sys.exit(app.exec_())