from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet


class DrawingWindow(QWidget):
    def __init__(self, myRealization):
        super().__init__()

        # Class fields
        self.x = 200
        self.y = 200
        self.drawing_mode = False
        self.realization = myRealization

        # Window params
        self.resize(800, 600)
        self.setWindowTitle("Draw here your closed polygonal chain")

        # Layout creating
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout_widget = QtWidgets.QWidget(self.central_widget)
        self.vertical_layout_widget.setGeometry(QtCore.QRect(0, 0, 800, 60))
        self.vertical_layout_widget.setObjectName("vertical_layout_widget")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 0, 500, 500))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.vertical_layout_widget.setAutoFillBackground(True)

        # Buttons creating
        self.pushButton_draw = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_draw.clicked.connect(self.draw_mode_on)
        self.pushButton_draw.setText('Start drawing chain')
        self.vertical_layout.addWidget(self.pushButton_draw)

        self.pushButton_finish = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_finish.clicked.connect(self.draw_mode_off)
        self.pushButton_finish.setText('Return to menu')
        self.vertical_layout.addWidget(self.pushButton_finish)

    def paintEvent(self, e):
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

    def mousePressEvent(self, event: QMouseEvent):
        if self.drawing_mode:
            self.realization.add_vertex(self.x, self.y)

            # If current vertex is too close to the first one, polygonal chain closes.
            if abs(self.realization.vector_of_segments[0][0] - event.x()) > 10 or abs(
                    self.realization.vector_of_segments[0][1] - event.y()) > 10:
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
        self.close()
