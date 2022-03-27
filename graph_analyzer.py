import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import networkx as nx
from numpy import gcd
import matplotlib.pyplot as plt


class GraphAnalyzerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dlg = QFileDialog()
        self.currentGraph = nx.Graph()
        self.setWindowTitle('Graph analyzer')

        self.file_name = ''
        self.result = ''
        self.resize(850, 800)

        # Flags
        self.DB_access = False
        self.upper_bound = False
        self.forbidden = False
        self.regular = False
        self.cycles = False
        self.paths = False
        self.complement = False

        layout = QtWidgets.QGridLayout()

        # Creating graph reader
        self.vertical_layout_widget_3 = QtWidgets.QWidget(self)
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.vertical_layout_widget_3)

        # Description
        self.vertical_layout_widget_4 = QtWidgets.QWidget(self)
        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self.vertical_layout_widget_4)
        self.vertical_layout_4.setAlignment(QtCore.Qt.AlignTop)

        self.l1 = QtWidgets.QLabel(self.vertical_layout_widget_4)
        self.l1.setText('Input Graph description:')
        self.l1.setFont(QFont('Times New Roman', 14))
        self.vertical_layout_4.addWidget(self.l1)

        self.description = QtWidgets.QLabel(self.vertical_layout_widget_4)
        self.description.setText('Your graph description must be an adjacency list (or dictionary). \n'
                                 'Input data can be entered in the text editor below, or you can upload \n'
                                 'a .txt or .json file. In the first two cases, the input data must be \n'
                                 'presented as strings, where the first value is the current vertex, and \n'
                                 'the ones following it are the list of vertices adjacent to it. Values \n'
                                 'in vertex names in a string are separated by a space. If the data is \n'
                                 'not correct, you will get an error.\n\n')
        self.description.setFont(QFont('Calibri', 12))
        self.vertical_layout_4.addWidget(self.description)

        self.l2 = QtWidgets.QLabel(self.vertical_layout_widget_4)
        self.l2.setText('Choose an appropriate format:')
        self.l2.setFont(QFont('Times New Roman', 14))
        self.vertical_layout_4.addWidget(self.l2)

        layout.addWidget(self.vertical_layout_widget_4, 0, 0)

        # Combo box
        self.combo = QtWidgets.QComboBox(self)
        self.options = ('.txt files', '.json files', 'input from text editor')
        self.combo.addItems(self.options)
        self.combo.setFont(QFont('Calibri', 12))
        layout.addWidget(self.combo, 1, 0)

        # Input Graph
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.resize(200, 800)
        self.text_edit.setText('Describe your graph here')
        layout.addWidget(self.text_edit, 2, 0)

        # Upload button
        self.push_button_file = QtWidgets.QPushButton(self)
        self.push_button_file.clicked.connect(self.load_file)
        self.push_button_file.setText('Upload file with graph description')
        self.push_button_file.setFont(QFont('Calibri', 12))
        layout.addWidget(self.push_button_file, 3, 0)

        # Combo box
        self.vertical_layout_widget = QtWidgets.QWidget()
        self.vertical_layout_widget.resize(400, 200)
        self.buttons_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QtWidgets.QLabel()
        self.label.setText('Analyze graph for belonging to a class CPC:')
        self.label.setFont(QFont('Times New Roman', 14))
        self.buttons_layout.addWidget(self.label)

        # Creating radio buttons
        self.DB_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.DB_button.setText('search in Database')
        self.DB_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.DB_button)

        self.edges_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.edges_button.setText('check upper bound for number of segments')
        self.edges_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.edges_button)

        self.subgraphs_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.subgraphs_button.setText('check forbidden subgraphs')
        self.subgraphs_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.subgraphs_button)

        self.regular_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.regular_button.setText('check bounds for regular graphs')
        self.regular_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.regular_button)

        self.cycle_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.cycle_button.setText('test for cycles')
        self.cycle_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.cycle_button)

        self.path_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.path_button.setText('test for paths')
        self.path_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.path_button)

        self.complement_button = QtWidgets.QCheckBox(self.vertical_layout_widget)
        self.complement_button.setText('hamiltonian cycle existing')
        self.complement_button.setFont(QFont('Calibri', 12))
        self.buttons_layout.addWidget(self.complement_button)

        layout.addWidget(self.vertical_layout_widget, 0, 1)

        # Getting result
        self.push_button_res = QtWidgets.QPushButton(self)
        self.push_button_res.setText('Get result')
        self.push_button_res.setFont(QFont('Calibri', 12))
        layout.addWidget(self.push_button_res, 1, 1)

        # Result editor
        self.text_edit_2 = QtWidgets.QTextEdit(self)
        self.text_edit_2.setText('There will be a result of graph processing')
        layout.addWidget(self.text_edit_2, 2, 1)

        # Creating result buttons
        self.horizontal_widget = QtWidgets.QWidget(self)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.horizontal_widget)

        self.show_graph = QtWidgets.QPushButton(self.horizontal_widget)
        self.show_graph.setText('Show graph')
        self.show_graph.setFont(QFont('Calibri', 12))
        self.horizontal_layout.addWidget(self.show_graph)

        self.show_realization = QtWidgets.QPushButton(self.horizontal_widget)
        self.show_realization.setText('Show realization')
        self.show_realization.setFont(QFont('Calibri', 12))
        self.horizontal_layout.addWidget(self.show_realization)

        layout.addWidget(self.horizontal_widget, 3, 1)

        # Connecting buttons
        self.push_button_res.clicked.connect(self.analyze)
        self.show_graph.clicked.connect(self.show_current_graph)

        self.setLayout(layout)

    # Constructing appropriate graph
    def show_current_graph(self):
        nx.draw(self.currentGraph, with_labels=True)
        plt.savefig("graph_analyzer.png")

        dlg = QDialog(self)
        dlg.setWindowTitle("CPC-Graph to current realization")
        dlg.resize(800, 600)

        labelImage = QLabel(dlg)
        pixmap = QPixmap("graph_analyzer.png").scaled(dlg.width(), dlg.height())
        labelImage.setPixmap(pixmap)

        dlg.exec()

    def load_file(self):
        current_option = self.options.index(self.combo.currentText())
        if current_option == '.txt files' or current_option == '.json files':
            self.file_name, _ = QFileDialog.getOpenFileName(parent=self,
                                                            caption="Choose file with graph description",
                                                            filter="Text Files (*.txt)",
                                                            directory=os.getcwd())
            text = open(self.file_name).read()
        else:
            text = self.text_edit.toPlainText()

        set_of_strings = list(text.split('\n'))
        for string in set_of_strings:
            items = list(string.split())
            self.currentGraph.add_node(items[0])
            for node in items[1:]:
                self.currentGraph.add_edge(items[0], node)

    def set_flags(self):
        if self.DB_button.isChecked():
            self.DB_access = True
        if self.edges_button.isChecked():
            self.upper_bound = True
        if self.subgraphs_button.isChecked():
            self.forbidden = True
        if self.regular_button.isChecked():
            self.regular = True
        if self.path_button.isChecked():
            self.paths = True
        if self.cycle_button.isChecked():
            self.cycles = True

    def analyze(self):
        self.set_flags()

        self.upper_bound_edges()
        self.hamilton()
        self.path()
        self.cycle()
        self.regular_check()

        self.text_edit_2.setText(self.result)
        self.update()

    # Functions for graph analyzer
    def upper_bound_edges(self):
        if self.upper_bound:
            n = self.currentGraph.number_of_nodes()
            e = self.currentGraph.number_of_edges()
            if n % 2 == 1:
                if e > (n - 3) * n / 2:
                    self.result += '''The upper bound on edges is not correct, 
                                      therefore current graph does not belong to CPC-graph. \n'''
                else:
                    self.result += 'Upper bound on edges is correct. \n'
            else:
                if e > n * (n - 4) / 2 + 1:
                    self.result += '''The upper bound on edges is not correct, 
                                                          therefore current graph does not belong to CPC-graph. \n'''
                else:
                    self.result += 'Upper bound on edges is correct. \n'

    def hamilton(self):
        if self.complement:
            G = nx.complement(self.currentGraph)
            F = [(G, [list(G.nodes())[0]])]
            n = G.number_of_nodes()
            while F:
                graph, path = F.pop()
                confs = []
                neighbors = (node for node in graph.neighbors(path[-1])
                             if node != path[-1])  # exclude self loops
                for neighbor in neighbors:
                    conf_p = path[:]
                    conf_p.append(neighbor)
                    conf_g = nx.Graph(graph)
                    conf_g.remove_node(path[-1])
                    confs.append((conf_g, conf_p))
                for g, p in confs:
                    if len(p) == n:
                        self.result += 'There exists a hamiltonian cycle in the complement. \n'
                    else:
                        F.append((g, p))
            self.result += '''There is no hamiltonian cycle in the complement, 
                              therefore current graph does not belong to the CPC-class. \n'''

    def path(self):
        if self.paths:
            if len(list(self.currentGraph.nodes())) != 0 and \
                    nx.is_simple_path(self.currentGraph, list(self.currentGraph.nodes())):
                print('haha')
                if len(list(self.currentGraph.nodes())) > 6:
                    self.result += f'''Current graph is a simple path with {len(list(self.currentGraph.nodes()))} nodes,
                                    therefore current graph belongs to CPC-class. \n'''
                else:
                    self.result += '''Number of nodes in current path graph is less than 7,
                                      therefore current graph does not belong to CPC. \n'''
            else:
                self.result += 'Graph is not a simple path. \n'

    def cycle(self):
        if self.cycles:
            if self.is_regular() == (True, 2):
                if self.currentGraph.number_of_nodes() > 4 and self.currentGraph.number_of_nodes() != 6:
                    self.result += f'''Current graph is a simple cycle with {self.currentGraph.number_of_nodes()} nodes,
                                    therefore current graph belongs to CPC-class. \n'''
                else:
                    self.result += f'''Number of nodes in current cycle graph is {self.currentGraph.number_of_nodes()},
                                      therefore current graph does not belong to CPC. \n'''
            else:
                self.result += 'Graph is not a simple cycle. \n'

    def is_regular(self):
        degrees = [val for (node, val) in nx.degree(self.currentGraph)]
        if nx.is_connected(self.currentGraph) and all(d == degrees[0] for d in degrees):
            return True, degrees[0]
        return False, -1

    def regular_check(self):
        if self.regular:
            reg, deg = self.is_regular()
            if reg:
                n = self.currentGraph.number_of_nodes()
                if (n % 2 == 1 and deg > n - 3) or (n % 4 == 0 and deg > n - 4) or (n % 2 == 0 and deg > n - 5):
                    self.result += '''Max degree for regular graph is not correct, 
                                      therefore the graph does not belong to CPC.'''
                    return
                if (deg % 2 == 0 and n >= deg * deg + 5 * deg + 7) or (
                        deg % 2 == 1 and n % 2 == 0 and n > 4 * (4 * deg * deg + 10 * deg + 7)) or (
                        (deg - 2) / 2 < n / 2 and gcd(n, (deg - 2) / 2) == 1) or (n % (4 * deg + 6) == 0):
                    self.result += 'Current graph is regular and belongs to CPC-class. \n'

    def database_call(self):
        pass
