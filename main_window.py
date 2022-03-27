from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CPC_realization import Realization, alphabet
from drawing_window import DrawingWindow
from graph_analyzer import GraphAnalyzerWindow
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

    def __init__(self, storage):
        super(Window, self).__init__()
        self.storage = storage
        self.dlg = RealizationDlg(self.realization, self.storage)
        self.analyzer = GraphAnalyzerWindow()
        self.drawing_window = DrawingWindow(myRealization=self.realization)
        self.setWindowTitle("CPC-Graphs constructor")
        self.resize(850, 800)
        layout = QtWidgets.QGridLayout()
        layout.setColumnStretch(0, 2)

        # Creating description
        self.general_description = QtWidgets.QLabel()
        self.general_description.setText('In the paper such subclass of string\ngraphs as intersection graphs of \n '
                                         'closed polygonal chains (class of \nCPC-graphs) was considered, \n'
                                         'necessary conditions for belonging\nto that class, forbidden subgraphs and \n'
                                         'operations with graphs which preserve\nbelonging to the CPC class were \n'
                                         'found. Considered question about the\nexistence of k-regular CPC-graphs, \n'
                                         'particularly, pairs (n, k) such that\nthere exists k-regular CPC-graph on n\n'
                                         'vertexes were found, proved that there\nare infinitely many k-regular \n'
                                         'CPC-graphs for any integer positive k, \nestimations for the number of k, '
                                         'such \n that '
                                         'k-regular graph on n  vertexes exists,\nnwere given. Algorithmic questions in'
                                         '\n '
                                         'the class of CPC-graphs were investigated.\nIt was proved that independent \n'
                                         'and dominating set problems, coloring\nproblem and the problem about \n'
                                         'maximal cycle are NP-hard in the class \nof CPC-graphs, and problem of \n'
                                         'recognition of the CPC-graphs belongs to \nthe PSPACE '
                                         'class.\n')
        self.general_description.setFont(QFont('Calibri', 13))
        self.general_description.resize(600, 400)
        layout.addWidget(self.general_description, 0, 0)

        # Creating buttons' widget and control buttons
        self.vertical_layout_widget = QtWidgets.QWidget()
        self.vertical_layout_widget.resize(400, 400)
        self.buttons_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QtWidgets.QLabel(self.vertical_layout_widget)
        self.label.setText('Context menu:')
        self.label.setFont(QFont('Times New Roman', 14))
        self.buttons_layout.addWidget(self.label)

        self.push_button_draw = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_draw.setText('Create chain')
        self.push_button_draw.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.push_button_draw)

        self.push_button_graph = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_graph.setText('Show CPC-graph')
        self.push_button_graph.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.push_button_graph)

        self.push_button_realization = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_realization.setText('Show realization')
        self.push_button_realization.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.push_button_realization)

        self.push_button_analyze = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.push_button_analyze.setText('Graph analyzer')
        self.push_button_analyze.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.push_button_analyze)

        layout.addWidget(self.vertical_layout_widget, 1, 0)

        # Creating info widget
        self.vert_widget = QtWidgets.QWidget()
        self.vert_layout = QtWidgets.QVBoxLayout(self.vert_widget)

        self.info_text = QtWidgets.QLabel(self.vert_widget)
        self.info_text.setFont(QFont('Times New Roman', 14))
        self.info_text.setText('Additional information:')
        self.vert_layout.addWidget(self.info_text)

        link_template = '<a href=https://github.com/KKDD41>Follow me on GitHub.</a>'
        self.link_github = HyperlinkLabel(self)
        self.link_github.setText(' ->  ' + link_template)
        self.vert_layout.addWidget(self.link_github)

        link_template = '<a href=https://www.linkedin.com/in/ekaterina-dul-226026234>Follow me on LinkedIn.</a>'
        self.link_in = HyperlinkLabel(self)
        self.link_in.setText(' ->  ' + link_template)
        self.vert_layout.addWidget(self.link_in)

        link_template = '<a href=https://drive.google.com/file/d/16LvuB0hO8Hi6mIvwill_IP68iQ14vH-L/view>Link to presentation \n   and main results.</a>'
        self.link_pres = HyperlinkLabel(self)
        self.link_pres.setText(' ->  ' + link_template)
        self.vert_layout.addWidget(self.link_pres)

        link_template = '<a href=https://drive.google.com/file/d/1OsHT6fjUOUUevcp-QlTW9MMLD9yrzHqg/view>Link to full article.</a>'
        self.link_article = HyperlinkLabel(self)
        self.link_article.setText(' ->  ' + link_template)
        self.vert_layout.addWidget(self.link_article)

        link_template = '<a href=https://Google.com>Link to the database.</a>'
        self.link_db = HyperlinkLabel(self)
        self.link_db.setText(' ->  ' + link_template)
        self.vert_layout.addWidget(self.link_db)

        self.vert_layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.vert_widget, 1, 1)

        # Creating an example
        self.another_vertical_vidget = QtWidgets.QWidget()
        self.another_vertical_layout = QtWidgets.QVBoxLayout(self.another_vertical_vidget)

        self.label_title = QtWidgets.QLabel(self.another_vertical_vidget)
        self.label_title.setText('Example of CPC-Graph:')
        self.setFont(QFont('Times New Roman', 14))
        self.another_vertical_layout.addWidget(self.label_title)

        self.example_label = QtWidgets.QLabel(self.another_vertical_vidget)
        self.example_label.resize(600, 400)
        pixmap = QPixmap("example.png")
        pixmap.scaled(self.example_label.width(), self.example_label.height())
        self.example_label.setPixmap(pixmap)
        self.another_vertical_layout.addWidget(self.example_label)
        self.another_vertical_layout.setAlignment(Qt.AlignTop)

        layout.addWidget(self.another_vertical_vidget, 0, 1)

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
        self.dlg.setWindowTitle("CPC-Graph to current realization")
        self.dlg.resize(800, 600)

        self.dlg.show()

    def start_graph_analyzer(self):
        self.analyzer.show()


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setFont(QFont('Calibri', 12))
        self.setOpenExternalLinks(True)
        self.setParent(parent)
