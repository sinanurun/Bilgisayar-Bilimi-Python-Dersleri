import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Python Çayeli'
        self.left = 30
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        btn = QPushButton("deneme",self)
        btn.clicked.connect(self.mesajsorusu)
    def mesajsorusu(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print("hayır tıklandı")


#if __name__ == '__main__':
def calistir():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())