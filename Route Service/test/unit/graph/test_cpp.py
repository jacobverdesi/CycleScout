import pytest
from networkx import Graph
from contextlib import nullcontext as does_not_raise

from graph.cpp import find_odd_degree_nodes, get_shortest_path_distances, compute_pairs, create_complete_graph
from graph.graph_vis import plot_nx


@pytest.mark.parametrize("t_id, graph, expected", [
    (1, Graph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]), []),  # Circle
    (2, Graph([(1, 2), (2, 3), (3, 4), (4, 5)]), [1, 5]),
    (3, Graph([(1, 2), (2, 3)]), [1, 3]),
    (4, Graph([]), []),
])
def test_odd_degree_nodes(t_id: int, graph: Graph, expected: list):
    """
    Test the find_odd_degree_nodes function with a given graph and expected output.

    :param graph: A NetworkX Graph object.
    :param expected: A list of expected odd degree nodes.
    """
    result = find_odd_degree_nodes(graph)
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("node_list, expected_pairs, exception", [
    ([1, 2, 3], [(1, 2), (1, 3), (2, 3)], None),  # Simple case with 3 nodes
    ([1, 2], [(1, 2)], None),  # Simple case with 2 nodes
    ([1], [], None),  # Single node, no pairs
    ([], [], None),  # Empty list, no pairs
    ([i for i in range(10)], None, None),  # Small list of 10 nodes
    ([i for i in range(100)], None, None),  # Medium list of 100 nodes
    ([i for i in range(1000)], None, None),  # Larger list of 1000 nodes
    ([i for i in range(10000)], None, None),  # Large list of 10,000 nodes
    ([i for i in range(10001)], None, ValueError),  # This will raise ValueError in compute_pairs
])
def test_node_pairs(node_list, expected_pairs, exception):
    pytest_exception = does_not_raise() if exception is None or not isinstance(exception, type) else pytest.raises(exception)
    with pytest_exception:
        result = compute_pairs(node_list)
        if expected_pairs is not None:
            assert sorted(result) == sorted(expected_pairs), f"Expected {expected_pairs}, but got {result}"
        # assert len result is n choices 2
        from math import comb
        assert len(result) == comb(len(node_list), 2), f"Expected {comb(len(node_list), 2)} pairs, but got {len(result)}"



def test_shortest_path_distances():
    g = Graph([(1, 2, {'weight': 1}), (2, 3, {'weight': 2}), (3, 4, {'weight': 1}), (4, 5, {'weight': 3})])
    pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
    expected_distances = {(1, 2): 1, (2, 3): 2, (3, 4): 1, (4, 5): 3}

    result = get_shortest_path_distances(g, pairs, 'weight')
    assert result == expected_distances


def test_create_complete_graph(graph: Graph):
    pairs =

    pair_weights = get_shortest_path_distances(graph, pairs, 'weight')
    g = create_complete_graph(pair_weights)

    assert isinstance(g, Graph)
    assert g.number_of_nodes() == 5
    assert g.number_of_edges() == len(pair_weights)

    for edge in pair_weights:
        assert g.has_edge(edge[0], edge[1])
        assert g[edge[0]][edge[1]]['weight'] == pair_weights[edge]

    plot_nx(g)
