import time

import networkx as nx
import numpy as np
import pandas as pd
import sqlalchemy as sa

from src.ORtools import VRPsolver

# import cvxpy as cp

engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')


class KCPPsolver:

    def __init__(self):
        self.edge_list = None
        self.G = None
        self.G_prime = None
        self.solution = {}
    @classmethod
    def build_graph(cls):
        kcpp_solver = cls()
        kcpp_solver.import_edge_list()
        kcpp_solver.G = nx.from_pandas_edgelist(kcpp_solver.edge_list, 'source', 'target', ['weight'])


        return kcpp_solver
    @classmethod
    def build_from_generator(cls, generator):
        kcpp_solver = cls()
        kcpp_solver.G = generator
        return kcpp_solver

    def import_edge_list(self):
        with engine.connect() as conn:
            query = "SELECT * FROM road_network_edges"
            df = pd.read_sql(query, conn)
            # split rows with one_way not equal to yes into two rows
            not_one_way_df = df[df['one_way'] != 'yes']
            not_one_way_df = not_one_way_df.rename(columns={'source': 'target', 'target': 'source'})
            df = pd.concat([df, not_one_way_df])
            self.edge_list = df.rename(columns={'length': 'weight'})

    def save_routes_to_postgresql(self,paths):
        with engine.connect() as conn:
            for path in paths:
                #Converte path ids into linestring
                  path_df = pd.DataFrame(path, columns=['source', 'target'])



    def distance_matrix(self):
        all_pairs_path_length = dict(nx.all_pairs_dijkstra_path_length(self.G))
        nodes = list(sorted(self.G.nodes()))
        matrix = np.full((max(nodes), max(nodes)), int(10e10))
        for source_node in nodes:
            for target_node in nodes:
                if target_node in all_pairs_path_length[source_node]:
                    matrix[source_node-1, target_node-1] = all_pairs_path_length[source_node][target_node]
        #round to integer
        matrix = np.round(matrix).astype(int)
        print(matrix.max(),matrix.min())
        return matrix
    def __repr__(self):
        return f'Graph with {self.G.number_of_nodes()} nodes and {self.G.number_of_edges()} edges'

kcpp_solver = KCPPsolver.build_from_generator(nx.fast_gnp_random_graph(100,0.1,seed=1))
print(kcpp_solver)
print(kcpp_solver.distance_matrix())
#start time and end time
start_time = time.time()

vrp_solver = VRPsolver(kcpp_solver.distance_matrix(),0,10,2500)
vrp_solver.solve()
vrp_solver.print_solution()
print("--- %s seconds ---" % (time.time() - start_time))
# paths=kcpp_solver.k_cpp(2)
# kcpp_solver.save_routes_to_postgresql(paths)