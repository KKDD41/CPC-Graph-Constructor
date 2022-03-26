from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet
from drawing_window import DrawingWindow


class RealizationDlg(QDialog):
    def __init__(self, myRealization):
        super().__init__()
        self.realization = myRealization

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if len(self.realization.vector_of_segments) != 0:
            for i in range(len(self.realization.vector_of_segments) - 1):
                painter.drawLine(self.realization.vector_of_segments[i + 1][0],
                                 self.realization.vector_of_segments[i + 1][1],
                                 self.realization.vector_of_segments[i][0], self.realization.vector_of_segments[i][1])
                painter.drawText(
                    (self.realization.vector_of_segments[i][0] + self.realization.vector_of_segments[i + 1][0]) // 2,
                    (self.realization.vector_of_segments[i][1] + self.realization.vector_of_segments[i + 1][1]) // 2,
                    alphabet[i])
            painter.drawLine(self.realization.vector_of_segments[0][0], self.realization.vector_of_segments[0][1],
                             self.realization.vector_of_segments[-1][0],
                             self.realization.vector_of_segments[-1][1])
            painter.drawText(
                (self.realization.vector_of_segments[0][0] + self.realization.vector_of_segments[-1][0]) // 2,
                (self.realization.vector_of_segments[0][1] + self.realization.vector_of_segments[-1][1]) // 2,
                alphabet[len(self.realization.vector_of_segments) - 1])
        painter.end()
