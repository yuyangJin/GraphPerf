from line_info import LineInfo
from perf_data import *

class Node(object):
    def __init__(self,
                type_,
                id_,
                address_,
                line_info_,
                performance_data_
                ):
        self.id_ = id_
        self.type_ = type_
        self.address_ = address_
        self.line_info_ = line_info_
        self.performance_data_ = performance_data_


    def get_type(self):
        return self.type_
    
    def get_id(self):
        return self.id_



class SingleProcessNode(Node):
    def __init__(self,
                node,
                performance_data
                ):


class MultiProcessNode(Node):
    def __init__(self,
                node,
                performance_data
                ):
        