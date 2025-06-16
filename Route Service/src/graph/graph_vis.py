import webbrowser

import folium
from geopandas import GeoDataFrame
from networkx import Graph, random_internet_as_graph


def plot_gdf(gdf:GeoDataFrame):
    m = gdf.explore(
        column='Name',
        cmap='tab20',
        categorical=True,
        legend=True,
        legend_kwds={'bbox_to_anchor': (1, 1)},
        figsize=(15, 15)
    )
    # positions = {n: [n[0], n[1]] for n in list(self.G.nodes)}
    # f, ax = plt.subplots(1, 2, figsize=(15, 15))
    # self.gdf.plot(color="k", ax=ax[0])
    # for i, facet in enumerate(ax):
    #     facet.set_title(("Rivers", "Graph")[i])
    #     facet.axis("off")
    # nx.draw(self.G, positions, ax=ax[1], node_size=10, node_color="r", edge_color="b")
    folium.TileLayer('cartodbpositron').add_to(m)

    def auto_open(path):
        html_page = f'{path}'
        m.save(html_page)
        # open in browser.
        new = 2
        webbrowser.open(html_page, new=new)

    auto_open('../service/map.html')

def plot_nx(g: Graph,seed=42):
    import matplotlib.pyplot as plt
    import networkx as nx

    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(g, seed=seed)  # positions for all nodes
    # if edge has 'color' attribute, use it for edge color
    edge_colors = [g[u][v].get('color', 'black') for u, v in g.edges()]
    # if edge has 'weight' attribute, use it for edge width
    edge_widths = [g[u][v].get('weight', 1) for u, v in g.edges()]
    # normalize edge widths to a range suitable for visualization
    edge_widths = [width / max(edge_widths) * 5 for width in edge_widths]  # Scale to a range of 0 to 2
    nx.draw(g, pos, with_labels=True, node_size=50, font_size=8, edge_color=edge_colors,width=edge_widths)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g, 'weight'), font_color='red', font_size=8)
    plt.title("NetworkX Graph Visualization")
    plt.show()

