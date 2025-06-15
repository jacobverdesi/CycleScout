import shutil
import webbrowser
from zipfile import ZipFile

import folium
import networkx as nx
from geopandas import GeoDataFrame, GeoSeries
import momepy
import matplotlib.pyplot as plt


class RouteGraph:

    def __init__(self):
        self.G = None

    @classmethod
    def from_kmz(cls, kmz_file) -> None:
        with ZipFile(kmz_file, 'r') as kmz:
            first_file = kmz.namelist()[0]
            kmz.extract(first_file, 'tmp')
            raw_gdf = GeoDataFrame.from_file(f"tmp/{first_file}", driver='KML')
            raw_gdf.geometry.set_crs(epsg=4326, inplace=True)
            raw_gdf['geometry'] = raw_gdf.geometry.to_crs(epsg=3857)  # convert to web mercator
            # split multi-linestrings into separate rows
            cls.gdf = raw_gdf.explode()
            # remove the temporary folder

            shutil.rmtree("tmp")

    def to_nx(self):
        self.gdf.geometry = momepy.close_gaps(self.gdf.geometry, tolerance=0.0001)
        # remove geometries with less than 2 points
        self.gdf = self.gdf[self.gdf.geometry.apply(lambda x: len(x.coords) > 1)]
        # remove geometries with no length
        self.gdf = self.gdf[self.gdf.geometry.length > 0]
        # self.gdf.geometry = momepy.remove_false_nodes(self.gdf.geometry)
        self.G = momepy.gdf_to_nx(self.gdf,length="length")
        self.G = momepy.consolidate_intersections(self.G, tolerance=1)
        return

    def plot(self):
        m = self.gdf.explore(
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

        auto_open('map.html')

    def __repr__(self):
        return f'{self.gdf.head()}'


def main():
    import os
    cwd = os.getcwd()
    print(cwd)
    graph = RouteGraph()

    graph.from_kmz("../../test/resources/wandrer-30-03-25.kmz")
    graph.to_nx()

    graph.plot()


if __name__ == '__main__':
    main()
