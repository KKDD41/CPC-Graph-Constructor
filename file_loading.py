from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FileWidget(QFileDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Choose file with graph description'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.fileName = ''

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog


    def return_file(self):
        return self.fileName
