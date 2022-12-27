import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.w = 400
        self.h = 400
        self.resize(self.w, self.h)
        self.setMinimumSize(self.w / 2, self.h / 2)

        self.widthFactor = 1
        self.heightFactor = 1

        self.label = QtWidgets.QLabel("Label", self, alignment=QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font: {}pt Arial; background:lightblue".format(20 * self.heightFactor))
        self.label.resize(self.w * self.widthFactor, self.h * 0.25 * self.heightFactor)
        self.label.adjustSize()

        self.lineEdit = QtWidgets.QLineEdit(" Hello World ! ", self)
        self.lineEdit.resize(self.w * 0.75 * self.widthFactor, self.h * 0.1 * self.heightFactor)

        self.button = QtWidgets.QPushButton('Button', self)
        self.button.clicked.connect(self.clickButton)
        self.button.resize(self.w * 0.25 * self.widthFactor, self.h * 0.2 * self.heightFactor)

    def clickButton(self):
        self.label.setText(self.lineEdit.text())
        self.label.adjustSize()
        self.label.move(
            self.rect().center() - self.label.rect().center() - QPoint(0, self.h * 0.25 * self.heightFactor))

    def resizeEvent(self, event):
        self.widthFactor = self.rect().width() / 400
        self.heightFactor = self.rect().height() / 400

        self.label.move(self.rect().center() - self.label.rect().center() - QPoint(0, self.h / 4 * self.heightFactor))
        self.lineEdit.resize(self.w * 0.75 * self.widthFactor, self.h * 0.1 * self.heightFactor)
        self.lineEdit.move(self.rect().center() - self.lineEdit.rect().center())
        self.button.resize(self.w * 0.25 * self.widthFactor, self.h * 0.2 * self.heightFactor)
        self.button.move(
            self.rect().center() - self.button.rect().center() - QPoint(0, -self.h * 0.3 * self.heightFactor))
        super(Window, self).resizeEvent(event)


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setWindowTitle('SSAU GUI. 1 laboratory work 2022')
    window.show()
    sys.exit(application.exec_())
