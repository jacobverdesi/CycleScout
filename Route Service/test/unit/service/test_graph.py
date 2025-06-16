from service.graph import RouteGraph

def test_graph(resource_dir):

    graph = RouteGraph.from_kmz(resource_dir / "wandrer-30-03-25.kmz")
    assert graph.gdf is not None

    graph.to_nx()
    assert graph.G is not None

    graph.plot()
