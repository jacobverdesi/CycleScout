import pytest
from pathlib import Path

from networkx import random_internet_as_graph, Graph


@pytest.fixture(scope='session')
def resource_dir():
    """Fixture to provide the resource directory path."""
    return Path(__file__).parent.parent / 'resources'


@pytest.fixture(scope='session')
def graph() -> Graph:
    g = random_internet_as_graph(10, seed=42)
    for edge in g.edges():
        g.edges[edge]['color'] = 'green' if edge[0] % 2 == 0 else 'orange'

    return g