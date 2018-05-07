import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 30
        self.top = 30
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(200, 20)


        # Create a button in the window
        self.button1 = QPushButton('Şifrele', self)
        self.button1.move(20, 80)
        self.button2 = QPushButton('Coz', self)
        self.button2.move(200, 80)
        self.button2.clicked.connect(self.coz)
        self.button1.clicked.connect(self.sifrele)
        self.show()

    def sifrele(self):
        textboxValue = self.textbox.text()
        self.textbox2.setText(textboxValue)

    def coz(self):
        textboxValue2 = self.textbox2.text()
        self.textbox.setText(textboxValue2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())