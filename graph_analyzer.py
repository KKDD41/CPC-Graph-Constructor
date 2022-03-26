from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet


class GraphAnalyzerWindow(QWidget):
    def __init__(self, myRealization):
        super().__init__()
        self.realization = myRealization

        self.setWindowTitle('Graph Analyzer')

        self.resize(1000, 800)
        layout = QtWidgets.QGridLayout()

        # Creating graph reader


        # Creating buttons' widget and control buttons