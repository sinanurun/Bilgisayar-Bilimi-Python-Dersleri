import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import pyqtSlot
class ev02(QDialog):
    def __init__(self, parent):
        super(ev02, self).__init__(parent)
        loadUi("ev02.ui", self)
