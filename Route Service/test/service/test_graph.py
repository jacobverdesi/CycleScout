from service.graph import RouteGraph


def test_graph():

    graph = RouteGraph()
    graph.from_kmz("resources/wandrer-30-03-25.kmz")
    graph.to_nx()
    assert graph.G is not None
    assert graph.gdf is not None

    graph.plot()
