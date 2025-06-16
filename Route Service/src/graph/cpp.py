import itertools

from networkx import Graph,dijkstra_path_length


def find_odd_degree_nodes(graph: Graph):
    """
    Find nodes with an odd degree in the graph.

    :param graph: A dictionary representing the graph where keys are node IDs and values are lists of connected node IDs.
    :return: A list of node IDs that have an odd degree.
    """
    odd_degree_nodes = [v for v, d in graph.degree() if d % 2 != 0]
    return odd_degree_nodes


def compute_pairs(node_list):
    """
    Compute all pairs of nodes from a list.

    :param node_list: A list of node IDs.
    :return: A list of tuples representing all pairs of nodes.
    """
    if len(node_list) > 10000:
        raise ValueError("Node list is too large to compute pairs. Please reduce the size of the node list.")
    node_pairs = list(itertools.combinations(node_list, 2))
    return node_pairs


def get_shortest_path_distances(graph: Graph, pairs,weight):
    """
    Get the shortest path distances for a list of node pairs in the graph.

    :param graph: A NetworkX Graph object.
    :param pairs: A list of tuples representing node pairs.
    :param weight: The edge attribute to use as weight (default is 'weight').
    :return: A dictionary with node pairs as keys and their shortest path distances as values.
    """
    """Compute shortest distance between each pair of nodes in a graph.  Return a dictionary keyed on node pairs (tuples)."""
    distances = {}
    for pair in pairs:
        distances[pair] = dijkstra_path_length(graph, pair[0], pair[1], weight=weight)
    return distances

def create_complete_graph(pair_weights):
    """
    Create a complete graph from a dictionary of node pairs and their weights.
    """
    g = Graph()
    for k,v in pair_weights.items():
        g.add_edge(k[0], k[1], weight=v)

    return g