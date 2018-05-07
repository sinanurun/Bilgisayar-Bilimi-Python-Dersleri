import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import pyqtSlot
from ev02 import ev02

class ev(QDialog):
    def __init__(self):
        super(ev, self).__init__()
        loadUi("ev01.ui", self)
        self.btn.clicked.connect(self.yeni_pencere)
    def yeni_pencere(self):
        y_pencere = ev02(self)
        y_pencere.show()
    def cyazdir(self):
        print("tiklandi")

app = QApplication(sys.argv)
prog = ev()
prog.show()
sys.exit(app.exec_())
