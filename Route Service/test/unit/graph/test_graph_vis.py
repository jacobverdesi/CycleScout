from networkx import random_internet_as_graph, Graph

from graph.graph_vis import plot_nx


def test_graph_vis(graph:Graph):
    plot_nx(graph)