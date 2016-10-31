# -*- coding: utf-8 -*-

class DAG(object):

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = set()

    def add_edge(self, n1, n2):

        if n1 in self.graph:
            self.graph[n1].add(n2) 

    def from_dict(self, dict_data):

        for key, value in dict_data.iteritems():
            self.graph[key] = set(value)

    def reset_graph(self):
        self.graph = {}

    def ind_nodes(self, graph=None):
        # 어떤 set에도 속하지 않은 Key를 리턴
        union_set = set()
        for value in self.graph.values():
            union_set = union_set.union(value)

        return list(set(self.graph.keys()).difference(union_set))
