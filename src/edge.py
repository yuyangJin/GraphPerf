class Edge:
    def __init__(self,
                edge_type,
                src_node_id,
                dest_node_id,
                performance_data
                ):
        self.type_ = edge_type
        self.src_node_id_ = src_node_id
        self.dest_node_id_ = dest_node_id
        self.performance_data_ = performance_data

class SingleProcessEdge(Edge):

class MultiProcessEdge(Edge):