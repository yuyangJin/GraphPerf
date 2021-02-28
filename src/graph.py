import igraph
from igraph import *


class ProgramAbstractGraph(Graph):
    def BFS(self):
        pass
    def DFS(self):
        pass
    def get_node_by_id(self, id):
        print("11")
        pass
    def get_node_by_fn_name(self, fn_name):
        pass
    def graph_contraction(self, func):
        pass
    def merge_nodes(self, merged_node_list):
        pass
    def get_common_feature(self):
        pass

# class ProgramAbstractGraph(object):
#     def __init__(self, node_file, edge_file):
#         self.node_file = node_file
#         self.edge_file = edge_file
#         self.nodes_ = dict() '''< id, Node >'''
#         self.edges_= dict()  '''< src_id, dest_id >'''
#         self.set_nodes_from_file(self.node_file)
#         self.set_edges_from_file(self.edge_file)
    
#     '''read JSON file'''
#     def set_nodes_from_file(self, node_file):
#         pass
    
#     def set_edges_from_file(self, edge_file):
#         pass
    
#     def BFS(self):
#         pass
    
#     def DFS(self):
#         pass
#     def get_node_by_id(self, id):
#         pass
#     def get_node_by_fn_name(self, fn_name):
#         pass
#     def graph_contraction(self, func):
#         pass
#     def merge_nodes(self, node_list):
#         pass
#     def get_common_feature(self):
#         pass


g = ProgramAbstractGraph.Read_GraphML("test.GraphML")
g.write_dot("test.dot")