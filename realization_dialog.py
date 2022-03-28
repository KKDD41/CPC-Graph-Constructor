from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet, graph_to_string


class RealizationDlg(QWidget):
    def __init__(self, myRealization):
        super().__init__()
        self.realization = myRealization

        layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton(self)
        self.button.setFont(QFont('Calibri', 12))
        self.button.setText('Push to save realization')
        self.button.clicked.connect(self.save_realization)
        layout.addWidget(self.button)

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(1500, 1500)
        canvas.fill(QtCore.Qt.white)
        self.label.setPixmap(canvas)
        layout.addWidget(self.label)

    def paintEvent(self, event):
        painter = QPainter(self.label.pixmap())
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

    def save_realization(self):
        image = self.label.pixmap().toImage()
        self.realization.create_graph()
        print(self.realization.vector_of_segments)

        graph_file_name = graph_to_string(self.realization.graph)
        print(graph_file_name)
        image.save(f'{graph_file_name}.jpeg')
