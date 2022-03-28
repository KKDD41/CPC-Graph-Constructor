from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet


class DrawingWindow(QWidget):
    def __init__(self, myRealization):
        super().__init__()

        # Class fields
        self.drawing_mode = False
        self.x = 300
        self.y = 300

        self.realization = myRealization
        self.realization.add_vertex(self.x, self.y)

        # Window params
        self.resize(1700, 1500)
        self.setWindowTitle("Draw here your closed polygonal chain")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)

        # Buttons creating
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Draw your own polygonal chain and this realization will be uploaded to the Database.')
        self.label.setFont(QFont('Times New Roman', 14))
        layout.addWidget(self.label)

        self.pushButton_draw = QtWidgets.QPushButton(self)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_draw.clicked.connect(self.draw_mode_on)
        self.pushButton_draw.setText('Start drawing chain')
        self.pushButton_draw.setFont(QFont('Calibri', 12))
        layout.addWidget(self.pushButton_draw)

        self.pushButton_finish = QtWidgets.QPushButton(self)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_finish.clicked.connect(self.draw_mode_off)
        self.pushButton_finish.setText('Return to menu')
        self.pushButton_finish.setFont(QFont('Calibri', 12))
        layout.addWidget(self.pushButton_finish)

        # Image creating
        self.draw_widget = QtWidgets.QWidget(self)
        layout.addWidget(self.draw_widget)

        self.setLayout(layout)

    def paintEvent(self, e):
        if self.drawing_mode:
            painter = QPainter(self)
            painter.begin(self)
            if len(self.realization.vector_of_segments) != 1:
                for i in range(len(self.realization.vector_of_segments) - 1):
                    painter.drawLine(self.realization.vector_of_segments[i + 1][0],
                                     self.realization.vector_of_segments[i + 1][1],
                                     self.realization.vector_of_segments[i][0],
                                     self.realization.vector_of_segments[i][1])
                    painter.drawText(
                        (self.realization.vector_of_segments[i][0] + self.realization.vector_of_segments[i + 1][
                            0]) // 2,
                        (self.realization.vector_of_segments[i][1] + self.realization.vector_of_segments[i + 1][
                            1]) // 2,
                        alphabet[i])
                painter.drawLine(self.x, self.y, self.realization.vector_of_segments[-1][0],
                                 self.realization.vector_of_segments[-1][1])
                painter.drawText((self.x + self.realization.vector_of_segments[-1][0]) // 2,
                                 (self.y + self.realization.vector_of_segments[-1][1]) // 2,
                                 alphabet[len(self.realization.vector_of_segments) - 1])
            painter.end()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        self.update()

    def mousePressEvent(self, event):
        if self.drawing_mode:

            # If current vertex is too close to the first one, polygonal chain closes.
            if abs(self.realization.vector_of_segments[0][0] - event.x()) > 10 or abs(
                    self.realization.vector_of_segments[0][1] - event.y()) > 10:
                self.realization.add_vertex(self.x, self.y)
                self.x = event.x()
                self.y = event.y()
            else:
                self.x = self.realization.vector_of_segments[0][0]
                self.y = self.realization.vector_of_segments[0][1]
                self.drawing_mode = False
            self.update()

    def draw_mode_on(self):
        self.drawing_mode = True

    def draw_mode_off(self):
        self.drawing_mode = False
        self.close()
