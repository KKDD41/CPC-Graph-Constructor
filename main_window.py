from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet
from drawing_window import DrawingWindow
from realization_dialog import RealizationDlg


class Window(QMainWindow):
    """
    Main window that provides general description of CPC-graphs and provides functions for working with them.
        -- create_chain (provides an instrument to build a polygonal chain)
        -- show_graph (creates a CPC-graph of current realization)
        -- show_realization (shows current chain realization)
        -- start_graph_analyzer (provides tools for working with arbitrary graph)
    """
    realization = Realization()

    def __init__(self):
        super(Window, self).__init__()
        self.drawing_window = DrawingWindow(myRealization=self.realization)
        self.setWindowTitle("CPC-Graphs constructor")
        self.resize(1000, 800)
        layout = QtWidgets.QGridLayout()

        # Creating description
        self.general_description = QtWidgets.QLabel()
        self.general_description.setText('There will be a text')
        self.general_description.resize(700, 600)
        layout.addWidget(self.general_description, 0, 0)

        # Creating buttons' widget and control buttons
        self.vertical_layout_widget = QtWidgets.QWidget()
        self.buttons_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.push_button_draw = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_draw.setText('Create chain')
        self.buttons_layout.addWidget(self.push_button_draw)

        self.push_button_graph = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_graph.setText('Show CPC-graph')
        self.buttons_layout.addWidget(self.push_button_graph)

        self.push_button_realization = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_realization.setText('Show realization')
        self.buttons_layout.addWidget(self.push_button_realization)

        self.push_button_analyze = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_analyze.setText('Graph analyzer')
        self.buttons_layout.addWidget(self.push_button_analyze)

        layout.addWidget(self.vertical_layout_widget, 0, 1)

        # Creating info widget
        self.info_text = QtWidgets.QLabel()
        self.info_text.setText('There will be an info')

        layout.addWidget(self.info_text, 1, 1)

        # Creating an example
        self.example_label = QtWidgets.QLabel()
        self.example_label.resize(300, 600)
        pixmap = QPixmap("graph.png")
        pixmap.scaled(self.example_label.sizeHint())
        self.example_label.setPixmap(pixmap)

        layout.addWidget(self.example_label, 1, 0)

        # Creating central widget
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(layout)

        self.setCentralWidget(self.central_widget)

        # Connecting buttons
        self.push_button_draw.clicked.connect(self.create_chain)
        self.push_button_graph.clicked.connect(self.show_graph)
        self.push_button_realization.clicked.connect(self.show_realization)
        self.push_button_analyze.clicked.connect(self.start_graph_analyzer)

        self.show()
        self.setMouseTracking(True)

    # Buttons events
    def create_chain(self):
        self.drawing_window.show()
        self.drawing_window.setMouseTracking(True)

    def show_graph(self):
        self.realization.create_graph()

        dlg = QDialog(self)
        dlg.setWindowTitle("CPC-Graph to current realization")
        dlg.resize(800, 600)

        labelImage = QLabel(dlg)
        pixmap = QPixmap("graph.png").scaled(dlg.width(), dlg.height())
        labelImage.setPixmap(pixmap)

        dlg.exec()

    def show_realization(self):
        dlg = RealizationDlg(self.realization)
        dlg.setWindowTitle("CPC-Graph to current realization")
        dlg.resize(800, 600)

        dlg.exec()

    def start_graph_analyzer(self):
        pass

    # useless features
    def read_chain(self):
        self.read_chain_flag = True
        string_with_coordinates = self.textEdit.toPlainText().split('\n')
        self.realization.vector_of_segments = list(
            tuple(map(int, string_with_coordinates[i].split())) for i in range(len(string_with_coordinates)))
        self.update()
