import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"

"""
Class of CPC-graph realization that contains a CPC-graph and coordinates of corresponding polygonal chain.
It provides following methods:
    -- create_graph (initializing field 'graph' with CPC-graph of given polygonal chain)
    
"""


class Realization:
    vector_of_segments = []
    graph = nx.Graph()

    def __init__(self):
        pass

    def add_vertex(self, x, y):
        self.vector_of_segments.append((x, y))
        self.graph.add_node(alphabet[len(self.vector_of_segments) - 1])

    def create_graph(self):
        n = len(self.vector_of_segments)
        for i in range(n - 1):
            for j in range(i + 1, n):
                A = np.array([[self.vector_of_segments[i][1] - self.vector_of_segments[i + 1][1],
                               self.vector_of_segments[i + 1][0] - self.vector_of_segments[i][0]],
                              [self.vector_of_segments[j][1] - self.vector_of_segments[(j + 1) % n][1],
                               self.vector_of_segments[(j + 1) % n][0] - self.vector_of_segments[j][0]]])
                b = np.array([self.vector_of_segments[i + 1][0] * self.vector_of_segments[i][1] -
                              self.vector_of_segments[i][0] * self.vector_of_segments[i + 1][1],
                              self.vector_of_segments[(j + 1) % n][0] * self.vector_of_segments[j][1] -
                              self.vector_of_segments[j][0] * self.vector_of_segments[(j + 1) % n][1]])

                x = np.linalg.solve(A, b)[0]

                if (min(self.vector_of_segments[i][0], self.vector_of_segments[i + 1][0]) < x < max(
                        self.vector_of_segments[i][0], self.vector_of_segments[i + 1][0])) and (min(
                    self.vector_of_segments[j][0], self.vector_of_segments[(j + 1) % n][0]) < x < max(
                    self.vector_of_segments[j][0], self.vector_of_segments[(j + 1) % n][0])):
                    self.graph.add_edge(alphabet[i], alphabet[j])
        nx.draw(self.graph, with_labels=True)
        plt.savefig("graph.png")
